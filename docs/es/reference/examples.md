---
{
  "id": "examples",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Rutas de proyectos de referencia

## Seis rutas concretas

| Proyecto | Arquitectura inicial | Primera prueba | Señal de expansión |
| --- | --- | --- | --- |
| Web pública | Build estático, CDN, contenido Git | Búsqueda, teclado, reversión | Escrituras confiables necesitan API |
| SaaS | App modular, base relacional, worker | Tenants, reconciliación de pagos, restore | Contención medida o equipos independientes |
| Herramienta interna | SSO, app pequeña, auditoría | Cuenta revocada no exporta | Responsabilidades de integración distintas |
| Aplicación IA | API, adaptador, retrieval autorizado | Respuestas fundamentadas, documentos denegados, timeout | Límites medidos de calidad/coste |
| Automatización agente | Cola, worker limitado, registro durable, tools acotadas | Duplicados, parada presupuestaria, aprobación | Cargas independientes requieren responsables |
| Móvil + backend | UI, API versionada, caché local | Offline, conflictos, cliente antiguo | Límites medidos de sync/latencia |

`data/blueprints.json` detalla límites, aceptación, recuperación y migración. Son referencias de diseño, no aplicaciones desplegadas. Copia el perfil adecuado y convierte ejemplos en pruebas del stack real.

Los clientes móviles no actualizan a la vez. Prefiere APIs aditivas, sync reanudable, conflictos explícitos, revocación de dispositivos y almacenamiento seguro. Retrieval de IA debe conservar autorización y borrado; una respuesta plausible no demuestra corrección. La red corporativa no sustituye autorización por acción.

Acuerda presupuesto, SLO, residencia y recuperación con la persona responsable antes de lanzar. Un equipo pequeño puede elegir plataformas gestionadas para todas las rutas; contratos y obligaciones siguen siendo diferentes.

## Decisiones relacionadas

[Adoptar la biblioteca en un proyecto](../guides/adoption.md) · [Elegir y conectar arquitecturas](../guides/architecture.md) · [Dirección humana, ejecución de agentes](../guides/agents.md) · [Arquitectura frontend y contratos](../guides/frontend.md)

## Evidencia primaria

[owasp](https://raw.githubusercontent.com/OWASP/ASVS/master/README.md) · [openai-agents](https://raw.githubusercontent.com/openai/openai-agents-python/main/docs/agents.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml) · [wcag](https://raw.githubusercontent.com/w3c/wcag/main/guidelines/index.html)
