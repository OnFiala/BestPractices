---
{
  "id": "scaling",
  "language": "en",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Scale from measurements

## Describe work, not account counts

Record peak arrival rate, concurrent work, payload sizes, read/write mix, hot tenants or keys, data growth, background jobs and dependency quotas. Define the user journey, service objective, cost envelope and required failure headroom before selecting capacity. A million mostly inactive accounts can be easier to serve than a small set of expensive concurrent jobs.

The escalation order below is a library recommendation, not a guarantee that every workload should take every step. Keep measurements and the rejected alternatives in an ADR.

## Change one constraint at a time

| Observed constraint | Candidate change | Proof and tradeoff |
| --- | --- | --- |
| Slow queries or excessive round trips | Profile, index, bound result sizes, batch carefully | Compare query plans, latency and write cost on representative data |
| Repeated expensive reads | Cache with explicit tenant keys and freshness rules | Test cold start, invalidation and simultaneous misses; measure origin load |
| Work arrives faster than it can finish | Bounded queues/workers, quotas and admission control | Check queue age, fair sharing and recovery; reject predictably before exhaustion |
| Application CPU or independent I/O is saturated | Add stateless replicas | Recalculate total database connections and downstream request rate |
| Read traffic dominates | Replica or query projection | Define lag and read-after-write behavior; test stale and unavailable reads |
| Measured storage/write/routing limit remains | Partition or isolate a workload | Prove routing, hot-key behavior, rebalancing, migration and cross-partition semantics |

Do not assume a cache makes authorization safe: scope keys and invalidate permissions appropriately. A miss storm can overload the origin. Adding application replicas can make a database outage worse when every replica opens a large pool or retries the same work.

## Specify the experiment before generating traffic

Use the [performance-testing guide](performance-testing.md) to distinguish baseline load, burst, stress, endurance and recovery experiments. Define the target environment, authorization, synthetic dataset, traffic distribution, stop conditions and cost limit. Test denied and expensive operations as well as the common path. Keep request-level results, resource metrics, queue age and a versioned workload description.

Measure successful throughput, p95/p99 latency, errors and rejected work separately. A system that reports excellent latency only by dropping most requests has not met its objective. Include one slow dependency and observe whether it consumes all concurrency or causes retry amplification. After reducing traffic, confirm that queues drain and service objectives recover without manual restart.

As a rough check in a stable system, average in-flight work is average arrival rate multiplied by average time within the same measured boundary. It is not a tail-latency estimate or a capacity promise; an overloaded growing queue breaks the steady-state assumption. Validate any estimate with the real distribution and failure mode.

## Decide and reverse

Scale when sustained measurements or a justified forecast threaten the agreed objective or failure headroom. Record the trigger, expected gain, operating cost, change owner and rollback/forward-repair plan. Autoscaling needs bounded maximums, startup time, dependency capacity and budget controls. It cannot repair an inefficient transaction or guarantee availability.

Multi-region writes and sharding add routing and consistency decisions. Introduce them only after testing failover, conflict or reconciliation behavior and migration on representative data. The provider-specific partitioning source below illustrates those obligations; its product limits are not universal limits for another database.

## Related decisions

[Performance testing](performance-testing.md) · [Hosting](hosting.md) · [Data](data.md) · [Operations](operations.md) · [Architecture](architecture.md)

## Primary evidence

[observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md) · [azure-cache-aside](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/cache-aside-content.md) · [azure-data-partitioning](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/best-practices/data-partitioning-strategies-content.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml)
