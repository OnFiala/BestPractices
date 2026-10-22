---
{
  "id": "github",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# GitHub, versiones y árboles limpios

## Flujo revisable

Mantén `main` publicable. Usa ramas breves por cambio y commits pequeños con intención clara. Guarda incrementos comprensibles y verificables, sin secretos ni cachés. `feat:`, `fix:` y `docs:` son convenciones locales, no explicaciones.

El PR describe problema, comportamiento, pruebas, riesgos y reversión. Revisa el diff final, no solo el resumen del agente. Exige checks, revisión apropiada de propietarios, conversaciones resueltas y nueva aprobación tras cambios importantes. Los agentes no aprueban ni fusionan. Configura rulesets contra force-push, borrado y cambios directos en `main`; los archivos no los activan.

Usa SemVer para un contrato público definido. Etiqueta entregas deliberadas, registra cambios y migración; no reemplaces tags silenciosamente. Cada commit no necesita versión. Los IDs y metadatos de esta biblioteca son contratos: romperlos exige migración y decisión de versión.

## Limpieza

Inspecciona status y conserva trabajo ajeno. Ignora salidas generadas, revisa staging y borrados. Evita reset/clean generalizados. Borra ramas fusionadas tras comprobar trabajo local; poda referencias por separado. En esta nube usa worktrees solo si se solicitan. Asigna responsable y caducidad a ramas abandonadas.

## Decisiones relacionadas

[Controles que demuestran comportamiento](quality.md) · [Dirección humana, ejecución de agentes](agents.md) · [Evidencia y mantenimiento automático](maintenance.md)

## Evidencia primaria

[github-rulesets](https://raw.githubusercontent.com/github/docs/main/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/main/content/actions/reference/security/secure-use.md) · [semver](https://raw.githubusercontent.com/semver/semver/master/semver.md)
