---
{
  "id": "coverage",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Abdeckung und Verifikation ehrlich beurteilen

## Die erklärte Abdeckungsübersicht verwenden

Das maschinenlesbare Abdeckungsregister beschreibt die von dieser Ausgabe unterstützten Lebenszyklusbereiche. Jeder Eintrag verknüpft Leitfäden und Primärquellen, benennt vorhandene ausführbare Referenzen und genaue Testfälle, definiert die eng begrenzte Aussage und führt Nachweise auf, die in einem übernehmenden Projekt noch benötigt werden. Die Übersicht erklärt einen Geltungsbereich; sie erhebt keinen Anspruch, das gesamte Software Engineering aufzuzählen.

Lesen Sie sie über `python -m library.coverage`, das schreibgeschützte MCP-Werkzeug oder die exportierten Websitedaten. Ein optionaler lokaler Prüfbericht kann Beobachtungen ergänzen, die an den aktuellen Eingabedateistand gebunden sind. Das statische Register einer Website wird nicht dadurch zu einem frisch ausgeführten Ergebnis, dass jemand es öffnet.

## Arten der Unterstützung unterscheiden

| Unterstützung | Was vorhanden ist | Was unbekannt bleibt |
| --- | --- | --- |
| Dokumentierte Empfehlungen | Eine eigenständige Entscheidungserklärung und Quellenlinks mit begrenztem Geltungsbereich | Ob die Erklärung auf dieses Projekt zutrifft oder umgesetzt wurde |
| Ausführbare Referenz | Eigenständiger Code und benannte Prüfungen, die eine angegebene lokale Grenze erproben können | Ob diese Prüfungen mit genau diesen Eingaben ausgeführt wurden und was dabei geschah |
| Aktuelle aufgezeichnete Beobachtung | Passende Eingabehashes und eine als bestanden aufgezeichnete Suite mit den erforderlichen benannten Fällen | Ob der Bericht authentisch ist, das Prüfkriterium ausreicht oder sich ein anderes Ziel gleich verhält |
| Fehlende, veraltete, fehlgeschlagene oder teilweise Beobachtung | Erforderliche Nachweise fehlen, haben sich geändert, sind fehlgeschlagen oder unvollständig | Die unbelegte Aussage bleibt unbelegt; aus Schweigen darf kein Erfolg abgeleitet werden |

Jedes lokale Ergebnis bleibt seinem Geltungsbereich untergeordnet. Ein SQLite-Nachweis zum Prozessneustart belegt keine Wiederherstellung eines replizierten Speichers. Ein kurzer Loopback-Lauf mit geschlossenem Lastmodell belegt keine Last von einer Million Nutzern. Ein deterministisches Testmodell belegt keine Qualität eines echten Modells. Ein einzelner Chromium-Smoke-Test belegt weder vollständige Barrierefreiheit noch eine Matrix unterstützter Browser.

## Die richtige Frage zum Abschluss stellen

Bestimmen Sie für ein konkretes Projekt, welche Anforderungen und Fehlerfolgen wesentlich sind. Wählen Sie den passenden Projektleitfaden und die Prüfstufen des Planers, und ordnen Sie anschließend jede Abnahmepflicht einem beobachtbaren Ergebnis zu. Prüfen Sie neben erfolgreichen Antworten auch verweigerte Effekte, dauerhaft gespeicherten Zustand und Wiederherstellung. Erfassen Sie bewusst ausgelassene Tests und deren Risiko, statt aus einem bestandenen Beispiel einen ganzen Bereich als abgeschlossen zu markieren.

Die prüfende Rolle sollte Quellenaussage, Implementierungsgrenze, Testkriterium, ausgeführtes Artefakt und Umgebung untersuchen. Ein passender Hash belegt lediglich Identität. Quellenzahlen, Zahlen übersetzter Seiten und eine grüne Übersicht ersetzen diese Kette nicht. Lokale Berichte und Rollenbezeichnungen sind weder signierte Bescheinigungen noch authentifizierte menschliche Genehmigung.

## Lücken ausdrücklich pflegen

Das Register benennt Erweiterungen, die zusätzliche Projektarbeit benötigen: native Clients und Geräte, reguliertes oder sicherheitskritisches Verhalten, harte Echtzeitsysteme, regionsübergreifende Ausfallsicherung, große Daten- und Trainingspipelines, produktive Identitäts- und Zahlungsintegrationen sowie Langzeitkapazität. Allgemeine Empfehlungen können auch diese Projekte unterstützen, aber diese Ausgabe enthält nicht für jede spezialisierte Grenze eine ausgeführte Referenz.

Ergänzen Sie beim Ausbau eines Bereichs eigenständige Empfehlungen, Quellenbelege, bei Bedarf eine widerlegbare Referenz, Negativfälle, Einschränkungen und alle vier Sprachversionen. Eine Quellenänderung löst eine inhaltliche Prüfung aus; ein neues Testergebnis gehört zu seinen genauen Eingaben. Bewahren Sie historische Berichte als datierte Nachweise auf, statt ihre Bedeutung stillschweigend zu ersetzen. Die Übernahme durch Menschen bleibt eine getrennte Entscheidung.

## Verwandte Entscheidungen

[Agentengestützter Auslieferungsablauf](project-delivery.md) · [Referenzprüfungen](reference-labs.md) · [Qualitätsprüfungen](quality.md) · [Nachweispflege](maintenance.md)

## Primärquellen

[github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md) · [owasp-asvs-requirements](https://raw.githubusercontent.com/OWASP/ASVS/3383877f732ce89a458a1af43288f2f1b1d7db0c/5.0/docs_en/OWASP_Application_Security_Verification_Standard_5.0.0_en.csv)
