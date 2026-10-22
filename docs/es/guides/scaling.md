---
{
  "id": "scaling",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Escalar con mediciones

## Medir antes de distribuir

Las cuentas registradas no miden capacidad. Registra concurrencia, llegadas máximas, tamaño de datos, lecturas/escrituras, distribución de tenants, percentiles y trabajo en segundo plano. Define primero objetivos y presupuesto.

## Escalera de decisiones

1. Perfila carga representativa; corrige consultas caras, índices ausentes, listas ilimitadas y llamadas excesivas.
2. Usa caché con reglas de frescura, invalidación, aislamiento y avalancha. Mide aciertos y carga del origen.
3. Introduce workers limitados, contrapresión, cuotas y admisión. Rechaza de forma segura antes del colapso.
4. Replica procesos sin estado; externaliza sesiones y archivos cuando corresponda. Dimensiona conexiones de base de datos para todas las réplicas.
5. Las réplicas de lectura necesitan un contrato sobre datos antiguos. Particiona después de medir límites y diseñar rutas, redistribución y operaciones entre particiones.

## Verificar

Prueba distribución realista, ráfagas, dependencias lentas y recuperación. Mide rendimiento, p95/p99, errores, edad de cola, saturación y coste por operación útil. Estima concurrencia como llegadas × tiempo de servicio y compruébala.

Escala cuando se incumplan objetivos persistentemente o una previsión medida elimine el margen. Conserva la referencia y la reversión. El autoescalado depende de capacidad posterior, arranques, cuotas y presupuesto; no repara transacciones ineficientes.

## Decisiones relacionadas

[Alojamiento y estrategias de salida](hosting.md) · [Datos, contratos y migraciones](data.md) · [Salud, recuperación y costes](operations.md) · [Elegir y conectar arquitecturas](architecture.md)

## Evidencia primaria

[observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/main/content/en/docs/concepts/observability-primer.md) · [kubernetes](https://raw.githubusercontent.com/kubernetes/website/main/content/en/docs/concepts/architecture/_index.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/mvcc.sgml)
