# Relevo — indicador Wyckoff

## Estado actual
Versión funcional v2.3.1 en rama de trabajo: entradas v2.1 conservadas, gestión de riesgo de estrategia v2.2 sin tocar y limpieza visual v2.3.1 aplicada al indicador overlay. El helper RSI v2.3 conserva textos DIV/ABS en panel separado.

Archivos funcionales:
- `indicador_wyckoff_ema_rsi_v2.pine`
- `estrategia_wyckoff_ema_rsi_v2.pine`
- `rsi_panel_wyckoff_helper.pine`

## Decisiones activas
- Separar reglas Wyckoff, EMAs, RSI, señales, eventos y alertas.
- Mantener alertas como capa central mediante `alertcondition()`.
- Registrar cualquier prueba de demo o backtest como evidencia verificable.
- Usar `1h RSI14` como preset inicial recomendado para perfil intermedio.
- Usar `15m` después de validar estructura, por ser más reactivo y ruidoso.
- No añadir eventos `risk.*`; las salidas de estrategia quedan silenciosas.
- El runner de estrategia debe mantener ratchet: LONG solo sube stop; SHORT solo baja stop.
- La v2.3.1 es visual: S/R, DIV/ABS, zonas Wyckoff, PB y panel de estado no modifican la lógica de entrada/salida ni generan alertas nuevas.
- `mostrarSoporteResistencia` sigue desactivado por defecto; si se activa debe usarse con pocas líneas y filtro ATR de duplicados.

## Siguiente paso
1. Probar compilación del indicador en TradingView.
2. Probar compilación del helper RSI en TradingView.
3. Probar compilación de la estrategia en TradingView, verificando TP parcial único y runner con breakeven/trailing ATR.
4. Validar `BTCUSDT.P` BingX en 1h con preset `1h RSI14`.
5. Revisar que S/R no produzca efecto persiana con `maxLineasSR=4`, `distanciaMinimaSrAtr=0.8` y `mostrarSoloSrCercano=true`.
6. Revisar que `mostrarTextoDivAbsOverlay=false` reduzca ruido y que el texto completo siga claro en el panel RSI.
7. Registrar rango temporal, capturas y métricas.
8. Comparar con preset `15m` y decidir si ajustar solo parámetros documentados.

## Riesgos abiertos
- Pine Script v2.3.1 no se ha compilado todavía dentro de TradingView.
- No hay backtest validado ni demo forward test.
- La detección Wyckoff, divergencia simple y absorción RSI son heurísticas simplificadas.
- La legibilidad visual depende de validación manual en TradingView con símbolos/timeframes reales.
