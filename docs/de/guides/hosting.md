---
{
  "id": "hosting",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Hosting und Ausstiegswege

## Die gesamte Verpflichtung vergleichen

| Option | Eignung | Zu berücksichtigende Kosten |
| --- | --- | --- |
| Statisches Hosting/CDN | Öffentliche Dokumente und Dateien | Baulimits, Cache, Domainverantwortung |
| Verwaltete Plattform | Kleine Produktteams | Limits, Datentransfer, Laufzeiten, Export |
| Verwaltete Funktionen | Stoßweise begrenzte Arbeit | Laufzeit, Kaltstarts, Verbindungsdruck |
| VPS mit Containern | Planbare Last und Betriebsverantwortliche | Updates, Backups, Überwachung, Wiederherstellung, Reserve |
| Verwaltetes Kubernetes | Mehrere Lasten und ein befähigtes Team | Richtlinien, Upgrades, Netzwerk, Sicherheit |

Verwaltete Dienste übertragen Aufgaben, nicht Verantwortung. Rechenleistung, Speicher, Transfer, Beobachtung, Support und Arbeitszeit kalkulieren. Region, Datenresidenz, Wiederherstellung, Quoten und Fehlerdomänen prüfen. Erwartetes Wachstum allein begründet kein Kubernetes.

## Portabilitätsvertrag

Konfiguration auslagern, Infrastruktur als Code beschreiben, Domain behalten und Export nachweisen. Artefakte anhand ihres Digests bereitstellen. Anbieterspezifische Funktionen und akzeptierte Bindung benennen; auch Portabilität kostet.

## Prüfen und migrieren

Isoliert bereitstellen, funktionalen Aufruf, Wiederherstellung, Geheimnisrotation und Spitzenkosten prüfen. Migration an einer Kopie üben: Export, Import, Abgleich, Umschaltung, Beobachtung und Rückkehrfenster. DNS-Rollback nimmt neue Schreibvorgänge nicht zurück. Diese Bibliothek nutzt statisches Hosting; manuelle Pages-Bereitstellung hostet keinen MCP-Server.

## Verwandte Entscheidungen

[Eigene Server betreiben](self-hosting.md) · [Anhand von Messungen skalieren](scaling.md) · [Zustand, Wiederherstellung und Kosten](operations.md)

## Primärbelege

[docker-security](https://raw.githubusercontent.com/docker/docs/main/content/manuals/engine/security/_index.md) · [kubernetes](https://raw.githubusercontent.com/kubernetes/website/main/content/en/docs/concepts/architecture/_index.md) · [opentofu](https://raw.githubusercontent.com/opentofu/opentofu/main/README.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml)
