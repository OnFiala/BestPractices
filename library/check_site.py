"""Check every generated local page/resource link and same-page language switch."""

import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from library.content import LANGUAGES, ROOT, catalog


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []
        self.alternates = {}
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("hreflang"):
            self.alternates[attrs["hreflang"]] = attrs["href"]
        for key in ("href", "src"):
            if attrs.get(key):
                self.targets.append(attrs[key])


def check(root: Path = ROOT) -> list[str]:
    site = (root / "site").resolve()
    errors, parsed = [], {}
    for path in site.rglob("*.html"):
        parser = Links()
        parser.feed(path.read_text(encoding="utf-8"))
        parsed[path.resolve()] = parser
    if not parsed:
        return ["No built pages"]
    for path, parser in parsed.items():
        for target in parser.targets:
            url = urlsplit(target)
            if url.scheme or url.netloc or target.startswith("/"):
                continue
            dest = (path.parent / unquote(url.path)).resolve() if url.path else path
            if dest.is_dir():
                dest /= "index.html"
            if not dest.is_relative_to(site) or not dest.exists():
                errors.append(f"Broken generated link: {path.relative_to(site)} -> {target}")
            elif url.fragment and dest in parsed and unquote(url.fragment) not in parsed[dest].ids:
                # Material owns runtime search/skip controls; ordinary document anchors must exist.
                errors.append(f"Broken generated anchor: {path.relative_to(site)} -> {target}")
    for g in catalog(root):
        suffix = Path("index.html") if g["path"] == "index.md" else Path(g["path"][:-3]) / "index.html"
        for lang in LANGUAGES:
            page = site / ("" if lang == "en" else lang) / suffix
            if page not in parsed:
                errors.append(f"Missing generated page: {page}")
                continue
            if set(parsed[page].alternates) != set(LANGUAGES):
                errors.append(f"Missing language switch: {page}")
            for other, href in parsed[page].alternates.items():
                dest = (page.parent / href).resolve()
                if dest.is_dir():
                    dest /= "index.html"
                expected = site / ("" if other == "en" else other) / suffix
                if dest != expected:
                    errors.append(f"Language switch loses page: {page} -> {href}")
    for lang in LANGUAGES:
        folder = site / ("" if lang == "en" else lang)
        for name in ("guides.json", "search/search_index.json"):
            if not (folder / name).is_file():
                errors.append(f"Missing index: {folder / name}")
            else:
                json.loads((folder / name).read_text(encoding="utf-8"))
    return errors


if __name__ == "__main__":
    errors = check()
    if errors:
        print("\n".join(errors))
        raise SystemExit(1)
    print("All generated local links, anchors, language switches, and search indexes passed.")
