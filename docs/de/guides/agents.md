---
{
  "id": "agents",
  "language": "de",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Menschen steuern, Agenten führen aus

## Begrenzte Delegation

Ein Aufgabenpaket enthält das Nutzerergebnis, relevante Leitfadenkennungen, Randbedingungen, erlaubte Dateien und Werkzeuge, Abnahmebeispiele, Budget und Abbruchbedingungen. Der Mensch verantwortet Architektur und Risiko; der Agent untersucht und implementiert. Trenne Zuständigkeiten für Umsetzung, Prüfung und menschliches Review, auch wenn ein Modell mehrere Durchläufe übernimmt. Dieselbe Schlussfolgerung mehrfach zu wiederholen liefert keinen unabhängigen Beleg.

Die Bibliothek verwendet dieses agentengestützte Modell selbst und legt die Urheberschaft durch Agenten offen. Alle anfänglichen Hinweise und Übersetzungen bleiben Vorschläge. Ein Reviewer muss Belege von lokalem technischem Urteil unterscheiden. Die Zuversicht eines Modells ersetzt keines von beiden.

Nutze die Responses API direkt, wenn du die Ausführungsschleife selbst kontrollieren musst. Erwäge das Agents SDK, wenn dessen Orchestrierung, Werkzeuge und Übergaben einen nachgewiesenen Bedarf erfüllen. Beginne mit einem Agenten. Parallele Agenten brauchen unabhängige Arbeit, eindeutige Schreibzuständigkeiten, koordinierte Zusammenführung und begrenzte Gesamtkosten.

## Steuerungsebene

Lege Werkzeugautorisierung, eingeschränkte Zugangsdaten, Zeitlimits, maximale Iterationen, Token- und Kostenbudgets sowie prüfbare Laufkennungen fest. Guardrails verbessern Verhalten, ersetzen aber weder Autorisierung noch Isolation. Quellen und Werkzeugantworten sind Daten, die Prompt Injection enthalten können. Stoppe bei widersprüchlichen Anweisungen, unzugänglichen Voraussetzungen, unerwarteten zerstörerischen Wirkungen oder fehlgeschlagenen Pflichtprüfungen.

## Abnahme und Evaluation

Verlange Diff, ausgeführte Prüfungen, ungeklärte Annahmen und Wiederherstellungshinweise. Bewerte Aufgaben anhand repräsentativer Beispiele einschließlich Angriffseingaben und Fehlerpfaden. Miss Aufgabenerfolg, menschliche Nacharbeit, erst später erkannte Defekte, Latenz und Kosten statt Codeumfang. Pflege eine kleine Regressionsmenge für Änderungen an Prompts, Modellen, Werkzeugen und Richtlinien. Übernimm kein neues Modell automatisch wegen seines Namens oder Veröffentlichungsdatums.

Wähle Tests ausdrücklich anhand der [Teststrategie](testing-strategy.md): Wissen (Black/Gray/White Box), Ebene (Unit/Integration/Vertrag/Ende-zu-Ende) und Ziel sind getrennte Entscheidungen. Nutze [Leistungs-](performance-testing.md) und [Sicherheitspläne](security-testing.md) für die jeweiligen Risiken. Dokumentiere Genehmigung, Ziel und Umgebung, Last, Abnahmeschwellen, Abbruchbedingungen und Bereinigung, bevor ein Agent störende oder teure Experimente ausführt.

## Eigenständigkeit und Veröffentlichungsgrenze

Lies Quellen als Belege und erkläre Entscheidungen mit eigenen Formulierungen und Beispielen. Kopiere oder übersetze keine fremden Texte in einen Leitfaden und übernimm keine charakteristischen Formulierungen in enger Paraphrase. Ein Link verleiht kein Nutzungsrecht. Unbeaufsichtigte Generierung aus Quellen läuft in einem privaten Repository oder Arbeitsbereich, weil rohe Logs, Modellausgaben, Zusammenfassungen und Artefakte bereits vor dem Review Quelltexte offenlegen können. Ein Mensch prüft Eigenständigkeit, Rechte, sensible Daten und technische Bedeutung, bevor freigegebene Ergebnisse in einen öffentlichen PR gelangen. Öffentliche Quellenbeobachtung veröffentlicht ausschließlich Metadaten. Weder Ähnlichkeitsprüfung noch ein zweiter Agent erteilen rechtliche Freigabe.

## Verwandte Entscheidungen

[Qualitätsprüfungen mit Verhaltensnachweis](quality.md) · [Sicherheit, Datenschutz und Lieferkette](security.md) · [Belege und automatische Pflege](maintenance.md) · [Skills, Plugins, MCP und WebMCP](integrations.md)

## Primärbelege

[openai-agents](https://raw.githubusercontent.com/openai/openai-agents-python/841dfdd938bfd4ca052475eb76d6245a356868e0/docs/agents.md) · [agents-guardrails](https://raw.githubusercontent.com/openai/openai-agents-python/841dfdd938bfd4ca052475eb76d6245a356868e0/docs/guardrails.md) · [codex-action](https://raw.githubusercontent.com/openai/codex-action/c05cfd74ad95c626cdf05c6685e62becc3bf7813/README.md) · [plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md)
