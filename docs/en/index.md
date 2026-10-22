---
{
  "id": "start",
  "language": "en",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Build systems that can last

A working library for the whole life of software: from the first problem statement to reliable operation, migration, and retirement. Humans own intent and risk. Agents turn bounded decisions into tested changes. English is canonical; Czech, German, and Spanish are maintained with the same guide IDs and revisions.

This library itself is an **agent-maintained decision system**: AI agents research, write, translate, and verify; humans own applicability, rights review, merge, and publication. Recommendations are contextual proposals, not universally certified rules. The engineering explanations are original synthesis; cited documents keep their own licenses and are not reproduced as our content.

## Start with a decision

1. Define the outcome, data sensitivity, operating budget, and acceptable downtime in a project profile.
2. Select the smallest architecture that meets those constraints. A personal tool can still handle sensitive data; a million registered accounts can still have modest concurrency.
3. Capture consequential choices in an architecture decision record (ADR). Link evidence, alternatives, and a reversal plan.
4. Give an agent a small task with acceptance criteria. Require an independent check and human merge.
5. Operate what you build: observe real behavior, test recovery, and revisit assumptions when evidence changes.

## Read by need

The architecture and hosting guides help you choose a shape. Durability, data, security, and frontend explain the contracts inside that shape. GitHub, quality, and agents govern delivery. Operations and maintenance keep both products and this library healthy.

For verification, start with [test selection](guides/testing-strategy.md). It distinguishes the purpose, level, and knowledge available to the tester; black-box does not mean only penetration testing. Use [performance testing](guides/performance-testing.md) for load, stress, spike, soak, and capacity experiments, and [security testing](guides/security-testing.md) for risk-based controls and bounded assessment. Each gives agents selection criteria, evidence requirements, and stop conditions.

Every guide states an applicable context, a decision, tradeoffs, checks, and change signals. Source retrieval is evidence of availability, not proof that a recommendation is correct. This initial edition is proposed guidance awaiting human review; translations also require editorial review. Experimental browser integrations remain explicitly experimental.

Use the language menu to change languages, search to find a concept, and related guides to follow consequences. Clone the repository for offline reading; the website and read-only MCP adapter use the same content. No paid model API is required to read, build, or validate the library.

## Related decisions

[Decision principles](guides/foundations.md) · [The complete project lifecycle](guides/lifecycle.md) · [Choose and connect architectures](guides/architecture.md) · [Adopt the library in a project](guides/adoption.md)

## Primary evidence

[plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md) · [github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md)
