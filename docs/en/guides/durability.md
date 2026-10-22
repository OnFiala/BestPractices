---
{
  "id": "durability",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Durability and distributed work

## Define what must survive

Separate persistence of data, availability of a service, and resumability of work. A replica is not a backup; a queue is not proof of exactly-once business effects. Define the accepted data-loss window (RPO) and recovery time (RTO) per business capability. These are business decisions, not properties inherited from a tool name.

## Reliable execution

- Give an operation a stable idempotency key scoped to its tenant and business action. Store the result or state transition with a uniqueness constraint; define expiry and payload mismatch behavior.
- Bound timeouts and retries. Retry only eligible failures with exponential backoff, jitter, and a total deadline; permanent validation errors go to an explicit failure path.
- Commit business state and an outbox entry in one transaction when a later event must reflect that state. A relay may publish duplicates; consumers deduplicate and handle ordering within a documented scope.
- Persist progress for long work. Record cancellation, compensation, and manual reconciliation. Compensation is a new business action, not guaranteed reversal of external side effects.
- Quarantine poison messages; make replay authorized, observable, bounded, and safe for duplicates. Define schema compatibility and deduplication retention.

## Worked failure

An order is committed, but the process crashes before publishing its event. An outbox relay resumes publishing. If payment succeeds but its response is lost, reuse the provider's supported idempotency mechanism and reconcile provider state before retrying. A local key alone cannot make an external payment exactly once.

## Verify and simplify

Crash the worker before and after each durable boundary; deliver a message twice and out of order. Restore into an isolated environment and reconcile totals. Adopt a workflow engine when persisted orchestration reduces proven failure complexity, and test code upgrades against in-flight work. If the business can tolerate manual retry, a transactional job table may be sufficient.

## Related decisions

[Data, contracts, and migrations](data.md) · [Health, recovery, and cost](operations.md) · [Choose and connect architectures](architecture.md)

## Primary evidence

[postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/mvcc.sgml) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml) · [durable-workflows](https://raw.githubusercontent.com/temporalio/temporal/main/README.md)
