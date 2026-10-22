---
{
  "id": "scaling",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Scale from measurements

## Measure before distributing

Registered users are not a capacity measure. Record concurrent requests, peak arrival rate, payload sizes, read/write mix, tenant skew, latency percentiles, and background work. Define the service objective and cost envelope before choosing capacity.

## Escalation ladder

1. Profile representative traffic; fix expensive queries, missing indexes, unbounded lists, and excess round trips.
2. Cache only with explicit freshness, invalidation, tenant isolation, and stampede behavior. Measure hit rate and origin load.
3. Add bounded workers, backpressure, per-tenant quotas, and admission control. Reject safely before overload collapses dependencies.
4. Replicate stateless application processes; move sessions and files out of local memory/disk where appropriate. Size database connection pools across all replicas.
5. Consider read replicas with an explicit stale-read contract. Partition data only after measuring a write/storage limit and designing routing, rebalancing, and cross-partition operations.

## Verify

Load-test a realistic distribution and a burst, including a slow dependency and recovery after saturation. Track throughput, p95/p99 latency, errors, queue age, saturation, and cost per useful operation. Estimate concurrency using arrival rate × service time, then validate the model under load.

Scale when objectives fail persistently or a measured forecast removes required headroom. Record a baseline and rollback. Autoscaling is bounded by downstream capacity, startup time, quotas, and budget; it cannot repair an inefficient transaction or guarantee availability.

## Related decisions

[Hosting and exit strategies](hosting.md) · [Data, contracts, and migrations](data.md) · [Health, recovery, and cost](operations.md) · [Choose and connect architectures](architecture.md)

## Primary evidence

[observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/main/content/en/docs/concepts/observability-primer.md) · [kubernetes](https://raw.githubusercontent.com/kubernetes/website/main/content/en/docs/concepts/architecture/_index.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/mvcc.sgml)
