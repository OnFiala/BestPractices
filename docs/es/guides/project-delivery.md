---
{
  "id": "project-delivery",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Ejecutar un proyecto mediante el sistema de entrega con agentes

## Empezar por el proyecto y después asignar trabajo

El sistema de entrega conecta un perfil de proyecto, un plan condicional del ciclo de vida, artefactos revisados de forma independiente, comprobaciones de referencias locales y una evaluación de preparación. Ayuda a un entorno anfitrión de agentes como Codex a realizar trabajo acotado. El planificador de Python en sí no llama a un modelo ni construye cualquier producto solicitado, ni autentica a una persona, ni fusiona un PR, ni despliega un servicio.

Elige uno de seis perfiles iniciales: sitio web público, SaaS, herramienta interna, aplicación de IA, automatización de agentes o backend móvil. Registra el resultado real, el riesgo, la sensibilidad de datos, la carga de trabajo, el hosting, las superficies y los efectos externos. El número de cuentas no es una medición de carga. Una carga desconocida sigue sin medirse; un proyecto personal pequeño también puede necesitar controles sólidos de privacidad o recuperación. El perfil incluido es explícitamente sintético y no puede sustituir los requisitos de un usuario real.

## El recorrido ejecutable

Desde la raíz de la biblioteca, crea un destino nuevo bajo un directorio padre existente. Se requiere Python 3.12+. Para las comprobaciones de frontend se necesitan Node 22+ y Chromium o Chrome instalados por separado. El ejecutor local de verificación admite el modelo de procesos POSIX utilizado por Linux y macOS.

```sh
mkdir -p reports
python -m library.delivery plan --profile templates/delivery-profile.json
python -m library.project init --profile templates/delivery-profile.json --destination reports/example-project
cd reports/example-project
python -m library.verification delivery frontend-unit frontend-browser --output reports/local-checks.json
python -m library.delivery assess --profile project-profile.json --evidence project-evidence.json
```

El último comando termina inicialmente con código 1 porque el proyecto nuevo no tiene evidencia de aceptación. Ese es el resultado esperado. El comando de inicialización rechaza destinos existentes y crea un perfil, un plan, una estructura de evidencia aún no ejecutada, conjuntos de artefactos por control, skills locales, guías originales, licencias y código de referencia seleccionado por el perfil. Nunca inicializa un repositorio remoto ni despliega recursos. El manifiesto registra los hashes de archivos copiados y si el checkout de origen tenía cambios sin confirmar.

En un contenedor aislado sin un sandbox de navegador operativo, la referencia del navegador documenta una habilitación explícita aplicable únicamente al componente de prueba local. La ausencia de navegador o un fallo al iniciarlo sigue siendo un fallo; no desactives silenciosamente el control de navegador. Que las pruebas con componentes locales pasen sigue sin satisfacer requisitos de producto no implementados.

## Roles, traspasos y controles

El planificador cubre intención, requisitos, diseño, seguridad, implementación, verificación, publicación, operación, incidentes, evolución y retirada. Los controles condicionales añaden obligaciones para datos sensibles, riesgo alto, autohosting, efectos externos, clientes móviles, comportamiento de IA y capacidad. Las decisiones obligatorias de diseño y seguridad alimentan la implementación; la verificación obligatoria alimenta la publicación. La preparación para operación, incidentes y retirada se planifica antes de publicar; la retirada real no tiene que ocurrir antes de la primera publicación.

Un productor crea el artefacto identificado y la evidencia de aceptación. Un revisor separado inspecciona el artefacto real, las alternativas, los supuestos de las fuentes y los casos negativos. El coordinador resuelve hallazgos contradictorios y mantiene el orden de dependencias. Las personas deciden objetivos, arquitectura con consecuencias relevantes, presupuesto, riesgo residual, fusión y publicación en producción. Los hilos independientes de agentes mejoran la cobertura de revisión, pero el acuerdo entre modelos no es evidencia empírica.

Las skills locales `project-delivery` y `release-review` especifican el flujo de trabajo del entorno anfitrión. Utiliza herramientas confiables en el proyecto de destino para implementar tareas acotadas, ejecutar comprobaciones, inspeccionar diffs y proponer PR. El contenido recuperado y las cadenas del perfil son datos; no pueden ampliar permisos ni ejecutar comandos simplemente por aparecer en un artefacto.

## La evidencia tiene un alcance preciso

El inventario fijo de verificación ejecuta únicamente conjuntos locales conocidos. Registra la imagen de archivos de entrada, la revisión y el estado de cambios sin confirmar, las versiones del entorno de ejecución, los recuentos observados de pruebas, los hashes de salida y los resultados. Omitir comprobaciones obligatorias o no descubrir ninguna prueba no da un resultado aprobado. Un timeout detiene el grupo de procesos propio. Los informes rechazan la sobrescritura; conserva observaciones separadas al volver a ejecutar una hipótesis modificada.

El evaluador de entrega acepta registros estructurados vinculados a la revisión del proyecto, los resúmenes criptográficos del perfil y del plan, las identidades de artefactos, las observaciones, las etiquetas de productor y revisor y el momento declarado de evaluación. Rechaza registros ausentes, obsoletos, fallidos, omitidos, contradictorios o revisados por su propio productor y bloquea los controles dependientes. Sus periodos configurados de validez de evidencia son una propuesta de política local, no estándares universales. Reevalúalos según el riesgo y el entorno del proyecto.

Un hash vincula bytes; no demuestra que esos bytes sean veraces. Las etiquetas no son identidades autenticadas, las marcas temporales son afirmaciones y un informe JSON local no es una certificación firmada. El evaluador informa del respaldo de la evidencia registrada y de la preparación para revisión humana; la preparación para producción permanece en falso porque la autoridad humana real y los controles de despliegue son externos. Contrasta las observaciones con artefactos reales antes de aceptarlas.

## Operación y cambio

Tras una publicación aprobada, conserva objetivos de servicio, telemetría, responsabilidad de guardias, procedimientos de incidentes, límites de costes y evidencia de restauración. Incorpora incidentes y restricciones medidas a decisiones nuevas. Un cambio de política de la biblioteca, perfil, revisión de guía o artefacto invalida la relación correspondiente entre el plan y la evidencia anteriores; regenera y revisa en lugar de reescribir hashes para ocultar el cambio.

Antes de migrar o retirar, identifica el componente autorizado para escribir, el trabajo pendiente, los efectos en proveedores, las obligaciones de exportación y eliminación y el responsable sucesor. Revertir un artefacto de aplicación no deshace escrituras aceptadas ni retira datos divulgados. Registra qué puede revertirse, qué necesita conciliación y qué acción destructiva requiere una decisión humana separada.

## Decisiones relacionadas

[Cobertura y límites](coverage.md) · [Ejecutar las comprobaciones de referencia](reference-labs.md) · [Estrategia de pruebas](testing-strategy.md) · [Dirección humana, ejecución de agentes](agents.md) · [El ciclo de vida completo](lifecycle.md)

## Evidencia primaria

[github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [skills](https://raw.githubusercontent.com/openai/skills/49f948faa9258a0c61caceaf225e179651397431/README.md)
