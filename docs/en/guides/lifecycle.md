---
{
  "id": "lifecycle",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# The complete project lifecycle

## A sequence with exit criteria

| Stage | Required artifact | Exit evidence |
| --- | --- | --- |
| Discover | Problem brief, stakeholder and data map | A measurable user outcome and explicit non-goals |
| Design | Project profile, context diagram, first ADR, threat model | Constraints and recovery objectives accepted by a human |
| Plan | Small backlog, dependency map, acceptance examples | Each task has an owner, scope, tests, and stop conditions |
| Build | Code, migrations, tests, updated explanations | Reproducible checks and reviewer-visible diff |
| Release | Version, release notes, rollout and rollback plan | Staging smoke test, backup readiness, approval |
| Operate | Runbook, dashboards, support and cost ownership | Service objectives measured and recovery exercised |
| Evolve | Incident learning, deprecation and migration records | Consumers migrate before removal |
| Retire | Data export/deletion and access-revocation plan | Retention obligations met; billing and credentials closed |

The same gates apply at different depth. A personal script may use one short document; a high-consequence system needs stronger independent evidence. Avoid creating documents nobody uses: each artifact must support an actual decision or operational action.

## Human and agent contract

The human chooses value, priorities, risk tolerance, and release authority. The agent investigates, proposes, implements, tests, and reports uncertainty. A task ends with evidence, not a claim of completion. Record assumptions in the repository rather than relying on chat history.

## Verify and change course

Demonstrate one vertical user journey before expanding features. Include errors, denied access, empty state, and recovery. If the intended outcome cannot be measured, return to discovery. If operations exceed the budget or ownership capacity, simplify the design before adding more automation. Retirement is planned at creation: know how users leave and retrieve their data.

## Related decisions

[Quality gates that prove behavior](quality.md) · [Health, recovery, and cost](operations.md) · [Human direction, agent execution](agents.md) · [Adopt the library in a project](adoption.md)

## Primary evidence

[github-rulesets](https://raw.githubusercontent.com/github/docs/main/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/main/content/en/docs/concepts/observability-primer.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml)
