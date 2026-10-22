---
{
  "id": "reference-labs",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Referenzprojekte ausführen und auswerten

## Drei ausführbare Grenzen

Die Referenzprojekte sind eigenständige Lehrimplementierungen mit lokalen Testvorrichtungen unter eigener Kontrolle. Sie ermöglichen Agenten, konkrete Verträge zu untersuchen, Fehler bewusst auszulösen und gemessene Ergebnisse ohne Anbieterkonto oder kostenpflichtigen Modellaufruf aufzubewahren. Es sind Komponenten, die von den sechs Projektleitfäden ausgewählt werden, keine sechs fertigen Produkte oder Deployment-Vorlagen für Produktion.

| Referenz | Tatsächliche Implementierung | Bewusster Ersatz und Grenze |
| --- | --- | --- |
| `examples/durable_service` | Loopback-HTTP, mandantengebundene Testidentität, SQLite-Transaktionen, Idempotenz- und Versionsregeln, Outbox und Konsument, Absturzübungen mit Kindprozessen, Snapshot-Wiederherstellung und begrenzte Überlast | Synthetische Bearer-Zugangsdaten; lokales SQLite und ein Rechner; keine echte Zahlung, kein Identitätsanbieter, Broker oder regionales Failover |
| `examples/agent_workflow` | Dauerhaft gespeicherter Workflow und getrenntes Effektprotokoll, Autorisierung vor Kontextaufnahme, Befugnisprüfungen für genaue Aktionen, Abbruch, Budgets und Abgleich | Deterministisches Testmodell, vertrauenswürdiger Freigabeaussteller der Testvorrichtung, simulierter Absturz mit erneutem Öffnen und synthetische Budgeteinheiten; keine echte Modellqualität oder produktive Authentifizierung |
| `examples/frontend` | Semantisches HTML und native Module, URL-, lokaler und entfernter Zustand, Abbruch anhand der Anfrageidentität, sichere Textausgabe und tatsächliche Chromium-Prüfungen | Schreibgeschützte synthetische API, ein beobachteter Browser und eine Umgebung sowie teilweise Barrierefreiheitsprüfungen; keine produktive Authentifizierung, Schreibvorgänge oder nativen mobilen Clients |

Jede README benennt Voraussetzungen, Befehle, Annahmen, negative Prüfkriterien, Aufräumarbeiten und ausgelassene Produktionsarbeit. Verwenden Sie diese Verträge beim Anpassen eines Beispiels; das Kopieren von Code übernimmt dessen Annahmen nicht automatisch.

## Ausführen und Beobachtungen aufbewahren

Vom Repository-Stammverzeichnis aus:

```sh
python -m examples.durable_service demo
python -m examples.durable_service drills
python -m examples.durable_service benchmark --operations 120 --concurrency 8 --capacity 2 --delay-ms 10 --seconds 5
python -m examples.agent_workflow demo
python -m examples.agent_workflow evaluate
python -m library.verification delivery durable-service agent-workflow frontend-unit frontend-browser --output reports/reference-checks.json
```

Der Benchmark startet ausschließlich seine eigene Loopback-Testvorrichtung, akzeptiert begrenzte lokale Parameter und keine entfernte Ziel-URL. Die obigen Zahlen definieren ein kleines Lehrexperiment; sie sind keine empfohlenen Produktionsgrenzen oder Dienstziele. Untersuchen Sie die Anzahl angebotener, gestarteter, abgeschlossener, abgelehnter und mit Transportfehlern beendeter Vorgänge zusammen mit gemessener Latenz, Testdauer und anschließender Integrität und Wiederherstellung. Generatorverhalten und geschlossenes Lastmodell begrenzen die Interpretation.

Die Agentenevaluation meldet deterministische Richtlinienfälle getrennt von ihrem ausdrücklich nicht ausgeführten Punkt zur Qualität eines Live-Modells. Bestandene ausgeführte Fälle sind nützliche Nachweise für diese lokalen Regeln, kein Grund, den übersprungenen Punkt als erfolgreich zu zählen. Modell und Freigabeaussteller der Demo sind klar als Testvorrichtungen benannt.

Der Prüfer verlangt tatsächlich ausgeführte Tests, erfasst Laufzeitversionen und den Eingabedateistand und behandelt fehlende, fehlgeschlagene oder übersprungene Pflichtprüfungen als unvollständig. Seine Browsersuite benötigt Node 22+ und ein installiertes Chromium/Chrome. Eine ausdrückliche Sandbox-Option für einen kontrollierten Container ist in der Frontend-README dokumentiert; sie gilt ausschließlich für die lokale Testvorrichtung unter eigener Kontrolle. Berichte sind lokale Beobachtungen, keine authentifizierten Bescheinigungen oder menschlichen Genehmigungen.

## Fehler- und Wiederherstellungsgrenzen prüfen

Vergleichen Sie bei dauerhaften Schreibvorgängen zulässige Ergebnisse und verweigerte Nebeneffekte. Wiederholte Anfragen mit demselben Mandanten, derselben Aktion, demselben Schlüssel und denselben Nutzdaten sollten ein Ergebnis erneut ausgeben; abweichende Nutzdaten müssen scheitern. Gleichzeitige versionierte Schreiber benötigen ein definiertes Gewinner- und Konfliktergebnis. Outbox-Eintrag und geschäftlicher Schreibvorgang teilen eine lokale Transaktion; Konsumenten dürfen unbekannte Ereignisschemata nicht bestätigen. Die Wiederherstellung eines Snapshots verliert spätere lokale Schreibvorgänge und macht externe Effekte nicht rückgängig.

Untersuchen Sie bei Agentenaktionen, was den Kontext erreicht, bevor ein Vorschlag existiert, und anschließend, was die Ausführung unabhängig validiert. Eine bearbeitete Aktion oder abgelaufene beziehungsweise widerrufene Befugnis darf nicht ausgeführt werden. Prüfen Sie nach einem unklaren Effekt die unabhängige Empfangsbestätigung und gleichen Sie ab; eine fehlende oder unpassende Bestätigung muss ungeklärt bleiben, statt eine blinde Wiederholung auszulösen. Auch bei einem abgebrochenen Lauf oder einem Lauf mit Zeitüberschreitung muss bereits geleistete Arbeit weiterhin erfasst und berücksichtigt werden.

Testen Sie im Browser echte öffentliche Bedienelemente und Wettläufe im Transport. Ein abgebrochener Transport kann trotzdem noch einen Antwortkörper liefern; die Anfrageidentität muss verhindern, dass ein veralteter Abschluss den aktuellen Zustand ersetzt. Verweigerte oder fehlerhaft geformte Daten dürfen nicht zu aktivem Markup werden. Tastatur-, Fokus- und Prüfungen schmaler Ansichten decken bestimmte Abläufe ab, nicht alle assistiven Technologien oder Geräte.

## Von einer Referenz zum Produkt gelangen

Generieren Sie ein Auslieferungspaket, geben Sie wiederverwendete Teile an und ersetzen Sie jede Grenze der Testvorrichtung durch einen geprüften Projektvertrag. Ergänzen Sie die gewählten Speicher-, Anbieter-, Identitäts- und Client-Integrationen samt Tests. Führen Sie Negativ- und Wiederherstellungsfälle erneut gegen diese tatsächlichen Grenzen aus, messen Sie repräsentative Lasten und lassen Sie Deployment und betriebliche Verantwortung unabhängig prüfen. Bewahren Sie fehlgeschlagene und nicht ausgeführte Beobachtungen auf. Das Produktionsrelease ist eine gesonderte menschliche Entscheidung, nachdem Projektnachweise vorliegen.

## Verwandte Entscheidungen

[Agentengestützter Auslieferungsablauf](project-delivery.md) · [Abdeckung und Grenzen](coverage.md) · [Dauerhaftigkeit](durability.md) · [Sicherheitstests](security-testing.md) · [Leistungstests](performance-testing.md)

## Primärquellen

[azure-idempotent-consumer](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/idempotent-consumer.md) · [azure-outbox](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/databases/guide/transactional-out-box-cosmos.md) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [playwright-testing](https://raw.githubusercontent.com/microsoft/playwright/ca7ca36145b84183cf423c2a099bd7e9cd8b1cb3/docs/src/best-practices-js.md) · [k6-open-vs-closed](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/using-k6/scenarios/concepts/open-vs-closed.md)
