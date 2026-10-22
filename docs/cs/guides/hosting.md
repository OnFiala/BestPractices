---
{
  "id": "hosting",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Hosting a cesta k migraci

## Porovnejte celou povinnost

| Varianta | Vhodné použití | Započítané náklady |
| --- | --- | --- |
| Statický hosting/CDN | Veřejné dokumenty a soubory | Limity sestavení, cache, vlastnictví domény |
| Spravovaná aplikační platforma | Malý produktový tým | Limity, egress, runtime, export |
| Spravované funkce | Nárazová omezená práce | Doba běhu, studené starty, databázová spojení |
| VPS s kontejnery | Předvídatelná zátěž a provozní vlastník | Aktualizace, zálohy, dohled, obnova, rezerva |
| Spravovaný Kubernetes | Více úloh a schopný provozní tým | Pravidla clusteru, upgrady, síť a bezpečnost |

Správa poskytovatelem převádí práci, nikoli odpovědnost. Počítejte compute, úložiště, přenosy, dohled, podporu i lidský čas. Ověřte region, umístění dat, obnovu, kvóty a nezávislost oblastí selhání. Kubernetes nevybírejte jen kvůli očekávanému růstu.

## Přenositelnost

Oddělte konfiguraci, popište infrastrukturu kódem, držte doménu a otestujte export dat. Nasazujte artefakty podle digestu. Zapište specifické funkce poskytovatele i přijatelnou závislost; přenositelnost také něco stojí.

## Ověření a migrace

V izolovaném prostředí otestujte požadavek, obnovu, rotaci přístupu a špičkovou cenu. Migraci nacvičte na kopii: export, import, porovnání, přepnutí, sledování a okno návratu. Samotné vrácení DNS nevrátí nové zápisy. Tato knihovna používá statický hosting; ruční GitHub Pages nasazení nehostuje MCP server.

## Související rozhodnutí

[Provoz vlastních serverů](self-hosting.md) · [Škálování podle měření](scaling.md) · [Zdraví, obnova a náklady](operations.md)

## Primární zdroje

[docker-security](https://raw.githubusercontent.com/docker/docs/main/content/manuals/engine/security/_index.md) · [kubernetes](https://raw.githubusercontent.com/kubernetes/website/main/content/en/docs/concepts/architecture/_index.md) · [opentofu](https://raw.githubusercontent.com/opentofu/opentofu/main/README.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml)
