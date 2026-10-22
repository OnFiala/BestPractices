---
{
  "id": "start",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Systeme bauen, die Bestand haben

Eine Arbeitsbibliothek für den gesamten Softwarelebenszyklus: von der Problemdefinition über zuverlässigen Betrieb bis zur Migration und Stilllegung. Menschen verantworten Ziele und Risiken. Agenten setzen begrenzte Entscheidungen in geprüfte Änderungen um. Englisch ist maßgeblich; Tschechisch, Deutsch und Spanisch verwenden dieselben Kennungen und Revisionen.

## Mit einer Entscheidung beginnen

1. Ergebnis, Datensensibilität, Betriebsbudget und tolerierbare Ausfälle im Projektprofil festhalten.
2. Die kleinste Architektur wählen, die diese Anforderungen erfüllt. Ein persönliches Werkzeug kann sensible Daten verarbeiten; eine Million registrierter Konten bedeutet nicht automatisch hohe Parallelität.
3. Wesentliche Entscheidungen in einem ADR festhalten: Belege, Alternativen und Rückweg gehören dazu.
4. Einem Agenten eine kleine Aufgabe mit Abnahmekriterien geben. Unabhängige Prüfung und menschliche Freigabe zum Zusammenführen verlangen.
5. Das Gebaute betreiben: reales Verhalten beobachten, Wiederherstellung testen und Annahmen anhand neuer Belege prüfen.

## Nach Bedarf lesen

Architektur und Hosting helfen bei der Systemform. Beständigkeit, Daten, Sicherheit und Frontend beschreiben innere Verträge. GitHub, Qualität und Agenten regeln die Lieferung. Betrieb und Pflege erhalten Produkte und Bibliothek.

Jeder Leitfaden beschreibt Kontext, Entscheidung, Zielkonflikte, Prüfungen und Änderungssignale. Ein abgerufener Text belegt Erreichbarkeit, nicht die Richtigkeit einer Empfehlung. Diese erste Ausgabe enthält Vorschläge zur menschlichen Prüfung; auch Übersetzungen benötigen redaktionelle Prüfung. Experimentelle Browserintegration bleibt gekennzeichnet.

Über das Sprachmenü wechseln, mit der Suche Begriffe finden und über verwandte Leitfäden Zusammenhänge verfolgen. Das Repository ermöglicht Offlinelektüre; Website und lesender MCP-Adapter nutzen denselben Inhalt. Lesen, Bauen und Validieren benötigen keine kostenpflichtige Modell-API.

## Verwandte Entscheidungen

[Entscheidungsprinzipien](guides/foundations.md) · [Der vollständige Projektlebenszyklus](guides/lifecycle.md) · [Architekturen auswählen und verbinden](guides/architecture.md) · [Die Bibliothek im Projekt einsetzen](guides/adoption.md)

## Primärbelege

[plugins](https://raw.githubusercontent.com/openai/plugins/main/README.md) · [github-rulesets](https://raw.githubusercontent.com/github/docs/main/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/main/content/en/docs/concepts/observability-primer.md)
