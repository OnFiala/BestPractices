---
{
  "id": "architecture",
  "language": "en",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Choose and connect architectures

## Choose by constraints and ownership

Record transaction boundaries, latency and recovery needs, data sensitivity, workload shape and who can operate the system. Compare the simplest viable design with the proposed alternative. The table below is this library's original decision framework; cited pattern documents establish relevant mechanisms and tradeoffs, not a universal ranking.

| Approach | A useful starting condition | Cost and reason to reconsider |
| --- | --- | --- |
| Static site | Public content with no trusted server writes | Build/cache limits; add a protected API for authenticated changes |
| Modular monolith | One product needs coordinated transactions and frequent change | Module dependency discipline; extract only a measured constraint or independently owned capability |
| Functions | Bounded, bursty work fits the provider's execution contract | Cold starts, quotas, connection pressure and retries; reassess sustained or long-running work |
| Services | Independent ownership, release or failure isolation produces a concrete benefit | Network failures, versioned contracts, observability and consistency operations |
| Event-driven work | Work can finish later and consumers have distinct responsibilities | Duplicate/out-of-order delivery, lag, replay and schema evolution |
| Durable workflows | Long-running business steps must survive interruption | Engine constraints, history retention, code upgrades and reconciliation of external effects |

These choices compose. A monolith can serve a static frontend and use a queue without becoming a microservice system. Code-level dependency direction and deployment topology are separate decisions: splitting processes does not by itself create useful domain boundaries.

CQRS separates read and write models; it can begin inside one database. Separate stores add synchronization delay and a stale-read contract. Event sourcing makes the event history authoritative, requiring event evolution, replay and privacy/retention decisions. A queue or audit table alone is not event sourcing. Introduce these patterns selectively when their specific benefit outweighs the added recovery and testing obligations.

## Make boundaries reviewable

For each browser, API, worker, data store and provider connection, record:

| Contract | Evidence the reviewer should see |
| --- | --- |
| Authority | Which principal may perform which action, on whose data |
| Data ownership | Which component can write each invariant; how other components request changes |
| Failure | Timeout, cancellation, retry owner, duplicate handling and user-visible pending/error state |
| Compatibility | Supported producers/consumers, schema version and removal condition |
| Operations | Traces/metrics, support owner, restore/reconciliation procedure and budget |

A shared database can be a deliberate transitional choice. Unrestricted writes from several services make independent ownership and migration harder; document that coupling instead of calling the services independent.

## Prove the change before extraction

For a proposed worker or service, first identify the symptom: queue age, lock contention, deployment coordination or an isolation requirement. Capture a representative baseline and compare a small vertical slice with the existing path. Use [contract and black-box checks](testing-strategy.md), [load and recovery tests](performance-testing.md), and [security tests](security-testing.md) at the new boundary. Include a slow dependency, an old consumer and a repeated request.

A migration plan names data ownership during transition, traffic selection, compatibility and reconciliation. Keep one authoritative writer unless a deliberate conflict-resolution design has been tested. Define the evidence that allows traffic to move, the abort condition and the recovery path after new writes. Rolling traffic back does not automatically undo migrated data.

If the benefit is not demonstrated, keep the simpler topology and the useful internal boundary. Record the result in an ADR so the next agent does not repeat an unsupported redesign.

## Related decisions

[Durability and distributed work](durability.md) · [Frontend architecture](frontend.md) · [Scale from measurements](scaling.md) · [Hosting](hosting.md) · [Testing strategy](testing-strategy.md)

## Primary evidence

[azure-architecture-styles](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/guide/architecture-styles/index.md) · [azure-cqrs](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/cqrs.md) · [azure-event-sourcing](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/event-sourcing.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml) · [durable-workflows](https://raw.githubusercontent.com/temporalio/temporal/e8ee627110a98501103827745aab18aedf312dd0/README.md)
