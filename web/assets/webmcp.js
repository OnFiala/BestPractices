/* Experimental adapter for the inspected WebMCP explainer, 2026-10-21.
 * Ordinary Material search works independently. No external telemetry or writes.
 */
(async () => {
  const api = document.modelContext;
  if (!api || typeof api.registerTool !== "function") return;
  const script = document.currentScript;
  if (!script) return;
  const indexURL = new URL("../guides.json", script.src);
  const registration = new AbortController();
  const normalize = (text) => text.normalize("NFD").replace(/\p{M}/gu, "").toLowerCase();
  try {
    await api.registerTool({
      name: "search-bestpractices",
      description: "Search public architecture guidance in this page's language. Read only; results include maturity and sources.",
      inputSchema: { type: "object", properties: { query: { type: "string", minLength: 1, maxLength: 300 } }, required: ["query"], additionalProperties: false },
      async execute({ query }, options = {}) {
        if (typeof query !== "string" || !query.trim() || query.length > 300) throw new Error("Invalid query");
        const response = await fetch(indexURL, { signal: options.signal });
        if (!response.ok) throw new Error("Library index unavailable");
        const records = await response.json();
        const terms = normalize(query).trim().split(/\s+/);
        const results = records.filter((g) => terms.every((term) => normalize(g.title + " " + g.content).includes(term)))
          .slice(0, 8).map(({ content, ...g }) => ({ ...g, excerpt: content.slice(0, 500), url: new URL(g.url, indexURL).href }));
        return { content: [{ type: "text", text: JSON.stringify(results) }] };
      }
    }, { signal: registration.signal });
    // toolchange belongs to the browser API; do not synthesize standard events.
    window.addEventListener("pagehide", () => registration.abort(), { once: true });
  } catch (error) {
    // Missing permission/API compatibility must not break normal document reading.
    console.info("Optional WebMCP search unavailable:", error.name);
  }
})();
