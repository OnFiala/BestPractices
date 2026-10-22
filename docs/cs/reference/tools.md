---
{
  "id": "tools",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Zdroje a nástroje

Registr je výběr možností, nikoli požadavek vše instalovat. Vycházejte z omezení projektu a před přijetím ověřte reprezentativní průchod. Kandidáti nejsou touto knihovnou nainstalovaní ani otestovaní, pokud nemají used-here. MCP a sestavení dokumentace fungují místně; workflow vyžadují aktivaci GitHubu. Stav zdroje popisuje prohlédnutý dokument, negarantuje všechny vydané verze. Kontrolujte nainstalovanou verzi a API. Hash zachytí změnu, člověk posoudí význam, licenci a použitelnost. Názvy nástrojů zůstávají stejné pro jednoznačné rozpoznání. Před vystavením služby a přidělením přístupů čtěte integrace a hosting. Každý nový nástroj přináší náklady na aktualizace, obnovu i znalosti. Počet použitých nástrojů není měřítkem kvality architektury.

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

## Související rozhodnutí

[Skills, pluginy, MCP a WebMCP](../guides/integrations.md) · [Hosting a cesta k migraci](../guides/hosting.md) · [Důkazy a automatická údržba](../guides/maintenance.md)

## Primární zdroje

[mkdocs-material](https://raw.githubusercontent.com/squidfunk/mkdocs-material/master/README.md) · [mcp-python](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md) · [plugins](https://raw.githubusercontent.com/openai/plugins/main/README.md)
