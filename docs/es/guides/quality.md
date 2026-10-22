---
{
  "id": "quality",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Controles que demuestran comportamiento

## Probar contratos, no copiar la implementación

Un formateador correcto no demuestra un producto funcional. Elige pruebas por consecuencias: unitarias para reglas, integración para bases y servicios, contratos para consumidores y pocos recorridos completos. Incluye acceso denegado, entradas inválidas, timeout, duplicados y recuperación. Usa datos sintéticos y efectos externos aislados.

## Control de entrega

Exige instalación reproducible, build/tipos cuando corresponda, pruebas significativas y revisión del diff real. Distingue éxito, fallo, omisión y no ejecutado. Nunca debilites assertions para publicar. Un test inestable necesita responsable y caducidad de cuarentena.

En trabajo de IA, comprueba si la prueba puede detectar el defecto. Una revisión independiente examina supuestos y casos negativos. Los snapshots necesitan comprobación semántica; el porcentaje de cobertura no basta.

## Esta biblioteca

Ejecuta validador, pruebas Python, lint y construcción estricta de cuatro idiomas. Se rechazan traducciones ausentes, revisiones antiguas, fuentes desconocidas y enlaces rotos. Monitorizar fuentes es una observación de red separada; CI no demuestra exactitud ni calidad de traducción.

## Revisar

Mide defectos escapados, cambios fallidos, tiempo de recuperación y controles lentos. Elimina redundancia sin protección y conserva evidencia de caminos críticos. Una persona decide si es suficiente.

## Decisiones relacionadas

[GitHub, versiones y árboles limpios](github.md) · [Dirección humana, ejecución de agentes](agents.md) · [El ciclo de vida completo](lifecycle.md)

## Evidencia primaria

[owasp](https://raw.githubusercontent.com/OWASP/ASVS/master/README.md) · [wcag](https://raw.githubusercontent.com/w3c/wcag/main/guidelines/index.html) · [github-workflows](https://raw.githubusercontent.com/github/docs/main/content/actions/reference/security/secure-use.md)
