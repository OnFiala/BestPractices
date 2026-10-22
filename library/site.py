"""Build four isolated MkDocs sites with a shared catalog and portable language links."""

import argparse
import functools
import html
import http.server
import json
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

from library.content import LANGUAGES, ROOT, catalog, guide
from library.licensing import publish_licenses
from library.validate import validate

NAMES = {"en": "English", "cs": "Čeština", "de": "Deutsch", "es": "Español"}
DISCLOSURE = {
    "en": "Created and maintained with AI agents. Humans own review and publication.",
    "cs": "Vytvořeno a udržováno pomocí AI agentů. Za posouzení a zveřejnění odpovídají lidé.",
    "de": "Mit KI-Agenten erstellt und gepflegt. Menschen verantworten Prüfung und Veröffentlichung.",
    "es": "Biblioteca creada y mantenida con agentes de IA. Las personas son responsables de la revisión y publicación.",
}
LICENSE_LABELS = {
    "en": ("Original text: CC BY 4.0 · Original code: MIT", "Third-party notices"),
    "cs": ("Vlastní texty: CC BY 4.0 · Vlastní kód: MIT", "Licence třetích stran"),
    "de": ("Eigene Texte: CC BY 4.0 · Eigener Code: MIT", "Hinweise zu Drittanbietern"),
    "es": ("Textos originales: CC BY 4.0 · Código original: MIT", "Avisos de terceros"),
}
LABELS = {
    "en": ("Proposed guidance · human review required", "Choose → build → verify → operate → revisit"),
    "cs": ("Návrh doporučení · vyžaduje lidské posouzení", "Zvolit → postavit → ověřit → provozovat → přezkoumat"),
    "de": ("Vorgeschlagene Leitlinien · menschliche Prüfung erforderlich", "Wählen → bauen → prüfen → betreiben → überdenken"),
    "es": ("Orientación propuesta · requiere revisión humana", "Elegir → construir → verificar → operar → revisar"),
}
STATUS = {
    "en": {"proposed": "Proposed · human review required", "adopted": "Adopted guidance",
           "experimental": "Experimental · verify compatibility", "deprecated": "Deprecated · plan migration"},
    "cs": {"proposed": "Návrh · vyžaduje lidské posouzení", "adopted": "Přijaté doporučení",
           "experimental": "Experiment · ověřte kompatibilitu", "deprecated": "Zastaralé · naplánujte migraci"},
    "de": {"proposed": "Vorschlag · menschliche Prüfung erforderlich", "adopted": "Angenommene Leitlinie",
           "experimental": "Experiment · Kompatibilität prüfen", "deprecated": "Abgekündigt · Migration planen"},
    "es": {"proposed": "Propuesta · requiere revisión humana", "adopted": "Orientación adoptada",
           "experimental": "Experimental · verificar compatibilidad", "deprecated": "Obsoleto · planificar migración"},
}


def build(root: Path = ROOT):
    errors = validate(root)
    if errors:
        raise ValueError("\n".join(errors))
    stage = root / ".build"
    stage.mkdir(exist_ok=True)
    entries = catalog(root)
    for language in LANGUAGES:
        docs = stage / language
        if docs.exists():
            shutil.rmtree(docs)
        shutil.copytree(root / "docs" / language, docs, dirs_exist_ok=True)
        shutil.copytree(root / "web/assets", docs / "assets", dirs_exist_ok=True)
        for entry in entries:
            path = docs / entry["path"]
            text = path.read_text(encoding="utf-8")
            _, rest = text[4:].split("\n---\n", 1)
            title, body = rest.split("\n", 1)
            badge = f'<p class="bp-status">{STATUS[language][entry["status"]]} · r{entry["revision"]}</p>'
            disclosure = ('<p class="bp-agent" data-authorship="agent-assisted">'
                          + html.escape(DISCLOSURE[language]) + '</p>')
            flow = ""
            if entry["id"] == "start":
                flow = f'<p class="bp-flow">{html.escape(LABELS[language][1])}</p>'
            path.write_text(title + "\n\n" + disclosure + badge + flow + body, encoding="utf-8")
        config = {
            "site_name": "BestPractices",
            "site_description": DISCLOSURE[language],
            "site_url": "https://onfiala.github.io/BestPractices/" +
                        ("" if language == "en" else language + "/"),
            "repo_url": "https://github.com/OnFiala/BestPractices",
            "edit_uri": "",
            "docs_dir": str(docs),
            "site_dir": str(root / "site" / ("" if language == "en" else language)),
            "theme": {
                "name": "material", "language": language,
                "custom_dir": str(root / "web/overrides"),
                "font": False,
                "palette": {"scheme": "default", "primary": "teal", "accent": "teal"},
                "features": ["navigation.sections", "navigation.top", "search.highlight", "content.code.copy"],
            },
            "plugins": [{"search": {"lang": [language if language != "cs" else "en"]}}],
            "hooks": [str(root / "library/site_hooks.py")],
            "markdown_extensions": ["admonition", "tables", "fenced_code", "attr_list", "toc"],
            "extra_css": ["assets/library.css"],
            "extra_javascript": ["assets/webmcp.js"],
            "extra": {"generator": False, "root_prefix": "." if language == "en" else "..",
                      "license_label": LICENSE_LABELS[language][0],
                      "notices_label": LICENSE_LABELS[language][1],
                      "alternate": [{"name": name, "lang": code,
                                     "link": "https://onfiala.github.io/BestPractices/" +
                                             ("" if code == "en" else code + "/")}
                                    for code, name in NAMES.items()]},
            "copyright": LICENSE_LABELS[language][0] + " · OnFiala & contributors",
            "nav": [{g["title"][language]: g["path"]} for g in entries],
            "validation": {"links": {"not_found": "warn", "anchors": "warn"},
                           "nav": {"omitted_files": "warn", "not_found": "warn"}},
        }
        cfg = stage / f"mkdocs-{language}.yml"
        cfg.write_text(yaml.safe_dump(config, allow_unicode=True, sort_keys=False), encoding="utf-8")
        subprocess.run([sys.executable, "-m", "mkdocs", "build", "--strict", "-f", str(cfg)],
                       cwd=root, check=True)
        destination = Path(config["site_dir"])
        payload = [guide(g["id"], language, root) | {
            "url": "" if g["path"] == "index.md" else g["path"].removesuffix(".md") + "/"
        } for g in entries]
        (destination / "guides.json").write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
    shutil.copy(root / "data/catalog.json", root / "site/catalog.json")
    for name in ("sources", "evidence", "tools", "blueprints"):
        shutil.copy(root / f"data/{name}.json", root / f"site/{name}.json")
    publish_licenses(root, root / "site")
    (root / "site/.nojekyll").touch()
    (root / "site/llms.txt").write_text(
        "# BestPractices\n\nAgent-maintained decision system. "
        "Original guidance and translations are agent-assisted; human review is required. "
        "Text including guides.json: CC BY 4.0; original code: MIT; third-party notices: "
        "third-party-notices.html. Proposed contextual guidance. "
        "English is canonical. Stable IDs and evidence: catalog.json.\n\n" +
        "\n".join(f"- [{g['id']}]({g['path'].replace('.md', '/') if g['path'] != 'index.md' else './'}): "
                  f"{g['title']['en']}" for g in entries) + "\n", encoding="utf-8")
    print(f"Built {len(entries) * len(LANGUAGES)} localized pages in {root / 'site'}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["build", "serve"])
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    build()
    if args.command == "serve":
        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT / "site")
        server = http.server.ThreadingHTTPServer(("127.0.0.1", args.port), handler)
        print(f"Serving all languages on loopback port {args.port}; Ctrl-C stops it.", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            server.server_close()


if __name__ == "__main__":
    main()
