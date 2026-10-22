---
{
  "id": "architecture",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Elegir y conectar arquitecturas

## Elegir según acoplamiento y responsabilidad

| Enfoque | Cuándo usarlo | Coste y señal de cambio |
| --- | --- | --- |
| Sitio estático | Contenido poco cambiante, sin secretos de servidor | Construcción y edición; backend para escrituras confiables |
| Monolito modular | Un producto/equipo necesita transacciones y rapidez | Hacer cumplir límites; extraer cuellos medidos o responsabilidades independientes |
| Funciones serverless | Trabajo breve y variable dentro de límites del proveedor | Arranque en frío, cuotas, trazabilidad y dependencia |
| Servicios | Equipos o cargas necesitan despliegues y aislamiento independientes | Fallos de red, contratos, consistencia y guardias |
| Eventos | Trabajo diferido y consumidores independientes | Duplicados, orden, reproducción, esquemas y depuración |
| Motor de workflows duraderos | Procesos largos deben reanudarse tras fallos | Determinismo, versiones, operación y migración |

Son decisiones combinables. Un monolito modular puede servir un frontend estático, usar workers y extraer después un dominio. La arquitectura hexagonal/clean dirige dependencias dentro de un componente; no exige microservicios. CQRS separa lecturas y escrituras cuando divergen sus necesidades. Event sourcing además conserva eventos como fuente de verdad y necesita reproducción y retención.

## Límites

Dibuja navegador, API, worker, base de datos, proveedores y fronteras de confianza. Cada módulo controla sus escrituras; otros acceden mediante una interfaz explícita. Mantén pequeñas las bibliotecas comunes. Escrituras indiscriminadas de varios servicios en una base compartida debilitan la responsabilidad independiente.

## Verificar y evolucionar

Prueba un fallo entre componentes y un cambio de contrato. Mide tiempo de entrega, ciclos de dependencias, conflictos y esfuerzo de recuperación. Extrae servicios cuando el beneficio supere los costes de operación y consistencia. Documenta migración y retirada del camino anterior; un diagrama no basta como plan.

## Decisiones relacionadas

[Durabilidad y trabajo distribuido](durability.md) · [Arquitectura frontend y contratos](frontend.md) · [Escalar con mediciones](scaling.md) · [Alojamiento y estrategias de salida](hosting.md)

## Evidencia primaria

[kubernetes](https://raw.githubusercontent.com/kubernetes/website/main/content/en/docs/concepts/architecture/_index.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/mvcc.sgml) · [durable-workflows](https://raw.githubusercontent.com/temporalio/temporal/main/README.md)
