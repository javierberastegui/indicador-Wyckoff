# Relevo — TradingView / visual

## Estado actual
Pine Script v2.6.0 en `main`; indicador overlay ajustado para modo `DAYTRADING`, sincronía `1D` macro / `1H` lupa / `5m` pistola, EMA50 visible como filtro fuerte y marcadores visuales de manos fuertes. La estrategia v2.2 con TP parcial único y runner ATR manual no se tocó.

Archivos:
- `indicador_wyckoff_ema_rsi_v2.pine`
- `estrategia_wyckoff_ema_rsi_v2.pine`
- `rsi_panel_wyckoff_helper.pine`

## Decisiones activas
La visualización debe ayudar a entender la señal, no esconder la lógica.

La señal visual LONG/SHORT solo aparece cuando se cumplen filtros Wyckoff simplificados, EMAs, RSI, lateralidad, volumen si está activado, EMA50, puerta DayTrading 1D/1H/5m si `exigirFractalidadDayTrading=true`, y gráfico 5m si `exigirGraficoEntrada5m=true`. El modo v2.6.0 adapta fractalidad a DayTrading, pero mantiene alertas centralizadas al final del indicador.

Jerarquía visual v2.6.0:
- Panel de estado: mantenerlo; ahora muestra `DAYTRADING`, plan, comentario, macro 1D, lupa 1H, pistola 5m, gráfico, EMA50, RSI y Wyckoff local.
- Configuración visible: filtros opcionales, fractalidad day trading, visualización, estilo EMAs y soporte/resistencia on/off.
- EMA50: línea visible y filtro fuerte operativo.
- Sincronía DayTrading: `DT+` / `DT-`, separados de LONG/SHORT.
- Manos fuertes: `MF+` / `MF-`, separados de LONG/SHORT.
- Cruces EMA: `EMA+` / `EMA-`, separados de LONG/SHORT.
- Retrocesos: `PB+` = pullback long y `PB-` = pullback short; no son entrada por sí solos.
- Contexto: fondos suaves para acumulación, distribución, markup y markdown, con etiqueta solo en cambio de fase (`ACUM`, `DIST`, `MARKUP`, `MARKDOWN`).
- Divergencias/absorciones overlay: iconos pequeños sin texto por defecto; texto opcional con `mostrarTextoDivAbsOverlay`.
- Panel RSI: modo AUTO RSI14, textos claros `DIV+`, `DIV-`, `ABS+`, `ABS-` y fondo operativo por nivel 50 + pendiente.
- Soporte/resistencia: opcional, desactivado por defecto, parámetros anti-persiana internos.

## Siguiente paso
1. Compilar indicador en TradingView.
2. Compilar helper RSI en TradingView.
3. Compilar estrategia en TradingView sabiendo que aún no incluye la puerta DayTrading v2.6.0.
4. Revisar `BTCUSDT.P` BingX diario, 1h y 5m y confirmar panel `DAYTRADING`.
5. Revisar que `DAYTRADING_SYNC` muestra `1`, `-1` o `0` correctamente en Data Window.
6. Revisar que `CAMBIAR A 5m` impide señales si `exigirGraficoEntrada5m=true`.
7. Revisar que `ESPERAR` impide señales si `exigirFractalidadDayTrading=true`.
8. Revisar legibilidad de EMA50, `DT+`, `DT-`, `MF+` y `MF-`.
9. Registrar errores exactos si Pine marca problemas de sintaxis.
10. Registrar capturas antes/después si se confirma legibilidad.
