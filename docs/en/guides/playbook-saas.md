---
{
  "id": "playbook-saas",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Deliver a tenant-aware SaaS

## Fit and initial architecture

Use this profile when independent customer organizations share an application and its infrastructure. Capture tenant isolation, billing semantics, data residency, recovery objectives, peak workload shape, and who owns customer support. A proposed starting point is a modular application, relational database, and bounded background worker. One deployment can still enforce separate membership, business-record, billing, and delivery modules. This agent-authored guide is local synthesis, pending human adoption.

A single-host database may fit an isolated prototype with accepted availability limits. Managed relational hosting is an alternative when recovery, concurrent writes, and operational support require it. Separate databases per tenant may satisfy isolation or residency constraints but increase migration and support cost. Measure query latency, lock waits, queue age, and noisy-neighbor effects before adding replicas, partitions, or services. Extract a module only with an independent contract, owner, and measurable gain; tenant count is not an architecture threshold.

## Put invariants in the repository

Use boundaries such as `domain/`, `api/`, `persistence/`, `billing/`, `workers/`, `contracts/`, and `ops/`. The authenticated principal determines authorized tenant membership; a tenant selector supplied by the client never establishes authority. Every read, mutation, export, cached view, and queued job carries verified tenant context. Keep support impersonation explicit and audited.

Specify record identity, tenant-scoped uniqueness, currency/units, state transitions, pagination, errors, and retention. For a retried command, bind its idempotency key to tenant, operation kind, and canonical request fingerprint. Reusing the key with different input must conflict. Commit the business change, stored response, and outbox entry atomically where they share a database. The relay can deliver twice; its consumer or provider contract must prevent duplicate business effects. A local transaction cannot make a remote charge atomic.

## Sequence agents and artifacts

1. The discovery role writes a principal/action/object matrix, business invariants, workload envelope, and billing uncertainty cases. The human owner accepts recovery and financial-risk decisions.
2. The implementer delivers one vertical slice: authenticated command, tenant-scoped transaction, durable status, and a retriable worker path. It records storage and tenancy alternatives in an ADR and supplies a compatibility migration.
3. The verifier exercises HTTP and persistence together, then challenges tenant boundaries, concurrency, interruption, and restoration. The release role prepares a bounded rollout and reconciliation procedure; human review controls production acceptance.

The packet includes the profile, ADR, API schema, authorization matrix, migration order, operation/outbox ledger examples, observed test evidence, restore report, provider reconciliation instructions, cost estimate, and named service/data owners. `examples/durable_service` is a local reference to inspect and adapt. Its presence does not prove authentication, provider billing, high availability, or this project's recovery objectives.

## Test business outcomes, including forbidden ones

Use unit tests for money and state rules, contract tests for consumers, and integration tests with the actual chosen database for isolation and atomicity. A SQLite result cannot establish PostgreSQL lock or isolation behavior. In two synthetic tenants, substitute identifiers in reads, writes, exports, and worker payloads. The oracle is no unauthorized response data and no changed foreign-tenant state, not merely an HTTP denial.

Submit simultaneous copies of a command and reuse its key with a different amount. Inspect records, stored responses, and effects: one intended business operation remains, and mismatched reuse fails. Crash before commit, after commit, and after provider success but before acknowledgement. The latter must produce a safe retry under a documented provider guarantee or a visible reconciliation state, never a blind second charge. Restore an isolated backup, compare business invariants, and reconcile provider records before restarting delivery. Preserve failed and unrun cases.

Load tests should reproduce expensive queries, skewed tenants, concurrent writes, and bounded backlog recovery. Agree latency/error/queue targets and abort limits before running. Include browser tests for denied, pending, and ambiguous outcomes, so users are not encouraged to resubmit an uncertain payment.

## Deploy and operate across the data boundary

Expand schema first, deploy compatible readers/writers, backfill in resumable batches, reconcile, then remove the old representation only after the compatibility window. Abort on agreed error, lock-wait, or reconciliation thresholds. Rolling application code back does not restore deleted data or reverse a charge. Retain the previous artifact, backups, migration checkpoints, and a plan for forward repair or isolated restoration.

Monitor authorization denials, transaction failures, queue age, delivery attempts, billing discrepancies, and recovery freshness with privacy-safe correlation IDs. Budget database capacity, backups, provider fees, transfer, and operational labor per useful business outcome. Assign incident authority to pause billing and workers separately. Production gaps include identity lifecycle, key management, payment contracts, tenant offboarding, restore rehearsal, and on-call cover. On retirement, stop new writes, settle pending external effects, export authorized customer data, honor retention/deletion rules, and revoke integrations without destroying required financial evidence.

## Continue with related decisions

[Data and migrations](data.md) · [Durability](durability.md) · [Security testing](security-testing.md) · [Scaling](scaling.md)

## Primary evidence

[owasp-multi-tenant](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.md) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [azure-outbox](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/databases/guide/transactional-out-box-cosmos.md) · [azure-idempotent-consumer](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/idempotent-consumer.md)
