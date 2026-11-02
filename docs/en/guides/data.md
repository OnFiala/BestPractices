---
{
  "id": "data",
  "language": "en",
  "revision": 3,
  "translation_revision": 3,
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

[pekko-cqrs](https://raw.githubusercontent.com/apache/pekko-projection/d1bcc1ed09efd8a11ce3dca0a7edea306dff6e02/docs/src/main/paradox/use-cases.md) · [postgres-partitioning](https://raw.githubusercontent.com/postgres/postgres/5681f0cfa5acfdc5146e2b74ff5b7e940df039f3/doc/src/sgml/ddl.sgml) · [rabbitmq-reliability](https://raw.githubusercontent.com/rabbitmq/rabbitmq-website/483c5f73095c3d808e98840e50c1ed5f2b148369/docs/reliability.md) · [pekko-event-sourcing](https://raw.githubusercontent.com/apache/pekko/0b963c40b68bfb8788f91a265a13f6ce38947b63/docs/src/main/paradox/typed/persistence.md) · [debezium-outbox](https://raw.githubusercontent.com/debezium/debezium/d67bfa5a10efac6eb74c0d62f43777b1198ad454/documentation/modules/ROOT/pages/quarkus/outbox.adoc) · [owasp](https://raw.githubusercontent.com/OWASP/ASVS/2b47a9dd16760ee484a6672d197f1f7e25d9c632/README.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml)
