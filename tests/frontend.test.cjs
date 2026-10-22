const assert = require('node:assert/strict');
const { test } = require('node:test');
const { request } = require('node:http');
const stateModule = import('../examples/frontend/state.mjs');
const controllerModule = import('../examples/frontend/controller.mjs');
const item = { id: 'r1', title: 'A result', summary: 'Synthetic text' };
const response = (items = [item]) => ({ ok: true, json: async () => ({ items }) });
const deferred = () => {
  let resolve;
  let reject;
  const promise = new Promise((yes, no) => { resolve = yes; reject = no; });
  return { promise, resolve, reject };
};

test('URL state is bounded, encoded, and round-trips without adopting an arbitrary target', async () => {
  const { readQuery, queryString, normalizeQuery } = await stateModule;
  const query = { q: 'testing & <script> / café', scenario: 'retry' };
  assert.deepEqual(readQuery(queryString(query)), query);
  assert.deepEqual(readQuery('?q=++state++&scenario=https://example.invalid'), { q: 'state', scenario: 'normal' });
  assert.equal(normalizeQuery({ q: 'x'.repeat(100) }).q.length, 80);
  assert.equal(queryString({ q: '', scenario: 'normal' }), '');
});

test('response contract rejects malformed records while retaining HTML-shaped text as data', async () => {
  const { decodeResources } = await stateModule;
  const hostile = { ...item, title: '<img src=x onerror=alert(1)>' };
  assert.deepEqual(decodeResources({ items: [hostile], futureField: true }), [hostile]);
  for (const payload of [null, {}, { items: {} }, { items: [null] }, { items: [{ ...item, title: 7 }] },
    { items: Array(21).fill(item) }, { items: [{ ...item, summary: 'x'.repeat(501) }] }]) {
    assert.throws(() => decodeResources(payload), /Unexpected response/);
  }
});

test('loading clears prior data, then empty/error/cancel phases do not keep misleading results', async () => {
  const { transition, initialRemoteState, statusText } = await stateModule;
  let state = transition(initialRemoteState(), { type: 'start', requestId: 1 });
  assert.equal(state.phase, 'loading');
  state = transition(state, { type: 'resolve', requestId: 1, items: [item] });
  assert.equal(state.phase, 'success');
  state = transition(state, { type: 'start', requestId: 2 });
  assert.deepEqual(state.items, []);
  state = transition(state, { type: 'resolve', requestId: 2, items: [] });
  assert.equal(state.phase, 'empty');
  assert.match(statusText(state), /No resources/);
  state = transition(state, { type: 'start', requestId: 3 });
  state = transition(state, { type: 'reject', requestId: 3, message: 'Please retry.' });
  assert.equal(state.phase, 'error');
  assert.deepEqual(state.items, []);
  state = transition(state, { type: 'start', requestId: 4 });
  state = transition(state, { type: 'cancel', requestId: 4 });
  assert.equal(state.phase, 'cancelled');
  assert.strictEqual(transition(state, { type: 'resolve', requestId: 4, items: [item] }), state);
});

test('superseded success and failure cannot replace a newer result even when transport ignores abort', async () => {
  const { createResourceController } = await controllerModule;
  for (const lateFailure of [false, true]) {
    const calls = [];
    const controller = createResourceController({ fetcher: (url, options) => {
      const pending = deferred(); calls.push({ ...pending, url, options }); return pending.promise;
    } });
    const old = controller.search({ q: 'old' });
    const current = controller.search({ q: 'new' });
    assert.equal(calls[0].options.signal.aborted, true);
    calls[1].resolve(response([{ ...item, title: 'Current result' }]));
    await current;
    if (lateFailure) calls[0].reject(new Error('late failure')); else calls[0].resolve(response());
    await old;
    assert.equal(controller.getState().phase, 'success');
    assert.equal(controller.getState().items[0].title, 'Current result');
  }
});

test('cancel remains final for that request even after the response body arrives', async () => {
  const { createResourceController } = await controllerModule;
  const body = deferred();
  const controller = createResourceController({ fetcher: async () => ({ ok: true, json: () => body.promise }) });
  const pending = controller.search({ scenario: 'slow' });
  await Promise.resolve();
  controller.cancel();
  body.resolve({ items: [item] });
  await pending;
  assert.equal(controller.getState().phase, 'cancelled');
  assert.deepEqual(controller.getState().items, []);
});

test('retry is explicit, bounded to one request per action, and uses the submitted query', async () => {
  const { createResourceController } = await controllerModule;
  const calls = [];
  const controller = createResourceController({ fetcher: async (url, options) => {
    calls.push({ url, options });
    return calls.length === 1 ? { ok: false } : response();
  } });
  await controller.search({ q: 'testing', scenario: 'retry' });
  assert.equal(controller.getState().phase, 'error');
  assert.equal(calls.length, 1);
  await controller.retry();
  assert.equal(controller.getState().phase, 'success');
  assert.match(calls[1].url, /^\/api\/resources\?q=testing&scenario=retry&attempt=2$/);
  assert.equal(calls[1].options.credentials, 'omit');
  assert.equal(calls[1].options.redirect, 'error');
  await controller.retry();
  assert.equal(calls.length, 2);
});

test('owned loopback fixture serves the consumer contract and rejects files/queries outside its allowlist', { timeout: 10000 }, async (t) => {
  const { startFixture } = await import('../examples/frontend/fixture-process.mjs');
  const fixture = await startFixture();
  t.after(() => fixture.stop());
  const { decodeResources } = await stateModule;
  const get = (path) => fetch(`${fixture.origin}${path}`, { signal: AbortSignal.timeout(2000) });
  const normal = await get('/api/resources');
  assert.equal(normal.status, 200);
  assert.equal(decodeResources(await normal.json()).length, 3);
  assert.equal(normal.headers.get('cache-control'), 'no-store');
  assert.match(normal.headers.get('content-security-policy'), /connect-src 'self'/);
  assert.equal((await (await get('/api/resources?q=testing')).json()).items.length, 1);
  assert.deepEqual(await (await get('/api/resources?scenario=empty')).json(), { items: [] });
  assert.equal((await get('/api/resources?scenario=error')).status, 503);
  assert.equal((await get('/api/resources?scenario=retry&attempt=1')).status, 503);
  assert.equal((await get('/api/resources?scenario=retry&attempt=2')).status, 200);
  const injection = decodeResources(await (await get('/api/resources?scenario=injection')).json());
  assert.match(injection[0].title, /^<img/);
  for (const path of ['/server.py', '/README.md', '/.git/config', '/%2e%2e/README.md']) {
    assert.equal((await get(path)).status, 404, path);
  }
  for (const query of ['q=a&q=b', 'scenario=unknown', 'attempt=3', 'target=https://example.invalid', `q=${'x'.repeat(81)}`]) {
    assert.equal((await get(`/api/resources?${query}`)).status, 400, query);
  }
  const denied = await new Promise((resolve, reject) => {
    const req = request(fixture.origin, { headers: { Host: 'example.invalid' }, timeout: 2000 }, (res) => {
      res.resume(); resolve(res.statusCode);
    });
    req.on('error', reject); req.on('timeout', () => req.destroy(new Error('timeout'))); req.end();
  });
  assert.equal(denied, 403);
});
