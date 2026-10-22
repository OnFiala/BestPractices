"""Fail closed on broken IDs, translations, evidence references, and local links."""

import argparse
import datetime as dt
import re
from pathlib import Path

from library.content import LANGUAGES, ROOT, catalog, read_json, read_markdown


def validate(root: Path = ROOT) -> list[str]:
    errors = []

    def require(condition, message):
        if not condition:
            errors.append(message)

    for filename in ("catalog", "sources", "source-baseline", "tools", "blueprints"):
        require(read_json(root / f"data/{filename}.json").get("schema_version") == 1,
                f"Unsupported schema version: {filename}")
    sources = read_json(root / "data/sources.json")["sources"]
    source_ids = {s["id"] for s in sources}
    require(len(source_ids) == len(sources), "Duplicate source ID")
    for source in sources:
        require(bool(re.fullmatch(r"[a-z0-9-]+", source["id"])), "Invalid source ID")
        require(source["url"].startswith("https://raw.githubusercontent.com/"),
                f"Source must use the reviewed fetch host: {source['id']}")
        require(source["authority"] == "primary", f"Unclassified source: {source['id']}")
        require(source["review_days"] in range(7, 366), "Invalid source review window")
    guides = catalog(root)
    ids = {g["id"] for g in guides}
    profiles = read_json(root / "data/blueprints.json")["profiles"]
    require(len({p["id"] for p in profiles}) == len(profiles), "Duplicate blueprint ID")
    for profile in profiles:
        require(set(profile["guides"]) <= ids and bool(profile["acceptance"]),
                f"Invalid blueprint: {profile['id']}")
    require(len(ids) == len(guides), "Duplicate guide ID")
    paths = set()
    for g in guides:
        gid = g["id"]
        require(bool(re.fullmatch(r"[a-z0-9-]+", gid)), f"Invalid guide ID: {gid}")
        require(g["path"] not in paths, f"Duplicate guide path: {g['path']}")
        paths.add(g["path"])
        require(g["status"] in {"proposed", "adopted", "experimental", "deprecated"},
                f"Invalid status: {gid}")
        require(bool(g["sources"]) and set(g["sources"]) <= source_ids,
                f"Missing/unknown evidence: {gid}")
        require(set(g["related"]) <= ids and gid not in g["related"],
                f"Invalid related guides: {gid}")
        require(set(g["title"]) == set(LANGUAGES), f"Missing localized titles: {gid}")
        for lang in LANGUAGES:
            base = (root / "docs" / lang).resolve()
            path = (base / g["path"]).resolve()
            if not path.is_relative_to(base):
                errors.append(f"Escaping guide path: {gid}")
                continue
            if not path.is_file():
                errors.append(f"Missing translation: {lang}/{g['path']}")
                continue
            try:
                meta, body = read_markdown(path)
                require(meta["id"] == gid and meta["language"] == lang,
                        f"Mismatched identity: {path}")
                require(meta["revision"] == g["revision"] == meta["translation_revision"],
                        f"Stale translation: {path}")
                reviewed = dt.date.fromisoformat(meta["reviewed_on"])
                require(reviewed <= dt.date.today(), f"Future review: {path}")
                require(len(body.split()) >= 100, f"Incomplete guide: {path}")
                require(body.startswith("# "), f"Missing page title: {path}")
                require(not re.search(r"\b(TODO|TBD|LOREM IPSUM)\b", body),
                        f"Unresolved placeholder: {path}")
                # Check file links here; strict MkDocs builds check rendered anchors.
                for target in re.findall(r"\[[^\]]*\]\(([^)\s]+)\)", body):
                    if ":" in target or target.startswith("#"):
                        continue
                    local = (path.parent / target.split("#")[0]).resolve()
                    require(local.is_relative_to(base) and local.exists(),
                            f"Broken or escaping local link in {path}: {target}")
            except (KeyError, ValueError) as exc:
                errors.append(f"Invalid guide {path}: {exc}")
    for lang in LANGUAGES:
        actual = {str(p.relative_to(root / "docs" / lang))
                  for p in (root / "docs" / lang).rglob("*.md")}
        require(actual == paths, f"Uncatalogued/missing pages: {lang}: {actual ^ paths}")
    for tool in read_json(root / "data/tools.json")["tools"]:
        require(set(tool["sources"]) <= source_ids and bool(tool["sources"]),
                f"Tool without known evidence: {tool['id']}")
        require(tool["status"] in {"candidate", "used-here", "experimental", "deprecated"},
                f"Invalid tool status: {tool['id']}")
    baseline = read_json(root / "data/source-baseline.json")["observations"]
    require(set(baseline) == source_ids, "Source baseline does not cover registry")
    for sid, observation in baseline.items():
        require(bool(re.fullmatch(r"[0-9a-f]{64}", observation["sha256"])),
                f"Invalid source hash: {sid}")
        require(observation["status"] == "ok", f"Unverified baseline: {sid}")
    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        errors = validate(args.root)
    except (ValueError, KeyError, OSError) as exc:
        errors = [f"Invalid library: {exc}"]
    if errors:
        print("\n".join(errors))
        return 1
    print(f"Validated {len(catalog(args.root))} guides in {len(LANGUAGES)} languages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
