---
{
  "id": "examples",
  "language": "en",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Reference project paths

## Six design profiles, not deployed applications

These original profiles connect architecture choices to a first observable proof. They are illustrative starting points, not benchmarked stacks, compliance certifications or completed test results. The [machine-readable design profiles](https://github.com/OnFiala/BestPractices/blob/main/data/blueprints.json) contain boundaries, recovery, change signals and planned test packets. Pin the repository revision when adopting them.

| Project | Starting design | First proof | Revisit when |
| --- | --- | --- | --- |
| Public website | Static build/CDN and content history | Accessible navigation, no private output, previous artifact recovery | Trusted writes or measured publishing limits appear |
| SaaS | Modular app, transactional database and bounded worker | Tenant isolation, payment reconciliation and restore | Measured contention or independent domain ownership appears |
| Internal tool | SSO, small app, scoped integrations and audit | Revoked users cannot read or export; delayed work is accountable | Owners or reliability obligations diverge |
| AI application | Model adapter, authorized retrieval and evaluation set | Denied documents stay out of model context; failures remain bounded | Evaluated quality, cost, latency or residency changes |
| Agent automation | Durable run ledger, bounded workers and scoped tools | Duplicates, stale approvals and budget stops cannot exceed authority | Independent tools/workloads need separate failure boundaries |
| Mobile/backend | Client cache, compatible API and explicit sync rules | Offline recovery, conflicts and old-client support | Measured sync pressure or geography justifies redesign |

## Public website

Assume public authored content and no user-specific server writes. Build an immutable artifact and publish through a reviewed deployment identity. Before release, navigate and search through each supported locale using keyboard and a narrow viewport. Check the generated output and search index for private data; a client-side login cannot protect public files. Deploy a known previous artifact in a test environment and verify a real route. Add a protected API only when the product needs trusted writes; do not turn a static build token into a public browser credential.

## SaaS with payments

Assume multiple tenants and a provider responsible for charges. Bind every operation to the authenticated tenant; persist local business transitions with a stable operation identity. Before changing authorization or billing, exercise cross-tenant object/export attempts, duplicate submissions and a lost provider response. Inspect local and provider records, rather than trusting only an HTTP status, to establish one intended business outcome or an explicit unresolved reconciliation state. Restore an isolated copy, reconcile payments and resume pending work deliberately. Introduce services only for measured ownership/isolation or capacity benefit.

## Internal tool

Assume an organization identity provider and one upstream business integration. SSO establishes identity; the application still authorizes each action and export. Test revocation through both a current session and a queued job within the agreed revocation window. Make an upstream unavailable, then verify that pending work is visible and retried only within its policy. Reconciliation uses a stable operation ID so an operator can determine whether an upstream write happened. Give audit records an owner and retention rule; corporate network access alone is not authorization.

## AI application

Assume a bounded model feature that retrieves documents for an authenticated user. Apply document authorization before content enters retrieval results or the model context, and preserve revocation/deletion across indexes and caches. Before changing a model, prompt, retrieval path or policy, run held-out representative and adversarial evaluations with explicit scoring and human review where judgment is required. Include denied documents, abstention, prompt injection and provider timeout. Measure success and grounding alongside latency and cost; plausible language is not correctness. A safe fallback can disable the feature or offer ordinary authorized search.

## Agent automation

Assume queued tasks may cause consequential tool writes. The run ledger records task identity, authorized scope, approval binding, attempts and observable outcome. Test a duplicate task, an expired approval, a changed action after approval, hostile retrieved instructions and a consumed budget. The enforcement boundary must stop unauthorized tool calls independently of model cooperation. Use fake or isolated external destinations for failure tests. After a crash, reconcile whether the effect happened before resuming; a worker restart must not blindly repeat an irreversible action.

## Mobile application and backend

Assume clients cannot all upgrade immediately and can edit while offline. Keep authorization and canonical state on the server, necessary local data in platform-appropriate protected storage, and conflicts governed by an explicit rule. Before release, test the oldest supported client against the new API, interrupted synchronization, repeated upload and competing offline edits. Verify that device revocation blocks refresh and subsequent protected operations according to the documented session contract. Do not assume revocation erases data already downloaded to a device. Regional or partitioned sync requires evidence about conflict rate, latency and recovery cost.

## Give an agent a testable task

For the selected profile, agree workload, SLO/RTO/RPO, data rules and budget with the human owner. Convert its planned cases into the actual stack's tests using the [testing strategy](../guides/testing-strategy.md), [performance-testing plan](../guides/performance-testing.md) and [security-testing plan](../guides/security-testing.md). Record setup, stimulus, observable oracle, negative cases, stop conditions and retained evidence. An agent must distinguish a proposed test from an executed result and report a missing prerequisite instead of inventing a pass.

## Related decisions

[Adoption](../guides/adoption.md) · [Architecture](../guides/architecture.md) · [Agents](../guides/agents.md) · [Frontend](../guides/frontend.md) · [Testing strategy](../guides/testing-strategy.md)

## Primary evidence

[owasp](https://raw.githubusercontent.com/OWASP/ASVS/2b47a9dd16760ee484a6672d197f1f7e25d9c632/README.md) · [openai-agents](https://raw.githubusercontent.com/openai/openai-agents-python/841dfdd938bfd4ca052475eb76d6245a356868e0/docs/agents.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [wcag](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/index.html) · [azure-architecture-styles](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/guide/architecture-styles/index.md) · [azure-retry](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/retry-content.md) · [azure-idempotent-consumer](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/idempotent-consumer.md)
