---
{
  "id": "foundations",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Entscheidungsprinzipien

## Kontext und Standard

Beständige Architektur übersteht Änderungen, Ausfälle und den Verlust individuellen Wissens. Sie verspricht keinen ewigen Stack. Klare Grenzen, wenige Abhängigkeiten und Verantwortliche für jede Betriebsaufgabe bilden den Anfang. Reversible Entscheidungen bevorzugen, bis stärkere Belege eine Bindung rechtfertigen.

## Projektprofile

| Profil | Ausgangspunkt | Pflichten |
| --- | --- | --- |
| Persönlich oder explorativ | Statische Seite oder ein Prozess, bei Bedarf verwalteter Speicher | Reproduzierbarer Aufbau, geschützte Geheimnisse, Export und Wiederherstellung |
| Produkt mit Nutzern | Modulare Anwendung, verwaltete Datenbank, Worker nach Bedarf | Dienstziele, Wiederherstellungstest, Rollback, Supportverantwortung |
| Viel Verkehr oder viele Teams | Gemessene Aufteilung, klare Verträge, Kapazitätsplanung | Bereitschaft, Lasttests, Isolation und Migrationsplan |
| Hohe Konsequenzen | Jede Größe, auch ein Nutzer | Bedrohungsmodell, Nachvollziehbarkeit, Aufbewahrung, Fach- und Rechtsprüfung |

Profile beschreiben Einschränkungen, keinen Reifewettbewerb. Ein kleiner regulierter Dienst kann stärkere Kontrollen benötigen als ein großer öffentlicher Katalog. Bewusst aufgeschobene Schritte samt Auslöser dokumentieren.

## Entscheidungsprotokoll

Jede wesentliche Wahl benennt Problem, Einschränkungen, Alternativen, Belege, Verantwortliche, Kosten, Prüfung und Ausstieg. Fakten von Annahmen und lokale Regeln von externen Standards trennen. Prüftermin und beobachtbaren Auslöser festlegen, etwa dauerhaft überschrittenes Warteschlangenalter.

## Prüfen und überdenken

Neue Mitwirkende müssen die Entwicklungsumgebung reproduzieren, eine Nutzeraktion bis zu ihren Daten verfolgen und eine fehlgeschlagene Veröffentlichung beheben können. Versteht nur der ursprüngliche Autor oder eine Modellsitzung das System, zuerst Dokumentation und Grenzen verbessern. Nach Vorfällen, wesentlichen Kostenänderungen, Produktwechseln oder neuen Rechtspflichten Entscheidungen erneut prüfen.

## Verwandte Entscheidungen

[Architekturen auswählen und verbinden](architecture.md) · [Anhand von Messungen skalieren](scaling.md) · [Verantwortung und offene Entscheidungen](governance.md)

## Primärbelege

[owasp](https://raw.githubusercontent.com/OWASP/ASVS/master/README.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/main/content/en/docs/concepts/observability-primer.md) · [github-rulesets](https://raw.githubusercontent.com/github/docs/main/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md)
