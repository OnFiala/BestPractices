---
{
  "id": "foundations",
  "language": "de",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Entscheidungsprinzipien

## Kontext und Ausgangspunkt

Beständige Architektur bedeutet, dass Änderungen, Ausfälle und der Verlust individuellen Wissens überstanden werden können. Sie verspricht nicht, dass ein Stack für immer hält. Beginne mit ausdrücklichen Grenzen, wenigen Abhängigkeiten und einem Verantwortlichen für jede Betriebsverpflichtung. Bevorzuge reversible Entscheidungen, bis stärkere Belege eine Bindung rechtfertigen.

## Projektprofile

| Profil | Ausgangspunkt | Pflichten |
| --- | --- | --- |
| Persönlich oder explorativ | Statische Website oder ein Prozess, bei Bedarf verwalteter Speicher | Reproduzierbare Einrichtung, sorgfältiger Umgang mit Secrets, Export und Wiederherstellung |
| Produkt mit echten Nutzern | Modulare Anwendung, verwaltete Datenbank, Hintergrund-Worker bei Bedarf | Dienstziele, Wiederherstellungstest, Deployment-Rollback und Supportverantwortlicher |
| Viel Verkehr oder viele Teams | Gemessene Partitionierung, ausdrückliche Verträge und Kapazitätsplanung | Bereitschaftsabdeckung, Lasttests, Isolation und Migrationspläne |
| Schwerwiegende Folgen | Jede Größe, auch ein Nutzer | Bedrohungsmodell, Auditierbarkeit, Aufbewahrung sowie Rechts- und Fachprüfung |

Profile beschreiben Rahmenbedingungen, keinen Reifewettbewerb. Ein kleiner regulierter Dienst kann stärkere Kontrollen benötigen als ein großer öffentlicher Katalog. Dokumentiere bewusst zurückgestellte Maßnahmen und das Signal, das sie erforderlich macht.

## Entscheidungsprotokoll

Jede folgenreiche Wahl benennt Problem, Rahmenbedingungen, Optionen, Belege, Verantwortlichen, erwartete Kosten, Prüfung und Ausstiegsweg. Trenne Fakten von Annahmen und lokale Richtlinien von externen Standards. Lege einen Prüftermin und einen beobachtbaren Auslöser fest, etwa ein dauerhaft über dem vereinbarten Ziel liegendes Alter wartender Aufgaben.

## Prüfen und neu bewerten

Ein neuer Mitwirkender muss den Entwicklungsablauf reproduzieren, eine Nutzeraktion bis zu ihren Daten verfolgen und eine fehlgeschlagene Veröffentlichung beheben können. Kann nur der ursprüngliche Autor oder eine Modellsitzung das System erklären, verbessere Dokumentation und Grenzen, bevor du Komponenten hinzufügst. Bewerte Entscheidungen nach Vorfällen, wesentlichen Kostenänderungen, einer Neuausrichtung des Produkts oder geänderten rechtlichen Pflichten erneut.

## Verwandte Entscheidungen

[Architekturen auswählen und verbinden](architecture.md) · [Anhand von Messungen skalieren](scaling.md) · [Verantwortung und offene Entscheidungen](governance.md)

## Primärbelege

[owasp](https://raw.githubusercontent.com/OWASP/ASVS/2b47a9dd16760ee484a6672d197f1f7e25d9c632/README.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md) · [github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md)
