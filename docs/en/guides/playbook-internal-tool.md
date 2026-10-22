---
{
  "id": "playbook-internal-tool",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Deliver an internal operations tool

## Fit and constraints

Use this profile for a staff application that reviews records, exports data, or changes an upstream business system. A small audience can still have high-impact permissions. Record the identity provider, business approvers, data classification, revocation window, upstream rate limits, and maximum acceptable time for unresolved work. This agent-authored playbook proposes a local delivery approach; it is not an adopted organization policy.

Begin with one application and explicit integration adapters. Use organization SSO for authentication and a separate application policy for actions and record scope. A spreadsheet or existing workflow product remains an alternative when its permission, audit, and export behavior meets the actual need. A worker is justified by operations that outlast the request deadline or need durable retry. Separate integrations only when measured failure coupling, queue delays, or independent ownership repay the extra deployment cost.

## Repository and authority boundaries

Keep `identity/`, `policy/`, `cases/`, `integrations/`, `exports/`, and `audit/` distinct in code. Define which system owns each field; an imported upstream value must not silently become an independently editable truth. An operation ledger records requester, action, object scope, input version, approval identity, stable operation ID, and status. Store necessary audit facts with access controls and retention, not unrestricted copies of confidential payloads.

Authentication proves identity, not permission. Check action and scope at API entry, export creation, export download, and worker execution. Queued work needs a declared delegation policy: either revalidate the requester's current rights or use a separately authorized service mandate. Do not accidentally preserve former employee authority in a job payload. Define revocation timing across application sessions, cached permissions, download links, and running jobs. For consequential upstream writes, bind any required business approval to the precise intended change.

## Delivery sequence and handoff

1. Discovery maps one business journey, its source-of-truth fields, an authorization matrix, and the manual fallback when upstream systems are unavailable. A human business owner resolves ambiguous approvals and retention.
2. Implementation builds a narrow vertical slice with read-only inspection, scoped mutation, durable pending status, and an operation lookup. Introduce export only after defining its separate authorization and expiration contract.
3. Verification challenges access changes during a session and during queued work, then simulates an upstream response lost after success. The operations role writes a reconciliation runbook using stable operation IDs and prepares rollout to a named staff cohort.

Deliver a profile, ADR, policy matrix, upstream contract inventory, state-transition diagram, export specification, evidence with expected and observed outcomes, release/recovery procedure, and support owner. Agents may fill these roles sequentially; extra agents do not create independent assurance. The local `examples/durable_service` and `examples/agent_workflow` directories can inform persistence and gated-work experiments. They do not supply an enterprise identity provider or approval from business owners.

## Select adversarial and operational checks

Unit-test policy decisions and state transitions. Use integration tests for session invalidation, upstream adapters, export materialization, and durable jobs. Browser tests should cover denied access, unavailable upstream data, an empty case list, and pending work that remains visible after refresh. A disabled button is never an authorization oracle.

Create a restricted employee and an administrator over synthetic records. Call protected endpoints directly; request an oversized export and manipulate its filters and download identifier. The exported bytes and resulting changes must stay within the caller's scope. Revoke the employee while a session, signed link, and queued operation exist; after the agreed window, protected access must fail and jobs must follow the declared delegation policy. Observe state and upstream effects, not just response codes.

Make the upstream accept a change and drop its response. Retrying must reuse a supported idempotency identity or hold the operation for reconciliation. An unavailable provider must not appear as success, and a timeout must not erase uncertainty. Test bounded retries, queue saturation, and recovery pacing against provider quotas; stop before agreed resource limits. Record blocked and skipped cases with the missing prerequisite.

## Release, recover, and own the service

Release to a defined staff cohort with a known rollback artifact and upstream writes initially bounded by the accepted rollout plan. For schema changes, support mixed versions and backfill with checkpoints before removing fields. Application rollback cannot undo an upstream action. Pause dispatch, inspect the ledger, query provider state, and apply a business-approved correction where reversal is possible. Restore audit and application records together or explain how gaps are reconciled.

Monitor aged pending work, denied operations, revocation delay, export volume, provider throttling, and cases requiring manual repair. Assign separate business and technical owners and an escalation deadline for uncertain effects. Include integration licenses, staff time, audit storage, and on-call work in cost estimates. Production gaps include real SSO integration, session policy, emergency access, approver coverage, retention, and incident drills. Retirement requires closing pending cases, transferring necessary audit records, notifying process owners, revoking service access, and verifying that scheduled jobs no longer issue writes.

## Continue with related decisions

[Security](security.md) · [Operations](operations.md) · [Testing strategy](testing-strategy.md) · [Durability](durability.md)

## Primary evidence

[owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-session](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Session_Management_Cheat_Sheet.md) · [azure-idempotent-consumer](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/idempotent-consumer.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md)
