# Onboarding correction and publication candidate

A fresh-reader review found two insufficiently connected adoption paths, a weak
localized first step, and no continuous example of producing one real evidence
record. This change gives new readers one recommended route in all four languages:
adoption, one first gate, then a project-specific playbook and host-agent task.

The strict JSON delivery profile is now distinguished from the optional richer
YAML decision brief. The guide explains deliberate field mapping, data that stays
in decisions, and the difference between the library revision and the target
project revision. Existing-project use does not call init over an existing folder.
README and localized homepages give a directly usable bounded agent prompt.

The new first-project guide creates a local intent document and an actual Git
commit. No successful review or reviewer identity is generated. A separate
reviewer must inspect the actual document before submitting their observations.
An accepted document review supports only intent-brief; release stays blocked.
The explicit walkthrough observation is in
[onboarding-walkthrough.json](2026-10-22-onboarding-walkthrough.json): zero supported
gates before review, one after, seventeen still blocked. Changed bytes and a
missing reviewer both prevented new evidence and preserved the initial packet.
This was independent agent inspection of original document text, not human
approval or an executed website acceptance test.

## Validation

[The exact-input record](2026-10-22-onboarding-checks.json) captures 89 passing
Python tests, 4 passing WebMCP fixture tests, the five fixed reference suites
(including 12 frontend tests and 20 actual Chromium checks), content validation,
Ruff, actionlint and a strict 136-page site build with link/language/search checks.
The Python reference suites are subsets of the 89 tests. No required test was
skipped. The browser used the explicit no-sandbox exception only for the owned
synthetic local fixture in this container. It is not evidence of production
browser isolation, exhaustive accessibility or native WebMCP support.

All seven runnable tutorial blocks are byte-identical across the four languages;
the surrounding explanations, review table and stop conditions are translated.
There are now 34 catalog entries and 82 representative claim mappings. None of
those counts establishes complete software-engineering coverage.

## Sources and rights

The new explanations and exercise are original library work. Existing immutable
primary citations are preserved and the tutorial is explicitly local synthesis.
No external source text, screenshots or new third-party code were imported.
Dependency notices and licensing remain unchanged.

The independent review's [latest tracking observation](2026-10-22-onboarding-source-observations.json)
reports two changed source documents, owasp-csrf and owasp-multi-tenant, with zero
unavailable or overdue records. Immutable references and the reviewed baseline
remain unchanged. Tracking drift requires inspection; a green build does not
accept upstream changes or convert a reference-only source license into reuse rights.

## Publication boundary and rollback

The Pages build now explicitly has contents:read and pages:read for its pinned
configure-pages metadata lookup. Deployment remains a separate job with pages:write
and id-token:write. The workflow is manually dispatched and restricted to main.
External Pages/environment configuration is separate from these repository files.
This record does not assert that merge, remote approval or deployment has occurred.
The user's specific instruction authorizes merging and publishing this candidate
only after independent review and successful checks; it does not grant future
unattended agents permission to approve or merge their own work.

Revert this onboarding commit to restore the previous navigation and profile
explanations. A deployed site rollback requires a separately selected reviewed
commit and another manual publication; a source revert alone does not replace
already published bytes. The existing local delivery/evidence authority contracts
and proposed-guidance status are unchanged.
