---
{
  "id": "coverage",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Read coverage and verification honestly

## Use the declared coverage map

The machine-readable coverage registry describes the lifecycle domains supported by this edition. Each record links guidance and primary references, names any executable reference and exact test cases, defines the narrow claim, and lists evidence still needed in an adopting project. The map is a declared scope, not a claim to enumerate all of software engineering.

Read it through `python -m library.coverage`, the read-only MCP tool, or the exported website data. An optional local verification report can add observations bound to the current input image. A website's static registry does not become a fresh executed result because a reader opens it.

## Separate the kinds of support

| Support | What exists | What remains unknown |
| --- | --- | --- |
| Documented guidance | An original decision explanation and scoped source links | Whether the explanation applies to this project or has been implemented |
| Executable reference | Original code and named checks that can exercise a stated local boundary | Whether those checks were run on these exact inputs and what happened |
| Current recorded observation | Matching input hashes and a passed recorded suite with the required named cases | Whether the report is authentic, the oracle is sufficient, or a different target behaves the same way |
| Missing, stale, failed or partial observation | Required evidence is absent, changed, failed or incomplete | The unsupported claim stays unsupported; do not infer success from silence |

Every local result remains subordinate to its scope. SQLite process-restart evidence does not prove replicated-store recovery. A short closed-model loopback run does not prove a million-user workload. A deterministic fixture model does not establish real-model quality. A single Chromium smoke check does not establish complete accessibility or a supported-browser matrix.

## Ask the right completion question

For a concrete project, identify which requirements and failure consequences matter. Select the corresponding playbook and planner gates, then map each acceptance obligation to an observable result. Check denied effects, persisted state and recovery alongside successful responses. Record deliberately omitted tests and their risk rather than marking an entire domain complete from one passing example.

A reviewer should inspect the source proposition, implementation boundary, test oracle, executed artifact and environment. A matching hash only establishes identity. Source counts, translated-page counts and a green dashboard cannot replace that chain. Local reports and role labels are not signed attestations or authenticated human approval.

## Maintain gaps explicitly

The registry names extensions needing additional project work: native clients and devices, regulated or safety-critical behavior, hard-real-time systems, multi-region failover, large data/training pipelines, production identity/payment integrations and long-duration capacity. General guidance can still inform those projects, but this edition does not contain an executed reference for each specialized boundary.

When expanding a domain, add original guidance, source support, a falsifiable reference where useful, negative cases, limitations and all four language versions. A source change triggers semantic review; a new test result belongs to its exact inputs. Keep historical reports as dated evidence rather than silently replacing their meaning. Human adoption remains a separate decision.

## Related decisions

[Agent delivery workflow](project-delivery.md) · [Reference checks](reference-labs.md) · [Quality gates](quality.md) · [Evidence maintenance](maintenance.md)

## Primary evidence

[github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md) · [owasp-asvs-requirements](https://raw.githubusercontent.com/OWASP/ASVS/3383877f732ce89a458a1af43288f2f1b1d7db0c/5.0/docs_en/OWASP_Application_Security_Verification_Standard_5.0.0_en.csv)
