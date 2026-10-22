---
{
  "id": "playbook-mobile-backend",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Dodání backendu pro mobilní klienty

## Vhodnost a kontrakt podporovaných klientů

Tento profil použijte pro backend obsluhující nainstalované klienty, kteří mohou zůstat offline, opakovat zápisy a aktualizovat se v různou dobu. Zaznamenejte podporované verze klienta a API, maximální dobu offline, chráněná data povolená na zařízení, aktuálnost synchronizace, politiku odebrání přístupu a cíle obnovy. Tento návrh vytvořený agentem řeší dodání backendu a protokolu. Netvrdí, že byl implementován nativní klient, bezpečné úložiště zařízení, push integrace nebo platformní přístupnost.

Začněte modulárním API, kanonickými relačními daty a ohraničenou synchronizací. Aplikace fungující pouze online je jednodušší alternativou, pokud to uživatelský úkol dovoluje. Offline editace přidává trvalou identitu operací, řešení konfliktů, význam smazání a náklady podpory. Regionální umístění, specializovanou synchronizační infrastrukturu nebo partitioning přidávejte teprve po změření zpoždění synchronizace, četnosti konfliktů, soupeření zápisů, velikosti přenosů nebo geografické latence. Počet nainstalovaných zařízení sám o sobě migraci nespouští.

## Hranice a datový model

Oddělte `api/`, `policy/`, `domain/`, `sync/`, `contracts/` a `ops/`. Server vlastní kanonický stav a autorizaci. Identifikátor zařízení je atribut směrování a auditu, nikoli důkaz oprávnění uživatele. Přístup validujte při čtení, stahování synchronizace, nahrávání a obnově přihlašovacích údajů. Push zprávy mají signalizovat, že mohou být dostupná povolená data, nikoli obsahovat citlivý obsah záznamů.

Pro každou offline změnu definujte stabilní ID operace, autentizovaný subjekt, ID záznamu, výchozí revizi a zamýšlenou změnu. Výsledky deduplikace ukládejte v transakci, která změnu aplikuje. Opětovné použití ID s jinou změnou musí způsobit konflikt. Zastaralé editace detekujte revizemi řízenými serverem; hodiny zařízení nejsou vhodné jako jediná autorita pro pořadí obchodních změn.

Politiku konfliktů vybírejte podle domény. Editovatelná poznámka může zobrazit obě verze pro lidské sloučení. Rezervace zásob má odmítnout zastaralou podmínku nebo vynutit transakční invariant, nikoli potichu vybrat nejnovější čas hodin. Záznamy o smazání nebo ekvivalentní znalost musí přežít podporovanou dobu offline. Při expiraci synchronizačního kurzoru vyžadujte zdokumentovanou úplnou resynchronizaci, která potichu neobnoví smazané záznamy ani neztratí čekající lokální záměr.

## Dodávejte v bezpečném pořadí

1. Průzkum mapuje scénáře čtení, offline práce, editace a opětovného připojení, klasifikaci dat, podporované verze a příklady konfliktů. Lidský vlastník přijme politiku offline uchovávání a aktualizací.
2. Implementace vytvoří verzované API a syntetický klientský testovací nástroj před úplnou synchronizací. Přidejte deduplikaci operací, podmíněné aktualizace, stránkování a kurzory, mazání a pozorovatelný stav synchronizace s explicitními chybovými kontrakty.
3. Ověření spustí staré a nové konzumenty proti přechodným schématům a simuluje dvě zařízení, přerušení sítě, odebrání přístupu a obnovu. Vlastník vydání stanoví postupné zavádění a kritéria ukončení podpory klienta.

Předejte profil, schéma API a synchronizace, matici kompatibility, ADR konfliktů, příklady operací, požadavky na data v zařízení, migrační plán, pozorované výsledky kontraktů a obnovy, dobu podpory a jmenované vlastníky backendu a klienta. `examples/durable_service` může pomoci s lokálními experimenty perzistence. Není to mobilní synchronizační systém ani důkaz chování nativního zařízení; skutečné ověření klienta a platformy zůstává samostatným výstupem.

## Ověřujte nepřítomnost nezamýšlených účinků

Jednotkové testy použijte pro slučování a stavová pravidla, integrační pro transakce a autorizaci a kontraktní pro nejstarší podporovaný klient i kandidáta. Samotný štítek verze kompatibilitu nedokládá. Kontrolujte volitelná pole, zacházení s neznámými hodnotami výčtů, stránkování, chybové kódy, jednotky a chování smazaných záznamů. Jakmile existuje klient, použijte skutečné zařízení nebo platformní emulátor pro nativní cache, úložiště přihlašovacích údajů, práci na pozadí a push chování.

Nechte dvě syntetická zařízení upravit stejnou revizi offline a potom je připojte v obou pořadích. Orákulem je deklarovaný výsledek konfliktu se zachovaným záměrem uživatele, nikoli jen dvě úspěšné odpovědi. Přerušte upload po commitu databázové transakce, zopakujte jej a zkontrolujte kanonické záznamy: nesmí vzniknout další obchodní účinek. Zopakujte ID operace se změněným obsahem a vyžadujte konflikt. Smažte záznam, zatímco je druhé zařízení offline; zastaralá aktualizace jej nesmí oživit mimo deklarované pravidlo.

Odeberte přístup zařízení nebo relaci před obnovou přihlašovacích údajů a chráněnou synchronizací. Obnovovací cesta nesmí vrátit přístup; explicitně otestujte případnou zdokumentovanou toleranční dobu přístupového tokenu. Simulujte expiraci kurzoru a obnovu starší zálohy serveru: klienti musejí rozpoznat neslučitelnou historii synchronizace, sjednotit čekající operace a bezpečně se znovu synchronizovat. Měřte dobu obnovy, skutečnou ztrátu dat, zpoždění synchronizace, četnost konfliktů a přenos při omezených podmínkách špatné sítě. Netestované platformní chování ponechte viditelné.

## Zavádění, provoz a ukončení

Kontrakty a schéma rozšiřte před nasazením konzumentů; po celou publikovanou dobu podporujte smíšené verze klientů. Doplňujte data s checkpointy, validujte invarianty synchronizace a stará pole odstraňte až tehdy, když to dovolí politika podpory. Rollback backendu nemůže donutit instalované klienty k aktualizaci ani smazat stažená data. Obnovujte izolovaně, podle potřeby zaveďte novou epochu synchronizace nebo ekvivalentní značku obnovy a před opětovným otevřením zápisů sjednoťte operace.

Sledujte selhání podle verze klienta a API, nejstarší čekající operaci, četnost konfliktů, objem resynchronizací, zamítnutí obnovy přihlašovacích údajů a doručení notifikací bez logování chráněných dat. Vlastníky incidentů backendu a kompatibility klienta určete odděleně. Rozpočtujte úložiště, přenos, použití push poskytovatele, podporu starých verzí a nácviky obnovy. Produkční mezery zahrnují skutečnou identitu, úložiště zařízení, bezpečnost sítě, nativní chování na pozadí, push přihlašovací údaje a souhlas i uchovávání. Ukončení dává klientům srozumitelnou odpověď s dalším postupem při konci podpory, nabízí oprávněný export, podle možností dokončí čekající práci, zruší přihlašovací údaje a řeší uchované offline kopie podle dohodnuté politiky.

## Navazující rozhodnutí

[Kontrakty frontendu](frontend.md) · [Data a migrace](data.md) · [Bezpečnost](security.md) · [Strategie testování](testing-strategy.md)

## Primární zdroje

[owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-session](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Session_Management_Cheat_Sheet.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [semver](https://raw.githubusercontent.com/semver/semver/f99d5485190a47c0863949e7da810a5553e0ed4d/semver.md)
