# Material 9.8.0 distribution review

Agent-authored proposal; no human approval or publication is implied.

PR #6 changes the locked theme from 9.7.7 to 9.8.0. The existing license gate
correctly rejects this until the redistributed assets have been inspected.

The 9.8.0 tag resolves to `0f72ad68d1bee212f909f3b82e0189e221b06374`.
Its [npm lockfile](https://github.com/squidfunk/mkdocs-material/blob/0f72ad68d1bee212f909f3b82e0189e221b06374/package-lock.json)
retains the same versions and archive integrity values for all fourteen npm
components in our distribution inventory. Its
[MIT license](https://github.com/squidfunk/mkdocs-material/blob/0f72ad68d1bee212f909f3b82e0189e221b06374/LICENSE)
is byte-identical to the retained notice. Existing component notices and the
Lunr languages preferred-form sources therefore remain applicable and unchanged.

The four regenerated JavaScript/CSS source maps have the same source membership
as the 9.7.7 wheel. JavaScript maps include source contents: the only changed
entry is the theme's own Mermaid component stylesheet; the search worker source
contents are identical. CSS maps do not include source contents, so this is not
a claim of byte-identical CSS source. No new bundled dependency was identified.
The favicon and retained language stemmers are unchanged. Both JavaScript
bundles, both stylesheets, and their four maps have new filenames/hashes, all
recorded from the actual generated site. Inline icon package versions and
archive identities are unchanged; their notices remain retained.

The gate still checks package versions, exact asset membership and hashes,
notices, and corresponding source in every locale. It has not been bypassed or
relaxed. Hash equality establishes artifact identity, not legal clearance.
Rollback is to revert this inventory/notice change together with the dependency
bump, then rebuild. No generated site files belong in Git.

Local verification passed: Ruff, catalog/translation validation, 89 Python tests
(including all three licensing rejection/preservation tests), four WebMCP tests,
five reference check groups and coverage assessment, strict four-locale build,
and generated link/anchor/search checks. The first browser run failed because
this container's Chromium sandbox could not start. The separate repeat used the
documented `BP_BROWSER_NO_SANDBOX=1` exception only for the owned local fixture;
all five groups then passed. Both reports remain distinct in ignored `reports/`.
GitHub CI must additionally validate the pushed commit in its own environment.
