# Relevo — documentación

## Estado actual
Documentación viva inicial aplicada y ampliada para v2.0 Wyckoff + EMA + RSI en rama `feat/wyckoff-ema-rsi-v2`.

## Decisiones activas
- AGENTS.md manda.
- Logs por dominio son bitácora principal.
- No usar histórico global como fuente principal.
- Ejecutar validador tras tocar documentación.
- Documentar cambios funcionales de Pine Script en dominios `core_indicador`, `tradingview`, `alertas` y `documentacion`.

## Siguiente paso
1. Ejecutar `python3 scripts/validar_documentacion_viva.py` en local.
2. Compilar Pine Script en TradingView.
3. Registrar salida exacta y capturas en logs por dominio.
