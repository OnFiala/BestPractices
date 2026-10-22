---
{
  "id": "adoption",
  "language": "en",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Adopt the library in a project

## Build a portable decision packet

Copy the templates you need, not the entire library. Fill `project-profile.yaml` with outcome, data sensitivity, accountable owner, workload, budget, service objectives and recovery assumptions. Pin this library to a reviewed release or full commit and stable guide IDs. Following mutable `main` silently can change production policy without project approval.

Create a context diagram and an ADR for the first consequential decision. Record accepted guidance, deliberately deferred controls, an owner, expiry and compensating checks. Keep project-specific agent instructions in `AGENTS.md`; link supporting material. This library is an agent-maintained proposal source. Its recommendations become project policy only through the project's human decision process.

## Three starting examples

- **Personal public website:** use a static build, content history and a reproducible deployment. Keep private notes, credentials and personal source data out of public Git history and public build assets, including search indexes. A login screen cannot protect publicly downloadable files. A private knowledge base needs private storage and server-enforced access checks for documents, assets, downloads and search; a private repository alone does not make its published output private.
- **Small SaaS:** begin with a modular application, transactional database and worker only where needed. Define tenant boundaries, payment reconciliation and an operating owner. Before accepting real customers, prove denial across tenants, compatibility during deployment and restoration into an isolated environment.
- **High-traffic platform:** first measure traffic mix, skew, data growth and dependency limits. Partition or isolate a workload only after demonstrating the constraint and assigning ownership for consistency, migration, on-call response and recovery. A large account count alone does not establish a capacity requirement.

These are original starting recommendations, not universal prescriptions or benchmarked deployment templates.

## Turn guidance into acceptance evidence

For each adopted guide, identify the observable obligation and the check that could refute compliance. For example, “tenant isolation” becomes a test where tenant A's authenticated session requests tenant B's object through the API, export and worker paths, and none returns B's data. Record test setup, expected result, executed revision and retained evidence in the [testing strategy](testing-strategy.md).

Use the [reference profiles](../reference/examples.md) to identify missing boundaries. An unexecuted acceptance statement is a planned test, not proof. Do not claim safety because a template is filled in or a generated summary says “passed.” Review the actual result, including failures and omissions.

## Revisit without losing control

Consult applicable guides during planning and link them in the implementation task. At review, compare the diff with the chosen decision and failure cases. Before release, validate migration and recovery; during operation, feed measurements and incidents back into ADRs. Upgrade the pinned library through a PR explaining changed obligations, affected projects and the migration or exception plan.

If a new recommendation cannot be validated within the project's budget or ownership capacity, record that gap and simplify the design. Do not silently accept a policy that nobody can operate.

## Related decisions

[Decision principles](foundations.md) · [The complete project lifecycle](lifecycle.md) · [Testing strategy](testing-strategy.md) · [Human direction, agent execution](agents.md) · [Governance and unanswered decisions](governance.md)

## Primary evidence

[plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md) · [github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md)
