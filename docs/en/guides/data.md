---
{
  "id": "data",
  "language": "en",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Data, contracts, and migrations

## Choose storage around invariants

Define access patterns, consistency, retention, residency and recovery needs before selecting technology. A relational database is a strong candidate for transactional business records; object storage often fits large blobs. Search indexes and caches are derived data unless the system explicitly makes them authoritative. These defaults are library recommendations, not universal mandates.

Give each record a stable identity and owner. Identify uniqueness, ordering and allowed state transitions, including deletion and restoration. Enforce critical invariants with the database's supported constraints/transactions; application checks alone can race. Understand the deployed isolation level and retry an entire affected transaction safely when required, rather than replaying an arbitrary fragment.

Tenant identity must come from trusted authorization context and accompany reads, writes, exports and background processing. Check derived views, analytics, logs and backups as well as the main tables. Retention and deletion rules must cover those copies; deleting a visible row is not proof that every copy was removed.

## Expand, migrate, contract

| Stage | Required decision and evidence |
| --- | --- |
| Expand | Add a compatible representation; document null/default and old-client behavior |
| Transition | Define the authoritative writer and how mixed versions read/write without losing meaning |
| Backfill | Use bounded, resumable work with checkpoints, conflict handling and observed resource/lock limits |
| Reconcile | Compare business invariants and representative records, not just row counts |
| Cut over | Select traffic deliberately, observe errors/lag and retain an abort condition |
| Contract | Remove the old form only after all supported clients/workers have migrated and recovery is ready |

Dual writing without a consistency strategy can create two contradictory truths. A code rollback does not undo a destructive migration. Decide whether recovery is rollback, forward repair or restoration plus reconciliation, and rehearse the actual path on production-shaped synthetic or appropriately protected data.

## Test concurrency and compatibility

Before changing a schema or public contract, run [integration and contract tests](testing-strategy.md) with old/new application versions against the transitional schema. Include concurrent updates, duplicate requests, interrupted backfills, import/export round trips and resumed jobs. A useful negative case has two clients compete for the same constrained resource and verifies that the invariant survives, not merely that one request returns an error.

Use [performance testing](performance-testing.md) to observe locks, replication lag, connection pools and migration duration on representative volume. A migration that succeeds on ten rows does not establish behavior on the real dataset. [Security tests](security-testing.md) must cover cross-tenant identifiers, export scope and revoked access after indexes/caches are refreshed.

Restore into an isolated environment, validate user-visible behavior and reconcile external effects before resuming processing. Measure recovery time and actual data loss against the agreed RTO/RPO, and record the backup/artifact versions. A replica can replicate accidental deletion; it is not a substitute for a tested recovery copy.

## Revisit the model

Version a contract when consumers need coordination; never silently change units, nullability, identifiers or meaning. Introduce another database only for a measured requirement that justifies consistency, backup and expertise costs. Partitioning needs explicit routing, ownership and cross-partition operation rules. Separate read models can help a measured query requirement but introduce a freshness contract when updated asynchronously.

## Related decisions

[Durability](durability.md) · [Security](security.md) · [Scaling](scaling.md) · [Testing strategy](testing-strategy.md) · [Performance testing](performance-testing.md)

## Primary evidence

[postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [owasp](https://raw.githubusercontent.com/OWASP/ASVS/2b47a9dd16760ee484a6672d197f1f7e25d9c632/README.md) · [azure-cqrs](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/cqrs.md) · [azure-data-partitioning](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/best-practices/data-partitioning-strategies-content.md) · [azure-idempotent-consumer](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/idempotent-consumer.md) · [azure-outbox](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/databases/guide/transactional-out-box-cosmos.md)
