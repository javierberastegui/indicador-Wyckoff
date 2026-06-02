# Relevo — TradingView / visual

## Estado actual
Pine Script v2.4.0 en rama de trabajo; indicador overlay y helper RSI ajustados para modo automático limpio y menos configuración visible. La estrategia v2.2 con TP parcial único y runner ATR manual no se tocó.

Archivos:
- `indicador_wyckoff_ema_rsi_v2.pine`
- `estrategia_wyckoff_ema_rsi_v2.pine`
- `rsi_panel_wyckoff_helper.pine`

## Decisiones activas
La visualización debe ayudar a entender la señal, no esconder la lógica.

La señal visual LONG/SHORT solo aparece cuando se cumplen filtros Wyckoff simplificados, EMAs, RSI, lateralidad y volumen si está activado. El modo automático v2.4.0 reduce inputs visibles, pero no cambia entradas/salidas ni añade alertas sueltas.

Jerarquía visual v2.4.0:
- Panel de estado: mantenerlo; ahora muestra AUTO, TF, EMAs activas, RSI activo, tendencia estructural, fuerza, fase simplificada y RSI actual.
- Configuración visible: visualización, filtros opcionales y soporte/resistencia on/off.
- Cruces EMA: `EMA+` / `EMA-`, separados de LONG/SHORT.
- Retrocesos: `PB+` = pullback long y `PB-` = pullback short; no son entrada por sí solos.
- Contexto: fondos suaves para acumulación, distribución, markup y markdown, con etiqueta solo en cambio de fase (`ACUM`, `DIST`, `MARKUP`, `MARKDOWN`).
- Divergencias/absorciones overlay: iconos pequeños sin texto por defecto; texto opcional con `mostrarTextoDivAbsOverlay`.
- Panel RSI: modo AUTO RSI14, textos claros `DIV+`, `DIV-`, `ABS+`, `ABS-` y fondo operativo por nivel 50 + pendiente.
- Soporte/resistencia: opcional, desactivado por defecto, parámetros anti-persiana internos.

## Siguiente paso
1. Compilar indicador en TradingView.
2. Compilar helper RSI en TradingView.
3. Compilar estrategia en TradingView y revisar que el TP parcial no se reemite después de ejecutarse.
4. Revisar `BTCUSDT.P` BingX 1h y confirmar AUTO 10/20 RSI14.
5. Revisar `BTCUSDT.P` BingX 15m y confirmar AUTO 9/21 RSI14.
6. Revisar que no se necesiten inputs técnicos para uso operativo rápido.
7. Registrar errores exactos si Pine marca problemas de sintaxis.
8. Registrar capturas antes/después si se confirma legibilidad.
