---
{
  "id": "coverage",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Interpretar con honestidad la cobertura y la verificación

## Utilizar el mapa de cobertura declarado

El registro de cobertura legible por máquinas describe los ámbitos del ciclo de vida respaldados por esta edición. Cada registro enlaza las guías y referencias primarias, identifica las referencias ejecutables y los casos de prueba exactos que existan, define la afirmación acotada y enumera la evidencia que sigue siendo necesaria en un proyecto que adopte la biblioteca. El mapa declara un alcance, no pretende enumerar toda la ingeniería de software.

Consúltalo mediante `python -m library.coverage`, la herramienta MCP de solo lectura o los datos exportados del sitio web. Un informe local opcional de verificación puede añadir observaciones vinculadas a la imagen actual de entradas. El registro estático de un sitio web no se convierte en un resultado recién ejecutado porque alguien lo abra.

## Distinguir los tipos de respaldo

| Respaldo | Qué existe | Qué sigue siendo desconocido |
| --- | --- | --- |
| Orientación documentada | Una explicación original de la decisión y enlaces a fuentes de alcance definido | Si la explicación se aplica a este proyecto o se ha implementado |
| Referencia ejecutable | Código original y comprobaciones identificadas que pueden ejercitar un límite local declarado | Si esas comprobaciones se ejecutaron con estas entradas exactas y qué ocurrió |
| Observación registrada vigente | Hashes de entrada coincidentes y un conjunto registrado de pruebas aprobado con los casos identificados obligatorios | Si el informe es auténtico, el criterio de verificación es suficiente o un destino diferente se comporta igual |
| Observación ausente, obsoleta, fallida o parcial | La evidencia obligatoria falta, ha cambiado, ha fallado o está incompleta | La afirmación sin respaldo sigue sin respaldo; no deduzcas éxito del silencio |

Todo resultado local sigue subordinado a su alcance. La evidencia de reinicio de procesos con SQLite no demuestra recuperación de un almacén replicado. Una ejecución breve en la interfaz de bucle local con un modelo de carga cerrado no demuestra una carga de un millón de usuarios. Un modelo determinista de prueba no establece calidad de modelos reales. Una única comprobación básica en Chromium no demuestra accesibilidad completa ni una matriz de navegadores compatibles.

## Plantear la pregunta adecuada sobre la finalización

Para un proyecto concreto, identifica qué requisitos y consecuencias de fallo importan. Selecciona el procedimiento correspondiente y los controles del planificador y después vincula cada obligación de aceptación a un resultado observable. Comprueba efectos denegados, estado persistido y recuperación junto con las respuestas exitosas. Registra las pruebas omitidas deliberadamente y su riesgo en lugar de marcar un ámbito entero como completado a partir de un ejemplo aprobado.

Un revisor debe inspeccionar la afirmación de la fuente, el límite de implementación, el criterio de verificación de la prueba, el artefacto ejecutado y el entorno. Un hash coincidente solo establece identidad. Los recuentos de fuentes y páginas traducidas y un panel en verde no pueden sustituir esa cadena. Los informes locales y las etiquetas de roles no son certificaciones firmadas ni aprobación humana autenticada.

## Mantener explícitas las carencias

El registro identifica extensiones que necesitan trabajo adicional en el proyecto: clientes y dispositivos nativos, comportamiento regulado o crítico para la seguridad física, sistemas de tiempo real estricto, conmutación por fallo entre regiones, grandes flujos de datos y entrenamiento, integraciones de identidad y pagos en producción y capacidad de larga duración. Las guías generales pueden seguir orientando esos proyectos, pero esta edición no contiene una referencia ejecutada para cada límite especializado.

Al ampliar un ámbito, añade orientación original, respaldo de fuentes, una referencia con afirmaciones que puedan refutarse cuando resulte útil, casos negativos, limitaciones y las cuatro versiones de idioma. Un cambio de fuente desencadena una revisión semántica; un resultado nuevo de prueba pertenece a sus entradas exactas. Conserva los informes históricos como evidencia fechada en lugar de sustituir silenciosamente su significado. La adopción humana sigue siendo una decisión separada.

## Decisiones relacionadas

[Flujo de entrega con agentes](project-delivery.md) · [Comprobaciones de referencia](reference-labs.md) · [Controles de calidad](quality.md) · [Mantenimiento de evidencia](maintenance.md)

## Evidencia primaria

[github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md) · [owasp-asvs-requirements](https://raw.githubusercontent.com/OWASP/ASVS/3383877f732ce89a458a1af43288f2f1b1d7db0c/5.0/docs_en/OWASP_Application_Security_Verification_Standard_5.0.0_en.csv)
