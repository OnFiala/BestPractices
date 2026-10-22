---
{
  "id": "security",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Sicherheit, Datenschutz und Lieferkette

## Mit Werten und Grenzen beginnen

Sensible Daten, Akteure, Eingänge, Vertrauensgrenzen und plausible Missbrauchsfälle erfassen. Schutz richtet sich nach Folgen, nicht Projektgröße. Vertrauenswürdig validieren, Objekte und Aktionen autorisieren, Daten minimieren sowie Aufbewahrung und Löschung definieren. Rechtliche und fachliche Pflichten brauchen qualifizierte menschliche Prüfung; diese Bibliothek ist kein Zertifikat.

## Lieferung und Betrieb

Identitäten für Entwicklung, CI und Produktion trennen; kurzlebige eingeschränkte Zugangsdaten, Geheimnisspeicher und Rotation bevorzugen. Abhängigkeiten sperren und Actions auf vollständige Commits fixieren. Updates, Lizenzen, Herkunft und Schwachstellen prüfen. TLS, Signaturen und Prüfsummen beibehalten.

Unvertrauenswürdige PRs nie mit Produktionsgeheimnissen oder privilegiertem `pull_request_target` ausführen. Keinen Host-Docker-Socket in Agentenarbeit einbinden. Werkzeugziele und Aktionen beschränken; Beschreibungen und Dokumente bleiben unvertrauenswürdige Eingaben. Prompts erzwingen keine Autorisierung.

## Prüfen und reagieren

Mandantengrenzen, verweigerte Aktionen, Sitzungsentzug und Rotation testen. Logs auf sensible Daten prüfen. Vorfallkontakt, Eindämmung, Wiederherstellung und Meldung dokumentieren. Sensible Funktionen anhand von Bedrohungen und Belegen prüfen. Schutz mit Sensibilität und Auswirkungsradius erhöhen, nicht erst mit Nutzerzahlen.

## Verwandte Entscheidungen

[Menschen steuern, Agenten führen aus](agents.md) · [Eigene Server betreiben](self-hosting.md) · [Daten, Verträge und Migrationen](data.md)

## Primärbelege

[owasp](https://raw.githubusercontent.com/OWASP/ASVS/master/README.md) · [docker-security](https://raw.githubusercontent.com/docker/docs/main/content/manuals/engine/security/_index.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/main/content/actions/reference/security/secure-use.md)
