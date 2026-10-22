---
{
  "id": "maintenance",
  "language": "es",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Evidencia y mantenimiento automático

## Flujo de evidencia

`data/sources.json` separa la fuente inmutable inspeccionada de la URL supervisada para detectar cambios posteriores. Registra el editor, el alcance, el intervalo de revisión y la evidencia de licencia. La referencia de recuperación registra hashes obtenidos correctamente, no aprobación humana. Un observador programado obtiene documentos HTTPS con límites y notifica fuentes modificadas, no disponibles o con revisión vencida. Un hash distinto es una señal para revisar, nunca autorización para cambiar recomendaciones. Una descarga fallida sigue siendo no disponible, no «sin cambios».

El workflow de fuentes crea o actualiza un PR de evidencia cuando hace falta actuar. No actualiza la referencia aceptada ni fusiona cambios. Una persona lee el diff relevante de la fuente, verifica afirmaciones y aplicabilidad y decide si actualizar conjuntamente guías, traducciones, fechas de revisión y referencia. No reinicies una fecha de revisión solo porque una URL devuelva 200.

## Actualizaciones asistidas por agentes

El repositorio público observa metadatos de fuentes. Los trabajos de generación con modelos alimentados con fuentes y de propuesta de cambios se restringen a un repositorio privado independiente, una réplica privada o un espacio de trabajo privado: registros, resúmenes, parches y artefactos pueden contener texto de las fuentes antes de la revisión de derechos. El workflow privado y opcional de Codex requiere un secreto configurado y habilitación explícita; la validación local y las comprobaciones de fuentes no necesitan una API de pago. El modelo devuelve datos estructurados de propuesta con límites. Un consumidor nuevo y de confianza valida esos datos en lugar de ejecutar un script producido por el agente o confiar en sus metadatos Git.

Una persona inspecciona la salida privada para comprobar expresión original, licencias, datos sensibles, evidencia y significado de las traducciones antes de trasladar el contenido aprobado a un PR público. No hay traslado público automático. Escribe explicaciones y ejemplos independientes; no copies ni traduzcas prosa externa ni parafrasees de cerca una expresión distintiva. Los avisos obligatorios del software de terceros conservan sus propias licencias. Una cita o una comprobación de similitud no conceden derechos de reutilización.

El agente no tiene autoridad para aprobar, fusionar o publicar. Los conjuntos de reglas y la revisión obligatoria siguen necesitando configuración real en GitHub; un archivo de workflow no los impone. No se ha desplegado un servicio privado de generación como parte de esta biblioteca.

## Actualidad y fallos

Revisa las fuentes de IA y protocolos que cambian deprisa con más frecuencia que los principios estables. Identifica experimentos y elementos obsoletos, conserva enlaces de migración y registra recomendaciones controvertidas. Credenciales ausentes, redes bloqueadas, comprobaciones fallidas y traducciones desactualizadas siguen siendo bloqueos visibles. Registra el tiempo transcurrido desde una revisión vencida y el tiempo hasta resolver cambios en las fuentes. Revierte por commit un cambio incorrecto de recomendaciones y evalúa los proyectos que lo adoptaron.

No consideres que un README o un índice que incluye archivos externos cubre la especificación subyacente. Registra el control o mecanismo sustantivo en que se basa realmente la recomendación. Las correspondencias entre afirmaciones y fuentes deben distinguir el comportamiento respaldado por fuentes de la síntesis local, registrar aplicabilidad y mantenerse vinculadas a la versión revisada. Actualiza la evidencia del ciclo de vida del producto antes de adoptar una plataforma de IA; una metodología puede seguir siendo útil después de retirarse el producto utilizado en su ejemplo.

## Decisiones relacionadas

[GitHub, versiones y árboles de trabajo limpios](github.md) · [Dirección humana, ejecución de agentes](agents.md) · [Gobierno y decisiones abiertas](governance.md)

## Evidencia primaria

[codex-action](https://raw.githubusercontent.com/openai/codex-action/c05cfd74ad95c626cdf05c6685e62becc3bf7813/README.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md) · [plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md)
