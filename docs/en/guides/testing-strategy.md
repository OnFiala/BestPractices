---
{
  "id": "testing-strategy",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Choose a testing strategy

## Describe the test on three independent axes

An agent should state what it knows about the system, which boundary it exercises, and which failure it is looking for. These are different choices. A black-box test can check ordinary functionality, performance, or security; the term does not mean penetration testing.

| Axis | Choices | What the choice tells the reviewer |
| --- | --- | --- |
| Available knowledge | Black box: observable interfaces; gray box: selected internals or instrumentation; white box: code and internal paths | Which information informed test design and which blind spots remain |
| Exercised boundary | Unit, integration, consumer/provider contract, end-to-end | How much of the real system participates and where failures can be localized |
| Objective | Functional correctness, security, performance, recovery, accessibility, compatibility | Which risk the result supports; success on one objective does not prove another |

For example, a black-box API test can verify that two identical purchase requests return one business result. A white-box unit test can explore every retry branch. A gray-box integration test can additionally inspect the transaction and outbox. They provide complementary evidence. Document local terminology if the team's definition of “integration” or “contract” differs.

## Select from the change and its consequence

The following matrix is this library's recommended starting policy, not a universal mandated test suite. Add or remove checks with an explicit risk argument.

| Change or risk | Useful first checks | Escalation and acceptance evidence |
| --- | --- | --- |
| Documentation or translation | Meaning, terminology, links, locale parity | Render the changed presentation when layout or navigation changes; no new runtime suite for a harmless wording correction |
| Business calculation or state transition | Unit examples, boundaries, invalid inputs; property-based cases for genuine invariants | Show a violating input fails; integration test if persistence or external state is part of correctness |
| Database schema or transaction | Real database integration, constraints, concurrency, migration compatibility | Representative data volume, locks, restart/resume and recovery; old supported consumers remain compatible |
| API or event schema | Producer/consumer contract examples and compatibility checks | Actual serialization and transport path; reject invalid inputs without unwanted effects |
| User journey or frontend state | Component checks and a small browser journey using public semantics | Loading, empty, error, cancellation, keyboard and narrow viewport states; verify real browser events |
| Authentication, permissions, tenant scope | Policy tests plus unauthorized API/object access with distinct identities | Review untested entry points and perform targeted security testing; denied requests leave no protected data or side effect |
| Worker, payment, or durable workflow | Duplicate, reorder, timeout and crash-boundary integration cases | Reconcile intended effects after retry/restart; provider sandbox compatibility where necessary |
| Concurrency, caching, scheduling, capacity | Functional checks under concurrency and a measured baseline | Select load, stress, spike or soak checks from the performance guide; preserve correctness and bounded recovery |
| Model, prompt, retrieval, tool or agent policy | Versioned task evaluations, adversarial cases, deterministic policy tests | Compare against held-out cases, inspect actual tool effects, repeat stochastic cases and report variability |

## Plan before choosing a tool

Write a short test packet: the affected requirement; a failure hypothesis; knowledge model, boundary, and objective; fixtures and environment; expected results; safe execution limits; and the evidence to retain. The tool follows this packet. A browser driver, HTTP client, property generator, load generator, scanner, or human review each observes different things.

Use the smallest boundary that can reveal the defect, then add a realistic boundary check when substitutes could hide it. A mocked database cannot prove a database uniqueness constraint, and a mocked browser event cannot prove native browser support. Keep external providers controlled in deterministic tests; label a sandbox compatibility test separately from a simulated response.

Make fixtures independent and reproducible. Control relevant clocks and randomness, record seeds, and isolate accounts, tenants, state, and cleanup. Do not share a mutable test user across parallel runs unless that concurrency is the subject. Protect fixtures and traces as data; never copy production records just to make a test realistic.

## Make assertions falsifiable

Check outputs, persisted state, and prohibited effects relevant to the requirement. An HTTP success code alone does not prove the correct object was returned. An authorization test should exercise both a permitted action and a denied one, then verify the denial did not modify protected state.

For a consequential fix, demonstrate that the test can expose the original bug or a deliberately broken local variant. Use boundary-value and equivalence-class examples where applicable. Property-based tests explore a defined invariant; they still depend on a sound invariant and input model. Coverage can reveal unvisited code, but high coverage cannot prove requirements are correct or security boundaries complete.

## Decide when enough evidence exists

Stop the affected release if required checks fail, the target is outside approved scope, test data escapes its boundary, or a high-consequence claim lacks evidence. Report omissions and uncertainty. A human can accept a documented, time-limited residual risk; an agent cannot label an unexecuted check as passed.

Completion means the agreed behavior is supported by interpretable results, known limitations, and a recovery plan. Preserve the tested revision, configuration, fixture version, commands, results, and relevant traces with sensitive values removed. Add further testing when a new failure hypothesis warrants it rather than repeating the same green suite indefinitely.

## Evidence and related decisions

The three-axis model and selection matrix are original local synthesis. OWASP supports authorization testing at multiple boundaries; Playwright supports isolated browser checks based on visible behavior; PostgreSQL documents the concurrency properties that real database checks must exercise. These sources do not certify every cell of the matrix.

[Quality gates](quality.md) · [Performance and stress testing](performance-testing.md) · [Security testing](security-testing.md) · [Data and migrations](data.md) · [Durability](durability.md)

## Primary evidence

[owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [playwright-testing](https://raw.githubusercontent.com/microsoft/playwright/ca7ca36145b84183cf423c2a099bd7e9cd8b1cb3/docs/src/best-practices-js.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml) · [owasp-multi-tenant](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.md)
