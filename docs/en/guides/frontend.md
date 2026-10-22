---
{
  "id": "frontend",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Frontend architecture and contracts

## Choose rendering by the interaction

Use static generation for content, server rendering when initial data/freshness or indexing matters, and client rendering for sustained interaction. Hybrid rendering is a choice per route. Document hydration cost, caching, authentication boundaries, and deployment behavior. Microfrontends are an organizational tradeoff for independently owned surfaces, not a default component model.

## Keep state understandable

Separate server state, URL/navigation state, local interaction state, and durable user preferences. Use one clear owner per state; avoid copying server data into multiple stores. Organize around product features and explicit interfaces; share accessible primitives before creating a large design system.

Define API schemas, errors, pagination, cancellation, and stale-data behavior. Validate inputs on the server and authorize every protected operation there. A hidden button is not authorization. Never put backend secrets in client bundles. Keep effects cancellable and subscriptions cleaned up; optimistic updates need a failure and reconciliation path.

## Verify and evolve

Test keyboard navigation, focus, accessible names, contrast, loading/empty/error/offline states, and a narrow viewport. Measure real navigation performance, payload size, interaction latency, and JavaScript errors. Add a backend-for-frontend only when aggregation or security boundaries justify it. Change frameworks when measurable constraints outweigh migration cost, including accessibility and dependency support. WebMCP is progressive enhancement: normal human interactions must remain usable without it.

## Related decisions

[Choose and connect architectures](architecture.md) · [Quality gates that prove behavior](quality.md) · [Skills, plugins, MCP, and WebMCP](integrations.md)

## Primary evidence

[wcag](https://raw.githubusercontent.com/w3c/wcag/main/guidelines/index.html) · [owasp](https://raw.githubusercontent.com/OWASP/ASVS/master/README.md) · [webmcp](https://raw.githubusercontent.com/webmachinelearning/webmcp/main/README.md)
