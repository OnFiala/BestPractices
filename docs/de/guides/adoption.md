---
{
  "id": "adoption",
  "language": "de",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Die Bibliothek im Projekt einsetzen

## Ein übertragbares Entscheidungspaket erstellen

Kopiere die benötigten Vorlagen, nicht die gesamte Bibliothek. Erfasse in `project-profile.yaml` Ziel, Datensensibilität, verantwortlichen Eigentümer, Arbeitslast, Budget, Dienstziele und Wiederherstellungsannahmen. Fixiere diese Bibliothek auf eine geprüfte Veröffentlichung oder einen vollständigen Commit und verwende stabile Leitfaden-IDs. Wer dem veränderlichen `main` unbemerkt folgt, kann Produktionsrichtlinien ohne Projektfreigabe ändern.

Erstelle ein Kontextdiagramm und ein ADR für die erste folgenreiche Entscheidung. Dokumentiere übernommene Empfehlungen, bewusst zurückgestellte Kontrollen, einen Verantwortlichen, ein Ablaufdatum und ausgleichende Prüfungen. Projektspezifische Agentenanweisungen gehören in `AGENTS.md`; verlinke unterstützende Unterlagen. Diese Bibliothek liefert von Agenten gepflegte Vorschläge. Ihre Empfehlungen werden erst durch den menschlichen Entscheidungsprozess des Projekts zu dessen Richtlinien.

## Drei Einstiegsbeispiele

- **Persönliche öffentliche Website:** Nutze einen statischen Build, eine Inhaltshistorie und eine reproduzierbare Bereitstellung. Private Notizen, Zugangsdaten und personenbezogene Quelldaten gehören weder in die öffentliche Git-Historie noch in öffentliche Build-Dateien einschließlich Suchindizes. Eine Anmeldeseite schützt keine öffentlich herunterladbaren Dateien. Eine private Wissensbasis benötigt privaten Speicher und serverseitig durchgesetzte Zugriffsprüfungen für Dokumente, Dateien, Downloads und Suche; ein privates Repository allein macht seine veröffentlichten Ergebnisse nicht privat.
- **Kleines SaaS:** Beginne mit einer modularen Anwendung, einer transaktionalen Datenbank und einem Worker nur dort, wo er benötigt wird. Definiere Mandantengrenzen, Zahlungsabgleich und einen Betriebsverantwortlichen. Beweise vor der Aufnahme echter Kunden, dass mandantenübergreifende Zugriffe abgewiesen werden, Versionen während der Bereitstellung kompatibel bleiben und eine Wiederherstellung in einer isolierten Umgebung funktioniert.
- **Plattform mit hohem Verkehrsaufkommen:** Miss zuerst Anfragemix, ungleichmäßige Lastverteilung, Datenwachstum und Abhängigkeitsgrenzen. Partitioniere oder isoliere eine Arbeitslast erst, wenn die Begrenzung nachgewiesen und die Verantwortung für Konsistenz, Migration, Bereitschaftsdienst und Wiederherstellung vergeben ist. Eine hohe Kontenzahl allein definiert keinen Kapazitätsbedarf.

Dies sind eigenständig entwickelte Einstiegsempfehlungen, keine universellen Vorgaben oder durch Benchmarks bestätigten Bereitstellungsvorlagen.

## Empfehlungen in Abnahmenachweise übersetzen

Bestimme für jeden übernommenen Leitfaden die beobachtbare Verpflichtung und die Prüfung, die ihre Erfüllung widerlegen könnte. Aus „Mandantentrennung“ wird beispielsweise ein Test, bei dem die authentifizierte Sitzung von Mandant A über API-, Export- und Worker-Pfade ein Objekt von Mandant B anfordert und keiner dieser Pfade dessen Daten zurückgibt. Dokumentiere Testaufbau, erwartetes Ergebnis, ausgeführte Revision und aufbewahrte Nachweise in der [Teststrategie](testing-strategy.md).

Nutze die [Referenzprofile](../reference/examples.md), um fehlende Grenzen zu erkennen. Eine nicht ausgeführte Abnahmebedingung ist ein geplanter Test, kein Nachweis. Behaupte keine Sicherheit, nur weil eine Vorlage ausgefüllt ist oder eine erzeugte Zusammenfassung „bestanden“ meldet. Prüfe das tatsächliche Ergebnis einschließlich Fehlern und Auslassungen.

## Neu bewerten und die Kontrolle behalten

Ziehe passende Leitfäden bei der Planung heran und verlinke sie in der Implementierungsaufgabe. Vergleiche beim Review den Diff mit der gewählten Entscheidung und den Fehlerfällen. Prüfe vor der Veröffentlichung Migration und Wiederherstellung; führe im Betrieb Messwerte und Vorfälle in die ADRs zurück. Aktualisiere die fixierte Bibliotheksversion durch einen PR, der geänderte Verpflichtungen, betroffene Projekte und den Migrations- oder Ausnahmeplan erklärt.

Wenn eine neue Empfehlung mit Budget und Zuständigkeiten des Projekts nicht geprüft werden kann, dokumentiere diese Lücke und vereinfache den Entwurf. Übernimm nicht stillschweigend eine Richtlinie, die niemand betreiben kann.

## Verwandte Entscheidungen

[Entscheidungsprinzipien](foundations.md) · [Der vollständige Projektlebenszyklus](lifecycle.md) · [Teststrategie](testing-strategy.md) · [Menschen steuern, Agenten führen aus](agents.md) · [Verantwortung und offene Entscheidungen](governance.md)

## Primärbelege

[plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md) · [github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md)
