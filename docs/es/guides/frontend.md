---
{
  "id": "frontend",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Arquitectura frontend y contratos

## Renderizar según la interacción

Generación estática para contenido, servidor para datos iniciales frescos o indexación, cliente para interacción prolongada. Decide el híbrido por ruta. Documenta hidratación, caché, autenticación y despliegue. Microfrontends responden a responsabilidad independiente de equipos, no son el modelo básico de componentes.

## Estado comprensible

Separa datos del servidor, URL/navegación, interacción local y preferencias persistentes. Asigna un responsable por estado; evita duplicar datos remotos en varios almacenes. Organiza por funciones e interfaces. Comparte primitivas accesibles antes de un gran sistema de diseño.

Define esquemas API, errores, paginación, cancelación y datos antiguos. El servidor valida entradas y autoriza cada operación protegida. Ocultar un botón no autoriza. Nunca incluyas secretos backend en bundles. Cancela efectos y limpia suscripciones; las actualizaciones optimistas necesitan reconciliación y ruta de error.

## Verificar y evolucionar

Prueba teclado, foco, nombres accesibles, contraste, carga, vacío, error, desconexión y pantallas estrechas. Mide navegación real, tamaño, latencia y errores JS. Añade BFF por agregación o límites de seguridad demostrados. Cambia de framework cuando las restricciones superen el coste migratorio, incluida accesibilidad y soporte. WebMCP es una mejora opcional: la interacción humana sigue funcionando sin él.

## Decisiones relacionadas

[Elegir y conectar arquitecturas](architecture.md) · [Controles que demuestran comportamiento](quality.md) · [Skills, plugins, MCP y WebMCP](integrations.md)

## Evidencia primaria

[wcag](https://raw.githubusercontent.com/w3c/wcag/main/guidelines/index.html) · [owasp](https://raw.githubusercontent.com/OWASP/ASVS/master/README.md) · [webmcp](https://raw.githubusercontent.com/webmachinelearning/webmcp/main/README.md)
