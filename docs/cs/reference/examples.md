---
{
  "id": "examples",
  "language": "cs",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Referenční cesty projektů

## Šest návrhových profilů, nikoli nasazené aplikace

Tyto původní profily propojují architektonické volby s prvním pozorovatelným důkazem. Jsou ilustrativními výchozími body, nikoli sestavami ověřenými benchmarkem, certifikacemi shody nebo výsledky dokončených testů. [Strojově čitelné návrhové profily](https://github.com/OnFiala/BestPractices/blob/main/data/blueprints.json) obsahují hranice, obnovu, signály ke změně a plánovaná testovací zadání. Při přijetí připněte revizi repozitáře.

| Projekt | Výchozí návrh | První důkaz | Kdy přehodnotit |
| --- | --- | --- | --- |
| Veřejný web | Statické sestavení, CDN a historie obsahu | Přístupná navigace, žádný soukromý výstup, obnova předchozího artefaktu | Objeví se potřeba důvěryhodných zápisů nebo změřené limity publikování |
| SaaS | Modulární aplikace, transakční databáze a worker s limity | Izolace tenantů, sjednocení stavu plateb a obnova | Objeví se změřené soupeření o prostředky nebo nezávislá odpovědnost za doménu |
| Interní nástroj | SSO, malá aplikace, integrace s omezeným rozsahem a audit | Uživatelé s odebraným přístupem nemohou číst ani exportovat; odložená práce má dohledatelnou odpovědnost | Rozcházejí se vlastníci nebo požadavky na spolehlivost |
| AI aplikace | Adaptér modelu, autorizované načítání a evaluační sada | Odepřené dokumenty nevstoupí do kontextu modelu; selhání zůstávají ohraničená | Změní se vyhodnocená kvalita, náklady, latence nebo požadavky na umístění dat |
| Agentní automatizace | Trvalá evidence běhů, workery s limity a nástroje s omezeným rozsahem | Duplicity, zastaralá schválení ani rozpočtové zastavení neumožní překročit pravomoc | Nezávislé nástroje nebo zátěže potřebují oddělené hranice selhání |
| Mobilní aplikace a backend | Klientská cache, kompatibilní API a explicitní synchronizační pravidla | Obnova po práci offline, konflikty a podpora starých klientů | Změřený tlak synchronizace nebo geografie odůvodní změnu návrhu |

## Veřejný web

Předpokládejte veřejný autorský obsah a žádné uživatelsky specifické zápisy na serveru. Sestavte neměnný artefakt a zveřejněte jej prostřednictvím posouzené identity pro nasazování. Před vydáním projděte navigaci a vyhledávání v každém podporovaném jazyce pomocí klávesnice a úzkého zobrazení. Zkontrolujte, že generovaný výstup a vyhledávací index neobsahují soukromá data; přihlášení na straně klienta veřejné soubory neochrání. V testovacím prostředí nasaďte známý předchozí artefakt a ověřte skutečnou routu. Chráněné API přidejte, až když produkt potřebuje důvěryhodné zápisy; token pro statické sestavení neměňte na veřejný přihlašovací údaj v prohlížeči.

## SaaS s platbami

Předpokládejte více tenantů a poskytovatele odpovědného za účtování. Každou operaci svažte s autentizovaným tenantem; lokální obchodní přechody ukládejte se stabilní identitou operace. Před změnou autorizace nebo účtování vyzkoušejte pokusy o přístup k objektům a exportům jiných tenantů, duplicitní odeslání a ztracenou odpověď poskytovatele. Prohlédněte lokální záznamy i záznamy poskytovatele namísto důvěry v samotný HTTP stav, abyste doložili jeden zamýšlený obchodní výsledek nebo explicitní nevyřešený stav vyžadující sjednocení. Obnovte izolovanou kopii, sjednoťte stav plateb a čekající práci spouštějte záměrně. Služby zavádějte pouze pro změřený přínos odpovědnosti, izolace nebo kapacity.

## Interní nástroj

Předpokládejte poskytovatele identity organizace a jednu externí obchodní integraci. SSO stanovuje identitu; aplikace stále autorizuje každou akci a export. Odebrání přístupu testujte přes aktuální relaci i úlohu ve frontě v dohodnutém časovém okně odvolání. Znepřístupněte nadřazenou službu a poté ověřte, že čekající práce zůstává viditelná a opakuje se pouze podle svých pravidel. Sjednocení stavu používá stabilní identifikátor operace, aby obsluha zjistila, zda zápis v externí službě nastal. Auditním záznamům určete vlastníka a pravidlo uchovávání; samotný přístup do firemní sítě není autorizací.

## AI aplikace

Předpokládejte ohraničenou funkci modelu, která pro autentizovaného uživatele načítá dokumenty. Autorizaci dokumentů uplatněte dřív, než obsah vstoupí do výsledků vyhledání nebo kontextu modelu, a zajistěte účinnost odebrání přístupu a mazání napříč indexy a cache. Před změnou modelu, promptu, cesty načítání nebo pravidel spusťte vyhrazené reprezentativní a útočné evaluace s explicitním hodnocením a lidským posouzením tam, kde je potřebný úsudek. Zahrňte odepřené dokumenty, zdržení se odpovědi, prompt injection a časový limit poskytovatele. Vedle latence a nákladů měřte úspěšnost a oporu odpovědí ve zdrojích; věrohodný jazyk není správnost. Bezpečný náhradní režim může funkci vypnout nebo nabídnout běžné autorizované vyhledávání.

## Agentní automatizace

Předpokládejte, že úlohy ve frontě mohou způsobit významné zápisy nástroji. Evidence běhů zaznamenává identitu úkolu, autorizovaný rozsah, vazbu schválení, pokusy a pozorovatelný výsledek. Otestujte duplicitní úkol, propadlé schválení, změnu akce po schválení, nepřátelské instrukce z načtených zdrojů a vyčerpaný rozpočet. Vynucovací hranice musí zastavit neoprávněná volání nástrojů nezávisle na spolupráci modelu. Pro testy selhání používejte simulované nebo izolované externí cíle. Po pádu před pokračováním zjistěte a sjednoťte, zda účinek nastal; restart workeru nesmí slepě zopakovat nevratnou akci.

## Mobilní aplikace a backend

Předpokládejte, že všichni klienti nemohou okamžitě aktualizovat a mohou upravovat data offline. Autorizaci a kanonický stav udržujte na serveru, potřebná lokální data v chráněném úložišti vhodném pro platformu a konflikty řešte explicitním pravidlem. Před vydáním testujte nejstaršího podporovaného klienta proti novému API, přerušenou synchronizaci, opakované nahrání a soupeřící offline úpravy. Ověřte, že odvolání zařízení blokuje obnovení relace a následné chráněné operace podle dokumentovaného kontraktu relace. Nepředpokládejte, že odvolání přístupu vymaže data již stažená do zařízení. Regionální nebo rozdělená synchronizace vyžaduje důkazy o četnosti konfliktů, latenci a nákladech obnovy.

## Dejte agentovi testovatelný úkol

Pro zvolený profil dohodněte s lidským vlastníkem zátěž, SLO/RTO/RPO, pravidla dat a rozpočet. Plánované případy převeďte do testů skutečné technologické sestavy podle [strategie testování](../guides/testing-strategy.md), [plánu výkonnostních testů](../guides/performance-testing.md) a [plánu bezpečnostních testů](../guides/security-testing.md). Zaznamenejte přípravu, podnět, pozorovatelné kritérium správnosti, negativní případy, podmínky zastavení a uchované důkazy. Agent musí odlišit navržený test od provedeného výsledku a nahlásit chybějící předpoklad místo vymyšleného úspěchu.

## Související rozhodnutí

[Zavedení](../guides/adoption.md) · [Architektura](../guides/architecture.md) · [Agenti](../guides/agents.md) · [Frontend](../guides/frontend.md) · [Strategie testování](../guides/testing-strategy.md)

## Primární zdroje


[owasp](https://raw.githubusercontent.com/OWASP/ASVS/2b47a9dd16760ee484a6672d197f1f7e25d9c632/README.md) · [openai-agents](https://raw.githubusercontent.com/openai/openai-agents-python/841dfdd938bfd4ca052475eb76d6245a356868e0/docs/agents.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [wcag](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/index.html) · [azure-architecture-styles](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/guide/architecture-styles/index.md) · [azure-retry](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/retry-content.md) · [azure-idempotent-consumer](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/idempotent-consumer.md)
