---
{
  "id": "start",
  "language": "de",
  "revision": 3,
  "translation_revision": 3,
  "reviewed_on": "2026-10-22"
}
---
# Systeme bauen, die Bestand haben

Eine praktische Bibliothek für den gesamten Lebenszyklus von Software: von der ersten Problemformulierung über zuverlässigen Betrieb bis zu Migration und Stilllegung. Menschen verantworten Ziel und Risiko. Agenten setzen begrenzte Entscheidungen in geprüfte Änderungen um. Englisch ist maßgeblich; Tschechisch, Deutsch und Spanisch verwenden dieselben Leitfadenkennungen und Revisionen.

Diese Bibliothek ist selbst ein **von Agenten gepflegtes Entscheidungssystem**: KI-Agenten recherchieren, schreiben, übersetzen und prüfen. Menschen verantworten Anwendbarkeit, Rechteprüfung, Zusammenführung und Veröffentlichung. Empfehlungen sind kontextabhängige Vorschläge, keine universell zertifizierten Regeln. Die technischen Erläuterungen sind eigenständige Zusammenführungen; zitierte Dokumente behalten ihre Lizenzen und werden nicht als unsere Inhalte wiedergegeben.

## Ich habe ein Projekt: Wo fange ich an?

Nutze diese Bibliothek, um einem Agenten eine klare Aufgabe zu geben, einen
geeigneten Ansatz zu wählen und das Ergebnis zu prüfen. Sie liefert Empfehlungen,
einen Plan und Nachweisprüfungen. Dein Agent erstellt das eigentliche Produkt
in deiner Entwicklungsumgebung.

1. Lies [die Anleitung zur Einführung](guides/adoption.md): Wähle das JSON-Auslieferungsprofil
   für die Werkzeuge und bei Bedarf ein YAML-Dokument für ausführlichere Entscheidungsgrundlagen.
2. Durchlaufe [deinen ersten Prüfpunkt mit Nachweisen](guides/first-project.md): Erstelle
   ein tatsächliches Ergebnis, lass es prüfen und sieh nach, was weiterhin blockiert ist. Eine Modell-API ist nicht erforderlich.
3. Wähle unten dein Projekt und folge dann [dem Auslieferungsablauf](guides/project-delivery.md).

| Was entwickelst du? | Hier beginnen |
| --- | --- |
| Öffentliche Website | [Öffentliche Website](guides/playbook-public-website.md) |
| SaaS | [SaaS](guides/playbook-saas.md) |
| Internes Betriebswerkzeug | [Internes Werkzeug](guides/playbook-internal-tool.md) |
| KI-Anwendung | [KI-Anwendung](guides/playbook-ai-application.md) |
| Agentenautomatisierung | [Agentenautomatisierung](guides/playbook-agent-automation.md) |
| Backend und mobile Clients | [Mobiles Backend](guides/playbook-mobile-backend.md) |

## Gib deinem Agenten seine erste Aufgabe

Ersetze die Werte in eckigen Klammern und übergib diesen Text einem Agenten,
der dein Projekt und eine vertrauenswürdige lokale Arbeitskopie dieser Bibliothek
lesen kann. Eine Plugin- oder MCP-Installation ist nicht erforderlich.

```text
Arbeite in [Zielprojekt]. Nutze [BestPractices-Arbeitskopie] als Referenz.
Lies die Anweisungen des Zielprojekts, dann in der Bibliothek
plugins/bestpractices/skills/project-delivery/SKILL.md und den passenden Projektleitfaden.
Ergebnis: [beobachtbares Ergebnis]. Einschränkungen: [Daten, Budget, erlaubte Effekte].
Dokumentiere die Bibliotheksrevision. Erstelle ein JSON-Auslieferungsprofil anhand
der tatsächlichen Anforderungen und der Git-Zielrevision; kennzeichne Unbekanntes ausdrücklich.
Führe den Planer aus und bearbeite den ersten unerfüllten Prüfpunkt. Erstelle dessen
tatsächliches Artefakt, führe eine passende Prüfung durch und hole eine unabhängige
Begutachtung ein, sofern sie verfügbar ist.
Erfinde keine Ergebnisse oder Prüfer. Berichte über die Nachweise und verbleibenden Hindernisse.
Arbeite lokal; führe keine Bereitstellung durch und verändere die Referenzbibliothek nicht.
```

Ein **Prüfpunkt** verlangt bestimmte Ergebnisse. Ein **Artefakt** ist ein Dokument,
eine Codeänderung oder ein Bericht. **Nachweise** beschreiben eine tatsächlich
durchgeführte Begutachtung oder Prüfung dieses Ergebnisses. Das Erstellen eines
Plans setzt das Projekt nicht um und berechtigt nicht zur Veröffentlichung.
Was lokal nachgewiesen ist und was noch projektspezifische Belege erfordert,
erläutert [Abdeckung und Grenzen](guides/coverage.md).

## Nach Bedarf lesen

Architektur- und Hosting-Leitfäden helfen bei der Grundform. Beständigkeit, Daten, Sicherheit und Frontend erklären die Verträge innerhalb dieser Form. GitHub, Qualität und Agenten regeln die Auslieferung. Betrieb und Pflege halten Produkte und diese Bibliothek gesund.

Beginne zur Überprüfung mit der [Testauswahl](guides/testing-strategy.md). Sie trennt Zweck, Ebene und verfügbares Wissen; Black Box bedeutet nicht nur Penetrationstest. Nutze [Leistungstests](guides/performance-testing.md) für Last-, Stress-, Spitzenlast-, Dauer- und Kapazitätsexperimente sowie [Sicherheitstests](guides/security-testing.md) für risikobasierte Kontrollen und begrenzte Untersuchungen. Jeder Leitfaden gibt Agenten Auswahlkriterien, Nachweisanforderungen und Abbruchbedingungen.

Jeder Leitfaden nennt anwendbaren Kontext, Entscheidung, Abwägungen, Prüfungen und Änderungssignale. Ein erfolgreicher Quellenabruf belegt Verfügbarkeit, nicht die Richtigkeit einer Empfehlung. Diese erste Ausgabe enthält Vorschläge, die menschliches Review benötigen; auch Übersetzungen brauchen redaktionelle Prüfung. Experimentelle Browserintegrationen bleiben ausdrücklich experimentell.

Wechsle Sprachen über das Sprachmenü, finde Begriffe mit der Suche und verfolge Zusammenhänge über verwandte Leitfäden. Klone das Repository zum Offline-Lesen. Website und schreibgeschützter MCP-Adapter verwenden dieselben Inhalte. Zum Lesen, Bauen oder Validieren ist keine kostenpflichtige Modell-API erforderlich.

## Verwandte Entscheidungen

[Entscheidungsprinzipien](guides/foundations.md) · [Der vollständige Projektlebenszyklus](guides/lifecycle.md) · [Architekturen auswählen und verbinden](guides/architecture.md) · [Die Bibliothek im Projekt einsetzen](guides/adoption.md)

## Primärbelege

[plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md) · [github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md)
