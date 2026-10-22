---
{
  "id": "performance-testing",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Leistungs-, Last- und Stresstests

## Eine konkrete Fehlerfrage wählen

Ein Leistungstest soll eine Projektentscheidung ermöglichen: Erfüllt eine Veröffentlichung ihr Latenzziel, erholt sich eine Warteschlange nach einer Spitze, wo reicht die Kapazität nicht mehr oder wächst der Ressourcenverbrauch über die Zeit? Registrierte Nutzerzahlen und eine einzelne schnelle Anfrage beantworten diese Fragen nicht.

| Testform | Wann einsetzen? | Zu untersuchendes Ergebnis |
| --- | --- | --- |
| Kleiner Probelauf | Lastskript, Testdaten, Berechtigungen und Messungen vor größerem Ressourcenverbrauch prüfen | Anfragen erledigen die beabsichtigte Arbeit; Prüfungen und Abbruchkontrollen funktionieren |
| Repräsentative Last | Normalbetrieb und vereinbarte erwartete Spitzen nach einer relevanten Änderung prüfen | Nutzbarer Durchsatz, hohe Latenzperzentile, Fehler und Ressourcenverbrauch erfüllen das Projektziel |
| Stress | Verhalten oberhalb der erwarteten Last in einem begrenzten Experiment untersuchen | Zugangskontrolle für neue Arbeit, Fehler, Datenintegrität und Erholung verhalten sich wie vorgesehen |
| Spitzenlast | Veröffentlichung, Zeitplan oder externes Ereignis kann Ankünfte plötzlich erhöhen | Wachstum von Warteschlangen, Skalierungsverzögerung, Ablehnung und Erholung nach der Spitze |
| Dauertest | Lecks, Verbindungswechsel, Ablaufzeiten oder regelmäßige Arbeit können sich aufsummieren | Ressourcen- und Latenzverläufe bleiben über den relevanten Lebenszyklus erklärbar |
| Kapazitäts- oder Grenztest | Planung benötigt eine beobachtete Grenze bei festgelegter Konfiguration | Erstes verletztes Ziel, begrenzende Ressource, sichere Reserve und Wiederherstellungsweg |

Die Begriffe unterscheiden sich zwischen Werkzeugen. Dokumentiere tatsächlichen Lastverlauf und Ziel, damit ein anderer Agent das Experiment reproduzieren kann. Stress ist nicht automatisch der richtige nächste Test. Ein fehlgeschlagener Probelauf muss zuerst untersucht werden.

## Tatsächliche Arbeit modellieren

Leite Transaktionsmix, Ankunftsmuster, Nutzdaten- und Datenbestandsgrößen, Lese-/Schreibverhältnis, Cachezustand, Mandantenungleichgewicht, Hintergrundaktivität und Abhängigkeitsverhalten aus Messungen oder ausdrücklichen Annahmen ab. Unterscheide fachliche Transaktionen von ihren einzelnen HTTP-Anfragen. Erkläre Unterschiede zwischen Test und Produktion, bevor du Ergebnisse überträgst.

Wähle das Lastmodell bewusst. Bei einem geschlossenen Modell wartet eine feste Population virtueller Nutzer jeweils auf das Ende ihrer Iteration, bevor sie die nächste beginnt. Wird das System langsamer, kann die angebotene Arbeit sinken. Ein offenes Modell plant neue Arbeit mit einer Ankunftsrate unabhängig vom Abschluss und bildet unabhängige Ankünfte besser ab. Kein Modell passt automatisch zu jedem Produkt. Dokumentiere Denkzeiten und unterscheide eingestellte Rate, tatsächlich gestartete Arbeit, abgeschlossenen Durchsatz und ausgelassene Iterationen.

Stelle sicher, dass Generator, Netzwerk und Zugangsdaten nicht den Engpass bilden. Beobachte die Sättigung des Generators getrennt. Ein überlasteter Generator, der keine weitere Arbeit sendet, kann das Zielsystem gesund erscheinen lassen. Aufwärmphase, Caches, Verbindungspools, automatische Skalierung und Hintergrundjobs beeinflussen Ergebnisse. Untersuche relevante Zustände, statt sie in einer Gesamtauswertung zu verstecken.

## Grenzen vor der Ausführung festlegen

Das Testpaket des Agenten muss das kontrollierte Ziel, Umgebung, erlaubte Routen und Konten, maximale Last, Parallelität, Dauer, Ressourcen- und Ausgabenobergrenzen, Überwachung, Bereinigung und einen handlungsfähigen Verantwortlichen nennen. Isolierte Umgebungen und synthetische Daten sind der Ausgangspunkt. Richte Stressverkehr nicht ohne ausdrückliche, begrenzte Genehmigung und Berücksichtigung der Anbietergrenzen gegen Produktion, Drittanbieter, gemeinsam genutzte Mandanten oder kostenpflichtige Modellendpunkte.

Lege Abnahmeschwellen und Abbruchbedingungen getrennt fest. Die Abnahme bewertet gewünschtes Dienstverhalten; Abbruchbedingungen schützen Menschen, Daten, gemeinsame Systeme und Budget. Ein geplanter Stresstest darf sein normales Latenzziel überschreiten, muss aber an der vereinbarten Sicherheitsgrenze stoppen. Definiere, wie der Abbruch auf den Generator wirkt und wie laufende Arbeit beendet oder abgearbeitet wird. Ein Job-Timeout allein begrenzt keine Rechnung.

Prüfe, wie das Werkzeug Fehler meldet. Beispielsweise erfasst k6 fehlgeschlagene Checks als Metriken. Konfiguriere Schwellenwerte, damit eine verletzte Abnahmebedingung den gesamten Lauf fehlschlagen lässt. Periodische Abbruchauswertung in der Cloud erzwingt Ressourcen- oder Ausgabengrenzen nicht sofort. Ergänze nach Bedarf Begrenzungen auf Dienst- und Kontoebene.

Begrenze die automatische Skalierung bei Kapazitätsexperimenten oder dokumentiere ihre begrenzte Konfiguration. Sonst misst der Test möglicherweise steigende Ausgaben statt die Kapazität eines festgelegten Systems. Verwende Anbieter-Sandboxen oder kontrollierte Ersatzsysteme für teure externe Wirkungen und benenne die dadurch entstehenden Aussagegrenzen.

## Messen und auswerten

Erfasse erfolgreiche fachliche Operationen, Fehlerkategorien, p50-/p95-/p99-Latenzen bei ausreichender Stichprobe, Durchsatz, Parallelität, Alter und Tiefe von Warteschlangen, Verbindungen, CPU, Speicher, Datenträger und relevante Kosten. Werte kritische Routen und Mandanten getrennt aus. Ein schneller häufiger Endpunkt kann einen fehlerhaften Bezahlvorgang in einem globalen Perzentil verdecken. Beziehe fehlgeschlagene und abgelaufene Operationen ein, nicht nur erfolgreiche Antworten.

Bewahre genügend rohe Zeitmessungen und Konfigurationsbelege für eine aussagekräftige Wiederholung auf. Kleine Stichproben machen hohe Perzentile instabil; wiederhole kontrollierte Vergleiche, wenn diese Unsicherheit relevant ist. Gleiche Verschlechterungen mit Ressourcen- und Abhängigkeitsmessungen ab, bevor du sie einer Codeänderung zuschreibst. Unterschiede zwischen zwei unkontrollierten Umgebungen beweisen keine Regression.

Wähle die Dauer eines Dauertests so, dass der gefährdete Lebenszyklus enthalten ist, etwa Tokenverlängerung, geplante Jobs oder Pufferwachstum. Übernimm keine universelle Stundenzahl. Berichte bei Kapazitätstests die gemessene Grenze unter getesteter Konfiguration und Last, kein Versprechen für alle künftigen Nutzer.

## Erholung gehört zum Experiment

Verringere die Last und beobachte, ob Latenz, Warteschlangen und Ressourcenverbrauch innerhalb des vereinbarten Zeitfensters wieder einen brauchbaren Zustand erreichen. Prüfe Datenkonsistenz, doppelte Effekte und verzögerte Jobs. Ein System, das Überlast sicher abweist, seinen Rückstau aber nie abbaut, hat keine Erholung nachgewiesen. Entferne Testdaten und prüfe, dass keine geplanten Generatoren oder kostenpflichtigen Ressourcen unbeabsichtigt aktiv bleiben.

Dokumentiere Ergebnis, Aussagegrenzen, Engpasshypothese und Entscheidung: gemessene Reserve akzeptieren, einen konkreten Pfad optimieren, Zulassungsregeln ändern oder zusätzliche Kapazität untersuchen. Prüfe die geänderte Hypothese erneut. Leistungsanforderungen im Auslieferungsprozess sollen zum Risiko passen und stabil genug für nützliche Rückmeldungen bleiben.

## Belege und verwandte Entscheidungen

Die k6-Dokumentation von Grafana erklärt Lastformen, offene und geschlossene Lastmodelle, Schwellen und Abbruchkontrollen. Die obigen Planungs-, Abnahme- und Erholungsregeln sind eine eigenständige Zusammenführung dieser Bibliothek. Beispielschwellen und Lastwerte aus Anbieterdokumentation sind keine Projektanforderungen.

[Teststrategie](testing-strategy.md) · [Anhand von Messungen skalieren](scaling.md) · [Zustand und Wiederherstellung](operations.md) · [Beständigkeit](durability.md) · [Qualitätsprüfungen](quality.md)

## Primärbelege

[k6-test-types](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/testing-guides/test-types/_index.md) · [k6-open-vs-closed](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/using-k6/scenarios/concepts/open-vs-closed.md) · [k6-thresholds](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/using-k6/thresholds.md) · [k6-stress-testing](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/testing-guides/test-types/stress-testing.md) · [k6-spike-testing](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/testing-guides/test-types/spike-testing.md) · [k6-soak-testing](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/testing-guides/test-types/soak-testing.md) · [k6-breakpoint-testing](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/testing-guides/test-types/breakpoint-testing.md)
