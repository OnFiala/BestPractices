---
{
  "id": "maintenance",
  "language": "de",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Belege und automatische Pflege

## Belegprozess

`data/sources.json` trennt eine unveränderliche geprüfte Quelle von der URL, deren spätere Änderungen beobachtet werden. Erfasst werden Herausgeber, Geltungsbereich, Prüfintervall und Lizenzbelege. Die Abrufbasis speichert erfolgreiche Hashes, keine menschliche Freigabe. Eine geplante Beobachtung ruft begrenzte HTTPS-Dokumente ab und meldet geänderte, nicht verfügbare oder überfällige Quellen. Ein anderer Hash fordert zur Prüfung auf, autorisiert aber keine Änderung der Hinweise. Ein gescheiterter Abruf bleibt „nicht verfügbar“ und wird nicht zu „unverändert“.

Der Quellenworkflow erzeugt oder aktualisiert bei Handlungsbedarf einen Beleg-PR. Er ändert weder die akzeptierte Basis noch führt er Änderungen zusammen. Ein Mensch liest den relevanten Quelldiff, prüft Aussagen und Anwendbarkeit und entscheidet über die gemeinsame Anpassung von Leitfäden, Übersetzungen, Prüfdaten und Basis. Setze kein Prüfdatum allein wegen einer HTTP-200-Antwort zurück.

## Agentengestützte Aktualisierungen

Das öffentliche Repository beobachtet Quellenmetadaten. Modellerzeugung aus Quellen und Vorschlagsjobs sind auf ein separates privates Repository, einen Spiegel oder einen privaten Arbeitsbereich begrenzt. Logs, Zusammenfassungen, Patches und Artefakte könnten fremden Text vor der Rechteprüfung enthalten. Der optionale private Codex-Workflow benötigt ein konfiguriertes Secret und ausdrückliche Aktivierung; lokale Validierung und Quellenprüfungen brauchen keine kostenpflichtige API. Das Modell gibt begrenzte strukturierte Vorschlagsdaten zurück. Eine frische vertrauenswürdige Verarbeitung prüft diese Daten, statt ein vom Agenten erzeugtes Skript auszuführen oder seinen Git-Metadaten zu vertrauen.

Ein Mensch prüft die privaten Ergebnisse auf eigenständige Formulierungen, Lizenzen, sensible Daten, Belege und Übersetzungsbedeutung, bevor freigegebene Inhalte in einen öffentlichen PR übertragen werden. Es gibt keine automatische öffentliche Übertragung. Verfasse eigenständige Erläuterungen und Beispiele. Kopiere oder übersetze keine fremde Prosa und paraphrasiere charakteristische Formulierungen nicht eng. Erforderliche Hinweise zu fremder Software behalten ihre jeweiligen Lizenzen. Ein Quellenverweis oder Ähnlichkeitstest gewährt keine Nutzungsrechte.

Der Agent darf nicht freigeben, zusammenführen oder veröffentlichen. Rulesets und Pflichtreviews müssen tatsächlich in GitHub konfiguriert werden; eine Workflowdatei erzwingt sie nicht. Ein privater Generierungsdienst wurde als Teil dieser Bibliothek nicht bereitgestellt.

## Aktualität und Fehler

Prüfe schnelllebige KI- und Protokollquellen häufiger als stabile Grundsätze. Kennzeichne Experimente und abgelöste Ansätze, erhalte Migrationslinks und dokumentiere strittige Hinweise. Fehlende Zugangsdaten, blockierte Netzwerke, fehlgeschlagene Prüfungen und veraltete Übersetzungen bleiben sichtbare Hindernisse. Verfolge überfällige Reviews und die Zeit zur Klärung geänderter Quellen. Nimm eine fehlerhafte Empfehlung per Commit zurück und prüfe Projekte, die sie übernommen haben.

Behandle ein README oder einen Index mit eingebundenen Teildateien nicht als Prüfung der zugrunde liegenden Spezifikation. Registriere die tatsächlich verwendete fachliche Kontrolle oder den Mechanismus. Aussagezuordnungen müssen quellenbelegtes Verhalten von lokaler Zusammenführung trennen, Anwendbarkeit dokumentieren und an die geprüfte Version gebunden bleiben. Aktualisiere Lebenszyklusinformationen vor der Einführung einer KI-Plattform. Eine Methode kann sinnvoll bleiben, nachdem das Produkt aus ihrem Beispiel eingestellt wurde.

## Verwandte Entscheidungen

[GitHub, Versionen und saubere Arbeitsbäume](github.md) · [Menschen steuern, Agenten führen aus](agents.md) · [Verantwortung und offene Entscheidungen](governance.md)

## Primärbelege

[codex-action](https://raw.githubusercontent.com/openai/codex-action/c05cfd74ad95c626cdf05c6685e62becc3bf7813/README.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md) · [plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md)
