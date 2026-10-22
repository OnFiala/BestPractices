---
{
  "id": "agents",
  "language": "cs",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Člověk určuje směr, agent vykonává

## Ohraničené delegování

Zadání úkolu obsahuje uživatelský výsledek, relevantní identifikátory průvodců, omezení, povolené soubory a nástroje, akceptační příklady, rozpočet a podmínky zastavení. Člověk odpovídá za architekturu a riziko; agent zkoumá a implementuje. Oddělte odpovědnost implementátora, ověřovatele a lidského posuzovatele, i když několik průchodů provádí jeden model. Opakování stejného závěru není nezávislým důkazem.

Sama knihovna používá tento model údržby agenty a otevřeně uvádí jejich autorství. Všechna počáteční doporučení a překlady zůstávají návrhy. Posuzovatel musí rozlišovat důkazy od místního technického úsudku; sebejistota modelu nenahrazuje ani jedno.

Responses API používejte přímo, pokud potřebujete mít pod kontrolou vykonávací smyčku; Agents SDK zvažte tehdy, když jeho orchestrace, nástroje a předávání úloh řeší doloženou potřebu. Začněte jedním agentem. Paralelní agenti potřebují nezávislé úkoly, výslovně určenou odpovědnost za zápis, koordinaci slučování a omezené celkové náklady.

## Řídicí vrstva

Nastavte autorizaci na úrovni nástrojů, přihlašovací údaje s omezeným rozsahem, časové limity, maximální počet iterací, rozpočty tokenů a nákladů a auditovatelné identifikátory běhů. Ochranná pravidla zlepšují chování, ale nenahrazují autorizaci ani izolaci. Zdroje a odpovědi nástrojů považujte za data, která mohou obsahovat prompt injection. Zastavte se při rozporných instrukcích, nedostupných předpokladech, neočekávaných destruktivních účincích nebo selhání povinných kontrol.

## Akceptace a vyhodnocování

Vyžadujte diff, provedené kontroly, nevyřešené předpoklady a poznámky k obnově. Úkoly vyhodnocujte na reprezentativních příkladech včetně útočných vstupů a chybových cest. Měřte úspěšnost úkolu, lidské opravy, uniklé chyby, latenci a náklady, nikoli objem kódu. Pro změny promptů, modelů, nástrojů a pravidel udržujte malou regresní sadu. Novější model automaticky nepovyšujte jen kvůli změně názvu nebo data vydání.

Testy vybírejte explicitně podle [strategie testování](testing-strategy.md): znalost vnitřku systému (black/gray/white box), úroveň (jednotková, integrační, kontraktní, end-to-end) a cíl jsou samostatné volby. Pro příslušná rizika použijte plány [výkonnostních](performance-testing.md) a [bezpečnostních](security-testing.md) testů. Než agent spustí narušující nebo nákladný experiment, zaznamenejte oprávnění, cíl a prostředí, zátěž, akceptační prahy, podmínky přerušení a úklid.

## Originalita a hranice zveřejnění

Zdroje čtěte jako důkazy a rozhodnutí vysvětlujte vlastními slovy a příklady. Do průvodce nekopírujte, nepřekládejte ani těsně neparafrázujte text zdroje; odkaz neuděluje svolení k jeho převzetí. Bezobslužné generování využívající zdroje probíhá v soukromém repozitáři nebo pracovním prostoru, protože nezpracované logy, výstup modelu, shrnutí a artefakty mohou zveřejnit zdrojový text ještě před posouzením. Člověk před přenesením schváleného výstupu do veřejného PR ověří originalitu, práva, citlivá data a technický význam. Veřejné úlohy sledování zdrojů zveřejňují pouze metadata. Ani kontrola textových shod, ani druhý agent neposkytují právní schválení.

## Související rozhodnutí

[Kontroly kvality prokazující chování](quality.md) · [Bezpečnost, soukromí a dodavatelský řetězec softwaru](security.md) · [Důkazy a automatická údržba](maintenance.md) · [Skills, pluginy, MCP a WebMCP](integrations.md)

## Primární zdroje


[openai-agents](https://raw.githubusercontent.com/openai/openai-agents-python/841dfdd938bfd4ca052475eb76d6245a356868e0/docs/agents.md) · [agents-guardrails](https://raw.githubusercontent.com/openai/openai-agents-python/841dfdd938bfd4ca052475eb76d6245a356868e0/docs/guardrails.md) · [codex-action](https://raw.githubusercontent.com/openai/codex-action/c05cfd74ad95c626cdf05c6685e62becc3bf7813/README.md) · [plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md)
