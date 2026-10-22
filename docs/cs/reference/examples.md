---
{
  "id": "examples",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Referenční cesty projektů

## Šest konkrétních cest

| Projekt | Počáteční architektura | První důkaz | Signál rozšíření |
| --- | --- | --- | --- |
| Veřejný web | Statický build, CDN, obsah v Gitu | Hledání, klávesnice, návrat obsahu | Důvěryhodný zápis vyžaduje API |
| SaaS | Modulární aplikace, relační databáze, worker | Izolace tenantů, sladění plateb, obnova | Změřený konflikt nebo samostatné týmy |
| Interní nástroj | SSO, malá aplikace, audit | Odebraný účet nečte/neexportuje | Oddělená odpovědnost integrací |
| AI aplikace | API, adaptér modelu, oprávněný retrieval | Podložené odpovědi, zamítnuté dokumenty, timeout | Změřená kvalita/cena nebo izolace |
| Agentní automatizace | Fronta, omezený worker, evidence běhů, omezené nástroje | Duplicita, limit rozpočtu, schválení zápisu | Nezávislé zátěže potřebují vlastníky |
| Mobil + backend | UI, verzované API, místní cache | Offline změny, konflikty, starý klient | Změřený problém synchronizace či latence |

`data/blueprints.json` obsahuje hranice, příklady přijetí, obnovu a signály migrace. Jde o návrhové vzory, ne nasazené aplikace. Přeneste vhodný profil a jeho příklady do skutečných testů svého stacku.

Mobilní klienti neaktualizují současně. Preferujte aditivní API, obnovitelnou synchronizaci, explicitní konflikty, revokaci zařízení a bezpečné úložiště platformy. AI retrieval zachovává oprávnění i mazání; přesvědčivá odpověď nedokazuje správnost. Firemní síť nenahrazuje autorizaci interního nástroje.

Před spuštěním dohodněte cenu, SLO, umístění dat a obnovu s člověkem. Malý tým může pro všechny cesty použít spravovanou platformu; smlouvy a povinnosti zůstávají rozdílné.

## Související rozhodnutí

[Použití knihovny v projektu](../guides/adoption.md) · [Volba a propojení architektur](../guides/architecture.md) · [Člověk řídí, agent vykonává](../guides/agents.md) · [Architektura frontendu a smlouvy](../guides/frontend.md)

## Primární zdroje

[owasp](https://raw.githubusercontent.com/OWASP/ASVS/master/README.md) · [openai-agents](https://raw.githubusercontent.com/openai/openai-agents-python/main/docs/agents.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml) · [wcag](https://raw.githubusercontent.com/w3c/wcag/main/guidelines/index.html)
