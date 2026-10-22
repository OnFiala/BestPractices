// Original small CDP driver. Node 22+ and an externally installed Chromium are required.
import assert from 'node:assert/strict';
import { spawn } from 'node:child_process';
import { access, mkdtemp, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { setTimeout as delay } from 'node:timers/promises';
import { startFixture, stopProcess } from './fixture-process.mjs';
import { waitForBrowserPort } from './browser-startup.mjs';

if (process.argv.length !== 2) throw new Error('No arguments accepted; this runner owns its local target.');
if (typeof WebSocket === 'undefined') throw new Error('Use Node 22+ with its built-in WebSocket.');

class DevTools {
  constructor(socket) {
    this.socket = socket;
    this.sequence = 0;
    this.pending = new Map();
    this.listeners = [];
    socket.addEventListener('message', ({ data }) => {
      const message = JSON.parse(data);
      if (message.id) {
        const pending = this.pending.get(message.id);
        if (!pending) return;
        this.pending.delete(message.id);
        clearTimeout(pending.timeout);
        if (message.error) pending.reject(new Error(JSON.stringify(message.error)));
        else pending.resolve(message.result);
      } else for (const listener of this.listeners) listener(message);
    });
    socket.addEventListener('close', () => {
      for (const pending of this.pending.values()) {
        clearTimeout(pending.timeout);
        pending.reject(new Error('Browser connection closed.'));
      }
      this.pending.clear();
    });
  }

  send(method, params = {}, sessionId) {
    const id = ++this.sequence;
    return new Promise((resolve, reject) => {
      const timeout = setTimeout(() => { this.pending.delete(id); reject(new Error(`CDP timeout: ${method}`)); }, 5000);
      this.pending.set(id, { resolve, reject, timeout });
      this.socket.send(JSON.stringify({ id, method, params, ...(sessionId ? { sessionId } : {}) }));
    });
  }
}

async function findBrowser() {
  const candidates = process.env.CHROME_BIN ? [process.env.CHROME_BIN] :
    ['/usr/bin/chromium', '/usr/bin/chromium-browser', '/usr/bin/google-chrome', '/usr/bin/google-chrome-stable'];
  for (const candidate of candidates) {
    try { await access(candidate); return candidate; } catch { /* try next installed binary */ }
  }
  throw new Error('Install Chromium separately or set CHROME_BIN to its absolute executable path.');
}

let fixture;
let browser;
let profile;
let devtools;
let cleaning;
const checks = [];
const passed = (...names) => { checks.push(...names); console.log(`PASS ${names.join(', ')}`); };
const cleanup = () => cleaning ??= (async () => {
  devtools?.socket.close();
  await stopProcess(browser);
  await fixture?.stop();
  if (profile) await rm(profile, { recursive: true, force: true, maxRetries: 3, retryDelay: 100 });
})();
for (const signal of ['SIGINT', 'SIGTERM']) {
  process.once(signal, () => { void cleanup().finally(() => process.exit(1)); });
}
const deadline = setTimeout(() => {
  console.error('FAIL: browser smoke exceeded its 45 second deadline.');
  void cleanup().finally(() => process.exit(1));
}, 45000);

try {
  const executable = await findBrowser();
  fixture = await startFixture();
  profile = await mkdtemp(join(tmpdir(), 'bestpractices-browser-'));
  const args = [
    '--headless=new', '--remote-debugging-port=0', '--remote-debugging-address=127.0.0.1',
    `--user-data-dir=${profile}`, '--no-first-run', '--no-default-browser-check',
    '--disable-background-networking', '--disable-component-update', '--disable-default-apps',
    '--disable-sync', '--disable-domain-reliability', '--disable-client-side-phishing-detection',
    '--disable-features=MediaRouter,OptimizationHints', '--metrics-recording-only', '--no-pings',
    '--host-resolver-rules=MAP * ~NOTFOUND, EXCLUDE 127.0.0.1',
    '--proxy-server=http://127.0.0.1:9', '--proxy-bypass-list=127.0.0.1',
    '--disable-dev-shm-usage', '--disable-crash-reporter', '--disable-breakpad', 'about:blank',
  ];
  // Explicit opt-in for disposable containers where Chromium's sandbox is unavailable.
  if (process.env.BP_BROWSER_NO_SANDBOX === '1') args.unshift('--no-sandbox');
  browser = spawn(executable, args, { stdio: ['ignore', 'ignore', 'pipe'] });
  let diagnostics = '';
  browser.stderr.on('data', (chunk) => { diagnostics = (diagnostics + chunk).slice(-2500); });
  const portInfo = await waitForBrowserPort(browser, profile, { diagnostics: () => diagnostics })
    .catch((error) => {
      throw new Error(`Browser startup failed (executable=${executable}; Node=${process.version}): ${error.message}`, { cause: error });
    });
  const [port, endpoint] = portInfo.trim().split(/\r?\n/);
  assert.match(port, /^[0-9]+$/);
  assert.match(endpoint, /^\/devtools\/browser\/[a-zA-Z0-9-]+$/);
  const socket = new WebSocket(`ws://127.0.0.1:${port}${endpoint}`);
  await new Promise((resolve, reject) => { socket.addEventListener('open', resolve, { once: true }); socket.addEventListener('error', reject, { once: true }); });
  devtools = new DevTools(socket);
  const version = await devtools.send('Browser.getVersion');
  console.log(`Browser: ${version.product}; Node: ${process.version}; owned loopback fixture`);
  const { targetId } = await devtools.send('Target.createTarget', { url: 'about:blank' });
  const { sessionId } = await devtools.send('Target.attachToTarget', { targetId, flatten: true });
  const send = (method, params) => devtools.send(method, params, sessionId);
  const runtimeErrors = [];
  const deniedRequests = [];
  const requests = [];
  const interceptionErrors = [];
  devtools.listeners.push((message) => {
    if (message.sessionId !== sessionId) return;
    if (message.method === 'Runtime.exceptionThrown') runtimeErrors.push(message.params.exceptionDetails.text);
    if (message.method === 'Fetch.requestPaused') {
      const { requestId, request } = message.params;
      const allowed = request.url.startsWith(`${fixture.origin}/`);
      if (allowed) requests.push(request.url); else deniedRequests.push(request.url);
      void send(allowed ? 'Fetch.continueRequest' : 'Fetch.failRequest',
        allowed ? { requestId } : { requestId, errorReason: 'BlockedByClient' })
        .catch((error) => interceptionErrors.push(error.message));
    }
  });
  await send('Page.enable');
  await send('Runtime.enable');
  await send('Fetch.enable', { patterns: [{ urlPattern: '*' }] });
  await send('Emulation.setDeviceMetricsOverride', { width: 1100, height: 900, deviceScaleFactor: 1, mobile: false });

  const evaluate = async (expression) => {
    const result = await send('Runtime.evaluate', { expression, returnByValue: true, awaitPromise: true });
    if (result.exceptionDetails) throw new Error(result.exceptionDetails.text);
    return result.result.value;
  };
  async function until(expression, label) {
    for (let tries = 0; tries < 100; tries++) {
      if (await evaluate(expression)) return;
      await delay(30);
    }
    throw new Error(`Timed out waiting for ${label}`);
  }
  const phase = (name) => until(`document.querySelector('#result-content')?.dataset.phase === ${JSON.stringify(name)}`, name);
  const keyCodes = { Tab: 9, Enter: 13, Home: 36, ArrowDown: 40, Backspace: 8, Escape: 27, a: 65 };
  async function key(key, modifiers = 0) {
    const params = { key, code: key === 'a' ? 'KeyA' : key, windowsVirtualKeyCode: keyCodes[key], modifiers };
    await send('Input.dispatchKeyEvent', { type: 'keyDown', ...params,
      ...(key === 'Enter' ? { text: '\r', unmodifiedText: '\r' } : {}) });
    await send('Input.dispatchKeyEvent', { type: 'keyUp', ...params });
  }
  async function click(selector) {
    await evaluate(`document.querySelector(${JSON.stringify(selector)}).scrollIntoView({block: 'center'})`);
    const box = await evaluate(`(() => { const r = document.querySelector(${JSON.stringify(selector)}).getBoundingClientRect(); return {x: r.x + r.width / 2, y: r.y + r.height / 2}; })()`);
    await send('Input.dispatchMouseEvent', { type: 'mousePressed', button: 'left', clickCount: 1, ...box });
    await send('Input.dispatchMouseEvent', { type: 'mouseReleased', button: 'left', clickCount: 1, ...box });
  }
  async function scenario(name) {
    const names = ['normal', 'empty', 'error', 'retry', 'slow', 'injection'];
    await evaluate("document.querySelector('#scenario').focus()");
    await key('Home');
    for (let i = 0; i < names.indexOf(name); i++) await key('ArrowDown');
    assert.equal(await evaluate("document.querySelector('#scenario').value"), name);
    await key('Tab');
    assert.equal(await evaluate('document.activeElement.id'), 'search');
    await key('Enter');
  }

  await send('Page.navigate', { url: `${fixture.origin}/?scenario=slow` });
  await phase('loading');
  assert.equal(await evaluate("document.querySelector('#result-content').getAttribute('aria-busy')"), 'true');
  await click('#cancel');
  await phase('cancelled');
  assert.equal(await evaluate('document.activeElement.id'), 'retry');
  await delay(1000);
  await phase('cancelled');
  assert.equal(await evaluate("document.querySelectorAll('#resource-list li').length"), 0);
  passed('loading', 'cancellation', 'late-response safety', 'cancellation focus');

  await send('Page.navigate', { url: `${fixture.origin}/` });
  await phase('success');
  await key('Tab');
  assert.equal(await evaluate("document.activeElement.className"), 'skip-link');
  await key('Enter');
  assert.equal(await evaluate('document.activeElement.id'), 'main');
  await key('Tab');
  assert.equal(await evaluate('document.activeElement.id'), 'query');
  const focusStyle = await evaluate('getComputedStyle(document.activeElement).outlineStyle');
  assert.notEqual(focusStyle, 'none');
  await send('Input.insertText', { text: 'testing' });
  await key('Enter');
  await phase('success');
  assert.equal(await evaluate('location.search'), '?q=testing');
  assert.equal(await evaluate("document.querySelector('#resource-list h3').textContent"), 'Testing the recovery path');
  const beforeDraft = requests.length;
  await send('Input.insertText', { text: ' draft' });
  assert.equal(await evaluate('location.search'), '?q=testing');
  assert.equal(requests.length, beforeDraft);
  await key('a', 2);
  await key('Backspace');
  await key('Enter');
  await phase('success');
  await evaluate('history.back()');
  await until("location.search === '?q=testing' && document.querySelector('#query').value === 'testing'", 'URL back navigation');
  await phase('success');
  await evaluate("document.querySelector('#query').focus()");
  await key('a', 2);
  await key('Backspace');
  passed('native keyboard', 'skip link', 'visible focus', 'search', 'draft isolation', 'history');

  await scenario('empty');
  await phase('empty');
  assert.match(await evaluate("document.querySelector('#status').textContent"), /No resources found/);
  await scenario('error');
  await phase('error');
  await click('#retry');
  await phase('error');
  assert.equal(await evaluate('document.activeElement.id'), 'search');
  const beforeRetry = requests.filter((url) => url.includes('/api/resources')).length;
  await scenario('retry');
  await phase('error');
  await click('#retry');
  await phase('success');
  assert.equal(requests.filter((url) => url.includes('/api/resources')).length - beforeRetry, 2);
  passed('empty', 'persistent error', 'explicit retry recovery', 'bounded request count');

  await scenario('slow');
  await phase('loading');
  await scenario('normal');
  await phase('success');
  await delay(1000);
  assert.equal(await evaluate("document.querySelectorAll('#resource-list li').length"), 3);
  assert.doesNotMatch(await evaluate("document.querySelector('#resource-list').textContent"), /Slow response arrived/);
  await scenario('injection');
  await phase('success');
  assert.equal(await evaluate("document.querySelector('#resource-list h3').textContent"), '<img src=x onerror="window.__injected=true">');
  assert.equal(await evaluate("document.querySelectorAll('#resource-list img, #resource-list script').length"), 0);
  assert.equal(await evaluate('window.__injected === undefined'), true);
  passed('superseded request', 'text-only rendering of HTML-shaped server strings');

  await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 1, mobile: false });
  assert.equal(await evaluate('document.documentElement.scrollWidth <= 390'), true);
  for (const selector of ['#query', '#scenario', '#search', '#compact']) {
    assert.equal(await evaluate(`(() => { const r = document.querySelector(${JSON.stringify(selector)}).getBoundingClientRect(); return r.left >= 0 && r.right <= 390; })()`), true, selector);
  }
  const beforeCompact = requests.length;
  await click('#compact');
  assert.equal(await evaluate("document.querySelector('#resource-list').classList.contains('compact')"), true);
  assert.equal(requests.length, beforeCompact);
  const tree = await send('Accessibility.getFullAXTree');
  for (const name of ['Search the library', 'Demo response', 'Compact view', 'Resource desk']) {
    assert.ok(tree.nodes.some((node) => node.name?.value === name), `Accessible name: ${name}`);
  }
  assert.deepEqual(runtimeErrors, []);
  assert.deepEqual(deniedRequests, []);
  assert.deepEqual(interceptionErrors, []);
  passed('390px overflow/control bounds', 'local-only display state', 'accessible names', 'no external page requests');
  console.log('Browser smoke passed. These checks do not establish full WCAG conformance or performance capacity.');
  console.log(JSON.stringify({ status: 'passed', browser_version: version.product, browser_path: executable,
    node_version: process.version, checks, check_count: checks.length,
    sandbox_disabled: process.env.BP_BROWSER_NO_SANDBOX === '1' }));
} catch (error) {
  console.error(`FAIL: ${error.stack ?? error}`);
  process.exitCode = 1;
} finally {
  clearTimeout(deadline);
  await cleanup();
}
