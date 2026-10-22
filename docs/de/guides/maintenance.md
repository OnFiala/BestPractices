---
{
  "id": "maintenance",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Belege und automatische Pflege

## Evidenzablauf

`data/sources.json` erfasst Primärquellen, Umfang, Prüftermin und Intervall. Die Baseline enthält erfolgreiche Abrufhashes. Ein geplanter Beobachter lädt begrenzte HTTPS-Dokumente und meldet Änderungen, Unerreichbarkeit und überfällige Prüfung. Ein Hashwechsel verlangt Prüfung, keine automatische Empfehlung. Fehlgeschlagener Abruf bedeutet nicht unverändert.

Der Workflow erstellt oder aktualisiert bei Handlungsbedarf einen Evidenz-PR. Er ändert weder akzeptierte Baseline noch mergt er. Ein Mensch prüft Quelldiff, Aussagen und Anwendbarkeit und aktualisiert gegebenenfalls Leitfäden, Übersetzungen, Termine und Baseline gemeinsam. HTTP 200 erneuert keinen fachlichen Prüftermin.

## Agentenpflege

Der optionale Codex-Workflow schlägt begrenzte Dokumentationsänderungen vor. GitHub-Secret und explizite Aktivierung sind nötig; lokale Prüfung und Quellenabruf brauchen keine bezahlte API. Agenten ändern vorhandene Übersetzungen und Katalogmetadaten. Ein separater Job öffnet einen Entwurfs-PR; kein Merge durch Agenten. Rulesets und menschliche Freigaben in GitHub aktivieren.

## Aktualität und Fehler

Schnelle KI-/Protokollquellen häufiger prüfen als stabile Prinzipien. Experimente, Abkündigungen und strittige Aussagen markieren; Migrationen verlinken. Fehlende Rechte, Netzfehler, fehlgeschlagene Tests und alte Übersetzungen bleiben sichtbar. Prüfverzug und Behebungszeit messen. Falsche Empfehlungen per Commit zurücknehmen und betroffene Projekte bewerten.

## Verwandte Entscheidungen

[GitHub, Versionen und saubere Arbeitsbäume](github.md) · [Menschen steuern, Agenten führen aus](agents.md) · [Verantwortung und offene Entscheidungen](governance.md)

## Primärbelege

[codex-action](https://raw.githubusercontent.com/openai/codex-action/main/README.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/main/content/actions/reference/security/secure-use.md) · [plugins](https://raw.githubusercontent.com/openai/plugins/main/README.md)
