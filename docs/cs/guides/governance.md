---
{
  "id": "governance",
  "language": "cs",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Správa a nezodpovězená rozhodnutí

## Současná dohoda

Jde o veřejnou a přenositelnou knihovnu. Angličtina je kanonická, doplněná českým, německým a španělským překladem. Původní texty a diagramy používají CC BY 4.0; kód, konfigurace a opakovaně použitelné šablony kódu používají MIT. Zdroje třetích stran si ponechávají své licence. Agenti navrhují PR; člověk je posuzuje a slučuje. Počáteční doporučení a překlady nejsou automaticky schváleny člověkem.

Sama knihovna je vytvářena a udržována pomocí AI agentů a tento původ otevřeně uvádí. Původní texty si při exportu do JSON zachovávají svou licenci obsahu; licence softwaru třetích stran a povinný odpovídající zdrojový kód se uchovávají samostatně. Do veřejných doporučení nekopírujte, nepřekládejte ani těsně neparafrázujte zdrojový text. Citace je důkaz, nikoli svolení. Člověk ověří originalitu a práva dříve, než se materiál ze soukromé automatizace využívající zdroje přenese do veřejného PR.

## Otázky, které musí zodpovědět každý přebírající projekt

Kdo odpovídá za produkci a je dostupný při incidentu? Která data nikdy nesmějí opustit region nebo poskytovatele? Jak dlouhý výpadek a jakou ztrátu dat uživatelé snesou? Jaký je měsíční rozpočet infrastruktury a AI včetně vynuceného zastavení? Co se stane při nedostupnosti modelu nebo hostingu? Kdo schvaluje nevratné operace? Jak uživatelé exportují a mažou data? Jaké požadavky na přístupnost a právní požadavky platí? Kdo převezme projekt po odchodu vlastníka?

Odpovědi uchovávejte v profilu projektu a ADR. Nezodpovězené otázky se závažnými důsledky blokují příslušné spuštění, nikoli nesouvisející průzkum. Výjimky vyžadují vlastníka, důvod, kompenzační opatření a konec platnosti.

## Péče o knihovnu

Nové téma nebo zpochybnění doporučení navrhněte v issue; připojte protipříklad a primární důkazy. Oddělujte univerzální principy od preferencí závislých na kontextu. Postupy vyřazujte s odkazy na náhradu místo mazání historie. Publikujte verzované změny a sdělujte změněné povinnosti. O zachování významu překladů rozhodují lidští posuzovatelé; shodná čísla revizí kontrolují pouze evidenci. Užitečnost měřte úspěšnými rozhodnutími a snížením potřeby oprav, nikoli počtem stránek.

## Související rozhodnutí

[Důkazy a automatická údržba](maintenance.md) · [Zavedení knihovny v projektu](adoption.md) · [GitHub, verze a čisté stromy](github.md)

## Primární zdroje


[github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [semver](https://raw.githubusercontent.com/semver/semver/f99d5485190a47c0863949e7da810a5553e0ed4d/semver.md) · [plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md)
