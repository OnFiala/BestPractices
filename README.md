# BestPractices

**An agent-maintained decision and delivery system, created with AI agents under human direction.**
Use it to turn a software idea into a scoped task for an agent, a reviewable change,
and evidence of what was actually checked. You receive guidance, a delivery plan
and evidence checks; the agent in your development environment builds your product.

It connects project requirements, architecture decisions, bounded implementation,
verification, release review and operational ownership. The first operational edition
contains six project profiles, 28 conditional gates across 11 lifecycle stages,
35 declared coverage domains, and 34 catalog entries in **EN / CS / DE / ES**
(136 localized pages). These counts describe the implemented scope; they do not
establish complete coverage of software engineering or production readiness.

English is canonical. Guidance and translations remain proposed until human review.
The local planner does not call a model or build an arbitrary product. An agent host
uses the skills and project artifacts to perform authorized work. Production identity,
real payments, live-model evaluation and deployment remain project-specific work.
See [AGENT_SYSTEM.md](AGENT_SYSTEM.md) for roles and evidence boundaries and
[PROVENANCE.md](PROVENANCE.md) for original-writing and source-use rules.
The [operational delivery review](reviews/2026-10-22-operational-delivery-review.md)
tracks this edition's findings, observed checks and remaining limits; the
[foundation review](reviews/2026-10-22-agent-system-review.md) covers the earlier library.

## Start here

1. Read [how to adopt the library](docs/en/guides/adoption.md). The recommended
   tool input is a JSON delivery profile; the optional YAML decision brief keeps
   richer business and operating context. They are different schemas.
2. Follow [one complete first evidence gate](docs/en/guides/first-project.md).
   It creates a real intent document and shows an independent review, while
   leaving the unfinished project's release blocked. No browser or model API is needed.
3. Choose the matching playbook and give your agent the bounded task below.

| Your project | Starting playbook |
| --- | --- |
| Public website | [Public website](docs/en/guides/playbook-public-website.md) |
| SaaS | [SaaS](docs/en/guides/playbook-saas.md) |
| Internal operations tool | [Internal tool](docs/en/guides/playbook-internal-tool.md) |
| AI application | [AI application](docs/en/guides/playbook-ai-application.md) |
| Agent automation | [Agent automation](docs/en/guides/playbook-agent-automation.md) |
| Backend and mobile clients | [Mobile backend](docs/en/guides/playbook-mobile-backend.md) |

Open an agent in your target project and replace the bracketed values:

```text
Work in [absolute target-project path]. Use the trusted BestPractices checkout
at [absolute library path] as a reference; do not modify the library.
Outcome: [observable user outcome]. Constraints: [data, budget, allowed effects].
Read the target project's instructions, then the library's project-delivery
skill and the matching project playbook. Record the library commit used.
Create a JSON delivery profile from actual requirements and the real target
Git revision. Run the planner from the library root using that profile.
Take the first unmet gate, explain its required artifact and acceptance check,
and perform the authorized local work. Preserve unknowns and failed/unrun checks.
Request an independent review of the actual artifact. Do not invent approval
or evidence. Report results and blockers; deployment is outside this task.
```

The skill is at `plugins/bestpractices/skills/project-delivery/SKILL.md`.
A skill is an instruction file for the host agent, not a running service.
Plugin installation and MCP are optional. Continue with
[the delivery workflow](docs/en/guides/project-delivery.md),
[coverage and limits](docs/en/guides/coverage.md), or
[the reference projects](docs/en/guides/reference-labs.md).
Česky: [úvod](docs/cs/index.md). Deutsch: [Einstieg](docs/de/index.md).
Español: [inicio](docs/es/index.md). All entries are in [the catalog](data/catalog.json).

## Create a local delivery packet

Requires Python 3.12+ on PATH. The frontend checks also require Node 22+ and a
**separately installed Chromium or Google Chrome**; set `CHROME_BIN` to its absolute
executable path if needed. The verification runner uses the Linux/macOS POSIX process
model. Local references require no provider account, secret or paid model call.

From the repository root, this synthetic public-website example creates a new
workspace, runs its selected local checks, then assesses its acceptance evidence:

```sh
mkdir -p reports
python -m library.project init --profile templates/delivery-profile.json --destination reports/example-project
cd reports/example-project
python -m library.verification delivery frontend-unit frontend-browser --output reports/local-checks.json
python -m library.delivery assess --profile project-profile.json --evidence project-evidence.json
```

The initial assessment **must exit 1**: `project-evidence.json` contains no acceptance
records. Passing reference checks does not implement the requested product or fill
that gap. Adapt the synthetic profile to actual requirements, use the generated
plan and per-gate artifacts, implement authorized work, and record reviewed observations
at the exact project revision. The initializer refuses an existing destination;
verification refuses to overwrite reports. Inspect the packet's manifest for copied
file hashes and source revision/dirty state. It creates no remote repository or deployment.

Chromium's sandbox stays enabled by default. In this controlled container, where the
browser sandbox cannot start, the explicit exception is scoped to the runner's owned
synthetic local fixture:

```sh
BP_BROWSER_NO_SANDBOX=1 python -m library.verification delivery frontend-unit frontend-browser --output reports/local-checks-container.json
```

Use this opt-in only for that local fixture, never for browsing an untrusted site.
The result records reduced process isolation. A missing browser or failed startup
is a failure, not a reason to silently omit the required check. Read
[the frontend prerequisites and limits](examples/frontend/README.md) before using it.
A complete recorded packet can become ready for human review; the assessor always
reports `production_ready: false` and cannot authenticate human approval.

## Verify the library and references

From the original library root, install the pinned Python dependencies with
[uv](https://docs.astral.sh/uv/). The lockfile includes dependency hashes.

```sh
uv sync --frozen
uv run ruff check .
uv run python -m library.validate
uv run python -m unittest discover -s tests -v
node --test tests/webmcp.test.cjs
uv run python -m library.verification delivery durable-service agent-workflow frontend-unit frontend-browser --output reports/reference-checks.json
uv run python -m library.coverage --report reports/reference-checks.json
uv run python -m library.site build
uv run python -m library.check_site
uv run python -m library.site serve
```

The browser prerequisite and local-fixture sandbox exception above also apply to
the reference suite. The last command serves all four languages on loopback port
8000. Generated `site/`, `.build/`, and `reports/` stay out of Git. Run
`uv run python -m library.sources check` separately for live source availability,
drift and overdue review; it never accepts a new source baseline or new advice.

The three original executable references are
[durable service](examples/durable_service/README.md),
[bounded agent workflow](examples/agent_workflow/README.md), and
[frontend interaction](examples/frontend/README.md). They exercise local SQLite/HTTP
invariants, deterministic agent policy/effect fixtures, and real-browser journeys.
Their READMEs state negative oracles, recovery limits and omitted production work.
A SQLite restart is not regional failover; fixture policy results are not live-model
quality; one browser run is not complete accessibility evidence. Reports bind observed
results to inputs but are not signed attestations. Review failed, skipped, stale and
unrun evidence explicitly.

## Repository map

| Path | Purpose |
| --- | --- |
| `docs/{en,cs,de,es}` | Canonical guidance, six delivery playbooks and complete translations |
| `data/` | Catalog, immutable source references, claim evidence, blueprints, delivery gates and coverage map |
| `templates/` | Delivery profile/evidence, project profile, ADR, task, test, review, release, incident and exception packets |
| `examples/` | Three local executable references with synthetic boundaries and explicit production gaps |
| `library/` | Project initialization, planning, assessment, fixed verification, coverage, content validation, source observation, site and read-only MCP |
| `plugins/bestpractices/` | Five local skills for host-driven implementation and review |
| `decisions/` | Proposed architecture decisions about this system |
| `reviews/` | Dated review findings, executed evidence and limitations |
| `.github/workflows/` | CI, metadata evidence PRs, optional private agent proposals and manual Pages publication |

## Integrate with agents

Read [AGENTS.md](AGENTS.md). Start the local stdio MCP adapter with
`uv run python -m library.mcp_server`, or configure a host to run
`uv --directory /absolute/path/BestPractices run --frozen python -m library.mcp_server`.
Its five read-only tools are `search_guides`, `get_guide`, `plan_delivery`,
`assess_delivery` and `get_coverage`; `bestpractices://catalog` is a separate resource.
They retrieve guidance or assess submitted data. They do not execute tests, create
files, authenticate identities, approve, merge or deploy. This is not a deployed
ChatGPT connector; see [integration options](docs/en/guides/integrations.md).

The five local skills are
[project-delivery](plugins/bestpractices/skills/project-delivery/SKILL.md),
[release-review](plugins/bestpractices/skills/release-review/SKILL.md),
[test-strategy](plugins/bestpractices/skills/test-strategy/SKILL.md),
[architecture-review](plugins/bestpractices/skills/architecture-review/SKILL.md), and
[maintain-library](plugins/bestpractices/skills/maintain-library/SKILL.md).
They guide the host's authorized work and evidence handoffs. Installing a skill or
producing a plan does not grant tool access or production authority.

The static site includes a feature-detected **experimental** WebMCP search adapter.
Ordinary reading and search work without it. Native host support still needs a
separate compatibility check. The site exports `llms.txt`, `catalog.json`,
`coverage.json` and localized `guides.json` for retrieval; static coverage data is
not a newly executed verification result.

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
4. For source-fed AI generation, use a **separate private repository/mirror or private workspace**.
   The model-generation and proposal jobs refuse to run in a public repository:
   logs, model output, patches, and artifacts may contain third-party text before
   anyone has checked rights or originality. In the private repository, add
   `OPENAI_API_KEY` in **GitHub Actions secrets**, set repository variable
   `ENABLE_AGENT_MAINTENANCE=true`, and optionally set
   `CODEX_MODEL` to an account-supported evaluated model. Set provider spending
   limits. Never paste the key in chat or Git. The job has a timeout, not a guaranteed
   token-spend ceiling; provider limits and human review remain necessary. Review
   original wording, source use, licensing, and technical evidence privately before
   a human transfers approved prose to a public PR. There is no automatic public
   transfer. Public source-observation PRs contain metadata, not source documents.
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
