---
{
  "id": "integrations",
  "language": "en",
  "revision": 3,
  "translation_revision": 3,
  "reviewed_on": "2026-10-22"
}
---
# Skills, plugins, MCP, and WebMCP

## Distinct integration surfaces

| Surface | Role | Delivered here |
| --- | --- | --- |
| Skill | Repeatable agent procedure with scope and checks | `architecture-review`, `maintain-library`, `test-strategy`, `project-delivery`, and `release-review` |
| Codex plugin | Manifest packaging skills and optional tools | Local skill-only bundle; installation still needs host verification |
| MCP | Host-to-server tool/resource protocol | Read-only stdio search, guide retrieval, delivery planning/assessment, and coverage |
| ChatGPT Apps SDK | ChatGPT integration using MCP and optional UI | Integration guide; public hosting/authentication not provisioned |
| WebMCP | Browser-mediated tools inside a page | Experimental feature-detected search adapter |

OpenAI's former `skills` repository currently points to `plugins`. Follow the current plugin manifest examples; do not assume legacy ChatGPT plugins, Codex plugins, and Apps SDK apps are interchangeable.

## Local MCP

Run `uv run python -m library.mcp_server` from the checkout, or configure a host with `uv --directory /absolute/path/BestPractices run --frozen python -m library.mcp_server`. The stdio server exposes the catalog resource and `search_guides`, `get_guide`, `plan_delivery`, `assess_delivery`, and `get_coverage`, with no write or arbitrary-path tool. A ChatGPT remote connection needs a supported HTTPS transport, explicit authentication/rate limits, hosting, and a real host compatibility test. GitHub Pages cannot run that server.

Planning returns a conditional lifecycle plan; assessment evaluates supplied evidence records; coverage describes the declared guidance/reference scope and gaps. See the [project delivery workflow](project-delivery.md) and [coverage limits](coverage.md). These tools do not execute tasks or tests, authenticate reviewer labels or human approval, merge PRs, or deploy services. The host carries out authorized work through separate tools; local observations are not signed attestations.

## Browser experiment

The inspected WebMCP explainer uses `document.modelContext.registerTool`, abort-signal unregistration, and `toolchange` notifications. This is evolving work, not a universal browser guarantee. Feature-detect, preserve ordinary search, and test permissions, cancellation, navigation, and absent support. Do not invent standard events from proposals; application telemetry must use its own names. The bundled adapter exposes only public library search and emits no external analytics.

## What an integration must disclose

The returned guidance is agent-assisted, proposed content requiring human review. Preserve authorship, revision, source IDs, and content-license metadata when displaying or caching it. Prose remains CC BY 4.0 when transported in JSON; third-party source texts are not included or relicensed. A tool annotation such as read-only is descriptive, not server-side authorization. Do not give a retrieval connector production-write credentials or assume prompt instructions enforce a permission boundary.

Before adoption, run a real host compatibility test: successful search/read, unknown ID, unsupported locale, cancellation, malformed input, and an unavailable server. Mocked WebMCP tests cannot establish native browser support. Use the [testing strategy](testing-strategy.md) and [security testing](security-testing.md) guides to select further boundaries. Any source-fed generation must follow the private review and public-transfer boundary described in [maintenance](maintenance.md).

## Related decisions

[Human direction, agent execution](agents.md) · [Frontend architecture and contracts](frontend.md) · [Security, privacy, and supply chain](security.md) · [Evidence and automated maintenance](maintenance.md)

## Primary evidence

[plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md) · [skills](https://raw.githubusercontent.com/openai/skills/49f948faa9258a0c61caceaf225e179651397431/README.md) · [openai-apps](https://raw.githubusercontent.com/openai/openai-apps-sdk-examples/18cc38e78a968712c357bacdc3c79fead5bfc6b4/README.md) · [mcp-python](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/2af9e3089ac66b35c1550c500aae86a82efb1e17/README.md) · [webmcp](https://raw.githubusercontent.com/webmachinelearning/webmcp/51ed75653aaa7f174f8dbe05d1bc327359bbc57c/README.md)
