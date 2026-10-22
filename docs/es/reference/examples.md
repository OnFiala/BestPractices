---
{
  "id": "examples",
  "language": "es",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Rutas de referencia para proyectos

## Seis perfiles de diseño, no aplicaciones desplegadas

Estos perfiles originales conectan elecciones arquitectónicas con una primera demostración observable. Son puntos de partida ilustrativos, no combinaciones de tecnologías comparadas en pruebas de rendimiento, certificaciones de cumplimiento ni resultados de pruebas ejecutadas. Los [perfiles de diseño legibles por máquinas](https://github.com/OnFiala/BestPractices/blob/main/data/blueprints.json) contienen límites, recuperación, señales de cambio y planes de prueba. Fija la revisión del repositorio al adoptarlos.

| Proyecto | Diseño inicial | Primera demostración | Revisar cuando |
| --- | --- | --- | --- |
| Sitio web público | Compilación estática/CDN e historial del contenido | Navegación accesible, ausencia de contenido privado en la salida y recuperación del artefacto anterior | Aparezcan escrituras de confianza o límites medidos de publicación |
| SaaS | Aplicación modular, base de datos transaccional y proceso en segundo plano acotado | Aislamiento entre inquilinos, conciliación de pagos y restauración | Aparezca contención medida o responsabilidad independiente por dominio |
| Herramienta interna | SSO, aplicación pequeña, integraciones acotadas y auditoría | Los usuarios revocados no pueden leer ni exportar; el trabajo retrasado tiene responsables y seguimiento | Diverjan los responsables o las obligaciones de fiabilidad |
| Aplicación de IA | Adaptador de modelo, recuperación autorizada y conjunto de evaluación | Los documentos denegados no entran en el contexto del modelo; los fallos permanecen acotados | Cambien la calidad evaluada, el coste, la latencia o la residencia |
| Automatización con agentes | Registro duradero de ejecuciones, procesos acotados y herramientas con ámbito limitado | Duplicados, aprobaciones caducadas y paradas por presupuesto no pueden superar la autoridad concedida | Herramientas o cargas independientes necesiten límites de fallo separados |
| Móvil y backend | Caché del cliente, API compatible y reglas explícitas de sincronización | Recuperación sin conexión, conflictos y soporte de clientes antiguos | La presión de sincronización medida o la geografía justifiquen rediseñar |

## Sitio web público

Supón contenido público de autoría propia y ninguna escritura específica de usuario en el servidor. Compila un artefacto inmutable y publícalo mediante una identidad de despliegue revisada. Antes de publicar, navega y busca en cada idioma admitido con teclado y una ventana estrecha. Comprueba que ni la salida generada ni el índice de búsqueda contengan datos privados; un inicio de sesión en el cliente no protege archivos públicos. Despliega un artefacto anterior conocido en un entorno de prueba y verifica una ruta real. Añade una API protegida solo cuando el producto necesite escrituras de confianza; no conviertas un token de compilación estática en una credencial pública del navegador.

## SaaS con pagos

Supón varios inquilinos y un proveedor responsable de los cobros. Vincula cada operación al inquilino autenticado; conserva las transiciones locales de negocio con una identidad estable de operación. Antes de cambiar autorización o facturación, ejercita intentos de acceso a objetos y exportaciones de otros inquilinos, envíos duplicados y pérdida de una respuesta del proveedor. Inspecciona los registros locales y del proveedor, en lugar de confiar solo en un estado HTTP, para demostrar un único resultado de negocio previsto o un estado explícito de conciliación pendiente. Restaura una copia aislada, concilia los pagos y reanuda deliberadamente el trabajo pendiente. Introduce servicios solo por un beneficio medido de responsabilidad, aislamiento o capacidad.

## Herramienta interna

Supón un proveedor de identidad de la organización y una integración de negocio externa. El SSO establece la identidad; la aplicación sigue autorizando cada acción y exportación. Prueba la revocación tanto con una sesión actual como con un trabajo en cola dentro de la ventana de revocación acordada. Haz que la dependencia externa no esté disponible y verifica después que el trabajo pendiente sea visible y se reintente solo según su política. La conciliación utiliza un identificador estable de operación para que quien opere pueda determinar si se produjo una escritura en el sistema externo. Asigna a los registros de auditoría una persona responsable y una regla de retención; acceder a la red corporativa no es por sí solo autorización.

## Aplicación de IA

Supón una funcionalidad acotada del modelo que recupera documentos para un usuario autenticado. Aplica la autorización de documentos antes de que el contenido entre en resultados de recuperación o en el contexto del modelo y conserva el efecto de revocación y eliminación en índices y cachés. Antes de cambiar un modelo, prompt, ruta de recuperación o política, ejecuta evaluaciones representativas y adversariales reservadas para evaluación, con puntuación explícita y revisión humana donde haga falta criterio. Incluye documentos denegados, abstención, inyección de instrucciones y tiempo agotado del proveedor. Mide éxito y respaldo en fuentes junto con latencia y coste; un lenguaje plausible no equivale a corrección. Una alternativa segura puede desactivar la funcionalidad u ofrecer una búsqueda ordinaria autorizada.

## Automatización con agentes

Supón que las tareas en cola pueden provocar escrituras importantes mediante herramientas. El registro de ejecuciones conserva identidad de la tarea, ámbito autorizado, vinculación de la aprobación, intentos y resultado observable. Prueba una tarea duplicada, una aprobación caducada, una acción modificada después de aprobarla, instrucciones hostiles recuperadas y un presupuesto agotado. El límite de control debe detener las llamadas no autorizadas a herramientas con independencia de la cooperación del modelo. Usa destinos externos simulados o aislados para las pruebas de fallo. Después de una caída, concilia si se produjo el efecto antes de reanudar; reiniciar un proceso no debe repetir a ciegas una acción irreversible.

## Aplicación móvil y backend

Supón que no todos los clientes pueden actualizarse inmediatamente y que pueden editar sin conexión. Mantén la autorización y el estado canónico en el servidor, los datos locales necesarios en almacenamiento protegido adecuado a la plataforma y los conflictos regidos por una regla explícita. Antes de publicar, prueba el cliente más antiguo admitido contra la nueva API, la sincronización interrumpida, una carga repetida y ediciones concurrentes sin conexión. Verifica que revocar un dispositivo bloquee la renovación de acceso y las operaciones protegidas posteriores según el contrato de sesión documentado. No supongas que revocar borra los datos ya descargados en un dispositivo. La sincronización regional o particionada necesita evidencia sobre tasa de conflictos, latencia y coste de recuperación.

## Dar al agente una tarea comprobable

Para el perfil elegido, acuerda con la persona responsable la carga, el SLO/RTO/RPO, las reglas de datos y el presupuesto. Convierte sus casos planificados en pruebas para las tecnologías reales del proyecto mediante la [estrategia de pruebas](../guides/testing-strategy.md), el [plan de pruebas de rendimiento](../guides/performance-testing.md) y el [plan de pruebas de seguridad](../guides/security-testing.md). Registra preparación, estímulo, criterio observable del resultado correcto, casos negativos, condiciones de parada y evidencia conservada. Un agente debe distinguir una prueba propuesta de un resultado ejecutado e informar de un requisito previo ausente en lugar de inventar un éxito.

## Decisiones relacionadas

[Adopción](../guides/adoption.md) · [Arquitectura](../guides/architecture.md) · [Agentes](../guides/agents.md) · [Frontend](../guides/frontend.md) · [Estrategia de pruebas](../guides/testing-strategy.md)

## Evidencia primaria

[owasp](https://raw.githubusercontent.com/OWASP/ASVS/2b47a9dd16760ee484a6672d197f1f7e25d9c632/README.md) · [openai-agents](https://raw.githubusercontent.com/openai/openai-agents-python/841dfdd938bfd4ca052475eb76d6245a356868e0/docs/agents.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [wcag](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/index.html) · [azure-architecture-styles](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/guide/architecture-styles/index.md) · [azure-retry](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/retry-content.md) · [azure-idempotent-consumer](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/idempotent-consumer.md)
