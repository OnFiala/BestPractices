---
{
  "id": "start",
  "language": "en",
  "revision": 3,
  "translation_revision": 3,
  "reviewed_on": "2026-10-22"
}
---
# Build systems that can last

A working library for the whole life of software: from the first problem statement to reliable operation, migration, and retirement. Humans own intent and risk. Agents turn bounded decisions into tested changes. English is canonical; Czech, German, and Spanish are maintained with the same guide IDs and revisions.

This library itself is an **agent-maintained decision system**: AI agents research, write, translate, and verify; humans own applicability, rights review, merge, and publication. Recommendations are contextual proposals, not universally certified rules. The engineering explanations are original synthesis; cited documents keep their own licenses and are not reproduced as our content.

## I have a project: where do I start?

Use this library to give an agent a clear task, choose a suitable approach and
review the result. It provides guidance, a plan and evidence checks. Your agent
builds the actual product in your development environment.

1. Read [adoption](guides/adoption.md): choose the JSON delivery profile for the
   tools and optionally a YAML brief for richer decisions.
2. Follow [your first evidence gate](guides/first-project.md): create one actual
   output, have it reviewed and see what remains blocked. No model API is required.
3. Choose your project below, then follow [the delivery workflow](guides/project-delivery.md).

| What are you building? | Start here |
| --- | --- |
| Public website | [Public website](guides/playbook-public-website.md) |
| SaaS | [SaaS](guides/playbook-saas.md) |
| Internal operations tool | [Internal tool](guides/playbook-internal-tool.md) |
| AI application | [AI application](guides/playbook-ai-application.md) |
| Agent automation | [Agent automation](guides/playbook-agent-automation.md) |
| Backend and mobile clients | [Mobile backend](guides/playbook-mobile-backend.md) |

## Give your agent its first task

Replace the bracketed values and give this to an agent that can read your project
and a trusted local checkout of this library. No plugin or MCP installation is needed.

```text
Work in [target project]. Use [BestPractices checkout] as a reference.
Read the target project's instructions, then the library's
plugins/bestpractices/skills/project-delivery/SKILL.md and the matching playbook.
Outcome: [observable result]. Constraints: [data, budget, permitted effects].
Record the library revision. Create a JSON delivery profile using actual
requirements and the target Git revision; leave unknowns explicit.
Run the planner and take the first unmet gate. Produce its actual artifact,
perform a relevant check and obtain independent review when available.
Do not invent results or reviewers. Report the evidence and remaining blockers.
Work locally; do not deploy or modify the reference library.
```

A **gate** is a checkpoint with required outputs. An **artifact** is a document,
code change or report. **Evidence** describes an actual inspection or test of that
output. Creating a plan does not implement the project or authorize a release.
For what is demonstrated locally and what still needs project-specific proof,
read [coverage and limits](guides/coverage.md).

## Read by need

The architecture and hosting guides help you choose a shape. Durability, data, security, and frontend explain the contracts inside that shape. GitHub, quality, and agents govern delivery. Operations and maintenance keep both products and this library healthy.

For verification, start with [test selection](guides/testing-strategy.md). It distinguishes the purpose, level, and knowledge available to the tester; black-box does not mean only penetration testing. Use [performance testing](guides/performance-testing.md) for load, stress, spike, soak, and capacity experiments, and [security testing](guides/security-testing.md) for risk-based controls and bounded assessment. Each gives agents selection criteria, evidence requirements, and stop conditions.

Every guide states an applicable context, a decision, tradeoffs, checks, and change signals. Source retrieval is evidence of availability, not proof that a recommendation is correct. This initial edition is proposed guidance awaiting human review; translations also require editorial review. Experimental browser integrations remain explicitly experimental.

Use the language menu to change languages, search to find a concept, and related guides to follow consequences. Clone the repository for offline reading; the website and read-only MCP adapter use the same content. No paid model API is required to read, build, or validate the library.

## Related decisions

[Decision principles](guides/foundations.md) · [The complete project lifecycle](guides/lifecycle.md) · [Choose and connect architectures](guides/architecture.md) · [Adopt the library in a project](guides/adoption.md)

## Primary evidence

[plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md) · [github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md)
