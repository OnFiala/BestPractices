---
{
  "id": "examples",
  "language": "de",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Referenzpfade für Projekte

## Sechs Entwurfsprofile, keine bereitgestellten Anwendungen

Diese eigenständig entwickelten Profile verbinden Architekturentscheidungen mit einem ersten beobachtbaren Nachweis. Sie sind anschauliche Ausgangspunkte, keine durch Benchmarks bestätigten Stacks, Konformitätszertifizierungen oder abgeschlossenen Testergebnisse. Die [maschinenlesbaren Entwurfsprofile](https://github.com/OnFiala/BestPractices/blob/main/data/blueprints.json) enthalten Grenzen, Wiederherstellung, Änderungssignale und geplante Testpakete. Fixiere bei ihrer Übernahme die Repository-Revision.

| Projekt | Ausgangsentwurf | Erster Nachweis | Neu bewerten, wenn |
| --- | --- | --- | --- |
| Öffentliche Website | Statischer Build/CDN und Inhaltshistorie | Barrierefreie Navigation, keine privaten Ausgaben, Wiederherstellung eines früheren Artefakts | Vertrauenswürdige Schreiboperationen oder gemessene Veröffentlichungsgrenzen hinzukommen |
| SaaS | Modulare Anwendung, transaktionale Datenbank und begrenzter Worker | Mandantentrennung, Zahlungsabgleich und Wiederherstellung | Gemessene Konkurrenz um Ressourcen oder unabhängige fachliche Verantwortung entstehen |
| Internes Werkzeug | SSO, kleine Anwendung, eingeschränkte Integrationen und Audit | Nutzer mit widerrufenem Zugriff können weder lesen noch exportieren; verzögerte Arbeit ist zugeordnet | Verantwortliche oder Zuverlässigkeitspflichten auseinanderlaufen |
| KI-Anwendung | Modelladapter, autorisiertes Retrieval und Evaluationssatz | Nicht erlaubte Dokumente gelangen nicht in den Modellkontext; Fehler bleiben begrenzt | Evaluierte Qualität, Kosten, Latenz oder Datenstandort sich ändern |
| Agentenautomatisierung | Dauerhaftes Ausführungsregister, begrenzte Worker und eingeschränkte Werkzeuge | Duplikate, veraltete Freigaben und Budgetstopps können keine Befugnisse überschreiten | Unabhängige Werkzeuge oder Arbeitslasten getrennte Ausfallgrenzen benötigen |
| Mobilanwendung/Backend | Client-Cache, kompatible API und ausdrückliche Synchronisationsregeln | Offline-Wiederherstellung, Konflikte und Unterstützung alter Clients | Gemessener Synchronisationsdruck oder Geografie einen Umbau rechtfertigen |

## Öffentliche Website

Angenommen werden öffentliche, selbst verfasste Inhalte ohne nutzerspezifische serverseitige Schreiboperationen. Erzeuge ein unveränderliches Artefakt und veröffentliche es über eine geprüfte Bereitstellungsidentität. Navigiere und suche vor der Veröffentlichung in jeder unterstützten Sprache mit Tastatur und schmalem Ansichtsfenster. Prüfe erzeugte Ausgabe und Suchindex auf private Daten; eine clientseitige Anmeldung kann öffentliche Dateien nicht schützen. Stelle ein bekanntes früheres Artefakt in einer Testumgebung bereit und prüfe eine echte Route. Ergänze eine geschützte API erst, wenn das Produkt vertrauenswürdige Schreiboperationen benötigt; mache einen statischen Build-Token nicht zu öffentlichen Browserzugangsdaten.

## SaaS mit Zahlungen

Angenommen werden mehrere Mandanten und ein für Belastungen verantwortlicher Anbieter. Binde jede Operation an den authentifizierten Mandanten und speichere lokale Geschäftsübergänge mit einer stabilen Operationskennung. Prüfe vor Änderungen an Autorisierung oder Abrechnung mandantenübergreifende Objekt- und Exportversuche, doppelte Übermittlungen und eine verlorene Anbieterantwort. Untersuche lokale und anbieterseitige Aufzeichnungen statt allein dem HTTP-Status zu vertrauen, um genau ein beabsichtigtes Geschäftsergebnis oder einen ausdrücklich ungeklärten Abgleichzustand nachzuweisen. Stelle eine isolierte Kopie wieder her, gleiche Zahlungen ab und setze ausstehende Arbeit bewusst fort. Führe Dienste nur für einen gemessenen Nutzen bei Verantwortung, Isolation oder Kapazität ein.

## Internes Werkzeug

Angenommen werden ein organisatorischer Identitätsanbieter und eine vorgeschaltete Geschäftsintegration. SSO stellt die Identität fest; die Anwendung autorisiert weiterhin jede Aktion und jeden Export. Teste den Zugriffsentzug innerhalb des vereinbarten Widerrufsfensters sowohl mit einer bestehenden Sitzung als auch mit einem wartenden Job. Mache eine vorgelagerte Abhängigkeit unerreichbar und prüfe anschließend, dass ausstehende Arbeit sichtbar ist und nur im Rahmen ihrer Richtlinie wiederholt wird. Der Abgleich verwendet eine stabile Operations-ID, damit ein Betreiber feststellen kann, ob dort ein Schreibvorgang stattgefunden hat. Ordne Audit-Aufzeichnungen einem Verantwortlichen und einer Aufbewahrungsregel zu; Zugang zum Firmennetz allein ist keine Autorisierung.

## KI-Anwendung

Angenommen wird eine begrenzte Modellfunktion, die Dokumente für einen authentifizierten Nutzer abruft. Autorisiere Dokumente, bevor ihr Inhalt in Retrieval-Ergebnisse oder Modellkontext gelangt, und setze Widerruf und Löschung auch in Indizes und Caches um. Führe vor Änderungen an Modell, Prompt, Retrieval-Pfad oder Richtlinie Evaluationen mit zurückgehaltenen repräsentativen und adversarialen Fällen durch. Definiere die Bewertung ausdrücklich und nutze menschliches Review, wo Urteilsvermögen nötig ist. Beziehe nicht erlaubte Dokumente, Antwortverzicht, Prompt Injection und Anbieter-Timeouts ein. Miss Erfolg und Quellenbezug neben Latenz und Kosten; plausible Sprache ist keine Korrektheit. Ein sicherer Ersatzpfad kann die Funktion deaktivieren oder eine gewöhnliche autorisierte Suche anbieten.

## Agentenautomatisierung

Angenommen wird, dass wartende Aufgaben folgenreiche Schreibaktionen von Werkzeugen auslösen können. Das Ausführungsregister dokumentiert Aufgabenidentität, autorisierten Umfang, Freigabebindung, Versuche und beobachtbares Ergebnis. Teste eine doppelte Aufgabe, eine abgelaufene Freigabe, eine nach der Freigabe geänderte Aktion, feindliche abgerufene Anweisungen und ein ausgeschöpftes Budget. Die Durchsetzungsgrenze muss unautorisierte Werkzeugaufrufe unabhängig von der Kooperation des Modells stoppen. Nutze für Fehlertests simulierte oder isolierte externe Ziele. Kläre nach einem Absturz vor der Fortsetzung, ob die Wirkung eingetreten ist; ein Worker-Neustart darf keine irreversible Aktion blind wiederholen.

## Mobilanwendung und Backend

Angenommen wird, dass nicht alle Clients sofort aktualisiert werden können und Änderungen offline möglich sind. Autorisierung und maßgeblicher Zustand bleiben auf dem Server, notwendige lokale Daten in einem zur Plattform passenden geschützten Speicher; eine ausdrückliche Regel bestimmt die Konfliktbehandlung. Teste vor der Veröffentlichung den ältesten unterstützten Client gegen die neue API, unterbrochene Synchronisation, wiederholten Upload und konkurrierende Offline-Änderungen. Prüfe, dass der Gerätewiderruf gemäß dokumentiertem Sitzungsvertrag eine Erneuerung und nachfolgende geschützte Operationen blockiert. Nimm nicht an, dass der Widerruf bereits heruntergeladene Daten auf dem Gerät löscht. Regionale oder partitionierte Synchronisation benötigt Belege für Konfliktrate, Latenz und Wiederherstellungskosten.

## Einem Agenten eine testbare Aufgabe geben

Vereinbare für das ausgewählte Profil Arbeitslast, SLO/RTO/RPO, Datenregeln und Budget mit dem menschlichen Verantwortlichen. Übersetze die geplanten Fälle mithilfe der [Teststrategie](../guides/testing-strategy.md), des [Leistungstestplans](../guides/performance-testing.md) und des [Sicherheitstestplans](../guides/security-testing.md) in Tests des tatsächlichen Stacks. Dokumentiere Aufbau, Reiz, beobachtbares Testorakel, Negativfälle, Abbruchbedingungen und aufbewahrte Nachweise. Ein Agent muss einen vorgeschlagenen Test von einem ausgeführten Ergebnis unterscheiden und fehlende Voraussetzungen melden, statt einen Erfolg zu erfinden.

## Verwandte Entscheidungen

[Einführung](../guides/adoption.md) · [Architektur](../guides/architecture.md) · [Agenten](../guides/agents.md) · [Frontend](../guides/frontend.md) · [Teststrategie](../guides/testing-strategy.md)

## Primärbelege

[owasp](https://raw.githubusercontent.com/OWASP/ASVS/2b47a9dd16760ee484a6672d197f1f7e25d9c632/README.md) · [openai-agents](https://raw.githubusercontent.com/openai/openai-agents-python/841dfdd938bfd4ca052475eb76d6245a356868e0/docs/agents.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [wcag](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/index.html) · [azure-architecture-styles](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/guide/architecture-styles/index.md) · [azure-retry](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/retry-content.md) · [azure-idempotent-consumer](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/idempotent-consumer.md)
