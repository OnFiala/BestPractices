---
{
  "id": "playbook-public-website",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Entregar un sitio web público

## Aplicabilidad y primeras decisiones

Utiliza este perfil para contenido editorial público, documentación o una campaña cuyo recorrido principal consista en leer, buscar y seguir enlaces. Registra los idiomas, la frecuencia de publicación, las expectativas de accesibilidad, la titularidad del dominio, el presupuesto de recursos y el tiempo aceptable para corregir una publicación perjudicial. La opción inicial es una compilación estática a partir de contenido revisado, artefactos de publicación inmutables y una CDN. Se trata de una propuesta redactada por agentes y de una síntesis local, no de una política adoptada ni de una certificación para producción.

Una ruta renderizada en el servidor es una alternativa cuando la necesidad de actualización no permite esperar a una compilación. Los envíos autenticados requieren un límite de servidor explícito; no presentes un servicio de escritura como un detalle del sitio estático. Un sitio pequeño puede mantener juntos el contenido y la presentación. Cuando aumenten las compilaciones o los conflictos entre tareas editoriales, separa primero la validación de contenido e introduce compilaciones incrementales. Añade servicios solo cuando las mediciones del retraso de publicación, el trabajo dinámico o las necesidades de responsabilidad justifiquen su coste de operación; el número de visitantes por sí solo no lo justifica.

## Límites y contratos

Organiza `content/`, `ui/`, `build/`, `tests/` y `ops/` por responsabilidad, aunque compartan repositorio. El esquema de contenido define los identificadores estables de página, el idioma, las redirecciones, el estado de publicación y los metadatos públicos. La interfaz se encarga de la navegación, los estados de búsqueda, el foco y los mensajes de error accesibles. La compilación se encarga de una transformación determinista y de una lista explícita de recursos permitidos. Los borradores privados, las credenciales y los comentarios internos nunca deben entrar en el HTML desplegable, los índices de búsqueda JSON, los mapas de código fuente ni los paquetes descargables de fuentes.

Especifica la permanencia de las URL, el comportamiento de las redirecciones, las traducciones ausentes, la versión del índice de búsqueda y los tiempos de validez de la caché. Incluye el índice y las páginas en la misma publicación. Las identidades de previsualización pueden leer borradores; la identidad que publica en producción debe recibir únicamente el artefacto aprobado. Trata el HTML redactado, el Markdown importado y el texto de consulta como datos no confiables en los puntos donde se renderizan; utiliza representación segura como texto o una política de saneamiento revisada explícitamente.

## Ordenar el trabajo

1. El agente de descubrimiento registra en un perfil de proyecto tres recorridos públicos, un inventario de rutas e idiomas, la responsabilidad sobre el contenido y objetivos cuantitativos de publicación y rendimiento. Una persona resuelve las decisiones de marca, accesibilidad y riesgo de publicación.
2. El rol de diseño e implementación construye un recorrido completo que incluya búsqueda vacía, ruta inexistente, ventana móvil y navegación con teclado. Registra en un ADR la elección de renderizado y el alcance de las dependencias antes de multiplicar las plantillas de página.
3. El verificador comprueba un artefacto compilado en un navegador real aislado, revisa los datos de salida y prueba una publicación anterior. El responsable de la publicación elige el resumen criptográfico aprobado y controla las credenciales de despliegue.

Entrega un conjunto concreto de elementos: perfil, ADR, esquema de contenido, manifiesto de rutas, resumen criptográfico del artefacto y commit, observaciones del navegador, aspectos pendientes de la revisión de accesibilidad, inspección de los datos de salida, instrucciones de despliegue y restauración y responsables identificados del contenido y del dominio. Distingue las comprobaciones previstas, ejecutadas, fallidas y omitidas. El directorio de referencia local `examples/frontend` es un punto de partida para trabajar las interacciones, no evidencia de que se hayan verificado las rutas o la accesibilidad de este proyecto.

## Elegir comprobaciones capaces de refutar la preparación

Utiliza comprobaciones unitarias para las reglas del analizador y las rutas, comprobaciones de integración para la coherencia entre contenido e índice y comprobaciones de caja negra en el navegador para los recorridos públicos. Cuando una página cambie de nombre, la URL antigua debe llevar al reemplazo previsto, no a una página plausible pero incorrecta. Busca un marcador privado sintético en todos los recursos generados: encontrarlo supone un fallo de publicación, aunque no aparezca en las páginas visibles. Introduce marcado en la entrada de búsqueda y en los títulos importados; debe permanecer como texto inofensivo o seguir la regla de saneamiento revisada, sin ejecutar scripts.

Limita la velocidad de la red, provoca un fallo al obtener la búsqueda y navega antes de que termine. La página actual debe seguir siendo la referencia válida; un resultado tardío no debe sobrescribir una consulta más reciente, y un error debe permitir recuperarse. Comprueba que cada recorrido pueda completarse con teclado y que el foco sea visible en todos los idiomas compatibles; los resultados automáticos de accesibilidad por sí solos no demuestran conformidad. Mide la transferencia en frío, la demora de interacción, el tiempo de compilación y el comportamiento de aciertos de caché frente a los objetivos del proyecto en dispositivos representativos. Detén las pruebas al alcanzar el límite acordado de tráfico o gasto.

## Publicar, operar y retirar

Previsualiza el artefacto exacto, despliégalo para una audiencia limitada o en un nombre de host de preproducción y después verifica las rutas y cabeceras críticas antes de promoverlo. Conserva el artefacto anterior y la configuración de enrutamiento. Una reversión puede restaurar páginas, pero no retirar copias de cachés, buscadores, descargas o historial de Git; una divulgación requiere respuesta a incidentes y rotación de secretos cuando corresponda. Las migraciones de redirecciones necesitan conservar una correspondencia, y eliminar un idioma requiere revisar explícitamente los enlaces y el impacto en los usuarios.

Asigna un responsable de las compilaciones fallidas, la renovación del dominio y los certificados, el tráfico abusivo y la corrección urgente de contenido. Observa los fallos de rutas, los fallos de búsqueda, la antigüedad de la publicación y la disponibilidad de recorridos sintéticos sin conservar datos innecesarios de visitantes. Presupuesta la transferencia de la CDN, los minutos de compilación, los registros, las dependencias y el mantenimiento editorial. Antes de producción, resuelve los aspectos pendientes de configuración de hosting, política de cabeceras, copias de seguridad y exportación, accesibilidad y guardias; la referencia no los proporciona. Al retirar el sitio, conserva las exportaciones de contenido y redirecciones acordadas, revoca el acceso de publicación, elimina el seguimiento y mantén el control del dominio durante la transición acordada.

## Continuar con decisiones relacionadas

[Contratos de frontend](frontend.md) · [Hosting](hosting.md) · [Entrega con GitHub](github.md) · [Estrategia de pruebas](testing-strategy.md)

## Evidencia primaria

[github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md) · [owasp-xss](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.md) · [playwright-testing](https://raw.githubusercontent.com/microsoft/playwright/ca7ca36145b84183cf423c2a099bd7e9cd8b1cb3/docs/src/best-practices-js.md) · [wcag-keyboard](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/sc/20/keyboard.html) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md)
