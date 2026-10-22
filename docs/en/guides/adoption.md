---
{
  "id": "adoption",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Adopt the library in a project

## A portable project packet

Copy the templates you need, not the whole library. Fill `project-profile.yaml` with business constraints, ownership, sensitivity, budget, workload, SLO, and recovery assumptions. Reference this library by release or commit and guide IDs; do not silently follow mutable `main` for production policy.

Create a context diagram and the first ADR. Record accepted guidance, justified exceptions, owner, expiry, and compensating checks. Put short project-specific agent instructions in `AGENTS.md`; link details instead of copying a long constitution into every prompt. Use the task packet for each bounded change and the release checklist before shipping.

## Three starting examples

- A personal knowledge site can use static hosting, Git as content history, and a reproducible build. Add private authentication before storing private notes publicly.
- A small SaaS can start with a modular application, managed transactional database, and a bounded worker. Add tenant authorization, payment reconciliation, recovery tests, and an operating owner before accepting real customers.
- A high-traffic platform measures partitions and isolates critical paths. Independent deployments and regional recovery require explicit consistency, on-call, and migration ownership; account count alone is not justification.

## Continuous use

At planning, consult applicable guides. At review, link the decision and evidence. At release, check migration and recovery. At operation, feed measurements and incidents back into ADRs. Upgrade the pinned library through a reviewed PR that explains changed obligations and affected projects. Do not claim compliance merely because a template exists.

## Related decisions

[Decision principles](foundations.md) · [The complete project lifecycle](lifecycle.md) · [Human direction, agent execution](agents.md) · [Governance and unanswered decisions](governance.md)

## Primary evidence

[plugins](https://raw.githubusercontent.com/openai/plugins/main/README.md) · [github-rulesets](https://raw.githubusercontent.com/github/docs/main/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/main/content/en/docs/concepts/observability-primer.md)
