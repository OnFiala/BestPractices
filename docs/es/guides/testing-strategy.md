---
{
  "id": "testing-strategy",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Elegir una estrategia de pruebas

## Describir la prueba en tres ejes independientes

El agente debe indicar qué conoce del sistema, qué límite ejercita y qué fallo busca. Son elecciones distintas. Una prueba de caja negra puede comprobar funcionalidad ordinaria, rendimiento o seguridad; el término no significa prueba de penetración.

| Eje | Opciones | Qué informa la elección a quien revise |
| --- | --- | --- |
| Conocimiento disponible | Caja negra: interfaces observables; caja gris: componentes internos o instrumentación seleccionados; caja blanca: código y rutas internas | Qué información orientó el diseño de la prueba y qué puntos ciegos permanecen |
| Límite ejercitado | Unidad, integración, contrato entre consumidor y proveedor, extremo a extremo | Cuánto del sistema real participa y dónde pueden localizarse los fallos |
| Objetivo | Corrección funcional, seguridad, rendimiento, recuperación, accesibilidad, compatibilidad | Sobre qué riesgo aporta evidencia el resultado; el éxito en un objetivo no demuestra otro |

Por ejemplo, una prueba de API de caja negra puede verificar que dos solicitudes de compra idénticas devuelven un único resultado de negocio. Una prueba unitaria de caja blanca puede explorar todas las ramas de reintento. Una prueba de integración de caja gris puede inspeccionar además la transacción y el outbox. Aportan evidencia complementaria. Documenta la terminología local si la definición del equipo de «integración» o «contrato» difiere.

## Elegir según el cambio y sus consecuencias

La matriz siguiente es la política inicial recomendada por esta biblioteca, no una batería universal obligatoria. Añade o elimina comprobaciones con una justificación explícita del riesgo.

| Cambio o riesgo | Primeras comprobaciones útiles | Ampliación y evidencia de aceptación |
| --- | --- | --- |
| Documentación o traducción | Significado, terminología, enlaces y equivalencia entre idiomas | Renderizar la presentación modificada si cambia el diseño o la navegación; no crear una batería de ejecución nueva para una corrección inocua de redacción |
| Cálculo de negocio o transición de estado | Ejemplos unitarios, valores límite y entradas inválidas; casos basados en propiedades para invariantes reales | Demostrar que una entrada que viola el invariante falla; añadir integración si la persistencia o el estado externo forman parte de la corrección |
| Esquema o transacción de base de datos | Integración con una base de datos real, restricciones, concurrencia y compatibilidad de migración | Volumen de datos representativo, bloqueos, reinicio, reanudación y recuperación; los consumidores antiguos admitidos siguen siendo compatibles |
| Esquema de API o evento | Ejemplos de contrato entre productor y consumidor y comprobaciones de compatibilidad | Ruta real de serialización y transporte; rechazar entradas inválidas sin efectos no deseados |
| Recorrido de usuario o estado del frontend | Comprobaciones de componentes y un pequeño recorrido de navegador basado en semántica pública | Estados de carga, vacío, error y cancelación, teclado y ventana estrecha; verificar eventos reales del navegador |
| Autenticación, permisos o ámbito del inquilino | Pruebas de política y acceso no autorizado a API y objetos con identidades distintas | Revisar puntos de entrada no probados y ejecutar pruebas de seguridad específicas; las solicitudes denegadas no devuelven datos protegidos ni producen efectos |
| Proceso en segundo plano, pago o flujo duradero | Casos de integración con duplicados, reordenación, tiempos agotados y fallos en puntos críticos | Conciliar los efectos previstos después de reintentar o reiniciar; comprobar compatibilidad con el entorno de pruebas del proveedor cuando sea necesario |
| Concurrencia, caché, planificación o capacidad | Comprobaciones funcionales con concurrencia y una referencia medida | Elegir pruebas de carga, estrés, picos o duración prolongada según la guía de rendimiento; conservar la corrección y una recuperación acotada |
| Modelo, prompt, recuperación de información, herramienta o política de agente | Evaluaciones versionadas de tareas, casos adversariales y pruebas deterministas de política | Comparar con casos reservados para evaluación, inspeccionar efectos reales de herramientas, repetir casos estocásticos e informar de la variabilidad |

## Planificar antes de elegir una herramienta

Escribe un breve plan de prueba: requisito afectado; hipótesis de fallo; modelo de conocimiento, límite y objetivo; datos preparados y entorno; resultados esperados; límites de ejecución segura; y evidencia que se conservará. La herramienta se elige después de ese plan. Un controlador de navegador, un cliente HTTP, un generador de propiedades, un generador de carga, un escáner o una revisión humana observan cosas distintas.

Usa el límite más pequeño que pueda revelar el defecto y añade después una comprobación realista del límite cuando los sustitutos puedan ocultarlo. Una base de datos simulada no demuestra una restricción de unicidad de una base de datos real, y un evento simulado del navegador no demuestra compatibilidad nativa. Mantén los proveedores externos controlados en las pruebas deterministas; distingue una comprobación de compatibilidad en su entorno de pruebas de una respuesta simulada.

Haz que los datos preparados sean independientes y reproducibles. Controla los relojes y la aleatoriedad relevantes, registra las semillas y aísla cuentas, inquilinos, estado y limpieza. No compartas un usuario de prueba mutable entre ejecuciones paralelas, salvo que esa concurrencia sea el objeto de la prueba. Protege los datos preparados y las trazas como información; nunca copies registros de producción solo para hacer una prueba realista.

## Crear aserciones que puedan refutarse

Comprueba las salidas, el estado persistido y los efectos prohibidos relevantes para el requisito. Un código HTTP de éxito por sí solo no demuestra que se haya devuelto el objeto correcto. Una prueba de autorización debe ejercitar tanto una acción permitida como una denegada y verificar después que la denegación no modificó el estado protegido.

Para una corrección con consecuencias importantes, demuestra que la prueba puede revelar el error original o una variante local deliberadamente incorrecta. Usa valores límite y clases de equivalencia cuando corresponda. Las pruebas basadas en propiedades exploran un invariante definido; siguen dependiendo de que el invariante y el modelo de entradas sean correctos. La cobertura puede revelar código no visitado, pero una cobertura alta no demuestra que los requisitos sean correctos ni que los límites de seguridad estén completos.

## Decidir cuándo hay evidencia suficiente

Detén la publicación afectada si fallan comprobaciones obligatorias, el objetivo está fuera del ámbito aprobado, los datos de prueba salen de su límite o una afirmación de consecuencias importantes carece de evidencia. Informa de las omisiones y de la incertidumbre. Una persona puede aceptar un riesgo residual documentado y limitado en el tiempo; un agente no puede dar por superada una comprobación no ejecutada.

Terminar significa que el comportamiento acordado está respaldado por resultados interpretables, limitaciones conocidas y un plan de recuperación. Conserva la revisión probada, la configuración, la versión de los datos preparados, los comandos, los resultados y las trazas relevantes sin valores sensibles. Amplía las pruebas cuando una nueva hipótesis de fallo lo justifique, en lugar de repetir indefinidamente la misma batería que ya pasa.

## Evidencia y decisiones relacionadas

El modelo de tres ejes y la matriz de selección son una síntesis local original. OWASP respalda las pruebas de autorización en varios límites; Playwright respalda las comprobaciones de navegador aisladas y basadas en el comportamiento visible; PostgreSQL documenta las propiedades de concurrencia que deben ejercitar las pruebas con una base de datos real. Estas fuentes no certifican todas las celdas de la matriz.

[Controles de calidad](quality.md) · [Pruebas de rendimiento y estrés](performance-testing.md) · [Pruebas de seguridad](security-testing.md) · [Datos y migraciones](data.md) · [Durabilidad](durability.md)

## Evidencia primaria

[owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [playwright-testing](https://raw.githubusercontent.com/microsoft/playwright/ca7ca36145b84183cf423c2a099bd7e9cd8b1cb3/docs/src/best-practices-js.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml) · [owasp-multi-tenant](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.md)
