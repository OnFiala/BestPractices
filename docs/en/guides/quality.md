---
{
  "id": "quality",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Quality gates that prove behavior

## Test the contract, not the implementation

A green formatter is not a working product. Choose tests by failure consequence: unit tests for pure rules, integration tests for database and service boundaries, contract tests for consumers, and a small set of end-to-end journeys. Include authorization denial, invalid input, timeout, duplicate submission, and recovery where relevant. Use synthetic data and isolate external side effects.

## Delivery gate

Require reproducible dependency installation, build/type checks where applicable, meaningful tests, and review of the actual diff. Record counts and distinguish pass, fail, skip, and unrun. Never weaken an assertion to unblock a release. A flaky test needs an owner and expiry for quarantine; it must not disappear silently.

For AI-generated work, assess whether tests could fail for the proposed defect. An independent reviewer should inspect assumptions and negative cases. Snapshot tests need semantic assertions; coverage percentages alone do not establish quality.

## This library

Run the validator, Python tests, lint, and four-language strict site build. Validation rejects missing translations, stale revisions, unknown evidence, and broken local links. Source monitoring is a separate network observation; CI cannot prove factual correctness or translation quality.

## Revisit

Track escaped defects, change failure rate, restoration time, and slow checks. Remove redundant checks when they add no protection, but retain evidence for high-consequence paths. Human review decides whether the evidence is sufficient.

## Related decisions

[GitHub, versions, and clean trees](github.md) · [Human direction, agent execution](agents.md) · [The complete project lifecycle](lifecycle.md)

## Primary evidence

[owasp](https://raw.githubusercontent.com/OWASP/ASVS/master/README.md) · [wcag](https://raw.githubusercontent.com/w3c/wcag/main/guidelines/index.html) · [github-workflows](https://raw.githubusercontent.com/github/docs/main/content/actions/reference/security/secure-use.md)
