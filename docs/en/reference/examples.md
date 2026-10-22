---
{
  "id": "examples",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Reference project paths

## Six concrete starting paths

| Project | Initial architecture | First proof | Expansion trigger |
| --- | --- | --- | --- |
| Public website | Static build and CDN; Git content | Search, keyboard access, content rollback | Trusted user writes need an API |
| SaaS | Modular app, relational database, worker | Tenant isolation, payment reconciliation, restore | Measured contention or independent teams |
| Internal tool | SSO, small app, audit trail | Revoked account cannot read/export | Ownership and integration boundaries diverge |
| AI application | API gateway, model adapter, retrieval with access filters | Grounded answers, denied documents, provider timeout | Measured quality/cost or isolation need |
| Agent automation | Queue, bounded worker, durable run ledger, scoped tools | Duplicate task, budget stop, approval before writes | Independent workloads require queues/owners |
| Mobile + backend | Native/cross-platform UI, versioned API, local cache | Offline edits, conflict handling, old client compatibility | Measured sync or regional latency constraints |

Each path has an executable-design packet in `data/blueprints.json`: boundaries, acceptance examples, failure recovery, and migration signals. These are design references, not deployed starter applications. Copy the matching profile and turn its acceptance examples into tests for your actual stack.

For mobile, assume clients cannot all upgrade immediately. Prefer additive API changes, resumable synchronization, explicit conflict rules, device credential revocation, and platform-secure storage. For AI, retrieval must preserve document authorization and deletion; a plausible answer is not evidence of correctness. For internal tools, corporate network access does not replace per-action authorization.

Agree budgets, service objectives, data residency, and recovery targets with the human owner before launch. A small team may choose a managed platform across all six paths; the interfaces and obligations remain distinct.

## Related decisions

[Adopt the library in a project](../guides/adoption.md) · [Choose and connect architectures](../guides/architecture.md) · [Human direction, agent execution](../guides/agents.md) · [Frontend architecture and contracts](../guides/frontend.md)

## Primary evidence

[owasp](https://raw.githubusercontent.com/OWASP/ASVS/master/README.md) · [openai-agents](https://raw.githubusercontent.com/openai/openai-agents-python/main/docs/agents.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml) · [wcag](https://raw.githubusercontent.com/w3c/wcag/main/guidelines/index.html)
