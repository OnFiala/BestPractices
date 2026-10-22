"""A bounded agent proposal loop with two independent, durable SQLite ledgers.

Only data crosses the fixture model boundary. The trusted Python caller owns run
creation, fixture administration, and human-authority construction. This module is
not a sandbox for arbitrary Python code or a production identity system.
"""

import hashlib
import json
import math
import secrets
import sqlite3
import time
import uuid
from contextlib import contextmanager
from pathlib import Path

MAX_PROPOSAL_BYTES = 2048
MAX_CONTEXT_BYTES = 4096
MODEL_UNITS = 2
TOOL_UNITS = 3
TARGETS = {
    ("tenant-a", "review-ticket"): "synthetic:tenant-a:ticket-1",
    ("tenant-a", "review-other"): "synthetic:tenant-a:ticket-2",
    ("tenant-b", "review-ticket"): "synthetic:tenant-b:ticket-1",
}
TERMINAL = {"completed", "rejected", "denied", "cancelled", "expired", "budget_exhausted", "failed"}
UNCERTAIN = {"dispatched", "unresolved"}


class PolicyError(ValueError):
    """A stable reason code, safe to include in the audit log."""


class SimulatedCrash(RuntimeError):
    """Injected interruption after the dispatch reservation is durable."""


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def digest(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def action(value="reviewed", target="synthetic:tenant-a:ticket-1", tool="set_flag"):
    return {"version": 1, "tool": tool, "target": target, "arguments": {"value": value}}


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise PolicyError("duplicate_json_key")
        result[key] = value
    return result


def validate_proposal(raw, tenant, task):
    """Deterministic policy, invoked both on model output and at execution."""
    if not isinstance(raw, str):
        raise PolicyError("proposal_size")
    try:
        if len(raw.encode("utf-8")) > MAX_PROPOSAL_BYTES:
            raise PolicyError("proposal_size")
    except UnicodeEncodeError:
        raise PolicyError("proposal_encoding") from None
    try:
        value = json.loads(raw, object_pairs_hook=_unique_object)
    except (json.JSONDecodeError, RecursionError):
        raise PolicyError("proposal_json") from None
    if not isinstance(value, dict) or set(value) != {"version", "tool", "target", "arguments"}:
        raise PolicyError("proposal_schema")
    if type(value["version"]) is not int or value["version"] != 1:
        raise PolicyError("proposal_version")
    if value["tool"] != "set_flag":
        raise PolicyError("tool_not_allowed")
    if value["target"] != TARGETS.get((tenant, task)):
        raise PolicyError("target_out_of_scope")
    args = value["arguments"]
    if not isinstance(args, dict) or set(args) != {"value"}:
        raise PolicyError("argument_schema")
    if not isinstance(args["value"], str) or args["value"] not in {"reviewed", "held"}:
        raise PolicyError("argument_value")
    return canonical(value)


def connect(path):
    db = sqlite3.connect(path, isolation_level=None, timeout=5)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys = ON")
    db.execute("PRAGMA synchronous = FULL")
    return db


@contextmanager
def transaction(db):
    db.execute("BEGIN IMMEDIATE")
    try:
        yield
    except BaseException:
        db.rollback()
        raise
    else:
        db.commit()


class FixtureModel:
    """Scripted output, not an LLM. Can deliberately obey a document injection.

    Context capture is a test oracle. A real model adapter would need its own
    evaluation, privacy controls, cancellation, transport deadlines and cost cap.
    """

    def __init__(self, output=None, follow_document_proposal=False):
        self.output = canonical(action()) if output is None else output
        self.follow_document_proposal = follow_document_proposal
        self.seen_context = []

    def propose(self, context):
        self.seen_context.append(tuple(context))
        if self.follow_document_proposal:
            for document in context:
                if "PROPOSAL:" in document:
                    return document.split("PROPOSAL:", 1)[1]
        return self.output


class EffectFixture:
    """Independent provider ledger: operation receipt and effect commit together."""

    def __init__(self, path):
        self.db = connect(path)
        self.db.executescript("""
            CREATE TABLE IF NOT EXISTS receipts (
                operation TEXT PRIMARY KEY, tenant TEXT NOT NULL, task TEXT NOT NULL,
                action_digest TEXT NOT NULL, receipt TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS effects (
                operation TEXT PRIMARY KEY REFERENCES receipts(operation),
                target TEXT NOT NULL, value TEXT NOT NULL);
        """)

    def apply(self, operation, tenant, task, proposal):
        # Defense in depth: even this synthetic tool cannot select files/URLs.
        approved = validate_proposal(proposal, tenant, task)
        fingerprint = digest(approved)
        with transaction(self.db):
            prior = self.lookup(operation)
            if prior:
                if (prior["tenant"], prior["task"], prior["action_digest"]) != (
                    tenant, task, fingerprint
                ):
                    raise PolicyError("idempotency_conflict")
                return prior["receipt"]
            receipt = "fixture-receipt:" + digest(operation)
            self.db.execute("INSERT INTO receipts VALUES (?, ?, ?, ?, ?)",
                            (operation, tenant, task, fingerprint, receipt))
            parsed = json.loads(approved)
            self.db.execute("INSERT INTO effects VALUES (?, ?, ?)",
                            (operation, parsed["target"], parsed["arguments"]["value"]))
        return receipt

    def lookup(self, operation):
        row = self.db.execute("SELECT * FROM receipts WHERE operation = ?", (operation,)).fetchone()
        return dict(row) if row else None

    def count(self):
        return self.db.execute("SELECT count(*) FROM effects").fetchone()[0]

    def close(self):
        self.db.close()


class Workflow:
    def __init__(self, root, clock=time.time):
        # Root is a trusted embedding configuration, never model/CLI input.
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self.clock = clock
        self.db = connect(self.root / "workflow.sqlite")
        self.provider = EffectFixture(self.root / "provider.sqlite")
        self.db.executescript("""
            CREATE TABLE IF NOT EXISTS grants (
                tenant TEXT NOT NULL, task TEXT NOT NULL, active INTEGER NOT NULL,
                PRIMARY KEY (tenant, task));
            CREATE TABLE IF NOT EXISTS documents (
                id TEXT PRIMARY KEY, tenant TEXT NOT NULL, task TEXT NOT NULL, body TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS runs (
                id TEXT PRIMARY KEY, tenant TEXT NOT NULL, task TEXT NOT NULL,
                state TEXT NOT NULL, reason TEXT NOT NULL, revision INTEGER NOT NULL DEFAULT 0,
                proposal TEXT, action_digest TEXT, deadline REAL NOT NULL,
                max_model_calls INTEGER NOT NULL, max_tool_calls INTEGER NOT NULL,
                max_units INTEGER NOT NULL, model_calls INTEGER NOT NULL DEFAULT 0,
                tool_calls INTEGER NOT NULL DEFAULT 0, units INTEGER NOT NULL DEFAULT 0,
                cancel_requested INTEGER NOT NULL DEFAULT 0,
                operation TEXT NOT NULL UNIQUE, receipt TEXT);
            CREATE TABLE IF NOT EXISTS approvals (
                token_hash TEXT PRIMARY KEY, run_id TEXT NOT NULL REFERENCES runs(id),
                tenant TEXT NOT NULL, task TEXT NOT NULL, revision INTEGER NOT NULL,
                action_digest TEXT NOT NULL, expires REAL NOT NULL,
                actor TEXT NOT NULL, revoked INTEGER NOT NULL DEFAULT 0,
                consumed INTEGER NOT NULL DEFAULT 0);
            CREATE TABLE IF NOT EXISTS events (
                seq INTEGER PRIMARY KEY, run_id TEXT NOT NULL REFERENCES runs(id),
                phase TEXT NOT NULL, decision TEXT NOT NULL, reason TEXT NOT NULL);
        """)

    def seed_fixtures(self):
        """Trusted fixture administration; never exposed as an agent tool."""
        with transaction(self.db):
            self.db.executemany("INSERT OR IGNORE INTO grants VALUES (?, ?, 1)", TARGETS)
            self.db.executemany("INSERT OR IGNORE INTO documents VALUES (?, ?, ?, ?)", [
                ("a-ticket", "tenant-a", "review-ticket", "Synthetic ticket is ready for review."),
                ("a-other", "tenant-a", "review-other", "OTHER_TASK_MARKER"),
                ("b-ticket", "tenant-b", "review-ticket", "OTHER_TENANT_MARKER"),
            ])

    def create_run(self, tenant="tenant-a", task="review-ticket", *, ttl=60,
                   max_model_calls=2, max_tool_calls=1, max_units=7):
        if (tenant, task) not in TARGETS:
            raise PolicyError("unknown_scope")
        if not isinstance(ttl, (int, float)) or not math.isfinite(ttl) or not 0 < ttl <= 3600:
            raise ValueError("ttl must be finite and within (0, 3600]")
        for cap in (max_model_calls, max_tool_calls, max_units):
            if type(cap) is not int or not 0 <= cap <= 100:
                raise ValueError("caps must be integers within [0, 100]")
        run_id = str(uuid.uuid4())
        operation = digest(canonical([tenant, task, run_id]))
        with transaction(self.db):
            self.db.execute("""INSERT INTO runs
                (id, tenant, task, state, reason, deadline, max_model_calls,
                 max_tool_calls, max_units, operation)
                VALUES (?, ?, ?, 'created', 'created', ?, ?, ?, ?, ?)""",
                            (run_id, tenant, task, self.clock() + ttl,
                             max_model_calls, max_tool_calls, max_units, operation))
            self._event(run_id, "run", "created", "trusted_task_scope")
        return run_id

    def _run(self, run_id):
        row = self.db.execute("SELECT * FROM runs WHERE id = ?", (run_id,)).fetchone()
        if row is None:
            raise KeyError("unknown run")
        return dict(row)

    def _event(self, run_id, phase, decision, reason):
        self.db.execute("INSERT INTO events (run_id, phase, decision, reason) VALUES (?, ?, ?, ?)",
                        (run_id, phase, decision, reason))

    def _state(self, run_id, state, reason, phase="policy"):
        self.db.execute("UPDATE runs SET state = ?, reason = ? WHERE id = ?", (state, reason, run_id))
        self._event(run_id, phase, state, reason)

    def _active(self, run):
        grant = self.db.execute("SELECT active FROM grants WHERE tenant = ? AND task = ?",
                                (run["tenant"], run["task"])).fetchone()
        return grant is not None and grant[0] == 1

    def _preflight(self, run):
        if run["cancel_requested"]:
            self._state(run["id"], "cancelled", "cancellation_requested")
        elif self.clock() >= run["deadline"]:
            self._state(run["id"], "expired", "deadline_exceeded")
        elif not self._active(run):
            self._state(run["id"], "denied", "scope_revoked")
        else:
            return True
        return False

    def _reserve(self, run, phase, units):
        counter = "model_calls" if phase == "model" else "tool_calls"
        maximum = "max_" + counter
        if run[counter] >= run[maximum] or run["units"] + units > run["max_units"]:
            reason = "call_limit" if run[counter] >= run[maximum] else "synthetic_budget"
            self._state(run["id"], "budget_exhausted", reason, phase)
            return False
        # Column name comes exclusively from the two constants above.
        self.db.execute(f"UPDATE runs SET {counter} = {counter} + 1, units = units + ? WHERE id = ?",
                        (units, run["id"]))
        self._event(run["id"], phase, "reserved", "budget_reserved")
        return True

    def propose(self, run_id, model, document_ids=("a-ticket",)):
        if (not isinstance(document_ids, (tuple, list)) or len(document_ids) > 4
                or any(not isinstance(x, str) or len(x) > 80 for x in document_ids)):
            raise PolicyError("retrieval_request_bounds")
        with transaction(self.db):
            run = self._run(run_id)
            if run["state"] not in {"created", "awaiting_approval", "approved"}:
                return self.snapshot(run_id)
            if not self._preflight(run):
                return self.snapshot(run_id)
            context = []
            for doc_id in dict.fromkeys(document_ids):
                # Authorization predicates are part of retrieval, before the model call.
                row = self.db.execute("""SELECT body FROM documents
                    WHERE id = ? AND tenant = ? AND task = ?""",
                                      (doc_id, run["tenant"], run["task"])).fetchone()
                if row:
                    context.append(row[0])
                self._event(run_id, "retrieval", "allowed" if row else "denied",
                            "task_tenant_filter")
            if sum(len(x.encode("utf-8")) for x in context) > MAX_CONTEXT_BYTES:
                self._state(run_id, "rejected", "context_size", "retrieval")
                return self.snapshot(run_id)
            if not self._reserve(run, "model", MODEL_UNITS):
                return self.snapshot(run_id)
            self._state(run_id, "model_pending", "model_reserved", "model")
        # The fixture only receives strings; no ledger, authority, or credentials.
        try:
            raw = model.propose(tuple(context))
            proposal = validate_proposal(raw, run["tenant"], run["task"])
        except PolicyError as exc:
            with transaction(self.db):
                if self._run(run_id)["state"] == "model_pending":
                    self._state(run_id, "rejected", str(exc))
            return self.snapshot(run_id)
        except Exception:
            with transaction(self.db):
                if self._run(run_id)["state"] == "model_pending":
                    self._state(run_id, "failed", "model_failure", "model")
            return self.snapshot(run_id)
        with transaction(self.db):
            current = self._run(run_id)
            if current["state"] != "model_pending" or not self._preflight(current):
                return self.snapshot(run_id)
            self.db.execute("""UPDATE runs SET proposal = ?, action_digest = ?,
                revision = revision + 1 WHERE id = ?""", (proposal, digest(proposal), run_id))
            self._state(run_id, "awaiting_approval", "proposal_validated")
        return self.snapshot(run_id)

    def execute(self, run_id, capability=None, *, crash_at=None):
        if crash_at not in {None, "before_effect", "after_effect"}:
            raise ValueError("unknown crash point")
        with transaction(self.db):
            run = self._run(run_id)
            if run["state"] in UNCERTAIN:
                uncertain = True
            elif run["state"] in TERMINAL or run["state"] == "model_pending":
                return self.snapshot(run_id)
            else:
                uncertain = False
                if not self._preflight(run):
                    return self.snapshot(run_id)
                if run["proposal"] is None:
                    self._state(run_id, "rejected", "proposal_missing")
                    return self.snapshot(run_id)
                try:
                    proposal = validate_proposal(run["proposal"], run["tenant"], run["task"])
                    if digest(proposal) != run["action_digest"]:
                        raise PolicyError("proposal_digest_mismatch")
                except PolicyError as exc:
                    self._state(run_id, "rejected", str(exc), "executor")
                    return self.snapshot(run_id)
                approval = None
                if isinstance(capability, str) and len(capability) <= 128:
                    approval = self.db.execute("SELECT * FROM approvals WHERE token_hash = ?",
                                               (digest(capability),)).fetchone()
                reason = self._approval_error(run, approval)
                if reason:
                    self._state(run_id, "awaiting_approval", reason, "approval")
                    return self.snapshot(run_id)
                if not self._reserve(run, "tool", TOOL_UNITS):
                    return self.snapshot(run_id)
                self.db.execute("UPDATE approvals SET consumed = 1 WHERE token_hash = ?",
                                (digest(capability),))
                self._state(run_id, "dispatched", "dispatch_reserved", "executor")
        if uncertain:
            return self.reconcile(run_id)
        # Reservation/consumption commits BEFORE the independent provider transaction.
        if crash_at == "before_effect":
            raise SimulatedCrash("dispatch committed; effect not sent")
        receipt = self.provider.apply(run["operation"], run["tenant"], run["task"], proposal)
        if crash_at == "after_effect":
            raise SimulatedCrash("provider committed; acknowledgement lost")
        with transaction(self.db):
            self.db.execute("UPDATE runs SET receipt = ? WHERE id = ?", (receipt, run_id))
            self._state(run_id, "completed", "effect_acknowledged", "executor")
        return self.snapshot(run_id)

    def _approval_error(self, run, approval):
        if approval is None:
            return "approval_missing"
        if approval["revoked"]:
            return "approval_revoked"
        if approval["consumed"]:
            return "approval_consumed"
        if self.clock() >= approval["expires"]:
            return "approval_expired"
        for name in ("tenant", "task", "revision", "action_digest"):
            if approval[name] != run[name]:
                return "approval_mismatch"
        if approval["run_id"] != run["id"]:
            return "approval_mismatch"
        return None

    def reconcile(self, run_id):
        with transaction(self.db):
            run = self._run(run_id)
            if run["state"] not in UNCERTAIN:
                return self.snapshot(run_id)
            # Read-only lookup works after cancellation/revocation/expiry: it cannot
            # initiate an effect and is essential to account for work already sent.
            receipt = self.provider.lookup(run["operation"])
            if receipt is None:
                self._state(run_id, "unresolved", "provider_outcome_unknown", "reconciliation")
            elif (receipt["tenant"], receipt["task"], receipt["action_digest"]) != (
                run["tenant"], run["task"], run["action_digest"]
            ):
                self._state(run_id, "unresolved", "provider_receipt_mismatch", "reconciliation")
            else:
                self.db.execute("UPDATE runs SET receipt = ? WHERE id = ?",
                                (receipt["receipt"], run_id))
                self._state(run_id, "completed", "effect_reconciled", "reconciliation")
        return self.snapshot(run_id)

    def cancel(self, run_id):
        with transaction(self.db):
            run = self._run(run_id)
            if run["state"] not in TERMINAL:
                self.db.execute("UPDATE runs SET cancel_requested = 1 WHERE id = ?", (run_id,))
                if run["state"] in UNCERTAIN:
                    self._event(run_id, "cancellation", "pending", "reconciliation_required")
                else:
                    self._state(run_id, "cancelled", "cancellation_requested", "cancellation")
        return self.snapshot(run_id)

    def snapshot(self, run_id):
        run = self._run(run_id)
        # Neither bearer capabilities nor source/model content appear in reports.
        fields = ("state", "reason", "revision", "model_calls", "tool_calls", "units",
                  "max_units", "cancel_requested", "receipt")
        result = {key: run[key] for key in fields}
        result.update({"run_id": run_id, "action_digest": run["action_digest"],
                       "operation": run["operation"], "tenant": run["tenant"], "task": run["task"]})
        result["events"] = [dict(row) for row in self.db.execute(
            "SELECT phase, decision, reason FROM events WHERE run_id = ? ORDER BY seq", (run_id,))]
        return result

    def close(self):
        self.provider.close()
        self.db.close()


class FixtureHumanAuthority:
    """Trusted local test driver, never a tool supplied to FixtureModel.

    Constructing this object represents the human-side boundary in the example.
    Its actor string is explicitly NOT verified production human identity.
    """

    def __init__(self, workflow):
        self.workflow = workflow

    def approve(self, run_id, *, ttl=30):
        workflow = self.workflow
        if not isinstance(ttl, (int, float)) or not math.isfinite(ttl) or not 0 < ttl <= 300:
            raise ValueError("approval ttl must be finite and within (0, 300]")
        capability = secrets.token_urlsafe(32)
        with transaction(workflow.db):
            run = workflow._run(run_id)
            if run["state"] not in {"awaiting_approval", "approved"}:
                raise PolicyError("approval_state")
            if not workflow._preflight(run):
                return None
            workflow.db.execute("""INSERT INTO approvals
                (token_hash, run_id, tenant, task, revision, action_digest, expires, actor)
                VALUES (?, ?, ?, ?, ?, ?, ?, 'fixture-human')""",
                                (digest(capability), run_id, run["tenant"], run["task"],
                                 run["revision"], run["action_digest"],
                                 min(workflow.clock() + ttl, run["deadline"])))
            workflow._state(run_id, "approved", "fixture_human_approved", "approval")
        return capability

    def deny(self, run_id):
        workflow = self.workflow
        with transaction(workflow.db):
            run = workflow._run(run_id)
            if run["state"] in UNCERTAIN or run["state"] in TERMINAL:
                raise PolicyError("denial_too_late")
            workflow.db.execute("UPDATE approvals SET revoked = 1 WHERE run_id = ?", (run_id,))
            workflow._state(run_id, "denied", "fixture_human_denied", "approval")

    def revoke(self, capability):
        with transaction(self.workflow.db):
            row = self.workflow.db.execute("SELECT run_id FROM approvals WHERE token_hash = ?",
                                           (digest(capability),)).fetchone()
            if row:
                self.workflow.db.execute("UPDATE approvals SET revoked = 1 WHERE token_hash = ?",
                                         (digest(capability),))
                self.workflow._event(row[0], "approval", "revoked", "fixture_human_revoked")

    def revoke_scope(self, tenant, task):
        with transaction(self.workflow.db):
            self.workflow.db.execute("UPDATE grants SET active = 0 WHERE tenant = ? AND task = ?",
                                     (tenant, task))
