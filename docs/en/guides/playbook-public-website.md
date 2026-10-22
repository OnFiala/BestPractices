---
{
  "id": "playbook-public-website",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Deliver a public website

## Fit and first decisions

Use this profile for public editorial content, documentation, or a campaign whose main journey is reading, searching, and following links. Record locales, publishing frequency, accessibility expectations, domain ownership, asset budget, and acceptable time to correct a harmful publication. The default is a static build from reviewed content, immutable release artifacts, and a CDN. This is an agent-authored proposal and local synthesis, not adopted policy or a production certification.

A server-rendered route is an alternative when freshness cannot wait for a build. Authenticated submissions require an explicit server boundary; do not disguise a write service as a static-site detail. A small site can keep content and presentation together. As builds or editorial contention grow, separate content validation and incremental builds first. Add services only when measured publishing delay, dynamic work, or ownership demands justify their running cost; visitor count alone does not.

## Boundaries and contracts

Organize `content/`, `ui/`, `build/`, `tests/`, and `ops/` by responsibility, even if they share a repository. The content schema owns stable page IDs, locale, redirects, publication state, and public metadata. The UI owns navigation, search states, focus, and accessible error messages. The build owns deterministic transformation and an explicit asset allowlist. Private drafts, credentials, and internal comments must never enter deployable HTML, JSON search indexes, source maps, or downloadable source bundles.

Specify URL permanence, redirect behavior, missing translations, search index version, and cache lifetimes. Build the index and pages into the same release. Preview identities may read draft material; the production publishing identity must receive only the approved artifact. Treat authored HTML, imported Markdown, and query text as untrusted at their rendering boundaries; use safe text rendering or an explicitly reviewed sanitization policy.

## Sequence the work

1. The discovery agent records three public journeys, a route/locale inventory, content ownership, and quantitative publishing and performance targets in a project profile. A human resolves brand, accessibility, and publication-risk decisions.
2. The design and implementation role builds one complete journey including empty search, missing route, mobile viewport, and keyboard navigation. It records the rendering choice and dependency footprint in an ADR before multiplying page templates.
3. The verifier checks a built artifact in an isolated real browser, reviews output data, and exercises an older release. The release owner chooses the approved digest and controls deployment credentials.

Hand over a concrete packet: profile, ADR, content schema, route manifest, artifact digest and commit, browser observations, accessibility review gaps, output-data inspection, deploy/restore instructions, and named content/domain owners. Keep planned, executed, failed, and skipped checks separate. The local reference directory `examples/frontend` is a starting point for interaction work, not evidence that this project's routes or accessibility have been verified.

## Select checks that can disprove readiness

Use unit checks for parser and route rules, integration checks for content-to-index consistency, and black-box browser checks for public journeys. For a renamed page, the old URL must reach the intended replacement rather than a plausible but wrong page. Search for a synthetic private marker in every generated asset: a match is a release failure, even if the marker is absent from visible pages. Submit markup in search input and imported titles; it must remain harmless text or follow the reviewed sanitization rule without executing script.

Throttle the network, fail the search fetch, and navigate before it finishes. The current page must remain authoritative; a late result must not overwrite a newer query, and an error must allow recovery. Check keyboard completion and visible focus across each supported locale; automated accessibility results alone do not establish conformance. Measure cold transfer, interaction delay, build time, and cache hit behavior against project targets on representative devices. Stop tests at the agreed traffic or spending limit.

## Release, operate, and retire

Preview the exact artifact, deploy to a bounded audience or staging hostname, then verify critical routes and headers before promotion. Keep the previous artifact and routing configuration. A rollback can restore pages but cannot retract copies from caches, search engines, downloads, or Git history; a disclosure requires an incident response and secret rotation where relevant. Redirect migrations need a retained mapping, and deleting a locale requires explicit link and user-impact review.

Assign an owner for failed builds, domain/certificate renewal, abusive traffic, and emergency content correction. Observe route failures, search failures, publication age, and synthetic journey availability without retaining unnecessary visitor data. Budget CDN transfer, build minutes, logs, dependencies, and editorial maintenance. Before production, close hosting configuration, header policy, backup/export, accessibility, and on-call gaps; the reference does not supply them. On retirement, preserve agreed content exports and redirects, revoke publishing access, remove tracking, and retain domain control for the agreed transition.

## Continue with related decisions

[Frontend contracts](frontend.md) · [Hosting](hosting.md) · [GitHub delivery](github.md) · [Testing strategy](testing-strategy.md)

## Primary evidence

[github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md) · [owasp-xss](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.md) · [playwright-testing](https://raw.githubusercontent.com/microsoft/playwright/ca7ca36145b84183cf423c2a099bd7e9cd8b1cb3/docs/src/best-practices-js.md) · [wcag-keyboard](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/sc/20/keyboard.html) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md)
