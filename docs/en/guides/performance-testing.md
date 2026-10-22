---
{
  "id": "performance-testing",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Performance, load, and stress testing

## Choose a failure question

A performance test should answer a project decision: whether a release meets its latency objective, whether a queue recovers after a burst, where capacity becomes insufficient, or whether resource use grows over time. Registered-user counts and a single fast request do not answer those questions.

| Test shape | Use when | Result to examine |
| --- | --- | --- |
| Small smoke run | Validate the workload, fixtures, permissions and measurements before consuming resources | Requests do the intended work; assertions and stop controls function |
| Representative load | Check normal operation and an agreed expected peak after a relevant change | Useful throughput, tail latency, errors and resource use meet the project objective |
| Stress | Examine degradation above the expected workload within a bounded experiment | Admission control, errors, data integrity and recovery behave deliberately |
| Spike | A launch, schedule or external event may increase arrivals abruptly | Queue growth, scaling delay, rejection and recovery after the burst |
| Soak | Leaks, connection churn, expiry or periodic work may accumulate over time | Resource trends and latency remain explainable across the relevant lifecycle |
| Capacity or breakpoint | Planning needs an observed limit for a fixed configuration | The first violated objective, limiting resource, safe headroom and recovery path |

Names vary between tools. Record the actual workload shape and objective so another agent can reproduce the experiment. Stress is not automatically the best next test; a failing smoke run needs diagnosis first.

## Model real work

Derive transaction mix, arrival patterns, payload and dataset sizes, read/write ratio, cache state, tenant skew, background activity, and dependency behavior from measurements or explicit assumptions. Preserve the difference between a business transaction and its component HTTP requests. Explain how the test environment differs from production before extrapolating results.

Choose the scheduling model deliberately. A closed model keeps a population of virtual users that wait for their current iteration before starting the next. When the system slows, offered work can fall. An open arrival-rate model schedules new work independently of completion and better represents independent arrivals. Neither model automatically matches every product. Record think time and distinguish configured rate, actually started work, completed throughput, and dropped iterations.

Ensure the generator, its network, and its credentials are not the bottleneck. Observe generator saturation separately. An overloaded generator that stops issuing work can make the target appear healthy. Warm-up, caches, connection pools, autoscaling and background jobs can change results; include the states that matter instead of hiding them in one aggregate.

## Define limits before running

The agent's test packet must name the owned target, environment, permitted routes and accounts, maximum traffic, concurrency, duration, resource/spending caps, monitoring, cleanup, and operator who can stop the run. Use isolated environments and synthetic data by default. Do not direct stress traffic at production, third-party providers, shared tenants, or paid model endpoints without explicit scoped authorization and provider limits.

Set separate acceptance thresholds and abort conditions. Acceptance measures the desired service behavior; abort conditions protect people, data, shared systems and budget. A planned stress test may exceed its normal latency objective, but it must still stop at its agreed safety boundary. Define how the abort acts on the generator and how outstanding work will be drained or cancelled. A job timeout alone is not a billing ceiling.

Verify how the runner reports failure. For example, k6 records failed checks as metrics; configure thresholds so a failed acceptance condition produces a failing run. Periodic cloud abort evaluation is not instantaneous enforcement of resource or spending limits; provide limits at the service and account boundaries as needed.

Cap autoscaling during a capacity experiment or document its bounded configuration. Otherwise the test may measure spending growth instead of a fixed system's capacity. Use provider sandboxes or controlled substitutes for expensive external side effects and state which limitations that introduces.

## Measure and interpret

Track successful business operations, error categories, p50/p95/p99 latency where the sample size supports them, throughput, concurrency, queue age and depth, connection usage, CPU, memory, storage, and relevant cost. Segment critical routes and tenants; a fast common endpoint can hide a failing checkout path in a global percentile. Include failed and timed-out operations in the analysis, not just successful responses.

Keep raw timing and configuration evidence sufficient to reproduce a meaningful result. Low sample counts make tail estimates unstable; repeat controlled comparisons when uncertainty matters. Correlate observed degradation with resource and dependency measurements before attributing it to a code change. A difference between two uncontrolled environments is not a demonstrated regression.

For soak tests, choose a duration that spans the lifecycle at risk, such as token renewal, scheduled jobs or buffer growth; do not copy a universal number of hours. For capacity tests, report the measured limit under the tested configuration and workload, not a promise about all future users.

## Recovery is part of the experiment

Reduce load and observe whether latency, queues and resource use return to a useful state within the agreed recovery window. Verify data consistency, duplicate effects and delayed jobs. A system that rejects overload safely but never drains its backlog has not demonstrated recovery. Remove fixtures and confirm no scheduled generator or billable resource remains unintentionally active.

Record the result, confidence limits, bottleneck hypothesis, and decision: accept measured headroom, optimize a specific path, change admission policy, or evaluate additional capacity. Retest the changed hypothesis. Keep performance gates proportionate to risk and stable enough to provide useful release feedback.

## Evidence and related decisions

Grafana's k6 documentation explains workload shapes, open/closed scheduling, thresholds and abort controls. The planning, acceptance and recovery policy above is this library's original synthesis; example thresholds and traffic values from vendor documentation are not project requirements.

[Testing strategy](testing-strategy.md) · [Scale from measurements](scaling.md) · [Health and recovery](operations.md) · [Durability](durability.md) · [Quality gates](quality.md)

## Primary evidence

[k6-test-types](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/testing-guides/test-types/_index.md) · [k6-open-vs-closed](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/using-k6/scenarios/concepts/open-vs-closed.md) · [k6-thresholds](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/using-k6/thresholds.md) · [k6-stress-testing](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/testing-guides/test-types/stress-testing.md) · [k6-spike-testing](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/testing-guides/test-types/spike-testing.md) · [k6-soak-testing](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/testing-guides/test-types/soak-testing.md) · [k6-breakpoint-testing](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/testing-guides/test-types/breakpoint-testing.md)
