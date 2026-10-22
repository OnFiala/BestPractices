---
{
  "id": "playbook-agent-automation",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Deliver bounded agent automation

## Fit and minimum control plane

Use this profile when a model proposes or coordinates actions with durable consequences: changing records, preparing releases, or operating external tools. Record allowed destinations, task owner, maximum scope, approval requirements, retry policy, and time/token/cost limits. A deterministic workflow is preferable when the decision sequence is already known. Start with one bounded worker and a durable run ledger; add model reasoning only where it improves a measured task outcome. This agent-authored playbook is proposed local synthesis.

Do not start with a fleet of agents. Separate workers, queues, or identities when measurements show priority starvation, incompatible tool permissions, or independently owned reliability obligations. Delegation adds coordination, credential, and total-budget costs. A subtask inherits a narrower capability and budget, never new authority merely because another agent requested it.

## Repository, contracts, and persistent state

Separate `planner/`, `policy/`, `tool_gateway/`, `ledger/`, `reconciliation/`, and `evaluation/`. The planner proposes typed actions. The policy component independently checks actor, task, tool, exact destination, parameters, and scope. The tool gateway owns credentials and enforces the final decision. Tool output and retrieved text are untrusted observations; they cannot edit policy, renew approval, or select an unauthorized destination.

Persist task identity, action fingerprint, approval identity/expiry, attempts, budget reservations, result references, and state transitions. Distinguish planned, awaiting approval, authorized, executing, succeeded, failed, cancelled, and uncertain effects. For approval-required work, bind approval to actor and exact action; consume or reserve it atomically so concurrent workers cannot spend it twice. Parameter changes require a new decision. An approval flag inside model text is not a trusted record.

A crash after an external effect but before acknowledgement creates uncertainty. Use a provider idempotency key or a provider lookup keyed by stable operation identity when supported. Otherwise stop and reconcile with an authorized operator; do not relabel uncertainty as failure and retry blindly. Ledger durability does not make an arbitrary external action exactly once.

## Sequence implementation and review

1. The discovery role inventories each tool, read/write effect, destination, required authorization, recovery possibility, and owner. The human resolves irreversible action policy and explicit approval boundaries.
2. Implementation first completes a deterministic run against local fixtures, including persisted state, denial, cancellation, restart, and reconciliation. Add the model planner behind those boundaries and define its typed contract.
3. The verifier attacks capability and approval edges, duplicates work, and interrupts execution. The release role prepares scoped identities, a kill switch, monitoring, and an operator runbook before any real connector is enabled.

Deliver the task profile, capability matrix, state-machine ADR, tool schemas, exact-action approval examples, run/effect ledgers, observed test results, budget model, reconciliation instructions, and named escalation owner. `examples/agent_workflow` is a local reference for studying this boundary. Connecting a real tool still needs its authentication, destination restrictions, approval policy, and effect-recovery contract; a fixture run grants none of them.

## Tests with independent effect oracles

Use unit tests for policy and state transitions, persistence integration tests for restart/concurrency, and end-to-end tests against isolated tool destinations. Keep a separate effect ledger owned by the test fixture so the model's narrative cannot establish success. Duplicate the same task across workers: inspect both run records and actual effects. One intended effect or an explicit unresolved state is acceptable under the declared contract; silent duplicates are not.

Expire approval, replace its actor, modify an amount or destination, and replay a consumed approval. The external tool must not be called. Supply retrieved text claiming administrator permission and a forged tool response requesting a new destination. The gateway must still enforce the original capability. Revoke tool access between planning and execution to ensure policy is checked at the effect boundary.

Crash after the fixture records success but before the worker stores acknowledgement. Restart must reconcile or hold the action, not automatically repeat it. Exhaust run and delegated budgets and cancel a queued task; no additional work may be scheduled, while in-flight effects must be tracked to their eventual or uncertain outcome. Test queues under an agreed bounded workload and observe starvation, retry amplification, and operator backlog. Preserve failed, skipped, and unrun cases rather than treating a completed model conversation as a pass.

## Release, recover, and retire

Introduce connectors one at a time with reviewed scopes and bounded rollout targets. Version tool schemas and ledger migrations compatibly so existing runs remain interpretable; drain or explicitly migrate runs before removing old handlers. Application rollback does not reverse tool effects or renew approvals. On an incident, stop dispatch, revoke compromised capabilities, retain protected audit evidence, and reconcile outstanding operations before resuming authorized work.

Observe denied actions, stale approvals, uncertain-effect age, reconciliation backlog, task success, human correction, and spend per accepted outcome. Budget model calls, tool fees, retries, ledger storage, and operator time. Production gaps include real identity, protected approval storage, credential isolation, audit retention, provider guarantees, and on-call response. Retirement stops intake, settles or escalates pending effects, exports required evidence, revokes all connectors and schedules, and deletes sensitive run context under the agreed retention policy.

## Continue with related decisions

[Agents](agents.md) · [Durability](durability.md) · [Integrations](integrations.md) · [Security testing](security-testing.md)

## Primary evidence

[owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [azure-idempotent-consumer](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/idempotent-consumer.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md)
