---
{
  "id": "adoption",
  "language": "de",
  "revision": 3,
  "translation_revision": 3,
  "reviewed_on": "2026-10-22"
}
---
# Die Bibliothek im Projekt einsetzen

## Mit einem Auslieferungsweg beginnen

Wenn du die Bibliothek zum ersten Mal verwendest, durchlaufe
[deinen ersten Prüfpunkt mit Nachweisen](first-project.md). Nutze anschließend
[den Auslieferungsablauf](project-delivery.md) mit dem Leitfaden für dein Projekt.
Dabei entstehen ein Plan, ein kleines Arbeitsergebnis, eine tatsächliche Beobachtung
und eine Begutachtung. Ein **Prüfpunkt** verlangt bestimmte Ergebnisse und legt
blockierende Bedingungen fest. Ein **Artefakt** ist ein Ergebnis wie ein Entscheidungsdokument,
eine Quellcodeänderung oder ein Testbericht. **Nachweise** halten fest, was jemand
an diesem Ergebnis tatsächlich begutachtet oder ausgeführt hat. Eine geplante Prüfung
ist keine Beobachtung, und eine ausgefüllte Vorlage ist keine Genehmigung.

## Das richtige Profil verwenden

| Datei | Zweck | Wer sie liest |
| --- | --- | --- |
| `templates/delivery-profile.json` | Beispiel für die Eingabe mit strengem JSON-Schema: Projekttyp, genaue Zielrevision, Risiko, Daten, Last, Hosting, Schnittstellen, Effekte und Ziele | `library.delivery plan`, `library.delivery assess` und `library.project init` |
| `project-profile.json` | Das ausgefüllte JSON-Auslieferungsprofil deines Projekts; diesen Namen erzeugt `init` | Dieselben Werkzeuge; der Dateiname unterscheidet sich, das Schema nicht |
| `templates/project-profile.yaml` | Optionales ausführliches Entscheidungsdokument: Verantwortlicher, Budget, Dienstziele, Datenstandort, Wiederherstellung und Ausnahmen | Menschen und Agenten; die CLI liest oder konvertiert es nicht |

Beginne für die ausführbare Planung mit der JSON-Vorlage. Ersetze ihre synthetischen
Anforderungen durch tatsächliche Projektentscheidungen. Bewahre bei einem bestehenden
Projekt das Profil und die Nachweise am dafür genehmigten Ort im Projekt auf und
rufe die Bibliotheks-CLI mit ausdrücklichen Pfadangaben auf. Führe `init` nicht
über einem bestehenden Projekt aus: Es erstellt ausschließlich ein neues Zielverzeichnis.
Für ein neues übertragbares Paket kopiert `init` die benötigten Werkzeuge,
Leitfäden, Lizenzen und ausgewählten Referenzbeispiele; diese sind nicht dein fertiges Produkt.
Wenn du die Bibliothek nur zum Lesen und zur Entscheidungsunterstützung nutzt,
verlinke die passenden Leitfäden und kopiere nur die benötigten Vorlagen;
weder Paketerstellung noch MCP ist dafür erforderlich.

Wenn du auch das YAML-Entscheidungsdokument pflegst, übertrage Entscheidungen bewusst:

| Entscheidungsdokument | Auslieferungsprofil | Was ausgelegt werden muss |
| --- | --- | --- |
| `name`, `outcome`, `non_goals` | `project_id`, `description`, `objectives`, `constraints` | Wähle eine gültige stabile ID und beobachtbare Ergebnisse; benenne nicht einfach Schlüssel um |
| `data.classification` | `data_sensitivity` | Wähle nach Prüfung der tatsächlichen Daten eine unterstützte Kategorie |
| Gemessene `workload`-Felder | `workload` | Wähle eine begründete Kategorie; verwende `unmeasured`, wenn Messungen fehlen |
| `library_revision` | Kein entsprechendes Profilfeld | Fixiere die Bibliotheksrevision separat; `revision` im JSON bezeichnet den Git-Commit des Zielprojekts |
| Verantwortlicher, Budget, Dienstziele, Datenstandort, Wiederherstellung, Ausnahmen | Im Entscheidungsdokument und in den zugehörigen Prüfpunktartefakten festhalten | Diese Verpflichtungen gelten weiterhin; der Planer wertet diese YAML-Felder nicht aus |

Auch Projekttyp, Hosting, Schnittstellen, Effekte und Risiko erfordern ausdrückliche
Entscheidungen im JSON. Es gibt keine automatische Konvertierung oder Synchronisierung.
Wenn sich gemeinsame Annahmen ändern, aktualisiere beide Dokumente, erstelle den
Plan neu und bewerte die betroffenen Nachweise erneut. Füge dem strengen JSON-Schema
keine Felder hinzu, die nur für YAML vorgesehen sind. Fixiere die Bibliothek auf eine
geprüfte Veröffentlichung oder einen vollständigen Commit und verwende stabile
Leitfaden-IDs. Wer dem veränderlichen `main` unbemerkt folgt, kann Projektrichtlinien
ohne Projektfreigabe ändern.

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
