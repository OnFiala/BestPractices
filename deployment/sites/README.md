# Sites deployment preparation

Status: **prepared locally; not provisioned, domain-bound, or deployed**.
The requested destination is the integrated OpenAI Sites service, with Cloudflare
DNS and the proposed hostname `architecture.ofops.co`. See
[the architecture decision](../../decisions/0003-sites-portal.md).

## Build the public library for the custom domain

Run from the repository root:

```sh
uv sync --frozen
uv run python -m library.site build --site-url https://architecture.ofops.co/
uv run python -m library.check_site
```

The output is `site/`: all four languages, search, relative language switches,
canonical URLs, language metadata, machine-readable exports, and license notices.
Changing the base URL neither creates a site nor changes DNS. The default build
retains the existing GitHub Pages base for compatibility with its optional workflow.

For a local preview with matching canonical metadata:

```sh
uv run python -m library.site serve --site-url http://127.0.0.1:8000/
```

`hosting.example.json` records a static-directory configuration shape observed in
an existing Sites deployment. It is a **candidate**, not a validated current Sites
schema or a complete application configuration. Obtain the current Sites template
before creating `.openai/hosting.json`; use the new library site's assigned project
ID. Do not reuse another site's ID or credentials. Do not commit credentials or raw
external documentation. Preserve the existing site's custom domains and contents.

## Complete the native application using the current Sites contract

Read the official documentation before selecting implementation APIs:

- [Sites overview](https://learn.chatgpt.com/docs/sites)
- [Data and connections](https://learn.chatgpt.com/docs/sites/data-and-connections)
- [Creating a site](https://learn.chatgpt.com/docs/sites/creating-a-site)
- [Publishing and sharing](https://learn.chatgpt.com/docs/sites/publishing-and-sharing)
- [ChatGPT MCP connection](https://developers.openai.com/plugins/deploy/connect-chatgpt/)

The `developers.openai.com/codex/sites/...` redirects to these product-documentation
URLs were observed on 2026-10-22. This environment could not retrieve the destination
pages, so their contents, runtime contracts, limits and prices are **not reviewed
evidence**. The user's stated Sites database, storage and MCP capabilities are the
target requirement; they do not establish a specific SDK, schema or runtime here.

Use Sites-native facilities where their current contracts fit:

| Component | Intended responsibility | Required verification |
| --- | --- | --- |
| Site frontend | Public EN/CS/DE/ES library and connector documentation | Full article rendering, deep links, search, locale persistence, accessibility |
| Database | Rebuildable publication/search index and release metadata | Access boundaries, migrations, quotas, export and restore |
| Object storage | Original public assets and versioned public exports | Bucket visibility, retention, content types, integrity, export and cleanup |
| MCP runtime | Search/read, planning, submitted-evidence checks and coverage | Supported transport/runtime, authentication, bounded input, client compatibility |
| Domain binding | Library subdomain and HTTPS | Exact Sites-supplied DNS records, certificate issuance, routing and rollback |

GitHub remains the source of approved guidance. Do not make the database an
independently editable copy of the library. Keep project profiles/evidence out of
public storage; any later persistence needs authenticated access and retention
decisions. The first connector can process submitted data without retaining it.
Avoid database/storage calls on every static article view when a release export
already serves the content. A platform capability alone does not justify using it.

The current MCP adapter is Python stdio only. Check the Sites server/runtime
contract before wrapping or porting it. Prefer a native route on the library site
if supported. No `/mcp` endpoint or remote connector is currently deployed. Listing
its five tools on a website does not turn the static build into an MCP server.

## Publication evidence

Before marking a connector available, record the actual site ID, source commit,
release/artifact digest, Sites version, assigned endpoint, authentication settings
and tested client/date. Validate initialization, tool discovery and real calls;
also unknown guides, unsupported locales, malformed/oversized inputs, denied access,
timeouts and cancellation. Preserve the assessor's advisory and non-approval limits.

Keep source snapshots out of public assets. Deploy the web and connector against
the same library revision. Review a preview first, then perform authorized
publication, verify the custom domain and all locales, and retain a recoverable
previous version. Test data restoration separately from code rollback.
