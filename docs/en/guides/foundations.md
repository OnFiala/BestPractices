---
{
  "id": "foundations",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Decision principles

## Context and default

Durable architecture means that change, failure, and loss of individual knowledge are survivable. It is not a promise that one stack lasts forever. Start with explicit boundaries, a small dependency surface, and an owner for every operational obligation. Prefer reversible decisions until stronger evidence justifies commitment.

## Project profiles

| Profile | Starting point | Obligations |
| --- | --- | --- |
| Personal or exploratory | Static site or one process, managed storage if needed | Reproducible setup, secrets hygiene, export and restore |
| Product with real users | Modular application, managed database, background worker when needed | Service objectives, recovery test, deployment rollback, support owner |
| High traffic or many teams | Measured partitioning, explicit contracts, capacity planning | On-call coverage, load testing, isolation and migration plans |
| High consequence | Any scale, including one user | Threat model, auditability, retention, legal and domain review |

Profiles describe constraints, not a maturity competition. A regulated small service may need stronger controls than a large public catalog. Record what you deliberately defer and the signal that will make it necessary.

## Decision record

Every consequential choice names the problem, constraints, options, evidence, owner, expected costs, verification, and escape route. Separate a fact from an assumption and a local policy from an external standard. Set a review date and an observable trigger, such as sustained queue age beyond the agreed objective.

## Verify and revisit

A new contributor must reproduce the development workflow, trace a user action to its data, and recover from a failed release. If only the original author or model session can explain the system, improve documentation and boundaries before adding components. Revisit decisions after incidents, material cost changes, product pivots, or changed legal obligations.

## Related decisions

[Choose and connect architectures](architecture.md) · [Scale from measurements](scaling.md) · [Governance and unanswered decisions](governance.md)

## Primary evidence

[owasp](https://raw.githubusercontent.com/OWASP/ASVS/master/README.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/main/content/en/docs/concepts/observability-primer.md) · [github-rulesets](https://raw.githubusercontent.com/github/docs/main/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md)
