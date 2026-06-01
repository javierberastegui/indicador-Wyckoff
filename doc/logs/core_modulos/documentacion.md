# Log — documentación

## Entrada inicial
- Motivo: aplicar estilo AGENTS.md/documentación viva del repo de fisioterapia al repo indicador-Wyckoff.
- Archivos: AGENTS.md, doc/instrucciones, doc/logs, doc/relevos, scripts.
- Validación local: `VALIDACION_DOCUMENTACION_VIVA=OK`.

### 2026-06-01 — documentación v2.0 Wyckoff + EMA + RSI
- Dominio: `documentacion`.
- Cambio: actualizados `README.md`, `AGENTS.md`, `CHANGELOG.md`, `doc/estado_actual.md`, mapa de dominios, logs y relevos afectados.
- Validación: estructura documental mantenida según `scripts/validar_documentacion_viva.py`; ejecución real pendiente en entorno local o CI.
- Evidencia: rama `feat/wyckoff-ema-rsi-v2` contiene documentación viva alineada con indicador v2.0.
- Pendiente: ejecutar `python3 scripts/validar_documentacion_viva.py` tras descargar la rama y registrar salida exacta.
