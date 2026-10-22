---
{
  "id": "start",
  "language": "de",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Systeme bauen, die Bestand haben

Eine praktische Bibliothek für den gesamten Lebenszyklus von Software: von der ersten Problemformulierung über zuverlässigen Betrieb bis zu Migration und Stilllegung. Menschen verantworten Ziel und Risiko. Agenten setzen begrenzte Entscheidungen in geprüfte Änderungen um. Englisch ist maßgeblich; Tschechisch, Deutsch und Spanisch verwenden dieselben Leitfadenkennungen und Revisionen.

Diese Bibliothek ist selbst ein **von Agenten gepflegtes Entscheidungssystem**: KI-Agenten recherchieren, schreiben, übersetzen und prüfen. Menschen verantworten Anwendbarkeit, Rechteprüfung, Zusammenführung und Veröffentlichung. Empfehlungen sind kontextabhängige Vorschläge, keine universell zertifizierten Regeln. Die technischen Erläuterungen sind eigenständige Zusammenführungen; zitierte Dokumente behalten ihre Lizenzen und werden nicht als unsere Inhalte wiedergegeben.

## Mit einer Entscheidung beginnen

1. Halte Ergebnis, Datensensibilität, Betriebsbudget und akzeptable Ausfallzeit in einem Projektprofil fest.
2. Wähle die kleinste Architektur, die diese Bedingungen erfüllt. Ein persönliches Werkzeug kann sensible Daten verarbeiten; eine Million registrierte Konten kann dennoch geringe gleichzeitige Last erzeugen.
3. Dokumentiere folgenreiche Entscheidungen in einem Architecture Decision Record (ADR). Verknüpfe Belege, Alternativen und einen Rückweg.
4. Gib einem Agenten eine kleine Aufgabe mit Abnahmekriterien. Verlange eine unabhängige Prüfung und eine Zusammenführung durch einen Menschen.
5. Betreibe das Gebaute: Beobachte reales Verhalten, teste Wiederherstellung und überarbeite Annahmen bei neuen Erkenntnissen.

## Nach Bedarf lesen

Architektur- und Hosting-Leitfäden helfen bei der Grundform. Beständigkeit, Daten, Sicherheit und Frontend erklären die Verträge innerhalb dieser Form. GitHub, Qualität und Agenten regeln die Auslieferung. Betrieb und Pflege halten Produkte und diese Bibliothek gesund.

Beginne zur Überprüfung mit der [Testauswahl](guides/testing-strategy.md). Sie trennt Zweck, Ebene und verfügbares Wissen; Black Box bedeutet nicht nur Penetrationstest. Nutze [Leistungstests](guides/performance-testing.md) für Last-, Stress-, Spitzenlast-, Dauer- und Kapazitätsexperimente sowie [Sicherheitstests](guides/security-testing.md) für risikobasierte Kontrollen und begrenzte Untersuchungen. Jeder Leitfaden gibt Agenten Auswahlkriterien, Nachweisanforderungen und Abbruchbedingungen.

Jeder Leitfaden nennt anwendbaren Kontext, Entscheidung, Abwägungen, Prüfungen und Änderungssignale. Ein erfolgreicher Quellenabruf belegt Verfügbarkeit, nicht die Richtigkeit einer Empfehlung. Diese erste Ausgabe enthält Vorschläge, die menschliches Review benötigen; auch Übersetzungen brauchen redaktionelle Prüfung. Experimentelle Browserintegrationen bleiben ausdrücklich experimentell.

Wechsle Sprachen über das Sprachmenü, finde Begriffe mit der Suche und verfolge Zusammenhänge über verwandte Leitfäden. Klone das Repository zum Offline-Lesen. Website und schreibgeschützter MCP-Adapter verwenden dieselben Inhalte. Zum Lesen, Bauen oder Validieren ist keine kostenpflichtige Modell-API erforderlich.

## Verwandte Entscheidungen

[Entscheidungsprinzipien](guides/foundations.md) · [Der vollständige Projektlebenszyklus](guides/lifecycle.md) · [Architekturen auswählen und verbinden](guides/architecture.md) · [Die Bibliothek im Projekt einsetzen](guides/adoption.md)

## Primärbelege

[plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md) · [github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md)
