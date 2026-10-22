---
{
  "id": "data",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Data, smlouvy a migrace

## Explicitní invarianty

Úložiště vybírejte podle přístupů, konzistence, retence a obnovy. Relační databáze je silný výchozí kandidát pro transakční data; object storage pro velké soubory. Vyhledávací indexy a cache jsou odvozené pohledy, pokud není určeno jinak. Před frameworkem definujte identifikátory, vlastnictví, unikátnost a mazání.

Invarianty chraňte omezeními a transakcemi. Rozumějte izolaci a bezpečně opakujte serializační chyby. Autorizace tenanta doprovází čtení i zápis; testujte cizí identifikátory, exporty a úlohy na pozadí. Retence platí také pro logy, analytiku a zálohy.

## Rozšířit, migrovat, odstranit

Nejdříve přidejte kompatibilní schéma. Nasazujte čtečky a zapisovače tolerující obě podoby, doplňujte data v omezených obnovitelných dávkách, měřte soulad a starou podobu odstraňte až po migraci spotřebitelů. Nacvičte realistický objem a sledujte zámky. Návrat kódu nevrátí destruktivní migraci; potřebujete dopřednou opravu a ověřenou obnovu.

## Ověření

Testujte starou/novou aplikaci, duplicity, souběh, export/import a obnovu. Měřte RPO/RTO. Veřejné smlouvy verzujte při potřebě koordinace; neměňte tiše jednotky, nullability ani význam. Další databázi přidejte jen pro změřený požadavek, který ospravedlní provoz a konzistenci.

## Související rozhodnutí

[Odolnost a distribuovaná práce](durability.md) · [Bezpečnost, soukromí a závislosti](security.md) · [Škálování podle měření](scaling.md)

## Primární zdroje

[postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/mvcc.sgml) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml) · [owasp](https://raw.githubusercontent.com/OWASP/ASVS/master/README.md)
