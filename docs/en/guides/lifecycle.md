---
{
  "id": "lifecycle",
  "language": "en",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# The complete project lifecycle

## Use evidence to leave each stage

The stages below are this library's proposed operating model. Their depth changes with impact and ownership; the names are not an external certification. A personal script may use one short record, while a high-consequence service needs independent domain and security evidence.

| Stage | Required artifact | Exit evidence |
| --- | --- | --- |
| Discover | Problem brief, stakeholder and data map | Measurable user outcome, explicit non-goals and accountable owner |
| Design | Project profile, context diagram, ADR and threat model | Human acceptance of constraints, budget and recovery objectives |
| Plan | Small backlog and test plan | Each task has scope, owner, failure cases and stop conditions |
| Build | Code, migrations, tests and updated explanation | Reproducible checks and reviewer-visible diff |
| Release | Versioned artifact, rollout and recovery plan | Staging acceptance, migration/restore evidence and human approval |
| Operate | Runbook, service measurements and cost ownership | Objectives measured, alerts actionable and recovery exercised |
| Evolve | Incident learning and migration/deprecation record | Supported consumers migrate before removal |
| Retire | Export/deletion and access-revocation plan | Retention obligations met, external integrations closed and billing checked |

An artifact earns its place by supporting a decision or action. A generated document that nobody can use is not evidence of readiness.

## Make testing a continuing activity

During discovery, define what would show the user outcome is not met. During design, identify invariants and trust boundaries that deserve stronger tests. Before an agent writes code, establish acceptance examples and the expected failure behavior; use the [testing strategy](testing-strategy.md) to select the smallest useful set.

At implementation, run focused checks for the changed boundary. At integration/release, verify compatibility, denied actions and critical journeys through public interfaces. Use [performance testing](performance-testing.md) before capacity-sensitive releases and planned migrations, with explicit limits and authorization. Apply [security testing](security-testing.md) when identity, data sensitivity, external inputs, dependencies or tool authority change. Operations contributes restore drills, incident regressions and actual workload observations back to the plan.

A green build does not close an unmet acceptance criterion. Record failed, skipped and unrun checks separately, with a responsible owner for unresolved risk. Approval refers to the tested artifact and context; a later meaningful change needs renewed review.

## Human and agent responsibilities

The human chooses value, priority, acceptable risk, architecture direction and release authority. Agents investigate, draft, implement, test and report uncertainty within their assigned capabilities. Separate implementation and verification roles when consequence warrants it; several agents repeating the same assumption are not independent evidence.

Keep decisions, run IDs, artifact versions and recovery information in the repository rather than only in a chat. A bounded task ends with its actual result and unresolved questions, including why a proposed design was rejected. Never mark an unexecuted test or generated review checklist as human approval.

## Change course and close the system

Demonstrate one vertical journey, including error and denied-access paths, before expanding features. If the outcome cannot be measured, revisit discovery. If ownership or operating cost is unsustainable, simplify the architecture rather than adding unattended automation.

Plan retirement at creation: how do users export data, which records must be retained, and how are credentials and delegated agent access revoked? Test the export and closure path before it becomes urgent. Retire scheduled jobs, provider resources and recovery copies according to the agreed retention policy; deleting the application repository is not a complete shutdown.

## Related decisions

[Testing strategy](testing-strategy.md) · [Quality gates](quality.md) · [Operations](operations.md) · [Agents](agents.md) · [Adoption](adoption.md)

## Primary evidence

[github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml)
