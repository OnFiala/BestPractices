---
{
  "id": "lifecycle",
  "language": "es",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# El ciclo de vida completo del proyecto

## Usar evidencia para completar cada etapa

Las etapas siguientes son el modelo operativo propuesto por esta biblioteca. Su profundidad varía según el impacto y las responsabilidades; sus nombres no constituyen una certificación externa. Un script personal puede usar un registro breve, mientras que un servicio con consecuencias graves necesita evidencia independiente de dominio y seguridad.

| Etapa | Artefacto requerido | Evidencia para completarla |
| --- | --- | --- |
| Descubrir | Descripción del problema y mapa de partes interesadas y datos | Resultado medible para el usuario, exclusiones explícitas y una persona responsable |
| Diseñar | Perfil del proyecto, diagrama de contexto, ADR y modelo de amenazas | Aceptación humana de restricciones, presupuesto y objetivos de recuperación |
| Planificar | Lista breve de tareas y plan de pruebas | Cada tarea tiene ámbito, responsable, casos de fallo y condiciones de parada |
| Construir | Código, migraciones, pruebas y explicación actualizada | Comprobaciones reproducibles y diff visible para quien revise |
| Publicar | Artefacto versionado, plan de despliegue y recuperación | Aceptación en preproducción, evidencia de migración y restauración y aprobación humana |
| Operar | Manual operativo, mediciones del servicio y responsabilidad sobre costes | Objetivos medidos, alertas accionables y recuperación ejercitada |
| Evolucionar | Aprendizaje de incidentes y registro de migración o retirada | Los consumidores admitidos migran antes de retirar compatibilidad |
| Retirar | Plan de exportación, eliminación y revocación de acceso | Obligaciones de retención cumplidas, integraciones externas cerradas y facturación comprobada |

Un artefacto se justifica cuando apoya una decisión o acción. Un documento generado que nadie puede utilizar no es evidencia de preparación.

## Hacer de las pruebas una actividad continua

Durante el descubrimiento, define qué demostraría que no se cumple el resultado para el usuario. Durante el diseño, identifica invariantes y límites de confianza que merezcan pruebas más estrictas. Antes de que un agente escriba código, establece ejemplos de aceptación y el comportamiento esperado ante fallos; usa la [estrategia de pruebas](testing-strategy.md) para elegir el conjunto útil más pequeño.

Durante la implementación, ejecuta comprobaciones específicas del límite modificado. En integración y publicación, verifica compatibilidad, acciones denegadas y recorridos críticos a través de interfaces públicas. Usa [pruebas de rendimiento](performance-testing.md) antes de entregas sensibles a la capacidad y migraciones planificadas, con límites y autorización explícitos. Aplica [pruebas de seguridad](security-testing.md) cuando cambien identidad, sensibilidad de datos, entradas externas, dependencias o autoridad de herramientas. La operación devuelve al plan simulacros de restauración, regresiones de incidentes y observaciones de carga real.

Una compilación correcta no satisface un criterio de aceptación incumplido. Registra por separado las comprobaciones fallidas, omitidas y no ejecutadas, con una persona responsable del riesgo pendiente. La aprobación se refiere al artefacto y contexto probados; un cambio significativo posterior necesita una nueva revisión.

## Responsabilidades humanas y de agentes

La persona responsable elige el valor, la prioridad, el riesgo aceptable, la dirección arquitectónica y la autoridad de publicación. Los agentes investigan, redactan, implementan, prueban e informan de la incertidumbre dentro de sus capacidades asignadas. Separa los roles de implementación y verificación cuando las consecuencias lo justifiquen; varios agentes que repiten el mismo supuesto no constituyen evidencia independiente.

Conserva decisiones, identificadores de ejecución, versiones de artefactos e información de recuperación en el repositorio, no solo en un chat. Una tarea acotada termina con su resultado real y las preguntas pendientes, incluido el motivo de rechazar un diseño propuesto. Nunca presentes una prueba no ejecutada ni una lista de revisión generada como aprobación humana.

## Cambiar de rumbo y cerrar el sistema

Demuestra un recorrido funcional completo, incluidas rutas de error y acceso denegado, antes de ampliar funcionalidades. Si el resultado no se puede medir, vuelve al descubrimiento. Si las responsabilidades o el coste operativo no son sostenibles, simplifica la arquitectura en lugar de añadir automatización desatendida.

Planifica la retirada desde la creación: ¿cómo exportan datos los usuarios, qué registros deben conservarse y cómo se revocan credenciales y accesos delegados a agentes? Prueba la exportación y el cierre antes de que sean urgentes. Retira trabajos programados, recursos de proveedores y copias de recuperación según la política de retención acordada; borrar el repositorio de la aplicación no equivale a un cierre completo.

## Decisiones relacionadas

[Estrategia de pruebas](testing-strategy.md) · [Controles de calidad](quality.md) · [Operación](operations.md) · [Agentes](agents.md) · [Adopción](adoption.md)

## Evidencia primaria

[github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml)
