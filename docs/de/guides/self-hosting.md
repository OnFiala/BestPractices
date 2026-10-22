---
{
  "id": "self-hosting",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Eigene Server betreiben

## Minimale Topologie

Ein Reverse Proxy mit TLS führt zur Anwendung im privaten Netz; die Datenbank ist nicht öffentlich. Administration wird eingeschränkt und protokolliert. Produktion und Experimente trennen, Backups in einer anderen Fehlerdomäne und möglichst einem anderen Konto halten. Ein Host bleibt ein einzelner Ausfallpunkt; akzeptierten Ausfall und Wiederherstellung dokumentieren.

## Betriebsvertrag

Infrastruktur als Code, festgelegte Images, minimale Rechte, Ressourcenlimits, persistente Volumes und gezielte Geheimnisbereitstellung verwenden. Keinen Docker-Socket an Anwendungen geben; Container sind keine starke Sandbox. Patchrhythmus, Zertifikatserneuerung, Speicheralarme, Logaufbewahrung und Bereitschaft festlegen. Migrationsrechte vom normalen Datenbankzugang trennen.

Compose eignet sich für wenige Dienste. Orchestrierung braucht belegte Anforderungen an Planung, Verfügbarkeit oder Teamarbeit. Heimserver benötigen zusätzlich eine Bewertung von Strom, Verbindung, physischer Sicherheit und externer Wiederherstellung.

## Wiederherstellung üben

Einen sauberen Server aus dokumentierter Konfiguration erzeugen, Daten zurückspielen, Nutzerpfad prüfen und RTO/RPO messen. Ein erfolgreicher Backupjob reicht nicht. Zertifikatswechsel und vollen Datenträger sicher im Staging testen. Bei unzureichender Wartungs- oder Wiederherstellungskapazität verwaltete Dienste wählen; Replikate ersetzen keine Verantwortung.

## Verwandte Entscheidungen

[Sicherheit, Datenschutz und Lieferkette](security.md) · [Hosting und Ausstiegswege](hosting.md) · [Zustand, Wiederherstellung und Kosten](operations.md)

## Primärbelege

[docker-security](https://raw.githubusercontent.com/docker/docs/main/content/manuals/engine/security/_index.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml) · [opentofu](https://raw.githubusercontent.com/opentofu/opentofu/main/README.md)
