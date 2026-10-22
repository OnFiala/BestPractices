---
{
  "id": "hosting",
  "language": "cs",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Hosting a cesta k migraci

## Porovnejte úplnou odpovědnost

Začněte klasifikací a umístěním dat, charakterem provozu, cíli obnovy, dostupnými provozními lidmi a rozpočtem. Následující porovnání je původní výběrová pomůcka knihovny. Aktuální údaje o regionech, kvótách, podpoře a ceně skutečného nasazení musí dodat dokumentace produktu; kategorie produktu není zárukou služby.

| Varianta | Vhodné použití | Ověřované náklady a odpovědnost |
| --- | --- | --- |
| Statický hosting/CDN | Veřejná dokumentace a neměnné soubory | Limity sestavení, pravidla cache, kontrola domény a nepřítomnost soukromých výstupů |
| Spravovaná aplikační platforma | Malý tým dodávající aplikaci | Podporovaná běhová prostředí, síť, rozsah záloh, export a odchozí přenosy |
| Spravované funkce | Ohraničené nárazové operace | Limity běhu, studené starty, souběžnost, pooly spojení a opakování |
| VPS nebo kontejnerový hostitel | Předvídatelná práce s odpovědným provozovatelem | Aktualizace, certifikáty, dohled, zálohy, doba obnovy a volná kapacita |
| Spravovaný Kubernetes | Více zátěží s odůvodněnou potřebou plánování a izolace | Pravidla clusteru a úloh, aktualizace, síť, kapacita a schopnost řešit incidenty |

Spravované služby přebírají vybrané provozní úkoly; nepřebírají odpovědnost za autorizaci aplikace, klasifikaci dat ani důkazy obnovy. Porovnávejte výpočetní prostředky, úložiště, odchozí přenosy, pozorovatelnost, podporu, placená volání modelů a lidský čas. Zahrňte cenu špiček i neúspěšných a opakovaných požadavků, nejen měsíční odhad nečinného systému.

## Zaznamenejte rozhodnutí o hostingu

Uveďte vlastníka služby, oblasti selhání, podporované verze běhových prostředí, identitu nasazování a digest artefaktu. Určete oddělení produkce od experimentů, způsob předávání tajných údajů, autentizaci veřejného vstupu a soukromá datová úložiště. Kvóty a zdokumentované možnosti obnovy porovnejte s RTO/RPO aplikace. Počítejte také se zablokováním účtu poskytovatele, nejen s výpadkem regionu.

Konfiguraci udržujte mimo aplikaci a infrastrukturu opakovatelnou. Zachovejte kontrolu nad doménou a formátem exportu dat. Vyjmenujte funkce specifické pro poskytovatele a přijatou cenu migrace; přenositelnost je kompromis, nikoli požadavek odstranit všechny spravované služby. I platforma s automatickými zálohami potřebuje nácvik obnovy na úrovni aplikace.

## Prokažte zvolenou možnost

Před prvním produkčním vydáním nasaďte izolované prostředí a dokončete skutečný uživatelský průchod. Otestujte zamítnutý přístup, rotaci přístupů, neúspěšné nasazení a obnovu dat. Pomocí [výkonnostních testů](performance-testing.md) určete udržitelný provoz a pomocí [bezpečnostních testů](security-testing.md) ověřte vstupní hranice, tenanty a identity. Zaznamenejte nasazenou verzi, relevantní nastavení platformy a pozorované výsledky; dashboard s nápisem „zdravé“ nestačí.

Pro ilustraci porovnejte spravovanou aplikaci a databázi s jedním VPS pro stejný malý SaaS. VPS může mít nižší účet za infrastrukturu, ale vyžaduje vlastníka aktualizací a obnovy. Rozhodujte podle změřených nákladů a schopnosti plnit provozní dohodu, nikoli podle levnější hlavní ceny. Příklad je rozhodovací cvičení, ne naceněné nebo výkonnostně ověřené referenční nasazení.

## Odchod a obnova

Export a import nacvičte na kopii dat odpovídající produkční struktuře. Ověřte počty záznamů, obchodní součty, mapování identit, tajné údaje, objektové úložiště a stav workerů. Naplánujte autoritativního zapisovatele během přepnutí, pozorovací okno a podmínky zastavení migrace provozu. Původní cestu udržujte obnovitelnou jen po dobu, kdy její data zůstávají v souladu se zvoleným plánem obnovy.

Návrat DNS nevrátí zápisy přijaté novým systémem. Po přepnutí může návrat vyžadovat pozastavení zápisů, porovnání a sladění stavu nebo dopřednou opravu. Před migrací se závažnými důsledky tento plán otestujte. Web této knihovny používá statický hosting; publikace Pages nenasazuje její místní MCP server.

## Související rozhodnutí

[Vlastní servery](self-hosting.md) · [Škálování](scaling.md) · [Provoz](operations.md) · [Výkonnostní testování](performance-testing.md) · [Bezpečnostní testování](security-testing.md)

## Primární zdroje

[docker-security](https://raw.githubusercontent.com/docker/docs/4d64a8e4f0a59967fc0b391120d54a90e9ccb60d/content/manuals/engine/security/_index.md) · [kubernetes](https://raw.githubusercontent.com/kubernetes/website/bc7f3479bc8b0af48097b155c22c8d58e8e1afe4/content/en/docs/concepts/architecture/_index.md) · [opentofu](https://raw.githubusercontent.com/opentofu/opentofu/ec773ed37be4d07e00d4a2fbb237d0c0fe1ca3ce/README.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml)
