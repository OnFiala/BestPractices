# Local durable-service reference

This original, agent-authored teaching example makes the library's durability and
testing guidance executable. It uses Python's standard library, actual loopback
HTTP, and an actual SQLite database. It is proposed reference material for human
review, not a production service, authentication design, or payment implementation.

## Run it

From the repository root, with Python 3.12:

```sh
python -m examples.durable_service demo
python -m unittest discover -s tests -p test_durable_service.py -v
python -m examples.durable_service drills --output reports/durable-drills.json
python -m examples.durable_service benchmark --operations 120 --concurrency 8 --capacity 2 --delay-ms 10 --seconds 5 --output reports/durable-load.json
```

`uv run python` can replace `python` in the repository environment. No dependency,
service account, cloud deployment, paid API, or external destination is required.
Commands stop their servers and delete their temporary databases. JSON evidence
goes to stdout and optionally a file beneath ignored `reports/` or `/tmp/`.
The caller can stop a run with Ctrl-C. There is no arbitrary URL or bind-address
option in the experiment commands.

For a black-box test, obtain a fresh server this way:

```python
from examples.durable_service import FixtureServer, TOKEN_ALPHA

with FixtureServer() as fixture:
    print(fixture.url)  # http://127.0.0.1:<ephemeral-port>
    # Use an ordinary HTTP client and Authorization: Bearer synthetic-alpha-only.
```

`FixtureServer(db_path=path)` permits restart against an existing local fixture
database. Use a temporary directory or ignored reports directory. `.db_path`
exposes the database for explicitly gray-box integration checks. `.metrics`
provides admission counters. The context manager owns startup and shutdown;
reopening uses a new context manager. Its optional `fault` argument is strictly a
test harness control: it terminates the hosting process, so use only the isolated
child process in `experiments.py`. No HTTP request can turn fault injection on.

## HTTP and durable-state contracts

The literal tokens `synthetic-alpha-only` and `synthetic-beta-only` identify the
synthetic tenants `alpha` and `beta`. These are public test fixtures, never real
credentials. The server always binds `127.0.0.1`; it does not accept a host argument.
Do not tunnel, proxy, or expose it. There is no TLS, enrollment, revocation,
expiration, role model, session, or production authorization provider.

| Request | Contract |
| --- | --- |
| `POST /tenants/alpha/items` | JSON `{"id":"record","value":7,"expected_version":0}` and `Idempotency-Key: operation-1`; creates version 1 or replaces an item at the specified version |
| `GET /tenants/alpha/items/record` | Returns `{tenant,id,value,version}` or 404 within the authorized tenant |
| `GET /tenants/alpha/export` | Returns `{"items":[...]}` for the token's tenant, ordered by item ID |
| `POST /tenants/alpha/consume` | JSON `{}`; processes at most 100 pending events for that tenant and returns `{processed,effects,pending}` |

Every route requires the bearer token. Missing, unknown, or duplicate authorization
headers receive 401. A token addressing another tenant receives 403 for reads,
writes, exports, and consumption; supplying another tenant's item ID in the
authorized namespace finds no foreign record. Tenant context comes from the token,
and tenant predicates also constrain database access. The fixture deliberately
gives each tenant its own consume capability; it has no separate operator role.

IDs and keys contain 1–64 ASCII letters, digits, underscores, or hyphens. Payloads
have exactly the three documented fields; integer values are within ±1,000,000,
and expected versions are within 0–1,000,000. Booleans are not accepted as integers.
Duplicate JSON property names are rejected. POST bodies are limited to 4096 bytes and must use `application/json` with one
Content-Length; chunked input is unsupported. Invalid input receives 400, 413, or
415 without a business write. No list/search/delete/administration route exists;
unimplemented routes are not claimed as tested features.

`BEGIN IMMEDIATE` serializes SQLite writers. An item mutation, the saved operation
result, and an outbox event commit in one transaction. A key is scoped by tenant
and action (`items.upsert`). Identical canonical JSON replays return the original
result, even after a later version exists. Reusing a key for another payload yields
409 `idempotency_conflict`. A new key with a stale expected version yields 409
`version_conflict`. Denied, invalid, and version-conflicting attempts do not reserve
an operation key. This fixture retains operation keys and consumer receipts for
the lifetime of the database; it has no expiry or deletion policy.

Each outbox event has a stable random ID. Consumer processing transactionally
inserts a unique receipt/effect and increments a local tenant counter only if that
receipt is new. A separate commit marks the outbox event delivered. A crash between
these commits causes redelivery; the durable receipt prevents the second counter
increment. Concurrent consumers may select the same event and still produce one
local effect. There is no external message broker or provider call. The effect is
an append-only local event receipt and count, not fulfillment or a bank transfer.

## Fault drills and compatibility

`drills` starts dedicated Python subprocesses and terminates them with `os._exit(86)`
at precise boundaries, without graceful connection cleanup:

| Interruption | Oracle after reopening the database and retrying via HTTP |
| --- | --- |
| Before transaction commit | No item, saved result, or outbox event survived; retry creates exactly one of each |
| After commit, before HTTP response | All three survived; retry returns the stored version without another event |
| After consumer effect commit, before outbox acknowledgement | Effect and receipt survived while the event is pending; redelivery acknowledges it without incrementing twice |

These are real process termination and SQLite restart observations under the local
filesystem and `WAL`/`synchronous=FULL` configuration. They do not emulate power
loss, broken storage hardware, a partition, multi-host failover, or a provider's
ambiguous outcome. The child exit code and reconciled row counts are recorded.

The restore drill uses SQLite's backup API into a new file, then restores into a
separate new database and serves it in isolation. It proves that the snapshot's
item, operation, and pending event survive together and its local consumer can
resume. A known operation written after the snapshot is absent after restoration;
this makes the data-loss boundary visible. Existing destinations are refused.
Elapsed local drill time is not an agreed RTO, and the snapshot timing is not a
production backup/RPO policy. No backup encryption, offsite retention, corruption
repair, or tenant-selective restore is implemented. `integrity_check` and counts
cannot reconcile effects in another database or provider. Restoring deduplication
state to an earlier point can replay external effects: real operators must
reconcile those systems and authorize resumption before starting workers.

The migration drill writes and queues work with schema v1, expands to v2 in a
transaction, replays the old operation, and consumes both old and new events.
Version 2 adds an optional item label with an empty default and an outbox schema
version with a default of 1. A rolled-back SQL probe verifies that the original
column insert/read contract remains compatible. This is a SQL/event compatibility
demonstration, not an old application binary running alongside a new binary or a
large-table migration benchmark. Startup rejects newer unknown database versions;
the consumer rejects unsupported event versions without acknowledging those
events. Poison-event quarantine and operator resolution are deliberately omitted.
There is no destructive contraction or automatic down-migration. Rollback means
stopping the fixture and reopening a separately restored compatible snapshot,
with the same post-snapshot loss and external-effect reconciliation caveats.

## Bounded load and overload experiment

The benchmark self-starts one fixture, sends unique item writes from a closed-loop
worker population, stops scheduling at the operation or time bound, drains work,
then checks a successful recovery write and consumes the entire local backlog.
It asserts that the number of committed items, saved operations, events, receipts,
and effects equals successful requests plus the recovery operation, with no
pending events. Unexpected transport/HTTP outcomes or failed integrity make the
command exit nonzero. The `passed` flag and individual `checks` are saved alongside
failed response samples before returning a failing exit code. Rejection is expected
under stress; lower-load configurations need not produce 503s. The integration test explicitly requires both acceptance
and rejection with capacity 1, eight workers, and a 100 ms bounded fixture delay.

Hard input caps are 500 operations, 16 generator workers, 16 admitted server
workers, a 10-second scheduling window, and 250 ms artificial delay. Client/socket
timeouts are two seconds; the experiment allows a separate three-second drain
check. It stops scheduling at its deadline; already started requests may finish
afterward. There is no retry storm or background scheduled generator. Server
admission happens before thread creation: excess connections receive 503 and
`Retry-After: 1`. At most the configured worker count performs application work.
A single synchronous rejection handler drains a bounded request before closing
the connection; the kernel also has a bounded listen backlog. This simple handler
can delay acceptance behind a slow client and is not a production DoS defense.

The report separates configured operations, actually offered/started work,
completed HTTP responses, successful mutations, rejected responses, transport
errors, and work never offered before the deadline. Server admission counts are
captured before the recovery traffic. Raw per-operation timings are included.
Nearest-rank p50/p95/p99 estimates are segmented into success and rejection, with
sample counts: a small sample cannot establish a tail-latency objective. Rapid
503s can make aggregate latency look deceptively good.

The generator and target share a process, CPU, host, and filesystem. The report
records Python/SQLite/platform versions, total process CPU time, and database
bytes, but does not independently measure generator saturation, RSS, network
capacity, or storage latency. Closed-loop arrivals fall when responses slow.
Artificial delay demonstrates admission behavior and has no calibrated production
meaning. These experiments establish local invariants for the tested configuration;
they provide no user-count limit, capacity guarantee, or production latency promise.

## What the tests establish

`DurableHTTPContractTests` uses an independent standard-library HTTP client and
asserts outputs and prohibited effects through HTTP: allowed and denied tenant
access, payload/key conflicts, stable replay, invalid input, simultaneous retries,
and optimistic writer races. `DurableIntegrationTests` intentionally inspects
SQLite tables, fault checkpoints, migrations, and admission metrics as gray-box
evidence. Authenticated routes, serialization, sockets, SQL, locks, and process
restarts are real. Identity, business records, processing delay, and crash trigger
placement are controlled fixtures. There is no claim of independent human review,
full security assessment, external-provider compatibility, or production durability.

Related proposed guidance: [durability](../../docs/en/guides/durability.md),
[testing strategy](../../docs/en/guides/testing-strategy.md),
[security testing](../../docs/en/guides/security-testing.md), and
[performance testing](../../docs/en/guides/performance-testing.md).
