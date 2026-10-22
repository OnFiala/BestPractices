---
{
  "id": "scaling",
  "language": "de",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Anhand von Messungen skalieren

## Arbeit beschreiben statt Konten zählen

Erfasse Spitzenankunftsrate, parallele Arbeit, Nutzdatengrößen, Lese-/Schreibmix, stark belastete Mandanten oder Schlüssel, Datenwachstum, Hintergrundjobs und Abhängigkeitsquoten. Definiere Nutzerablauf, Dienstziel, Kostenrahmen und benötigte Reserve bei Ausfällen, bevor du Kapazität auswählst. Eine Million meist inaktiver Konten kann leichter zu bedienen sein als wenige aufwendige gleichzeitige Jobs.

Die folgende Eskalationsfolge ist eine Empfehlung der Bibliothek, keine Zusicherung, dass jede Arbeitslast jeden Schritt benötigt. Halte Messungen und verworfene Alternativen in einem ADR fest.

## Jeweils eine Begrenzung ändern

| Beobachtete Begrenzung | Mögliche Änderung | Nachweis und Abwägung |
| --- | --- | --- |
| Langsame Abfragen oder zu viele Einzelaufrufe | Profilieren, indizieren, Ergebnismengen begrenzen und sorgfältig bündeln | Abfragepläne, Latenz und Schreibaufwand mit repräsentativen Daten vergleichen |
| Wiederholte aufwendige Lesevorgänge | Cache mit ausdrücklichen Mandantenschlüsseln und Aktualitätsregeln | Kaltstart, Invalidierung und gleichzeitige Cache-Fehltreffer testen; Last des Ursprungssystems messen |
| Arbeit trifft schneller ein, als sie abgeschlossen wird | Begrenzte Queues und Worker, Quoten und Zulassungssteuerung | Queue-Alter, faire Verteilung und Wiederherstellung prüfen; vor Erschöpfung vorhersehbar ablehnen |
| Anwendungs-CPU oder unabhängige Ein-/Ausgabe ist ausgelastet | Zustandslose Replikate hinzufügen | Gesamte Datenbankverbindungen und nachgelagerte Anfragerate neu berechnen |
| Leseverkehr dominiert | Replik oder Abfrageprojektion | Verzögerung und Verhalten beim Lesen nach einem Schreibvorgang definieren; veraltete und nicht verfügbare Lesezugriffe testen |
| Gemessene Speicher-, Schreib- oder Routinggrenze bleibt bestehen | Arbeitslast partitionieren oder isolieren | Routing, stark belastete Schlüssel, Umverteilung, Migration und partitionsübergreifende Semantik nachweisen |

Nimm nicht an, dass ein Cache sichere Autorisierung schafft: Begrenze Schlüssel auf den richtigen Kontext und invalidiere Berechtigungen angemessen. Viele gleichzeitige Fehltreffer können das Ursprungssystem überlasten. Zusätzliche Anwendungsreplikate können einen Datenbankausfall verschärfen, wenn jedes Replikat einen großen Pool öffnet oder dieselbe Arbeit wiederholt.

## Das Experiment vor der Lasterzeugung festlegen

Unterscheide mit dem [Leitfaden für Leistungstests](performance-testing.md) Grundlast-, Spitzenlast-, Stress-, Dauer- und Wiederherstellungsexperimente. Definiere Zielumgebung, Autorisierung, synthetischen Datenbestand, Verkehrsverteilung, Abbruchbedingungen und Kostenlimit. Teste neben dem häufigsten Pfad auch abgewiesene und aufwendige Operationen. Bewahre Ergebnisse einzelner Anfragen, Ressourcenmetriken, Queue-Alter und eine versionierte Lastbeschreibung auf.

Miss erfolgreichen Durchsatz, p95-/p99-Latenz, Fehler und abgewiesene Arbeit getrennt. Ein System, das hervorragende Latenz nur durch das Verwerfen der meisten Anfragen erreicht, erfüllt sein Ziel nicht. Beziehe eine langsame Abhängigkeit ein und beobachte, ob sie die gesamte Parallelität verbraucht oder Wiederholungen verstärkt. Prüfe nach der Lastreduktion, dass sich Queues leeren und Dienstziele ohne manuellen Neustart wieder erreicht werden.

Als grobe Kontrolle gilt in einem stabilen System: Die durchschnittlich gleichzeitig laufende Arbeit entspricht der durchschnittlichen Ankunftsrate multipliziert mit der durchschnittlichen Verweildauer innerhalb derselben Messgrenze. Dies schätzt keine hohe Latenzperzentile und verspricht keine Kapazität; eine unter Überlast wachsende Queue verletzt die Gleichgewichtsannahme. Prüfe jede Schätzung anhand der tatsächlichen Verteilung und des Fehlerverhaltens.

## Entscheiden und zurückkehren

Skaliere, wenn anhaltende Messungen oder eine begründete Prognose das vereinbarte Ziel oder die Ausfallreserve gefährden. Dokumentiere Auslöser, erwarteten Nutzen, Betriebskosten, Änderungsverantwortlichen und einen Plan für Rücknahme oder Vorwärtskorrektur. Autoscaling benötigt Obergrenzen, Startzeit, Abhängigkeitskapazität und Budgetkontrollen. Es repariert keine ineffiziente Transaktion und garantiert keine Verfügbarkeit.

Regionsübergreifendes Schreiben und Sharding bringen zusätzliche Routing- und Konsistenzentscheidungen mit sich. Führe sie erst nach Tests von Failover, Konflikt- oder Abgleichverhalten und Migration mit repräsentativen Daten ein. Die unten zitierte anbieterspezifische Partitionierungsquelle veranschaulicht diese Pflichten; ihre Produktgrenzen sind keine universellen Grenzen für andere Datenbanken.

## Verwandte Entscheidungen

[Leistungstests](performance-testing.md) · [Hosting](hosting.md) · [Daten](data.md) · [Betrieb](operations.md) · [Architektur](architecture.md)

## Primärbelege

[observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md) · [azure-cache-aside](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/cache-aside-content.md) · [azure-data-partitioning](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/best-practices/data-partitioning-strategies-content.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml)
