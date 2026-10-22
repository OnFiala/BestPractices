---
{
  "id": "foundations",
  "language": "es",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Principios de decisión

## Contexto y criterio inicial

Una arquitectura duradera permite sobrevivir a los cambios, los fallos y la pérdida de conocimiento individual. No promete que una misma combinación de tecnologías dure para siempre. Empieza con límites explícitos, pocas dependencias y una persona responsable de cada obligación operativa. Prefiere decisiones reversibles hasta que una evidencia más sólida justifique asumir un compromiso mayor.

## Perfiles de proyecto

| Perfil | Punto de partida | Obligaciones |
| --- | --- | --- |
| Personal o exploratorio | Sitio estático o un proceso; almacenamiento gestionado si hace falta | Preparación reproducible del entorno, gestión segura de secretos, exportación y restauración |
| Producto con usuarios reales | Aplicación modular, base de datos gestionada y proceso en segundo plano cuando sea necesario | Objetivos del servicio, prueba de recuperación, reversión del despliegue y responsable de soporte |
| Mucho tráfico o varios equipos | Partición basada en mediciones, contratos explícitos y planificación de capacidad | Cobertura de guardias, pruebas de carga, planes de aislamiento y migración |
| Consecuencias graves | Cualquier escala, incluso un solo usuario | Modelo de amenazas, capacidad de auditoría, retención y revisión legal y especializada |

Los perfiles describen restricciones, no una competición de madurez. Un servicio regulado pequeño puede necesitar controles más estrictos que un catálogo público grande. Documenta lo que aplazas deliberadamente y la señal que lo hará necesario.

## Registro de decisiones

Cada elección importante identifica el problema, las restricciones, las alternativas, la evidencia, la persona responsable, los costes esperados, la verificación y una vía de salida. Distingue los hechos de los supuestos y las reglas locales de los estándares externos. Fija una fecha de revisión y una condición observable que la active, por ejemplo una antigüedad de la cola que supere de forma sostenida el objetivo acordado.

## Verificar y revisar

Una persona que se incorpore al proyecto debe poder reproducir el flujo de desarrollo, seguir una acción del usuario hasta sus datos y recuperarse de una entrega fallida. Si solo el autor original o una sesión del modelo pueden explicar el sistema, mejora la documentación y los límites antes de añadir componentes. Revisa las decisiones después de incidentes, cambios importantes de coste, cambios de orientación del producto o nuevas obligaciones legales.

## Decisiones relacionadas

[Elegir y conectar arquitecturas](architecture.md) · [Escalar con mediciones](scaling.md) · [Gobierno y decisiones abiertas](governance.md)

## Evidencia primaria

[owasp](https://raw.githubusercontent.com/OWASP/ASVS/2b47a9dd16760ee484a6672d197f1f7e25d9c632/README.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md) · [github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md)
