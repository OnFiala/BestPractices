"""Publication checks for third-party attribution and corresponding program source."""

import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from library.licensing import LOCALE_DIRS, publish_licenses


def digest(value):
    return hashlib.sha256(value).hexdigest()


class WebsiteLicenseTests(unittest.TestCase):
    def fixture(self, root):
        files = {
            "LICENSES/vendor.txt": b"Upstream license and copyright notice\n",
            "third_party/lunr_languages/stemmer.js": b"/* MPL source */ function stem() {}\n",
            "web/assets/own.js": b"// original project code\n",
            "LICENSE-CONTENT": b"Original prose remains CC BY 4.0 in exports.\n",
            "LICENSE-CODE": b"MIT license for original code.\n",
            "THIRD_PARTY_NOTICES.md": b"# Third-party notices\n\n[License](LICENSES/vendor.txt)\n",
        }
        for name, data in files.items():
            target = root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        vendor = b"/* reviewed vendor asset */\n"
        for locale in LOCALE_DIRS:
            site = root / "site" / locale
            (site / "assets/lunr").mkdir(parents=True)
            (site / "assets/vendor.js").write_bytes(vendor)
            (site / "assets/own.js").write_bytes(files["web/assets/own.js"])
            (site / "assets/lunr/unused.js").write_bytes(b"not redistributed\n")
        manifest = {
            "schema_version": 1, "reviewed_on": "2026-10-22",
            "build_dependencies": {"reviewed-package": "1.0"},
            "legal_files": [{"path": "LICENSES/vendor.txt",
                             "sha256": digest(files["LICENSES/vendor.txt"])}],
            "corresponding_sources": [{"path": "third_party/lunr_languages/stemmer.js",
                                       "sha256": digest(files["third_party/lunr_languages/stemmer.js"])}],
            "vendor_assets": [{"path": "assets/vendor.js", "sha256": digest(vendor)}],
            "prune_unused": [{"directory": "assets/lunr", "keep": []}],
        }
        (root / "data").mkdir()
        (root / "data/third-party-assets.json").write_text(json.dumps(manifest))
        return files

    @patch("library.licensing.importlib.metadata.version", return_value="1.0")
    def test_every_locale_has_only_reviewed_code_and_published_legal_source(self, _version):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            files = self.fixture(root)
            publish_licenses(root, root / "site")
            for locale in LOCALE_DIRS:
                self.assertFalse((root / "site" / locale / "assets/lunr/unused.js").exists())
            for name in ("LICENSES/vendor.txt", "third_party/lunr_languages/stemmer.js",
                         "LICENSE-CONTENT", "LICENSE-CODE"):
                self.assertEqual((root / "site" / name).read_bytes(), files[name])
            self.assertIn('href="LICENSES/vendor.txt"',
                          (root / "site/third-party-notices.html").read_text())

    @patch("library.licensing.importlib.metadata.version", return_value="1.0")
    def test_changed_source_notice_or_vendor_cannot_be_silently_published(self, _version):
        for relative in ("LICENSES/vendor.txt", "third_party/lunr_languages/stemmer.js",
                         "site/de/assets/vendor.js", "site/es/assets/unknown.js"):
            with self.subTest(relative=relative), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                self.fixture(root)
                (root / relative).write_bytes(b"changed without license review")
                with self.assertRaises(ValueError):
                    publish_licenses(root, root / "site")

    @patch("library.licensing.importlib.metadata.version", return_value="2.0")
    def test_dependency_upgrade_requires_inventory_review(self, _version):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture(root)
            with self.assertRaisesRegex(ValueError, "Review website licenses"):
                publish_licenses(root, root / "site")


if __name__ == "__main__":
    unittest.main()
