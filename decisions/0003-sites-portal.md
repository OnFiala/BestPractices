# 0003: Integrated Sites portal for OFOps Architecture

Status: proposed implementation; user-selected platform; deployment pending.
Date: 2026-10-22. Authorship: AI agent, under human direction.

## Context

The public BestPractices library needs an understandable human entry point and
discoverable agent integrations under `ofops.co`. The user selected integrated
OpenAI Sites, already used for their portfolio, and Cloudflare for DNS. They
specified native Sites database, storage and MCP support as capabilities to use.
Do not replace that choice with GitHub Pages or assume Sites is static-only.

## Decision

Prepare `architecture.ofops.co` as a separate Sites project. Keep GitHub as the
source of guidance, translations, schemas and reviewed implementation changes.
Build the website and MCP content from one identified release. English is canonical;
Czech, German and Spanish preserve the same article when switching language.

The portal should offer visible entry points for starting a project, selecting an
engineering approach and connecting an agent. Separate human explanations, technical
contracts and source/verification status. Clearly identify agent-assisted authorship
and distinguish available, experimental and planned integrations.

Use native Sites backend, database, storage and MCP facilities according to their
current documented contracts. Prefer one application and a same-origin MCP route
when supported. An additional MCP host is not a prerequisite. Keep publication/search
indexes rebuildable; reserve object storage for original assets and public exports.
Do not persist private project inputs merely to demonstrate a database integration.

Remote MCP must preserve the five existing advisory tools' boundaries: no execution,
write, merge, deployment or authenticated approval. Validate authentication and
client compatibility independently of website publication. A successful assessment
does not establish production readiness.

## Evidence and unresolved implementation contracts

The existing frontend is portable static output. Its canonical URLs and hreflang
metadata are now configurable instead of bound to a GitHub Pages hostname. A prior
Sites deployment demonstrated the static-directory configuration shape. That does
not establish the current backend SDK or database/storage/MCP API.

Official Sites documentation was located via OpenAI's developer navigation and
verified redirects. Its destination is `learn.chatgpt.com/docs/sites`; the current
environment denied access to that host. The service contracts remain unread here.
No provider limits, backup guarantees, Python support or authentication mechanism
are assumed. Resolve them before provisioning or publishing; record the exact
configuration and measured behavior in the deployment review.

## Validation and reversal

Build and inspect all locales with the intended canonical base; check generated
links, same-article language switches and license notices. Test the actual native
MCP transport and client behavior after its implementation. Check database/storage
isolation and restoration if those facilities are provisioned. Verify custom-domain
TLS and the deployed release before reporting availability.

Reverting website code does not undo database changes or disclosed data. Retain
versioned exports and a tested migration/restore path. DNS edits are scoped to the
new library subdomain. Existing portfolio content and domain bindings remain under
their own project. See [the implementation handoff](../deployment/sites/README.md).
