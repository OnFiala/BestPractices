# Contributing

Open an issue with a concrete decision, counterexample, or outdated source. Explain
context, consequences, and primary evidence. A preference alone is not a universal rule.

For a guidance change, edit all four languages and increment the guide revision in
`data/catalog.json` and matching front matter. Keep IDs stable. JSON front matter is
deliberately accepted as YAML by MkDocs and parsed without dependencies by our validator.
Update review dates only after reading the relevant source. Initial translations
are machine-authored and need human editorial review; revision parity does not prove quality.

Run the README checks. Keep source network checks separate from deterministic CI.
If a source changes, inspect its upstream diff and affected claims, record reasoning,
then propose guide/translation updates. A reviewer may copy successfully inspected
observations into `data/source-baseline.json` in the same PR and update source review
dates; never copy unavailable results or reset dates automatically. Delete a resolved
`data/source-observations.json` candidate after review to avoid stale evidence.

PRs explain the problem, final behavior, tested evidence, affected guide IDs/locales,
tradeoffs, and rollback. Humans approve and merge; agents may not. Published releases
use SemVer for catalog/adapter contracts; every commit does not need a new release.
Contributions use the applicable repository license. Avoid copying source documents
wholesale; cite primary URLs and keep third-party notices for any excerpts.
