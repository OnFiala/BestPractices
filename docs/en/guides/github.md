---
{
  "id": "github",
  "language": "en",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# GitHub, versions, and clean trees

## A reviewable flow

Keep `main` releasable. Use short-lived branches for one change and small coherent commits that explain intent. Commit when a meaningful increment can be understood and checked; do not wait for an entire project or commit generated secrets and caches. `feat:`, `fix:`, and `docs:` are useful local conventions, not a substitute for a clear description.

Open a PR with problem, behavior, evidence, risks, and rollback. Review the final diff, not only the agent summary. Require status checks, code-owner review where applicable, resolved discussions, and fresh approval after meaningful changes. Agents never approve or merge their own work. Configure a ruleset to block force-push/deletion and direct changes to `main`; files alone do not activate it.

Use SemVer for a defined public contract. Tag deliberate releases, publish a changelog and migration notes, and never silently replace a release tag. Internal commits need not be releases. For this library, guide IDs and metadata are contracts: breaking them requires a migration and version decision.

## Cleanliness

Before editing, inspect status and preserve other work. Ignore generated outputs; review staged files and accidental deletions before committing. Never use blanket reset/clean commands. Delete merged branches after confirming no local-only work; prune references separately. Use worktrees only when needed and explicitly requested in this cloud environment. Track abandoned branches with an owner and expiry.

## Related decisions

[Quality gates that prove behavior](quality.md) · [Human direction, agent execution](agents.md) · [Evidence and automated maintenance](maintenance.md)

## Primary evidence

[github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md) · [semver](https://raw.githubusercontent.com/semver/semver/f99d5485190a47c0863949e7da810a5553e0ed4d/semver.md)
