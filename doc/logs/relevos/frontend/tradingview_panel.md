# Relevo — TradingView / visual

## Estado actual
Pine Script v2.3.1 en rama de trabajo; indicador overlay ajustado para reducir ruido visual detectado en TradingView. La estrategia v2.2 con TP parcial único y runner ATR manual no se tocó.

Archivos:
- `indicador_wyckoff_ema_rsi_v2.pine`
- `estrategia_wyckoff_ema_rsi_v2.pine`
- `rsi_panel_wyckoff_helper.pine`

## Decisiones activas
La visualización debe ayudar a entender la señal, no esconder la lógica.

La señal visual LONG/SHORT solo aparece cuando se cumplen filtros Wyckoff simplificados, EMAs, RSI, lateralidad y volumen si está activado. La limpieza v2.3.1 añade ayudas visuales menos invasivas, pero no cambia entradas/salidas ni añade alertas sueltas.

Jerarquía visual v2.3.1:
- Panel de estado: mantenerlo; resume tendencia estructural, fuerza, fase simplificada y RSI confirmador.
- LONG/SHORT: `modoEtiquetas` (`Compacto`, `Detallado`, `Solo flechas`).
- Cruces EMA: `EMA+` / `EMA-`, separados de LONG/SHORT.
- Retrocesos: `PB+` = pullback long y `PB-` = pullback short; no son entrada por sí solos.
- Contexto: fondos suaves para acumulación, distribución, markup y markdown, con etiqueta solo en cambio de fase (`ACUM`, `DIST`, `MARKUP`, `MARKDOWN`).
- Divergencias/absorciones overlay: iconos pequeños sin texto por defecto; texto opcional con `mostrarTextoDivAbsOverlay`.
- Panel RSI: textos claros `DIV+`, `DIV-`, `ABS+`, `ABS-` y fondo operativo por nivel 50 + pendiente.
- Soporte/resistencia: opcional, desactivado por defecto, 4 líneas por lado, filtro de duplicados por ATR y ocultación de líneas lejanas.

## Siguiente paso
1. Compilar indicador en TradingView.
2. Compilar helper RSI en TradingView.
3. Compilar estrategia en TradingView y revisar que el TP parcial no se reemite después de ejecutarse.
4. Revisar Strategy Tester en `BTCUSDT.P` BingX 1h.
5. Validar legibilidad visual con preset `1h RSI14`, después `1h RSI21` y `15m`.
6. Revisar especialmente S/R activado y desactivado, textos DIV/ABS apagados, etiquetas de fase y lectura PB.
7. Registrar errores exactos si Pine marca problemas de sintaxis.
8. Registrar capturas antes/después si se confirma legibilidad.
