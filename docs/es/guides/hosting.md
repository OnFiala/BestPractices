---
{
  "id": "hosting",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Alojamiento y estrategias de salida

## Comparar toda la obligación

| Opción | Uso adecuado | Costes incluidos |
| --- | --- | --- |
| Hosting estático/CDN | Documentación y archivos públicos | Límites de construcción, caché, dominio |
| Plataforma gestionada | Equipos pequeños de producto | Límites, tráfico saliente, runtimes, exportación |
| Funciones gestionadas | Trabajo acotado y variable | Duración, arranques y presión de conexiones |
| VPS con contenedores | Carga previsible y responsable operativo | Parches, copias, supervisión, recuperación y reserva |
| Kubernetes gestionado | Varias cargas y un equipo preparado | Políticas, actualizaciones, red y seguridad |

Gestionar delega tareas, no responsabilidad. Calcula cómputo, almacenamiento, tráfico, observabilidad, soporte y tiempo humano. Comprueba región, residencia, restauración, cuotas y dominios de fallo. El crecimiento esperado no basta para elegir Kubernetes.

## Contrato de portabilidad

Externaliza configuración, describe infraestructura como código, conserva el dominio y demuestra exportación. Despliega artefactos por digest. Identifica funciones específicas y dependencia aceptada; la portabilidad también cuesta.

## Verificar y migrar

En un entorno aislado prueba una petición funcional, restauración, rotación y coste máximo. Ensaya exportar, importar, reconciliar, cambiar tráfico, observar y volver atrás. Revertir DNS no revierte escrituras posteriores. Esta biblioteca usa hosting estático; el despliegue manual de Pages no aloja el servidor MCP.

## Decisiones relacionadas

[Operar servidores propios](self-hosting.md) · [Escalar con mediciones](scaling.md) · [Salud, recuperación y costes](operations.md)

## Evidencia primaria

[docker-security](https://raw.githubusercontent.com/docker/docs/main/content/manuals/engine/security/_index.md) · [kubernetes](https://raw.githubusercontent.com/kubernetes/website/main/content/en/docs/concepts/architecture/_index.md) · [opentofu](https://raw.githubusercontent.com/opentofu/opentofu/main/README.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml)
