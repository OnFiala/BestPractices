---
{
  "id": "data",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Data, contracts, and migrations

## Default to explicit invariants

Choose storage by access patterns, consistency, retention, and recovery needs. A relational database is a strong starting candidate for transactional business data; object storage suits large blobs. Search indexes and caches are derived views unless explicitly designed otherwise. Define identifiers, ownership, uniqueness, and deletion semantics before choosing a framework.

Use constraints and transactions for invariants. Understand the selected isolation level and retry serialization failures safely. Tenant authorization must accompany every read and write; test cross-tenant identifiers, exports, and background jobs. Logs, analytics, and backups also contain data and require retention rules.

## Expand, migrate, contract

Add a compatible schema first. Deploy readers/writers that tolerate both forms, backfill in bounded resumable batches, measure consistency, and remove the old form only after all consumers migrate. Rehearse on representative volume and observe locks. Do not assume a code rollback can undo a destructive data migration; keep a forward repair and tested recovery plan.

## Verify and revisit

Test old/new application compatibility, duplicate requests, concurrency, import/export round trips, and restoration. Record RPO/RTO and measure them. Version public contracts when consumers need coordination; do not silently change units, nullability, or meaning. Add another database technology only for a measured access requirement that justifies backup, expertise, and consistency costs.

## Related decisions

[Durability and distributed work](durability.md) · [Security, privacy, and supply chain](security.md) · [Scale from measurements](scaling.md)

## Primary evidence

[postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/mvcc.sgml) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml) · [owasp](https://raw.githubusercontent.com/OWASP/ASVS/master/README.md)
