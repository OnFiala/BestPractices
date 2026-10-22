---
{
  "id": "self-hosting",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Operar servidores propios

## Topología mínima

Un proxy inverso con TLS dirige a la aplicación en una red privada; la base no es pública. Restringe y audita administración. Separa producción y experimentos; conserva copias en otro dominio de fallo y, si es viable, otra cuenta. Un host es un punto único de fallo: documenta interrupción aceptada y recuperación.

## Contrato operativo

Usa infraestructura como código, imágenes fijadas, privilegios mínimos, límites, volúmenes persistentes e inyección explícita de secretos. No expongas el socket Docker a la aplicación ni supongas que un contenedor es una sandbox fuerte. Define parches, renovación TLS, alertas de disco, retención de logs y guardias. Separa permisos de migración de los habituales.

Compose es un comienzo razonable para pocos servicios. La orquestación requiere necesidades demostradas de planificación, disponibilidad o equipos. Un servidor doméstico añade evaluación de energía, conectividad, seguridad física y recuperación externa.

## Ensayo de recuperación

Recrea un servidor limpio, restaura datos, verifica un recorrido real y mide RTO/RPO. Una copia terminada no basta. Prueba certificados y disco lleno en staging. Migra a servicios gestionados si el equipo no cumple mantenimiento o recuperación; las réplicas no sustituyen responsabilidad.

## Decisiones relacionadas

[Seguridad, privacidad y dependencias](security.md) · [Alojamiento y estrategias de salida](hosting.md) · [Salud, recuperación y costes](operations.md)

## Evidencia primaria

[docker-security](https://raw.githubusercontent.com/docker/docs/main/content/manuals/engine/security/_index.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml) · [opentofu](https://raw.githubusercontent.com/opentofu/opentofu/main/README.md)
