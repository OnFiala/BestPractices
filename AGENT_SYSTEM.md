# Agent-maintained decision system

This library is created and maintained with AI agents. It is decision support for
humans and other agents, not an autonomous authority or a certification service.
The English guidance and Czech, German, and Spanish translations are agent-assisted
drafts until a human reviews their meaning and approves publication. The website
and machine-readable guide responses disclose this origin.

## Responsibilities and boundaries

| Role | Permitted work | Required handoff |
| --- | --- | --- |
| Human architect/owner | Set objectives, budget, risk tolerance, and decision criteria | Project profile, approved scope, named reviewer |
| Research agent | Inspect primary evidence and its version/license | Claim support, immutable source reference, limitations; no republished source prose |
| Implementation agent | Write original guidance/code inside an assigned scope | Reviewable diff, rationale, executed checks, recovery plan |
| Verification agent | Independently challenge assumptions, examples, translations, and behavior | Reproducible findings, coverage, missing evidence |
| Human reviewer | Decide applicability, originality/rights, acceptance, merge and publication | Explicit approval of the actual proposed output |

Different model passes can find mistakes, but agreement among models is not
independent empirical evidence. Tests, source inspection, runtime measurements, and
human review answer different questions. Preserve negative results and uncertainty.

## Maintenance and publication

The public repository may observe source URLs and propose metadata-only source
updates. It must not publish fetched source documents, source excerpts, model logs,
or an unreviewed summary merely to demonstrate provenance. A hash proves the bytes
observed, not their truth or permission to reproduce them.

Source-fed automated generation runs only in a private repository/workspace. A
separate trusted consumer accepts bounded structured proposal data; agent-modified
scripts or Git metadata are not a trust root. Private logs and artifacts still need
access controls, retention limits, and credential hygiene. Before any transfer to a
public PR, a human reviews the actual prose/code for original expression, source
use, license obligations, sensitive data, factual support, and translation meaning.
No private generation service or automatic public-transfer service is deployed here.

Agents never approve or merge their own changes, widen their permissions, change
publication rules, or mark recommendations human-approved. Local MCP tools only
retrieve public library content; they do not authorize deployment or production tests.
WebMCP is experimental and normal reading/search works without it.

## Selecting and evaluating agent work

Start with the outcome, failure consequences, and observable acceptance criteria.
Use the testing-strategy, performance-testing, and security-testing guides to choose
appropriate methods. A black-box test can be functional, security-oriented, or
performance-oriented; its limited knowledge is separate from its purpose.

Record scope, environment, credentials, permitted traffic, resource/cost ceilings,
abort conditions, evidence retention, and the human responsible for elevated risk.
An agent must report an unrun or inconclusive test as such. It must not interpret a
green smoke test or a similarity screen as complete assurance.
