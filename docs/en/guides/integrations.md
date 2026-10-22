---
{
  "id": "integrations",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Skills, plugins, MCP, and WebMCP

## Distinct integration surfaces

| Surface | Role | Delivered here |
| --- | --- | --- |
| Skill | Repeatable agent procedure with scope and checks | Architecture-review and maintenance skills |
| Codex plugin | Manifest packaging skills and optional tools | Local skill-only bundle; installation still needs host verification |
| MCP | Host-to-server tool/resource protocol | Tested read-only stdio search and guide retrieval |
| ChatGPT Apps SDK | ChatGPT integration using MCP and optional UI | Integration guide; public hosting/authentication not provisioned |
| WebMCP | Browser-mediated tools inside a page | Experimental feature-detected search adapter |

OpenAI's former `skills` repository currently points to `plugins`. Follow the current plugin manifest examples; do not assume legacy ChatGPT plugins, Codex plugins, and Apps SDK apps are interchangeable.

## Local MCP

Run `uv run python -m library.mcp_server` from the checkout, or configure a host with `uv --directory /absolute/path/BestPractices run --frozen python -m library.mcp_server`. It exposes catalog, search, and known guide IDs, with no write or arbitrary-path tool. A ChatGPT remote connection needs a supported HTTPS transport, explicit authentication/rate limits, hosting, and a real host compatibility test. GitHub Pages cannot run that server.

## Browser experiment

The inspected WebMCP explainer uses `document.modelContext.registerTool`, abort-signal unregistration, and `toolchange` notifications. This is evolving work, not a universal browser guarantee. Feature-detect, preserve ordinary search, and test permissions, cancellation, navigation, and absent support. Do not invent standard events from proposals; application telemetry must use its own names. The bundled adapter exposes only public library search and emits no external analytics.

## Related decisions

[Human direction, agent execution](agents.md) · [Frontend architecture and contracts](frontend.md) · [Security, privacy, and supply chain](security.md) · [Evidence and automated maintenance](maintenance.md)

## Primary evidence

[plugins](https://raw.githubusercontent.com/openai/plugins/main/README.md) · [skills](https://raw.githubusercontent.com/openai/skills/main/README.md) · [openai-apps](https://raw.githubusercontent.com/openai/openai-apps-sdk-examples/main/README.md) · [mcp-python](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md) · [webmcp](https://raw.githubusercontent.com/webmachinelearning/webmcp/main/README.md)
