---
{
  "id": "hosting",
  "language": "es",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Alojamiento y estrategias de salida

## Comparar la obligación completa

Empieza por la clasificación y residencia de los datos, la forma del tráfico, los objetivos de recuperación, los operadores disponibles y el presupuesto. La comparación siguiente es una ayuda original de esta biblioteca para elegir. La documentación del producto debe aportar los datos actuales de regiones, cuotas, soporte y precios del despliegue real; una categoría de producto no es una garantía de servicio.

| Opción | Encaje útil | Coste y responsabilidad que se deben comprobar |
| --- | --- | --- |
| Alojamiento estático/CDN | Documentación pública y recursos inmutables | Límites de compilación, reglas de caché, control del dominio y ausencia de contenido privado en la salida |
| Plataforma de aplicaciones gestionada | Un equipo pequeño que entrega una aplicación | Entornos de ejecución admitidos, red, alcance de las copias de seguridad, exportación y tráfico saliente |
| Funciones gestionadas | Operaciones acotadas con picos de carga | Límites de ejecución, arranques en frío, concurrencia, conjuntos de conexiones y reintentos |
| VPS o anfitrión de contenedores | Trabajo previsible con una persona responsable de operarlo | Parches, certificados, supervisión, copias de seguridad, tiempo de restauración y capacidad de reserva |
| Kubernetes gestionado | Varias cargas con necesidades justificadas de planificación o aislamiento | Políticas del clúster y de las cargas, actualizaciones, red, capacidad y experiencia en incidentes |

Los servicios gestionados transfieren determinadas tareas operativas; no transfieren la responsabilidad de autorizar acciones de la aplicación, clasificar los datos ni demostrar la recuperación. Compara cómputo, almacenamiento, tráfico saliente, observabilidad, soporte, llamadas de pago a modelos y tiempo humano. Incluye los costes de picos, solicitudes fallidas y reintentos, no solo una estimación mensual en reposo.

## Registrar la decisión de alojamiento

Identifica a la persona responsable del servicio, los dominios de fallo, las versiones de ejecución admitidas, la identidad de despliegue y el resumen criptográfico del artefacto. Especifica cómo se separa producción de los experimentos, cómo llegan los secretos, cómo se autentica el acceso público y qué almacenes de datos son privados. Contrasta las cuotas y las capacidades documentadas de restauración con el RTO/RPO de la aplicación. Ten en cuenta tanto el bloqueo de la cuenta del proveedor como una caída regional.

Mantén la configuración externa y la infraestructura reproducible. Conserva el control del dominio y del formato de exportación de datos. Enumera las funciones específicas del proveedor y el coste de migración aceptado; la portabilidad implica compensaciones y no exige eliminar todos los servicios gestionados. Una plataforma que ofrece copias de seguridad automáticas sigue necesitando un simulacro de restauración a nivel de aplicación.

## Demostrar la opción elegida

Antes de la primera publicación en producción, despliega un entorno aislado y completa un recorrido real de usuario. Ejercita el acceso denegado, la rotación de credenciales, un despliegue fallido y la restauración de datos. Usa [pruebas de rendimiento](performance-testing.md) para establecer el tráfico sostenible y [pruebas de seguridad](security-testing.md) para los límites de entrada, separación entre inquilinos e identidad. Registra la versión desplegada, los ajustes relevantes de la plataforma y los resultados observados; un panel que diga «saludable» no basta.

Como ejemplo, compara una aplicación y base de datos gestionadas con un VPS para el mismo SaaS pequeño. El VPS puede tener una factura de infraestructura menor y, a la vez, exigir una persona responsable de parches y recuperación. Elige según el coste medido y la capacidad de cumplir el contrato operativo, no según el precio anunciado más bajo. Este ejemplo es un ejercicio de decisión, no un despliegue de referencia con precios o rendimiento medidos.

## Salida y recuperación

Ensaya la exportación e importación con una copia de datos que tenga características de producción. Comprueba recuentos de registros, totales de negocio, correspondencias de identidades, secretos, almacenamiento de objetos y estado de los procesos en segundo plano. Planifica el escritor autoritativo durante la transición, la ventana de observación y las condiciones para detener la migración del tráfico. Mantén recuperable la ruta anterior solo mientras sus datos sigan siendo coherentes con el plan de recuperación elegido.

Revertir el DNS no revierte las escrituras aceptadas por el nuevo sistema. Después de la transición, la reversión puede necesitar suspender escrituras, conciliar o reparar hacia delante. Prueba ese plan antes de una migración con consecuencias importantes. El sitio de esta biblioteca utiliza alojamiento estático; publicar en Pages no despliega su servidor MCP local.

## Decisiones relacionadas

[Alojamiento propio](self-hosting.md) · [Escalado](scaling.md) · [Operación](operations.md) · [Pruebas de rendimiento](performance-testing.md) · [Pruebas de seguridad](security-testing.md)

## Evidencia primaria

[docker-security](https://raw.githubusercontent.com/docker/docs/4d64a8e4f0a59967fc0b391120d54a90e9ccb60d/content/manuals/engine/security/_index.md) · [kubernetes](https://raw.githubusercontent.com/kubernetes/website/bc7f3479bc8b0af48097b155c22c8d58e8e1afe4/content/en/docs/concepts/architecture/_index.md) · [opentofu](https://raw.githubusercontent.com/opentofu/opentofu/ec773ed37be4d07e00d4a2fbb237d0c0fe1ca3ce/README.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml)
