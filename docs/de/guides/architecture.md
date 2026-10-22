---
{
  "id": "architecture",
  "language": "de",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Architekturen auswählen und verbinden

## Nach Anforderungen und Zuständigkeiten entscheiden

Dokumentiere Transaktionsgrenzen, Latenz- und Wiederherstellungsanforderungen, Datensensibilität, Lastprofil und die Personen, die das System betreiben können. Vergleiche den einfachsten tragfähigen Entwurf mit der vorgeschlagenen Alternative. Die folgende Tabelle ist der eigenständige Entscheidungsrahmen dieser Bibliothek; die zitierten Musterbeschreibungen belegen relevante Mechanismen und Abwägungen, keine universelle Rangfolge.

| Ansatz | Geeignete Ausgangsbedingung | Aufwand und Anlass zur Neubewertung |
| --- | --- | --- |
| Statische Website | Öffentliche Inhalte ohne vertrauenswürdige serverseitige Schreiboperationen | Build- und Cache-Grenzen; geschützte API für authentifizierte Änderungen ergänzen |
| Modularer Monolith | Ein Produkt benötigt koordinierte Transaktionen und häufige Änderungen | Disziplin bei Modulabhängigkeiten; nur bei nachgewiesener Begrenzung oder unabhängig verantworteter Fähigkeit auslagern |
| Funktionen | Begrenzte, schubweise Arbeit passt zum Ausführungsvertrag des Anbieters | Kaltstarts, Quoten, Verbindungsdruck und Wiederholungen; dauerhafte oder lang laufende Arbeit neu bewerten |
| Dienste | Unabhängige Verantwortung, Veröffentlichung oder Fehlerisolierung schafft einen konkreten Nutzen | Netzwerkausfälle, versionierte Verträge, Beobachtbarkeit und Konsistenzbetrieb |
| Ereignisgesteuerte Arbeit | Arbeit darf später abgeschlossen werden und Verbraucher haben unterschiedliche Aufgaben | Doppelte oder ungeordnete Zustellung, Verzögerung, Wiederverarbeitung und Schemaentwicklung |
| Dauerhafte Workflows | Lang laufende Geschäftsschritte müssen Unterbrechungen überstehen | Grenzen der Engine, Aufbewahrung der Historie, Code-Upgrades und Abgleich externer Wirkungen |

Diese Ansätze lassen sich kombinieren. Ein Monolith kann ein statisches Frontend bereitstellen und eine Queue nutzen, ohne zum Microservice-System zu werden. Abhängigkeitsrichtung im Code und Bereitstellungstopologie sind getrennte Entscheidungen: Eine Aufteilung in Prozesse schafft allein noch keine sinnvollen fachlichen Grenzen.

CQRS trennt Lese- und Schreibmodelle; der Einstieg ist innerhalb einer Datenbank möglich. Separate Speicher bringen Synchronisationsverzögerung und einen Vertrag für veraltete Lesedaten mit sich. Event Sourcing macht die Ereignishistorie zur maßgeblichen Wahrheit und verlangt Entscheidungen zu Ereignisversionen, Wiederverarbeitung sowie Datenschutz und Aufbewahrung. Eine Queue oder Audit-Tabelle allein ist kein Event Sourcing. Führe diese Muster gezielt ein, wenn ihr konkreter Nutzen die zusätzlichen Wiederherstellungs- und Testpflichten überwiegt.

## Grenzen prüfbar machen

Dokumentiere für jeden Browser, jede API, jeden Worker, Datenspeicher und jede Anbieteranbindung:

| Vertrag | Nachweis für das Review |
| --- | --- |
| Befugnis | Welcher Akteur welche Aktion mit wessen Daten ausführen darf |
| Datenverantwortung | Welche Komponente welche Invariante schreiben darf und wie andere Komponenten Änderungen anfordern |
| Fehler | Timeout, Abbruch, Verantwortung für Wiederholungen, Umgang mit Duplikaten und sichtbarer Warte- oder Fehlerzustand |
| Kompatibilität | Unterstützte Erzeuger und Verbraucher, Schemaversion und Bedingung für die Entfernung |
| Betrieb | Traces und Metriken, Supportverantwortlicher, Wiederherstellungs- und Abgleichverfahren sowie Budget |

Eine gemeinsame Datenbank kann eine bewusste Übergangslösung sein. Uneingeschränkte Schreibzugriffe mehrerer Dienste erschweren unabhängige Verantwortung und Migration; dokumentiere diese Kopplung, statt die Dienste als unabhängig zu bezeichnen.

## Änderungen vor der Auslagerung nachweisen

Benenne für einen vorgeschlagenen Worker oder Dienst zuerst das Symptom: Alter wartender Aufgaben, Sperrkonflikte, Bereitstellungskoordination oder eine Isolierungsanforderung. Erfasse eine repräsentative Ausgangsmessung und vergleiche einen kleinen durchgängigen Ausschnitt mit dem bestehenden Pfad. Nutze an der neuen Grenze [Vertrags- und Black-Box-Prüfungen](testing-strategy.md), [Last- und Wiederherstellungstests](performance-testing.md) sowie [Sicherheitstests](security-testing.md). Beziehe eine langsame Abhängigkeit, einen alten Verbraucher und eine wiederholte Anfrage ein.

Ein Migrationsplan benennt Datenverantwortung während des Übergangs, Verkehrszuordnung, Kompatibilität und Abgleich. Behalte einen maßgeblichen Schreiber bei, sofern kein bewusst entworfenes Konfliktlösungsverfahren getestet wurde. Definiere die Nachweise für die Verkehrsverlagerung, die Abbruchbedingung und den Wiederherstellungsweg nach neuen Schreibvorgängen. Das Zurückleiten von Verkehr macht migrierte Daten nicht automatisch rückgängig.

Wenn der Nutzen nicht belegt ist, behalte die einfachere Topologie und die nützliche interne Grenze bei. Dokumentiere das Ergebnis in einem ADR, damit der nächste Agent keinen unbegründeten Umbau wiederholt.

## Verwandte Entscheidungen

[Beständigkeit und verteilte Arbeit](durability.md) · [Frontendarchitektur](frontend.md) · [Anhand von Messungen skalieren](scaling.md) · [Hosting](hosting.md) · [Teststrategie](testing-strategy.md)

## Primärbelege

[azure-architecture-styles](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/guide/architecture-styles/index.md) · [azure-cqrs](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/cqrs.md) · [azure-event-sourcing](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/event-sourcing.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml) · [durable-workflows](https://raw.githubusercontent.com/temporalio/temporal/e8ee627110a98501103827745aab18aedf312dd0/README.md)
