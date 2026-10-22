---
{
  "id": "foundations",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Principios de decisión

## Contexto y criterio inicial

Una arquitectura duradera sobrevive a cambios, fallos y pérdida de conocimiento individual. No promete un stack eterno. Empieza con límites explícitos, pocas dependencias y una persona responsable de cada obligación operativa. Prefiere decisiones reversibles hasta que existan pruebas para asumir un compromiso mayor.

## Perfiles de proyecto

| Perfil | Punto de partida | Obligaciones |
| --- | --- | --- |
| Personal o exploratorio | Sitio estático o un proceso, almacenamiento gestionado si hace falta | Instalación reproducible, secretos protegidos, exportación y restauración |
| Producto con usuarios | Aplicación modular, base gestionada, worker cuando sea necesario | Objetivos del servicio, restauración, reversión del despliegue, soporte |
| Mucho tráfico o varios equipos | Partición medida, contratos explícitos, planificación de capacidad | Guardias, pruebas de carga, aislamiento y migración |
| Consecuencias graves | Cualquier escala, incluso un usuario | Modelo de amenazas, auditoría, retención, revisión legal y especializada |

Los perfiles describen restricciones, no una competición de madurez. Un servicio regulado pequeño puede necesitar más controles que un catálogo público grande. Documenta lo que aplazas y la señal que lo hará necesario.

## Registro de decisiones

Cada elección importante identifica problema, restricciones, alternativas, evidencia, responsable, costes, validación y salida. Distingue hechos de supuestos y reglas locales de estándares externos. Fija una fecha de revisión y un disparador observable, por ejemplo una cola cuya antigüedad supera persistentemente el objetivo.

## Verificar y revisar

Una persona nueva debe reproducir el entorno, seguir una acción hasta sus datos y recuperarse de una entrega fallida. Si solo el autor original o una sesión del modelo puede explicar el sistema, mejora primero documentación y límites. Revisa las decisiones después de incidentes, variaciones importantes de coste, cambios de producto u obligaciones legales.

## Decisiones relacionadas

[Elegir y conectar arquitecturas](architecture.md) · [Escalar con mediciones](scaling.md) · [Gobierno y decisiones abiertas](governance.md)

## Evidencia primaria

[owasp](https://raw.githubusercontent.com/OWASP/ASVS/master/README.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/main/content/en/docs/concepts/observability-primer.md) · [github-rulesets](https://raw.githubusercontent.com/github/docs/main/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md)
