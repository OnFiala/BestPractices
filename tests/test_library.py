import datetime as dt
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from mcp import Client, StdioServerParameters

from library.agent_gate import export_patch
from library.content import ROOT, guide, search
from library.sources import MAX_BYTES, SafeRedirect, compare, observe, validate_url
from library.validate import validate


class ContentTests(unittest.TestCase):
    def test_real_catalog_and_all_translations(self):
        self.assertEqual(validate(), [])

    def test_search_and_read_all_languages(self):
        for lang, query in (("en", "idempotency"), ("cs", "idempotence"),
                            ("de", "Idempotenz"), ("es", "idempotencia")):
            with self.subTest(lang=lang):
                self.assertIn("durability", [g["id"] for g in search(query, lang)])
                result = guide("durability", lang)
                self.assertTrue(result["sources"])
                self.assertIn("RPO", result["content"])

    def test_rejects_arbitrary_paths_and_invalid_inputs(self):
        for gid in ("../../etc/passwd", "missing", "/etc/passwd"):
            with self.assertRaises(ValueError):
                guide(gid)
        for args in (("x", "xx", 5), ("x", "en", 21), ("x" * 301, "en", 5)):
            with self.assertRaises(ValueError):
                search(*args)
        self.assertEqual(search(""), [])

    def test_validator_rejects_missing_stale_and_broken_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for folder in ("docs", "data"):
                shutil.copytree(ROOT / folder, root / folder)
            (root / "docs/es/guides/data.md").unlink()
            stale = root / "docs/cs/guides/data.md"
            stale.write_text(stale.read_text().replace('"translation_revision": 1',
                                                       '"translation_revision": 0'))
            broken = root / "docs/en/guides/data.md"
            broken.write_text(broken.read_text() + "\n[Bad](missing.md)\n")
            errors = "\n".join(validate(root))
            for expected in ("Missing translation", "Stale translation", "Broken or escaping"):
                self.assertIn(expected, errors)

    def test_unknown_evidence_and_traversal_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for folder in ("docs", "data"):
                shutil.copytree(ROOT / folder, root / folder)
            path = root / "data/catalog.json"
            data = json.loads(path.read_text())
            data["schema_version"] = 99
            data["guides"][0]["sources"] = ["invented-source"]
            data["guides"][1]["path"] = "../../etc/passwd"
            path.write_text(json.dumps(data))
            errors = "\n".join(validate(root))
            self.assertIn("Unsupported schema version", errors)
            self.assertIn("Missing/unknown evidence", errors)
            self.assertIn("Escaping guide path", errors)


class SourceTests(unittest.TestCase):
    def test_drift_unavailability_and_overdue_are_distinct(self):
        sources = [{"id": i, "reviewed_on": "2026-01-01", "review_days": 14}
                   for i in ("same", "changed", "failed")]
        baseline = {i: {"sha256": "a"} for i in ("same", "changed", "failed")}
        current = {"same": {"status": "ok", "sha256": "a"},
                   "changed": {"status": "ok", "sha256": "b"},
                   "failed": {"status": "unavailable"}}
        result = compare(sources, baseline, current, dt.date(2026, 2, 1))
        self.assertEqual(result["changed"], ["changed"])
        self.assertEqual(result["unavailable"], ["failed"])
        self.assertEqual(len(result["overdue"]), 3)

    def test_url_and_redirect_policy(self):
        for url in ("http://raw.githubusercontent.com/a", "https://evil.example/a",
                    "https://user:secret@raw.githubusercontent.com/a",
                    "https://127.0.0.1/a", "https://raw.githubusercontent.com:444/a"):
            with self.assertRaises(ValueError):
                validate_url(url)
        with self.assertRaises(ValueError):
            SafeRedirect().redirect_request(None, None, 302, "", {}, "https://evil.example/")

    def test_network_error_remains_unavailable(self):
        with patch("urllib.request.build_opener", side_effect=OSError("denied")):
            result = observe({"id": "x", "url": "https://raw.githubusercontent.com/a/b"})
        self.assertEqual(result["status"], "unavailable")
        self.assertNotIn("sha256", result)

    def test_response_size_is_bounded(self):
        from unittest.mock import MagicMock
        response = MagicMock()
        response.__enter__.return_value.read.return_value = b"a" * (MAX_BYTES + 1)
        opener = MagicMock()
        opener.open.return_value = response
        with patch("urllib.request.build_opener", return_value=opener):
            result = observe({"id": "x", "url": "https://raw.githubusercontent.com/a/b"})
        self.assertEqual(result["status"], "unavailable")


class AgentBoundaryTests(unittest.TestCase):
    def test_export_accepts_prose_and_rejects_policy_and_symlinks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            def git(*args):
                return subprocess.check_output(["git", "-C", tmp, *args], stderr=subprocess.DEVNULL)
            git("init")
            path = root / "docs/en/guides/example.md"
            path.parent.mkdir(parents=True)
            path.write_text("original")
            (root / "AGENTS.md").write_text("policy")
            git("add", ".")
            git("-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit", "-m", "base")
            base = git("rev-parse", "HEAD").decode().strip()
            path.write_text("changed")
            output = root.parent / (root.name + ".patch")
            try:
                export_patch(base, output, root)
                self.assertIn(b"changed", output.read_bytes())
                (root / "AGENTS.md").write_text("weakened")
                with self.assertRaises(ValueError):
                    export_patch(base, output, root)
                (root / "AGENTS.md").write_text("policy")
                path.unlink()
                path.symlink_to(root / "AGENTS.md")
                with self.assertRaises(ValueError):
                    export_patch(base, output, root)
            finally:
                output.unlink(missing_ok=True)


class MCPTests(unittest.IsolatedAsyncioTestCase):
    async def test_real_stdio_round_trip_and_error(self):
        params = StdioServerParameters(command=sys.executable,
                                       args=["-m", "library.mcp_server"], cwd=ROOT)
        async with Client(params, read_timeout_seconds=15) as client:
            tools = await client.list_tools()
            names = {t.name for t in tools.tools}
            self.assertEqual(names, {"search_guides", "get_guide"})
            result = await client.call_tool("get_guide", {"guide_id": "durability", "language": "cs"})
            self.assertFalse(result.is_error)
            self.assertIn("RPO", str(result))
            result = await client.call_tool("search_guides", {"query": "idempotency"})
            self.assertFalse(result.is_error)
            self.assertIn("durability", str(result))
            bad = await client.call_tool("get_guide", {"guide_id": "../../etc/passwd"})
            self.assertTrue(bad.is_error)
            resource = await client.read_resource("bestpractices://catalog")
            self.assertIn("architecture", str(resource))


if __name__ == "__main__":
    unittest.main()
