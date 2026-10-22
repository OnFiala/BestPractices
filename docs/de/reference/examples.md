---
{
  "id": "examples",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Referenzpfade für Projekte

## Sechs konkrete Ausgangspfade

| Projekt | Anfangsarchitektur | Erster Nachweis | Erweiterungssignal |
| --- | --- | --- | --- |
| Öffentliche Website | Statischer Bau, CDN, Git-Inhalte | Suche, Tastatur, Inhaltsrollback | Vertrauenswürdiges Schreiben braucht API |
| SaaS | Modulare App, relationale Datenbank, Worker | Mandantentrennung, Zahlungsabgleich, Restore | Gemessene Konflikte oder unabhängige Teams |
| Internes Werkzeug | SSO, kleine App, Audit | Entzogener Account kann nicht exportieren | Getrennte Integrationsverantwortung |
| KI-Anwendung | API, Modelladapter, autorisiertes Retrieval | Belegte Antworten, verweigerte Dokumente, Timeout | Gemessene Qualitäts-/Kostengrenzen |
| Agentenautomation | Queue, begrenzter Worker, Laufregister, eingeschränkte Tools | Duplikat, Budgetstopp, Schreibfreigabe | Unabhängige Lasten brauchen Eigentümer |
| Mobil + Backend | UI, versionierte API, lokaler Cache | Offlineänderung, Konflikt, alter Client | Gemessene Sync-/Latenzgrenzen |

`data/blueprints.json` enthält Grenzen, Abnahmebeispiele, Wiederherstellung und Migrationssignale. Dies sind Entwurfsreferenzen, keine bereitgestellten Anwendungen. Passendes Profil übernehmen und Beispiele in echte Stacktests verwandeln.

Mobile Clients aktualisieren nicht gleichzeitig. Additive APIs, fortsetzbare Synchronisierung, Konfliktregeln, Geräteentzug und sicheren Plattformspeicher bevorzugen. KI-Retrieval muss Dokumentrechte und Löschung erhalten; plausible Antworten beweisen keine Richtigkeit. Unternehmensnetze ersetzen keine Aktionsautorisierung.

Budget, SLO, Datenresidenz und Wiederherstellung vor Start menschlich vereinbaren. Kleine Teams können für alle Pfade verwaltete Plattformen wählen; Verträge und Pflichten bleiben unterschiedlich.

## Verwandte Entscheidungen

[Die Bibliothek im Projekt einsetzen](../guides/adoption.md) · [Architekturen auswählen und verbinden](../guides/architecture.md) · [Menschen steuern, Agenten führen aus](../guides/agents.md) · [Frontendarchitektur und Verträge](../guides/frontend.md)

## Primärbelege

[owasp](https://raw.githubusercontent.com/OWASP/ASVS/master/README.md) · [openai-agents](https://raw.githubusercontent.com/openai/openai-agents-python/main/docs/agents.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml) · [wcag](https://raw.githubusercontent.com/w3c/wcag/main/guidelines/index.html)
