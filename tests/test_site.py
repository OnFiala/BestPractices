"""Deployment URL regressions, including same-article multilingual metadata."""

import unittest
from types import SimpleNamespace
from urllib.parse import urljoin

from library.site import normalize_site_url
from library.site_hooks import on_page_context


class SiteURLTests(unittest.TestCase):
    def test_public_bases_and_loopback_preview(self):
        for value, expected in (
            ("https://architecture.ofops.co", "https://architecture.ofops.co/"),
            ("https://example.org/library/", "https://example.org/library/"),
            ("http://127.0.0.1:8000", "http://127.0.0.1:8000/"),
            ("http://[::1]:8000", "http://[::1]:8000/"),
        ):
            with self.subTest(value=value):
                self.assertEqual(normalize_site_url(value), expected)

    def test_ambiguous_or_secret_bearing_urls_fail(self):
        for value in ("", "/library", "//example.org", "javascript:alert(1)",
                      "http://example.org", "https://user:secret@example.org",
                      "https://example.org/?token=secret", "https://example.org/#part",
                      "https://example.org/?", "https://example.org/#",
                      "https://example.org:99999", "https://example.org:0",
                      "https://example.org:wrong", "https://exa\nmple.org",
                      "https://example.org/with space", "https://example.org/\\path"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                normalize_site_url(value)

    def test_language_links_preserve_origin_subpath_and_article(self):
        for base in ("https://architecture.ofops.co/", "https://example.org/library/"):
            for language in ("en", "cs", "de", "es"):
                for path in ("", "guides/architecture/"):
                    with self.subTest(base=base, language=language, path=path):
                        alternatives = [{"lang": code} for code in ("en", "cs", "de", "es")]
                        config = SimpleNamespace(theme={"language": language}, extra={
                            "base_url": base, "license_label": "CC BY 4.0",
                            "notices_label": "Notices", "alternate": alternatives,
                        })
                        on_page_context({}, SimpleNamespace(url=path), config, None)
                        current = base + ("" if language == "en" else language + "/") + path
                        for alternate in alternatives:
                            code = alternate["lang"]
                            expected = base + ("" if code == "en" else code + "/") + path
                            self.assertEqual(alternate["link"], expected)
                            self.assertEqual(urljoin(current, alternate["local"]), expected)


if __name__ == "__main__":
    unittest.main()
