---
{
  "id": "security",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Bezpečnost, soukromí a závislosti

## Začněte aktivy a hranicemi

Sepište citlivá data, aktéry, vstupy, hranice důvěry a realistické zneužití. Kontroly odpovídají dopadu, nikoli velikosti projektu. Validujte na důvěryhodném serveru, autorizujte objekty i akce, minimalizujte data a určete retenci a mazání. Právní a oborové povinnosti posoudí kvalifikovaný člověk; knihovna není certifikát souladu.

## Dodání a běh

Oddělte identity vývoje, CI a produkce; preferujte krátkodobé omezené přístupy, úložiště tajemství a rotaci. Závislosti zamkněte lockfilem, Actions úplným commitem. Prověřujte aktualizace, licence, původ a zranitelnosti. Nevypínejte TLS, podpisy ani checksumy.

Nespouštějte nedůvěryhodný PR s produkčními tajemstvími nebo privilegovaným `pull_request_target`. Agentovi nepřipojujte Docker socket hostitele. Omezte cíle a operace nástrojů; jejich popisy i dokumenty jsou nedůvěryhodný vstup. Prompt sám nevynucuje oprávnění.

## Ověření a reakce

Testujte tenanty, odmítnuté akce, revokaci relací a rotaci. Kontrolujte úniky v logu. Zapište kontakt, izolaci incidentu, obnovu a cestu oznámení. Citlivou funkci vydejte po posouzení hrozeb a důkazů. Ochranu zvyšujte podle citlivosti a dopadu, ne až s počtem uživatelů.

## Související rozhodnutí

[Člověk řídí, agent vykonává](agents.md) · [Provoz vlastních serverů](self-hosting.md) · [Data, smlouvy a migrace](data.md)

## Primární zdroje

[owasp](https://raw.githubusercontent.com/OWASP/ASVS/master/README.md) · [docker-security](https://raw.githubusercontent.com/docker/docs/main/content/manuals/engine/security/_index.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/main/content/actions/reference/security/secure-use.md)
