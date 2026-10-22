---
{
  "id": "durability",
  "language": "de",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Beständigkeit und verteilte Arbeit

## Festlegen, was erhalten bleiben muss

Unterscheide die Beständigkeit gespeicherter Daten, die Verfügbarkeit des Dienstes und wiederaufnehmbare Arbeit. Eine Replik ist kein Backup, und eine erfolgreiche Nachrichtenzustellung beweist keine genau einmal ausgeführte geschäftliche Wirkung. Vereinbare für jede Fähigkeit den akzeptierten Datenverlustzeitraum (RPO), die Wiederherstellungszeit (RTO) und die nach außen sichtbaren Abgleichregeln. Der folgende Ausführungs- und Testvertrag ist eine eigenständige Synthese dieser Bibliothek; das Verhalten des Anbieters muss für die eingesetzte Version geprüft werden.

## Jeder Wirkung ein Zustandsmodell geben

Eine dauerhafte Operation benötigt eine stabile ID, einen authentifizierten Eigentümer, validierte Nutzdaten, einen aktuellen Zustand und ein beobachtbares Ergebnis. Begrenze Idempotenzschlüssel auf Mandant und Geschäftsaktion. Definiere das Verhalten, wenn ein Schlüssel mit anderen Nutzdaten wiederverwendet wird, eine Anfrage noch läuft oder Einträge ablaufen. Bewahre Informationen zur Duplikaterkennung mindestens für den unterstützten Wiederholungs- und Wiederverarbeitungshorizont auf; ältere Arbeit benötigt andernfalls einen gesonderten autorisierten Abgleichprozess.

Speichere bei einem lokalen Geschäftsübergang dessen Ergebnis und die Eindeutigkeitssicherung atomar. Muss eine Veröffentlichung einen festgeschriebenen Übergang abbilden, kann eine transaktionale Outbox Geschäftsänderung und Ereignis zusammen speichern. Verliert der Relay-Prozess die Bestätigung, kann er zweimal veröffentlichen; die Duplikaterkennung des Verbrauchers muss deshalb Teil seines eigenen dauerhaften Schreibvorgangs sein. Unabhängige externe Aufrufe werden dadurch nicht transaktional.

Klassifiziere Fehler vor einer Wiederholung. Validierungsfehler und verweigerte Berechtigungen benötigen eine endgültige Antwort; vorübergehende Fehler können begrenzte Wiederholungen erlauben. Weise einer Schicht die Verantwortung für Gesamtfrist und Wiederholungsbudget zu und berücksichtige darunterliegende SDK-Wiederholungen. Backoff und Zufallsstreuung mindern gleichzeitigen Wiederholungsdruck; sie rechtfertigen nicht, eine unsichere Wirkung zu wiederholen. Ein Abbruch nach dem Versand einer externen Anfrage kann ein unbekanntes Ergebnis hinterlassen, das abgeglichen werden muss.

## Durchgearbeitete Fehlerfolge

Betrachte einen Auftrag mit Zahlungsanbieter und nachgelagertem Erfüllungsereignis:

| Unterbrechung | Erforderliches beobachtbares Verhalten |
| --- | --- |
| Bevor die Auftrags-/Outbox-Transaktion festgeschrieben wird | Keines von beiden wird sichtbar; eine Wiederholung kann sicher beginnen |
| Nach dem Commit, vor der Ereignisveröffentlichung | Ein Relay-Prozess findet schließlich das ausstehende Ereignis; kein Auftrag verschwindet |
| Nach der Veröffentlichung, vor der Relay-Bestätigung | Doppelte Zustellung erzeugt einen beabsichtigten Zustandsübergang beim Verbraucher |
| Nach erfolgreicher Zahlung, bevor die Antwort eintrifft | Die unterstützte Operationskennung des Anbieters wiederverwenden oder dessen Zustand abfragen und abgleichen; nicht blind eine neue Belastung erzeugen |
| Während eines Worker-Upgrades | Laufende Arbeit wird unter einem ausdrücklich kompatiblen Zustands-/Versionsvertrag fortgesetzt oder zum Abgleich weitergeleitet |

Dies sind Abnahmebedingungen, keine Belege dafür, dass ein eingesetztes System sie erfüllt hat. Erzwinge in Staging jede Unterbrechung bei kontrolliertem Anbieterverhalten, wiederhole die Anfrage und untersuche anschließend dauerhaften Zustand und Anbieteraufzeichnungen. Prüfe sowohl erfolgreiche Wiederherstellung als auch ungeklärte Zustände, die einen Menschen benötigen. Nutze die [Teststrategie](testing-strategy.md) für Testorakel und Nachweispaket.

## Wiederverarbeitung und Wiederherstellung betreiben

Isoliere dauerhaft fehlschlagende Nachrichten mit einem Verantwortlichen und einer Begründung. Begrenze Wiederholungs- und Wiederverarbeitungsvolumen und autorisiere Wiederverarbeitung getrennt vom gewöhnlichen Lesen. Der Betreiber muss geltendes Schema, Reihenfolgeumfang und Duplikaterkennungszeitraum kennen. Eine Kompensation ist eine neue Geschäftsaktion; Rückerstattungen, Benachrichtigungen und physische Auslieferungen lassen sich möglicherweise nicht rückgängig machen.

Stelle in einer isolierten Umgebung wieder her, gleiche Geschäftssummen und externe Wirkungen ab und setze die Arbeit anschließend bewusst fort. Teste anhand des [Leistungstestplans](performance-testing.md) auch die Wiederherstellung bei gefüllter Queue und langsamen Abhängigkeiten. Eine Engine für dauerhafte Workflows ist gerechtfertigt, wenn sie nachgewiesene Orchestrierungskomplexität reduziert; bei einem einfacheren Prozess mit akzeptabler manueller Wiederherstellung kann eine transaktionale Job-Tabelle genügen. Beide benötigen weiterhin Backups, klare Verantwortung und Kompatibilitätstests.

## Verwandte Entscheidungen

[Daten und Migrationen](data.md) · [Zustand und Wiederherstellung](operations.md) · [Architekturentscheidungen](architecture.md) · [Teststrategie](testing-strategy.md)

## Primärbelege

[postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [durable-workflows](https://raw.githubusercontent.com/temporalio/temporal/e8ee627110a98501103827745aab18aedf312dd0/README.md) · [azure-retry](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/retry-content.md) · [azure-cqrs](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/cqrs.md) · [azure-outbox](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/databases/guide/transactional-out-box-cosmos.md) · [azure-idempotent-consumer](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/idempotent-consumer.md)
