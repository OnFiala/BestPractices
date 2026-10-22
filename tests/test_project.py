import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from library.content import ROOT
from library.project import create_packet
from library.verification import report_matches


class PortableProjectTests(unittest.TestCase):
    def test_packet_cannot_be_created_within_copied_guidance_or_skills(self):
        for directory in ("docs", "plugins", ".git"):
            with self.subTest(directory=directory), self.assertRaises(ValueError):
                create_packet(self.profile(), ROOT / directory / "invalid-packet-output")

    def profile(self):
        profile = json.loads((ROOT / "templates/delivery-profile.json").read_text())
        return {**profile, "project_type": "agent-automation"}

    def test_portable_packet_executes_its_own_checks_and_blocks_empty_project_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            destination = Path(tmp) / "project"
            created = create_packet(self.profile(), destination)
            self.assertEqual(created["components"], ["agent_workflow"])
            self.assertTrue((destination / "docs/en/guides/agents.md").is_file())
            self.assertTrue((destination / "data/sources.json").is_file())
            self.assertTrue((destination / "LICENSE-CONTENT").is_file())
            run = subprocess.run([sys.executable, "-m", "library.verification", "delivery",
                                  "agent-workflow", "--output", "reports/local.json"],
                                 cwd=destination, capture_output=True, text=True, timeout=90)
            self.assertEqual(run.returncode, 0, run.stderr)
            report = json.loads((destination / "reports/local.json").read_text())
            self.assertTrue(report["all_selected_passed"])
            self.assertIsNone(report["input_image"]["revision"])
            self.assertTrue(report_matches(report, destination))
            check = subprocess.run([sys.executable, "-m", "library.delivery", "assess",
                                    "--profile", "project-profile.json", "--evidence",
                                    "project-evidence.json"], cwd=destination,
                                   capture_output=True, text=True, timeout=15)
            self.assertEqual(check.returncode, 1, check.stderr)
            assessment = json.loads(check.stdout)
            self.assertFalse(assessment["ready_for_human_review"])
            self.assertFalse(assessment["production_ready"])
            (destination / "examples/agent_workflow/workflow.py").write_text("# changed\n")
            self.assertFalse(report_matches(report, destination))

    def test_existing_paths_links_and_bad_profile_never_get_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            existing = root / "existing"
            existing.mkdir()
            (existing / "owner.txt").write_text("preserve")
            link = root / "link"
            link.symlink_to(root / "missing", target_is_directory=True)
            for destination in (existing, link):
                with self.assertRaises(ValueError):
                    create_packet(self.profile(), destination)
            self.assertEqual((existing / "owner.txt").read_text(), "preserve")
            with self.assertRaises(ValueError):
                create_packet({**self.profile(), "project_type": "unknown"}, root / "invalid")
            self.assertFalse((root / "invalid").exists())
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"project_type":"saas","project_type":"agent-automation"}')
            result = subprocess.run([sys.executable, "-m", "library.project", "init", "--profile",
                                     str(duplicate), "--destination", str(root / "duplicate")],
                                    cwd=ROOT, capture_output=True, timeout=15)
            self.assertEqual(result.returncode, 2)
            self.assertFalse((root / "duplicate").exists())


if __name__ == "__main__":
    unittest.main()
