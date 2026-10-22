---
{
  "id": "performance-testing",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Pruebas de rendimiento, carga y estrés

## Elegir una pregunta sobre fallos

Una prueba de rendimiento debe responder a una decisión del proyecto: si una versión cumple su objetivo de latencia, si una cola se recupera tras una ráfaga, dónde deja de ser suficiente la capacidad o si el uso de recursos crece con el tiempo. El número de usuarios registrados y una sola solicitud rápida no responden a esas preguntas.

| Forma de la prueba | Cuándo usarla | Resultado que se debe examinar |
| --- | --- | --- |
| Pequeña prueba inicial de funcionamiento | Validar carga, datos preparados, permisos y mediciones antes de consumir recursos | Las solicitudes hacen el trabajo previsto; funcionan las aserciones y los controles de parada |
| Carga representativa | Comprobar la operación normal y un pico esperado acordado después de un cambio relevante | El rendimiento útil, la latencia de los percentiles altos, los errores y el uso de recursos cumplen el objetivo del proyecto |
| Estrés (stress) | Examinar la degradación por encima de la carga esperada dentro de un experimento acotado | El control de admisión, los errores, la integridad de los datos y la recuperación se comportan de forma deliberada |
| Pico abrupto (spike) | Un lanzamiento, una programación o un evento externo pueden aumentar bruscamente las llegadas | Crecimiento de la cola, retraso del escalado, rechazo y recuperación después de la ráfaga |
| Duración prolongada (soak) | Las fugas, la renovación de conexiones, las caducidades o el trabajo periódico pueden acumularse con el tiempo | Las tendencias de recursos y latencia siguen siendo explicables durante el ciclo de vida relevante |
| Capacidad o punto de ruptura | La planificación necesita un límite observado con una configuración fija | Primer objetivo incumplido, recurso limitante, margen seguro y ruta de recuperación |

Los nombres varían entre herramientas. Registra la forma real de la carga y el objetivo para que otro agente pueda reproducir el experimento. Una prueba de estrés no es automáticamente la mejor siguiente prueba; una prueba inicial fallida necesita primero un diagnóstico.

## Modelar el trabajo real

Obtén de mediciones o supuestos explícitos la mezcla de transacciones, los patrones de llegada, el tamaño de las solicitudes y de los conjuntos de datos, la proporción entre lecturas y escrituras, el estado de la caché, la desigualdad entre inquilinos, la actividad en segundo plano y el comportamiento de las dependencias. Conserva la distinción entre una transacción de negocio y las solicitudes HTTP que la componen. Explica en qué difiere el entorno de pruebas de producción antes de extrapolar resultados.

Elige deliberadamente el modelo de planificación. Un modelo cerrado mantiene una población de usuarios virtuales que esperan a terminar su iteración actual antes de iniciar la siguiente. Cuando el sistema se ralentiza, puede disminuir el trabajo ofrecido. Un modelo abierto basado en tasa de llegadas programa trabajo nuevo con independencia de cuándo termine el anterior y representa mejor las llegadas independientes. Ninguno de los modelos se ajusta automáticamente a todos los productos. Registra los tiempos de espera entre acciones del usuario y distingue la tasa configurada, el trabajo realmente iniciado, el rendimiento completado y las iteraciones descartadas.

Asegúrate de que el generador, su red y sus credenciales no sean el cuello de botella. Observa por separado la saturación del generador. Un generador sobrecargado que deja de emitir trabajo puede hacer que el sistema objetivo parezca sano. El calentamiento, las cachés, los conjuntos de conexiones, el escalado automático y los trabajos en segundo plano pueden cambiar los resultados; incluye los estados relevantes en lugar de ocultarlos en un único agregado.

## Definir límites antes de ejecutar

El plan del agente debe identificar el objetivo bajo control del proyecto, el entorno, las rutas y cuentas permitidas, el tráfico máximo, la concurrencia, la duración, los límites de recursos y gasto, la supervisión, la limpieza y la persona que pueda detener la ejecución. Usa por defecto entornos aislados y datos sintéticos. No dirijas tráfico de estrés a producción, proveedores externos, inquilinos compartidos o endpoints de modelos de pago sin autorización explícita y acotada y sin límites del proveedor.

Define por separado los umbrales de aceptación y las condiciones de interrupción. La aceptación mide el comportamiento deseado del servicio; las condiciones de interrupción protegen a las personas, los datos, los sistemas compartidos y el presupuesto. Una prueba de estrés planificada puede superar su objetivo normal de latencia, pero debe detenerse en el límite de seguridad acordado. Define cómo actúa la interrupción sobre el generador y cómo se completará o cancelará el trabajo pendiente. Un tiempo máximo del trabajo no es por sí solo un límite de facturación.

Verifica cómo informa el ejecutor de los fallos. Por ejemplo, k6 registra como métricas las comprobaciones fallidas; configura umbrales para que incumplir una condición de aceptación haga fallar la ejecución. La evaluación periódica de interrupción en la nube no impone de forma instantánea los límites de recursos o gasto; establece también los límites necesarios en el servicio y en la cuenta.

Limita el escalado automático durante un experimento de capacidad o documenta su configuración acotada. De lo contrario, la prueba puede medir el crecimiento del gasto en lugar de la capacidad de un sistema fijo. Utiliza los entornos de prueba de los proveedores o sustitutos controlados para los efectos externos costosos e indica qué limitaciones introduce esa elección.

## Medir e interpretar

Registra las operaciones de negocio correctas, las categorías de error, la latencia p50/p95/p99 cuando el tamaño de muestra lo permita, el rendimiento, la concurrencia, la antigüedad y longitud de la cola, las conexiones, la CPU, la memoria, el almacenamiento y el coste relevante. Separa las rutas e inquilinos críticos; un endpoint habitual rápido puede ocultar una ruta de compra fallida dentro de un percentil global. Incluye en el análisis las operaciones fallidas y con tiempo agotado, no solo las respuestas correctas.

Conserva evidencia suficiente de tiempos sin agregar y configuración para reproducir un resultado significativo. Las muestras pequeñas vuelven inestables las estimaciones de percentiles altos; repite comparaciones controladas cuando importe la incertidumbre. Relaciona la degradación observada con las mediciones de recursos y dependencias antes de atribuirla a un cambio de código. Una diferencia entre dos entornos no controlados no demuestra una regresión.

Para las pruebas de duración prolongada, elige una duración que abarque el ciclo de vida en riesgo, como la renovación de tokens, los trabajos programados o el crecimiento de búferes; no copies un número universal de horas. Para las pruebas de capacidad, informa del límite medido con la configuración y la carga probadas, no de una promesa sobre todos los usuarios futuros.

## La recuperación forma parte del experimento

Reduce la carga y observa si la latencia, las colas y los recursos vuelven a un estado útil dentro del plazo de recuperación acordado. Verifica la coherencia de los datos, los efectos duplicados y los trabajos retrasados. Un sistema que rechaza con seguridad la sobrecarga pero nunca vacía el trabajo acumulado no ha demostrado recuperación. Elimina los datos preparados y confirma que no queda activo involuntariamente ningún generador programado ni recurso facturable.

Registra el resultado, sus límites de confianza, la hipótesis sobre el cuello de botella y la decisión: aceptar el margen medido, optimizar una ruta específica, cambiar la política de admisión o evaluar capacidad adicional. Vuelve a probar la hipótesis modificada. Mantén los controles de rendimiento proporcionados al riesgo y suficientemente estables para aportar información útil a las publicaciones.

## Evidencia y decisiones relacionadas

La documentación de k6 de Grafana explica las formas de carga, la planificación abierta y cerrada, los umbrales y los controles de interrupción. Las reglas anteriores de planificación, aceptación y recuperación son una síntesis original de esta biblioteca; los umbrales y valores de tráfico de ejemplo de la documentación del proveedor no son requisitos del proyecto.

[Estrategia de pruebas](testing-strategy.md) · [Escalar con mediciones](scaling.md) · [Salud y recuperación](operations.md) · [Durabilidad](durability.md) · [Controles de calidad](quality.md)

## Evidencia primaria

[k6-test-types](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/testing-guides/test-types/_index.md) · [k6-open-vs-closed](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/using-k6/scenarios/concepts/open-vs-closed.md) · [k6-thresholds](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/using-k6/thresholds.md) · [k6-stress-testing](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/testing-guides/test-types/stress-testing.md) · [k6-spike-testing](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/testing-guides/test-types/spike-testing.md) · [k6-soak-testing](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/testing-guides/test-types/soak-testing.md) · [k6-breakpoint-testing](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/testing-guides/test-types/breakpoint-testing.md)
