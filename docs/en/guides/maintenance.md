---
{
  "id": "maintenance",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Evidence and automated maintenance

## Evidence pipeline

`data/sources.json` lists primary sources, scope, review date, and review interval. The baseline records successful retrieval hashes. A scheduled observer fetches bounded HTTPS documents and reports changed, unavailable, or overdue sources. A changed hash is a review signal, never authorization to alter guidance. A failed fetch remains unavailable, not unchanged.

The source workflow creates or refreshes an evidence PR when action is needed. It does not update the accepted baseline or merge. A human reads the relevant source diff, verifies claims and applicability, and decides whether to update guides, translations, review dates, and baseline together. Do not reset a review date just because a URL returned 200.

## Agent-assisted updates

The opt-in Codex workflow proposes bounded documentation changes. It requires a configured GitHub secret and explicit enablement; local validation and source checks need no paid API. Agent edits are restricted to existing translated guides and catalog metadata. A separate job opens a draft PR; the agent has no merge authority. Rulesets and required human review must be activated in GitHub settings.

## Freshness and failure

Check fast-moving AI/protocol sources more often than stable principles. Label experiments and deprecations, retain migration links, and record contested advice. Missing credentials, blocked networks, failed checks, and stale translations remain visible blockers. Track overdue review age and time-to-resolve source drift. Revert a bad guidance change by commit and assess projects that adopted it.

## Related decisions

[GitHub, versions, and clean trees](github.md) · [Human direction, agent execution](agents.md) · [Governance and unanswered decisions](governance.md)

## Primary evidence

[codex-action](https://raw.githubusercontent.com/openai/codex-action/main/README.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/main/content/actions/reference/security/secure-use.md) · [plugins](https://raw.githubusercontent.com/openai/plugins/main/README.md)
