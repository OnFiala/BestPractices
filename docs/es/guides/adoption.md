---
{
  "id": "adoption",
  "language": "es",
  "revision": 3,
  "translation_revision": 3,
  "reviewed_on": "2026-10-22"
}
---
# Adoptar la biblioteca en un proyecto

## Empezar por una ruta de entrega

Si empiezas a usar la biblioteca, sigue
[tu primer punto de control con evidencias](first-project.md) y después utiliza
[el flujo de entrega](project-delivery.md) con la guía de tu tipo de proyecto.
Producirás un plan, una pequeña parte del trabajo, una observación real y una revisión.
Un **punto de control** exige determinados resultados y establece condiciones de bloqueo.
Un **artefacto** es un resultado, como un documento de decisión, un cambio de código
fuente o un informe de pruebas. Las **evidencias** registran lo que alguien inspeccionó
o ejecutó realmente sobre ese resultado. Una comprobación planificada no es una
observación, y una plantilla rellenada no es una aprobación.

## Usar el perfil adecuado

| Archivo | Propósito | Quién lo lee |
| --- | --- | --- |
| `templates/delivery-profile.json` | Ejemplo de la entrada con esquema JSON estricto: tipo de proyecto, revisión exacta de destino, riesgo, datos, carga de trabajo, hosting, superficies, efectos y objetivos | `library.delivery plan`, `library.delivery assess` y `library.project init` |
| `project-profile.json` | El perfil de entrega JSON rellenado de tu proyecto; este es el nombre que genera `init` | Las mismas herramientas; cambia el nombre del archivo, no el esquema |
| `templates/project-profile.yaml` | Documento detallado opcional para decisiones: responsable, presupuesto, objetivos del servicio, residencia de datos, recuperación y excepciones | Personas y agentes; la CLI no lo lee ni lo convierte |

Empieza por la plantilla JSON para la planificación ejecutable. Sustituye sus
requisitos sintéticos por decisiones reales del proyecto. Para un proyecto existente,
conserva el perfil y las evidencias en la ubicación aprobada de ese proyecto y
ejecuta la CLI de la biblioteca con rutas explícitas. No ejecutes `init` sobre un
proyecto existente: solo crea un destino nuevo. Para un nuevo paquete portable,
`init` copia las herramientas necesarias, las guías, las licencias y los ejemplos
de referencia seleccionados; estos no son tu producto terminado.
Si solo necesitas leer y apoyar decisiones, enlaza las guías pertinentes y copia
únicamente las plantillas necesarias; no hace falta generar un paquete ni usar MCP.

Si también mantienes el documento YAML, traslada las decisiones de forma deliberada:

| Documento de decisiones | Perfil de entrega | Qué requiere interpretación |
| --- | --- | --- |
| `name`, `outcome`, `non_goals` | `project_id`, `description`, `objectives`, `constraints` | Elige un identificador estable válido y resultados observables; no te limites a renombrar claves |
| `data.classification` | `data_sensitivity` | Selecciona una categoría admitida después de revisar los datos reales |
| Campos de `workload` medidos | `workload` | Elige una categoría justificada; usa `unmeasured` cuando falten mediciones |
| `library_revision` | No hay un campo correspondiente en el perfil | Fija la revisión de la biblioteca por separado; `revision` en JSON significa el commit Git del proyecto de destino |
| Responsable, presupuesto, objetivos del servicio, residencia de datos, recuperación, excepciones | Consérvalos en el documento y en los artefactos de los puntos de control pertinentes | Estas obligaciones siguen siendo relevantes; el planificador no evalúa esos campos YAML |

El tipo de proyecto, el hosting, las superficies, los efectos y el riesgo también
requieren decisiones explícitas en JSON. No hay conversión ni sincronización automática.
Cuando cambien los supuestos compartidos, actualiza ambos documentos, vuelve a generar
el plan y reevalúa las evidencias afectadas. No añadas al esquema JSON estricto campos
que solo pertenecen a YAML. Fija la biblioteca a una versión revisada o a un commit
completo y utiliza identificadores estables de las guías. Seguir silenciosamente
la rama mutable `main` puede cambiar las reglas del proyecto sin su aprobación.

Crea un diagrama de contexto y un ADR para la primera decisión importante. Registra las recomendaciones aceptadas, los controles aplazados deliberadamente, una persona responsable, una fecha de caducidad y comprobaciones compensatorias. Conserva las instrucciones específicas del proyecto para los agentes en `AGENTS.md` y enlaza los materiales de apoyo. Esta biblioteca es una fuente de propuestas mantenida por agentes. Sus recomendaciones solo se convierten en reglas del proyecto mediante el proceso humano de decisión del propio proyecto.

## Tres ejemplos iniciales

- **Sitio web público personal:** utiliza una compilación estática, historial del contenido y un despliegue reproducible. Mantén las notas privadas, las credenciales y los datos personales de origen fuera del historial público de Git y de los archivos públicos generados, incluidos los índices de búsqueda. Una pantalla de inicio de sesión no protege los archivos que se pueden descargar públicamente. Una base de conocimiento privada necesita almacenamiento privado y comprobaciones de acceso aplicadas por el servidor a documentos, recursos, descargas y búsquedas; un repositorio privado no convierte por sí solo su publicación en privada.
- **SaaS pequeño:** empieza con una aplicación modular, una base de datos transaccional y un proceso en segundo plano solo donde haga falta. Define los límites entre inquilinos —clientes con datos separados—, la conciliación de pagos y una persona responsable de la operación. Antes de aceptar clientes reales, demuestra la denegación de acceso entre inquilinos, la compatibilidad durante el despliegue y la restauración en un entorno aislado.
- **Plataforma de tráfico elevado:** primero mide la mezcla de tráfico, su distribución desigual, el crecimiento de los datos y los límites de las dependencias. Particiona o aísla una carga de trabajo solo después de demostrar la restricción y asignar responsabilidades sobre coherencia, migración, respuesta de guardia y recuperación. Un número elevado de cuentas no determina por sí solo una necesidad de capacidad.

Estas son recomendaciones iniciales originales, no recetas universales ni plantillas de despliegue sometidas a pruebas comparativas de rendimiento.

## Convertir las recomendaciones en evidencia de aceptación

Para cada guía adoptada, identifica la obligación observable y la comprobación que podría refutar su cumplimiento. Por ejemplo, «aislamiento entre inquilinos» se convierte en una prueba en la que la sesión autenticada del inquilino A solicita un objeto del inquilino B por las rutas de API, exportación y procesos en segundo plano, y ninguna devuelve datos de B. Registra la preparación de la prueba, el resultado esperado, la revisión ejecutada y la evidencia conservada en la [estrategia de pruebas](testing-strategy.md).

Usa los [perfiles de referencia](../reference/examples.md) para detectar límites que falten. Una condición de aceptación que no se ha ejecutado es una prueba planificada, no una demostración. No declares un sistema seguro porque se haya rellenado una plantilla o un resumen generado diga «superado». Revisa el resultado real, incluidos los fallos y las omisiones.

## Revisar sin perder el control

Consulta las guías aplicables durante la planificación y enlázalas en la tarea de implementación. Durante la revisión, compara el diff con la decisión elegida y los casos de fallo. Antes de publicar, valida la migración y la recuperación; durante la operación, incorpora las mediciones y los incidentes a los ADR. Actualiza la versión fijada de la biblioteca mediante un PR que explique las obligaciones modificadas, los proyectos afectados y el plan de migración o excepción.

Si una nueva recomendación no se puede validar dentro del presupuesto del proyecto o de la capacidad de sus responsables, registra esa carencia y simplifica el diseño. No aceptes silenciosamente una regla que nadie pueda operar.

## Decisiones relacionadas

[Principios de decisión](foundations.md) · [El ciclo de vida completo](lifecycle.md) · [Estrategia de pruebas](testing-strategy.md) · [Dirección humana, ejecución de agentes](agents.md) · [Gobierno y decisiones abiertas](governance.md)

## Evidencia primaria

[plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md) · [github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md)
