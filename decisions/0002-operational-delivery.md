# ADR-0002: Connect guidance to bounded project delivery and observable references

Status: proposed · Owner: OnFiala · Date: 2026-10-22

## Context

The decision library explains architecture, verification and operations, but prose
alone does not turn a project request into reviewable artifacts or establish whether
its advice was exercised. Agents need explicit dependencies, bounded tasks, observable
acceptance cases and a way to preserve missing evidence. The implementation must also
separate local demonstrations from production authentication, external effects and
human release authority. A larger page count cannot resolve those boundaries.

## Decision

Implement a model-independent operational layer alongside the original library.
Six profiles select a conditional plan from 28 gates across 11 lifecycle stages:
intent, requirements, design, security, implementation, verification, release,
operation, incident, evolution and retirement. Profiles carry actual constraints,
risk, data, surfaces, external effects and measured workload. Architecture evolves
from observed limits and ownership; an account count alone is not a sizing rule.

`library.project init` creates a new portable local packet with profile, plan,
per-gate artifact instructions, empty evidence, selected reference code, original
guidance, skills, licenses and a copied-file manifest. It refuses an existing
output directory. `library.verification` runs only known local suites and records
the exact input image, runtime versions and outcomes. `library.delivery assess`
checks recorded artifacts/observations, revision/profile/plan bindings, prerequisite
order, reviewer labels and evidence age. Empty evidence exits 1 even if references
pass. Invalid inputs exit 2; a valid plan or complete recorded packet exits 0.

Keep execution in the user's authorized host, guided by five local skills. Expose
five read-only MCP tools for search, guide retrieval, planning, assessment and coverage.
The Python planner and MCP adapter do not call an LLM, implement an arbitrary product,
run remote tools, authenticate a human, merge or deploy. Authenticated human decisions
and real deployment controls remain outside the evaluator. `production_ready` and
`human_authorization.verified` stay false even when a packet is ready for human review.

Provide three original executable references: local SQLite/HTTP durability,
persisted agent-policy/effect fixtures, and browser state/rendering behavior. Keep
synthetic identity, approvals, providers, model responses and cost units explicit.
Record real local observations without treating them as live-model quality, real
billing, native-client behavior, regional recovery or production acceptance. The
browser reference requires Node 22+ and separately installed Chromium/Chrome. Its
sandbox stays enabled unless an operator explicitly selects the owned-local-fixture
exception in a controlled container; this is not permission to browse untrusted sites.

Publish a transparent coverage registry for 35 declared domains, linking guidance,
named checks, narrow claims and missing project evidence. The integrated catalog
contains 33 entries and 132 localized pages. These are scope inventories, not a claim
that the system covers all software engineering or independently proves its advice.
Keep English and all three translations aligned and distinguish source-supported
propositions from original local synthesis.

## Alternatives and tradeoffs

Keeping only documentation would be simpler to maintain, but leave handoffs and
negative evidence entirely implicit. A general autonomous orchestration/deployment
service would introduce identities, credentials, paid execution and approval trust
that this local repository does not supply. The chosen approach makes authorized
host work concrete without claiming that local labels establish authority.

Fixed reference suites are inspectable and bounded, but require extensions for new
stacks and specialized domains. Portable packet copies make the starting point
explicit and offline-readable; they also need deliberate regeneration and review
when source policy changes. Input hashes expose changes but cannot prove truth,
clock accuracy, independent identities or the sufficiency of a test oracle. Local
reports are observations, not signed attestations.

Separate producer/reviewer responsibilities increase review effort. Evidence age
windows are proposed defaults, not universal standards. Teams must justify them
against risk, release cadence and environment. Operational, incident and retirement
readiness are prepared before first release; actual retirement is a later activity.

## Validation and limits

Review the actual CLI journey from initialization through selected verification to
the intentionally blocked empty assessment. Check malformed and stale evidence,
negative permission/effect cases, concurrency, crash/restart, restoration, browser
transport races and bounded overload within each reference's documented scope.
Validate catalog/source/coverage relationships, localized meaning, static exports
and MCP behavior. Preserve failed, skipped and unrun cases. The dated
[operational delivery review](../reviews/2026-10-22-operational-delivery-review.md)
records observed outcomes and remaining limits; this ADR does not declare tests
passed or substitute for human adoption.

## Reversal and change triggers

Retain original Markdown/JSON guidance and immutable source references so the
operational layer can be replaced without discarding the library. Stop using new
planner/MCP/skill entry points if their contract proves unsuitable; preserve existing
packets and historical evidence as dated records. Review regenerated plans against
changed profiles, policies, blueprints, guide revisions and artifacts rather than
editing old hashes to hide drift. Copied project packets need their own migration;
removing the library feature does not roll those projects back.

Revisit when measured planning ambiguity, false acceptance/rejection, verification
cost, review backlog, specialized coverage needs or credential/attestation requirements
outgrow the local design. Any real model, identity, provider or deployment integration
requires a concrete contract and project evidence. Rollback of code or a snapshot
cannot reverse external actions or retract published data; reconcile those effects
and obtain the applicable human decision for destructive changes.
