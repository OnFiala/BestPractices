---
{
  "id": "self-hosting",
  "language": "es",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Operar servidores propios

## Definir la topología y sus límites

Un servicio público pequeño puede colocar un proxy inverso TLS en el límite de entrada, una aplicación en una red privada y una base de datos accesible solo para identidades autorizadas de aplicación y administración. La ubicación en la red complementa la autenticación; no sustituye la autorización. Separa producción de los experimentos y proporciona al acceso administrativo una ruta restringida y auditable. Una sola máquina sigue siendo un único dominio de fallo aunque ejecute varios contenedores.

El contrato operativo mínimo siguiente es una recomendación de la biblioteca basada en documentación de seguridad de contenedores y recuperación. Adáptalo a la plataforma y al impacto; no es una configuración de servidor reforzada y lista para desplegar.

| Obligación | Qué registrar y verificar |
| --- | --- |
| Administración | Persona responsable, acceso acotado, ruta de revocación y evidencia de acceso denegado |
| Actualizaciones | Sistema operativo y entorno de ejecución con soporte, responsable de parches, ventana de mantenimiento y artefacto de recuperación |
| Aislamiento de recursos | Límites de CPU, memoria y disco, alertas de capacidad y comportamiento ante agotamiento |
| Secretos | Mecanismo de inyección y rotación; identidades separadas para despliegue, migración y aplicación |
| Persistencia | Volúmenes de datos explícitos, alcance de copias de seguridad, cifrado, acceso a claves y retención |
| Límite público | Renovación de TLS, puertos permitidos, autenticación y respuestas de error seguras |
| Recuperación | Copia de seguridad fuera del anfitrión, última restauración correcta, RTO/RPO y contacto para incidentes |

Prefiere una cuenta o un dominio de fallo separado para las copias de seguridad cuando sea viable. Una copia en el mismo disco con permiso de escritura puede fallar junto con el servidor o ser eliminada por la misma identidad comprometida. Verifica que restaurar no dependa de credenciales almacenadas únicamente en el anfitrión perdido.

## Desplegar una unidad reproducible

Usa infraestructura como código y fija la imagen desplegable mediante su resumen criptográfico. Guarda el estado de la aplicación en persistencia gestionada explícitamente, no por accidente en una capa del contenedor. No expongas el socket de Docker a la aplicación o al agente ni trates un contenedor como un aislamiento fuerte frente a código hostil. Restringe privilegios y recursos a lo que necesite la carga.

Compose puede encajar en unos pocos servicios con un comportamiento de fallos y actualizaciones comprendido. Adopta orquestación cuando los requisitos de planificación, disponibilidad o equipo justifiquen su carga operativa. Más réplicas en una máquina no convierten esa máquina en altamente disponible. Un servidor doméstico necesita además evaluar alimentación eléctrica, conectividad, acceso físico y recuperación fuera de la ubicación.

## Simulacro de fallos y recuperación

En una máquina de prueba separada, recrea el anfitrión a partir de la configuración registrada y restaura una copia reciente. Desactiva correo real, pagos y otros efectos externos. Valida un recorrido representativo de usuario, permisos de los inquilinos, totales de negocio y trabajo en cola antes de declarar correcta la restauración. Mide el tiempo de recuperación y la ventana real de pérdida de datos frente a los objetivos acordados.

Antes de un cambio importante de alojamiento, usa [pruebas de rendimiento](performance-testing.md) para ejercitar sobrecarga y recuperación acotadas en un entorno autorizado. Prueba de forma segura la presión sobre el disco, una aplicación detenida, una base de datos no disponible y la renovación de certificados. Usa [pruebas de seguridad](security-testing.md) para verificar desde el límite público que los puertos administrativos y de base de datos están cerrados y que las credenciales revocadas no funcionan.

Una prueba solo pasa cuando el comportamiento visible para el usuario y el estado registrado cumplen el contrato de aceptación. Si la recuperación depende de pasos manuales no documentados, regístralos y repite el simulacro. Pasa a un servicio gestionado o reduce el alcance cuando las personas responsables no puedan cumplir las obligaciones de parches, respuesta o recuperación; añadir maquinaria no resuelve la falta de responsabilidad operativa.

## Decisiones relacionadas

[Seguridad](security.md) · [Alojamiento](hosting.md) · [Operación](operations.md) · [Pruebas de rendimiento](performance-testing.md) · [Pruebas de seguridad](security-testing.md)

## Evidencia primaria

[docker-security](https://raw.githubusercontent.com/docker/docs/4d64a8e4f0a59967fc0b391120d54a90e9ccb60d/content/manuals/engine/security/_index.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [opentofu](https://raw.githubusercontent.com/opentofu/opentofu/ec773ed37be4d07e00d4a2fbb237d0c0fe1ca3ce/README.md)
