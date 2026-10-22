---
{
  "id": "playbook-public-website",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Eine öffentliche Website bereitstellen

## Eignung und erste Entscheidungen

Verwenden Sie dieses Profil für öffentliche redaktionelle Inhalte, Dokumentation oder eine Kampagne, deren wichtigste Nutzung aus Lesen, Suchen und dem Folgen von Links besteht. Erfassen Sie Sprachversionen, Veröffentlichungsfrequenz, Erwartungen an die Barrierefreiheit, Domainverantwortung, das Budget für ausgelieferte Ressourcen und die akzeptable Zeit zur Korrektur einer schädlichen Veröffentlichung. Der Ausgangspunkt ist ein statischer Build aus geprüften Inhalten, unveränderliche Release-Artefakte und ein CDN. Dies ist ein von Agenten verfasster Vorschlag und eine lokale Synthese, keine verabschiedete Richtlinie oder Zertifizierung für den Produktionsbetrieb.

Eine serverseitig gerenderte Route ist eine Alternative, wenn die erforderliche Aktualität keinen Build abwarten kann. Authentifizierte Eingaben erfordern eine ausdrückliche serverseitige Grenze; behandeln Sie einen schreibenden Dienst nicht als bloßes Detail einer statischen Website. Eine kleine Website kann Inhalte und Darstellung zusammenhalten. Wenn Builds oder konkurrierende redaktionelle Änderungen wachsen, trennen Sie zunächst die Inhaltsvalidierung und führen Sie inkrementelle Builds ein. Ergänzen Sie Dienste erst, wenn gemessene Veröffentlichungsverzögerungen, dynamische Arbeit oder Verantwortungsanforderungen ihre Betriebskosten rechtfertigen; die Besucherzahl allein genügt nicht.

## Grenzen und Verträge

Ordnen Sie `content/`, `ui/`, `build/`, `tests/` und `ops/` nach Verantwortung, auch wenn sie dasselbe Repository teilen. Das Inhaltsschema verantwortet stabile Seiten-IDs, Sprache, Weiterleitungen, Veröffentlichungsstatus und öffentliche Metadaten. Die Benutzeroberfläche verantwortet Navigation, Suchzustände, Fokus und barrierefreie Fehlermeldungen. Der Build verantwortet die deterministische Umwandlung und eine ausdrückliche Positivliste zulässiger Ressourcen. Private Entwürfe, Zugangsdaten und interne Kommentare dürfen niemals in auslieferbares HTML, JSON-Suchindizes, Source Maps oder herunterladbare Quellpakete gelangen.

Legen Sie die Beständigkeit von URLs, das Verhalten von Weiterleitungen, fehlenden Übersetzungen, die Version des Suchindex und Cache-Laufzeiten fest. Bauen Sie Index und Seiten in dasselbe Release ein. Vorschauidentitäten dürfen Entwurfsmaterial lesen; die Identität für die Veröffentlichung in Produktion darf nur das genehmigte Artefakt erhalten. Behandeln Sie verfasstes HTML, importiertes Markdown und Suchtext an ihren Rendering-Grenzen als nicht vertrauenswürdig; verwenden Sie sichere Textausgabe oder eine ausdrücklich geprüfte Bereinigungsrichtlinie.

## Die Arbeit in Schritte gliedern

1. Der Erkundungsagent erfasst drei öffentliche Nutzungsszenarien, ein Verzeichnis der Routen und Sprachversionen, die Inhaltsverantwortung sowie quantitative Veröffentlichungs- und Leistungsziele in einem Projektprofil. Ein Mensch entscheidet über Marke, Barrierefreiheit und Veröffentlichungsrisiken.
2. Die Rolle für Entwurf und Implementierung erstellt ein vollständiges Nutzungsszenario einschließlich leerer Suche, fehlender Route, mobiler Bildschirmbreite und Tastaturnavigation. Sie hält die Rendering-Entscheidung und den Umfang der Abhängigkeiten in einem ADR fest, bevor weitere Seitenvorlagen entstehen.
3. Die prüfende Rolle untersucht ein gebautes Artefakt in einem isolierten echten Browser, prüft die Ausgabedaten und erprobt ein älteres Release. Die Release-Verantwortung wählt den genehmigten Digest aus und kontrolliert die Zugangsdaten für das Deployment.

Übergeben Sie ein konkretes Paket: Profil, ADR, Inhaltsschema, Routenmanifest, Artefakt-Digest und Commit, Browserbeobachtungen, offene Punkte der Barrierefreiheitsprüfung, Prüfung der Ausgabedaten, Deployment- und Wiederherstellungsanleitung sowie benannte Inhalts- und Domainverantwortliche. Halten Sie geplante, ausgeführte, fehlgeschlagene und übersprungene Prüfungen auseinander. Das lokale Referenzverzeichnis `examples/frontend` ist ein Ausgangspunkt für Interaktionsarbeit, kein Nachweis dafür, dass die Routen oder die Barrierefreiheit dieses Projekts geprüft wurden.

## Prüfungen auswählen, die Bereitschaft widerlegen können

Verwenden Sie Unit-Prüfungen für Parser- und Routenregeln, Integrationsprüfungen für die Konsistenz zwischen Inhalten und Index sowie Black-Box-Browserprüfungen für öffentliche Nutzungsszenarien. Bei einer umbenannten Seite muss die alte URL zum vorgesehenen Ersatz führen, nicht zu einer plausiblen, aber falschen Seite. Suchen Sie in jeder generierten Ressource nach einer synthetischen privaten Markierung: Ein Treffer lässt die Release-Prüfung scheitern, auch wenn die Markierung auf sichtbaren Seiten fehlt. Geben Sie Markup in die Suche und in importierte Titel ein; es muss harmloser Text bleiben oder der geprüften Bereinigungsregel folgen, ohne Skriptcode auszuführen.

Drosseln Sie das Netzwerk, lassen Sie den Suchabruf fehlschlagen und navigieren Sie weiter, bevor er abgeschlossen ist. Maßgeblich muss die aktuelle Seite bleiben; ein verspätetes Ergebnis darf keine neuere Suchanfrage überschreiben, und nach einem Fehler muss eine Wiederherstellung möglich sein. Prüfen Sie in jeder unterstützten Sprachversion, ob Aufgaben vollständig per Tastatur ausführbar sind und der Fokus sichtbar ist; automatisierte Ergebnisse zur Barrierefreiheit allein belegen keine Konformität. Messen Sie die Übertragung bei kaltem Cache, Interaktionsverzögerung, Build-Zeit und Cache-Trefferverhalten auf repräsentativen Geräten anhand der Projektziele. Stoppen Sie Tests am vereinbarten Verkehrs- oder Ausgabenlimit.

## Veröffentlichen, betreiben und stilllegen

Prüfen Sie genau das vorgesehene Artefakt in der Vorschau, stellen Sie es einem begrenzten Publikum oder unter einem Staging-Hostnamen bereit und verifizieren Sie vor der Freigabe kritische Routen und Header. Bewahren Sie das vorherige Artefakt und die Routing-Konfiguration auf. Ein Rollback kann Seiten wiederherstellen, aber keine Kopien aus Caches, Suchmaschinen, Downloads oder der Git-Historie zurückholen; eine Offenlegung erfordert eine Incident-Reaktion und gegebenenfalls die Rotation geheimer Zugangsdaten. Weiterleitungsmigrationen benötigen eine aufbewahrte Zuordnung, und das Entfernen einer Sprachversion erfordert eine ausdrückliche Prüfung von Links und Nutzerauswirkungen.

Benennen Sie Verantwortliche für fehlgeschlagene Builds, Domain- und Zertifikatsverlängerung, missbräuchlichen Verkehr und dringende Inhaltskorrekturen. Beobachten Sie Routenfehler, Suchfehler, das Alter der Veröffentlichung und die Verfügbarkeit synthetischer Nutzungsszenarien, ohne unnötige Besucherdaten aufzubewahren. Planen Sie CDN-Übertragung, Build-Minuten, Logs, Abhängigkeiten und redaktionelle Pflege ein. Schließen Sie vor dem Produktionsbetrieb Lücken bei Hosting-Konfiguration, Header-Richtlinie, Sicherung und Export, Barrierefreiheit und Rufbereitschaft; die Referenz liefert diese nicht mit. Bei der Stilllegung bewahren Sie vereinbarte Inhaltsexporte und Weiterleitungen auf, entziehen den Veröffentlichungszugriff, entfernen Tracking und behalten für den vereinbarten Übergang die Kontrolle über die Domain.

## Mit verwandten Entscheidungen fortfahren

[Frontend-Verträge](frontend.md) · [Hosting](hosting.md) · [Auslieferung über GitHub](github.md) · [Teststrategie](testing-strategy.md)

## Primärquellen

[github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md) · [owasp-xss](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.md) · [playwright-testing](https://raw.githubusercontent.com/microsoft/playwright/ca7ca36145b84183cf423c2a099bd7e9cd8b1cb3/docs/src/best-practices-js.md) · [wcag-keyboard](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/sc/20/keyboard.html) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md)
