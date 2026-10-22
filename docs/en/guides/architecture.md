---
{
  "id": "architecture",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Choose and connect architectures

## Choose by coupling and responsibility

| Approach | Use when | Main cost and exit signal |
| --- | --- | --- |
| Static site | Content changes more slowly than requests; no server secrets | Build time and content workflow; add a backend for trusted writes |
| Modular monolith | One product/team needs transactions and fast change | Enforce module ownership; extract only a measured bottleneck or independent responsibility |
| Serverless functions | Bursty bounded jobs fit provider limits | Cold starts, quotas, tracing, and lock-in; move sustained or long work to workers |
| Services | Separate teams or workloads need independent release/isolation | Network failure, contracts, consistency, and on-call cost |
| Event-driven system | Delayed work and independent consumers are natural | Duplicate/out-of-order events, replay, schema evolution, and debugging |
| Durable workflow engine | Long-running business steps must resume after failure | Determinism/versioning constraints, operations, and workflow migration |

These are composable choices. A modular monolith can serve a statically rendered frontend, run asynchronous workers, and later extract one domain. Hexagonal/clean architecture governs dependency direction inside a component; it does not require microservices. CQRS separates read/write models when their needs diverge; event sourcing additionally stores events as the source of truth and demands a replay/retention strategy.

## Boundaries

Draw browser, API, worker, database, external providers, and trust boundaries. Each module owns its writes; cross-module access goes through an explicit interface. Keep shared libraries small. A shared database with unrestricted cross-service writes undermines independent ownership.

## Verify and evolve

Test one cross-boundary failure and one contract change. Measure delivery lead time, dependency cycles, transaction conflicts, and recovery effort. Extract a service only when its benefit exceeds deployment, consistency, and support costs. Record how consumers migrate and how the old path is retired; a diagram alone is not an implementation plan.

## Related decisions

[Durability and distributed work](durability.md) · [Frontend architecture and contracts](frontend.md) · [Scale from measurements](scaling.md) · [Hosting and exit strategies](hosting.md)

## Primary evidence

[kubernetes](https://raw.githubusercontent.com/kubernetes/website/main/content/en/docs/concepts/architecture/_index.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/mvcc.sgml) · [durable-workflows](https://raw.githubusercontent.com/temporalio/temporal/main/README.md)
