# ADR-0001: A portable, reviewed, multilingual decision library

Status: proposed · Owner: OnFiala · Date: 2026-10-21

The repository starts empty and must serve humans and agents across project sizes.
English is canonical, with complete Czech, German, and Spanish translations. Agents
propose changes; humans approve them. Prose/diagrams use CC BY 4.0 and code uses MIT.

Use Markdown plus JSON registries in Git. Build four independent static MkDocs Material
sites with relative language links; avoid coupling translations to an additional i18n
plugin. Python standard-library checks and source observation remain usable independently
of the renderer. The MCP adapter uses the official Python SDK and exposes read-only
catalog/search. WebMCP is an optional experimental layer with feature detection.

Pin tested dependencies and hashes. The current tested renderer resolves MkDocs 1.6.1
with Material 9.7.7. Material emits an upstream warning about a future incompatible
MkDocs 2 migration; do not promote a major renderer change without rebuilding all
languages, checking licenses, overrides, and navigation. Markdown/JSON remain portable
if the renderer needs replacement. This is a compatibility choice, not a universal stack.

Source hashes detect drift but cannot establish correctness. A separate human-reviewed
change updates recommendations, translations, review dates, and the accepted baseline.
Network observations do not gate every offline content PR. Scheduled source checks and
opt-in paid agent work remain distinct. GitHub settings enforce human review; workflow
files cannot enforce it alone.

Validation: deterministic content checks, failure-path tests, real stdio MCP calls,
four-language strict build, local HTTP checks, browser interaction, and live source reads.
Publication, GitHub-hosted runs, native WebMCP, and ChatGPT remote installation require
separate evidence. Revisit when content scale, search needs, SDK compatibility, or
translation review effort exceeds this design's capabilities.
