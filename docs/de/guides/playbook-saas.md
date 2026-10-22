---
{
  "id": "playbook-saas",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Ein mandantenfähiges SaaS bereitstellen

## Eignung und Ausgangsarchitektur

Verwenden Sie dieses Profil, wenn unabhängige Kundenorganisationen eine Anwendung und ihre Infrastruktur gemeinsam nutzen. Erfassen Sie Mandantenisolation, Abrechnungssemantik, Datenresidenz, Wiederherstellungsziele, Form der Spitzenlast und die Verantwortung für den Kundensupport. Ein vorgeschlagener Ausgangspunkt ist eine modulare Anwendung, eine relationale Datenbank und ein begrenzter Hintergrund-Worker. Auch ein einzelnes Deployment kann getrennte Module für Mitgliedschaft, Geschäftsdatensätze, Abrechnung und Zustellung durchsetzen. Dieser von Agenten verfasste Leitfaden ist eine lokale Synthese, deren Übernahme durch Menschen noch aussteht.

Eine Datenbank auf einem einzelnen Host kann zu einem isolierten Prototyp mit akzeptierten Verfügbarkeitsgrenzen passen. Verwaltetes relationales Hosting ist eine Alternative, wenn Wiederherstellung, gleichzeitige Schreibvorgänge und betriebliche Unterstützung es erfordern. Getrennte Datenbanken je Mandant können Isolations- oder Residenzanforderungen erfüllen, erhöhen aber die Migrations- und Supportkosten. Messen Sie Abfragelatenz, Wartezeiten auf Sperren, Warteschlangenalter und Störungen durch andere Mandanten, bevor Sie Replikate, Partitionen oder Dienste hinzufügen. Extrahieren Sie ein Modul nur mit eigenständigem Vertrag, eigener Verantwortung und messbarem Nutzen; die Mandantenzahl ist kein Architekturschwellenwert.

## Invarianten im Repository verankern

Verwenden Sie Grenzen wie `domain/`, `api/`, `persistence/`, `billing/`, `workers/`, `contracts/` und `ops/`. Die authentifizierte Identität bestimmt die zulässige Mandantenmitgliedschaft; eine vom Client übermittelte Mandantenauswahl begründet niemals eine Berechtigung. Jeder Lesezugriff, jede Änderung, jeder Export, jede zwischengespeicherte Ansicht und jeder eingereihte Auftrag trägt einen verifizierten Mandantenkontext. Die Übernahme einer Benutzeridentität durch den Support muss ausdrücklich geregelt und protokolliert sein.

Legen Sie Datensatzidentität, mandantenbezogene Eindeutigkeit, Währung und Einheiten, Zustandsübergänge, Seitennavigation, Fehler und Aufbewahrung fest. Binden Sie bei einem wiederholten Befehl dessen Idempotenzschlüssel an Mandant, Operationsart und kanonischen Fingerabdruck der Anfrage. Die Wiederverwendung des Schlüssels mit anderen Eingaben muss einen Konflikt auslösen. Schreiben Sie Geschäftsänderung, gespeicherte Antwort und Outbox-Eintrag atomar fest, wenn sie dieselbe Datenbank nutzen. Der Weiterleitungsprozess kann zweimal zustellen; der Vertrag seines Konsumenten oder des Anbieters muss doppelte Geschäftseffekte verhindern. Eine lokale Transaktion kann eine entfernte Abbuchung nicht atomar machen.

## Agenten und Artefakte aufeinander abstimmen

1. Die Erkundungsrolle erstellt eine Matrix aus Identität, Aktion und Objekt, Geschäftsinvarianten, den vorgesehenen Lastbereich und Fälle unklarer Abrechnungsergebnisse. Die menschliche Verantwortung akzeptiert Entscheidungen zu Wiederherstellung und finanziellen Risiken.
2. Die implementierende Rolle liefert einen vollständigen vertikalen Ausschnitt: authentifizierter Befehl, mandantenbezogene Transaktion, dauerhaft gespeicherter Status und ein wiederholbarer Worker-Ablauf. Sie erfasst Speicher- und Mandantenalternativen in einem ADR und liefert eine kompatible Migration.
3. Die prüfende Rolle erprobt HTTP und Persistenz gemeinsam und hinterfragt anschließend Mandantengrenzen, Gleichzeitigkeit, Unterbrechung und Wiederherstellung. Die Release-Rolle bereitet eine begrenzte Einführung und einen Abgleichprozess vor; die Abnahme für Produktion unterliegt menschlicher Prüfung.

Das Paket enthält Profil, ADR, API-Schema, Berechtigungsmatrix, Migrationsreihenfolge, Beispiele für Operations- und Outbox-Protokolle, beobachtete Testergebnisse, Wiederherstellungsbericht, Anleitung zum Abgleich mit dem Anbieter, Kostenschätzung und benannte Dienst- und Datenverantwortliche. `examples/durable_service` ist eine lokale Referenz zum Untersuchen und Anpassen. Ihre Existenz belegt weder Authentifizierung, Anbieterabrechnung, Hochverfügbarkeit noch die Wiederherstellungsziele dieses Projekts.

## Geschäftsergebnisse einschließlich verbotener Ergebnisse testen

Verwenden Sie Unit-Tests für Geld- und Zustandsregeln, Vertragstests für Konsumenten und Integrationstests mit der tatsächlich gewählten Datenbank für Isolation und Atomarität. Ein SQLite-Ergebnis kann das Sperr- oder Isolationsverhalten von PostgreSQL nicht belegen. Tauschen Sie in zwei synthetischen Mandanten Identifikatoren bei Lesezugriffen, Schreibvorgängen, Exporten und Worker-Nutzdaten aus. Das Prüfkriterium sind das Ausbleiben unberechtigter Antwortdaten und unveränderte Zustände des fremden Mandanten, nicht bloß eine HTTP-Ablehnung.

Senden Sie gleichzeitig mehrere Kopien eines Befehls und verwenden Sie dessen Schlüssel mit einem anderen Betrag erneut. Untersuchen Sie Datensätze, gespeicherte Antworten und Effekte: Es bleibt genau eine beabsichtigte Geschäftsoperation, und eine abweichende Wiederverwendung schlägt fehl. Lösen Sie Abstürze vor dem Commit, nach dem Commit und nach einem Erfolg beim Anbieter, aber vor dessen Bestätigung aus. Der letzte Fall muss unter einer dokumentierten Anbietergarantie eine sichere Wiederholung oder einen sichtbaren Abgleichzustand ergeben, niemals eine blinde zweite Abbuchung. Stellen Sie eine isolierte Sicherung wieder her, vergleichen Sie Geschäftsinvarianten und gleichen Sie Anbieterdatensätze ab, bevor die Zustellung erneut beginnt. Halten Sie fehlgeschlagene und nicht ausgeführte Fälle fest.

Lasttests sollten teure Abfragen, ungleich belastete Mandanten, gleichzeitige Schreibvorgänge und eine begrenzte Aufarbeitung des Rückstaus nachbilden. Vereinbaren Sie vor dem Start Ziele für Latenz, Fehler und Warteschlangen sowie Abbruchgrenzen. Ergänzen Sie Browsertests für abgelehnte, ausstehende und unklare Ergebnisse, damit Nutzer nicht zur erneuten Übermittlung einer Zahlung mit unklarem Ausgang verleitet werden.

## Über die Datengrenze hinweg ausliefern und betreiben

Erweitern Sie zuerst das Schema, stellen Sie kompatible Leser und Schreiber bereit, ergänzen Sie Daten in fortsetzbaren Batches, gleichen Sie den Zustand ab und entfernen Sie die alte Darstellung erst nach dem Kompatibilitätsfenster. Brechen Sie bei vereinbarten Schwellen für Fehler, Sperrwartezeiten oder Abgleichabweichungen ab. Das Zurückrollen des Anwendungscodes stellt gelöschte Daten nicht wieder her und macht keine Abbuchung rückgängig. Bewahren Sie das vorherige Artefakt, Sicherungen, Migrationskontrollpunkte und einen Plan für eine Vorwärtskorrektur oder isolierte Wiederherstellung auf.

Überwachen Sie Berechtigungsablehnungen, Transaktionsfehler, Warteschlangenalter, Zustellversuche, Abrechnungsabweichungen und die Aktualität der Wiederherstellungsnachweise mit datenschutzgerechten Korrelations-IDs. Planen Sie Datenbankkapazität, Sicherungen, Anbietergebühren, Übertragung und Betriebsarbeit je nützlichem Geschäftsergebnis ein. Legen Sie für Incidents getrennt fest, wer Abrechnung und Worker anhalten darf. Zu den noch zu schließenden Produktionslücken gehören der Identitätslebenszyklus, Schlüsselverwaltung, Zahlungsverträge, Mandantenausstieg, Wiederherstellungsübungen und Rufbereitschaft. Bei der Stilllegung stoppen Sie neue Schreibvorgänge, klären ausstehende externe Effekte, exportieren autorisierte Kundendaten, beachten Aufbewahrungs- und Löschregeln und widerrufen Integrationen, ohne erforderliche Finanznachweise zu vernichten.

## Mit verwandten Entscheidungen fortfahren

[Daten und Migrationen](data.md) · [Dauerhaftigkeit](durability.md) · [Sicherheitstests](security-testing.md) · [Skalierung](scaling.md)

## Primärquellen

[owasp-multi-tenant](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.md) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [azure-outbox](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/databases/guide/transactional-out-box-cosmos.md) · [azure-idempotent-consumer](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/idempotent-consumer.md)
