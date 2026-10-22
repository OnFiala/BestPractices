# Agent-system, evidence, rights, and engineering review

Review date: 2026-10-22. Initial reviewed artifact:
`f5b327c22ffd35d3ed7e31fc387b3aef20fcab82`, compared with the empty initialization
base `df54744`. Remediation is proposed in
[PR #1](https://github.com/OnFiala/BestPractices/pull/1). This report does not approve
merge, publication, legal compliance, translation meaning, or production adoption.

## Review organization and scope

A separate read-only control reviewer used **gpt-6-astra with maximum reasoning**.
Specialist agents reviewed architecture and lifecycle, security/testing evidence,
implementation boundaries, source and redistributed-software licenses, and
translation quality. Czech, German and Spanish remediation had separate ownership.
The coordinator reconciled the findings and tested the assembled result. Seven
specialist/control agents participated; agreement between models is not independent
empirical evidence or a substitute for human review.

The final control pass found no remaining release blocker within its inspected
scope. It independently rechecked the earlier translation omissions and the
testing/scope/limits/recovery clauses in Czech, German and Spanish, verified the
53 source/license commit pairs, and confirmed the final page/evidence hash
inventory. One minor Codex license-revision mismatch and the inaccurate “private
fork” wording were corrected before closure. Integrated execution results below
belong to the coordinator's verification, not to an unperformed second test run.

The review covered original Markdown, four locales, catalog/source/tool/project
registries, the static-site builder and exported content, read-only MCP, WebMCP
adapter, proposal/source workflows, project templates, and local skills. Source
checks distinguish actual requirements and mechanism documentation from repository
README introductions. Review depth is recorded for representative consequential
claims in [evidence.json](../data/evidence.json); it is not exhaustive sentence-level
proof.

## Findings and resulting behavior

| Finding in the initial artifact | Consequence | Remediation and evidence |
| --- | --- | --- |
| High: site distributions lacked required third-party notices and corresponding source | Theme, search, dependency and icon material could be published under incomplete or misleading license information | `library/licensing.py` inventories retained assets, checks dependency versions and file hashes, publishes notices/legal files and unchanged MPL source, and rejects unknown or altered assets. Every guide links to the notice page. |
| High: source-fed generation could expose model output publicly before rights review | A public log, artifact or draft PR can already disclose copied expression before a human rejects the merge | Both model and proposal jobs now require a private repository. No public override or automatic public transfer exists. A human must check originality and rights privately before transferring prose to a public PR. No private generation service has been provisioned or exercised. |
| Medium: ignored artifact paths and a symlink could bypass the old export boundary | An agent could export an ignored file outside the intended changed-file set | Removed `export_patch` and its CLI. The model is the last producer step and emits bounded JSON; a fresh trusted checkout validates the entire proposal before writing. Negative tests cover paths, links, duplicate properties, budgets, identity/maturity changes and malformed input. |
| Medium: mutable citations and broad source lists weakened review reproducibility | A source could change after the claimed review; an introductory README did not directly establish detailed advice | Recorded immutable commits, inspected URLs and content hashes, separate tracking URLs, document-license evidence and representative claim mappings. Validation rejects stale hashes, unpinned citations and missing claim references. |
| Medium: testing/security guidance was too compressed for agent selection | Agents lacked concrete criteria for when to use a particular test and what a result could establish | Added testing strategy, performance/stress and security-testing guides; expanded quality/security chapters. Knowledge model, exercised boundary and objective are independent axes. A test-plan template and skill capture scope, workload, oracle, limits, stopping, recovery and evidence. |
| Medium: architecture recommendations and examples omitted consequential boundaries | Generic scaling or rollback advice could hide write ownership, ambiguous side effects, recovery or team capacity | Expanded architecture matrices, frontend state/contracts/accessibility, hosting/data migration, durability, operations, lifecycle and six reference profiles. User count alone does not select topology. Reference acceptance packets are explicitly planned, not executed. |
| Medium: the static/personal-project example could mix private notes with a public site | Private Git history, generated assets or search indexes could remain publicly downloadable despite a login UI | Public content and private knowledge-base requirements are now explicit; access control must cover documents, assets, downloads and search at an enforceable boundary. |
| Medium: license scope depended ambiguously on file container | CC BY prose exported inside JSON could be mistaken for MIT metadata | `LICENSE-CONTENT` preserves the prose license across HTML, JSON/YAML, search and MCP; original code/configuration and factual metadata use MIT. Third-party material retains its own terms. |
| Medium: translation revisions and brief summaries did not establish meaning parity | Caveats, negative cases or new advice could disappear in a locale | Rewrote complete Czech/German/Spanish counterparts to the expanded English edition. Compared terminology, obligations, negation, tables, links and examples. Metadata parity and structural checks supplement editorial review; no native-speaker approval is claimed. |
| Low: WebMCP registration did not survive back/forward cache restoration | Returning to a page could leave browser tools permanently unavailable | A fresh controller/register cycle runs on restoration; a browser-API simulation checks lifecycle behavior. Native WebMCP support remains unverified and experimental. |

The system is now labeled as agent-assisted in the README, every rendered guide,
MCP/JSON exports and `llms.txt`. [AGENT_SYSTEM.md](../AGENT_SYSTEM.md) defines human
and agent authority. All initial guidance remains proposed; tests do not promote it
to adopted policy.

## Evidence and rights review

The registry contains **53 primary-source documents**, each with an immutable
reviewed URL and SHA-256 digest, plus a mutable monitoring URL. The 57 representative
claim records distinguish direct support from local synthesis and state limits.
Sources include substantive architecture patterns, PostgreSQL mechanisms, OWASP
requirements and cheat sheets, Playwright guidance, k6 test mechanisms, WCAG
criteria and OpenAI/agent ecosystem documentation. A larger source count by itself
is not a quality score.

Document-license review classified **43 grants as reviewed, one as mixed, and nine
as unresolved**. The unresolved cases are OpenAI plugin/skill index material and
seven k6 documentation pages. Runtime software licenses must not be assumed to
cover separate documentation. All 53 entries are reference-only for this library;
no permission to reproduce their expression is inferred from a citation.

Original explanations, decision tables and examples are independently written.
Translations translate this library's own English text. Raw research documents
remain outside the public repository, generated site, logs and artifacts.
[PROVENANCE.md](../PROVENANCE.md) prohibits copied, translated or closely paraphrased
upstream prose. Required software notices and corresponding source are a separate,
explicitly licensed redistribution, not library advice relabeled as our code.

The static distribution inventory covers 16 components and 12 retained vendor files
per locale. Legal files, upstream evidence and corresponding source are tracked in
[THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md) and
[third-party-assets.json](../data/third-party-assets.json). It does not inventory a
redistributed Python environment or container; such a product needs its own review.

A finite literal-overlap screen compared all **96 localized pages and 57 claim/limits
pairs** with all 53 byte-verified source snapshots (1,156,007 bytes; 145,787 Unicode
word/number tokens). It found **zero normalized exact sequences of ten or more
consecutive tokens**. Front matter, source footers, URLs and markup were excluded;
body text, tables and code examples were retained. Required third-party notices and
program source were outside this original-prose screen. The
[measurement inventory](2026-10-22-overlap-evidence.json) records method, source and
page hashes, exclusions and limitations without republishing source bodies.
The control reviewer separately sampled actual source mechanisms and performed an
independent twelve-word overlap check; it likewise found no exact match.
No literal-overlap screen establishes legal clearance: translated expression,
close paraphrases, unregistered sources, diagrams, trademarks and other rights can
fall outside that method. Ambiguous reuse requires a concrete rights determination.

## Verification record

| Check on assembled remediation | Observed outcome |
| --- | --- |
| Frozen dependency sync and Ruff | Passed with the committed lock |
| Catalog/provenance validation | 24 entries × 4 locales; titles/revisions, immutable source/license pins, claim hashes and citations passed |
| Python tests | 25 passed, 0 skipped; includes a real stdio MCP round trip, proposal boundary and license-publication regressions |
| Browser-adapter tests | 4 passed, 0 skipped; includes back/forward cache restoration with a mocked WebMCP API |
| Workflow syntax | All four workflows passed actionlint 1.7.12 |
| Strict static build | 96 localized pages built with required third-party notices/source |
| Generated-site checks | Local links/anchors, same-page language switches, indexes, agent disclosures and notice links passed |
| Real Chromium interaction | All four locale searches returned the durability guide; same-page language links, disclosures and notices passed; 390 px mobile page had no horizontal overflow; no page errors |
| Live source observation | 53 observed; 0 changed, 0 unavailable, 0 overdue |
| Editorial/structural locale review | All 72 translated counterparts passed final heading/table/link/code-token parity; specialist meaning reviews and independent high-consequence clause checks completed |
| Working-tree whitespace | `git diff --check` passed |

The browser run used the installed `/usr/bin/chromium`; the default Playwright
bundled-browser lookup was unavailable and was corrected before the successful run.
The mocked WebMCP lifecycle result remains separate from real-browser reading/search.
Material's notice about a future MkDocs 2 migration does not change the pinned
MkDocs 1.6.1 build; see ADR-0001. No such framework migration was attempted.

GitHub-hosted results for the final pushed commit are visible on
[PR #1](https://github.com/OnFiala/BestPractices/pull/1). This report records the
local assembled checks; it does not substitute an earlier CI run for the final
commit's status.

## Practical limits and follow-up

- Human editorial, source-applicability and rights review is still required before
  adoption/publication. No agent approved or merged its own proposal.
- This pass creates guidance for selecting security, black-box, load, stress, spike,
  soak and recovery checks. It did not stress-test or penetration-test an adopter's
  service, and the reference project packets are not capacity certifications.
- The security implementation review was manual, with code inspection, a benign
  reproduction and regression checks. Formal Codex Security scan/preflight tools
  were unavailable in this environment; no completed formal scan is claimed.
- A point-in-time PyPI metadata check covered all 58 locked registry packages and
  found no listed advisories. This is neither a full supply-chain audit nor proof
  that those versions have no vulnerabilities.
- Native WebMCP hosting, remote ChatGPT/MCP integration, paid generation and private
  proposal transfer were not exercised. Their configuration files are not proof of
  deployment, supported host APIs, bounded provider spending or enforced rulesets.
- Future updates must preserve claim/source/translation alignment, inspect source
  changes semantically, and review new redistributed assets. An observation never
  accepts a new baseline or updates production policy by itself.

To roll back a proposed implementation change, revert its commit through a reviewed
PR and rebuild with the pinned dependencies. Do not restore the old unsafe exporter
or remove legally required notices from an already distributed artifact. Retain
corresponding-source availability for the period required by its upstream license,
including when a website is retired or moved.
