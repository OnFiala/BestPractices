---
{
  "id": "maintenance",
  "language": "en",
  "revision": 3,
  "translation_revision": 3,
  "reviewed_on": "2026-10-22"
}
---
# Evidence and automated maintenance

## Evidence pipeline

`data/sources.json` separates an immutable inspected source from the URL monitored for later changes. It records publisher, scope, review interval, and license evidence. The retrieval baseline records successful hashes, not human approval. A scheduled observer fetches bounded HTTPS documents and reports changed, unavailable, or overdue sources. A changed hash is a review signal, never authorization to alter guidance. A failed fetch remains unavailable, not unchanged.

By default the source workflow publishes a metadata artifact and review instructions, using read-only permissions. Download `source-evidence` from the run within 14 days, inspect `source-observations.json`, and copy that candidate to `data/source-observations.json` on a review branch. Check an existing `automation/source-observations` branch before reusing it, open a draft PR, and run Validate on its exact head. Automatic proposals require the explicit `ENABLE_SOURCE_REVIEW_PRS=true` variable and an owner-configured GitHub policy allowing Actions to create PRs. A failed proposal may have pushed a branch without creating a PR; inspect the actual result. Do not add credentials or weaken permissions to bypass a denial.

Neither path accepts the baseline or merges. New references carry `baseline_status: pending-human-review` and remain outside `data/source-baseline.json`; a successful fetch does not accept them. A human reads the relevant source diff, verifies claims and applicability, and decides whether to update guides, translations, review dates, and baseline together. Acceptance of a new source adds its inspected observation and removes the pending marker in the same reviewed change. Do not reset a review date just because a URL returned 200.

## Agent-assisted updates

The public repository observes source metadata. Source-fed model generation and proposal jobs are restricted to a separate private repository/mirror or private workspace: logs, summaries, patches, and artifacts may contain upstream text before rights review. The opt-in private Codex workflow requires a configured secret and explicit enablement; local validation and source checks need no paid API. The model returns bounded structured proposal data. A fresh trusted consumer validates that data instead of executing an agent-produced script or trusting the agent's Git metadata.

A human inspects the private output for original expression, licensing, sensitive data, evidence, and translation meaning before transferring approved content into a public PR. There is no automatic public transfer. Write independent explanations and examples; do not copy or translate upstream prose, or closely paraphrase distinctive expression. Required third-party software notices remain under their own licenses. A source citation or similarity screen does not grant reuse rights.

The agent has no approval, merge, or publication authority. Rulesets and required review still need actual GitHub configuration; a workflow file does not enforce them. A private generation service has not been deployed as part of this library.

## Freshness and failure

Check fast-moving AI/protocol sources more often than stable principles. Label experiments and deprecations, retain migration links, and record contested advice. Missing credentials, blocked networks, failed checks, and stale translations remain visible blockers. Track overdue review age and time-to-resolve source drift. Revert a bad guidance change by commit and assess projects that adopted it.

Do not treat a README or an index with transcluded files as coverage of the underlying specification. Register the substantive control or mechanism actually relied on. Claim mappings must separate source-supported behavior from local synthesis, record applicability, and remain tied to the reviewed version. Refresh product lifecycle evidence before adopting an AI platform; a methodology can remain useful after the product used by its example is retired.

## Related decisions

[GitHub, versions, and clean trees](github.md) · [Human direction, agent execution](agents.md) · [Governance and unanswered decisions](governance.md)

## Primary evidence

[codex-action](https://raw.githubusercontent.com/openai/codex-action/c05cfd74ad95c626cdf05c6685e62becc3bf7813/README.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md) · [plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md)
