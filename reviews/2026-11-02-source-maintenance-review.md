# Source maintenance recovery

Agent-authored proposal. Human baseline acceptance, merge and publication remain
separate decisions. No repository security setting, credential or approval policy
was changed.

## Failure and scope

The scheduled observation failed on the retired data-partitioning document.
The following proposal job pushed `automation/source-observations` but GitHub
refused PR creation. A pushed branch is not evidence that a PR exists.
The precise repository/organization setting responsible was not established.

All nine Azure registry entries and their active citations are removed. Eleven
guides, their four locales, the catalog, claim mappings and coverage references
use inspected alternatives. These sources describe mechanisms in independent
projects; they do not prescribe adopting those products or any cloud provider.
The partitioning paragraph now explicitly distinguishes PostgreSQL table
partitioning from distributed sharding and multi-region guarantees.

| Replacement evidence | Inspected support and important limit |
| --- | --- |
| Spring Modulith fundamentals | Internal APIs and dependency boundaries; the topology comparison remains library synthesis. |
| Apache Pekko Projection use cases | Read/write separation and projected models; one-store layouts and freshness budgets remain local choices. |
| Apache Pekko event sourcing | Persisted events, replay, evolution, deletion and external side-effect limits; no remote exactly-once guarantee. |
| Redis cache-aside | Origin fallback, expiry, invalidation and miss storms; advertised latency and cost claims are not adopted. |
| PostgreSQL table partitioning | Keys, pruning, constraint limits and maintenance/planning costs; not distributed sharding evidence. |
| Kubernetes probes | Health/readiness distinctions, restarts, traffic removal and cascading/resource risks; no orchestration requirement. |
| RabbitMQ reliability | Lost acknowledgements and duplicate delivery; application deduplication and reconciliation remain synthesis. |
| Debezium Quarkus outbox | Event persistence within the business transaction and subsequent CDC relay; no external-effect atomicity. |
| gRPC retry guide | Eligible failures, attempt limits, backoff/jitter, throttling and transparent retries; total cross-layer budgets remain local policy. |

Exact commits, inspected URLs, SHA-256 values, publisher, scope and license evidence
are in `data/sources.json`. Documentation is reference-only; no source bodies,
examples or diagrams were copied into the repository. Mixed documentation/code
licenses and Redis's noncommercial/share-alike terms are recorded explicitly.

## Baselines and historical evidence

Only the nine retired entries are removed from the monitoring baseline. All 44
retained records are unchanged. The nine replacements carry
`baseline_status: pending-human-review` and have no accepted baseline entry.
Validation requires every source to have either its matching baseline or an
explicit pending status, never both, and still enforces immutable references,
hash format, claim hash bindings and locale citation equality. Observation
reports pending sources even when retrieval succeeds, and detects changes from
their inspected hash. It never writes the baseline.

The original reports below are unchanged historical attribution, not active
recommendations or monitored sources:

- `2026-10-22-overlap-evidence.json`
- `2026-10-22-operational-originality.json`
- `2026-10-22-operational-evidence.json`
- `2026-10-22-operational-control.md`
- `2026-10-22-onboarding-source-observations.json`

They still name the sources actually inspected in October. Rewriting them would
misrepresent that work. Git history and the previous observation branch are
preserved. The candidate in this proposal contains only the current registry.

## Inspection of the nine pre-fix hash drifts

| Observed source | Assessment and disposition |
| --- | --- |
| Retired architecture styles | Diagram accessibility description changed; source removed from active use. |
| Retired idempotent consumer | Added HTTP idempotency crosslink; source removed from active use. |
| Retired retry pattern | Added the same HTTP crosslink; source removed from active use. |
| Material for MkDocs | README now announces end of life on May 5, 2027 and a successor. PR #6 repairs the 9.8.0 license inventory; generator migration requires a separate compatibility decision. |
| OWASP ASVS overview | Added a Persian translation link. No change to the pinned English control set was established by this index diff. |
| OWASP CSRF | Revised cookie-default caveats, explicit attributes and destination-scoped token attachment. Current guidance already treats SameSite as supplementary; framework and browser behavior still require project verification. |
| OWASP multi-tenant | Replaced a long lifecycle example with requirements, clarified credential entropy and deletion/key retention across copies. Existing tenant/retention guidance remains compatible; no sample was imported. |
| OWASP XSS | Clarified text sinks, CSS value/URL constraints, attribute context and Trusted Types limits. Existing context-specific encoding and validation caveats remain compatible; no universal safe-attribute claim is adopted. |
| WebMCP | Added `outputSchema` to discovery metadata and removed it from the exploratory list. The current adapter returns text content and declares no output schema; a new structured result contract needs separate native-host compatibility evidence. Mock tests do not establish that compatibility. |

No drift baseline was accepted and no old review date was refreshed merely from
retrieval. Private diffs and source bodies were inspected locally and are not
public artifacts. The current metadata candidate reports six changed sources,
nine awaiting an initial baseline, zero unavailable and zero overdue sources
among 53 tracked entries.

## Review path and reversal

The default workflow uses read-only observation, a metadata artifact and a run
summary with manual draft-PR instructions. Optional automated proposals now
require `ENABLE_SOURCE_REVIEW_PRS=true`; the existing GitHub policy must also
allow PR creation. If an optional proposal fails, the summary warns that a
branch may already exist and points back to the artifact path. No alternate
token or permission bypass is introduced. A green observation run establishes
reachability, not accepted guidance or baseline approval.

Maintenance instructions and revisions are aligned in all four languages.
The synthetic delivery-evidence template's plan digest is recalculated for the
changed guide revisions; its `example: true`, unrun records, empty observations
and unverified human approval remain unchanged. No recorded execution report
was rehashed. A validation test now selects its source by stable ID rather than
depending on the retired source's former array position.

Revert the proposal commit to restore the previous configuration, while noting
that doing so also restores the unavailable source and unsupported automatic
PR attempt. No deployment, data migration or remote resource change is involved.

## Verification

Ruff, validation of 34 guides in four languages, all 93 Python tests, four
WebMCP tests, all five reference verification groups and coverage assessment,
the strict four-language build, and generated link/anchor/search checks passed.
The local browser run used the documented container exception only for the
owned synthetic fixture. An earlier full-suite attempt exposed the stale
synthetic plan digest and the positional source test; both were corrected and
the complete suite rerun. Baseline and historical-report preservation were
checked against `origin/main`. Active data, documentation, workflows, runtime
code, examples and skills contain no Azure source or dependency references.

The live source check returned exit 0 with the counts above; its metadata is in
`data/source-observations.json`. GitHub must run Validate for the final pushed
commit. The modified scheduled workflow has not been executed on GitHub by
this local verification; its default/optional permission boundaries and
metadata-only export paths are covered by tests. No native WebMCP host,
production service, deployment or human approval was exercised.
