"""Preserve reviewed website notices and corresponding source without fetching at build time."""

import hashlib
import html
import importlib.metadata
import json
import shutil
from pathlib import Path

LOCALE_DIRS = ("", "cs", "de", "es")


def _digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _inside(root: Path, relative: str) -> Path:
    path = root / relative
    if Path(relative).is_absolute() or ".." in Path(relative).parts:
        raise ValueError(f"Unsafe license inventory path: {relative}")
    if path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"License inventory path escapes its root: {relative}")
    return path


def publish_licenses(root: Path, destination: Path) -> None:
    """Validate reviewed assets in all locales and publish notices and MPL source.

    Unknown or changed vendor code fails the build. Unused upstream language
    assets are removed from this four-language distribution. No upstream prose
    or network access is needed; legal files and required source are versioned.
    """
    manifest_path = root / "data/third-party-assets.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("schema_version") != 1:
        raise ValueError("Unsupported third-party asset inventory")
    for package, expected in manifest["build_dependencies"].items():
        if importlib.metadata.version(package) != expected:
            raise ValueError(f"Review website licenses after changing {package}")

    legal = manifest["legal_files"] + manifest["corresponding_sources"]
    if not manifest["legal_files"] or not manifest["corresponding_sources"]:
        raise ValueError("Website distribution requires notices and corresponding source")
    legal_paths = {entry["path"] for entry in manifest["legal_files"]}
    for component in manifest.get("components", []):
        if not component.get("license_files") or not set(component["license_files"]) <= legal_paths:
            raise ValueError(f"Component has no retained license notice: {component['id']}")
    for entry in legal:
        source = _inside(root, entry["path"])
        if not source.is_file() or _digest(source) != entry["sha256"]:
            raise ValueError(f"Missing or altered required legal/source file: {entry['path']}")

    reviewed = {item["path"]: item["sha256"] for item in manifest["vendor_assets"]}
    own_assets = {"assets/" + str(p.relative_to(root / "web/assets")): _digest(p)
                  for p in (root / "web/assets").rglob("*") if p.is_file()}
    allowed = reviewed | own_assets
    for locale in LOCALE_DIRS:
        site = destination / locale
        for pruning in manifest["prune_unused"]:
            directory = _inside(site, pruning["directory"])
            keep = set(pruning["keep"])
            if directory.is_dir():
                for path in directory.rglob("*"):
                    if path.is_symlink():
                        raise ValueError(f"Unexpected symlink in vendor assets: {path}")
                    if path.is_file() and str(path.relative_to(directory)) not in keep:
                        path.unlink()
        actual = {str(p.relative_to(site)): p for p in (site / "assets").rglob("*")
                  if p.is_file()}
        if set(actual) != set(allowed):
            missing, extra = set(allowed) - set(actual), set(actual) - set(allowed)
            raise ValueError(f"Unreviewed website asset inventory ({locale or 'en'}): "
                             f"missing={sorted(missing)}, extra={sorted(extra)}")
        for relative, path in actual.items():
            _inside(site, relative)
            if _digest(path) != allowed[relative]:
                raise ValueError(f"Changed website asset needs license review: {relative}")

    for entry in legal:
        target = _inside(destination, entry["path"])
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(_inside(root, entry["path"]), target)
    for name in ("LICENSE-CONTENT", "LICENSE-CODE", "THIRD_PARTY_NOTICES.md"):
        shutil.copyfile(root / name, destination / name)
    shutil.copyfile(manifest_path, destination / "third-party-assets.json")
    (destination / "data").mkdir(exist_ok=True)
    shutil.copyfile(manifest_path, destination / "data/third-party-assets.json")

    # The Markdown renderer is already a locked documentation dependency. Legal
    # notices contain trusted, reviewed repository text, never fetched evidence.
    import markdown

    body = markdown.markdown((root / "THIRD_PARTY_NOTICES.md").read_text(encoding="utf-8"),
                             extensions=["tables"])
    page = ('<!doctype html><html lang="en"><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            '<title>Third-party notices · BestPractices</title>'
            '<style>body{max-width:78rem;margin:2rem auto;padding:0 1rem;'
            'font:1rem/1.6 system-ui,sans-serif}table{border-collapse:collapse;'
            'display:block;overflow-x:auto}td,th{padding:.4rem;border:1px solid #aaa}'
            'pre{white-space:pre-wrap}a{overflow-wrap:anywhere}</style><body>'
            '<nav><a href="./">BestPractices</a></nav><main>' + body + '</main>'
            '<p>Reviewed asset inventory: <a href="third-party-assets.json">' +
            html.escape(manifest["reviewed_on"]) + '</a>.</p></body></html>')
    (destination / "third-party-notices.html").write_text(page, encoding="utf-8")
