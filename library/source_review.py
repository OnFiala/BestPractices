"""Render metadata-only source review instructions, including failed observation runs."""

import json
import os

from library.content import ROOT


def summary(report: dict | None, artifact_url: str = "") -> str:
    lines = ["## Primary-source review", ""]
    if report is None:
        lines.append("No observation report was produced. Inspection failed; source state is unknown.")
    else:
        for key, label in (("changed", "Changed"), ("unavailable", "Unavailable"),
                           ("overdue", "Overdue"), ("unbaselined", "Awaiting initial baseline")):
            lines.append(f"- {label}: {len(report.get(key, []))}")
        lines += ["", "Review is required." if report["action_required"]
                  else "No source review signal was observed in this run."]
    if artifact_url:
        lines += ["", f"[Download source-evidence metadata]({artifact_url}) (retained for 14 days)."]
    else:
        lines += ["", "No artifact link is available. Check the upload step; evidence may be missing."]
    lines += ["", "This job does not create a PR or accept a baseline. A green observation run",
              "only means every tracked source was reachable; changed or new sources still need review.",
              "", "Download the artifact from this run. If it contains `source-observations.json`,",
              "inspect it, copy it to `data/source-observations.json` on a fresh branch from `main`,",
              "and open a draft PR. If `automation/source-observations` already exists, compare it",
              "with `main` first and reuse it only if it contains the intended metadata changes.",
              "Run Validate on the exact proposed head. Do not copy observations into",
              "`data/source-baseline.json` before human review. See README.md, Activate on GitHub.",
              "", "Automatic PR proposals are optional (`ENABLE_SOURCE_REVIEW_PRS=true`).",
              "When enabled, inspect the separate propose job for its actual outcome."]
    return "\n".join(lines) + "\n"


def main():
    path = ROOT / "reports/sources.json"
    report = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else None
    print(summary(report, os.environ.get("ARTIFACT_URL", "")), end="")


if __name__ == "__main__":
    main()
