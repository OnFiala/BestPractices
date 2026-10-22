---
{
  "id": "playbook-mobile-backend",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Deliver a backend for mobile clients

## Fit and supported-client contract

Use this profile for a backend serving installed clients that may remain offline, retry writes, and update at different times. Record the supported client/API versions, maximum offline interval, protected data allowed on devices, sync freshness, revocation policy, and recovery objectives. This agent-authored proposal concerns backend and protocol delivery. It does not claim a native client, secure device storage, push integration, or platform accessibility has been implemented.

Start with a modular API, canonical relational data, and a bounded synchronization path. An online-only application is a simpler alternative if the user task permits it. Offline editing adds durable operation identity, conflict handling, deletion semantics, and support cost. Add regional placement, specialized sync infrastructure, or partitioning only after measuring sync lag, conflict frequency, write contention, payload size, or geographic latency. Installed-device count alone is not a migration trigger.

## Boundaries and data model

Separate `api/`, `policy/`, `domain/`, `sync/`, `contracts/`, and `ops/`. The server owns canonical state and authorization. A device identifier is a routing/audit attribute, not proof of user authority. Validate access on reads, sync downloads, uploads, and credential refresh. Push messages should signal that permitted data may be available, rather than carry sensitive record contents.

For each offline mutation, define a stable operation ID, authenticated principal, record ID, base revision, and intended change. Store deduplication results within the transaction that applies the mutation. Reusing an ID with a different change must conflict. Use server-controlled revisions to detect stale edits; device clocks are unsuitable as the sole authority for ordering business changes.

Choose conflict policy per domain. An editable note may present both versions for human merge. An inventory reservation should reject a stale precondition or enforce a transactional invariant rather than silently choose the latest clock. Tombstones or equivalent deletion knowledge must outlive the supported offline interval. If a sync cursor expires, require a documented full resynchronization that does not silently resurrect deleted records or lose pending local intent.

## Deliver in a safe sequence

1. Discovery maps read/offline/edit/reconnect journeys, data classification, supported versions, and conflict examples. A human owner accepts offline retention and upgrade policy.
2. Implementation builds a versioned API and synthetic client harness before a full sync path. Add operation deduplication, conditional updates, pagination/cursors, deletion, and observable sync status with explicit error contracts.
3. Verification runs old and new consumers against transitional schemas and simulates two devices, network interruption, revocation, and restoration. The release owner sets staged rollout and client-support retirement criteria.

Hand over a profile, API and sync schema, compatibility matrix, conflict ADR, operation examples, device-data requirements, migration plan, observed contract/recovery results, support window, and named backend/client owners. `examples/durable_service` can inform local persistence experiments. It is not a mobile sync engine or evidence of native-device behavior; real client/platform verification remains a separate deliverable.

## Exercise absence of unintended effects

Use unit tests for merge/state rules, integration tests for transactions and authorization, and contract tests for the oldest supported client plus the candidate. A version label alone does not establish compatibility. Check optional fields, unknown enum handling, pagination, error codes, units, and deleted-record behavior. Use an actual device or platform emulator for native cache, credential-storage, background-work, and push behavior once a client exists.

Have two synthetic devices edit the same revision offline, then reconnect in both orders. The oracle is the declared conflict result with preserved user intent, not merely two successful responses. Interrupt an upload after commit, replay it, and inspect canonical records: there must be no extra business effect. Replay the operation ID with altered content and require conflict. Delete a record while another device is offline; a stale update must not resurrect it outside the declared rule.

Revoke a device/session before refresh and protected sync. It must not regain access through a refresh path; test any documented access-token grace window explicitly. Simulate cursor expiry and restore to an older server backup: clients must detect incompatible sync history, reconcile pending operations, and resynchronize safely. Measure recovery time, actual data loss, sync lag, conflict rate, and bandwidth under bounded poor-network conditions. Keep untested platform behavior visible.

## Rollout, operations, and retirement

Expand contracts and schema before deploying consumers; support mixed client versions throughout the published window. Backfill with checkpoints, validate sync invariants, and remove old fields only when the support policy permits it. A backend rollback cannot force installed clients to update or erase downloaded data. Restore into isolation, establish a new sync epoch or equivalent recovery marker when needed, and reconcile operations before reopening writes.

Monitor failures by client/API version, oldest pending operation, conflict rate, resync volume, refresh denial, and notification delivery without logging protected payloads. Assign owners for backend incidents and client compatibility separately. Budget storage, transfer, push-provider usage, support for old versions, and recovery drills. Production gaps include real identity, device storage, network security, native background behavior, push credentials, and consent/retention. Retirement gives clients an actionable end-of-support response, offers authorized export, drains pending work where possible, revokes credentials, and handles retained offline copies under the agreed policy.

## Continue with related decisions

[Frontend contracts](frontend.md) · [Data and migrations](data.md) · [Security](security.md) · [Testing strategy](testing-strategy.md)

## Primary evidence

[owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-session](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Session_Management_Cheat_Sheet.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [semver](https://raw.githubusercontent.com/semver/semver/f99d5485190a47c0863949e7da810a5553e0ed4d/semver.md)
