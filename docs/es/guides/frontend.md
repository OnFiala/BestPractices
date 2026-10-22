---
{
  "id": "frontend",
  "language": "es",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Arquitectura y contratos del frontend

## Elegir el renderizado para cada interacción

La generación estática encaja con contenido público que se puede recompilar. El renderizado en servidor puede ayudar a la actualización inicial o al descubrimiento, mientras que el renderizado en cliente encaja con la interacción sostenida. Las rutas híbridas pueden combinar estos enfoques. Este es el marco de decisión original de la biblioteca: mide el recorrido relevante e inspecciona el comportamiento actual del framework elegido antes de adoptarlo.

Registra quién controla la caché, el coste de hidratación y JavaScript y los límites de autenticación y despliegue. No coloques la respuesta privada de un usuario renderizada en servidor en una caché compartida con otra identidad. Los microfrontends pueden facilitar responsabilidades independientes, pero añaden costes de enrutamiento, dependencias y coherencia de diseño; no son la forma predeterminada de dividir componentes.

## Dar un único propietario a cada estado

Distingue entre estado del servidor, estado de URL y navegación, estado local de interacción y preferencias duraderas. Decide qué estado sobrevive a una recarga o al uso sin conexión y cómo se invalida después de cerrar sesión o cambiar permisos. Organiza las funcionalidades en torno a interfaces explícitas y componentes básicos accesibles compartidos. Copiar los mismos datos del servidor en varios almacenes crea trabajo de conciliación en lugar de resiliencia.

Para cada interacción respaldada por una API, define:

| Contrato | Ejemplo de evidencia de aceptación |
| --- | --- |
| Autorización | Las solicitudes directas a la API fallan cuando el usuario carece de permiso, aunque se omita la interfaz |
| Forma de la respuesta | Los clientes antiguos y nuevos manejan los campos, errores, paginación y unidades documentados |
| Carga y cancelación | Salir de la página detiene trabajo innecesario o ignora de forma segura un resultado tardío |
| Cambio optimista | El rechazo restaura o concilia el estado visible sin perder la entrada del usuario |
| Sin conexión y conflictos | Una edición en cola tiene una identidad estable y una regla de conflicto explícita al reconectar |
| Privacidad | El cierre de sesión y la revocación de acceso borran o invalidan los datos privados relevantes en caché |

El servidor es responsable de la validación y la autorización de confianza. Los botones ocultos y los esquemas del cliente mejoran la usabilidad, pero no pueden imponer control de acceso. Mantén los secretos del backend fuera de los paquetes del navegador, los mapas de código fuente y los índices generados. El código del navegador y las salidas de modelos o herramientas son datos no confiables en el límite del servidor.

## Probar el recorrido observable

Durante la implementación, prueba las reglas de dominio por separado de los detalles de renderizado. Ante cambios de API, ejecuta pruebas de compatibilidad de consumidores. Antes de publicar, ejercita los recorridos clave como [usuario de caja negra](testing-strategy.md): teclado y orden del foco, nombres accesibles, contraste, ventana estrecha, estados de carga, vacío y error, acceso denegado y solicitudes interrumpidas. Combina comprobaciones automatizadas de accesibilidad con revisión de tareas mediante teclado y tecnologías de asistencia cuando corresponda; superar un comprobador automático no demuestra conformidad completa.

Usa [pruebas de rendimiento](performance-testing.md) con condiciones representativas de dispositivo y red y carga sostenida de API; mide navegación, latencia de interacción, recursos transferidos y errores. Confirma que el frontend no multiplique las llamadas al backend durante reintentos, sondeos o reconexiones. Prueba los límites de autenticación y caché mediante el [plan de pruebas de seguridad](security-testing.md).

## Evolucionar deliberadamente

Un backend para un frontend concreto puede ser útil cuando ese cliente necesita agregación o un límite más fuerte en servidor. Explica la mejora y quién será responsable del despliegue adicional. Cambia de framework o introduce microfrontends solo cuando restricciones medidas justifiquen la migración, incluidos los costes de accesibilidad, compatibilidad y soporte de dependencias. Conserva un plan de publicación e invalidación de caché para que los recursos antiguos del navegador sigan siendo compatibles con la API desplegada.

Aquí WebMCP es una mejora progresiva. La lectura y búsqueda ordinarias deben funcionar sin él; los navegadores compatibles siguen necesitando pruebas de permisos, cancelación y navegación. La exposición experimental de herramientas no debe conceder acceso que el usuario no tenga ya.

## Decisiones relacionadas

[Arquitectura](architecture.md) · [Estrategia de pruebas](testing-strategy.md) · [Pruebas de rendimiento](performance-testing.md) · [Pruebas de seguridad](security-testing.md) · [Integraciones](integrations.md)

## Evidencia primaria

[wcag](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/index.html) · [owasp](https://raw.githubusercontent.com/OWASP/ASVS/2b47a9dd16760ee484a6672d197f1f7e25d9c632/README.md) · [webmcp](https://raw.githubusercontent.com/webmachinelearning/webmcp/51ed75653aaa7f174f8dbe05d1bc327359bbc57c/README.md) · [wcag-keyboard](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/sc/20/keyboard.html) · [wcag-focus-order](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/sc/20/focus-order.html) · [wcag-focus-visible](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/sc/20/focus-visible.html) · [wcag-contrast](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/sc/20/contrast-minimum.html) · [azure-cqrs](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/cqrs.md)
