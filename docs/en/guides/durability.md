---
{
  "id": "durability",
  "language": "en",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Durability and distributed work

## Define what must survive

Separate stored-data durability, service availability and resumable work. A replica is not a backup, and successful message delivery does not prove exactly-once business effects. Agree the accepted data-loss window (RPO), recovery time (RTO) and externally visible reconciliation rules for each capability. The following execution and test contract is this library's original synthesis; provider behavior must be verified for the deployed version.

## Give every effect a state model

A durable operation needs a stable ID, authenticated owner, validated payload, current state and an observable outcome. Scope idempotency keys to tenant and business action. Define what happens when a key is reused with a different payload, when a request is still running, and when records expire. Keep deduplication information at least as long as the supported retry/replay horizon, or require a separate authorized reconciliation process for older work.

For a local business transition, persist its result and uniqueness guard atomically. When publication must reflect a committed transition, a transactional outbox can store the business change and event together. A relay can publish twice after losing its acknowledgement; consumer deduplication must therefore be part of the consumer's own durable write. This does not make unrelated external calls transactional.

Classify failures before retrying. Validation and denied authorization need a final response; transient failures may allow bounded retry. Give one layer responsibility for the total deadline and retry budget, and account for SDK retries underneath it. Backoff and jitter reduce synchronized retry pressure; they do not justify retrying an unsafe effect. Cancellation after an external request was sent can leave an unknown outcome that needs reconciliation.

## Worked failure sequence

Consider an order with a payment provider and a downstream fulfillment event:

| Interruption | Required observable behavior |
| --- | --- |
| Before the order/outbox transaction commits | Neither becomes visible; a retry can start safely |
| After commit, before event publication | A relay eventually finds the pending event; no order disappears |
| After publication, before relay acknowledgement | Duplicate delivery produces one intended consumer transition |
| After payment succeeds, before the response arrives | Reuse the provider's supported operation identity or query/reconcile its state; do not create a new charge blindly |
| During a worker upgrade | In-flight work resumes under an explicitly compatible state/version contract or is routed to reconciliation |

These are acceptance requirements, not evidence that any deployed system has passed them. In staging, inject each interruption with controlled provider behavior, repeat the request, then inspect durable state and provider records. Check both successful recovery and unresolved states that require a human. Follow the [testing strategy](testing-strategy.md) for the test oracle and evidence packet.

## Operate replay and recovery

Quarantine poison messages with an owner and a reason. Bound retry/replay volume and authorize replay separately from ordinary reading. An operator must know which schema, ordering scope and deduplication window apply. Compensation is a new business action; refunds, notifications and physical fulfillment may not be reversible.

Restore into an isolated environment, reconcile business totals and external effects, then resume work deliberately. Test recovery while the queue is backlogged and dependencies are slow using the [performance test plan](performance-testing.md). A durable workflow engine is justified when it reduces demonstrated orchestration complexity; a transactional job table may suffice for a simpler process with acceptable manual recovery. Neither removes the need for backups, ownership or compatibility tests.

## Related decisions

[Data and migrations](data.md) · [Health and recovery](operations.md) · [Architecture choices](architecture.md) · [Testing strategy](testing-strategy.md)

## Primary evidence

[postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [durable-workflows](https://raw.githubusercontent.com/temporalio/temporal/e8ee627110a98501103827745aab18aedf312dd0/README.md) · [azure-retry](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/retry-content.md) · [azure-cqrs](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/cqrs.md) · [azure-outbox](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/databases/guide/transactional-out-box-cosmos.md) · [azure-idempotent-consumer](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/idempotent-consumer.md)
