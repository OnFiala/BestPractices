---
{
  "id": "playbook-agent-automation",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Begrenzte Agentenautomatisierung bereitstellen

## Eignung und minimale Steuerungsebene

Verwenden Sie dieses Profil, wenn ein Modell Aktionen mit dauerhaften Folgen vorschlägt oder koordiniert: Datensätze ändern, Releases vorbereiten oder externe Werkzeuge bedienen. Erfassen Sie zulässige Ziele, Aufgabenverantwortung, maximalen Umfang, Freigabeanforderungen, Wiederholungsrichtlinie und Zeit-, Token- sowie Kostenlimits. Ein deterministischer Workflow ist vorzuziehen, wenn die Entscheidungsfolge bereits bekannt ist. Beginnen Sie mit einem begrenzten Worker und einem dauerhaften Ausführungsprotokoll; ergänzen Sie Modellschlussfolgerungen nur dort, wo sie ein gemessenes Aufgabenergebnis verbessern. Dieser von Agenten verfasste Leitfaden ist eine vorgeschlagene lokale Synthese.

Beginnen Sie nicht mit einer Agentenflotte. Trennen Sie Worker, Warteschlangen oder Identitäten, wenn Messungen eine dauerhafte Verdrängung nach Priorität, unvereinbare Werkzeugberechtigungen oder unabhängig verantwortete Zuverlässigkeitsverpflichtungen zeigen. Delegation bringt zusätzliche Koordinations-, Zugangsdaten- und Gesamtbudgetkosten mit sich. Eine Teilaufgabe erbt einen engeren Befugnisrahmen und ein kleineres Budget, niemals neue Rechte allein deshalb, weil ein anderer Agent sie angefordert hat.

## Repository, Verträge und dauerhafter Zustand

Trennen Sie `planner/`, `policy/`, `tool_gateway/`, `ledger/`, `reconciliation/` und `evaluation/`. Der Planer schlägt typisierte Aktionen vor. Die Richtlinienkomponente prüft unabhängig Akteur, Aufgabe, Werkzeug, genaues Ziel, Parameter und Umfang. Das Werkzeug-Gateway verwaltet die Zugangsdaten und setzt die endgültige Entscheidung durch. Werkzeugausgaben und abgerufener Text sind nicht vertrauenswürdige Beobachtungen; sie dürfen weder Richtlinien bearbeiten noch Freigaben erneuern oder ein unberechtigtes Ziel auswählen.

Speichern Sie Aufgabenidentität, Aktionsfingerabdruck, Freigabeidentität und -ablauf, Versuche, Budgetreservierungen, Ergebnisreferenzen und Zustandsübergänge dauerhaft. Unterscheiden Sie geplante, auf Freigabe wartende, autorisierte, laufende, erfolgreiche, fehlgeschlagene, abgebrochene und unklare Effekte. Binden Sie bei freigabepflichtiger Arbeit die Freigabe an Akteur und genaue Aktion; verbrauchen oder reservieren Sie sie atomar, damit parallele Worker sie nicht zweimal verwenden können. Parameteränderungen erfordern eine neue Entscheidung. Ein Freigabeflag im Modelltext ist kein vertrauenswürdiger Datensatz.

Ein Absturz nach einem externen Effekt, aber vor dessen Bestätigung erzeugt Ungewissheit. Verwenden Sie, sofern unterstützt, einen Idempotenzschlüssel des Anbieters oder eine Anbieterabfrage anhand einer stabilen Operationsidentität. Andernfalls stoppen Sie und gleichen den Zustand mit einer autorisierten Betriebsperson ab; deklarieren Sie Ungewissheit nicht als Fehler, um blind zu wiederholen. Ein dauerhaftes Protokoll verleiht einer beliebigen externen Aktion keine Exactly-once-Garantie.

## Implementierung und Prüfung aufeinander abstimmen

1. Die Erkundungsrolle erfasst jedes Werkzeug, seine Lese- und Schreibeffekte, das Ziel, die erforderliche Autorisierung, Wiederherstellungsmöglichkeiten und Verantwortung. Der Mensch klärt die Richtlinie für irreversible Aktionen und ausdrückliche Freigabegrenzen.
2. Die Implementierung vollendet zunächst einen deterministischen Lauf gegen lokale Testvorrichtungen, einschließlich dauerhaftem Zustand, Ablehnung, Abbruch, Neustart und Abgleich. Ergänzen Sie den Modellplaner hinter diesen Grenzen und definieren Sie dessen typisierten Vertrag.
3. Die prüfende Rolle greift Befugnis- und Freigabegrenzen an, dupliziert Arbeit und unterbricht die Ausführung. Die Release-Rolle bereitet begrenzte Identitäten, eine Notabschaltung, Überwachung und eine Betriebsanleitung vor, bevor ein echter Konnektor aktiviert wird.

Liefern Sie Aufgabenprofil, Befugnismatrix, Zustandsautomaten-ADR, Werkzeugschemata, Beispiele für Freigaben genauer Aktionen, Ausführungs- und Effektprotokolle, beobachtete Testergebnisse, Budgetmodell, Abgleichanleitung und benannte Eskalationsverantwortung. `examples/agent_workflow` ist eine lokale Referenz zur Untersuchung dieser Grenze. Für den Anschluss eines echten Werkzeugs sind weiterhin dessen Authentifizierung, Zielbeschränkungen, Freigaberichtlinie und Vertrag zur Wiederherstellung nach Effekten erforderlich; ein Lauf mit einer Testvorrichtung erteilt nichts davon.

## Tests mit unabhängigen Prüfkriterien für Effekte

Verwenden Sie Unit-Tests für Richtlinien und Zustandsübergänge, Persistenz-Integrationstests für Neustart und Gleichzeitigkeit sowie End-to-End-Tests gegen isolierte Werkzeugziele. Halten Sie ein getrenntes Effektprotokoll unter Kontrolle der Testvorrichtung, damit die Erzählung des Modells keinen Erfolg begründen kann. Duplizieren Sie dieselbe Aufgabe über mehrere Worker hinweg: Untersuchen Sie sowohl Ausführungsdatensätze als auch tatsächliche Effekte. Ein beabsichtigter Effekt oder ein ausdrücklich ungeklärter Zustand ist unter dem erklärten Vertrag akzeptabel; unbemerkte Doppeleffekte sind es nicht.

Lassen Sie eine Freigabe ablaufen, ersetzen Sie ihren Akteur, ändern Sie einen Betrag oder ein Ziel und verwenden Sie eine verbrauchte Freigabe erneut. Das externe Werkzeug darf nicht aufgerufen werden. Liefern Sie abgerufenen Text, der Administratorrechte behauptet, und eine gefälschte Werkzeugantwort, die ein neues Ziel verlangt. Das Gateway muss weiterhin den ursprünglichen Befugnisrahmen durchsetzen. Widerrufen Sie Werkzeugzugriff zwischen Planung und Ausführung, um sicherzustellen, dass die Richtlinie an der Effektgrenze geprüft wird.

Lösen Sie einen Absturz aus, nachdem die Testvorrichtung Erfolg aufgezeichnet hat, aber bevor der Worker die Bestätigung speichert. Ein Neustart muss die Aktion abgleichen oder zurückhalten, nicht automatisch wiederholen. Erschöpfen Sie Ausführungs- und delegierte Budgets und brechen Sie eine eingereihte Aufgabe ab; es darf keine zusätzliche Arbeit eingeplant werden, während bereits laufende Effekte bis zu ihrem endgültigen oder unklaren Ergebnis verfolgt werden müssen. Testen Sie Warteschlangen unter einer vereinbarten begrenzten Last und beobachten Sie Verdrängung, sich verstärkende Wiederholungen und den Rückstau für Betriebspersonen. Bewahren Sie fehlgeschlagene, übersprungene und nicht ausgeführte Fälle auf, statt ein abgeschlossenes Modellgespräch als bestandenen Test zu behandeln.

## Veröffentlichen, wiederherstellen und stilllegen

Führen Sie Konnektoren einzeln mit geprüften Berechtigungsumfängen und begrenzten Einführungszielen ein. Versionieren Sie Werkzeugschemata und Protokollmigrationen kompatibel, damit bestehende Läufe interpretierbar bleiben; lassen Sie Läufe auslaufen oder migrieren Sie sie ausdrücklich, bevor alte Handler entfernt werden. Ein Anwendungsrollback kehrt Werkzeugwirkungen nicht um und erneuert keine Freigaben. Stoppen Sie bei einem Incident die Auftragsweitergabe, widerrufen Sie kompromittierte Befugnisse, bewahren Sie geschützte Audit-Nachweise auf und gleichen Sie ausstehende Operationen ab, bevor autorisierte Arbeit fortgesetzt wird.

Beobachten Sie verweigerte Aktionen, veraltete Freigaben, das Alter unklarer Effekte, Abgleichrückstau, Aufgabenerfolg, menschliche Korrekturen und Ausgaben pro akzeptiertem Ergebnis. Planen Sie Modellaufrufe, Werkzeuggebühren, Wiederholungen, Protokollspeicher und Betriebszeit ein. Zu den Produktionslücken gehören echte Identitäten, geschützte Freigabespeicherung, Isolation der Zugangsdaten, Audit-Aufbewahrung, Anbietergarantien und Rufbereitschaft. Die Stilllegung stoppt neue Aufträge, klärt oder eskaliert ausstehende Effekte, exportiert erforderliche Nachweise, widerruft alle Konnektoren und Zeitpläne und löscht sensiblen Ausführungskontext gemäß der vereinbarten Aufbewahrungsrichtlinie.

## Mit verwandten Entscheidungen fortfahren

[Agenten](agents.md) · [Dauerhaftigkeit](durability.md) · [Integrationen](integrations.md) · [Sicherheitstests](security-testing.md)

## Primärquellen

[owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [azure-idempotent-consumer](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/idempotent-consumer.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md)
