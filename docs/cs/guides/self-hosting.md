---
{
  "id": "self-hosting",
  "language": "cs",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Provoz vlastních serverů

## Vymezte topologii a její limity

Malá veřejná služba může mít na vstupní hranici reverzní proxy s TLS, aplikaci v privátní síti a databázi dosažitelnou jen oprávněnými aplikačními nebo správcovskými identitami. Umístění v síti doplňuje autentizaci; nenahrazuje autorizaci. Oddělte produkci od experimentů a pro správu zajistěte auditovanou, omezenou přístupovou cestu. Jeden stroj zůstává jedinou oblastí selhání, i když na něm běží více kontejnerů.

Následující minimální provozní dohoda je doporučení knihovny vycházející z dokumentace kontejnerové bezpečnosti a obnovy. Přizpůsobte ji platformě a dopadu; nejde o zabezpečenou konfiguraci serveru připravenou k nasazení.

| Povinnost | Co zaznamenat a ověřit |
| --- | --- |
| Správa | Vlastník, omezený přístup, postup odebrání oprávnění a důkaz zamítnutého přístupu |
| Aktualizace softwaru | Podporovaný OS a runtime, vlastník aktualizací, servisní okno a artefakt pro obnovu |
| Izolace zdrojů | Limity CPU, paměti a disku, kapacitní alarmy a chování při vyčerpání |
| Tajné údaje | Způsob předávání a rotace; oddělené identity nasazování, migrace a aplikace |
| Persistence | Výslovné datové svazky, rozsah záloh, šifrování a přístup ke klíčům, retence |
| Veřejná hranice | Obnova TLS, povolené porty, autentizace a bezpečné chybové odpovědi |
| Obnova | Záloha mimo hostitele, poslední úspěšná obnova, RTO/RPO a kontakt pro incidenty |

Kde je to možné, upřednostněte samostatný účet pro zálohy nebo jinou oblast selhání. Záloha na stejném zapisovatelném disku může selhat se serverem nebo ji může smazat stejná kompromitovaná identita. Ověřte, že obnova nezávisí na přístupech uložených pouze na ztraceném hostiteli.

## Nasazujte opakovatelnou jednotku

Používejte infrastrukturu jako kód a nasazovaný obraz připněte digestem. Stav aplikace ukládejte do výslovně spravované persistence, nikoli do náhodné vrstvy kontejneru. Nevystavujte Docker socket aplikaci ani agentovi a nepovažujte kontejner za silný sandbox pro nepřátelský kód. Oprávnění a zdroje omezte na potřeby úlohy.

Compose může vyhovovat několika službám s pochopeným chováním při selhání a aktualizaci. Orchestraci přijměte, když požadavky plánování, dostupnosti nebo týmů ospravedlní její provozní zátěž. Více replik na jednom stroji tomuto stroji nezajistí vysokou dostupnost. Domácí server navíc potřebuje posouzení napájení, konektivity, fyzického přístupu a obnovy mimo původní lokalitu.

## Nácvik obnovy a selhání

Na samostatném testovacím stroji znovu vytvořte hostitele podle zaznamenané konfigurace a obnovte nedávnou zálohu. Vypněte skutečné e-maily, platby a další externí účinky. Než obnovu prohlásíte za úspěšnou, ověřte reprezentativní uživatelský průchod, oprávnění tenantů, obchodní součty a čekající práci. Naměřenou dobu obnovy a skutečné časové okno ztráty dat porovnejte s dohodnutými cíli.

Před významnou změnou hostingu využijte [výkonnostní testování](performance-testing.md) k ověření omezeného přetížení a obnovy v autorizovaném prostředí. Bezpečně otestujte tlak na disk, zastavenou aplikaci, nedostupnou databázi a obnovu certifikátu. Pomocí [bezpečnostního testování](security-testing.md) ověřte, že z veřejné hranice nejsou otevřené správcovské a databázové porty a že odebrané přístupy nefungují.

Test projde jen tehdy, když chování z pohledu uživatele a zaznamenaný stav splňují podmínky přijetí. Závisí-li obnova na nezdokumentovaných ručních krocích, zapište je a nácvik zopakujte. Když odpovědné osoby nezvládají aktualizace, reakci nebo obnovu, přejděte na spravovanou službu nebo zmenšete rozsah; další technika nedostatek odpovědnosti nevyřeší.

## Související rozhodnutí

[Bezpečnost](security.md) · [Hosting](hosting.md) · [Provoz](operations.md) · [Výkonnostní testování](performance-testing.md) · [Bezpečnostní testování](security-testing.md)

## Primární zdroje

[docker-security](https://raw.githubusercontent.com/docker/docs/4d64a8e4f0a59967fc0b391120d54a90e9ccb60d/content/manuals/engine/security/_index.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [opentofu](https://raw.githubusercontent.com/opentofu/opentofu/ec773ed37be4d07e00d4a2fbb237d0c0fe1ca3ce/README.md)
