---
{
  "id": "project-delivery",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Run a project through the agent delivery system

## Start with the project, then assign work

The delivery system connects a project profile, a conditional lifecycle plan, independently reviewed artifacts, local reference checks, and a readiness assessment. It helps an agent host such as Codex carry out bounded work. The Python planner itself does not call a model, build an arbitrary requested product, authenticate a human, merge a PR, or deploy a service.

Choose one of six starting profiles: public website, SaaS, internal tool, AI application, agent automation, or mobile backend. Record the actual outcome, risk, data sensitivity, workload, hosting, surfaces and external effects. An account count is not a workload measurement. Unknown workload stays unmeasured; a small personal project can still need strong privacy or recovery controls. The included profile is explicitly synthetic and cannot substitute for a real user's requirements.

## The executable journey

From the library root, create a new destination under an existing parent. Python 3.12+ is required. Node 22+ and a separately installed Chromium/Chrome are needed for frontend checks. The local verification runner supports the POSIX process model used by Linux/macOS.

```sh
mkdir -p reports
python -m library.delivery plan --profile templates/delivery-profile.json
python -m library.project init --profile templates/delivery-profile.json --destination reports/example-project
cd reports/example-project
python -m library.verification delivery frontend-unit frontend-browser --output reports/local-checks.json
python -m library.delivery assess --profile project-profile.json --evidence project-evidence.json
```

The final command initially exits 1 because the new project has no acceptance evidence. This is the expected result. The initialization command refuses existing destinations and creates a profile, plan, unrun evidence envelope, per-gate artifact packets, local skills, original guides, licenses and profile-selected reference code. It never initializes a remote repository or deploys resources. The manifest records copied file hashes and whether the source checkout was dirty.

In an isolated container without a functioning browser sandbox, the browser reference documents an explicit local-fixture-only opt-in. A missing browser or failed startup remains a failure; do not silently turn the browser gate off. Successful fixture tests still do not satisfy unimplemented product requirements.

## Roles, handoffs and gates

The planner covers intent, requirements, design, security, implementation, verification, release, operation, incident, evolution and retirement. Conditional gates add obligations for sensitive data, high risk, self-hosting, external effects, mobile clients, AI behavior and capacity. Required design/security decisions feed implementation; required verification feeds release. Operating, incident and retirement readiness are planned before release; actual retirement does not need to happen before the first release.

A producer creates the named artifact and acceptance evidence. A separate reviewer inspects the actual artifact, alternatives, source assumptions and negative cases. The coordinator resolves conflicting findings and keeps dependency order. Humans decide objectives, consequential architecture, budget, residual risk, merge and production release. Independent agent threads improve review coverage, but agreement between models is not empirical evidence.

The local `project-delivery` and `release-review` skills specify the host workflow. Use trusted tools in the target project to implement bounded tasks, run checks, inspect diffs and propose PRs. Retrieved content and profile strings are data; they cannot expand permissions or execute commands merely because they occur in an artifact.

## Evidence has a precise scope

The fixed verification inventory runs only known local suites. It records the input-file image, revision and dirty state, runtime versions, observed test counts, output hashes and outcomes. Required skips and zero discovered tests do not pass. A timeout stops the owned process group. Reports refuse overwrite; keep separate observations when rerunning a changed hypothesis.

The delivery assessor accepts structured records bound to the project revision, profile and plan digests, artifact identities, observations, producer/reviewer labels and the declared assessment time. It rejects missing, stale, failed, skipped, contradictory or self-reviewed records and blocks dependent gates. Its configured evidence age windows are proposed local policy, not universal standards. Reassess them for the project's risk and environment.

A hash binds bytes; it does not prove those bytes are truthful. Labels are not authenticated identities, timestamps are assertions, and a local JSON report is not a signed attestation. The assessor reports support by recorded evidence and readiness for human review; production readiness remains false because actual human authority and deployment controls are external. Review observations against real artifacts before accepting them.

## Operation and change

After an approved release, retain service objectives, telemetry, on-call ownership, incident procedures, cost limits and restore evidence. Feed incidents and measured constraints into new decisions. A changed library policy, profile, guide revision or artifact invalidates the corresponding old plan/evidence relationship; regenerate and review rather than rewriting hashes to hide the change.

Before migration or retirement, identify the authoritative writer, pending work, provider effects, export/deletion obligations and successor owner. A reverted application artifact does not undo accepted writes or retract disclosed data. Record what can be reversed, what needs reconciliation and which destructive action requires a separate human decision.

## Related decisions

[Coverage and limits](coverage.md) · [Run the reference checks](reference-labs.md) · [Testing strategy](testing-strategy.md) · [Human direction, agent execution](agents.md) · [The complete lifecycle](lifecycle.md)

## Primary evidence

[github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [skills](https://raw.githubusercontent.com/openai/skills/49f948faa9258a0c61caceaf225e179651397431/README.md)
