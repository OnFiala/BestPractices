---
{
  "id": "data",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Datos, contratos y migraciones

## Invariantes explícitas

Elige almacenamiento según acceso, consistencia, retención y recuperación. Una base relacional es un buen candidato inicial para transacciones; almacenamiento de objetos para archivos grandes. Índices y cachés son vistas derivadas salvo diseño explícito. Define identidad, propiedad, unicidad y borrado antes del framework.

Protege invariantes con restricciones y transacciones. Entiende el aislamiento y reintenta fallos de serialización con seguridad. Autoriza cada lectura y escritura por tenant; prueba IDs ajenos, exportaciones y jobs. Logs, analítica y copias también requieren retención.

## Expandir, migrar, contraer

Añade primero un esquema compatible. Despliega lectores y escritores que toleren ambas formas, rellena en lotes limitados y reanudables, mide consistencia y elimina lo anterior después de migrar consumidores. Ensaya volumen real y bloqueos. Revertir código no deshace migraciones destructivas; prepara reparación hacia delante y recuperación probada.

## Verificar

Prueba versiones antiguas/nuevas, duplicados, concurrencia, exportación/importación y restauración. Mide RPO/RTO. Versiona contratos públicos cuando necesiten coordinación; no cambies silenciosamente unidades, nulabilidad o significado. Añade otra tecnología solo si una necesidad medida justifica operación y consistencia.

## Decisiones relacionadas

[Durabilidad y trabajo distribuido](durability.md) · [Seguridad, privacidad y dependencias](security.md) · [Escalar con mediciones](scaling.md)

## Evidencia primaria

[postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/mvcc.sgml) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml) · [owasp](https://raw.githubusercontent.com/OWASP/ASVS/master/README.md)
