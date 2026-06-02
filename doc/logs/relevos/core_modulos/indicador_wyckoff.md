# Relevo — indicador Wyckoff

## Estado actual
Versión funcional v2.2 en rama de trabajo: entradas v2.1 conservadas y gestión de riesgo de estrategia ajustada con TP parcial único + runner ATR manual.

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
- No añadir eventos `risk.*` todavía; las salidas de estrategia quedan silenciosas.
- El runner de estrategia debe mantener ratchet: LONG solo sube stop; SHORT solo baja stop.

## Siguiente paso
1. Probar compilación del indicador en TradingView.
2. Probar compilación de la estrategia en TradingView, verificando TP parcial único y runner con breakeven/trailing ATR.
3. Validar `BTCUSDT.P` BingX en 1h con preset `1h RSI14`.
4. Registrar rango temporal, capturas y métricas.
5. Comparar con preset `15m` y decidir si ajustar ratio rango/ATR, RSI o EMAs.

## Riesgos abiertos
- Pine Script v2.2 no se ha compilado todavía dentro de TradingView.
- No hay backtest validado ni demo forward test.
- La detección Wyckoff y absorción RSI son heurísticas simplificadas.
