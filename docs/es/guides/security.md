---
{
  "id": "security",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Seguridad, privacidad y dependencias

## Activos y límites primero

Identifica datos sensibles, actores, entradas, fronteras y abusos plausibles. Los controles dependen del impacto, no del tamaño. Valida en servidores confiables, autoriza objetos y acciones, minimiza datos y define retención y borrado. Obligaciones legales y sectoriales necesitan revisión humana cualificada; esta biblioteca no certifica cumplimiento.

## Entrega y ejecución

Separa identidades de desarrollo, CI y producción; prefiere credenciales breves y limitadas, almacenes de secretos y rotación. Bloquea dependencias y fija Actions por commit completo. Revisa actualizaciones, licencias, procedencia y vulnerabilidades. Mantén TLS, firmas y checksums.

No ejecutes PRs no confiables con secretos productivos ni `pull_request_target` privilegiado. No montes el socket Docker del host en agentes. Limita destinos y operaciones; descripciones y documentos son entradas no confiables. Un prompt no impone autorización.

## Verificar y responder

Prueba límites entre tenants, denegaciones, revocación y rotación. Busca datos sensibles en logs. Documenta contacto, contención, recuperación y comunicación de incidentes. Revisa amenazas antes de entregar funciones sensibles. Aumenta protección con sensibilidad e impacto, sin esperar más usuarios.

## Decisiones relacionadas

[Dirección humana, ejecución de agentes](agents.md) · [Operar servidores propios](self-hosting.md) · [Datos, contratos y migraciones](data.md)

## Evidencia primaria

[owasp](https://raw.githubusercontent.com/OWASP/ASVS/master/README.md) · [docker-security](https://raw.githubusercontent.com/docker/docs/main/content/manuals/engine/security/_index.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/main/content/actions/reference/security/secure-use.md)
