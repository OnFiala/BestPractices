---
{
  "id": "quality",
  "language": "en",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Quality gates that prove behavior

## Choose evidence from the change

Testing is part of the agent's task definition. Before implementation, name the behavior at risk, the consequence of failure, and the observation that would demonstrate a defect. Choose a proportionate set of checks using the [testing strategy](testing-strategy.md). Security-sensitive boundaries also use [security testing](security-testing.md); concurrency, resource, or capacity changes use [performance testing](performance-testing.md).

A text correction needs editorial and link checks, not a new mock-heavy test suite. A payment retry, tenant filter, database migration, or privileged tool change needs evidence about its failure paths. “All existing tests pass” does not answer whether the changed contract has a test.

## Evidence before implementation

The task packet records the affected consumer, expected success and refusal behavior, representative data, execution environment, and acceptable result. Include at least one relevant negative or boundary case when a behavior can fail consequentially. Keep expected results independent of the algorithm being implemented: a test that recomputes the same flawed formula may agree with the bug.

For a bug fix, show that the focused check detects the original failure when practical. For a new invariant, challenge the test with a deliberately invalid fixture or a temporary local mutation. Remove that mutation before proposing the change. This library recommends such checks according to risk; it does not require mutation testing for every edit or a universal coverage percentage.

## Build a useful delivery gate

Require reproducible dependency installation and a build appropriate to the stack. Add type, lint, and static checks where they detect plausible defects. Execute focused behavioral checks first, then the affected integration or contract suite. Use real boundary implementations when isolation, transactions, serialization, browser events, or permissions are the concern; mocks alone cannot establish those properties.

Keep a small set of end-to-end journeys that cover valuable user outcomes and their critical failure states. Use isolated accounts and synthetic data. Control external dependencies in repeatable tests, then run separately scoped compatibility checks against provider sandboxes. An email or payment test must not contact real customers or charge a live account accidentally.

Required checks must fail the delivery job when they fail. Report passed, failed, skipped, quarantined, and unrun cases separately. Do not lower a threshold or remove an assertion merely to make a change pass. A genuinely changed requirement needs its own explanation and human review. Quarantined flaky tests need an owner, reason, expiry, and substitute evidence for the protected behavior.

## Evidence for AI-generated changes

Review the final diff and the tests together. The reviewer should challenge the implementer's assumptions, not just repeat the same prompt. Use a representative regression set for changes to models, prompts, tools, retrieval, and policies. Keep development examples separate from held-out evaluation cases. Score both useful task completion and unwanted effects; a convincing response does not prove that a tool executed safely.

Record the model and configuration, test data version, tool policy, repetitions, scoring rubric, and observed variability. Calibrate model-based grading with human-reviewed examples and deterministic checks where possible. Protect evaluation data from tenant leaks and prompt injection. Changing an evaluation product or provider does not remove the need for these records.

## Release decision and maintenance

The agent returns the exact revision, commands, environment, outcomes, known omissions, and recovery plan. Stop the affected release when a required check fails, a consequential behavior remains untested, or available evidence contradicts the claimed result. A human may record a time-limited exception with an owner and compensating control; the agent must not silently reinterpret failure as success.

Track escaped defects, flaky checks, slow feedback, and change recovery. Add a focused regression after a meaningful incident. Remove checks only when their protective purpose is obsolete or covered better elsewhere. The goal is credible evidence at sustainable cost, not the largest test count.

## This library and evidence scope

This repository validates content identity, source references, translation revisions, links, integration behavior, and site generation. Those checks do not certify architectural advice or the meaning of translations. Human editorial review remains a separate gate.

The workflow above is an original local synthesis. Playwright supports isolated user-facing browser checks; OWASP supports authorization and agent-abuse testing; GitHub documents workflow trust boundaries. These sources are not a universal testing standard or endorsement of this library.

## Related decisions

[Testing strategy](testing-strategy.md) · [Performance and stress testing](performance-testing.md) · [Security testing](security-testing.md) · [Human direction, agent execution](agents.md) · [The complete project lifecycle](lifecycle.md)

## Primary evidence

[playwright-testing](https://raw.githubusercontent.com/microsoft/playwright/ca7ca36145b84183cf423c2a099bd7e9cd8b1cb3/docs/src/best-practices-js.md) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md)
