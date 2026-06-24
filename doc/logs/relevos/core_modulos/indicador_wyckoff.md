# Relevo — indicador Wyckoff

## Estado actual
Versión funcional v2.6.0 en `main`: indicador overlay actualizado a modo DayTrading con macro `1D`, lupa `1H` y pistola `5m`. Mantiene EMA50 como filtro fuerte, EMA200 como filtro estructural, lectura visual de manos fuertes, eventos estructurados y alertas JSON centralizadas. La estrategia v2.2 con gestión de riesgo y runner ATR manual no se tocó.

Archivos funcionales:
- `indicador_wyckoff_ema_rsi_v2.pine`
- `estrategia_wyckoff_ema_rsi_v2.pine`
- `rsi_panel_wyckoff_helper.pine`

## Decisiones activas
- Separar reglas Wyckoff, EMAs, RSI, señales, eventos y alertas.
- Mantener alertas como capa central mediante `alertcondition()`.
- Registrar pruebas de demo o backtest como evidencia verificable.
- El indicador v2.6.0 mantiene configuración automática: `tfMin <= 5` usa EMAs 5/8/13 + RSI14; `tfMin <= 15` usa EMAs 9/21 + RSI14; el resto usa EMAs 10/20 + RSI14.
- La puerta DayTrading usa `request.security()` con `D`, `60` y `5`; si `exigirFractalidadDayTrading=true`, LONG/SHORT no aparecen sin alineación de macro 1D, lupa 1H y pistola 5m.
- Si `exigirGraficoEntrada5m=true`, LONG/SHORT no aparecen si el indicador no está cargado sobre gráfico 5m.
- La EMA50 es filtro fuerte obligatorio junto con EMA200.
- La lectura de manos fuertes se aproxima con absorción, barrida, volumen y esfuerzo/resultado; `exigirManosFuertes` queda desactivado por defecto.
- La estrategia no replica todavía la puerta DayTrading v2.6.0.

## Siguiente paso
1. Compilar `indicador_wyckoff_ema_rsi_v2.pine` en TradingView.
2. Confirmar que `request.security()` acepta `f_estadoFractal()` y los timeframes `D`, `60`, `5`.
3. Validar `BTCUSDT.P` BingX en diario/1h/5m y revisar panel `DAYTRADING`.
4. Confirmar que `CAMBIAR A 5m` bloquea señales con `exigirGraficoEntrada5m=true`.
5. Confirmar que `ESPERAR` bloquea señales con `exigirFractalidadDayTrading=true`.
6. Revisar EMA50, `EMA50_FILTER`, `DAYTRADING_SYNC`, `MACRO_1D`, `LUPA_1H`, `PISTOLA_5M` y `ENTRY_TF_OK`.
7. Crear alerta real en TradingView y capturar payload con campos DayTrading.
8. Ejecutar `python3 scripts/validar_documentacion_viva.py` en clon local.
9. Decidir si se crea v2.6.1 o v2.7.0 para adaptar la estrategia/backtest a la puerta DayTrading.

## Riesgos abiertos
- Pine Script v2.6.0 no se ha compilado todavía dentro de TradingView.
- No hay backtest validado ni demo forward test.
- La detección Wyckoff, divergencia simple, absorción RSI y manos fuertes son heurísticas simplificadas.
- La estrategia v2.2 no debe usarse para afirmar rendimiento de la lógica DayTrading v2.6.0.
- `request.security()` de 5m desde timeframes superiores debe revisarse visualmente; la ejecución real se recomienda en gráfico 5m.
