---
{
  "id": "durability",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Odolnost a distribuovaná práce

## Co musí přežít

Oddělte uchování dat, dostupnost služby a pokračování rozpracované úlohy. Replika není záloha; fronta negarantuje právě jeden obchodní účinek. Pro schopnosti produktu určete přijatelnou ztrátu dat (RPO) a dobu obnovy (RTO). Jde o obchodní rozhodnutí, ne vlastnost názvu nástroje.

## Spolehlivé vykonávání

- Operace má stabilní klíč idempotence v rozsahu tenanta a akce. Výsledek nebo změnu stavu ukládejte s unikátním omezením; definujte expiraci a odlišný payload pod stejným klíčem.
- Omezte timeouty a retry. Opakujte jen vhodná selhání s exponenciálním odstupem, jitterem a celkovým termínem; validační chyby mají vlastní cestu.
- Obchodní stav a outbox zapište v jedné transakci. Publikování může vytvořit duplicity; odběratelé deduplikují a řeší pořadí ve vymezeném rozsahu.
- U dlouhé práce ukládejte průběh. Zaznamenejte zrušení, kompenzaci a ruční nápravu. Kompenzace je nová obchodní akce, nikoli zaručené vrácení vnějšího účinku.
- Chybné zprávy izolujte; replay musí být oprávněný, pozorovatelný, omezený a odolný duplicitám. Určete kompatibilitu schématu a dobu uchování deduplikace.

## Příklad selhání

Objednávka se uloží, proces však spadne před publikováním události. Outbox pokračuje. Když platba projde, ale odpověď se ztratí, použijte idempotenci poskytovatele a nejprve ověřte jeho stav. Místní klíč sám nezajistí jedinou externí platbu.

## Ověření a jednoduchost

Ukončete worker před i po trvalém zápisu, doručte zprávu dvakrát a mimo pořadí. Obnovte izolované prostředí a porovnejte součty. Workflow engine přidejte, když snižuje prokázanou složitost selhání; ověřte aktualizaci běžících úloh. Pokud lze práci ručně opakovat, může stačit transakční tabulka úloh.

## Související rozhodnutí

[Data, smlouvy a migrace](data.md) · [Zdraví, obnova a náklady](operations.md) · [Volba a propojení architektur](architecture.md)

## Primární zdroje

[postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/mvcc.sgml) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml) · [durable-workflows](https://raw.githubusercontent.com/temporalio/temporal/main/README.md)
