# Operational delivery review — 2026-10-22

This edition connects a local project packet, conditional lifecycle plan, bounded
reference execution, evidence consistency assessment, and human release review.
It is an agent-maintained operational reference system. It does not autonomously
build arbitrary products or establish universal software-engineering completeness.
All guidance and translations remain proposed pending human approval.

## Current verified state

The current implementation is `4ecd1c23e4693d6a739397e879580db92ab7d0b4` and the
current observed input image is
`662f3feb9a2a5d6149e5b4a9e5944bead4834cecfd9b8b4e6c9344cdc0043e90`.
The complete [hosted quality run](https://github.com/OnFiala/BestPractices/actions/runs/39770522601)
passed. The local inventory now includes 12 frontend tests (five added startup
regressions), 20 actual browser journeys and the unchanged 89-test Python suite.
The earlier counts and images below are retained historical observations.
[Current receipts](2026-10-22-browser-startup-evidence.json) and the
[browser-startup control review](2026-10-22-browser-startup-control.md) describe the
final bounded-startup correction; no failed run is reclassified as passed.

## Reviewed scope and identity

The change extends base commit `34aca583b2a7366f17138bb2c4a5d1ddfbb6bfbf` on PR #1.
The initial integrated code/configuration/guidance image is
`55ea3827294494770273d91e9771b1c4bf9dd846c4bc3ddc890e942960be1959`.
The full file inventory and execution receipts are in
[operational evidence](2026-10-22-operational-evidence.json). Execution occurred
before commit, so the receipt correctly records the previous HEAD and dirty state;
its input digest identifies the actual tested files. Reviews, generated reports,
caches and runtime state are outside that image. This is a local content binding,
not a signed provenance attestation. Remote CI is reported separately on the PR.

The inventory contains six project profiles, 28 conditional gates across eleven
lifecycle stages, 35 declared coverage domains, 33 catalog entries in four languages
(132 pages), three executable references, five read-only MCP tools, and five skills.
The source registry has 53 pinned primary documents and 81 representative claim
mappings. Counts measure scope, not correctness, exhaustive support or certification.

## Review process and corrections

Specialist agent workstreams implemented and checked the planner, transactional
service, frontend, agent workflow, playbooks and translations. A separate read-only
control thread using GPT-6-astra at maximum reasoning challenged the implementation,
ran isolated reproductions and checked the integrated handoffs. Its
[independent report](2026-10-22-operational-control.md) separates its own runs from
coordinator observations. These are agent reviews, not human approval or a formal
Codex Security scan; the formal scanning tools were unavailable in this environment.

Six independent findings were corrected: required skips could look like passes;
malformed policy could omit retirement; copied packets lacked their referenced
guides; the managed container could not start the browser sandbox; coverage could
trust a missing suite or contradictory receipt; and TAP diagnostic text could hide
a skipped test. Regression checks preserve the failure cases. Browser sandbox
relaxation is an explicit condition for the owned synthetic fixture, not a default.
The coordinator also prevented packet output within copied docs, skills and Git
metadata. A process-group timeout was independently exercised with a delayed child
and stopped that ordinary descendant; this verifier is not a hostile-code sandbox.

## Observed behavior

| Check | Observation and scope |
| --- | --- |
| Full Python suite | 89 passed, zero skipped; content/source/license invariants, planner, verifier, packet, security and reference cases |
| Fixed reference inventory | Delivery 19, durable service 12 and agent workflow 22 passed; these are subsets of the full Python suite |
| JavaScript | 7 frontend unit/HTTP tests and 4 mocked WebMCP adapter tests passed |
| Real browser | 20 journeys passed on Chrome 154.0.8037.57 / Node 24.19.0; explicit sandbox-disabled local fixture |
| Packaging and site | Ruff, actionlint, 33-entry/four-locale validation, strict 132-page build and generated link/anchor/language/search/license checks passed |
| Portable journey | Fresh copied agent-automation, mobile-backend and public-website packets executed their selected component suites; initial empty evidence remained blocked with exit 1 |
| Coverage receipt | Current image matches; 23 domains have narrowly scoped observed local reference support, 12 contain documented guidance |
| Agent corpus | 26 passed, zero failed, one explicitly skipped live-model-quality record; model quality is unverified |

The service drill used actual child-process termination before commit, after commit
and after a consumer effect before acknowledgement. Each recovered to one local
effect with no pending record. Schema v1-to-v2 compatibility and a separate-file
restore passed; one known post-snapshot operation was absent after restore, as
expected. The workflow reference instead uses simulated interruption and reopened
SQLite ledgers. Neither exercise establishes regional recovery or storage-loss safety.

The bounded baseline completed 30 requests successfully, with zero rejected or
transport failures. The overload run offered/completed 120 requests with eight
workers, admission capacity two and an artificial 10 ms delay: six succeeded,
114 received deliberate overload rejection, and zero had transport errors. A
subsequent accepted request returned 200, integrity passed and pending work was
zero. These are short closed-loop local observations with a shared generator/server,
not production capacity, sustained-load, soak or tail-SLO evidence. Raw counts,
configuration, measured latencies and limits are retained in the evidence JSON.

## Sources, originality, translations and licensing

The explanation, code, examples and translations were written for this repository.
External documentation is referenced by immutable URL and hash; source prose,
model source-fed logs and raw source snapshots are not published with this change.
Text remains CC BY 4.0 and original code/configuration MIT. Existing third-party
website notices and corresponding source retain their own licenses; no new vendor
asset or application dependency was introduced. Prior document-license classifications
remain reference-only, including unresolved and mixed grants; citations do not grant
reuse permission. See [PROVENANCE](../PROVENANCE.md) and the foundation review.

The control thread hash-checked 53 private immutable snapshots and screened the new
and changed prose against that finite corpus. The metadata-only
[originality screen](2026-10-22-operational-originality.json) records exact scope,
normalization and exclusions. Literal overlap checks cannot establish absence of
paraphrase, translation reuse, unseen-source overlap or rights issues. Human editorial
and rights review still applies before acceptance/publication.

Specialists checked all 27 new CS/DE/ES translations for complete meaning and
structural parity; control independently checked structure and consequential
semantics. The four integration guides were updated together to revision 3. Commands,
stable IDs, source links, constraints and fixture-versus-production limits agree.
This is agent language review, not native-editor sign-off.

Live monitoring observed one changed document, `owasp-csrf`, with no unavailable or
overdue sources. The agent's bounded semantic review is recorded in
[CSRF drift evidence](2026-10-22-csrf-source-drift.json). The immutable reviewed
baseline remains unchanged; a monitoring hash is never automatically adopted.

## Remaining adoption decisions

The planner is advisory and the host performs authorized work. Caller-provided
roles, timestamps, evidence and approval fields are assertions. Even a complete
packet only becomes ready for human review; `production_ready` and verified human
authority remain false. Real identities, provider semantics, project requirements
and trusted evidence capture must be implemented and assessed in an adopting project.

Live-model quality, native WebMCP host compatibility, remote ChatGPT hosting,
production identity/payment integration, distributed capacity, long-duration tests,
native mobile behavior and regulated/safety-critical assurance are unverified or
outside these local references. The coverage map exposes additional project evidence
rather than representing those gaps as passes. Do not deploy teaching credentials,
fixture approvals or local test servers as production services.

Human review/merge remains required. Rulesets, Pages publication, private source-fed
maintenance and paid providers need actual platform configuration; repository files
do not activate them. No production deployment or remote connector is claimed.
Future changes should regenerate affected plans, preserve historical observations,
repeat relevant checks and propose a reviewable PR rather than silently promoting
source/model updates or rewriting old evidence.

## GitHub execution follow-up

The initial remote [run 39768595418](https://github.com/OnFiala/BestPractices/actions/runs/39768595418)
passed the full Python suite, content validation and WebMCP tests, but failed in the
fixed-reference step. Redirected log downloads returned HTTP 403; the precise cause
could not be established. That failure is retained, not reclassified as a pass.

Commit `00d7bf56e95d58922ef43ead220b3c064c20c000` adds only bounded, escaped failure
annotations to the CI wrapper. It preserves the original verifier exit status, fixed
suite arguments and read-only workflow permissions. No reference implementation,
skip rule, automatic retry or sandbox default changed. The independent control
thread inspected this delta and found no authorization or diagnostic-scope blocker.

The subsequent [run 39769062394](https://github.com/OnFiala/BestPractices/actions/runs/39769062394)
passed every quality step, including the fixed references, coverage and built site.
A new local fixed-suite observation passed with unchanged inputs at digest
`5284b9a2a766f75209284e98805d4e9d3fab8d49fe8d0f2170ec24ec8adf63c1`.
Its receipts and both remote outcomes are in the
[CI follow-up evidence](2026-10-22-operational-ci-followup.json). A later green run
cannot prove why the initial run failed. Any recurrence remains a failed gate;
the new annotation supplies bounded diagnostics for investigation. This retained
uncertainty is separate from the six corrected implementation findings above.

## Browser readiness correction

[Run 39769618962](https://github.com/OnFiala/BestPractices/actions/runs/39769618962)
repeated the reference-step failure. The new annotation identified the immediate
condition: no browser debugging port within the old roughly five-second polling
budget, with empty stderr. It does not prove the cause of the earlier unlogged run.

The startup helper now waits for a complete valid port/endpoint for at most
20 seconds, checks monotonic expiry, fails promptly on spawn/exit errors, and
ignores readiness after its deadline. The whole browser run still has a 45-second
limit and owns child/profile cleanup. Five real-child regressions exercise a
marker arriving after 5.5 seconds, partial marker, early exit, spawn failure and
late readiness after timeout. Browser selection, network restrictions, required
journeys and the default sandbox are unchanged; startup failures identify the
selected executable and actual Node version.

All 12 frontend tests and 20 browser journeys passed locally and independently.
The fixed local report retained an unchanged image; the full hosted quality run
at the implementation commit above then passed. This is evidence for the bounded
correction and observed run, not proof of unlimited host or browser reliability.
The original first failure remains without its detailed log and is preserved in
the history above.
