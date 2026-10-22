---
{
  "id": "self-hosting",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Provoz vlastních serverů

## Minimální topologie

Reverzní proxy s TLS vede na aplikaci v privátní síti; databáze není veřejně vystavena. Správa má omezený a auditovaný přístup. Oddělte produkci od experimentů, zálohy držte v jiné oblasti selhání a pokud možno i účtu. Jeden host je jediný bod selhání: zapište přijatelný výpadek a obnovu.

## Provozní dohoda

Používejte infrastrukturu jako kód, připnuté obrazy, minimální oprávnění, limity zdrojů, trvalé svazky a explicitní tajemství. Nevystavujte aplikaci Docker socket; kontejner není silný sandbox. Určete aktualizace, obnovování certifikátů, diskové alarmy, retenci logů i pohotovost. Oddělte migrační databázové oprávnění od běžného přístupu.

Compose je vhodný začátek pro několik služeb. Orchestrace má smysl při doložených potřebách plánování, dostupnosti nebo týmů. Domácí server navíc vyžaduje posouzení proudu, konektivity, fyzického zabezpečení a vzdálené obnovy.

## Nácvik obnovy

Vytvořte čistý server podle konfigurace, obnovte data, ověřte uživatelský průchod a změřte RTO/RPO. Úspěšná zálohovací úloha nestačí. Ve stagingu bezpečně testujte certifikáty a zaplnění disku. Pokud tým nezvládá aktualizace nebo obnovu, přejděte na spravované služby; repliky nenahradí odpovědnost.

## Související rozhodnutí

[Bezpečnost, soukromí a závislosti](security.md) · [Hosting a cesta k migraci](hosting.md) · [Zdraví, obnova a náklady](operations.md)

## Primární zdroje

[docker-security](https://raw.githubusercontent.com/docker/docs/main/content/manuals/engine/security/_index.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml) · [opentofu](https://raw.githubusercontent.com/opentofu/opentofu/main/README.md)
