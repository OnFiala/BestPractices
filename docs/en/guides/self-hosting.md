---
{
  "id": "self-hosting",
  "language": "en",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Operate your own servers

## Define the topology and its limits

A small public service can place a TLS reverse proxy at the ingress boundary, an application on a private network and a database reachable only by authorized application/administrative identities. Network placement supplements authentication; it does not replace authorization. Separate production from experiments and give administrative access an audited, restricted path. A single machine remains a single failure domain even when it runs several containers.

The minimum operating contract below is a library recommendation informed by container-security and recovery documentation. Adapt it to the platform and impact; this is not a hardened server configuration ready to deploy.

| Obligation | Record and verify |
| --- | --- |
| Administration | Owner, scoped access, revocation path and evidence of denied access |
| Software updates | Supported OS/runtime, patch owner, maintenance window and recovery artifact |
| Resource isolation | CPU/memory/disk limits, capacity alerts and behavior under exhaustion |
| Secrets | Injection/rotation mechanism and separate deployment, migration and application identities |
| Persistence | Explicit data volumes, backup scope, encryption/key access and retention |
| Public boundary | TLS renewal, allowed ports, authentication and safe error responses |
| Recovery | Off-host backup, last successful restore, RTO/RPO and incident contact |

Prefer a separate backup account or failure domain where feasible. A backup on the same writable disk can fail with the server or be deleted by the same compromised identity. Verify that restoration does not depend on credentials stored only on the lost host.

## Deploy a reproducible unit

Use infrastructure as code and pin the deployable image by digest. Store application state in explicitly managed persistence, not an accidental container layer. Do not expose the Docker socket to the application or agent, and do not treat a container as a strong hostile-code sandbox. Restrict privileges and resources to what the workload needs.

Compose can fit a few services with understood failure and update behavior. Adopt orchestration when scheduling, availability or team requirements justify its operational burden. More replicas on one machine do not make that machine highly available. A home server additionally needs power, connectivity, physical-access and off-site recovery assessment.

## Recovery and failure drill

On a separate test machine, recreate the host from recorded configuration and restore a recent backup. Disable real email, payments and other external side effects. Validate a representative user journey, tenant permissions, business totals and queued work before declaring restoration successful. Measure recovery time and the actual loss window against the agreed objectives.

Before a material hosting change, use [performance testing](performance-testing.md) to exercise bounded overload and recovery in an authorized environment. Test disk pressure, a stopped application, an unavailable database and certificate renewal safely. Use [security testing](security-testing.md) to verify closed administrative/database ports from the public boundary and revoked credentials.

A test passes only when the user-facing behavior and recorded state meet the acceptance contract. If recovery depends on undocumented manual steps, record them and repeat the drill. Move to a managed service or reduce scope when ownership cannot meet patching, response or recovery obligations; adding machinery does not resolve an ownership gap.

## Related decisions

[Security](security.md) · [Hosting](hosting.md) · [Operations](operations.md) · [Performance testing](performance-testing.md) · [Security testing](security-testing.md)

## Primary evidence

[docker-security](https://raw.githubusercontent.com/docker/docs/4d64a8e4f0a59967fc0b391120d54a90e9ccb60d/content/manuals/engine/security/_index.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [opentofu](https://raw.githubusercontent.com/opentofu/opentofu/ec773ed37be4d07e00d4a2fbb237d0c0fe1ca3ce/README.md)
