---
{
  "id": "security",
  "language": "en",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Security, privacy, and supply chain

## Turn risk into enforceable boundaries

Before handling sensitive data or granting tools write access, identify the assets, actors, entry points, and trust boundaries. Describe plausible misuse: a user supplies another tenant's record ID, a document asks an agent to export secrets, a CI job runs an untrusted dependency, or a recovery process restores the wrong customer's data. Assign each consequential risk an owner, preventive control, observable failure, and recovery action.

Choose a supported version of a verification standard such as OWASP ASVS and select requirements appropriate to the application. Record versioned requirement identifiers and local exceptions; linking an ASVS overview or completing a checklist is not certification. This guide is an original decision framework, not a reproduction of that standard.

## Identity, permissions, and tenants

Use maintained authentication components rather than inventing a password, session, or token protocol. Document account enrollment, recovery, revocation, and stronger authentication for sensitive actions. Separate recognizing an identity from deciding what that identity may do.

Make the trusted execution layer check the actor, target object, and requested operation. An opaque identifier, hidden button, private network, or successful login is insufficient permission evidence. Unknown access combinations should fail safely. Test read, write, search, export, administrative, and background paths, including access after membership changes.

Derive tenant context from verified membership. Apply that context to database queries, jobs, caches, file storage, retrieval indexes, and restoration. If database row policies provide an additional boundary, verify the actual runtime role does not bypass them and pooled connections do not retain another tenant's context. Treat operator-wide exports and cross-tenant administration as distinct capabilities.

For browser sessions, use supported cookie protections and deliberate expiration, logout, rotation, and revocation behavior. Cookie-authenticated state changes need CSRF protection appropriate to the framework; SameSite is a supplementary control. Authentication recovery and privilege changes deserve the same scrutiny as login.

## Data, rendering, and outbound requests

Keep private records, credentials, and customer fixtures out of public Git history, site builds, client bundles, and generated search indexes. Putting a login screen over publicly downloadable files does not make them private. Classify data before collection; define retention, deletion, export, backup handling, and who may investigate incidents.

Validate input against the application's contract. Use parameterized database operations and maintained output-encoding or sanitization facilities appropriate to the output context. Validation alone does not prevent script execution when data is rendered as HTML. Restrict file-upload size and type, storage location, and execution behavior.

A server or agent that fetches user-influenced URLs needs an outbound-request policy. Limit schemes, destinations, redirects, response size, and duration; prevent access to internal services and cloud metadata unless explicitly required and authorized. Resolve and check destinations at the network boundary so DNS changes and redirects cannot turn an apparently allowed URL into internal access.

## Agent and supply-chain boundaries

Treat retrieved text, tool output, model output, and delegated messages as untrusted data. Enforce tool access outside the model: bind identity and resource scope, validate arguments, and keep sensitive credentials in the execution service. An approval for a consequential operation must identify the action and parameters, expire, and resist reuse. A tool annotation or an agent saying “approved” cannot grant authority.

Constrain run duration, retries, concurrency, tokens, and spending at the layers that can enforce them. Isolate memory and retrieval by authorized user or tenant. Test indirect prompt injection, information leakage, policy changes, and multi-agent handoffs. Guardrails can reduce failures but are not a security perimeter.

Separate development, build, deployment, and runtime identities. Keep secrets out of repository content and use scoped, short-lived credentials where supported. Pin resolved dependency versions with a lockfile, verify update provenance and licenses, and monitor vulnerabilities. Pin CI actions to immutable commits and review who can alter workflows, artifacts, and dependency resolution. Never expose production credentials to untrusted PR execution or give an agent a host Docker socket.

## Verify, respond, and revisit

Use the [security-testing guide](security-testing.md) to connect threats to automated and manual evidence. Before releasing sensitive behavior, exercise unauthorized access, tenant separation, revocation, recovery, and misuse of privileged tools. Ensure logs support investigation without exposing credentials or unnecessary personal data; protect log access and retention too.

Record incident contact, containment steps, credential revocation, evidence preservation, restore procedure, and disclosure handling. Revisit the threat model after a new integration, privilege change, data class, incident, or architectural boundary change. Regulatory obligations and risk acceptance belong to qualified human owners.

## Related decisions

[Security testing](security-testing.md) · [Testing strategy](testing-strategy.md) · [Human direction, agent execution](agents.md) · [Data, contracts, and migrations](data.md) · [Operate your own servers](self-hosting.md)

## Primary evidence

[owasp-asvs-requirements](https://raw.githubusercontent.com/OWASP/ASVS/3383877f732ce89a458a1af43288f2f1b1d7db0c/5.0/docs_en/OWASP_Application_Security_Verification_Standard_5.0.0_en.csv) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-multi-tenant](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.md) · [owasp-authentication](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authentication_Cheat_Sheet.md) · [owasp-session](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Session_Management_Cheat_Sheet.md) · [owasp-csrf](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.md) · [owasp-xss](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.md) · [owasp-ssrf](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md)
