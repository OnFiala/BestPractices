# Initial verification — 2026-10-21

Current-instance evidence, not a claim of publication or human editorial approval.

| Check | Outcome |
| --- | --- |
| Frozen dependency synchronization | Passed; Python 3.12, uv 0.12.23, committed hash lock |
| Content validation | 21 guides × 4 languages; identities, revisions, sources, links |
| Python suite | 11 passed, 0 skipped; includes real stdio MCP calls and rejected traversal |
| Browser-adapter tests | 3 passed, 0 skipped; missing support, input limits, cancellation, denial |
| Strict static build | 84 localized pages built |
| Generated site checks | Local resources, anchors, same-page language switches and indexes passed |
| Chromium interaction | EN/CS/DE/ES search and language switching passed; 390px mobile layout passed |
| HTTP behavior | Expected English guide and Czech homepage returned successfully |
| Primary-source observation | 23 available, 0 changed from initial baseline, 0 overdue |
| Workflow validation | actionlint 1.7.12 passed; action references use full commit SHAs |

The browser test must simulate typing/keyup for Material search; filling a value
without the expected keyboard events was not a valid interaction test. The discovered
cross-language link-generation defect was corrected and the full link check rerun.

Material emits a notice about a future incompatible MkDocs 2 transition. This build
uses the locked, tested 1.6.1 renderer. See ADR-0001 for the migration boundary.
Optional theme GitHub statistics/sitemap lookups can fail under this environment's
network policy; document reading, local search, and language links were verified.

Not yet verified: GitHub-hosted workflow runs, enforced rulesets, Pages deployment,
native browser WebMCP support, Codex plugin installation, paid agent execution, or a
remote ChatGPT connection. A mocked browser API is not evidence of native support.
Translations need human editorial review; this report does not approve their meaning.

## GitHub connectivity — 2026-10-22

The initial API restriction was resolved after the environment configuration changed.
The repository API now reports a public repository and write access using the existing
platform authentication. GitHub plugin tools are still unavailable in this chat;
the handoff uses the GitHub CLI/API. Reading Actions permission settings returns
`Resource not accessible by integration` (HTTP 403), so repository access must not be
mistaken for permission to administer every GitHub feature.

The remote has no branches before the handoff. An empty `main` commit provides the
base for the library proposal; all content is submitted in a separate PR for human
review. Consult that PR for the actual GitHub-hosted check results. No website
deployment or paid agent run is implied by the local results above.

The saved install/start instructions and network additions are now returned as the
published cloud configuration. Restoring the complete project into a fresh task has
not been independently verified.
