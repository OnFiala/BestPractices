"""Deterministic delivery planning and consistency checks on submitted evidence.

No commands, networks, artifact paths, or identity providers are invoked. A matching
hash identifies a submitted assertion; it does not authenticate its contents.
"""

import argparse
import hashlib
import json
import math
import re
import sys
import unicodedata
from datetime import datetime
from pathlib import Path

from .content import ROOT

MAX_INPUT_BYTES = 262_144
MAX_ERRORS = 64
MAX_GATES = 48
PROJECT_TYPES = (
    "public-website", "saas", "internal-tool", "ai-application",
    "agent-automation", "mobile-backend",
)
STAGES = (
    "intent", "requirements", "design", "security", "implementation",
    "verification", "release", "operation", "incident", "evolution", "retirement",
)
ENUMS = {
    "project_type": PROJECT_TYPES,
    "risk": ("low", "moderate", "high", "critical"),
    "data_sensitivity": ("public", "internal", "confidential", "restricted"),
    "workload": ("small", "variable", "high", "unmeasured"),
    "hosting": ("local", "managed", "self-hosted", "hybrid"),
    "surfaces": ("api", "browser", "mobile", "worker", "cli"),
    "external_side_effects": (
        "payments", "messaging", "publishing", "third-party-writes", "infrastructure",
    ),
}
PROFILE_REQUIRED = {"schema_version", "project_id", "revision", *ENUMS}
PROFILE_OPTIONAL = {"description", "objectives", "constraints"}
SHA256 = re.compile(r"[a-f0-9]{64}\Z")
REVISION = re.compile(r"(?:[a-f0-9]{40}|[a-f0-9]{64})\Z")
IDENTIFIER = re.compile(r"[a-z][a-z0-9-]{0,63}\Z")
AUTHORITY = {
    "verified": False,
    "required": True,
    "reason": "Human decisions must be checked in their trusted external system; JSON is not approval.",
}
LIMITATIONS = [
    "Submitted observations, artifact digests and identity labels are unverified assertions.",
    "Distinct labels do not establish independent people, credentials or independent empirical evidence.",
    "Freshness is relative to the supplied as_of timestamp, not an authenticated clock.",
    "No test, agent, command, artifact retrieval, merge, deployment or approval is executed.",
]


def _bounded(value):
    """Reject oversized, cyclic, deeply nested and non-JSON objects before encoding."""
    pending = [(value, 0)]
    nodes = 0
    characters = 0
    while pending:
        item, depth = pending.pop()
        nodes += 1
        if nodes > 12_000 or depth > 12:
            return False
        if isinstance(item, str):
            if len(item) > 4096:
                return False
            characters += len(item)
        elif type(item) is dict:
            if len(item) > 64 or any(not isinstance(k, str) or len(k) > 80 for k in item):
                return False
            characters += sum(len(k) for k in item)
            pending.extend((v, depth + 1) for v in item.values())
        elif type(item) is list:
            if len(item) > 256:
                return False
            pending.extend((v, depth + 1) for v in item)
        elif item is None or type(item) is bool:
            pass
        elif type(item) is int:
            if abs(item) > 10**15:
                return False
        elif type(item) is float:
            if not math.isfinite(item):
                return False
        else:
            return False
        if characters > MAX_INPUT_BYTES:
            return False
    return len(json.dumps(value, ensure_ascii=True).encode("utf-8")) <= MAX_INPUT_BYTES


def _text(value, maximum=500):
    return (isinstance(value, str) and bool(value.strip()) and len(value) <= maximum
            and not any(unicodedata.category(c).startswith("C") for c in value))


def _identifier(value):
    return isinstance(value, str) and bool(IDENTIFIER.fullmatch(value))


def _strings(value, maximum=16):
    return (type(value) is list and len(value) <= maximum
            and all(_text(item) for item in value) and len(value) == len(set(value)))


def _digest(value):
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def _identity(value):
    return " ".join(unicodedata.normalize("NFKC", value).casefold().split())


def _timestamp(value):
    if not isinstance(value, str) or len(value) > 40:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None and parsed.utcoffset() is not None else None


def validate_profile(profile):
    """Return {valid, errors}; validate only data, with no filesystem access."""
    if not _bounded(profile) or type(profile) is not dict:
        return {"valid": False, "errors": ["Profile must be a bounded JSON object."]}
    errors = []
    if set(profile) - PROFILE_REQUIRED - PROFILE_OPTIONAL:
        errors.append("Profile contains unknown fields.")
    for key in sorted(PROFILE_REQUIRED - set(profile)):
        errors.append(f"Profile is missing {key}.")
    if type(profile.get("schema_version")) is not int or profile.get("schema_version") != 1:
        errors.append("Profile schema_version must be 1.")
    if not _identifier(profile.get("project_id")):
        errors.append("project_id must be a lowercase identifier of at most 64 characters.")
    if not isinstance(profile.get("revision"), str) or not REVISION.fullmatch(profile["revision"]):
        errors.append("revision must be an immutable lowercase 40 or 64 character hex identity.")
    for key, choices in ENUMS.items():
        value = profile.get(key)
        if key in ("surfaces", "external_side_effects"):
            if (not _strings(value) or any(v not in choices for v in value)
                    or (key == "surfaces" and not value)):
                errors.append(f"{key} must contain distinct supported values.")
        elif not isinstance(value, str) or value not in choices:
            errors.append(f"Unsupported {key}.")
    if "description" in profile and not _text(profile["description"], 1000):
        errors.append("description must be a nonempty string of at most 1000 characters.")
    for key in ("objectives", "constraints"):
        if key in profile and (not _strings(profile[key]) or not profile[key]):
            errors.append(f"{key} must contain 1 to 16 distinct nonempty strings.")
    return {"valid": not errors, "errors": errors[:MAX_ERRORS]}


def _load_json(path):
    # Only fixed registry names or explicitly requested CLI inputs reach this function.
    if not path.is_file():
        raise ValueError("JSON input must be a regular file.")
    with path.open("rb") as stream:
        raw = stream.read(MAX_INPUT_BYTES + 1)
    if len(raw) > MAX_INPUT_BYTES:
        raise ValueError("JSON file exceeds the input bound.")

    def unique_object(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("Duplicate JSON object keys are not accepted.")
            result[key] = value
        return result

    try:
        data = json.loads(raw, object_pairs_hook=unique_object)
    except (UnicodeDecodeError, RecursionError) as exc:
        raise ValueError("Invalid JSON encoding or nesting.") from exc
    if not _bounded(data):
        raise ValueError("JSON input exceeds structural bounds or contains nonfinite values.")
    return data


def _registry(root, name):
    base = Path(root).resolve()
    path = (base / "data" / name).resolve()
    if not path.is_relative_to(base):
        raise ValueError("Registry path escapes the supplied library root.")
    return _load_json(path)


def _configuration(root):
    config = _registry(root, "delivery.json")
    catalog = _registry(root, "catalog.json")
    blueprints = _registry(root, "blueprints.json")
    if (type(config) is not dict or config.get("schema_version") != 1
            or config.get("stage_order") != list(STAGES)):
        raise ValueError("Invalid delivery schema or stage order.")
    for key in ("evidence_max_age_days", "high_risk_evidence_max_age_days"):
        if type(config.get(key)) is not int or not 1 <= config[key] <= 365:
            raise ValueError("Invalid evidence age policy.")
    guides = {g["id"]: g["revision"] for g in catalog["guides"]}
    profiles = {p["id"]: p for p in blueprints["profiles"]}
    if (len(guides) != len(catalog["guides"])
            or len(profiles) != len(blueprints["profiles"])
            or set(profiles) != set(PROJECT_TYPES)):
        raise ValueError("Catalog and blueprints must have unique, supported IDs.")
    gates = config.get("gates")
    if type(gates) is not list or not 1 <= len(gates) <= MAX_GATES:
        raise ValueError("Delivery configuration must contain 1 to 48 gates.")
    by_id = {}
    fields = {"id", "stage", "producer_role", "reviewer_role", "artifacts", "prerequisites",
              "guides", "blocking_conditions", "release_required", "reason", "when"}
    for gate in gates:
        if type(gate) is not dict or set(gate) != fields:
            raise ValueError("Invalid delivery gate fields.")
        if not _identifier(gate["id"]) or gate["id"] in by_id:
            raise ValueError("Invalid or duplicate gate ID.")
        by_id[gate["id"]] = gate
        if gate["stage"] not in STAGES or not _text(gate["reason"]):
            raise ValueError("Invalid gate stage or reason.")
        if (not _identifier(gate["producer_role"]) or not _identifier(gate["reviewer_role"])
                or gate["producer_role"] == gate["reviewer_role"]):
            raise ValueError("Gate roles must be distinct identifiers.")
        for field in ("artifacts", "prerequisites", "guides", "blocking_conditions"):
            if not _strings(gate[field]) or (field != "prerequisites" and not gate[field]):
                raise ValueError("Invalid gate list.")
        if any(not _identifier(x) for x in gate["artifacts"] + gate["prerequisites"]):
            raise ValueError("Artifact and prerequisite IDs must be identifiers.")
        if any(g not in guides for g in gate["guides"]):
            raise ValueError("Gate references an unknown guide.")
        expected_release = STAGES.index(gate["stage"]) <= STAGES.index("release")
        if type(gate["release_required"]) is not bool or gate["release_required"] != expected_release:
            raise ValueError("Gate release scope does not match its stage.")
        if type(gate["when"]) is not dict:
            raise ValueError("Gate selector must be an object.")
        for key, choices in gate["when"].items():
            if (key not in ENUMS or not _strings(choices) or not choices
                    or any(choice not in ENUMS[key] for choice in choices)):
                raise ValueError("Invalid gate selector.")
    for gate in gates:
        for prerequisite in gate["prerequisites"]:
            if prerequisite not in by_id:
                raise ValueError("Unknown gate prerequisite.")
            if STAGES.index(by_id[prerequisite]["stage"]) > STAGES.index(gate["stage"]):
                raise ValueError("A prerequisite cannot occur in a later lifecycle stage.")
    if {g["stage"] for g in gates} != set(STAGES):
        raise ValueError("Every lifecycle stage must have a configured gate.")
    _ordered(gates)  # Reject cycles even when the affected selector is not active.
    return config, guides, profiles


def _ordered(gates):
    remaining = {g["id"]: g for g in gates}
    result = []
    resolved = set()
    while remaining:
        ready = [g for g in remaining.values() if set(g["prerequisites"]) <= resolved]
        if not ready:
            raise ValueError("Gate dependencies contain a cycle or missing prerequisite.")
        ready.sort(key=lambda g: (STAGES.index(g["stage"]), g["id"]))
        gate = ready[0]
        result.append(gate)
        resolved.add(gate["id"])
        del remaining[gate["id"]]
    return result


def _effective_profile(profile):
    # Blueprint assumptions cannot be removed by declaring an empty surface/effect list.
    result = json.loads(json.dumps(profile))
    implied = {
        "public-website": {"surfaces": ["browser"], "external_side_effects": ["publishing"]},
        "saas": {"surfaces": ["api", "worker"], "external_side_effects": ["payments"]},
        "internal-tool": {"surfaces": ["api"], "external_side_effects": ["third-party-writes"]},
        "ai-application": {"surfaces": ["api"]},
        "agent-automation": {"surfaces": ["worker"], "external_side_effects": ["third-party-writes"]},
        "mobile-backend": {"surfaces": ["api", "mobile"]},
    }
    for field in ("surfaces", "external_side_effects"):
        result[field] = sorted(set(profile[field]) | set(implied[profile["project_type"]].get(field, [])))
    return result


def _selected(gate, profile):
    return all(bool(set(profile[key] if type(profile[key]) is list else [profile[key]])
                    & set(choices)) for key, choices in gate["when"].items())


def _invalid(errors):
    return {"schema_version": 1, "valid": False, "errors": errors[:MAX_ERRORS],
            "advisory": True, "production_ready": False, "ready_for_human_review": False,
            "human_authorization": dict(AUTHORITY)}


def plan_project(profile, root=ROOT):
    """Build a bounded lifecycle DAG; input errors are JSON, not raised exceptions."""
    validation = validate_profile(profile)
    if not validation["valid"]:
        return _invalid(validation["errors"])
    try:
        config, guides, blueprints = _configuration(root)
        effective = _effective_profile(profile)
        selected = [g for g in config["gates"] if _selected(g, effective)]
        if {g["stage"] for g in selected} != set(STAGES):
            raise ValueError("Every lifecycle stage must have an active gate.")
        # Every active security/design condition becomes an implementation prerequisite;
        # every active verification condition becomes a release prerequisite.
        gates = json.loads(json.dumps(selected))
        implementation = next(g for g in gates if g["id"] == "implementation-packet")
        implementation["prerequisites"] = sorted(set(implementation["prerequisites"]) | {
            g["id"] for g in gates if g["stage"] in ("design", "security")
        })
        release = next(g for g in gates if g["id"] == "release-candidate")
        release["prerequisites"] = sorted(set(release["prerequisites"]) | {
            g["id"] for g in gates if g["stage"] == "verification"
        })
        gates = _ordered(gates)
        max_age = config["high_risk_evidence_max_age_days"] if effective["risk"] in (
            "high", "critical") else config["evidence_max_age_days"]
        for gate in gates:
            gate["max_evidence_age_days"] = max_age
            gate["selection"] = gate.pop("when")
            gate["guide_revisions"] = {g: guides[g] for g in gate["guides"]}
        blueprint = blueprints[profile["project_type"]]
        if any(g not in guides for g in blueprint["guides"]):
            raise ValueError("Blueprint references an unknown guide.")
        result = {
            "schema_version": 1, "valid": True, "errors": [], "advisory": True,
            "production_ready": False, "ready_for_human_review": False,
            "authorship": "agent-authored-policy", "project_id": profile["project_id"],
            "project_revision": profile["revision"], "profile_digest": _digest(profile),
            "effective_profile": effective, "stage_order": list(STAGES), "gates": gates,
            "blueprint": blueprint, "human_authorization": dict(AUTHORITY),
            "human_decisions": ["objectives", "architecture", "budget", "residual-risk",
                                "merge", "production-release", "destructive-retirement"],
            "limitations": list(LIMITATIONS),
        }
        result["plan_digest"] = _digest(result)
        return result
    except (OSError, ValueError, TypeError, KeyError, StopIteration) as exc:
        # Configuration content is trusted input, but errors should not expose local paths.
        detail = str(exc) if isinstance(exc, ValueError) else "Missing or malformed library registry."
        return _invalid([f"Delivery configuration error: {detail[:300]}"])


def _evidence_shape(evidence, plan):
    errors = []
    required = {"schema_version", "project_id", "project_revision", "profile_digest",
                "plan_digest", "as_of", "records"}
    optional = {"example", "notes", "human_approval"}
    if not _bounded(evidence) or type(evidence) is not dict:
        return ["Evidence must be a bounded JSON object."]
    if not required <= set(evidence) or set(evidence) - required - optional:
        return ["Evidence envelope has missing or unknown fields."]
    if type(evidence["schema_version"]) is not int or evidence["schema_version"] != 1:
        errors.append("Evidence schema_version must be 1.")
    for key in ("project_id", "project_revision", "profile_digest", "plan_digest"):
        if evidence[key] != plan[key]:
            errors.append(f"Evidence {key} does not match the current plan.")
    if _timestamp(evidence["as_of"]) is None:
        errors.append("Evidence as_of must be a timezone-aware ISO 8601 timestamp.")
    if "example" in evidence and type(evidence["example"]) is not bool:
        errors.append("Evidence example must be a boolean when supplied.")
    if "notes" in evidence and not _text(evidence["notes"], 1000):
        errors.append("Evidence notes must be a nonempty bounded string.")
    records = evidence["records"]
    if type(records) is not list or len(records) > MAX_GATES:
        return errors + ["Evidence records must contain at most 48 entries."]
    seen = set()
    gate_ids = {g["id"] for g in plan["gates"]}
    fields = {"gate_id", "status", "project_revision", "producer", "reviewer", "review_status",
              "artifacts", "observations"}
    for index, record in enumerate(records):
        location = f"Record {index + 1}"
        if type(record) is not dict or set(record) != fields:
            errors.append(f"{location} has missing or unknown fields.")
            continue
        gate_id = record["gate_id"]
        if not isinstance(gate_id, str) or gate_id not in gate_ids:
            errors.append(f"{location} references an unknown or inactive gate.")
        elif gate_id in seen:
            errors.append(f"{location} duplicates a gate; keep one authoritative current record.")
        else:
            seen.add(gate_id)
        if record["status"] not in ("passed", "failed", "skipped", "unrun"):
            errors.append(f"{location} has an unsupported status.")
        if record["review_status"] not in ("accepted", "changes-requested", "unreviewed"):
            errors.append(f"{location} has an unsupported review_status.")
        if not _text(record["producer"], 100) or not _text(record["reviewer"], 100):
            errors.append(f"{location} requires producer and reviewer identity labels.")
        if not _strings([record["project_revision"]]):
            errors.append(f"{location} requires a revision string.")
        for key in ("artifacts", "observations"):
            if type(record[key]) is not list or len(record[key]) > 16:
                errors.append(f"{location} {key} must contain at most 16 entries.")
    return errors[:MAX_ERRORS]


def _record_issues(record, gate, plan, as_of, identities, observation_ids):
    issues = []
    if record["status"] != "passed":
        issues.append(f"Recorded status is {record['status']}.")
    if record["project_revision"] != plan["project_revision"]:
        issues.append("Record is for a different project revision.")
    if _identity(record["producer"]) == _identity(record["reviewer"]):
        issues.append("Producer and reviewer labels identify self-review.")
    if record["review_status"] != "accepted":
        issues.append("Review is not recorded as accepted.")
    artifacts = {}
    artifact_fields = {"id", "sha256", "revision"}
    for artifact in record["artifacts"]:
        if type(artifact) is not dict or set(artifact) != artifact_fields:
            issues.append("Artifact requires id, sha256 and revision.")
            continue
        artifact_id, digest = artifact["id"], artifact["sha256"]
        if not _identifier(artifact_id) or artifact_id not in gate["artifacts"]:
            issues.append("Artifact ID is unknown for this gate.")
            continue
        if artifact_id in artifacts:
            issues.append("Duplicate artifact ID within this gate.")
        if not isinstance(digest, str) or not SHA256.fullmatch(digest):
            issues.append("Artifact requires a lowercase SHA-256 identity.")
            continue
        if artifact["revision"] != plan["project_revision"]:
            issues.append("Artifact is for a different project revision.")
        identity = (digest, artifact["revision"])
        if artifact_id in identities and identities[artifact_id] != identity:
            issues.append("The same artifact ID has conflicting identities.")
        identities[artifact_id] = identity
        artifacts[artifact_id] = digest
    if set(artifacts) != set(gate["artifacts"]):
        issues.append("Required artifact identities are missing.")
    covered = set()
    observation_fields = {"id", "artifact_id", "artifact_sha256", "observed_at", "environment",
                          "method", "expected", "actual", "outcome"}
    for observation in record["observations"]:
        if type(observation) is not dict or set(observation) != observation_fields:
            issues.append("Observation has missing or unknown fields.")
            continue
        if not _identifier(observation["id"]) or observation["id"] in observation_ids:
            issues.append("Observation IDs must be distinct across the evidence packet.")
        else:
            observation_ids.add(observation["id"])
        artifact_id = observation["artifact_id"]
        if (not isinstance(artifact_id, str) or artifact_id not in artifacts
                or observation["artifact_sha256"] != artifacts.get(artifact_id)):
            issues.append("Observation is not bound to a required artifact identity.")
        else:
            covered.add(artifact_id)
        for key in ("environment", "method", "expected", "actual"):
            if not _text(observation[key], 1000):
                issues.append(f"Observation {key} must describe an actual bounded observation.")
        observed_at = _timestamp(observation["observed_at"])
        if observed_at is None:
            issues.append("Observation time must be a timezone-aware ISO 8601 timestamp.")
        elif observed_at > as_of:
            issues.append("Observation time is after the supplied assessment time.")
        elif (as_of - observed_at).total_seconds() > gate["max_evidence_age_days"] * 86400:
            issues.append("Observation is older than the selected evidence age limit.")
        if observation["outcome"] != "passed":
            issues.append("An observation is failed, skipped, unrun or has an unsupported outcome.")
    if covered != set(gate["artifacts"]):
        issues.append("Every required artifact needs an identity-bound observed result.")
    return list(dict.fromkeys(issues))[:MAX_ERRORS]


def assess_project(profile, evidence, root=ROOT):
    """Check current recorded evidence; never establish real execution or authority."""
    plan = plan_project(profile, root)
    if not plan["valid"]:
        return plan
    errors = _evidence_shape(evidence, plan)
    if errors:
        return _invalid(errors)
    records = {record["gate_id"]: record for record in evidence["records"]}
    results = []
    supported = set()
    identities = {}
    observation_ids = set()
    as_of = _timestamp(evidence["as_of"])
    for gate in plan["gates"]:
        record = records.get(gate["id"])
        issues = (["No evidence record was supplied."] if record is None else
                  _record_issues(record, gate, plan, as_of, identities, observation_ids))
        if evidence.get("example") is True:
            issues.append("Illustrative example evidence cannot support project readiness.")
        unmet = sorted(set(gate["prerequisites"]) - supported)
        if unmet:
            issues.append("Prerequisite evidence is not supported.")
        if not issues:
            supported.add(gate["id"])
        results.append({
            "gate_id": gate["id"], "stage": gate["stage"],
            "status": "supported-by-recorded-evidence" if not issues else "blocked",
            "recorded_status": record["status"] if record else "missing",
            "release_required": gate["release_required"],
            "issues": issues, "unmet_prerequisites": unmet,
        })
    release_blockers = [r["gate_id"] for r in results if r["release_required"] and r["issues"]]
    return {
        "schema_version": 1, "valid": True, "errors": [], "advisory": True,
        "project_id": plan["project_id"], "project_revision": plan["project_revision"],
        "profile_digest": plan["profile_digest"], "plan_digest": plan["plan_digest"],
        "as_of": evidence["as_of"], "gate_results": results,
        "release_blockers": release_blockers, "ready_for_human_review": not release_blockers,
        "production_ready": False, "human_authorization": dict(AUTHORITY),
        "human_approval_claim_present": "human_approval" in evidence,
        "summary": {"required_for_release": sum(g["release_required"] for g in plan["gates"]),
                    "supported": len(supported), "blocked": len(results) - len(supported)},
        "limitations": list(LIMITATIONS),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    plan_parser = commands.add_parser("plan", help="Print a deterministic proposed lifecycle plan.")
    plan_parser.add_argument("--profile", type=Path, required=True)
    assess_parser = commands.add_parser("assess", help="Assess consistency of recorded evidence.")
    assess_parser.add_argument("--profile", type=Path, required=True)
    assess_parser.add_argument("--evidence", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        profile = _load_json(args.profile)
        result = (plan_project(profile) if args.command == "plan" else
                  assess_project(profile, _load_json(args.evidence)))
    except (OSError, ValueError):
        result = _invalid(["Cannot read a bounded valid JSON input from the requested file."])
    json.dump(result, sys.stdout, indent=2, ensure_ascii=True, allow_nan=False)
    sys.stdout.write("\n")
    # 0 means a valid plan or a complete recorded-evidence packet, never authorization.
    if not result["valid"]:
        return 2
    if args.command == "assess" and not result["ready_for_human_review"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
