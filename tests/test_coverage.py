import copy
import shutil
import tempfile
import unittest
from pathlib import Path

from library.content import ROOT
from library.coverage import _passed, coverage, validate_coverage


class CoverageTests(unittest.TestCase):
    def test_missing_suite_entry_cannot_claim_executable_coverage(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for name in ("data", "docs", "tests", "examples", "library"):
                shutil.copytree(ROOT / name, root / name, ignore=shutil.ignore_patterns("__pycache__"))
            (root / "tests/frontend.test.cjs").unlink()
            self.assertTrue(any("Missing/unsafe coverage suite entry" in error
                                for error in validate_coverage(root)))
            with self.assertRaises(ValueError):
                coverage("frontend-state", root=root)

    def test_declared_references_do_not_claim_execution_or_production(self):
        self.assertEqual(validate_coverage(), [])
        result = coverage("tenant-isolation")
        self.assertEqual(result["domains"][0]["status"], "executable-reference")
        self.assertFalse(result["production_ready"])
        self.assertFalse(result["report_matches_current_inputs"])
        result = coverage("mobile-offline")
        self.assertEqual(result["domains"][0]["status"], "documented-guidance")
        with self.assertRaises(ValueError):
            coverage("../../etc/passwd")

    def test_claimed_pass_cannot_hide_required_skips_or_failures(self):
        receipt = {"suite_id": "delivery", "status": "passed", "returncode": 0,
                   "tests_observed": 1, "test_observation": {
                       "tests_run": 1, "case_ids": ["test_case"], "skipped": 0,
                       "failures": 0, "errors": 0, "expected_failures": 0,
                       "unexpected_successes": 0}}
        self.assertTrue(_passed(receipt))
        for key in ("skipped", "failures", "errors", "expected_failures", "unexpected_successes"):
            with self.subTest(key=key):
                broken = copy.deepcopy(receipt)
                broken["test_observation"][key] = 1
                self.assertFalse(_passed(broken))
        receipt["returncode"] = 1
        self.assertFalse(_passed(receipt))
        self.assertFalse(_passed({"suite_id": "frontend-browser", "status": "passed",
                                  "returncode": 0, "tests_observed": 20}))
        for malformed in (None, [], {**receipt, "returncode": 0, "test_observation": None},
                          {**receipt, "returncode": 0, "suite_id": []}):
            self.assertFalse(_passed(malformed))


if __name__ == "__main__":
    unittest.main()
