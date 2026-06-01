# Changelog

## [2.0.0] - 2026-06-01

### Added
- Nuevo indicador `indicador_wyckoff_ema_rsi_v2.pine`.
- Nueva estrategia `estrategia_wyckoff_ema_rsi_v2.pine`.
- Helper opcional `rsi_panel_wyckoff_helper.pine` para panel RSI separado.
- Presets `15m`, `1h RSI14`, `1h RSI21` y `Manual`.
- Filtro de tendencia por EMA200 y pendiente de EMA200.
- Confirmación RSI por nivel 50 y pendiente.
- Divergencia RSI simple.
- Heurística de absorción estilo Wyckoff.
- Filtro lateral por ratio rango/ATR.
- Confirmación opcional por volumen.
- Alertas JSON para webhook con `event_type`, señal, símbolo, timeframe, precio, SL, TP, módulo origen y severidad.

### Changed
- La metodología pasa de enfoque inicial documental a primera versión funcional Wyckoff + EMA + RSI.
- `README.md` documenta uso, presets, alertas y validación pendiente.
- `AGENTS.md` incorpora reglas específicas para RSI y presets operativos.
- `doc/instrucciones/mapa_dominios.md` incorpora el dominio `rsi`.

### Docs
- Estado actual actualizado a v2.0 en rama de trabajo.
- Logs y relevos actualizados por dominios `core_indicador`, `tradingview`, `alertas` y `documentacion`.

### Tests
- Validación documental prevista mediante `python3 scripts/validar_documentacion_viva.py`.
- Validación funcional pendiente en TradingView sobre `BTCUSDT.P` de BingX en 1h y 15m.
- No se registran resultados de rentabilidad, winrate ni drawdown hasta backtest o demo con evidencia.
