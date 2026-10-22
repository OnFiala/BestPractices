---
{
  "id": "security",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Security, privacy, and supply chain

## Start from assets and boundaries

List sensitive data, actors, entry points, trust boundaries, and credible abuse cases. Choose controls proportional to impact, not project size. Validate on trusted servers, authorize every object/action, minimize collected data, and define retention and deletion. Regulatory and domain obligations require qualified human review; this library is not a compliance certificate.

## Delivery and runtime

Use separate identities for development, CI, and production; short-lived scoped credentials where supported; secret stores and rotation. Pin dependencies with a lockfile and actions by immutable commit. Review dependency updates, license changes, provenance, and vulnerability alerts. Keep TLS, signatures, and checksums enabled.

Never run untrusted pull-request code with production secrets or privileged `pull_request_target` workflows. Do not mount a host Docker socket into an agent workspace. Restrict tool destinations and operations; tool descriptions and retrieved documents are untrusted input. Model instructions alone do not enforce authorization.

## Verify and respond

Test access across tenants, denied actions, session revocation, and secret rotation. Review logs for sensitive data leakage. Record an incident contact, containment procedure, recovery, and disclosure path. Before releasing a sensitive feature, review its threat model and evidence. Raise protection when data sensitivity or blast radius increases; do not postpone it until user count grows.

## Related decisions

[Human direction, agent execution](agents.md) · [Operate your own servers](self-hosting.md) · [Data, contracts, and migrations](data.md)

## Primary evidence

[owasp](https://raw.githubusercontent.com/OWASP/ASVS/master/README.md) · [docker-security](https://raw.githubusercontent.com/docker/docs/main/content/manuals/engine/security/_index.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/main/content/actions/reference/security/secure-use.md)
