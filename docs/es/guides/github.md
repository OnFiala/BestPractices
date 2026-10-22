---
{
  "id": "github",
  "language": "es",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# GitHub, versiones y árboles de trabajo limpios

## Un flujo que se pueda revisar

Mantén `main` listo para publicar. Usa ramas de corta duración para un solo cambio y commits pequeños y coherentes que expliquen su intención. Crea un commit cuando un incremento significativo pueda entenderse y comprobarse; no esperes a terminar todo el proyecto ni incluyas secretos generados o cachés. `feat:`, `fix:` y `docs:` son convenciones locales útiles, pero no sustituyen una descripción clara.

Abre un PR que describa el problema, el comportamiento resultante, la evidencia, los riesgos y la reversión. Revisa el diff final, no solo el resumen del agente. Exige comprobaciones de estado, revisión de los responsables del código cuando corresponda, conversaciones resueltas y una nueva aprobación tras cambios significativos. Los agentes nunca aprueban ni fusionan su propio trabajo. Configura un conjunto de reglas que bloquee los envíos forzados, el borrado de ramas protegidas y los cambios directos en `main`; los archivos por sí solos no activan estas reglas.

Usa SemVer para un contrato público definido. Etiqueta las entregas deliberadas, publica un registro de cambios y notas de migración, y nunca sustituyas silenciosamente una etiqueta de versión. Los commits internos no tienen por qué ser entregas. En esta biblioteca, los identificadores de las guías y los metadatos son contratos: romperlos exige una migración y una decisión de versionado.

## Limpieza

Antes de editar, inspecciona el estado y conserva el trabajo de otras personas. Excluye los resultados generados; revisa los archivos preparados para el commit y los posibles borrados accidentales antes de confirmar los cambios. Nunca utilices comandos generales de reset o limpieza. Elimina las ramas fusionadas después de comprobar que no contienen trabajo exclusivamente local; limpia las referencias por separado. En este entorno de nube, usa árboles de trabajo adicionales solo cuando sean necesarios y se soliciten explícitamente. Asigna una persona responsable y una fecha de caducidad a las ramas abandonadas.

## Decisiones relacionadas

[Controles que demuestran comportamiento](quality.md) · [Dirección humana, ejecución de agentes](agents.md) · [Evidencia y mantenimiento automático](maintenance.md)

## Evidencia primaria

[github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md) · [semver](https://raw.githubusercontent.com/semver/semver/f99d5485190a47c0863949e7da810a5553e0ed4d/semver.md)
