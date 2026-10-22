# BestPractices

A decision library for durable software built by agents under human direction.
English is canonical; the website switches between **EN / CS / DE / ES** on the
same page. This first edition is proposed guidance, pending human editorial review.

Start with [the library](docs/en/index.md), [the decision matrix](docs/en/guides/architecture.md),
[six project paths](docs/en/reference/examples.md), or [the full catalog](data/catalog.json).
Česky: [úvod](docs/cs/index.md). Deutsch: [Einstieg](docs/de/index.md).
Español: [inicio](docs/es/index.md).

## Run and verify

Requires Python 3.12 and [uv](https://docs.astral.sh/uv/). Dependencies and hashes
are committed in `uv.lock`; no model API or service credentials are needed locally.

```sh
uv sync --frozen
uv run ruff check .
uv run python -m library.validate
uv run python -m unittest discover -s tests -v
node --test tests/webmcp.test.cjs
uv run python -m library.site build
uv run python -m library.check_site
uv run python -m library.site serve
```

The last command builds and serves all languages on loopback port 8000. Generated
`site/`, `.build/`, and `reports/` stay out of Git. Node 22+ is only needed for the
browser-adapter unit tests. Run `uv run python -m library.sources check` separately
for live source availability, drift, and overdue review. It never accepts new advice.

## Repository map

| Path | Purpose |
| --- | --- |
| `docs/{en,cs,de,es}` | Canonical prose and complete translations |
| `data/` | Stable guide IDs, primary sources, retrieval baseline, tool and project registries |
| `templates/` | Project profile, ADR, agent task, review, release, incident, exception |
| `decisions/` | Decisions about this library itself |
| `library/` | Validation, source observation, static build, read-only MCP |
| `plugins/bestpractices/` | Local Codex skill bundle |
| `.github/workflows/` | CI, evidence PRs, optional agent PRs, manual Pages deployment |

## Integrate with agents

Read [AGENTS.md](AGENTS.md). Start the read-only MCP server with
`uv run python -m library.mcp_server`; it provides `search_guides`, `get_guide`, and
`bestpractices://catalog`. A host can launch it using
`uv --directory /absolute/path/BestPractices run --frozen python -m library.mcp_server`.
This is local stdio, not a deployed ChatGPT connector. See the
[integration guide](docs/en/guides/integrations.md) for the distinction.

The static site includes a feature-detected **experimental** WebMCP search adapter.
Normal reading and search do not depend on browser support. Current API assumptions
are recorded against the primary-source hash; native WebMCP host support needs a
separate compatibility test. `llms.txt`, `catalog.json`, and localized `guides.json`
are exported with the website for plain retrieval.

## Activate on GitHub

1. Review the initial change and merge it into `main`. Local tests do not prove a
   GitHub-hosted workflow has run.
2. Configure a ruleset for `main`: require PRs, the `quality` check, resolved
   conversations, and approval from a human code owner; dismiss stale approvals.
   Block force pushes/deletion and avoid bot bypass. A sole owner cannot approve
   their own PR: use bot-authored PRs with owner review or add another reviewer.
3. Enable Actions and “Allow GitHub Actions to create and approve pull requests”.
   This grants platform capability; this project never automates PR approval.
   Weekly evidence PRs require `contents: write` and `pull-requests: write` only in
   the publication job. PRs created with `GITHUB_TOKEN` may not trigger new workflow
   runs: run **Validate** manually on the bot branch before human review/merge.
4. For the optional agent workflow, add `OPENAI_API_KEY` in **GitHub Actions secrets**,
   set repository variable `ENABLE_AGENT_MAINTENANCE=true`, and optionally set
   `CODEX_MODEL` to an account-supported evaluated model. Set provider spending
   limits. Never paste the key in chat or Git. The job has a timeout, not a guaranteed
   token-spend ceiling; provider limits and human review remain necessary.
5. For the website, choose GitHub Pages source **GitHub Actions**, configure the
   `github-pages` environment with human approval, then manually run **Publish docs**
   on `main`. This publishes only static documentation, never MCP hosting.

No remote ruleset, deployment, paid automation, or connector installation is implied
by these files. Scheduling and secrets become effective only in the configured repository.

## Stewardship

Agents propose, humans merge. A source hash change is a review request, not a truth
update. Keep English and translations at the same revision; review meaning as well
as metadata. Follow [CONTRIBUTING.md](CONTRIBUTING.md) and the
[maintenance guide](docs/en/guides/maintenance.md).

Text and diagrams: [CC BY 4.0](LICENSE-CONTENT). Code/configuration: [MIT](LICENSE-CODE).
Third-party sources keep their own licenses.
