# Relevo — TradingView / visual

## Estado actual
Pine Script v2.2 en rama de trabajo; estrategia actualizada con TP parcial único y runner con trailing manual ATR.

Archivos:
- `indicador_wyckoff_ema_rsi_v2.pine`
- `estrategia_wyckoff_ema_rsi_v2.pine`
- `rsi_panel_wyckoff_helper.pine`

## Decisiones activas
La visualización debe ayudar a entender la señal, no esconder la lógica.

La señal visual LONG/SHORT solo aparece cuando se cumplen filtros Wyckoff simplificados, EMAs, RSI, lateralidad y volumen si está activado. La estrategia conserva esas entradas; solo cambia la gestión de salidas.

## Siguiente paso
1. Compilar indicador en TradingView.
2. Compilar estrategia en TradingView y revisar que el TP parcial no se reemite después de ejecutarse.
3. Revisar Strategy Tester en `BTCUSDT.P` BingX 1h.
4. Comparar preset `15m` con `1h RSI14` y revisar runner con trailing manual ATR (`trailDebil=1.2`, `trailFuerte=2.5`).
5. Registrar errores exactos si Pine marca problemas de sintaxis.
