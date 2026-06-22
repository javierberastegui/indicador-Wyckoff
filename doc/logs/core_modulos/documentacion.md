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

### 2026-06-22 — documentación v2.5.0 fractalidad swing
- Dominio: `documentacion`, `core_indicador`, `tradingview`, `alertas`.
- Cambio: actualizados `README.md`, `CHANGELOG.md`, `doc/estado_actual.md`, logs de indicador, TradingView, alertas, relevos y deuda técnica para reflejar la puerta W/D/1H, EMA50 y manos fuertes.
- Validación: revisión estructural hecha desde GitHub; ejecución real de `python3 scripts/validar_documentacion_viva.py` queda pendiente en clon local.
- Evidencia: commits en `main` con cambios de v2.5.0 y documentación por dominio.
- Pendiente: ejecutar validación documental local y compilar Pine en TradingView.
