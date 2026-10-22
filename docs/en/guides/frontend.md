---
{
  "id": "frontend",
  "language": "en",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Frontend architecture and contracts

## Choose rendering for each interaction

Static generation fits public content that can be rebuilt. Server rendering may help initial freshness or discovery, while client rendering fits sustained interaction. Hybrid routes can combine these approaches. This is the library's original decision framework: measure the relevant journey and inspect the selected framework's current behavior before adopting it.

Record cache ownership, hydration/JavaScript cost, authentication and deployment boundaries. Do not place a user's private server-rendered response in a cache shared with another principal. Microfrontends can support independent ownership, but introduce routing, dependency and design-consistency costs; they are not a default way to split components.

## Give state one owner

Distinguish server state, URL/navigation state, local interaction state and durable preferences. Decide which state survives refresh or offline use and how it is invalidated after sign-out or permission change. Organize features around explicit interfaces and shared accessible primitives. Copying the same server data into several stores creates reconciliation work rather than resilience.

For each API-backed interaction, define:

| Contract | Example acceptance evidence |
| --- | --- |
| Authorization | Direct API requests fail when the user lacks permission, even if the UI is bypassed |
| Response shape | Old/new clients handle documented fields, errors, pagination and units |
| Loading/cancellation | Leaving the page stops unnecessary work or safely ignores a late result |
| Optimistic change | Rejection restores or reconciles visible state without losing the user's input |
| Offline/conflict | A queued edit has a stable identity and an explicit conflict rule on reconnect |
| Privacy | Sign-out and revoked access clear or invalidate relevant cached private data |

The server owns trusted validation and authorization. Hidden buttons and client schemas improve usability but cannot enforce access control. Keep backend secrets out of browser bundles, source maps and generated indexes. Browser code and model/tool outputs are untrusted at the server boundary.

## Test the observable journey

During implementation, test domain rules separately from rendering details. At API changes, run consumer compatibility tests. Before release, exercise key journeys as a [black-box user](testing-strategy.md): keyboard and focus order, accessible names, contrast, narrow viewport, loading/empty/error states, denied access and interrupted requests. Combine automated accessibility checks with task-based keyboard and assistive-technology review where relevant; passing an automated checker is not full conformance evidence.

Use [performance testing](performance-testing.md) for representative device/network conditions and sustained API load, measuring navigation, interaction latency, transferred assets and errors. Confirm that the frontend does not multiply backend calls during retries, polling or reconnect. Test authentication and cache boundaries using the [security test plan](security-testing.md).

## Evolve deliberately

A backend-for-frontend may be useful when a particular client needs aggregation or a stronger server-side boundary. State the gain and who owns the additional deployment. Change framework or introduce microfrontends only when measured constraints justify migration, including accessibility, compatibility and dependency support costs. Retain a release and cache-invalidation plan so old browser assets remain compatible with the deployed API.

WebMCP is a progressive enhancement here. Ordinary reading and search must work without it; supported browsers still require permission, cancellation and navigation tests. Experimental tool exposure must not grant access that the user does not already have.

## Related decisions

[Architecture](architecture.md) · [Testing strategy](testing-strategy.md) · [Performance testing](performance-testing.md) · [Security testing](security-testing.md) · [Integrations](integrations.md)

## Primary evidence

[wcag](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/index.html) · [owasp](https://raw.githubusercontent.com/OWASP/ASVS/2b47a9dd16760ee484a6672d197f1f7e25d9c632/README.md) · [webmcp](https://raw.githubusercontent.com/webmachinelearning/webmcp/51ed75653aaa7f174f8dbe05d1bc327359bbc57c/README.md) · [wcag-keyboard](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/sc/20/keyboard.html) · [wcag-focus-order](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/sc/20/focus-order.html) · [wcag-focus-visible](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/sc/20/focus-visible.html) · [wcag-contrast](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/sc/20/contrast-minimum.html) · [azure-cqrs](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/cqrs.md)
