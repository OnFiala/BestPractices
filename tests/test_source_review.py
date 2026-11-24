import contextlib
import datetime as dt
import io
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from library.content import ROOT
from library.source_review import summary
from library.sources import check, compare
from library.validate import validate


class SourceReviewTests(unittest.TestCase):
    def test_initial_reference_stays_pending_and_detects_later_drift(self):
        source = {"id": "new", "reviewed_on": "2026-11-02", "review_days": 90,
                  "reviewed_sha256": "a" * 64, "baseline_status": "pending-human-review"}
        baseline = {}
        current = {"new": {"status": "ok", "sha256": "a" * 64}}
        result = compare([source], baseline, current, dt.date(2026, 11, 2))
        self.assertEqual(result["unbaselined"], ["new"])
        self.assertEqual(result["changed"], [])
        self.assertTrue(result["action_required"])
        self.assertEqual(baseline, {})
        current["new"]["sha256"] = "b" * 64
        self.assertEqual(compare([source], baseline, current, dt.date(2026, 11, 2))[
            "changed"], ["new"])

    def test_missing_or_unaccepted_baseline_cannot_silently_pass_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for folder in ("docs", "data"):
                shutil.copytree(ROOT / folder, root / folder)
            path = root / "data/sources.json"
            data = json.loads(path.read_text())
            pending = next(s for s in data["sources"] if s.get("baseline_status"))
            del pending["baseline_status"]
            path.write_text(json.dumps(data))
            self.assertIn("Source baseline does not cover registry", "\n".join(validate(root)))
            pending["baseline_status"] = "pending-human-review"
            pending["reviewed_sha256"] = "not-a-hash"
            path.write_text(json.dumps(data))
            self.assertIn("Reviewed source hash differs", "\n".join(validate(root)))
            accepted = next(s for s in data["sources"] if not s.get("baseline_status"))
            accepted["baseline_status"] = "pending-human-review"
            path.write_text(json.dumps(data))
            self.assertIn("includes pending proposals", "\n".join(validate(root)))

    def test_observation_preserves_failure_and_never_writes_baseline(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "data").mkdir()
            sources = [{"id": sid, "reviewed_on": "2026-11-02", "review_days": 90,
                        "reviewed_sha256": "a" * 64} for sid in ("new", "failed")]
            (root / "data/sources.json").write_text(json.dumps({"sources": sources}))
            baseline = root / "data/source-baseline.json"
            baseline.write_text('{"observations": {}}\n')
            before = baseline.read_bytes()
            observed = [{"status": "ok", "sha256": "a" * 64},
                        {"status": "unavailable", "error": "fetch failed"}]
            report, candidate = root / "report.json", root / "candidate.json"
            with patch("library.sources.observe", side_effect=observed), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(check(report, candidate, root), 1)
            self.assertEqual(baseline.read_bytes(), before)
            self.assertEqual(report.read_bytes(), candidate.read_bytes())
            result = json.loads(report.read_text())
            self.assertEqual(result["unavailable"], ["failed"])
            self.assertEqual(result["unbaselined"], ["new", "failed"])
            self.assertTrue(result["action_required"])

    def test_summary_distinguishes_missing_evidence_drift_and_no_action(self):
        missing = summary(None)
        self.assertIn("source state is unknown", missing)
        self.assertIn("evidence may be missing", missing)
        report = {"changed": ["changed"], "unavailable": [], "overdue": [],
                  "unbaselined": ["new"], "action_required": True,
                  "observations": {"raw_body": "NEVER PUBLISH THIS"}}
        rendered = summary(report, "https://github.com/example/repo/artifacts/1")
        self.assertIn("Changed: 1", rendered)
        self.assertIn("Awaiting initial baseline: 1", rendered)
        self.assertIn("Review is required", rendered)
        self.assertIn("does not create a PR or accept a baseline", rendered)
        self.assertNotIn("NEVER PUBLISH THIS", rendered)
        report.update(changed=[], unbaselined=[], action_required=False)
        self.assertIn("No source review signal", summary(report))


if __name__ == "__main__":
    unittest.main()
