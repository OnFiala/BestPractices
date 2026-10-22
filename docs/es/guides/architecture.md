---
{
  "id": "architecture",
  "language": "es",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Elegir y conectar arquitecturas

## Elegir según las restricciones y las responsabilidades

Registra los límites de las transacciones, las necesidades de latencia y recuperación, la sensibilidad de los datos, la forma de la carga y quién puede operar el sistema. Compara el diseño viable más sencillo con la alternativa propuesta. La tabla siguiente es un marco de decisión original de esta biblioteca; los documentos de patrones citados explican mecanismos y compensaciones relevantes, no una clasificación universal.

| Enfoque | Una condición inicial útil | Coste y motivo para reconsiderarlo |
| --- | --- | --- |
| Sitio estático | Contenido público sin escrituras de confianza en el servidor | Límites de compilación y caché; añade una API protegida para cambios autenticados |
| Monolito modular | Un producto necesita transacciones coordinadas y cambios frecuentes | Disciplina en las dependencias entre módulos; extrae solo una restricción medida o una capacidad con responsabilidad independiente |
| Funciones | Trabajo acotado y con picos que encaja en el contrato de ejecución del proveedor | Arranques en frío, cuotas, presión sobre conexiones y reintentos; reconsidera el trabajo sostenido o de larga duración |
| Servicios | La responsabilidad, la publicación o el aislamiento de fallos independientes aportan un beneficio concreto | Fallos de red, contratos versionados, observabilidad y operación de la coherencia |
| Trabajo dirigido por eventos | El trabajo puede terminar después y los consumidores tienen responsabilidades distintas | Entrega duplicada o fuera de orden, retraso, repetición y evolución de esquemas |
| Flujos de trabajo duraderos | Los pasos de negocio de larga duración deben sobrevivir a interrupciones | Restricciones del motor, retención del historial, actualizaciones del código y conciliación de efectos externos |

Estas opciones se pueden combinar. Un monolito puede servir un frontend estático y usar una cola sin convertirse en un sistema de microservicios. La dirección de las dependencias en el código y la topología de despliegue son decisiones distintas: dividir procesos no crea por sí mismo límites de dominio útiles.

CQRS separa los modelos de lectura y escritura; puede empezar dentro de una sola base de datos. Los almacenes separados añaden retraso de sincronización y un contrato para las lecturas desactualizadas. Event sourcing convierte el historial de eventos en la fuente autoritativa y exige decidir sobre evolución de eventos, repetición, privacidad y retención. Una cola o una tabla de auditoría no constituyen por sí solas event sourcing. Introduce estos patrones de forma selectiva cuando su beneficio específico compense las obligaciones adicionales de recuperación y pruebas.

## Hacer que los límites se puedan revisar

Para cada conexión entre navegador, API, proceso en segundo plano, almacén de datos y proveedor, registra:

| Contrato | Evidencia que debe ver quien revise |
| --- | --- |
| Autoridad | Qué identidad puede realizar cada acción y sobre los datos de quién |
| Propiedad de los datos | Qué componente puede modificar cada invariante y cómo solicitan cambios los demás componentes |
| Fallo | Tiempo límite, cancelación, responsable de reintentos, tratamiento de duplicados y estado pendiente o de error visible para el usuario |
| Compatibilidad | Productores y consumidores compatibles, versión del esquema y condición para retirar compatibilidad |
| Operación | Trazas y métricas, responsable de soporte, procedimiento de restauración o conciliación y presupuesto |

Una base de datos compartida puede ser una elección transitoria deliberada. Las escrituras sin restricciones desde varios servicios dificultan la responsabilidad independiente y las migraciones; documenta ese acoplamiento en lugar de describir los servicios como independientes.

## Demostrar el cambio antes de extraer componentes

Para un proceso en segundo plano o servicio propuesto, identifica primero el síntoma: antigüedad de la cola, contención de bloqueos, coordinación de despliegues o necesidad de aislamiento. Registra una referencia representativa y compara una pequeña funcionalidad completa con la ruta existente. Aplica [comprobaciones de contrato y de caja negra](testing-strategy.md), [pruebas de carga y recuperación](performance-testing.md) y [pruebas de seguridad](security-testing.md) en el nuevo límite. Incluye una dependencia lenta, un consumidor antiguo y una solicitud repetida.

El plan de migración identifica la propiedad de los datos durante la transición, la selección del tráfico, la compatibilidad y la conciliación. Mantén un único escritor autoritativo, salvo que se haya probado un diseño deliberado de resolución de conflictos. Define la evidencia que permite trasladar tráfico, la condición de interrupción y la ruta de recuperación después de nuevas escrituras. Revertir el tráfico no deshace automáticamente los datos migrados.

Si no se demuestra el beneficio, conserva la topología más sencilla y el límite interno útil. Registra el resultado en un ADR para que el siguiente agente no repita un rediseño sin fundamento.

## Decisiones relacionadas

[Durabilidad y trabajo distribuido](durability.md) · [Arquitectura del frontend](frontend.md) · [Escalar con mediciones](scaling.md) · [Alojamiento](hosting.md) · [Estrategia de pruebas](testing-strategy.md)

## Evidencia primaria

[azure-architecture-styles](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/guide/architecture-styles/index.md) · [azure-cqrs](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/cqrs.md) · [azure-event-sourcing](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/event-sourcing.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml) · [durable-workflows](https://raw.githubusercontent.com/temporalio/temporal/e8ee627110a98501103827745aab18aedf312dd0/README.md)
