---
{
  "id": "operations",
  "language": "es",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Salud, recuperación y coste

## Observar el resultado del usuario

Elige un indicador de nivel de servicio (SLI) para un recorrido significativo, como terminar correctamente dentro de un límite de latencia. Define su numerador, denominador, ventana de observación y exclusiones, y acuerda después el objetivo de nivel de servicio (SLO) con la persona responsable. Incluye el trabajo fallido y rechazado cuando lo exija el contrato; un error rápido no es una transacción correcta.

Un presupuesto de errores expresa el incumplimiento permitido durante esa ventana. Como ejemplo, un objetivo basado en solicitudes del 99,9 % sobre 100 000 solicitudes elegibles permite 100 solicitudes fuera del objetivo; es un cálculo, no una recomendación de objetivo. Usa el consumo observado del presupuesto y el impacto de negocio para ajustar el riesgo de las publicaciones. Define la política de respuesta antes de un incidente en lugar de tratar un presupuesto agotado como un color del panel.

Este modelo operativo es una síntesis de la biblioteca. Los materiales citados sobre observabilidad y endpoints de salud respaldan los mecanismos de medición; la frecuencia de revisión y los umbrales de escalamiento siguen siendo decisiones del proyecto.

## Separar las señales de salud

| Señal | Finalidad y limitación |
| --- | --- |
| Arranque | Permitir que termine la inicialización dentro de un límite explícito |
| Actividad del proceso (liveness) | Detectar un proceso que no puede avanzar; reiniciarlo debe ser una respuesta útil |
| Preparación para recibir tráfico (readiness) | Decidir si una instancia debe recibir un tráfico determinado |
| Recorrido sintético | Ejercitar comportamiento visible para el usuario mediante una interfaz pública controlada |
| Métricas y trazas del servicio | Explicar resultados, saturación y contribución de dependencias a lo largo del tiempo |

No hagas que todo fallo transitorio de una dependencia haga fallar la señal de actividad y reinicie procesos sanos. Las comprobaciones profundas de preparación también pueden retirar todas las instancias durante la caída de una dependencia compartida; define el comportamiento degradado y los límites específicos de cada dependencia. Las sondas de salud no deben agotar los recursos que miden. Protege los diagnósticos detallados y evita que las sondas provoquen pagos o mensajes reales.

Usa registros estructurados, métricas y trazas con identificadores de correlación, cardinalidad acotada de etiquetas y eliminación o enmascaramiento de datos sensibles. Alerta ante síntomas accionables o consumo sostenido del presupuesto de errores, con gravedad, responsable, manual operativo y escalamiento. Valida que la alerta llegue a alguien capaz de responder. Un panel o un HTTP 200 por sí solos no demuestran disponibilidad.

## Ensayar un incidente y la recuperación

Asigna una persona que dirija el incidente, establece el impacto en usuarios, estabiliza el sistema, conserva la evidencia necesaria y comunica la incertidumbre. Desactiva reintentos o acciones de agentes que amplifiquen el daño. Prefiere una acción de recuperación conocida y segura a un rediseño de emergencia no probado. Tras restaurar, concilia el trabajo duradero y los efectos en proveedores antes de reanudar la automatización.

En un entorno aislado, restaura una copia de seguridad, revoca o rota credenciales y simula un proveedor no disponible. Mide el intervalo de recuperación y la ventana de pérdida de datos, y verifica después un recorrido real de usuario e invariantes de negocio. Usa [comprobaciones de caja negra](testing-strategy.md) para el comportamiento observable y [pruebas de rendimiento y recuperación](performance-testing.md) para vaciar la cola atrasada después de la saturación. Registra los resultados reales, las versiones de artefactos y los pasos manuales pendientes.

Después de un incidente, registra las condiciones que contribuyeron y las acciones con responsables y plazos. Añade una prueba de regresión cuando pueda demostrar el comportamiento corregido. Conserva el aprendizaje operativo útil sin publicar datos personales ni credenciales.

## Mantener visibles las responsabilidades y el gasto

Mide el coste por transacción útil y tarea de agente, incluidos reintentos, tokens, tráfico saliente y observabilidad. Define una alerta y un mecanismo efectivo de parada o degradación; un aviso por correo no es un límite de gasto. Revisa regularmente las alertas sin resolver, los cambios de fuentes y dependencias y el gasto. Revisa objetivos, capacidad y evidencia de restauración tras cambios importantes; elige una frecuencia recurrente que la persona responsable pueda mantener.

Un sistema está sano cuando sus responsables pueden demostrar su comportamiento, su recuperación y una obligación operativa sostenible. Más réplicas no sustituyen a una persona responsable, y ninguna ejecución de pruebas garantiza fiabilidad futura.

## Decisiones relacionadas

[Durabilidad](durability.md) · [Escalado](scaling.md) · [Ciclo de vida](lifecycle.md) · [Estrategia de pruebas](testing-strategy.md) · [Pruebas de rendimiento](performance-testing.md)

## Evidencia primaria

[observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [azure-health-endpoints](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/health-endpoint-monitoring.md)
