# Relevo — indicador Wyckoff

## Estado actual
Versión funcional v2.4.0 en rama de trabajo: indicador overlay y helper RSI pasan a modo automático limpio. La estrategia v2.2 con gestión de riesgo y runner ATR manual no se tocó.

Archivos funcionales:
- `indicador_wyckoff_ema_rsi_v2.pine`
- `estrategia_wyckoff_ema_rsi_v2.pine`
- `rsi_panel_wyckoff_helper.pine`

## Decisiones activas
- Separar reglas Wyckoff, EMAs, RSI, señales, eventos y alertas.
- Mantener alertas como capa central mediante `alertcondition()`.
- Registrar cualquier prueba de demo o backtest como evidencia verificable.
- El indicador v2.4.0 ya no expone preset, modo EMA manual ni RSI manual.
- Selección automática: `tfMin <= 15` usa EMAs 9/21 + RSI14; el resto usa EMAs 10/20 + RSI14.
- Lateralidad interna: 15m usa lookback 18 y ratio rango/ATR 4.5; el resto usa lookback 24 y ratio 5.5.
- No añadir eventos `risk.*`; las salidas de estrategia quedan silenciosas.
- El runner de estrategia debe mantener ratchet: LONG solo sube stop; SHORT solo baja stop.
- La v2.4.0 no modifica lógica de entrada/salida salvo selección automática de EMAs/RSI del indicador/helper y no genera alertas nuevas.

## Siguiente paso
1. Probar compilación del indicador en TradingView.
2. Probar compilación del helper RSI en TradingView.
3. Probar compilación de la estrategia en TradingView, verificando TP parcial único y runner con breakeven/trailing ATR.
4. Validar `BTCUSDT.P` BingX en 1h y confirmar panel AUTO con EMAs 10/20 + RSI14.
5. Validar `BTCUSDT.P` BingX en 15m y confirmar panel AUTO con EMAs 9/21 + RSI14.
6. Revisar que la configuración visible mínima sea suficiente para operar rápido.
7. Registrar rango temporal, capturas y métricas.
8. Comparar con preset 15m anterior solo como referencia documental, sin afirmar rentabilidad.

## Riesgos abiertos
- Pine Script v2.4.0 no se ha compilado todavía dentro de TradingView.
- No hay backtest validado ni demo forward test.
- La detección Wyckoff, divergencia simple y absorción RSI son heurísticas simplificadas.
- La legibilidad visual y selección automática dependen de validación manual en TradingView con símbolos/timeframes reales.
