/* Experimental adapter for the inspected WebMCP explainer, 2026-10-21.
 * Ordinary Material search works independently. No external telemetry or writes.
 */
(async () => {
  const api = document.modelContext;
  if (!api || typeof api.registerTool !== "function") return;
  const script = document.currentScript;
  if (!script) return;
  const indexURL = new URL("../guides.json", script.src);
  let registration = null;
  const normalize = (text) => text.normalize("NFD").replace(/\p{M}/gu, "").toLowerCase();
  const tool = {
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
    };
  async function register() {
    if (registration) return;
    const controller = new AbortController();
    registration = controller;
    try {
      await api.registerTool(tool, { signal: controller.signal });
    } catch (error) {
      if (registration === controller) registration = null;
      // Missing permission/API compatibility must not break ordinary reading.
      console.info("Optional WebMCP search unavailable:", error?.name || "Error");
    }
  }
  // bfcache restores this document without running its scripts again.
  window.addEventListener("pagehide", () => {
    registration?.abort();
    registration = null;
  });
  window.addEventListener("pageshow", (event) => {
    if (event.persisted) return register();
  });
  // toolchange belongs to the browser API; do not synthesize standard events.
  await register();
})();
