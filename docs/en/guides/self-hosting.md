---
{
  "id": "self-hosting",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Operate your own servers

## Minimum topology

For a small service, a reverse proxy with TLS routes to an application on a private network; the database is not publicly exposed. Administrative access is restricted and audited. Separate production from experiments, and keep backups in another failure domain and account where feasible. One host is a single point of failure: document the accepted outage and recovery plan.

## Operating contract

Use infrastructure as code, pinned images, least-privilege users, resource limits, persistent volumes, and explicit secret injection. Do not expose the Docker socket to an application or assume a container is a strong sandbox. Define patch cadence, certificate renewal, disk alerts, log retention, and who responds outside working hours. Keep database migration credentials separate from normal application access.

Compose is a reasonable starting point for a few services. Orchestration is justified by scheduling, availability, or team requirements that outweigh its operational cost. A home server additionally needs a power, connectivity, physical security, and off-site recovery assessment.

## Recovery drill

Recreate a clean server from recorded configuration, restore data, verify a real user journey, and measure time and loss against RTO/RPO. A successful backup job is insufficient. Test certificate renewal and disk exhaustion safely in staging. Move to managed services when the team cannot meet patching or recovery obligations; adding replicas does not replace competent ownership.

## Related decisions

[Security, privacy, and supply chain](security.md) · [Hosting and exit strategies](hosting.md) · [Health, recovery, and cost](operations.md)

## Primary evidence

[docker-security](https://raw.githubusercontent.com/docker/docs/main/content/manuals/engine/security/_index.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml) · [opentofu](https://raw.githubusercontent.com/opentofu/opentofu/main/README.md)
