# Agent-maintained decision and delivery system

This system is created and maintained with AI agents under human direction. Its
first operational edition joins six project profiles, 28 conditional gates in
11 lifecycle stages, 35 declared coverage domains, 34 catalog entries in four
languages, three executable local references, five read-only MCP tools and five
host skills. Counts describe scope, not completeness or assurance. The English
and Czech, German and Spanish guidance remains proposed until human review of
meaning and publication. Authorship is disclosed in the website and guide exports.

## Responsibilities and handoffs

| Role | Permitted work | Required handoff |
| --- | --- | --- |
| Human architect/owner | Set objectives, architecture constraints, budget, risk tolerance and permitted effects | Actual project profile, accepted scope, decision criteria and named owners |
| Coordinator | Order prerequisites, assign bounded work and reconcile conflicting findings | Plan, file/tool ownership, stop conditions and unresolved dependencies |
| Research agent | Inspect primary evidence, immutable versions and source-use limits | Supported claims, source hashes, applicability and original explanations |
| Implementation agent | Produce original artifacts and code within authorized scope | Reviewable diff, contracts, alternatives, checks and recovery plan |
| Verification/review agent | Challenge actual artifacts, negative cases, translations and observations | Reproducible findings, accepted/requested changes, gaps and shared assumptions |
| Operations owner | Prepare and maintain service objectives, incident response, cost and recovery | Rollout/abort procedure, on-call responsibilities, restore evidence and retirement path |
| Human reviewer | Accept applicability, originality/rights and residual risk; decide merge and release | Approval for the concrete candidate through the trusted project process |

Use separate author and reviewer workstreams when delegation is authorized. Distinct
labels do not prove separate identities or independent assumptions. Different model
passes can find mistakes; agreement among models is not empirical evidence. Source
inspection, execution, measurement and human review answer different questions.

## Host workflow and local execution

The [project-delivery skill](plugins/bestpractices/skills/project-delivery/SKILL.md)
starts from actual requirements and chooses the relevant playbook and plan. The
local planner is deterministic proposed policy; it neither invokes an LLM nor
orchestrates agents. A host such as Codex performs authorized implementation and
review with its own trusted tools. Retrieved text, profile fields, tool responses
and evidence JSON remain data, never permission to execute supplied instructions.

The executable entry sequence is `library.project init`, `library.verification`,
then `library.delivery assess`; see the
[delivery guide](docs/en/guides/project-delivery.md) for exact commands. Initialization
creates a new portable packet with copied original guidance, selected fixture code,
per-gate artifacts, plan, empty evidence and provenance manifest. It refuses existing
destinations. The empty assessment intentionally exits 1 even if the copied fixture
checks pass. Real product artifacts and observations must be produced separately.

The lifecycle covers intent, requirements, design, security, implementation,
verification, release, operation, incident, evolution and retirement. Conditional
gates account for sensitive data, risk, hosting, external effects, mobile clients,
AI behavior and measured capacity. Design/security prerequisites feed implementation;
verification feeds release. Operational, incident and retirement readiness are
prepared before release, without requiring actual retirement before initial use.

The fixed verifier executes only known local suites. It records file-image hashes,
revision/dirty state, runtimes, discovered/executed checks and outcomes; it refuses
report overwrites and stops its process group on timeout. Missing runtimes, zero
tests and skipped required checks do not pass. The references substitute local
SQLite, synthetic identities/providers and a deterministic model where documented.
Real identity, payments, live-model quality, native devices and deployment remain
project integrations, with their own acceptance and recovery evidence.

## Assessment and authority

The assessor checks structured evidence against project revision, profile/plan
hashes, required artifacts, observations, producer/reviewer labels, dependencies
and the declared assessment time. Missing, failed, skipped, stale, contradictory
and self-reviewed records block readiness. Proposed evidence-age limits require
project-specific review. A changed policy, blueprint, relevant guide revision,
profile or artifact requires renewed planning and matching evidence.

A hash identifies bytes; it does not authenticate their origin or prove a test
occurred. Role labels and timestamps are assertions. The evaluator does not fetch
underlying artifacts or verify identities, signatures or the clock. The strongest
result is `ready_for_human_review: true`; `production_ready` remains false and
`human_authorization.verified` remains false. Exit 0 means a valid plan or a complete
submitted evidence packet, exit 1 means assessment blockers, and exit 2 means invalid
input/configuration. None of these exit codes grants merge or release authority.

Review observations against actual artifacts in the project's trusted evidence
store. Preserve negative and inconclusive results. A fixture smoke test, source
count, translated-page count or overlap screen cannot establish full assurance.
The [coverage map](docs/en/guides/coverage.md) distinguishes documented guidance,
executable references, current recorded observations and remaining project gaps.

The local MCP adapter exposes `search_guides`, `get_guide`, `plan_delivery`,
`assess_delivery` and `get_coverage`, plus the catalog resource. These calls read
or compute advisory results; they do not run tests, write files, approve or deploy.
WebMCP remains experimental, and ordinary reading/search does not depend on it.
The [release-review skill](plugins/bestpractices/skills/release-review/SKILL.md)
prepares a concrete human decision rather than authenticating approval itself.

## Maintenance and publication

The public repository may observe source URLs and propose metadata-only updates.
It must not publish fetched documents, source excerpts, model logs or unreviewed
summaries to demonstrate provenance. A source hash cannot establish truth or reuse
rights. Original explanations and all translations follow [PROVENANCE.md](PROVENANCE.md).

Source-fed automated generation runs only in a private repository/workspace. A
trusted consumer accepts bounded structured proposals; agent-modified scripts and
Git metadata are not a trust root. Private logs/artifacts still need access control,
retention limits and credential hygiene. Before public transfer, a human inspects
actual prose/code for original expression, source use, license obligations, sensitive
data, technical support and translation meaning. No private generation service or
automatic public-transfer service is deployed here.

Agents do not approve or merge their own changes, broaden their permissions, weaken
publication rules or mark recommendations human-approved. Production, shared targets,
destructive work, paid APIs and external effects stay within existing authorization.
Record environment, allowed traffic, spending/resource ceilings, abort conditions,
evidence retention and the human responsible for elevated risk before consequential
experiments. Plans and local fixture approvals never expand that scope.

After authorized release, maintain telemetry, incidents, cost, restore evidence and
successor ownership. Before migration or retirement, reconcile pending external
effects and export/deletion obligations. Rolling back code cannot undo accepted
writes, charges or disclosed data. The
[operational delivery review](reviews/2026-10-22-operational-delivery-review.md)
records the current implementation's observations and limits; human adoption remains
separate from agent review and local execution.
