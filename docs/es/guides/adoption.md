---
{
  "id": "adoption",
  "language": "es",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Adoptar la biblioteca en un proyecto

## Crear un conjunto de decisiones portable

Copia las plantillas que necesites, no toda la biblioteca. Completa `project-profile.yaml` con el resultado esperado, la sensibilidad de los datos, la persona responsable, la carga de trabajo, el presupuesto, los objetivos del servicio y los supuestos de recuperación. Fija esta biblioteca a una versión revisada o a un commit completo y utiliza identificadores estables de las guías. Seguir silenciosamente la rama mutable `main` puede cambiar las reglas de producción sin la aprobación del proyecto.

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
