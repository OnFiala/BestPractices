---
{
  "id": "playbook-ai-application",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Deliver an AI application

## Fit and bounded outcome

Use this profile for an authenticated application that retrieves information or produces an answer with a model. Define the user task, acceptable errors, prohibited disclosures, latency deadline, cost ceiling, data residency, and an ordinary non-model fallback. Start with one bounded request pipeline, an adapter around the provider, and an evaluation dataset. This agent-authored proposal combines local engineering judgment with the cited evidence; it is not proof of model reliability.

Search or deterministic rules are alternatives when they satisfy the task more predictably. Retrieval can support answers grounded in project data; fine-tuning is not a replacement for document access policy or freshness. Add models, providers, caches, or asynchronous stages only when measured quality, delay, throughput, or residency constraints justify their evaluation and operational cost. A larger user population alone does not justify an agent loop.

## Separate authority, data, and model behavior

Organize `api/`, `policy/`, `retrieval/`, `model_adapter/`, `evaluation/`, and `telemetry/`. The server authenticates the caller and filters candidate documents by current access before content reaches a model. Include tenant, policy version, document version, and deletion status in cache and retrieval design. A global answer cache keyed only by query can leak another user's context. Define how revocation and deletion reach indexes, stored prompts, generated answers, and provider-held data under the selected provider contract.

The model returns untrusted content. Validate structured output, render text safely, and keep tool execution behind independent authorization. Retrieved instructions, citations, and model confidence never grant permissions. Define response contracts for grounded answer, insufficient evidence, unavailable provider, budget exhaustion, and cancellation. A citation must identify a retrieved source that actually supports the associated claim; a plausible-looking URL is not grounding. Keep raw credentials outside prompts and give logging an explicit privacy and retention policy.

## Sequence the work and its evidence

1. Discovery specifies representative tasks, failure severity, lawful data handling, and a scoring rubric before model selection. The human owner agrees acceptable error rates and adjudicates ambiguous cases.
2. Implementation builds one pipeline with authorized retrieval, bounded context, provider deadline, output validation, and fallback. Version model settings, prompt, retrieval/index configuration, and tool schemas together.
3. Verification runs a held-out, privacy-safe evaluation set and adversarial cases, then inspects authorization and cost traces. Release preparation compares the candidate against a fixed baseline and documents human review and unresolved failures.

The handoff packet includes the profile, data-flow ADR, provider/data-processing decision, access matrix, evaluation dataset identity, per-case scores and human adjudications, version manifest, latency/cost distribution, fallback evidence, and incident owner. `examples/frontend` and `examples/agent_workflow` offer local interaction and control-boundary references to inspect. Neither proves semantic answer quality, provider compliance, or the safety of a production retrieval service.

## Use oracles outside the model

Select unit tests for schema and budget accounting, integration tests for access filtering and provider failure, and evaluations for usefulness and grounding. Keep training/tuning examples separate from held-out acceptance cases. Score answer correctness, unsupported claims, appropriate abstention, and harmful omission separately; averaging can hide a severe disclosure. Human-reviewed rubrics remain necessary where outcomes are subjective. Model-based grading is a measurement aid, not independent acceptance authority.

Put a unique synthetic marker in a denied document. Query it directly, indirectly, and through an allowed document containing hostile instructions. The marker must be absent from retrieved context, provider requests, returned answers, and exposed logs. After revocation or deletion, repeat with warmed caches and indexes. Attempt schema-breaking output and script-like citations: they must not execute or broaden access. These are negative oracles, not checks that the model politely refuses.

Force provider timeouts, disconnect the browser, and exhaust an enforced request budget. The application must stop scheduling further calls, preserve a clear user state, and record any already incurred work; cancellation does not guarantee that a provider stopped billing. Compare repeated runs for quality variance and measure tail latency and cost per accepted task under a bounded workload. Record actual sample sizes, failed cases, and untested languages or domains.

## Release and long-term operation

Roll out to an agreed cohort behind a disable switch and observe quality, abstention, error, latency, and spend thresholds. Changing the model, prompt, retrieval, or fallback is a behavior release requiring renewed evaluation. Keep the prior version manifest and compatible index representation. Rollback can restore behavior but cannot retract disclosed information or unsend provider requests. A disclosure needs incident handling and access/data review; deleting a local log alone is insufficient.

Assign owners for evaluation drift, access policy, provider incidents, and cost escalation. Budget embedding/index updates, retries, evaluation runs, storage, and human review alongside inference. Before production, resolve provider retention/residency, real identity, encryption, deletion propagation, abuse limits, and operational coverage. Retirement disables entry points, drains safe work, deletes or retains derived artifacts according to policy, revokes provider access, and preserves only the evidence required for accountability.

## Continue with related decisions

[Agents](agents.md) · [Security](security.md) · [Quality gates](quality.md) · [Testing strategy](testing-strategy.md)

## Primary evidence

[owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-xss](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md)
