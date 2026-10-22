---
{
  "id": "tools",
  "language": "en",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Sources and tools

This is a shortlist for a defined decision, not an endorsement or an instruction to install every tool. Choose from project constraints and prove one representative workflow before adoption. Tool names and machine status keys remain stable across languages so agents and people identify the same product. `candidate` means evaluate before adoption; `used-here` describes a capability actually used by this library; `experimental` requires explicit compatibility checks. A used tool is not thereby suitable for every project.

The canonical inventory is `data/tools.json`; the source registry is `data/sources.json`. Website exports carry the same inventories. Source records separate the exact inspected version, the URL monitored for changes, and license evidence. These facts establish provenance and a review boundary, not approval to copy source prose. Source counts do not establish technical depth. No unknown license is treated as permission to reproduce documentation.

| Tool | Status | Source |
| --- | --- | --- |
| Codex | `candidate` | [codex](https://raw.githubusercontent.com/openai/codex/b337fe06b7d8d6e5b42295e04c5e92c2b9c46567/README.md), [plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md) |
| OpenAI Agents SDK | `candidate` | [openai-agents](https://raw.githubusercontent.com/openai/openai-agents-python/841dfdd938bfd4ca052475eb76d6245a356868e0/docs/agents.md), [agents-guardrails](https://raw.githubusercontent.com/openai/openai-agents-python/841dfdd938bfd4ca052475eb76d6245a356868e0/docs/guardrails.md) |
| MCP Python SDK | `used-here` | [mcp-python](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/2af9e3089ac66b35c1550c500aae86a82efb1e17/README.md) |
| WebMCP | `experimental` | [webmcp](https://raw.githubusercontent.com/webmachinelearning/webmcp/51ed75653aaa7f174f8dbe05d1bc327359bbc57c/README.md) |
| MkDocs Material | `used-here` | [mkdocs-material](https://raw.githubusercontent.com/squidfunk/mkdocs-material/cbee8f352745a974e1bae7dc595793be9b6875d7/README.md) |
| GitHub Actions | `used-here` | [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md), [github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) |
| PostgreSQL | `candidate` | [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml), [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml) |
| Docker / Compose | `candidate` | [docker-security](https://raw.githubusercontent.com/docker/docs/4d64a8e4f0a59967fc0b391120d54a90e9ccb60d/content/manuals/engine/security/_index.md) |
| Kubernetes | `candidate` | [kubernetes](https://raw.githubusercontent.com/kubernetes/website/bc7f3479bc8b0af48097b155c22c8d58e8e1afe4/content/en/docs/concepts/architecture/_index.md) |
| OpenTofu | `candidate` | [opentofu](https://raw.githubusercontent.com/opentofu/opentofu/ec773ed37be4d07e00d4a2fbb237d0c0fe1ca3ce/README.md) |
| OpenTelemetry | `candidate` | [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md) |
| Temporal | `candidate` | [durable-workflows](https://raw.githubusercontent.com/temporalio/temporal/e8ee627110a98501103827745aab18aedf312dd0/README.md) |
| Playwright | `candidate` | [playwright-testing](https://raw.githubusercontent.com/microsoft/playwright/ca7ca36145b84183cf423c2a099bd7e9cd8b1cb3/docs/src/best-practices-js.md) |
| Grafana k6 | `candidate` | [k6-test-types](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/testing-guides/test-types/_index.md), [k6-thresholds](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/using-k6/thresholds.md) |

## Choose by the task

Use Playwright for observable browser journeys, with isolated state and meaningful assertions; a browser script is not automatically an accessibility audit or a security assessment. Use k6 when a representative workload, latency/error thresholds, permitted environment, and abort budget have been defined. Merely generating more requests is not a useful capacity result. See the testing strategy, performance-testing, and security-testing guides before an agent runs these tools.

Agent orchestration needs permission boundaries, evaluated handoffs, and a total cost limit. Cloud/API usage can incur charges independently of whether a library is open source. The public repository runs metadata observation; source-fed AI generation belongs in a private review workspace. MCP hosting, plugin installation, and native WebMCP support require real integration checks. Never promote an experimental API or a newer model solely because it is recent. Confirm product support and retirement notices before adopting an example or buying a service.

Original prose in guide JSON exports is CC BY 4.0. Third-party software bundled in the site retains its own notices and licenses. The runtime dependency lock and asset notice inventory must change together when a new bundle changes redistribution obligations.

## Related decisions

[Skills, plugins, MCP, and WebMCP](../guides/integrations.md) · [Hosting and exit strategies](../guides/hosting.md) · [Evidence and automated maintenance](../guides/maintenance.md) · [Select and combine tests](../guides/testing-strategy.md) · [Performance testing](../guides/performance-testing.md)

## Primary evidence

[mkdocs-material](https://raw.githubusercontent.com/squidfunk/mkdocs-material/cbee8f352745a974e1bae7dc595793be9b6875d7/README.md) · [mcp-python](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/2af9e3089ac66b35c1550c500aae86a82efb1e17/README.md) · [plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md) · [playwright-testing](https://raw.githubusercontent.com/microsoft/playwright/ca7ca36145b84183cf423c2a099bd7e9cd8b1cb3/docs/src/best-practices-js.md) · [k6-test-types](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/testing-guides/test-types/_index.md)
