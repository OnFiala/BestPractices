---
{
  "id": "security",
  "language": "es",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Seguridad, privacidad y cadena de suministro

## Convertir el riesgo en límites aplicables

Antes de tratar datos sensibles o conceder acceso de escritura a herramientas, identifica los activos, los actores, los puntos de entrada y los límites de confianza. Describe usos indebidos plausibles: un usuario proporciona el identificador de un registro de otro inquilino, un documento pide a un agente que exporte secretos, un trabajo de CI ejecuta una dependencia no confiable o una recuperación restaura los datos del cliente equivocado. Asigna a cada riesgo importante una persona responsable, un control preventivo, un fallo observable y una acción de recuperación.

Elige una versión con soporte de un estándar de verificación, como OWASP ASVS, y selecciona los requisitos adecuados para la aplicación. Registra los identificadores versionados de los requisitos y las excepciones locales; enlazar una descripción general de ASVS o completar una lista no constituye una certificación. Esta guía es un marco de decisión original, no una reproducción de ese estándar.

## Identidad, permisos e inquilinos

Usa componentes de autenticación mantenidos en lugar de inventar un protocolo de contraseñas, sesiones o tokens. Documenta el alta de cuentas, la recuperación, la revocación y la autenticación reforzada para acciones sensibles. Distingue entre reconocer una identidad y decidir qué puede hacer esa identidad.

Haz que la capa de ejecución de confianza compruebe el actor, el objeto de destino y la operación solicitada. Un identificador opaco, un botón oculto, una red privada o un inicio de sesión correcto no bastan como evidencia de permiso. Las combinaciones de acceso desconocidas deben denegarse de forma segura. Prueba las rutas de lectura, escritura, búsqueda, exportación, administración y trabajo en segundo plano, incluido el acceso después de cambios de pertenencia.

Obtén el contexto del inquilino a partir de una pertenencia verificada. Aplica ese contexto a consultas de base de datos, trabajos, cachés, almacenamiento de archivos, índices de recuperación y restauraciones. Si las políticas por fila de la base de datos ofrecen un límite adicional, verifica que el rol real de ejecución no pueda eludirlas y que las conexiones reutilizadas no conserven el contexto de otro inquilino. Trata las exportaciones globales del operador y la administración entre inquilinos como capacidades distintas.

Para las sesiones de navegador, usa las protecciones de cookies admitidas y define deliberadamente la caducidad, el cierre de sesión, la rotación y la revocación. Los cambios de estado autenticados con cookies necesitan protección CSRF adecuada al framework; SameSite es un control complementario. La recuperación de la autenticación y los cambios de privilegios merecen el mismo rigor que el inicio de sesión.

## Datos, renderizado y solicitudes salientes

Mantén los registros privados, las credenciales y los datos de prueba de clientes fuera del historial público de Git, las compilaciones del sitio, los paquetes del cliente y los índices de búsqueda generados. Superponer una pantalla de inicio de sesión a archivos descargables públicamente no los convierte en privados. Clasifica los datos antes de recopilarlos; define retención, eliminación, exportación, tratamiento de copias de seguridad y quién puede investigar incidentes.

Valida las entradas según el contrato de la aplicación. Usa operaciones parametrizadas de base de datos y mecanismos mantenidos de codificación o saneamiento apropiados al contexto de salida. La validación por sí sola no evita la ejecución de scripts cuando los datos se renderizan como HTML. Restringe el tamaño y tipo de los archivos cargados, su ubicación de almacenamiento y su comportamiento de ejecución.

Un servidor o agente que obtiene URLs influidas por usuarios necesita una política de solicitudes salientes. Limita esquemas, destinos, redirecciones, tamaño de respuesta y duración; impide el acceso a servicios internos y metadatos de la nube salvo necesidad y autorización explícitas. Resuelve y comprueba los destinos en el límite de red para que los cambios de DNS y las redirecciones no conviertan una URL aparentemente permitida en acceso interno.

## Límites de agentes y cadena de suministro

Trata el texto recuperado, las salidas de herramientas y modelos y los mensajes delegados como datos no confiables. Aplica el control de acceso a herramientas fuera del modelo: vincula la identidad y el ámbito de recursos, valida los argumentos y conserva las credenciales sensibles en el servicio de ejecución. La aprobación de una operación importante debe identificar la acción y sus parámetros, caducar y resistir la reutilización. Una anotación de herramienta o un agente que diga «aprobado» no pueden conceder autoridad.

Limita la duración de las ejecuciones, los reintentos, la concurrencia, los tokens y el gasto en las capas capaces de imponer esos límites. Aísla la memoria y la recuperación de información según el usuario o inquilino autorizado. Prueba la inyección indirecta de instrucciones, las filtraciones de información, los cambios de política y los traspasos entre agentes. Las medidas de supervisión del comportamiento pueden reducir fallos, pero no forman un perímetro de seguridad.

Separa las identidades de desarrollo, compilación, despliegue y ejecución. Mantén los secretos fuera del contenido del repositorio y usa credenciales acotadas y de corta duración cuando se admitan. Fija las versiones resueltas de las dependencias mediante un archivo de bloqueo (lockfile), verifica la procedencia y las licencias de las actualizaciones y vigila las vulnerabilidades. Fija las acciones de CI a commits inmutables y revisa quién puede modificar workflows, artefactos y resolución de dependencias. Nunca expongas credenciales de producción a la ejecución de PR no confiables ni concedas a un agente el socket de Docker del anfitrión.

## Verificar, responder y revisar

Usa la [guía de pruebas de seguridad](security-testing.md) para vincular las amenazas con evidencia automatizada y manual. Antes de publicar comportamiento sensible, ejercita el acceso no autorizado, la separación entre inquilinos, la revocación, la recuperación y el uso indebido de herramientas con privilegios. Asegúrate de que los registros permitan investigar sin exponer credenciales ni datos personales innecesarios; protege también su acceso y retención.

Registra el contacto para incidentes, los pasos de contención, la revocación de credenciales, la conservación de evidencia, el procedimiento de restauración y la gestión de divulgación. Revisa el modelo de amenazas después de una nueva integración, un cambio de privilegios o clase de datos, un incidente o un cambio de límite arquitectónico. Las obligaciones normativas y la aceptación del riesgo corresponden a responsables humanos cualificados.

## Decisiones relacionadas

[Pruebas de seguridad](security-testing.md) · [Estrategia de pruebas](testing-strategy.md) · [Dirección humana, ejecución de agentes](agents.md) · [Datos, contratos y migraciones](data.md) · [Operar servidores propios](self-hosting.md)

## Evidencia primaria

[owasp-asvs-requirements](https://raw.githubusercontent.com/OWASP/ASVS/3383877f732ce89a458a1af43288f2f1b1d7db0c/5.0/docs_en/OWASP_Application_Security_Verification_Standard_5.0.0_en.csv) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-multi-tenant](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.md) · [owasp-authentication](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authentication_Cheat_Sheet.md) · [owasp-session](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Session_Management_Cheat_Sheet.md) · [owasp-csrf](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.md) · [owasp-xss](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.md) · [owasp-ssrf](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md)
