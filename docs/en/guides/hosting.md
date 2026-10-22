---
{
  "id": "hosting",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Hosting and exit strategies

## Compare the whole obligation

| Option | Good fit | Cost to account for |
| --- | --- | --- |
| Static hosting/CDN | Public documentation and assets | Build limits, cache invalidation, domain ownership |
| Managed application platform | Small teams shipping a product | Platform limits, egress, supported runtimes, export |
| Managed functions | Bursty bounded execution | Execution limits, cold starts, connection pressure |
| VPS with containers | Predictable workloads and an owner for operations | Patching, backups, monitoring, recovery, spare capacity |
| Managed Kubernetes | Multiple workloads needing orchestration and a capable team | Cluster policy, upgrades, networking, workload security |

Managed services delegate tasks, not accountability. Compare monthly compute, storage, egress, observability, support, and human time. Verify region and data residency, restore capabilities, service quotas, and failure-domain independence. Never select Kubernetes merely because growth is expected.

## Portability contract

Keep application configuration external, document infrastructure as code, retain domain ownership, and prove data export. Pin deployable artifacts by digest. Name provider-specific features and the acceptable lock-in; portability has a cost too.

## Verify and migrate

Deploy to an isolated environment, run a functional request, restore data, rotate a credential, and estimate peak cost. Test migration using a copy: export, import, reconcile, cut over, observe, and retain a rollback window. DNS rollback alone cannot reverse writes made after cutover. This library uses static hosting; GitHub Pages deployment is manual and does not host the MCP server.

## Related decisions

[Operate your own servers](self-hosting.md) · [Scale from measurements](scaling.md) · [Health, recovery, and cost](operations.md)

## Primary evidence

[docker-security](https://raw.githubusercontent.com/docker/docs/main/content/manuals/engine/security/_index.md) · [kubernetes](https://raw.githubusercontent.com/kubernetes/website/main/content/en/docs/concepts/architecture/_index.md) · [opentofu](https://raw.githubusercontent.com/opentofu/opentofu/main/README.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml)
