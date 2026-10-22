---
{
  "id": "frontend",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Frontendarchitektur und Verträge

## Rendering nach Interaktion wählen

Statische Generierung für Inhalte, Serverrendering für aktuelle Anfangsdaten oder Indexierung, Clientrendering für anhaltende Interaktion verwenden. Hybrid pro Route entscheiden. Hydrationskosten, Cache, Anmeldung und Bereitstellung beschreiben. Microfrontends sind ein organisatorischer Kompromiss für unabhängige Verantwortlichkeiten.

## Zustand verständlich halten

Serverdaten, URL/Navigation, lokalen Interaktionszustand und dauerhafte Präferenzen trennen. Je Zustand einen Eigentümer bestimmen; Serverdaten nicht mehrfach kopieren. Nach Produktfunktionen und Verträgen strukturieren. Zugängliche Grundelemente vor einem großen Designsystem teilen.

API-Schemata, Fehler, Seitennavigation, Abbruch und veraltete Daten definieren. Eingaben serverseitig prüfen und jede geschützte Aktion dort autorisieren. Verborgene Schaltflächen ersetzen keine Berechtigung. Keine Servergeheimnisse im Browserbundle. Effekte abbrechen und Abonnements entfernen; optimistische Änderungen benötigen Fehlerbehandlung und Abgleich.

## Prüfen und entwickeln

Tastatur, Fokus, zugängliche Namen, Kontrast, Lade-/Leer-/Fehler-/Offlinezustände und schmale Ansichten testen. Navigation, Datenmenge, Interaktionslatenz und JavaScript-Fehler messen. BFF nur bei begründeter Aggregation oder Sicherheitsgrenze ergänzen. Frameworkwechsel müssen ihre Migrationskosten einschließlich Barrierefreiheit und Wartung rechtfertigen. WebMCP ergänzt die Oberfläche; menschliche Bedienung bleibt ohne diese Funktion möglich.

## Verwandte Entscheidungen

[Architekturen auswählen und verbinden](architecture.md) · [Qualitätsprüfungen mit Verhaltensnachweis](quality.md) · [Skills, Plugins, MCP und WebMCP](integrations.md)

## Primärbelege

[wcag](https://raw.githubusercontent.com/w3c/wcag/main/guidelines/index.html) · [owasp](https://raw.githubusercontent.com/OWASP/ASVS/master/README.md) · [webmcp](https://raw.githubusercontent.com/webmachinelearning/webmcp/main/README.md)
