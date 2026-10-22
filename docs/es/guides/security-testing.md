---
{
  "id": "security-testing",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Seleccionar y ejecutar pruebas de seguridad

## Empezar por el límite que puede fallar

Las pruebas de seguridad aportan evidencia sobre una amenaza y un control explícitos. Antes de elegir un escáner, identifica el actor, el punto de entrada, el activo protegido, la autorización esperada y el posible efecto. Enlaza los requisitos aplicables de una versión identificada de un estándar como ASVS y define después una prueba cuyo resultado pueda contradecir la afirmación de que el control funciona.

Caja negra describe las pruebas a través de interfaces observables sin utilizar componentes internos de la implementación. No es sinónimo de pruebas de seguridad. El trabajo de caja gris puede usar credenciales de prueba, conocimiento del esquema o telemetría; el de caja blanca usa código y configuración. Combina perspectivas cuando corresponda: una revisión de código puede encontrar un filtro por inquilino omitido, mientras que una solicitud desde otro inquilino demuestra si la ruta desplegada expone datos.

## Elegir técnicas complementarias

| Técnica | Condición adecuada para aplicarla | Qué no puede demostrar por sí sola |
| --- | --- | --- |
| Análisis de código y revisión específica | Nuevos analizadores, consultas, renderizado, acceso a archivos o red, o rutas con privilegios | La configuración real de ejecución, toda la autorización de negocio o la ausencia de todas las vulnerabilidades |
| Análisis de dependencias e imágenes | Nuevas dependencias, cambios de lockfile o imagen, o cambios en las fuentes de vulnerabilidades | La posibilidad de explotación en este despliegue o la corrección de la lógica propia de la aplicación |
| Detección de secretos | Archivos modificados, artefactos de compilación e historial relevante | Que se detecten todas las credenciales expuestas o que borrar un archivo revoque una credencial |
| Revisión de infraestructura y configuración | Cambios de red, IAM, almacenamiento, TLS, CI o despliegue | Que los ajustes desplegados coincidan con la configuración propuesta sin una verificación separada |
| Escaneo dinámico de un despliegue de prueba propio | Cambios en la superficie web o API y en la configuración | Todo el control de acceso o la seguridad de flujos complejos; la cobertura autenticada puede ser incompleta |
| Casos manuales de abuso y comprobaciones específicas de API o navegador | Cambios de autenticación, permisos, separación entre inquilinos, recuperación, lógica de negocio o herramientas de agentes | Una cobertura amplia si no se registran rutas, roles y casos omitidos |
| Fuzzing o comprobaciones de límites basadas en propiedades | Analizadores, formatos de archivo, protocolos o validadores reciben datos no confiables | La corrección fuera del modelo de entradas o la validez de la propiedad de seguridad afirmada |

Elige herramientas compatibles con el lenguaje, el framework, el protocolo y el ámbito previsto de la prueba. El resultado de un escáner es un posible hallazgo: inspecciona la ruta alcanzable, los requisitos previos, el impacto y la reproducción antes de asignar gravedad. Un informe vacío significa que no se detectaron hallazgos con esa configuración; no es un certificado de seguridad.

## Comprobaciones concretas de límites habituales

Para la autorización de objetos, crea dos inquilinos distintos y varios roles. Ejercita lectura, actualización, eliminación, listado, búsqueda, exportación y rutas asíncronas con identificadores fuera del ámbito del actor. Incluye respuestas almacenadas en caché y cambios de permisos. Comprueba tanto la denegación como la ausencia de divulgación o modificación; variar únicamente la interfaz no basta.

Para las sesiones, cubre cierre de sesión y revocación, caducidad, cambios de privilegios, recuperación de cuentas y reutilización de credenciales antiguas. Para escrituras autenticadas mediante cookies, ejercita el límite CSRF del framework. Para renderizado y tratamiento de entradas, incluye los contextos que use realmente la aplicación: HTML, consultas de base de datos, rutas de archivos, cargas y análisis de mensajes estructurados. Verifica un fallo acotado sin invocar un endpoint externo no controlado.

Para las solicitudes salientes, usa destinos de prueba propios para ejercitar redirecciones, cambios de dirección y destinos no permitidos. Comprueba la política de red que se aplica durante la ejecución, además de la validación de entradas. Mantén los metadatos de la nube, los servicios internos y los secretos reales fuera de la prueba salvo que se incluyan específicamente en una evaluación autorizada.

Para los agentes, prueba contenido recuperado hostil, salidas de herramientas falsificadas, argumentos de herramientas no autorizados, reutilización de aprobaciones, parámetros modificados después de la aprobación, memoria persistente contaminada e instrucciones delegadas que pidan acceso más amplio. Comprueba que la capa de ejecución deniegue los efectos prohibidos incluso cuando el modelo los solicite. Incluye tareas legítimas para no puntuar erróneamente como útil y seguro un sistema que rechace todas las solicitudes.

Para los límites de cadena de suministro o CI, examina cómo el código no confiable, los cambios de workflows, los hooks de dependencias y los artefactos descargados podrían alcanzar credenciales o permisos de publicación. Valida el límite en un escenario aislado cuando haga falta. No uses un secreto real para demostrar que un secreto podría filtrarse.

## Reglas de ejecución para agentes

El paquete de la tarea identifica los objetivos aprobados por su propietario, las identidades permitidas, las técnicas admitidas, la ventana temporal, los límites de tráfico, las reglas de datos, las dependencias externas, las condiciones de parada y el destino del informe. Usa un despliegue aislado con cuentas sintéticas siempre que sea posible. Comprueba que las credenciales de prueba no permitan llegar accidentalmente a producción.

El permiso para leer un repositorio no autoriza el escaneo activo de su servicio de producción. El acceso amplio al proyecto no autoriza tráfico de estrés, entradas destructivas, comunicaciones de retorno externas ni objetivos de terceros. Solicita el ámbito que falte antes de realizar esas operaciones; continúa de forma independiente la revisión estática y la preparación.

Detén las pruebas activas cuando el objetivo quede fuera de ámbito, aparezcan datos reales de usuarios inesperadamente, la salud del servicio cruce el límite acordado o fallen la contención o la limpieza. Conserva evidencia mínima con los valores sensibles eliminados y avisa a la persona responsable mediante el canal autorizado. No amplíes el impacto para hacer más llamativo un hallazgo.

## Revisar, corregir y verificar

Un hallazgo útil registra la revisión y configuración probadas, la ruta exacta afectada, el actor y los requisitos previos, el comportamiento observado, la protección esperada, el impacto y una reproducción mínima. Distingue los casos confirmados, descartados y pendientes de resolver. Evita publicar credenciales, registros personales o detalles listos para explotar producción en un issue público.

Verifica la corrección frente a la reproducción original y una operación legítima permitida. Añade una regresión que detecte el fallo de límite subyacente en lugar de limitarse a reconocer una entrada concreta. Reevalúa las rutas relacionadas cuando el fallo proceda de un diseño compartido. Registra el riesgo residual y la aceptación humana cuando se aplace la corrección completa.

Las decisiones de publicación se basan en el modelo de amenazas y la evidencia, no en una puntuación universal de escáner. Un límite sin resolver con consecuencias graves bloquea la publicación afectada salvo que una persona cualificada asuma explícitamente una excepción documentada. Repite la evaluación específica cuando cambien los privilegios, las superficies expuestas, la sensibilidad de los datos, las dependencias o las capacidades de los agentes.

## Evidencia y decisiones relacionadas

OWASP ASVS proporciona requisitos de verificación versionados; las guías de autorización, sistemas multiinquilino y agentes aportan contexto concreto sobre amenazas y controles. GitHub explica los límites de confianza propios de sus workflows. La matriz de selección y las reglas de ejecución son políticas locales originales; no se afirma que ninguna fuente avale este proyecto concreto.

[Arquitectura de seguridad](security.md) · [Estrategia de pruebas](testing-strategy.md) · [Controles de calidad](quality.md) · [Dirección humana, ejecución de agentes](agents.md) · [Pruebas de rendimiento y estrés](performance-testing.md)

## Evidencia primaria

[owasp-asvs-requirements](https://raw.githubusercontent.com/OWASP/ASVS/3383877f732ce89a458a1af43288f2f1b1d7db0c/5.0/docs_en/OWASP_Application_Security_Verification_Standard_5.0.0_en.csv) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-multi-tenant](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.md) · [owasp-session](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Session_Management_Cheat_Sheet.md) · [owasp-ssrf](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md)
