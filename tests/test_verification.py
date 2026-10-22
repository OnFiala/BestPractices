import json
import shutil
import tempfile
import unittest
from pathlib import Path

from library.content import ROOT
from library.verification import input_image, report_matches, run_suites


class LocalEvidenceTests(unittest.TestCase):
    def test_tap_diagnostics_cannot_hide_skipped_cases(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "tests").mkdir()
            (root / "tests/frontend.test.cjs").write_text(
                "const test = require('node:test');\n"
                "console.log('# skipped 0');\n"
                "test.skip('required dependency unavailable', () => {});\n")
            report = run_suites(["frontend-unit"], root)
            self.assertFalse(report["all_selected_passed"])
            self.assertEqual(report["results"][0]["node_observation"]["skipped"], 1)
            self.assertEqual(report["results"][0]["status"], "failed")

    def fixture(self, root, test_body):
        (root / "library").mkdir()
        (root / "tests").mkdir()
        for name in ("__init__.py", "check_runner.py"):
            shutil.copyfile(ROOT / "library" / name, root / "library" / name)
        (root / "tests/test_delivery.py").write_text(test_body)

    def test_skipped_and_empty_suites_are_not_observed_passes(self):
        bodies = ["import unittest\n", "import unittest\nclass Tests(unittest.TestCase):\n"
                  " @unittest.skip('dependency unavailable')\n def test_required(self): pass\n"]
        for body in bodies:
            with self.subTest(body=body), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.fixture(root, body)
                report = run_suites(["delivery"], root)
                self.assertFalse(report["all_selected_passed"])
                self.assertEqual(report["results"][0]["status"], "failed")

    def test_real_execution_is_bound_to_exact_copied_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.fixture(root, "import unittest\nclass Tests(unittest.TestCase):\n"
                         " def test_requirement(self): self.assertEqual(2 + 2, 4)\n")
            report = run_suites(["delivery"], root)
            self.assertTrue(report["all_selected_passed"])
            self.assertEqual(report["results"][0]["tests_observed"], 1)
            self.assertFalse(report["authenticated_execution"])
            self.assertTrue(report_matches(report, root))
            forged_inventory = json.loads(json.dumps(report))
            forged_inventory["input_image"]["files"] = []
            self.assertFalse(report_matches(forged_inventory, root))
            (root / "tests/test_delivery.py").write_text("# changed after execution\n")
            self.assertFalse(report_matches(report, root))

    def test_mutating_tests_cannot_keep_a_pass_bound_to_original_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.fixture(root, "import unittest\nfrom pathlib import Path\n"
                         "class Tests(unittest.TestCase):\n def test_changes_input(self):\n"
                         "  Path('tests/new_input.py').write_text('changed')\n")
            report = run_suites(["delivery"], root)
            self.assertTrue(report["input_changed"])
            self.assertFalse(report["all_selected_passed"])

    def test_unknown_commands_missing_checks_and_symlinks_fail_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with self.assertRaises(ValueError):
                run_suites(["delivery; touch should-not-exist"], root)
            report = run_suites(["delivery"], root)
            self.assertEqual(report["results"][0]["status"], "not-run")
            self.assertFalse(report["all_selected_passed"])
            (root / "library").symlink_to(ROOT / "library", target_is_directory=True)
            with self.assertRaises(ValueError):
                input_image(root)


if __name__ == "__main__":
    unittest.main()
