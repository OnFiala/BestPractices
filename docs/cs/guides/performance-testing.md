---
{
  "id": "performance-testing",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Výkonnostní a zátěžové testování

## Vyberte otázku selhání

Výkonnostní test má odpovídat na rozhodnutí projektu: zda vydání splňuje cíl latence, zda se fronta zotaví po nárazu, kde přestává stačit kapacita nebo zda spotřeba zdrojů roste v čase. Počet registrovaných uživatelů ani jeden rychlý požadavek na tyto otázky neodpovídají.

| Podoba testu | Kdy ji použít | Zkoumaný výsledek |
| --- | --- | --- |
| Malý smoke test | Ověření zátěže, podkladů, oprávnění a měření před spotřebováním zdrojů | Požadavky vykonávají zamýšlenou práci; kontroly výsledků i zastavení fungují |
| Reprezentativní zátěž | Ověření běžného provozu a dohodnuté očekávané špičky po relevantní změně | Užitečná propustnost, krajní latence, chyby a spotřeba zdrojů splňují cíl projektu |
| Stresový test | Zkoumání degradace nad očekávanou zátěží v omezeném experimentu | Řízení přijímání práce, chyby, integrita dat a obnova mají záměrně navržené chování |
| Nárazový test | Spuštění produktu, harmonogram nebo vnější událost mohou skokově zvýšit příchody | Růst fronty, zpoždění škálování, odmítání a obnova po nárazu |
| Dlouhodobý test | Úniky zdrojů, obměna spojení, expirace nebo periodická práce se mohou hromadit | Vývoj zdrojů a latence zůstává vysvětlitelný po celý relevantní životní cyklus |
| Kapacitní test nebo hledání bodu zlomu | Plánování potřebuje pozorovaný limit pevné konfigurace | První porušený cíl, omezující zdroj, bezpečná rezerva a postup obnovy |

Názvy se mezi nástroji liší. Zaznamenejte skutečný průběh zátěže a cíl, aby další agent experiment zopakoval. Stresový test není automaticky nejlepší další krok; neúspěšný smoke test potřebuje nejprve diagnostiku.

## Modelujte skutečnou práci

Skladbu transakcí, vzorce příchodů, velikosti vstupů a dat, poměr čtení a zápisů, stav cache, nerovnoměrnost tenantů, práci na pozadí a chování závislostí odvozujte z měření nebo výslovných předpokladů. Zachovejte rozdíl mezi obchodní transakcí a jejími jednotlivými HTTP požadavky. Před zobecněním výsledků vysvětlete rozdíly testovacího prostředí vůči produkci.

Model plánování volte záměrně. Uzavřený model udržuje skupinu virtuálních uživatelů, kteří před další iterací čekají na dokončení aktuální. Když se systém zpomalí, nabídnutá práce může klesnout. Otevřený model rychlosti příchodů plánuje novou práci nezávisle na dokončení a lépe zastupuje nezávislé příchody. Ani jeden automaticky neodpovídá každému produktu. Zaznamenejte prodlevy uživatelů a rozlišujte nastavenou rychlost, skutečně zahájenou práci, dokončenou propustnost a vynechané iterace.

Zajistěte, aby generátor, jeho síť nebo přístupové údaje nebyly úzkým místem. Saturaci generátoru sledujte odděleně. Přetížený generátor, který přestane posílat práci, může vytvářet dojem zdravého cíle. Zahřátí, cache, pooly spojení, autoscaling a úlohy na pozadí mohou měnit výsledky; zahrňte důležité stavy místo jejich ukrytí v jediném souhrnu.

## Před spuštěním určete limity

Zadání testu agenta musí uvést vlastněný cíl, prostředí, povolené cesty a účty, nejvyšší provoz, souběžnost, dobu běhu, limity zdrojů a útraty, monitoring, úklid a operátora schopného běh zastavit. Výchozí volbou jsou izolovaná prostředí a syntetická data. Bez výslovného oprávnění s vymezeným rozsahem a limitů poskytovatele nesměrujte stresový provoz do produkce, ke třetím stranám, sdíleným tenantům ani placeným modelovým endpointům.

Oddělte prahy přijetí a podmínky přerušení. Přijetí měří požadované chování služby; podmínky přerušení chrání lidi, data, sdílené systémy a rozpočet. Plánovaný stresový test může překročit běžný cíl latence, ale stále musí skončit na dohodnuté bezpečnostní hranici. Určete, jak přerušení zastaví generátor a jak bude rozpracovaná práce dokončena nebo zrušena. Timeout úlohy sám není stropem účtovaných nákladů.

Ověřte, jak spouštěč vykazuje selhání. Například k6 zaznamenává neúspěšné kontroly jako metriky; nastavte prahy tak, aby porušení podmínky přijetí způsobilo neúspěšný běh. Periodické vyhodnocování přerušení v cloudu nevynucuje limity zdrojů nebo útraty okamžitě; podle potřeby nastavte limity také na hranicích služeb a účtů.

Při kapacitním experimentu omezte autoscaling nebo zdokumentujte jeho ohraničenou konfiguraci. Jinak test může měřit růst útraty místo kapacity pevně daného systému. Pro nákladné externí účinky používejte sandboxy poskytovatelů nebo řízené náhrady a uveďte z toho plynoucí omezení.

## Měřte a interpretujte

Sledujte úspěšné obchodní operace, kategorie chyb, latenci p50/p95/p99 tam, kde ji velikost vzorku podporuje, propustnost, souběžnost, stáří a délku fronty, využití spojení, CPU, paměť, úložiště a relevantní cenu. Rozlišujte kritické cesty a tenanty; rychlý běžný endpoint může v globálním percentilu skrýt selhávající platbu. Do analýzy zahrňte i neúspěšné operace a timeouty, nikoli pouze úspěšné odpovědi.

Uchovejte dostatečné původní časové údaje a konfiguraci pro reprodukci vypovídajícího výsledku. Malé vzorky činí odhady krajních latencí nestabilními; pokud na nejistotě záleží, opakujte řízená porovnání. Než degradaci přisoudíte změně kódu, propojte ji s měřením zdrojů a závislostí. Rozdíl mezi dvěma nekontrolovanými prostředími není prokázaná regrese.

Pro dlouhodobý test zvolte dobu pokrývající ohrožený životní cyklus, například obnovu tokenů, plánované úlohy nebo růst bufferu; nekopírujte univerzální počet hodin. U kapacitního testu oznamujte změřený limit při zkoušené konfiguraci a zátěži, nikoli příslib pro všechny budoucí uživatele.

## Obnova je součást experimentu

Snižte zátěž a sledujte, zda se latence, fronty a spotřeba zdrojů vrátí do použitelného stavu v dohodnutém okně obnovy. Ověřte konzistenci dat, duplicitní účinky a zpožděné úlohy. Systém, který bezpečně odmítá přetížení, ale nikdy nevyprázdní nahromaděnou práci, obnovu neprokázal. Odstraňte testovací podklady a potvrďte, že neúmyslně nezůstal aktivní žádný plánovaný generátor ani účtovaný zdroj.

Zaznamenejte výsledek, meze spolehlivosti závěru, hypotézu úzkého místa a rozhodnutí: přijmout změřenou rezervu, optimalizovat konkrétní cestu, změnit pravidla přijímání práce nebo vyhodnotit další kapacitu. Znovu testujte změněnou hypotézu. Výkonnostní brány udržujte přiměřené riziku a dostatečně stabilní pro užitečnou zpětnou vazbu k vydání.

## Důkazy a související rozhodnutí

Dokumentace Grafana k6 vysvětluje podoby zátěže, otevřené a uzavřené plánování, prahy a řízení přerušení. Výše uvedená pravidla plánování, přijetí a obnovy jsou původní syntéza této knihovny; příkladové prahy a hodnoty provozu z dokumentace dodavatele nejsou požadavky projektu.

[Strategie testování](testing-strategy.md) · [Škálování podle měření](scaling.md) · [Zdraví a obnova](operations.md) · [Odolnost](durability.md) · [Kontroly kvality](quality.md)

## Primární zdroje

[k6-test-types](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/testing-guides/test-types/_index.md) · [k6-open-vs-closed](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/using-k6/scenarios/concepts/open-vs-closed.md) · [k6-thresholds](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/using-k6/thresholds.md) · [k6-stress-testing](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/testing-guides/test-types/stress-testing.md) · [k6-spike-testing](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/testing-guides/test-types/spike-testing.md) · [k6-soak-testing](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/testing-guides/test-types/soak-testing.md) · [k6-breakpoint-testing](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/testing-guides/test-types/breakpoint-testing.md)
