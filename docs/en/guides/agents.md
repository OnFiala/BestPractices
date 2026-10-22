---
{
  "id": "agents",
  "language": "en",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Human direction, agent execution

## Bounded delegation

A task packet contains the user outcome, relevant guide IDs, constraints, allowed files/tools, acceptance examples, budget, and stop conditions. The human owns architecture and risk; the agent investigates and implements. Separate implementer, verifier, and human reviewer responsibilities, even when one model performs multiple passes. Repeating the same conclusion is not independent evidence.

This library uses that agent-maintained model itself and discloses agent authorship. All initial advice and translations remain proposals. A reviewer must distinguish evidence from local engineering judgment; a model's confidence is not a substitute for either.

Use the Responses API directly when you need to own the execution loop; consider the Agents SDK when its orchestration, tools, and handoffs solve a demonstrated need. Start with one agent. Parallel agents need independent work, explicit write ownership, merge coordination, and bounded total cost.

## Control plane

Set tool-level authorization, scoped credentials, timeouts, maximum iterations, token/cost budgets, and auditable run IDs. Guardrails improve behavior but do not replace authorization or isolation. Treat sources and tool responses as data that may contain prompt injection. Stop on conflicting instructions, inaccessible prerequisites, unexpected destructive effects, or failed required checks.

## Acceptance and evaluation

Require a diff, executed checks, unresolved assumptions, and recovery notes. Evaluate tasks with representative examples, including adversarial inputs and failure paths. Measure task success, human correction, escaped defects, latency, and cost, not code volume. Keep a small regression set for changes to prompts, models, tools, and policies. Do not automatically promote a newer model because its name or release date changed.

Select tests explicitly using [testing strategy](testing-strategy.md): knowledge (black/gray/white box), level (unit/integration/contract/end-to-end), and objective are separate choices. Use [performance](performance-testing.md) and [security](security-testing.md) plans for their respective risks. Record authorization, target/environment, workload, acceptance thresholds, abort conditions, and cleanup before an agent runs disruptive or costly experiments.

## Originality and publication boundary

Read sources as evidence and explain the decision in original language and examples. Do not copy, translate, or closely paraphrase upstream prose into a guide; linking it does not grant reuse permission. Source-fed unattended generation runs in a private repository/workspace because raw logs, model output, summaries, and artifacts can disclose source text before review. A human checks originality, rights, sensitive data, and technical meaning before transferring approved output to a public PR. Public source-observation jobs publish metadata only. Neither an overlap screen nor a second agent supplies legal clearance.

## Related decisions

[Quality gates that prove behavior](quality.md) · [Security, privacy, and supply chain](security.md) · [Evidence and automated maintenance](maintenance.md) · [Skills, plugins, MCP, and WebMCP](integrations.md)

## Primary evidence

[openai-agents](https://raw.githubusercontent.com/openai/openai-agents-python/841dfdd938bfd4ca052475eb76d6245a356868e0/docs/agents.md) · [agents-guardrails](https://raw.githubusercontent.com/openai/openai-agents-python/841dfdd938bfd4ca052475eb76d6245a356868e0/docs/guardrails.md) · [codex-action](https://raw.githubusercontent.com/openai/codex-action/c05cfd74ad95c626cdf05c6685e62becc3bf7813/README.md) · [plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md)
