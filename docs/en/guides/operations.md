---
{
  "id": "operations",
  "language": "en",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Health, recovery, and cost

## Observe the user outcome

Choose a service-level indicator (SLI) for a meaningful journey, such as successful completion within a latency bound. Define its numerator, denominator, observation window and exclusions, then agree the service-level objective (SLO) with the owner. Include failed and rejected work where the contract requires it; a fast error is not a successful transaction.

An error budget expresses the permitted shortfall over that window. For illustration, a request-based objective of 99.9% across 100,000 eligible requests permits 100 requests outside the objective; this is arithmetic, not a recommended target. Use observed burn and business impact to adjust release risk. Define the response policy before an incident rather than treating an exhausted budget as a dashboard color.

This operating model is the library's synthesis. The cited observability and health-endpoint material supports the measurement mechanisms; review frequency and escalation thresholds remain project decisions.

## Separate health signals

| Signal | Purpose and limitation |
| --- | --- |
| Startup | Allow initialization to finish within an explicit bound |
| Liveness | Detect a process that cannot make progress; restarting must be a useful response |
| Readiness | Decide whether an instance should receive particular traffic |
| Synthetic journey | Exercise user-visible behavior through a controlled public interface |
| Service metrics/traces | Explain outcomes, saturation and dependency contribution over time |

Do not make every transient dependency failure fail liveness and restart healthy processes. Deep readiness checks can also remove all instances during a shared dependency outage; define degraded behavior and dependency-specific limits. Health probes must not exhaust the resources they measure. Protect detailed diagnostics and avoid triggering real payments or messages from probes.

Use structured logs, metrics and traces with correlation IDs, bounded label cardinality and sensitive-data redaction. Alert on actionable symptoms or sustained budget burn, with severity, owner, runbook and escalation. Validate that the alert reaches somebody who can respond. A dashboard or an HTTP 200 alone does not prove availability.

## Run an incident and recovery drill

Assign an incident lead, establish user impact, stabilize the system, preserve necessary evidence and communicate uncertainty. Disable risky retries or agent actions when they amplify damage. Prefer a known safe recovery action to an untested emergency redesign. After restoration, reconcile durable work and provider effects before resuming automation.

In an isolated environment, restore a backup, revoke/rotate credentials and simulate an unavailable provider. Measure the recovery interval and lost-data window, then verify a real user journey and business invariants. Use [black-box checks](testing-strategy.md) for observable behavior and [performance/recovery tests](performance-testing.md) for backlog drainage after saturation. Record the actual results, artifact versions and remaining manual steps.

After an incident, record contributing conditions and actions with owners and deadlines. Add a regression test when it can demonstrate the repaired behavior. Preserve useful operational learning without publishing personal data or credentials.

## Keep ownership and spending visible

Measure cost per useful transaction and agent task, including retries, tokens, egress and observability. Define an alert and an enforced stop or degradation mechanism; an email warning alone is not a spending cap. Review unresolved alerts, source/dependency changes and spending regularly. Review objectives, capacity and restore evidence after material changes; choose a recurring cadence that the owner can sustain.

A system is healthy when its owners can demonstrate behavior, recovery and a sustainable operating obligation. More replicas cannot replace an owner, and no single test run guarantees future reliability.

## Related decisions

[Durability](durability.md) · [Scaling](scaling.md) · [Lifecycle](lifecycle.md) · [Testing strategy](testing-strategy.md) · [Performance testing](performance-testing.md)

## Primary evidence

[observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [azure-health-endpoints](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/health-endpoint-monitoring.md)
