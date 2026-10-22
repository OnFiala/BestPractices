---
{
  "id": "reference-labs",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Run and interpret the reference projects

## Three executable boundaries

The reference projects are original teaching implementations with self-owned local fixtures. They let agents inspect concrete contracts, deliberately exercise failures and retain measured results without a provider account or paid model call. They are components selected by the six project playbooks, not six finished products or production deployment templates.

| Reference | Actual implementation | Deliberate substitution and limit |
| --- | --- | --- |
| `examples/durable_service` | Loopback HTTP, tenant-bound fixture identity, SQLite transactions, idempotency/version rules, outbox/consumer, child-process crash drills, snapshot restore and bounded overload | Synthetic bearer credentials; local SQLite and one machine; no real payment, identity provider, broker or regional failover |
| `examples/agent_workflow` | Persisted workflow and separate effect ledger, authorization before context, exact-action capability checks, cancellation/budgets and reconciliation | Deterministic fixture model, trusted fixture approval issuer, simulated crash/reopen and synthetic budget units; no real model quality or production authentication |
| `examples/frontend` | Semantic HTML and native modules, URL/local/remote state, request-identity cancellation, safe text rendering and actual Chromium checks | Read-only synthetic API, one observed browser/environment and partial accessibility checks; no production auth, writes or native mobile client |

Each README identifies prerequisites, commands, assumptions, negative oracles, cleanup and omitted production work. Use those contracts when adapting an example; copying code does not adopt its assumptions automatically.

## Execute and retain observations

From the repository root:

```sh
python -m examples.durable_service demo
python -m examples.durable_service drills
python -m examples.durable_service benchmark --operations 120 --concurrency 8 --capacity 2 --delay-ms 10 --seconds 5
python -m examples.agent_workflow demo
python -m examples.agent_workflow evaluate
python -m library.verification delivery durable-service agent-workflow frontend-unit frontend-browser --output reports/reference-checks.json
```

The benchmark starts only its own loopback fixture, accepts bounded local parameters and does not accept a remote target URL. The numbers above define a small teaching experiment; they are not recommended production limits or service objectives. Inspect offered, started, completed, rejected and transport-error counts together with measured latency, test duration and subsequent integrity/recovery. Generator behavior and the closed workload model limit interpretation.

The agent evaluation reports deterministic policy cases separately from its explicitly unrun live-model-quality item. Passing the executed cases is useful evidence for those local rules, not a reason to count the skipped item as successful. The demo's model and approval issuer are clearly named fixtures.

The verifier requires actual executed tests, records runtime versions and the input image, and treats missing, failed or skipped required checks as incomplete. Its browser suite needs Node 22+ and an installed Chromium/Chrome. A controlled-container sandbox opt-in is documented in the frontend README; it applies only to the owned local fixture. Reports are local observations, not authenticated attestations or human approval.

## Check the failure and recovery boundary

For durable writes, compare permitted results and denied side effects. Repeated requests with the same tenant/action/key and payload should replay one result; a conflicting payload must fail. Concurrent version writers need a defined winner/conflict outcome. An outbox entry and business write share the local transaction; consumers must not acknowledge unknown event schemas. Restoring a snapshot loses later local writes and does not undo external effects.

For agent actions, inspect what reaches context before a proposal exists, then what the executor validates independently. An edited action or expired/revoked capability must not execute. After an uncertain effect, inspect the independent receipt and reconcile; a missing or mismatched receipt must remain unresolved rather than triggering blind replay. A cancelled or timed-out run still needs accounting for work already performed.

For the browser, test genuine public controls and transport races. An aborted transport can still resolve a body; request identity must prevent stale completion from replacing current state. Denied or malformed data must not become active markup. Keyboard/focus and narrow layout checks cover specific journeys, not all assistive technologies or devices.

## Move from a reference to a product

Generate a delivery packet, state which pieces are reused and replace each fixture boundary with a reviewed project contract. Add the selected store/provider/identity/client integrations and tests. Re-run negative and recovery cases against those actual boundaries, measure representative workloads, and obtain independent review of deployment and operational ownership. Retain failed and unrun observations. Production release is a separate human decision after project evidence exists.

## Related decisions

[Agent delivery workflow](project-delivery.md) · [Coverage and limits](coverage.md) · [Durability](durability.md) · [Security testing](security-testing.md) · [Performance testing](performance-testing.md)

## Primary evidence

[azure-idempotent-consumer](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/idempotent-consumer.md) · [azure-outbox](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/databases/guide/transactional-out-box-cosmos.md) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [playwright-testing](https://raw.githubusercontent.com/microsoft/playwright/ca7ca36145b84183cf423c2a099bd7e9cd8b1cb3/docs/src/best-practices-js.md) · [k6-open-vs-closed](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/using-k6/scenarios/concepts/open-vs-closed.md)
