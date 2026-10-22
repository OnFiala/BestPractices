"""Read the same reviewed content from the website, CLI, and MCP adapter."""

import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = ("en", "cs", "de", "es")


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_markdown(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"Missing JSON front matter: {path}")
    metadata, body = text[4:].split("\n---\n", 1)
    return json.loads(metadata), body


def catalog(root: Path = ROOT) -> list[dict]:
    return read_json(root / "data/catalog.json")["guides"]


def guide(guide_id: str, language: str = "en", root: Path = ROOT) -> dict:
    if language not in LANGUAGES:
        raise ValueError("Unsupported language")
    entry = next((g for g in catalog(root) if g["id"] == guide_id), None)
    if entry is None:
        raise ValueError("Unknown guide ID")
    base = (root / "docs" / language).resolve()
    path = (base / entry["path"]).resolve()
    if not path.is_relative_to(base):
        raise ValueError("Guide path escapes the library")
    metadata, body = read_markdown(path)
    return {
        "id": guide_id,
        "language": language,
        "title": entry["title"][language],
        "status": entry["status"],
        "revision": entry["revision"],
        "sources": entry["sources"],
        "related": entry["related"],
        "reviewed_on": metadata["reviewed_on"],
        "content": body,
    }


def normalize(text: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", text.casefold())
                   if not unicodedata.combining(c))


def search(query: str, language: str = "en", limit: int = 8, root: Path = ROOT) -> list[dict]:
    if language not in LANGUAGES or not 1 <= limit <= 20 or len(query) > 300:
        raise ValueError("Invalid search parameters")
    terms = re.findall(r"\w+", normalize(query))
    if not terms:
        return []
    matches = []
    for entry in catalog(root):
        item = guide(entry["id"], language, root)
        title, body = normalize(item["title"]), normalize(item["content"])
        if not all(term in title or term in body for term in terms):
            continue
        score = sum(5 * title.count(t) + min(body.count(t), 5) for t in terms)
        excerpt = " ".join(item.pop("content").split())[:500]
        matches.append((score, {**item, "excerpt": excerpt}))
    matches.sort(key=lambda item: (-item[0], item[1]["id"]))
    return [item for _, item in matches[:limit]]
