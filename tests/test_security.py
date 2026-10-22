"""Regression checks for the private generation / trusted consumer boundary."""

import copy
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

from library.agent_gate import MAX_FILE_BYTES, MAX_PROPOSAL_BYTES, apply_proposal
from library.content import ROOT


class ProposalBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name) / "checkout"
        self.root.mkdir()
        self.doc = self.root / "docs/en/guides/example.md"
        self.doc.parent.mkdir(parents=True)
        self.doc.write_text("original\n", encoding="utf-8")
        (self.root / "data").mkdir()
        (self.root / "data/sources.json").write_text(json.dumps({
            "sources": [{"id": "primary-evidence"}],
        }))
        self.catalog = {
            "schema_version": 1, "canonical_language": "en", "languages": ["en"],
            "guides": [{"id": "example", "path": "guides/example.md",
                        "status": "proposed", "revision": 1}],
        }
        (self.root / "data/catalog.json").write_text(json.dumps(self.catalog))
        (self.root / "AGENTS.md").write_text("human policy\n")
        self.git("init")
        self.git("add", ".")
        self.commit()

    def git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.root), *args],
                                       stderr=subprocess.DEVNULL).decode().strip()

    def commit(self):
        self.git("-c", "user.name=Test", "-c", "user.email=test@example.invalid",
                 "commit", "-m", "trusted test base")
        self.base = self.git("rev-parse", "HEAD")

    def proposal(self, files=None):
        return {
            "schema_version": 1, "base_commit": self.base,
            "human_review_required": True, "rights_status": "unreviewed",
            "summary": "Independently authored proposal; review required.",
            "source_ids": ["primary-evidence"],
            "files": files if files is not None else [
                {"path": "docs/en/guides/example.md", "content": "proposed\n"}],
        }

    def apply(self, proposal):
        return apply_proposal(json.dumps(proposal), self.base, self.root)

    def test_applies_known_prose_without_executing_its_text(self):
        marker = Path(self.directory.name) / "must-not-exist"
        literal = f"$(touch {marker})\n`touch {marker}`\n"
        payload = self.proposal([{"path": "docs/en/guides/example.md", "content": literal}])
        env = os.environ | {"AGENT_PROPOSAL": json.dumps(payload)}
        subprocess.run([sys.executable, "-I", str(ROOT / "library/agent_gate.py"),
                        self.base, "--proposal-env", "AGENT_PROPOSAL"],
                       cwd=self.root, env=env, check=True, capture_output=True)
        self.assertEqual(self.doc.read_text(), literal)
        self.assertFalse(marker.exists())

    def test_noop_does_not_require_a_source_or_modify_checkout(self):
        proposal = self.proposal([])
        proposal["source_ids"] = []
        self.assertEqual(self.apply(proposal), [])
        self.assertEqual(self.git("status", "--porcelain"), "")

    def test_rejects_scope_escapes_and_checks_all_files_before_writing(self):
        paths = ["AGENTS.md", "library/validate.py", "../outside.md", "/tmp/outside.md",
                 ".git/config", "docs/en/guides/new.md", "docs/en/guides/example.md"]
        for name in paths:
            with self.subTest(path=name):
                payload = self.proposal()
                payload["files"].append({"path": name, "content": "forbidden"})
                with self.assertRaises(ValueError):
                    self.apply(payload)
                self.assertEqual(self.doc.read_text(), "original\n")
                self.assertEqual(self.git("status", "--porcelain"), "")

    def test_rejects_untrusted_review_state_and_unknown_sources(self):
        changes = [
            {"schema_version": True}, {"schema_version": 2}, {"base_commit": "0" * 40},
            {"human_review_required": False}, {"rights_status": "approved"},
            {"source_ids": []}, {"source_ids": ["invented"]},
            {"source_ids": ["primary-evidence", "primary-evidence"]},
            {"extra_command": "arbitrary"}, {"summary": "x" * 1001},
        ]
        for change in changes:
            with self.subTest(change=list(change)):
                with self.assertRaises(ValueError):
                    self.apply(self.proposal() | change)
        payload = json.dumps(self.proposal()).replace('"schema_version": 1',
                                                    '"schema_version": 1, "schema_version": 1')
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            apply_proposal(payload, self.base, self.root)

    def test_bounds_transfer_file_sizes_and_rejects_binary_content(self):
        for content in ("", "binary\0data", "é" * (MAX_FILE_BYTES // 2 + 1)):
            with self.subTest(length=len(content)):
                with self.assertRaises(ValueError):
                    self.apply(self.proposal([{"path": "docs/en/guides/example.md",
                                               "content": content}]))
        with self.assertRaisesRegex(ValueError, "transfer limit"):
            apply_proposal(" " * (MAX_PROPOSAL_BYTES + 1), self.base, self.root)
        with self.assertRaises(ValueError):
            self.apply(self.proposal([self.proposal()["files"][0]] * 10))

    def test_requires_pristine_consumer_at_exact_revision(self):
        with self.assertRaisesRegex(ValueError, "checkout does not match"):
            apply_proposal(json.dumps(self.proposal() | {"base_commit": "0" * 40}),
                           "0" * 40, self.root)
        self.doc.write_text("another person's work")
        with self.assertRaisesRegex(ValueError, "must be clean"):
            self.apply(self.proposal())
        self.assertEqual(self.doc.read_text(), "another person's work")

    def test_rejects_symlinks_and_hardlinks_even_when_git_is_clean(self):
        outside = Path(self.directory.name) / "outside.txt"
        outside.write_text(self.doc.read_text())
        self.doc.unlink()
        os.link(outside, self.doc)
        self.assertEqual(self.git("status", "--porcelain"), "")
        with self.assertRaisesRegex(ValueError, "regular in-repository"):
            self.apply(self.proposal())
        self.doc.unlink()
        self.doc.symlink_to(outside)
        self.git("add", ".")
        self.commit()
        with self.assertRaisesRegex(ValueError, "regular in-repository"):
            self.apply(self.proposal())
        self.assertEqual(outside.read_text(), "original\n")

    def test_cannot_promote_maturity_or_rewrite_guide_identity(self):
        for change in ({"status": "adopted"}, {"id": "new"}, {"path": "outside.md"}):
            with self.subTest(change=change):
                revised = copy.deepcopy(self.catalog)
                revised["guides"][0].update(change)
                with self.assertRaises(ValueError):
                    self.apply(self.proposal([{"path": "data/catalog.json",
                                               "content": json.dumps(revised)}]))
        revised = copy.deepcopy(self.catalog)
        revised["guides"][0]["revision"] = 2
        self.assertEqual(self.apply(self.proposal([{"path": "data/catalog.json",
                                                   "content": json.dumps(revised)}])),
                         ["data/catalog.json"])


class PublicationBoundaryTests(unittest.TestCase):
    def test_source_fed_generation_and_pr_cannot_run_in_public_repositories(self):
        workflow = yaml.safe_load((ROOT / ".github/workflows/agent.yml").read_text())
        required = {"github.event.repository.private == true",
                    "vars.ENABLE_AGENT_MAINTENANCE == 'true'",
                    "github.ref == 'refs/heads/main'"}
        for job in workflow["jobs"].values():
            self.assertEqual(set(job["if"].split(" && ")), required)
        worker = workflow["jobs"]["propose"]["steps"]
        self.assertTrue(worker[-1]["uses"].startswith("openai/codex-action@"))
        self.assertEqual(worker[-1]["with"]["permission-profile"], ":read-only")
        self.assertEqual(worker[-1]["with"]["safety-strategy"], "drop-sudo")
        self.assertNotIn("output-file", worker[-1]["with"])
        self.assertFalse(any("upload-artifact" in step.get("uses", "") for step in worker))
        consumer = workflow["jobs"]["open-pr"]["steps"]
        self.assertEqual(consumer[0]["with"]["ref"], "${{ needs.propose.outputs.base }}")
        self.assertFalse(any("git apply" in step.get("run", "") for step in consumer))

    def test_public_source_monitor_exports_only_metadata_paths(self):
        workflow = yaml.safe_load((ROOT / ".github/workflows/sources.yml").read_text())
        observer = workflow["jobs"]["observe"]["steps"]
        self.assertFalse(any("--documents" in step.get("run", "") for step in observer))
        uploads = [step for step in observer if "upload-artifact" in step.get("uses", "")]
        self.assertEqual(len(uploads), 1)
        self.assertEqual(set(uploads[0]["with"]["path"].splitlines()),
                         {"reports/sources.json", "reports/source-observations.json"})


if __name__ == "__main__":
    unittest.main()
