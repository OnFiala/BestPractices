---
{
  "id": "reference-labs",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Ejecutar e interpretar los proyectos de referencia

## Tres límites ejecutables

Los proyectos de referencia son implementaciones didácticas originales con componentes locales de prueba bajo su propio control. Permiten a los agentes inspeccionar contratos concretos, provocar fallos deliberadamente y conservar resultados medidos sin una cuenta de proveedor ni una llamada de pago a un modelo. Son componentes seleccionados por los seis procedimientos de proyecto, no seis productos terminados ni plantillas de despliegue en producción.

| Referencia | Implementación real | Sustitución deliberada y límite |
| --- | --- | --- |
| `examples/durable_service` | HTTP en la interfaz de bucle local, identidad de prueba vinculada al inquilino, transacciones SQLite, reglas de idempotencia y versiones, outbox y consumidor, simulacros de caída de procesos hijos, restauración de instantáneas y sobrecarga limitada | Credenciales bearer sintéticas; SQLite local y una máquina; sin pagos reales, proveedor de identidad, intermediario de mensajes ni conmutación por fallo regional |
| `examples/agent_workflow` | Flujo de trabajo persistido y registro de efectos separado, autorización antes del contexto, comprobaciones de capacidades para la acción exacta, cancelación, presupuestos y conciliación | Modelo determinista de prueba, emisor confiable de aprobaciones de prueba, simulación de caída y reapertura y unidades sintéticas de presupuesto; sin verificación de calidad de modelos reales ni autenticación de producción |
| `examples/frontend` | HTML semántico y módulos nativos, estado de URL, local y remoto, cancelación basada en identidad de solicitud, representación segura como texto y comprobaciones reales en Chromium | API sintética de solo lectura, un navegador y entorno observados y comprobaciones parciales de accesibilidad; sin autenticación de producción, escrituras ni cliente móvil nativo |

Cada README identifica requisitos previos, comandos, supuestos, criterios negativos de verificación, limpieza y trabajo de producción omitido. Utiliza esos contratos al adaptar un ejemplo; copiar código no implica adoptar automáticamente sus supuestos.

## Ejecutar y conservar observaciones

Desde la raíz del repositorio:

```sh
python -m examples.durable_service demo
python -m examples.durable_service drills
python -m examples.durable_service benchmark --operations 120 --concurrency 8 --capacity 2 --delay-ms 10 --seconds 5
python -m examples.agent_workflow demo
python -m examples.agent_workflow evaluate
python -m library.verification delivery durable-service agent-workflow frontend-unit frontend-browser --output reports/reference-checks.json
```

El benchmark inicia únicamente su propio componente de prueba en la interfaz de bucle local, acepta parámetros locales limitados y no admite una URL de destino remoto. Las cifras anteriores definen un pequeño experimento didáctico; no son límites recomendados para producción ni objetivos de servicio. Inspecciona conjuntamente los recuentos de trabajo ofrecido, iniciado, completado y rechazado y de errores de transporte, junto con la latencia medida, la duración de la prueba y la integridad y recuperación posteriores. El comportamiento del generador y el modelo de carga cerrado limitan la interpretación.

La evaluación del agente informa de los casos deterministas de políticas por separado de su elemento de calidad del modelo real, explícitamente no ejecutado. Que los casos ejecutados pasen aporta evidencia útil sobre esas reglas locales, no una razón para contar el elemento omitido como exitoso. El modelo y el emisor de aprobaciones de la demostración están claramente identificados como componentes de prueba.

El verificador exige pruebas realmente ejecutadas, registra las versiones del entorno de ejecución y la imagen de entradas y considera incompletas las comprobaciones obligatorias ausentes, fallidas u omitidas. Su conjunto de pruebas de navegador necesita Node 22+ y Chromium o Chrome instalado. El README de frontend documenta una habilitación explícita relativa al sandbox en un contenedor controlado; se aplica únicamente al componente local de prueba bajo control propio. Los informes son observaciones locales, no certificaciones autenticadas ni aprobación humana.

## Comprobar el límite de fallo y recuperación

Para escrituras duraderas, compara resultados permitidos y efectos secundarios denegados. Las solicitudes repetidas con el mismo inquilino, acción, clave y contenido deben devolver un único resultado ya registrado; un contenido incompatible debe fallar. Los escritores concurrentes por versión necesitan un resultado definido de ganador o conflicto. Una entrada de outbox y la escritura de negocio comparten la transacción local; los consumidores no deben confirmar eventos con esquemas desconocidos. Restaurar una instantánea pierde las escrituras locales posteriores y no deshace efectos externos.

Para acciones de agentes, inspecciona qué llega al contexto antes de que exista una propuesta y después qué valida el ejecutor de forma independiente. Una acción editada o una capacidad caducada o revocada no debe ejecutarse. Tras un efecto incierto, inspecciona el comprobante independiente y concilia; un comprobante ausente o que no coincida debe mantener el caso sin resolver, en lugar de desencadenar una repetición a ciegas. Una ejecución cancelada o terminada por timeout sigue necesitando contabilizar el trabajo ya realizado.

Para el navegador, prueba controles públicos reales y condiciones de carrera en el transporte. Un transporte abortado aún puede completar la obtención de un cuerpo de respuesta; la identidad de solicitud debe impedir que una finalización obsoleta sustituya el estado actual. Los datos denegados o malformados no deben convertirse en marcado activo. Las comprobaciones de teclado, foco y diseño estrecho cubren recorridos concretos, no todas las tecnologías de asistencia ni todos los dispositivos.

## Pasar de una referencia a un producto

Genera un conjunto de entrega, declara qué piezas se reutilizan y sustituye cada límite de componente de prueba por un contrato de proyecto revisado. Añade las integraciones y pruebas del almacenamiento, proveedor, identidad y cliente elegidos. Vuelve a ejecutar casos negativos y de recuperación contra esos límites reales, mide cargas representativas y obtén revisión independiente del despliegue y de la responsabilidad operativa. Conserva las observaciones fallidas y no ejecutadas. La publicación en producción es una decisión humana separada una vez que existe evidencia del proyecto.

## Decisiones relacionadas

[Flujo de entrega con agentes](project-delivery.md) · [Cobertura y límites](coverage.md) · [Durabilidad](durability.md) · [Pruebas de seguridad](security-testing.md) · [Pruebas de rendimiento](performance-testing.md)

## Evidencia primaria

[azure-idempotent-consumer](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/idempotent-consumer.md) · [azure-outbox](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/databases/guide/transactional-out-box-cosmos.md) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [playwright-testing](https://raw.githubusercontent.com/microsoft/playwright/ca7ca36145b84183cf423c2a099bd7e9cd8b1cb3/docs/src/best-practices-js.md) · [k6-open-vs-closed](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/using-k6/scenarios/concepts/open-vs-closed.md)
