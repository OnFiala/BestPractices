---
{
  "id": "start",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Build systems that can last

A working library for the whole life of software: from the first problem statement to reliable operation, migration, and retirement. Humans own intent and risk. Agents turn bounded decisions into tested changes. English is canonical; Czech, German, and Spanish are maintained with the same guide IDs and revisions.

## Start with a decision

1. Define the outcome, data sensitivity, operating budget, and acceptable downtime in a project profile.
2. Select the smallest architecture that meets those constraints. A personal tool can still handle sensitive data; a million registered accounts can still have modest concurrency.
3. Capture consequential choices in an architecture decision record (ADR). Link evidence, alternatives, and a reversal plan.
4. Give an agent a small task with acceptance criteria. Require an independent check and human merge.
5. Operate what you build: observe real behavior, test recovery, and revisit assumptions when evidence changes.

## Read by need

The architecture and hosting guides help you choose a shape. Durability, data, security, and frontend explain the contracts inside that shape. GitHub, quality, and agents govern delivery. Operations and maintenance keep both products and this library healthy.

Every guide states an applicable context, a decision, tradeoffs, checks, and change signals. Source retrieval is evidence of availability, not proof that a recommendation is correct. This initial edition is proposed guidance awaiting human review; translations also require editorial review. Experimental browser integrations remain explicitly experimental.

Use the language menu to change languages, search to find a concept, and related guides to follow consequences. Clone the repository for offline reading; the website and read-only MCP adapter use the same content. No paid model API is required to read, build, or validate the library.

## Related decisions

[Decision principles](guides/foundations.md) · [The complete project lifecycle](guides/lifecycle.md) · [Choose and connect architectures](guides/architecture.md) · [Adopt the library in a project](guides/adoption.md)

## Primary evidence

[plugins](https://raw.githubusercontent.com/openai/plugins/main/README.md) · [github-rulesets](https://raw.githubusercontent.com/github/docs/main/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/main/content/en/docs/concepts/observability-primer.md)
