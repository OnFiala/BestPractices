const { test } = require("node:test");
const assert = require("node:assert/strict");
const vm = require("node:vm");
const fs = require("node:fs");
const code = fs.readFileSync("web/assets/webmcp.js", "utf8");

function harness(api, fetcher) {
  const events = {};
  const context = { document: { modelContext: api, currentScript: { src: "https://example.test/cs/assets/webmcp.js" } },
    window: { addEventListener: (name, fn) => { events[name] = fn; } },
    URL, AbortController, fetch: fetcher, console: { info() {} } };
  return { events, run: () => vm.runInNewContext(code, context) };
}

test("missing browser support leaves normal reading untouched", async () => {
  await harness(undefined, () => assert.fail("unexpected request")).run();
});
test("registers bounded read-only search, passes cancellation and cleans up", async () => {
  let tool, options, passedSignal;
  const h = harness({ registerTool: async (t, o) => { tool = t; options = o; } },
    async (url, request) => {
      assert.equal(url.href, "https://example.test/cs/guides.json");
      passedSignal = request.signal;
      return { ok: true, json: async () => [{ id: "data", title: "Obnova dat", content: "RPO restore", url: "guides/data/", status: "proposed" }] };
    });
  await h.run();
  const invocation = new AbortController();
  const result = await tool.execute({ query: "obnova" }, { signal: invocation.signal });
  assert.equal(passedSignal, invocation.signal);
  const rows = JSON.parse(result.content[0].text);
  assert.equal(rows[0].id, "data");
  assert.equal(rows[0].url, "https://example.test/cs/guides/data/");
  await assert.rejects(() => tool.execute({ query: "x".repeat(301) }));
  h.events.pagehide();
  assert.equal(options.signal.aborted, true);
});
test("denied registration and unavailable index are explicit", async () => {
  await harness({ registerTool: async () => { throw new Error("denied"); } }).run();
  let tool;
  await harness({ registerTool: async (t) => { tool = t; } }, async () => ({ ok: false })).run();
  await assert.rejects(() => tool.execute({ query: "data" }), /unavailable/);
});

test("bfcache restores search with a fresh controller without duplicate tools", async () => {
  const registrations = [];
  const h = harness({ registerTool: async (tool, options) => {
    registrations.push({ tool, signal: options.signal });
  } }, async () => ({ ok: true, json: async () => [] }));
  await h.run();
  assert.equal(registrations.length, 1);
  await h.events.pageshow({ persisted: false });
  await h.events.pageshow({ persisted: true });
  assert.equal(registrations.length, 1);
  h.events.pagehide();
  assert.equal(registrations[0].signal.aborted, true);
  await h.events.pageshow({ persisted: true });
  assert.equal(registrations.length, 2);
  assert.notEqual(registrations[0].signal, registrations[1].signal);
  assert.equal(registrations[1].signal.aborted, false);
  await h.events.pageshow({ persisted: true });
  assert.equal(registrations.length, 2);
  const result = await registrations[1].tool.execute({ query: "architecture" });
  assert.equal(result.content[0].text, "[]");
  h.events.pagehide();
  assert.equal(registrations[1].signal.aborted, true);
  await h.events.pageshow({ persisted: true });
  assert.equal(registrations.length, 3);
});
