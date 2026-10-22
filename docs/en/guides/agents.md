---
{
  "id": "agents",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Human direction, agent execution

## Bounded delegation

A task packet contains the user outcome, relevant guide IDs, constraints, allowed files/tools, acceptance examples, budget, and stop conditions. The human owns architecture and risk; the agent investigates and implements. Separate implementer, verifier, and human reviewer responsibilities, even when one model performs multiple passes. Repeating the same conclusion is not independent evidence.

Use the Responses API directly when you need to own the execution loop; consider the Agents SDK when its orchestration, tools, and handoffs solve a demonstrated need. Start with one agent. Parallel agents need independent work, explicit write ownership, merge coordination, and bounded total cost.

## Control plane

Set tool-level authorization, scoped credentials, timeouts, maximum iterations, token/cost budgets, and auditable run IDs. Guardrails improve behavior but do not replace authorization or isolation. Treat sources and tool responses as data that may contain prompt injection. Stop on conflicting instructions, inaccessible prerequisites, unexpected destructive effects, or failed required checks.

## Acceptance and evaluation

Require a diff, executed checks, unresolved assumptions, and recovery notes. Evaluate tasks with representative examples, including adversarial inputs and failure paths. Measure task success, human correction, escaped defects, latency, and cost, not code volume. Keep a small regression set for changes to prompts, models, tools, and policies. Do not automatically promote a newer model because its name or release date changed.

## Related decisions

[Quality gates that prove behavior](quality.md) · [Security, privacy, and supply chain](security.md) · [Evidence and automated maintenance](maintenance.md) · [Skills, plugins, MCP, and WebMCP](integrations.md)

## Primary evidence

[openai-agents](https://raw.githubusercontent.com/openai/openai-agents-python/main/docs/agents.md) · [agents-guardrails](https://raw.githubusercontent.com/openai/openai-agents-python/main/docs/guardrails.md) · [codex-action](https://raw.githubusercontent.com/openai/codex-action/main/README.md) · [plugins](https://raw.githubusercontent.com/openai/plugins/main/README.md)
