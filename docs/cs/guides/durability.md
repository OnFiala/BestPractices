---
{
  "id": "durability",
  "language": "cs",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Odolnost a distribuovaná práce

## Určete, co musí přežít

Oddělte trvanlivost uložených dat, dostupnost služby a pokračování přerušené práce. Replika není záloha a úspěšné doručení zprávy nedokazuje právě jeden obchodní účinek. Pro každou schopnost dohodněte přijatelný časový rozsah ztráty dat (RPO), dobu obnovy (RTO) a pravidla porovnání vnějších účinků. Následující kontrakt vykonávání a testování je původní syntéza této knihovny; chování poskytovatele je nutné ověřit pro nasazenou verzi.

## Každému účinku přiřaďte stavový model

Odolná operace potřebuje stabilní ID, autentizovaného vlastníka, ověřená vstupní data, aktuální stav a pozorovatelný výsledek. Klíče idempotence omezte na tenanta a obchodní akci. Určete chování při opakovaném použití stejného klíče s odlišnými daty, během stále běžícího požadavku a po vypršení záznamů. Informace pro deduplikaci uchovávejte nejméně po celou podporovanou dobu opakování a přehrávání; u starší práce případně vyžadujte samostatný autorizovaný postup porovnání a opravy stavu.

Výsledek místní obchodní změny a ochranu unikátnosti uložte atomicky. Pokud má publikovaná událost odrážet potvrzenou změnu, může transakční outbox uložit obchodní změnu i událost společně. Předávací proces může po ztrátě potvrzení publikovat dvakrát; deduplikace proto musí být součástí vlastního trvalého zápisu spotřebitele. Nesouvisející volání externích služeb se tím nestávají transakčními.

Před opakováním roztřiďte selhání. Neplatné vstupy a zamítnutá autorizace vyžadují konečnou odpověď; přechodná selhání mohou připouštět omezené opakování. Za celkový časový limit a rozpočet opakování musí odpovídat jedna vrstva a musí počítat i s opakováním uvnitř SDK. Prodlevy a jitter snižují synchronizovaný tlak opakovaných požadavků; neospravedlňují opakování nebezpečného účinku. Zrušení po odeslání externího požadavku může zanechat neznámý výsledek, který je nutné porovnat se skutečným stavem.

## Příklad posloupnosti selhání

Uvažujte objednávku s poskytovatelem plateb a navazující událostí pro vyřízení:

| Přerušení | Požadované pozorovatelné chování |
| --- | --- |
| Před potvrzením transakce objednávky a outboxu | Ani jeden záznam není viditelný; opakování může bezpečně začít |
| Po potvrzení, před publikováním události | Předávací proces později najde čekající událost; žádná objednávka nezmizí |
| Po publikování, před potvrzením předávacímu procesu | Duplicitní doručení vyvolá jedinou zamýšlenou změnu u spotřebitele |
| Po úspěšné platbě, před přijetím odpovědi | Znovu použijte identitu operace podporovanou poskytovatelem nebo zjistěte a porovnejte jeho stav; nevytvářejte slepě další platbu |
| Během aktualizace workeru | Rozpracovaná práce pokračuje podle výslovně kompatibilního kontraktu stavu a verze nebo přejde k porovnání a nápravě |

Jde o požadavky přijetí, nikoli důkaz, že jimi prošel nějaký nasazený systém. Ve stagingu řízeně vyvolejte každé přerušení s kontrolovaným chováním poskytovatele, požadavek zopakujte a poté prohlédněte trvalý stav i záznamy poskytovatele. Ověřte úspěšnou obnovu i nevyřešené stavy vyžadující člověka. Při definici nezávislého očekávaného výsledku a balíčku důkazů se řiďte [strategií testování](testing-strategy.md).

## Provozujte přehrávání a obnovu

Chybné zprávy umisťujte do karantény s vlastníkem a důvodem. Omezte objem opakování a přehrávání; oprávnění k přehrání oddělte od běžného čtení. Operátor musí vědět, které schéma, rozsah pořadí a deduplikační okno platí. Kompenzace je nová obchodní akce; vrácení plateb, oznámení a fyzické vyřízení nemusí být vratné.

Obnovujte do izolovaného prostředí, porovnejte obchodní součty a externí účinky a teprve poté záměrně obnovte práci. Podle [plánu výkonnostních testů](performance-testing.md) ověřte obnovu při nahromaděné frontě a pomalých závislostech. Durable workflow engine má smysl, když snižuje prokázanou složitost orchestrace; jednoduššímu procesu s přijatelnou ruční obnovou může stačit transakční tabulka úloh. Ani jedno neodstraňuje potřebu záloh, odpovědnosti nebo testů kompatibility.

## Související rozhodnutí

[Data a migrace](data.md) · [Zdraví a obnova](operations.md) · [Volba architektury](architecture.md) · [Strategie testování](testing-strategy.md)

## Primární zdroje

[postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [durable-workflows](https://raw.githubusercontent.com/temporalio/temporal/e8ee627110a98501103827745aab18aedf312dd0/README.md) · [azure-retry](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/retry-content.md) · [azure-cqrs](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/cqrs.md) · [azure-outbox](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/databases/guide/transactional-out-box-cosmos.md) · [azure-idempotent-consumer](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/idempotent-consumer.md)
