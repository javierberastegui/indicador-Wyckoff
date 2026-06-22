# Relevo — indicador Wyckoff

## Estado actual
Versión funcional v2.5.0 en `main`: indicador overlay actualizado a modo swing fractal con sincronía semanal/diario/1h, EMA50 como filtro fuerte, lectura visual de manos fuertes y alertas JSON enriquecidas. La estrategia v2.2 con gestión de riesgo y runner ATR manual no se tocó.

Archivos funcionales:
- `indicador_wyckoff_ema_rsi_v2.pine`
- `estrategia_wyckoff_ema_rsi_v2.pine`
- `rsi_panel_wyckoff_helper.pine`

## Decisiones activas
- Separar reglas Wyckoff, EMAs, RSI, señales, eventos y alertas.
- Mantener alertas como capa central mediante `alertcondition()`.
- Registrar pruebas de demo o backtest como evidencia verificable.
- El indicador v2.5.0 mantiene configuración automática: `tfMin <= 15` usa EMAs 9/21 + RSI14; el resto usa EMAs 10/20 + RSI14.
- La puerta swing usa `request.security()` con `W`, `D` y `60`; si `exigirFractalidadSwing=true`, LONG/SHORT no aparecen sin sincronía de los tres fractales.
- La EMA50 es filtro fuerte obligatorio junto con EMA200.
- La lectura de manos fuertes se aproxima con absorción, barrida, volumen y esfuerzo/resultado; `exigirManosFuertes` queda desactivado por defecto.
- La estrategia no replica todavía la puerta fractal v2.5.0.

## Siguiente paso
1. Compilar `indicador_wyckoff_ema_rsi_v2.pine` en TradingView.
2. Confirmar que `request.security()` acepta `f_estadoFractal()` y los timeframes `W`, `D`, `60`.
3. Validar `BTCUSDT.P` BingX en semanal/diario/1h y revisar panel `AUTO SWING`.
4. Confirmar que `NO SYNC` bloquea señales con `exigirFractalidadSwing=true`.
5. Revisar EMA50, `EMA50_FILTER`, `SYNC+`, `SYNC-`, `MF+` y `MF-`.
6. Crear alerta real en TradingView y capturar payload con campos de fractalidad.
7. Ejecutar `python3 scripts/validar_documentacion_viva.py` en clon local.
8. Decidir si se crea v2.6.0 para adaptar la estrategia/backtest a la puerta fractal.

## Riesgos abiertos
- Pine Script v2.5.0 no se ha compilado todavía dentro de TradingView.
- No hay backtest validado ni demo forward test.
- La detección Wyckoff, divergencia simple, absorción RSI y manos fuertes son heurísticas simplificadas.
- La estrategia v2.2 no debe usarse para afirmar rendimiento de la lógica fractal v2.5.0.
