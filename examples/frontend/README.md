# Frontend reference: Fieldnotes resource desk

An original, framework-independent browser example, created with AI assistance
under human direction. This is a proposed reference for examining decisions,
not a production application or a prescribed frontend stack. All records are
synthetic; no provider account, credentials, package download, or model API is
needed to run it.

## Run it

From the repository root, use Python 3.12+:

```sh
python3 examples/frontend/server.py
```

Open the printed `http://127.0.0.1:<port>` URL. The default port is selected by
the operating system. An optional `--port 8001` selects a fixed local port;
there is deliberately no host or remote-target argument. Stop with Ctrl+C.
Open the printed numeric address: other Host headers, including `localhost`,
are rejected. No build step is required. Opening `index.html` as a file will
not provide the API or module loading behavior.

Try **Demo response** options and press **Search**. Normal results can be filtered
with `testing`; empty and error states can be forced. **Error, then retry succeeds**
fails its first attempt and succeeds after **Retry search**. **Slow response** takes
900 ms, allowing cancellation or a newer search. **Untrusted text** returns
HTML-shaped strings that must remain visible text.

## State and request ownership

| State | Owner | Lifetime and behavior |
| --- | --- | --- |
| Submitted query and fixture scenario | URL `q` and `scenario` parameters | Refresh and browser back/forward restore the query; submission adds history only when the query changes. Unknown scenarios fall back to normal. |
| Draft query and selected scenario before submission | Native form controls | Editing does not make a request or rewrite the URL. |
| Request phase and result records | `controller.mjs`, using `state.mjs` transitions | Each search replaces previous results. Only the current loading request can resolve, fail, or cancel. |
| Compact view | Checkbox and list class in `app.mjs` | Local to the open page; does not fetch, alter the URL, or write browser storage. |

`state.mjs` contains pure query normalization, response shape validation, and
result transitions. `controller.mjs` owns effects and injects its transport for
race tests. `app.mjs` connects native events to the controller and renders text
through DOM text nodes. `index.html` and `styles.css` provide the semantic page,
visible keyboard focus, skip link, persistent status region, and narrow layout.

Every request has a monotonically increasing identity. Starting a new request
aborts the previous transport and changes that identity. Completing work is
accepted only while that same request is still loading. Cancellation changes
the phase immediately, so even an already-resolved response body or a transport
that ignores abort cannot publish results afterward. `pagehide` cancels work;
a back-forward cache restoration starts the URL query again.

Requests are submitted explicitly. There is no polling, per-keystroke fetching,
prefetching, or automatic retry loop. One click of Retry makes one new request
for the previously submitted query. A retry does not accidentally send unsaved
draft input. The artificial `attempt=1|2` parameter makes retry outcomes
deterministic without a shared mutable server fixture.

This example clears old results during loading and failure rather than showing
data for a previous query under new filters. That costs continuity during a
request; a product that retains stale data should label its freshness and test
how users interpret it. Native HTML and small modules fit this single search
interaction. Revisit a framework, client cache, or server rendering only when
route complexity, reuse, discovery, or measured latency justifies their ownership
and deployment cost. Removing this directory reverses the example without a
database migration or remote resource cleanup.

## Fixture boundary

The Python standard-library server binds only to `127.0.0.1`, serves six explicit
asset paths, and exposes the read-only `/api/resources` route. Other files,
including its own source, are not downloadable. The API accepts at most three
query fields: `q` (at most 80 characters), an enumerated `scenario`, and `attempt`
(`1` or `2`). Duplicate, unknown, or oversized fields are rejected. Response delay
is fixed by scenario, not an arbitrary user-controlled duration. It does not
proxy URLs, execute query content, or log submitted text.

Browser fetches use a fixed relative route, omit credentials, reject redirects,
and avoid caching. The server sets a same-origin content security policy and
`Cache-Control: no-store`. Response shape checks support client correctness;
they do not make remote strings trusted. Titles, summaries, and status messages
use `textContent`; no server string is interpreted as markup or as an attribute.
The injection fixture intentionally contains an image event handler and script
text; the browser test checks both visible text and absence of inserted nodes.

**There is no authentication or authorization implementation here. Never put
backend secrets, session tokens, private records, or production credentials in
this browser example, its bundle, URL, or fixture data.** A production service
must enforce authentication, object permissions, and trusted validation on the
server. A hidden control or successful client validation is not that boundary.
The Host check and content policy are local containment measures, not evidence
that this development server is safe for Internet deployment.

## Verify it

Requires Node 22+ and Python 3.12+. There are no npm dependencies:

```sh
node --test tests/frontend.test.cjs
node examples/frontend/browser-smoke.mjs
```

The browser command also requires **a separately installed Chromium or Google
Chrome**. It looks for common Linux executable paths; set `CHROME_BIN` to an
absolute executable path elsewhere. The browser is not vendored, pinned, or
installed by this example. Pin and maintain that environment dependency in a
CI image if reproducibility requires it. The runner records the actual browser
and Node versions rather than claiming that installation is reproducible from
this repository alone. Set `BP_PYTHON` to a Python executable when the default
`python3` is not the intended interpreter.

Chromium's sandbox remains enabled by default. Some disposable containers lack
a working sandbox and fail before any test can run. Only for that controlled
environment, explicitly opt in to reduced browser process isolation:

```sh
BP_BROWSER_NO_SANDBOX=1 node examples/frontend/browser-smoke.mjs
```

That option is for the runner's synthetic local fixture, never browsing an
untrusted site. The JSON summary records `sandbox_disabled: true` when selected.
A missing browser or sandbox startup failure is a failed run, not a skipped pass.
This environment was exercised with Node v24.19.0, Python 3.12.14, and
Chrome/154.0.8037.57, with the explicit sandbox opt-in.

The runner starts its own ephemeral fixture and temporary Chromium profile,
drives real browser input through the Chrome DevTools Protocol using Node's
built-in WebSocket, and cleans up both child processes and its profile. Each
protocol command has a deadline. Browser startup allows up to 20 seconds for a
cold or busy CI host; an early process exit or spawn error fails immediately.
The whole run, including startup, retains its 45-second timeout. Regression
tests use real child processes to check readiness after five seconds, early
exit, spawn failure, and a readiness marker arriving after the deadline.
It accepts no target arguments. Requests from the page are intercepted and
allowed only to its fixture origin; background browser networking is disabled
and non-loopback browser proxy traffic is directed to an unavailable local
port. There is no external service exercised by this test. The last stdout
line is JSON containing `status`, `browser_version`, `checks`, and `check_count`;
any assertion or cleanup failure exits nonzero. A force-killed parent or machine
failure can still interrupt cleanup.

| Check packet | Knowledge, boundary, and objective | Failure it can reveal |
| --- | --- | --- |
| Pure state and injected transport tests | White box; unit; correctness and recovery | Old success/error replaces current results; cancelled response body is accepted; unsaved draft changes retry; automatic request amplification. |
| Actual fixture HTTP checks | Gray box; consumer/provider integration; contract and containment | Unexpected payload shape; query validation drift; source files exposed; unexpected Host accepted. The runner owns and stops the fixture. |
| Chromium journey | Public controls plus state observation; end-to-end; functionality, limited accessibility, and rendering safety | Loading/empty/error missing; retry fails to recover; cancellation or supersession leaves stale results; keyboard submit or skip link fails; focus is lost when an action disappears; HTML-shaped data becomes markup; horizontal overflow at 390 CSS pixels. |

The browser also checks URL back navigation, local-only compact view, accessible
names, and one API request per explicit retry. Unit races intentionally use a
transport that ignores abort to test the identity gate independently of browser
cancellation. Browser requests use the actual fixture transport. Neither is a
substitute for the other. Tests use synthetic data and a small fixed sequence,
with no load generation or production target.

These partial accessibility checks do **not** prove full WCAG conformance.
Assistive-technology use, contrast across changed palettes, zoom and text
spacing, broader devices, and supported browsers still need review. No latency,
throughput, or capacity claim follows from this smoke run. Before a production
decision, measure transferred assets and useful interaction latency on a
representative device/network, and confirm backend request volume stays bounded.

Production concerns intentionally absent include identity, write operations,
cross-user cache isolation, database persistence, deployment headers/TLS,
pagination, offline conflicts, dependency delivery, and release compatibility.
The threaded standard-library server is a development fixture without production
connection limits, abuse resistance, or operational controls. Keep it local.

Related library decisions: [frontend architecture](../../docs/en/guides/frontend.md),
[testing strategy](../../docs/en/guides/testing-strategy.md),
[performance testing](../../docs/en/guides/performance-testing.md), and
[security testing](../../docs/en/guides/security-testing.md).
