---
{
  "id": "governance",
  "language": "es",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Gobierno y decisiones abiertas

## Acuerdo actual

Esta biblioteca es pública y portable. El inglés es la versión canónica, con traducciones al checo, alemán y español. La prosa y los diagramas originales usan CC BY 4.0; el código, la configuración y las plantillas de código reutilizables usan MIT. Las fuentes de terceros conservan sus licencias. Los agentes proponen PR; una persona revisa y fusiona. Las recomendaciones y traducciones iniciales no cuentan automáticamente con aprobación humana.

La propia biblioteca se crea y mantiene con agentes de IA y declara ese origen. La prosa original conserva su licencia de contenido en las exportaciones JSON; las licencias del software de terceros y su código fuente correspondiente obligatorio se conservan por separado. No copies, traduzcas ni parafrasees de cerca texto de fuentes externas para incluirlo en recomendaciones públicas. Una cita es evidencia, no permiso. Una persona comprueba originalidad y derechos antes de que la automatización privada alimentada con fuentes traslade material a un PR público.

## Decisiones que debe responder cada proyecto que la adopte

¿Quién responde por producción y está disponible durante un incidente? ¿Qué datos no pueden salir nunca de una región o proveedor? ¿Cuánto tiempo de interrupción y qué pérdida de datos toleran los usuarios? ¿Cuál es el presupuesto mensual de infraestructura e IA, incluido un mecanismo efectivo de parada? ¿Qué ocurre si el modelo o el proveedor de alojamiento no están disponibles? ¿Quién aprueba las operaciones irreversibles? ¿Cómo exportan o eliminan sus datos los usuarios? ¿Qué requisitos de accesibilidad y legales se aplican? ¿Quién se hace cargo del proyecto si su responsable se marcha?

Conserva esas respuestas en el perfil del proyecto y en los ADR. Las preguntas sin resolver con consecuencias importantes bloquean el lanzamiento correspondiente, no la exploración que no dependa de ellas. Las excepciones requieren una persona responsable, un motivo, un control compensatorio y una fecha de caducidad.

## Cuidado de la biblioteca

Usa un issue para proponer un tema nuevo o cuestionar una recomendación; incluye un contraejemplo y evidencia primaria. Distingue los principios universales de las preferencias que dependen del contexto. Retira recomendaciones mediante enlaces a alternativas en lugar de borrar el historial. Publica cambios versionados y comunica las obligaciones modificadas. Las personas que revisan deciden si las traducciones conservan el significado; que coincidan los números de revisión solo comprueba la gestión de versiones. Mide la utilidad por decisiones acertadas y menos trabajo correctivo, no por el número de páginas.

## Decisiones relacionadas

[Evidencia y mantenimiento automático](maintenance.md) · [Adoptar la biblioteca en un proyecto](adoption.md) · [GitHub, versiones y árboles de trabajo limpios](github.md)

## Evidencia primaria

[github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [semver](https://raw.githubusercontent.com/semver/semver/f99d5485190a47c0863949e7da810a5553e0ed4d/semver.md) · [plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md)
