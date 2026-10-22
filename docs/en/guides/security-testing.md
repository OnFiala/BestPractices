---
{
  "id": "security-testing",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Select and run security tests

## Start with the boundary that could fail

Security testing supplies evidence about an explicit threat and control. Before choosing a scanner, identify the actor, entry point, protected asset, expected authorization and potential effect. Link applicable requirements from a named version of a standard such as ASVS, then define a test whose result can contradict the claim that the control works.

Black-box describes testing through observable interfaces without using implementation internals. It is not a synonym for security testing. Gray-box work may use test credentials, schema knowledge or telemetry; white-box work uses code and configuration. Combine perspectives when appropriate: code review can find an omitted tenant predicate, while a request from another tenant establishes whether the deployed path exposes data.

## Choose complementary techniques

| Technique | Appropriate trigger | What it cannot establish alone |
| --- | --- | --- |
| Source analysis and focused code review | New parsers, queries, rendering, file/network access or privileged paths | Actual runtime configuration, complete business authorization or absence of all vulnerabilities |
| Dependency and image analysis | New dependencies, lockfile/image updates, or vulnerability-feed changes | Exploitability in this deployment or correctness of custom application logic |
| Secret scanning | Changed files, build artifacts and relevant history | That every exposed credential is detected or that deleting a file revokes a credential |
| Infrastructure/configuration review | Network, IAM, storage, TLS, CI or deployment changes | That deployed settings match the proposed configuration without separate verification |
| Dynamic scanning of an owned test deployment | Web/API surface and configuration changed | Complete access control or complex workflow safety; authenticated coverage may be incomplete |
| Manual abuse cases and targeted API/browser checks | Authentication, permissions, tenancy, recovery, business logic or agent tools change | Broad coverage unless paths, roles and omitted cases are recorded |
| Fuzzing or property-based boundary checks | Parsers, file formats, protocol or validation code receives untrusted data | Correctness outside the input model or validity of the asserted security property |

Select tools compatible with the language, framework, protocol and intended test scope. A scanner result is a candidate finding: inspect reachability, prerequisites, impact and reproduction before assigning severity. An empty report means no findings under that configuration; it is not a security certificate.

## Concrete checks for common boundaries

For object authorization, create two distinct tenants and multiple roles. Exercise read, update, delete, list, search, export and asynchronous paths using identifiers outside the actor's scope. Include cached responses and permission changes. Check both the denial and the absence of disclosure or mutation; varying only the UI is insufficient.

For sessions, cover logout and revocation, expiration, privilege changes, account recovery and reuse of old credentials. For cookie-authenticated writes, exercise the framework's CSRF boundary. For rendering and input handling, include the contexts the application actually uses: HTML, database queries, file paths, uploads, and structured message parsing. Verify bounded failure without invoking an uncontrolled external endpoint.

For outbound fetching, use owned test destinations to exercise redirects, address changes and disallowed destinations. Check the executing network policy as well as input validation. Keep cloud metadata, internal services and real secrets outside the test unless specifically included in an authorized assessment.

For agents, test hostile retrieved content, forged tool output, unauthorized tool arguments, approval replay, changed parameters after approval, poisoned persistent memory, and delegated instructions that request broader access. Assert that the execution layer denies prohibited effects even if the model asks for them. Include benign tasks so a system that rejects every request is not incorrectly scored as useful and safe.

For supply-chain or CI boundaries, examine how untrusted code, workflow edits, dependency hooks and downloaded artifacts could reach credentials or publication rights. Validate the boundary in an isolated fixture where necessary. Do not use a real secret to prove that a secret could leak.

## Rules of engagement for agents

The task packet names the owner-approved targets, permitted identities, allowed techniques, time window, traffic limits, data rules, external dependencies, stop conditions and reporting destination. Use an isolated deployment with synthetic accounts whenever possible. Check that test credentials cannot reach production accidentally.

Permission to read a repository does not authorize active scanning of its production service. Broad project access does not authorize stress traffic, destructive payloads, external callbacks or third-party targets. Request the missing scope before those operations; continue static review and preparation independently.

Stop active tests when the target leaves scope, real user data appears unexpectedly, service health crosses the agreed limit, or containment/cleanup fails. Preserve minimal redacted evidence and notify the responsible owner through the authorized channel. Do not expand impact to make a finding more dramatic.

## Review, fix and verify

A useful finding records the tested revision/configuration, exact affected path, actor and prerequisites, observed behavior, expected protection, impact, and minimal reproduction. Separate confirmed, disproved, and unresolved candidates. Avoid publishing credentials, personal records or weaponized production details in a public issue.

Verify a fix against the original reproduction and an allowed legitimate operation. Add a regression that detects the underlying boundary failure rather than only matching one payload. Reassess sibling paths when the failure comes from a shared design. Record residual risk and human acceptance where complete remediation is deferred.

Release decisions use the threat model and evidence, not a universal scanner score. A high-consequence unresolved boundary blocks the affected release unless a qualified human explicitly owns a documented exception. Repeat targeted assessment when privileges, exposed surfaces, data sensitivity, dependencies or agent capabilities change.

## Evidence and related decisions

OWASP ASVS provides versioned verification requirements; the authorization, multi-tenant and agent guidance supplies concrete threat/control context. GitHub explains workflow-specific trust boundaries. The selection matrix and rules of engagement are original local policy; no source is claimed to endorse this particular project.

[Security architecture](security.md) · [Testing strategy](testing-strategy.md) · [Quality gates](quality.md) · [Human direction, agent execution](agents.md) · [Performance and stress testing](performance-testing.md)

## Primary evidence

[owasp-asvs-requirements](https://raw.githubusercontent.com/OWASP/ASVS/3383877f732ce89a458a1af43288f2f1b1d7db0c/5.0/docs_en/OWASP_Application_Security_Verification_Standard_5.0.0_en.csv) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-multi-tenant](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.md) · [owasp-session](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Session_Management_Cheat_Sheet.md) · [owasp-ssrf](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md)
