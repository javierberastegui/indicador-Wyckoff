# Relevo — TradingView / visual

## Estado actual
Pine Script v2.0 añadido en rama `feat/wyckoff-ema-rsi-v2`.

Archivos:
- `indicador_wyckoff_ema_rsi_v2.pine`
- `estrategia_wyckoff_ema_rsi_v2.pine`
- `rsi_panel_wyckoff_helper.pine`

## Decisiones activas
La visualización debe ayudar a entender la señal, no esconder la lógica.

La señal visual LONG/SHORT solo aparece cuando se cumplen filtros Wyckoff simplificados, EMAs, RSI, lateralidad y volumen si está activado.

## Siguiente paso
1. Compilar indicador en TradingView.
2. Compilar estrategia en TradingView.
3. Revisar Strategy Tester en `BTCUSDT.P` BingX 1h.
4. Comparar preset `15m` con `1h RSI14`.
5. Registrar errores exactos si Pine marca problemas de sintaxis.
