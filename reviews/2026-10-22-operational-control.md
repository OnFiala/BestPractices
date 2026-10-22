# Independent operational control review

Date: 2026-10-22. Read-only repository review in `/workspace/BestPractices`.
Initial base: `34aca583b2a7366f17138bb2c4a5d1ddfbb6bfbf`.
This is manual engineering/security control, not a formal Codex Security scan,
human approval, legal clearance, or production certification.

## Initial scope and integration risks

The proposed scope is an advisory delivery planner/evidence assessor, local
reference service, fixture-based agent workflow, browser behavior fixture, six
project playbooks, and a systematic coverage registry. It can create a useful
operational reference kit. It does not establish autonomous delivery of arbitrary
software, production capacity, or comprehensive lifecycle coverage.

1. A documented and executed vertical journey must join profile selection,
   roles/tasks/dependencies, reference checks, exact artifact/revision-bound
   evidence, and release/operate/retire decisions. Independent examples alone do
   not constitute integrated lifecycle operation.
2. Caller-supplied role, result and approval JSON is an assertion. Matching
   digests establish consistency of referenced bytes, not authenticated reviewer
   identity, test execution, result truth, or authority to release.
3. Local SQLite/TCP and deterministic model/provider fixtures establish only
   exercised local invariants and policy boundaries. They do not establish live
   model safety, distributed durability, provider effect semantics, or capacity.
4. Consequential guidance additions require matching four-locale meaning and
   revisions, precise source mappings, and the same original-writing/license
   distinctions as existing content. Source counts and structural parity are
   insufficient substitutes for source applicability or meaning review.

## Review plan

- Inspect planner schemas, digest/revision bindings, dependency ordering,
  duplicate/failed/stale/missing evidence, self-review and role semantics.
- Inspect service tenant boundary, idempotency collision scope, version conflicts,
  transaction/outbox recovery, HTTP error/input paths, and restore evidence.
- Inspect workflow ACL before context, cancellation and budget enforcement,
  exact-action capabilities, crash ambiguity and reconciliation, and fixture limits.
- Inspect frontend stale response/cancel/error behavior and actual browser evidence.
- Compare new claims with coverage/source records, CI commands, translations and
  truthful final scope; record concrete actionable defects as files arrive.

## Checks so far

- Read `AGENTS.md`, `README.md`, `AGENT_SYSTEM.md`, `PROVENANCE.md`, catalog,
  lifecycle/agents/examples guides, blueprints and prior review.
- Confirmed clean initial worktree at the base above.
- Formal Codex Security scan/preflight tools were not exposed by tool discovery.
- Managed environment was running; no credentials/capabilities were reported.
  Network policy state was `unknown`; no network assurance inferred.

## Concrete findings

### C1 — Medium: skipped suites reported as passed (remediated)

`library/verification.py:129–134,150` classifies a suite solely from process exit
status. A unittest suite containing one required but skipped test exits 0 and
produces `status: passed` and `all_selected_passed: true`. Reproduced with
`run_suites(['delivery'], isolated_tmp_root)` and a synthetic
`tests/test_delivery.py` containing `@unittest.skip('required dependency
unavailable')`. This contradicts the requirement to distinguish failed, skipped
and unrun checks and can falsely label a scaffold's unavailable checks as passed.
Use observed test totals/skips/failures and reject skipped required checks. Also
check the Python 3.12 zero-discovery case (the system interpreter already returned
nonzero for zero tests). Report runtime/dependency versions separately from source
file digests. Sent to coordinator promptly. The implementation now uses a structured
unittest runner and rejects empty/skipped/expected-failure suites. Its four verifier
tests passed independently, including the skipped/empty negative cases.

### C2 — Medium: malformed configuration could omit lifecycle work (remediated)

The initial `library/delivery.py` built blueprint IDs into a dict without checking
the original list length and did not require a gate in every lifecycle stage.
Isolated registry copies with a duplicate blueprint or removed retirement stage
both produced `valid: true`. The author added unique-ID and configured/active-stage
coverage checks; the 19-test delivery suite passed independently afterward.

### C3 — Medium: portable packet omitted referenced guides (remediated)

The initial `library/project.py:29–32,66–85` copied catalog/plan/README content but
omitted `docs/` and local skills. Generated AGENTS and example README files pointed
to unavailable guides; content retrieval could not resolve the copied catalog.
The coordinator was asked to copy original guidance/skills or produce precise
revision-pinned external links and disclose the network dependency. Also requested
strict duplicate-key parsing for profile CLI input and replanning against the staged
copy so a configuration edit between planning and copying cannot mismatch the plan.
Those changes are now present. Independently created standalone agent-automation,
mobile-backend and public-website packets and ran their copied verifier modules
from inside each new directory: delivery 19, agent 22, durable 12, frontend unit 7
and browser 20 checks passed for their selected components. Each retained an
unchanged input image and its initially empty project evidence correctly returned
assessment exit 1. This covers all three component families, not six finished products.

### C4 — Low: browser startup unsupported under managed sandbox (resolved with condition)

The first independent browser run failed before any journey: installed Chromium's
SUID helper is unavailable in this managed non-root environment. The runner now
requires the explicit `BP_BROWSER_NO_SANDBOX=1` opt-in for this environment. An
independent rerun passed 20 actual browser checks on Chrome 154.0.8037.57 and Node
24.19.0. The receipt records `sandbox_disabled: true`; this reduced process
isolation applies only to the owned synthetic loopback fixture, not arbitrary pages.

### C5 — Medium: coverage could overstate executable/observed support (remediated)

The initial `library/coverage.py` checked reference files but not each named suite
entry point; a missing frontend suite still yielded `executable-reference`. It also
trusted a result's `status: passed` without checking its exit code and skip/failure
counters. An isolated contradictory record with returncode 1 and every named test
skipped yielded `observed-local-reference`. The coordinator added suite entry
validation and internally consistent receipts. Independent reruns now reject the
missing entry and classify the contradictory record as `stale-or-missing-observation`;
the two initial coverage regression tests passed. Authenticity is still explicitly
unproven even when a supplied record is internally consistent.

### C6 — Medium: TAP diagnostics could hide required skips (remediated)

`library/verification.py` used unanchored regular expressions for Node's TAP
summary. An isolated frontend test file with `console.log('# skipped 0')` followed
by one skipped required test produced `all_selected_passed: true`,
`tests_observed: 1` and `skipped: 0`. Node wraps console text as a TAP diagnostic
(`# # skipped 0`), which the search matched before the real summary `# skipped 1`.
This is an observation parsing defect, independent of the disclosed absence of
report authentication. Sent to the coordinator with the minimal reproduction.
Require complete top-level summary lines for all counters and retain this case
as a regression test.
The coordinator now requires exactly one anchored whole-line summary for tests,
pass, fail, skipped, todo and cancelled. The independent current verifier suite
passed all five tests, including this reproduction with actual `skipped: 1` and
`status: failed`. The three current coverage tests also passed, including missing
suite entry and malformed receipt checks.

## Concrete implementation observations

- Service core scopes HTTP actions to the synthetic bearer tenant and uses an
  immediate SQLite transaction for idempotency/payload equality/version checks,
  local mutation and outbox. The consumer's receipt and effect are atomic in the
  same local database; acknowledgement is separate. These are local invariants,
  not external provider guarantees.
- Agent core binds capabilities to run/tenant/task/action digest/revision/expiry,
  commits consumption before dispatch and only reconciles ambiguous retries.
  The authority object is a trusted fixture caller, explicitly not authenticated
  human identity. Model exceptions now record a bounded failure without leaking
  exception text. Eval reports identify the run/operation/action digest and inspect
  exact effect target/value. Empty/invalid/no-oracle corpora fail. All 22 focused
  tests passed independently, including two-connection dispatch and receipt mismatch.
- Frontend request identity and loading-state guards prevent late resolve/reject
  from replacing cancelled or superseded results; DOM rendering uses textContent.
  Actual browser checks passed under the explicit condition in C4.
- Verifier subprocesses now use a dedicated process group and kill the group at
  timeout. An independent isolated suite spawned a delayed child effect and hung;
  the verifier returned `timeout`, `all_selected_passed: false`, and the child
  effect did not happen after its scheduled delay. This covers ordinary descendants,
  not hostile code escaping its process group; the verifier is not a sandbox.
- Independently executed durable-service tests: 12 passed; frontend Node checks:
  7 passed. These observations were made during assembly, not claimed as an
  immutable final-release run.

## Guidance, sources and translations

- Read all six English playbooks and their source/claim mapping (21 representative
  direct or synthesis claims with limits), plus the three English operational guides.
  Source mappings distinguish contextual support from proof of the local implementation.
  Independently inspected the cited exact-action approval and external-effect
  idempotency propositions in their immutable OWASP/Azure source snapshots.
- Compared the six playbooks' 18 translations for heading/paragraph structure, code
  tokens and links. Read Czech AI/agent/mobile in full and consequential clauses in
  the remaining Czech pages; reviewed selected authority, data, recovery and model
  boundaries across all six German and Spanish playbooks. Czech tail-latency and
  database-commit versus provider-response ambiguities were corrected by the author.
- Read the three operational guides in Czech, German and Spanish. No targeted
  meaning blocker remained. Independently checked all nine translations for matching
  metadata/revisions, heading count, inline code, command blocks and link destinations.
  This is agent semantic control, not native-editor or human publication approval.
- Byte-verified all 53 immutable cached source snapshots against the source registry.
  The final finite NFKC/casefold ten-consecutive-token screen covered 49 files:
  36 new guide pages, three example READMEs, four updated integration guides,
  README/AGENT_SYSTEM/AGENTS/ADR-0002 and two new skills. It found zero matching
  pages after excluding frontmatter, final guide primary-evidence sections, URLs
  and HTML tags. It does not detect all paraphrase,
  translation, unseen sources or rights issues, and is not legal clearance.
  Metadata-only output: `/tmp/bp-operational-control-overlap-final.json`; locale checks:
  `/tmp/bp-control-operational-locales.json`. No source text is copied into this report.
- At the coordinator's request, this reviewer authored three representative source
  mapping proposals in `/tmp/bp-operational-claims.json`; the coordinator merged and
  validated them. These cover the operational guides, use inspected immutable
  passages from GitHub, OWASP and Azure, and explicitly classify local contracts as
  synthesis. This authorship is disclosed; the control role made no repository edits
  or commits and does not claim independent approval of its own mapping proposals.

## Final integration and scope disposition

Findings C1–C6 are resolved in the current working files.
No unresolved blocking defect was identified for the declared local advisory and
delivery-reference scope. This is a finite manual review of an operational reference
kit, not an assertion of universal software completeness, production readiness,
authenticated approval, native-editor translation review or legal clearance.

The final reviewed input image is
`55ea3827294494770273d91e9771b1c4bf9dd846c4bc3ddc890e942960be1959`
(218 enumerated files). At inspection, Git HEAD remained
`34aca583b2a7366f17138bb2c4a5d1ddfbb6bfbf` with `dirty: true`; this is the assembled
candidate identified by its listed file hashes, not a claimed clean new commit.
The input manifest's explicit file scope applies; it excludes generated reports,
reviews, caches and runtime state. A later changed candidate requires renewed checks
for the affected scope.

Independently inspected the final README, AGENTS, AGENT_SYSTEM, proposed ADR-0002,
four integration-guide changes, catalog/blueprints/evidence, new MCP tools, grouped
site navigation/exports and CI diff. All 33 catalog entries map to navigation groups.
Static `coverage.json` contains declarations, not falsely fresh runtime observations.
The final catalog and generated-link/anchor/language-switch/search checks passed
independently. The live stdio MCP test passed for all five tools and rejected unknown
guide/domain requests; these tools remain read-only. Current project tests passed
three cases, including source-overlap rejection for docs, skills and Git metadata.

The coordinator supplied `reports/reference-checks-final.json`, observed at
2026-10-22T11:06:17.386881+00:00, on Python 3.12.14/Linux and Node v24.19.0.
I independently checked its input-file digest, current file-image match, unchanged
input flag, internal receipts and computed coverage. It records passed delivery 19,
durable-service 12, agent-workflow 22, frontend-unit 7 and frontend-browser 20.
Its browser is Chrome/154.0.8037.57 with the explicit `sandbox_disabled: true`
condition described in C4. Coverage computes 23 `observed-local-reference` domains
and 12 `documented-guidance` domains. These are local unauthenticated observations,
not 23 completed production domains.

The coordinator separately reports the assembled 89-test Python suite with zero
skips, Ruff, actionlint, catalog validation, site build and generated-site checks
passing. That full run is coordinator evidence, not an independently repeated run
by this reviewer. My independently executed component and negative-case checks are
listed above, including three standalone packet families, current verifier 5,
coverage 3, project 3, and real stdio MCP 1. Checks run earlier during assembly are
not retroactively relabeled as executions against the final image.

The accepted scope is six selectable project patterns, conditional lifecycle
planning and artifact handoffs, local execution/check recording, advisory evidence
assessment, three reusable teaching components, and explicitly bounded guidance.
The host still performs actual authorized product implementation. Real identity,
payments/providers, live-model evaluation, native clients, specialized regulated or
real-time systems, distributed/long-duration capacity, production operations and
authenticated human release controls require adopter-specific implementation and
evidence. Remote hosted CI, merge and publication are separate events; none is
certified by this local review.
