---
{
  "id": "testing-strategy",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Eine Teststrategie auswählen

## Tests auf drei unabhängigen Achsen beschreiben

Ein Agent sollte angeben, was er über das System weiß, welche Grenze er prüft und welchen Fehler er sucht. Das sind unterschiedliche Entscheidungen. Ein Black-Box-Test kann gewöhnliche Funktionalität, Leistung oder Sicherheit prüfen; der Begriff bedeutet nicht Penetrationstest.

| Achse | Möglichkeiten | Aussage für das Review |
| --- | --- | --- |
| Verfügbares Wissen | Black Box: beobachtbare Schnittstellen; Gray Box: ausgewählte Interna oder Instrumentierung; White Box: Code und interne Pfade | Welche Informationen den Testentwurf beeinflusst haben und welche blinden Flecken bleiben |
| Geprüfte Grenze | Unit-, Integrations-, Verbraucher-/Anbieter-Vertrags- oder Ende-zu-Ende-Test | Wie viel vom tatsächlichen System beteiligt ist und wo sich Fehler eingrenzen lassen |
| Ziel | Funktionale Korrektheit, Sicherheit, Leistung, Wiederherstellung, Barrierefreiheit, Kompatibilität | Welches Risiko das Ergebnis abdeckt; Erfolg bei einem Ziel beweist kein anderes |

Beispielsweise kann ein Black-Box-API-Test prüfen, dass zwei identische Kaufanfragen genau ein fachliches Ergebnis erzeugen. Ein White-Box-Unit-Test kann jeden Wiederholungszweig untersuchen. Ein Gray-Box-Integrationstest kann zusätzlich Transaktion und Outbox prüfen. Diese Nachweise ergänzen einander. Dokumentiere die lokale Terminologie, wenn „Integration“ oder „Vertrag“ im Team anders definiert werden.

## Aus Änderung und Folgen auswählen

Die folgende Matrix ist die empfohlene Ausgangsrichtlinie dieser Bibliothek und keine überall verpflichtende Testsuite. Ergänze oder entferne Prüfungen mit einer nachvollziehbaren Risikobegründung.

| Änderung oder Risiko | Nützliche erste Prüfungen | Weitergehende Prüfung und Abnahmenachweis |
| --- | --- | --- |
| Dokumentation oder Übersetzung | Bedeutung, Begriffe, Links, Sprachparität | Geänderte Darstellung bei Layout- oder Navigationsänderungen rendern; keine neue Laufzeitsuite für harmlose Formulierungskorrekturen |
| Fachliche Berechnung oder Zustandsübergang | Unit-Beispiele, Grenzen, ungültige Eingaben; eigenschaftsbasierte Fälle für echte Invarianten | Zeigen, dass eine verletzende Eingabe scheitert; Integrationstest, falls Persistenz oder externer Zustand zur Korrektheit gehören |
| Datenbankschema oder Transaktion | Integration mit echter Datenbank, Constraints, Parallelität, Migrationskompatibilität | Repräsentative Datenmenge, Sperren, Neustart/Fortsetzung und Wiederherstellung; bisher unterstützte Verbraucher bleiben kompatibel |
| API- oder Ereignisschema | Erzeuger-/Verbraucherverträge und Kompatibilität | Echte Serialisierung und Übertragung; ungültige Eingaben ohne unerwünschte Effekte abweisen |
| Nutzerablauf oder Frontendzustand | Komponententests und wenige Browserabläufe über öffentliche Semantik | Lade-, Leer-, Fehler-, Abbruch-, Tastatur- und schmale Ansichten; echte Browserereignisse prüfen |
| Authentifizierung, Rechte, Mandantengrenzen | Richtlinienprüfungen plus unberechtigte API-/Objektzugriffe mit verschiedenen Identitäten | Ungeprüfte Eintrittspunkte untersuchen und gezielte Sicherheitstests durchführen; Ablehnung legt keine geschützten Daten offen und hat keine unerlaubte Wirkung |
| Worker, Zahlung oder dauerhafter Workflow | Integrationsfälle für Duplikate, Reihenfolgeänderung, Timeout und Absturzgrenzen | Beabsichtigte Effekte nach Wiederholung/Neustart abgleichen; nötigenfalls Anbieter-Sandbox prüfen |
| Parallelität, Caching, Planung, Kapazität | Funktionale Prüfungen unter Parallelität und eine gemessene Basis | Last-, Stress-, Spitzenlast- oder Dauertest nach Leistungsleitfaden wählen; Korrektheit und begrenzte Wiederherstellung erhalten |
| Modell, Prompt, Retrieval, Werkzeug oder Agentenrichtlinie | Versionierte Aufgabenbewertungen, Angriffsfälle, deterministische Richtlinienprüfungen | Mit zurückgehaltenen Fällen vergleichen, tatsächliche Werkzeugwirkungen prüfen, stochastische Fälle wiederholen und Streuung berichten |

## Erst planen, dann Werkzeuge wählen

Schreibe ein kurzes Testpaket: betroffene Anforderung, Fehlerhypothese, Wissensmodell, Grenze und Ziel, Testdaten und Umgebung, erwartete Ergebnisse, sichere Ausführungsgrenzen und aufzubewahrende Belege. Daraus folgt das Werkzeug. Browsertreiber, HTTP-Client, Eigenschaftsgenerator, Lastgenerator, Scanner und menschliches Review beobachten jeweils andere Dinge.

Nutze die kleinste Grenze, an der der Fehler sichtbar wird. Ergänze eine realistische Schnittstellenprüfung, wenn Ersatzimplementierungen den Fehler verbergen könnten. Eine Datenbankattrappe kann keinen echten Eindeutigkeits-Constraint beweisen, ein simuliertes Browserereignis keine native Browserunterstützung. Kontrolliere externe Anbieter in deterministischen Tests. Kennzeichne Sandbox-Kompatibilität getrennt von einer simulierten Antwort.

Halte Testdaten unabhängig und reproduzierbar. Kontrolliere relevante Uhren und Zufallsquellen, dokumentiere Startwerte und trenne Konten, Mandanten, Zustand und Bereinigung. Teile kein veränderliches Testkonto zwischen parallelen Läufen, sofern nicht gerade diese Parallelität untersucht wird. Schütze Testdaten und Traces wie andere Daten. Kopiere keine Produktionsdatensätze bloß für realistischere Tests.

## Widerlegbare Prüfungen formulieren

Prüfe relevante Ausgaben, gespeicherten Zustand und verbotene Effekte. Ein erfolgreicher HTTP-Status beweist nicht, dass das richtige Objekt zurückgegeben wurde. Ein Autorisierungstest sollte eine erlaubte und eine abgewiesene Aktion ausführen und anschließend prüfen, dass die Ablehnung den geschützten Zustand nicht verändert hat.

Zeige bei einer folgenreichen Korrektur, dass der Test den ursprünglichen Fehler oder eine absichtlich beschädigte lokale Variante erkennt. Nutze gegebenenfalls Grenzwerte und Äquivalenzklassen. Eigenschaftsbasierte Tests untersuchen eine definierte Invariante; ihre Aussage hängt weiterhin von dieser Invariante und dem Eingabemodell ab. Abdeckung kann nicht besuchte Codepfade zeigen, aber hohe Abdeckung beweist weder richtige Anforderungen noch vollständige Sicherheitsgrenzen.

## Entscheiden, wann die Nachweise reichen

Stoppe die betroffene Veröffentlichung, wenn Pflichtchecks fehlschlagen, das Ziel außerhalb des genehmigten Umfangs liegt, Testdaten ihre Grenze verlassen oder eine folgenreiche Behauptung unbelegt bleibt. Berichte Lücken und Unsicherheit. Ein Mensch kann ein dokumentiertes, befristetes Restrisiko annehmen; ein Agent darf eine nicht ausgeführte Prüfung nicht als bestanden bezeichnen.

Fertig bedeutet, dass nachvollziehbare Ergebnisse, bekannte Grenzen und ein Wiederherstellungsplan das vereinbarte Verhalten stützen. Bewahre getestete Revision, Konfiguration, Testdatenversion, Befehle, Ergebnisse und relevante Traces auf; entferne sensible Werte. Ergänze weitere Tests, wenn eine neue Fehlerhypothese dies rechtfertigt, statt dieselbe grüne Suite endlos zu wiederholen.

## Belege und verwandte Entscheidungen

Drei-Achsen-Modell und Auswahlmatrix sind eigenständige lokale Zusammenführungen. OWASP behandelt Autorisierungsprüfungen auf mehreren Ebenen; Playwright stützt isolierte Tests sichtbaren Browserverhaltens; PostgreSQL beschreibt Parallelitätseigenschaften, die echte Datenbankprüfungen untersuchen müssen. Diese Quellen zertifizieren nicht jede Zelle der Matrix.

[Qualitätsprüfungen](quality.md) · [Leistungs- und Stresstests](performance-testing.md) · [Sicherheitstests](security-testing.md) · [Daten und Migrationen](data.md) · [Beständigkeit](durability.md)

## Primärbelege

[owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [playwright-testing](https://raw.githubusercontent.com/microsoft/playwright/ca7ca36145b84183cf423c2a099bd7e9cd8b1cb3/docs/src/best-practices-js.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml) · [owasp-multi-tenant](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.md)
