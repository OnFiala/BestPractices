---
{
  "id": "operations",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Health, recovery, and cost

## Observe user outcomes

Define an SLI from user-visible success or latency and an SLO over a stated window. Choose targets from business needs and measured capability; do not copy a fashionable percentage. An error budget informs release risk, not permission to ignore incidents. Separate readiness from liveness so a temporary dependency failure does not cause restart storms.

Use structured logs, metrics, and traces with correlation IDs; constrain cardinality and redact personal data. Alert on actionable symptoms and sustained budget burn, with owner, severity, runbook, and escalation. Dashboards are not a substitute for alerts. Measure cost per useful transaction and agent task, including retries and tokens.

## Response and recovery

Assign incident command, stabilize impact, preserve evidence, communicate, and restore service. Follow with a blameless account, contributing factors, and owned corrective actions. Run backup restoration, credential rotation, and provider-outage drills. Document the last successful restore date and measured RTO/RPO.

## Review cadence

Weekly: unresolved alerts, source drift, dependency risk, and spending anomalies. Monthly: service objectives, restore evidence, ownership, and capacity. Quarterly or after major change: threat model, disaster recovery, architecture decisions, and retirement candidates. These are initial cadences to adapt, not universal standards. A system is healthy when owners can demonstrate its behavior and recovery, not merely when all processes are running.

## Related decisions

[Durability and distributed work](durability.md) · [Scale from measurements](scaling.md) · [The complete project lifecycle](lifecycle.md)

## Primary evidence

[observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/main/content/en/docs/concepts/observability-primer.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml)
