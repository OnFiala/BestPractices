---
{
  "id": "operations",
  "language": "de",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Zustand, Wiederherstellung und Kosten

## Das Nutzerergebnis beobachten

Wähle einen Service-Level-Indikator (SLI) für einen sinnvollen Ablauf, etwa den erfolgreichen Abschluss innerhalb einer Latenzgrenze. Definiere Zähler, Nenner, Beobachtungsfenster und Ausschlüsse und vereinbare anschließend mit dem Verantwortlichen das Service-Level-Ziel (SLO). Beziehe fehlgeschlagene und abgewiesene Arbeit ein, wo der Vertrag es verlangt; ein schneller Fehler ist keine erfolgreiche Transaktion.

Ein Fehlerbudget beschreibt die erlaubte Zielunterschreitung in diesem Zeitraum. Beispielsweise erlaubt ein anfragebezogenes Ziel von 99,9 % bei 100.000 berücksichtigten Anfragen 100 Anfragen außerhalb des Ziels; dies ist eine Rechnung, keine Zielempfehlung. Passe das Veröffentlichungsrisiko anhand des beobachteten Budgetverbrauchs und der geschäftlichen Auswirkungen an. Definiere die Reaktionsrichtlinie vor einem Vorfall, statt ein aufgebrauchtes Budget lediglich als Dashboard-Farbe zu behandeln.

Dieses Betriebsmodell ist eine Synthese der Bibliothek. Die zitierten Unterlagen zu Beobachtbarkeit und Gesundheitsendpunkten stützen die Messmechanismen; Prüfhäufigkeit und Eskalationsschwellen bleiben Projektentscheidungen.

## Gesundheitssignale unterscheiden

| Signal | Zweck und Grenze |
| --- | --- |
| Start | Initialisierung innerhalb einer ausdrücklichen Grenze abschließen lassen |
| Liveness | Einen Prozess erkennen, der nicht mehr vorankommt; ein Neustart muss eine sinnvolle Reaktion sein |
| Readiness | Entscheiden, ob eine Instanz bestimmten Verkehr empfangen soll |
| Synthetischer Nutzerablauf | Nutzersichtbares Verhalten über eine kontrollierte öffentliche Schnittstelle prüfen |
| Dienstmetriken und Traces | Ergebnisse, Sättigung und Beiträge von Abhängigkeiten im Zeitverlauf erklären |

Lass nicht jeden vorübergehenden Abhängigkeitsausfall die Liveness-Prüfung fehlschlagen und gesunde Prozesse neu starten. Tiefgehende Readiness-Prüfungen können bei einer gemeinsamen ausgefallenen Abhängigkeit ebenfalls alle Instanzen aus dem Verkehr nehmen; definiere eingeschränkten Betrieb und abhängigkeitsbezogene Grenzen. Gesundheitsprüfungen dürfen die gemessenen Ressourcen nicht erschöpfen. Schütze detaillierte Diagnosen und löse durch Prüfungen keine echten Zahlungen oder Nachrichten aus.

Nutze strukturierte Logs, Metriken und Traces mit Korrelations-IDs, begrenzter Label-Kardinalität und Unkenntlichmachung sensibler Daten. Alarmiere bei Symptomen mit konkretem Handlungsbedarf oder anhaltendem Fehlerbudgetverbrauch und benenne Schweregrad, Verantwortlichen, Betriebshandbuch und Eskalation. Prüfe, dass der Alarm jemanden erreicht, der reagieren kann. Ein Dashboard oder HTTP 200 allein beweist keine Verfügbarkeit.

## Vorfall und Wiederherstellung üben

Benenne eine Vorfallleitung, bestimme die Nutzerauswirkungen, stabilisiere das System, sichere notwendige Nachweise und kommuniziere Unsicherheit. Deaktiviere riskante Wiederholungen oder Agentenaktionen, wenn sie Schäden verstärken. Bevorzuge eine bekannte sichere Wiederherstellungsmaßnahme gegenüber einem ungetesteten Notfallumbau. Gleiche nach der Wiederherstellung dauerhafte Arbeit und Anbieterwirkungen ab, bevor die Automatisierung fortgesetzt wird.

Stelle in einer isolierten Umgebung ein Backup wieder her, widerrufe oder rotiere Zugangsdaten und simuliere einen nicht erreichbaren Anbieter. Miss Wiederherstellungsdauer und Datenverlustzeitraum und prüfe anschließend einen echten Nutzerablauf sowie geschäftliche Invarianten. Nutze [Black-Box-Prüfungen](testing-strategy.md) für beobachtbares Verhalten und [Leistungs-/Wiederherstellungstests](performance-testing.md) für den Abbau eines Rückstaus nach Sättigung. Dokumentiere tatsächliche Ergebnisse, Artefaktversionen und verbleibende manuelle Schritte.

Halte nach einem Vorfall beitragende Bedingungen und Maßnahmen mit Verantwortlichen und Fristen fest. Ergänze einen Regressionstest, wenn er das reparierte Verhalten nachweisen kann. Bewahre nützliche Betriebserkenntnisse auf, ohne personenbezogene Daten oder Zugangsdaten zu veröffentlichen.

## Verantwortung und Ausgaben sichtbar halten

Miss Kosten pro nützlicher Transaktion und Agentenaufgabe einschließlich Wiederholungen, Tokens, ausgehendem Datentransfer und Beobachtbarkeit. Definiere einen Alarm und einen durchgesetzten Stopp oder eingeschränkten Betrieb; eine E-Mail-Warnung allein begrenzt keine Ausgaben. Prüfe regelmäßig ungeklärte Alarme, Änderungen an Quellen und Abhängigkeiten sowie Ausgaben. Bewerte Ziele, Kapazität und Wiederherstellungsnachweise nach wesentlichen Änderungen neu; wähle einen wiederkehrenden Rhythmus, den der Verantwortliche aufrechterhalten kann.

Ein System ist gesund, wenn seine Verantwortlichen Verhalten, Wiederherstellung und eine tragbare Betriebsverpflichtung nachweisen können. Mehr Replikate ersetzen keinen Verantwortlichen, und kein einzelner Testlauf garantiert zukünftige Zuverlässigkeit.

## Verwandte Entscheidungen

[Beständigkeit](durability.md) · [Skalierung](scaling.md) · [Lebenszyklus](lifecycle.md) · [Teststrategie](testing-strategy.md) · [Leistungstests](performance-testing.md)

## Primärbelege

[observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [azure-health-endpoints](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/health-endpoint-monitoring.md)
