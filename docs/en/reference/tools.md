---
{
  "id": "tools",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Sources and tools

This registry is a shortlist, not an endorsement or a requirement to install everything. Choose from the project constraints and prove one representative workflow before adoption. Candidate tools are not installed or tested by this library unless marked used-here. The MCP adapter and static documentation builder are local capabilities; cloud workflows still need GitHub activation. Source status describes the inspected document, not a guarantee about every released version. Check the installed version and its supported API. Source hashes only detect drift; humans must evaluate meaning, licensing, and applicability. Tool names remain unchanged in translations so agents and people can identify the same product. Read the integration and hosting guides before exposing services or granting credentials.

| Tool | Status | Source |
| --- | --- | --- |
| Codex | `candidate` | [codex](https://raw.githubusercontent.com/openai/codex/main/README.md), [plugins](https://raw.githubusercontent.com/openai/plugins/main/README.md) |
| OpenAI Agents SDK | `candidate` | [openai-agents](https://raw.githubusercontent.com/openai/openai-agents-python/main/docs/agents.md), [agents-guardrails](https://raw.githubusercontent.com/openai/openai-agents-python/main/docs/guardrails.md) |
| MCP Python SDK | `used-here` | [mcp-python](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md) |
| WebMCP | `experimental` | [webmcp](https://raw.githubusercontent.com/webmachinelearning/webmcp/main/README.md) |
| MkDocs Material | `used-here` | [mkdocs-material](https://raw.githubusercontent.com/squidfunk/mkdocs-material/master/README.md) |
| GitHub Actions | `used-here` | [github-workflows](https://raw.githubusercontent.com/github/docs/main/content/actions/reference/security/secure-use.md), [github-rulesets](https://raw.githubusercontent.com/github/docs/main/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) |
| PostgreSQL | `candidate` | [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml), [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/mvcc.sgml) |
| Docker / Compose | `candidate` | [docker-security](https://raw.githubusercontent.com/docker/docs/main/content/manuals/engine/security/_index.md) |
| Kubernetes | `candidate` | [kubernetes](https://raw.githubusercontent.com/kubernetes/website/main/content/en/docs/concepts/architecture/_index.md) |
| OpenTofu | `candidate` | [opentofu](https://raw.githubusercontent.com/opentofu/opentofu/main/README.md) |
| OpenTelemetry | `candidate` | [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/main/content/en/docs/concepts/observability-primer.md) |
| Temporal | `candidate` | [durable-workflows](https://raw.githubusercontent.com/temporalio/temporal/main/README.md) |

- **agents-guardrails** — [openai](https://raw.githubusercontent.com/openai/openai-agents-python/main/docs/guardrails.md); current; 2026-10-21; 14 days.
- **codex** — [openai](https://raw.githubusercontent.com/openai/codex/main/README.md); current; 2026-10-21; 14 days.
- **codex-action** — [openai](https://raw.githubusercontent.com/openai/codex-action/main/README.md); current; 2026-10-21; 14 days.
- **docker-security** — [docker](https://raw.githubusercontent.com/docker/docs/main/content/manuals/engine/security/_index.md); current; 2026-10-21; 90 days.
- **durable-workflows** — [temporalio](https://raw.githubusercontent.com/temporalio/temporal/main/README.md); current; 2026-10-21; 90 days.
- **github-rulesets** — [github](https://raw.githubusercontent.com/github/docs/main/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md); current; 2026-10-21; 90 days.
- **github-workflows** — [github](https://raw.githubusercontent.com/github/docs/main/content/actions/reference/security/secure-use.md); current; 2026-10-21; 90 days.
- **kubernetes** — [kubernetes](https://raw.githubusercontent.com/kubernetes/website/main/content/en/docs/concepts/architecture/_index.md); current; 2026-10-21; 90 days.
- **mcp-python** — [modelcontextprotocol](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md); current; 2026-10-21; 14 days.
- **mcp-spec** — [modelcontextprotocol](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/README.md); current; 2026-10-21; 14 days.
- **mkdocs-material** — [squidfunk](https://raw.githubusercontent.com/squidfunk/mkdocs-material/master/README.md); current; 2026-10-21; 90 days.
- **observability** — [open-telemetry](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/main/content/en/docs/concepts/observability-primer.md); current; 2026-10-21; 90 days.
- **openai-agents** — [openai](https://raw.githubusercontent.com/openai/openai-agents-python/main/docs/agents.md); current; 2026-10-21; 14 days.
- **openai-apps** — [openai](https://raw.githubusercontent.com/openai/openai-apps-sdk-examples/main/README.md); current; 2026-10-21; 14 days.
- **opentofu** — [opentofu](https://raw.githubusercontent.com/opentofu/opentofu/main/README.md); current; 2026-10-21; 90 days.
- **owasp** — [OWASP](https://raw.githubusercontent.com/OWASP/ASVS/master/README.md); current; 2026-10-21; 90 days.
- **plugins** — [openai](https://raw.githubusercontent.com/openai/plugins/main/README.md); current; 2026-10-21; 14 days.
- **postgres-backup** — [postgres](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml); current; 2026-10-21; 90 days.
- **postgres-isolation** — [postgres](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/mvcc.sgml); current; 2026-10-21; 90 days.
- **semver** — [semver](https://raw.githubusercontent.com/semver/semver/master/semver.md); current; 2026-10-21; 90 days.
- **skills** — [openai](https://raw.githubusercontent.com/openai/skills/main/README.md); deprecated; 2026-10-21; 14 days.
- **wcag** — [w3c](https://raw.githubusercontent.com/w3c/wcag/main/guidelines/index.html); current; 2026-10-21; 90 days.
- **webmcp** — [webmachinelearning](https://raw.githubusercontent.com/webmachinelearning/webmcp/main/README.md); experimental; 2026-10-21; 14 days.

## Related decisions

[Skills, plugins, MCP, and WebMCP](../guides/integrations.md) · [Hosting and exit strategies](../guides/hosting.md) · [Evidence and automated maintenance](../guides/maintenance.md)

## Primary evidence

[mkdocs-material](https://raw.githubusercontent.com/squidfunk/mkdocs-material/master/README.md) · [mcp-python](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md) · [plugins](https://raw.githubusercontent.com/openai/plugins/main/README.md)
