---
{
  "id": "hosting",
  "language": "en",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Hosting and exit strategies

## Compare the complete obligation

Begin with data classification and residency, traffic shape, recovery objectives, available operators and budget. The comparison below is the library's original selection aid. Product documentation must supply current region, quota, support and pricing facts for the actual deployment; a product category is not a service guarantee.

| Option | Useful fit | Cost and responsibility to check |
| --- | --- | --- |
| Static hosting/CDN | Public documentation and immutable assets | Build limits, cache rules, domain control and absence of private output |
| Managed application platform | A small team delivering an application | Supported runtimes, networking, backup scope, export and egress |
| Managed functions | Bounded bursty operations | Execution limits, cold starts, concurrency, connection pools and retry behavior |
| VPS/container host | Predictable work with an accountable operator | Patching, certificates, monitoring, backups, restore time and spare capacity |
| Managed Kubernetes | Several workloads with justified scheduling/isolation needs | Cluster and workload policy, upgrades, networking, capacity and incident expertise |

Managed services transfer selected operational tasks; they do not transfer responsibility for application authorization, data classification or recovery evidence. Compare compute, storage, egress, observability, support, paid model calls and human time. Include peak and failed-request/retry costs rather than only an idle monthly estimate.

## Record a hosting decision packet

Name the service owner, failure domains, supported runtime versions, deployment identity and artifact digest. Specify how production is separated from experiments, how secrets arrive, how public ingress is authenticated, and which data stores are private. Check quotas and documented restoration capabilities against the application's RTO/RPO. Account for a provider account lockout as well as a regional outage.

Keep configuration external and infrastructure reproducible. Retain control of the domain and data export format. List provider-specific features and the accepted migration cost; portability is a tradeoff, not a requirement to eliminate every managed service. A platform offering automatic backups still needs an application-level restoration drill.

## Prove the chosen option

Before first production release, deploy an isolated environment and complete a real user journey. Exercise denied access, credential rotation, a failed deployment and data restoration. Use [performance tests](performance-testing.md) to establish sustainable traffic and [security tests](security-testing.md) for ingress, tenancy and identity boundaries. Record the deployed version, relevant platform settings and observed results; a dashboard saying “healthy” is insufficient.

For illustration, compare a managed application/database with one VPS for the same small SaaS. The VPS may have a lower infrastructure bill while requiring an owner for patching and recovery. Choose based on measured cost and the ability to meet the operating contract, not the cheaper headline price. This example is a decision exercise, not a priced or benchmarked reference deployment.

## Exit and recovery

Rehearse export/import using a copy of production-shaped data. Check record counts, business totals, identity mappings, secrets, object storage and worker state. Plan the authoritative writer during cutover, observation window and the conditions for stopping traffic migration. Keep the old path recoverable only while its data remains consistent with the chosen recovery plan.

DNS rollback cannot reverse writes accepted by the new system. After cutover, rollback may require write suspension, reconciliation or forward repair. Test that plan before a high-consequence migration. This library's website uses static hosting; Pages publication does not deploy its local MCP server.

## Related decisions

[Self-hosting](self-hosting.md) · [Scaling](scaling.md) · [Operations](operations.md) · [Performance testing](performance-testing.md) · [Security testing](security-testing.md)

## Primary evidence

[docker-security](https://raw.githubusercontent.com/docker/docs/4d64a8e4f0a59967fc0b391120d54a90e9ccb60d/content/manuals/engine/security/_index.md) · [kubernetes](https://raw.githubusercontent.com/kubernetes/website/bc7f3479bc8b0af48097b155c22c8d58e8e1afe4/content/en/docs/concepts/architecture/_index.md) · [opentofu](https://raw.githubusercontent.com/opentofu/opentofu/ec773ed37be4d07e00d4a2fbb237d0c0fe1ca3ce/README.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml)
