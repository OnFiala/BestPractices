---
{
  "id": "governance",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Governance and unanswered decisions

## Current agreement

This is a public, portable library. English is canonical, with Czech, German, and Spanish translations. Original prose and diagrams use CC BY 4.0; code, configuration, and reusable code templates use MIT. Third-party sources retain their licenses. Agents propose PRs; a human reviews and merges. Initial recommendations and translations are not automatically human-approved.

## Decisions each adopting project must answer

Who is accountable for production and available during an incident? What data must never leave a region or provider? How much downtime and data loss can users tolerate? What is the monthly infrastructure and AI budget, including a hard stop? What happens when the model or hosting provider is unavailable? Who approves irreversible operations? How do users export/delete data? Which accessibility and legal requirements apply? Who inherits the project if its owner leaves?

Keep these answers in the project profile and ADRs. Unanswered high-consequence questions block the relevant launch, not unrelated exploration. Exceptions require an owner, reason, compensating control, and expiry.

## Library stewardship

Use an issue to propose a new topic or challenge advice; include a counterexample and primary evidence. Separate universal principles from context-dependent preferences. Deprecate with replacement links instead of deleting history. Publish versioned changes and communicate altered obligations. Human reviewers decide whether translations preserve meaning; matching revision numbers only check bookkeeping. Measure usefulness through successful decisions and reduced correction work, not page count.

## Related decisions

[Evidence and automated maintenance](maintenance.md) · [Adopt the library in a project](adoption.md) · [GitHub, versions, and clean trees](github.md)

## Primary evidence

[github-rulesets](https://raw.githubusercontent.com/github/docs/main/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [semver](https://raw.githubusercontent.com/semver/semver/master/semver.md) · [plugins](https://raw.githubusercontent.com/openai/plugins/main/README.md)
