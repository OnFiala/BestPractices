# Third-party notices and content provenance

BestPractices is an agent-maintained library under human direction. Its original
guidance is written independently from cited evidence; citations do not grant
permission to reproduce upstream prose, translations, tables, or diagrams. Fetched
research documents are reference material, not website content. Legal notices and
required corresponding program source below are intentionally redistributed under
their applicable licenses, separately from the library's guidance.

Our [content license](LICENSE-CONTENT) covers original prose, including translations
and text inside HTML, JSON, search indexes, and MCP responses. Our [MIT license](LICENSE-CODE)
covers original code and structural/factual metadata. Neither license replaces any
third-party terms. AI authorship does not establish rights in someone else's work.

## Components distributed with the website

The build retains the following components and their notices. Versions come from
the locked Python packages and Material's matching npm lockfile. The deployed
[asset inventory](data/third-party-assets.json) records archive integrity, exact retained
asset hashes, legal-file hashes, and corresponding-source hashes. Browser source maps
and npm dependency metadata were inspected to include bundled transitive code.

| Component | Version | Applicable license and retained terms |
| --- | --- | --- |
| Material for MkDocs — Martin Donath | 9.7.7 | [MIT](LICENSES/mkdocs-material-MIT.txt) |
| MkDocs — MkDocs team | 1.6.1 | [BSD-2-Clause](LICENSES/mkdocs-BSD-2-Clause.txt) |
| Clipboard.js — Zeno Rocha | 2.0.11 | [MIT](LICENSES/clipboard-LICENSE.txt) |
| good-listener — Zeno Rocha | 1.2.2 | [MIT](LICENSES/zenorocha-MIT.txt) |
| delegate — Zeno Rocha | 3.2.0 | [MIT](LICENSES/zenorocha-MIT.txt) |
| select — Zeno Rocha | 1.1.2 | [MIT](LICENSES/zenorocha-MIT.txt) |
| tiny-emitter — Scott Corgan | 2.1.0 | [MIT](LICENSES/tiny-emitter-LICENSE.txt) |
| escape-html — TJ Holowaychuk, Andreas Lubbe, Tiancheng Gu | 1.0.3 | [MIT](LICENSES/escape-html-LICENSE.txt) |
| focus-visible — WICG contributors | 5.2.1 | [W3C 2015 terms](LICENSES/W3C-20150513.txt), [upstream notice](LICENSES/focus-visible-NOTICE.txt) |
| RxJS — contributors | 7.8.2 | [Apache-2.0 with upstream notice](LICENSES/rxjs-Apache-2.0.txt) |
| tslib — Microsoft | 2.7.0 | [0BSD](LICENSES/tslib-0BSD.txt) |
| Lunr — Oliver Nightingale | 2.3.9 | [MIT](LICENSES/lunr-LICENSE.txt) |
| Lunr languages / Snowball — Mihai Valentin, Oleg Mazko and contributors | 1.14.0 | [MPL-1.1](LICENSES/lunr-languages-MPL-1.1.txt), corresponding source below |
| material-design-color — Denis Malinochkin | 2.3.2 | [MIT](LICENSES/material-design-color-LICENSE.txt) |
| Pictogrammers / Material Design SVG icons — Austin Andrews and contributors | 7.4.47 | [Upstream notice](LICENSES/pictogrammers-NOTICE.txt), [Apache-2.0](LICENSES/Apache-2.0.txt) |
| Font Awesome Free SVG icon — Fonticons, Inc. | 7.1.0 | Icons: CC-BY-4.0; [upstream notices](LICENSES/fontawesome-LICENSE.txt) |

The upstream legal notices are retained verbatim where supplied. The npm packages
good-listener, delegate, and select declare MIT in their metadata and tagged README
license notices but omit a standalone license file. We retain their named copyright
holder with the standard MIT terms; the exact evidence links are in the inventory.

The focus-visible implementation is included in Material's upstream compiled bundle.
Its notice points to the W3C Software and Document License dated 2015; we retain that
notice and the full terms from the SPDX license-text mirror. The upstream bundle is
redistributed unchanged. Full source maps remain available alongside its JavaScript.

Material and Font Awesome icon notices apply to their inline SVGs as well as files.
Font Awesome attribution comments are preserved. No font files or externally loaded
Google Fonts are used. Unused language stemmers, wordcut, and tinyseg are removed
from the published build to avoid distributing unrelated programs and dictionaries.

## Lunr languages: corresponding source

The German and Spanish stemmers and shared support program are unchanged from
Lunr languages 1.14.0. Their minified files match the integrity-verified npm archive.
The preferred-form source is distributed with this website and retained in Git:

- [German source](third_party/lunr_languages/lunr.de.js)
- [Spanish source](third_party/lunr_languages/lunr.es.js)
- [Shared stemmer source](third_party/lunr_languages/lunr.stemmer.support.js)
- [Source provenance and retirement obligations](third_party/lunr_languages/README.md)

These program files remain MPL-1.1; they are not relicensed as MIT or CC BY 4.0.
Keep this exact source available for the period required by MPL-1.1 section 3.2
when retiring or moving a deployment. A moving upstream URL is not our preservation
plan. No changes were made to their code or copyright notices.

## Updating and reusing the distribution

A dependency or vendor-asset change must update the inventory only after reviewing
actual bundled components, their license/notice obligations, and source availability.
The build rejects missing or altered reviewed assets or legal files. A successful
hash check proves identity against this inventory, not legal clearance or authorship.

Installed Python tooling and its transitive dependencies retain their own licenses;
their package distributions include license metadata and notices. They are not all
redistributed by the static website. If distributing a server/container or a bundled
Python environment, perform a separate inventory for those shipped packages.

Preserve notices when copying the generated website. This inventory does not license
trademarks, claim vendor endorsement, or authorize reuse of cited source documents.
