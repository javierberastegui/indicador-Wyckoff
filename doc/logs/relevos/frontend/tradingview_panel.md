# Relevo — TradingView / visual

## Estado actual
Pine Script v2.5.0 en `main`; indicador overlay ajustado para modo `AUTO SWING`, sincronía semanal/diario/1h, EMA50 visible como filtro fuerte y marcadores visuales de manos fuertes. La estrategia v2.2 con TP parcial único y runner ATR manual no se tocó.

Archivos:
- `indicador_wyckoff_ema_rsi_v2.pine`
- `estrategia_wyckoff_ema_rsi_v2.pine`
- `rsi_panel_wyckoff_helper.pine`

## Decisiones activas
La visualización debe ayudar a entender la señal, no esconder la lógica.

La señal visual LONG/SHORT solo aparece cuando se cumplen filtros Wyckoff simplificados, EMAs, RSI, lateralidad, volumen si está activado, EMA50 y fractalidad W/D/1H si `exigirFractalidadSwing=true`. El modo v2.5.0 añade fractalidad, pero mantiene alertas centralizadas al final del indicador.

Jerarquía visual v2.5.0:
- Panel de estado: mantenerlo; ahora muestra `AUTO SWING`, TF, EMAs activas, RSI activo, tendencia, fuerza, fractal W/D/1H, dirección de cada fractal, EMA50, manos fuertes, fase y RSI actual.
- Configuración visible: filtros opcionales, fractalidad swing, visualización y soporte/resistencia on/off.
- EMA50: línea visible y filtro fuerte operativo.
- Sincronía fractal: `SYNC+` / `SYNC-`, separados de LONG/SHORT.
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
3. Compilar estrategia en TradingView sabiendo que aún no incluye la puerta fractal v2.5.0.
4. Revisar `BTCUSDT.P` BingX semanal, diario y 1h y confirmar panel `AUTO SWING`.
5. Revisar que `FRACTAL_SYNC` muestra `1`, `-1` o `0` correctamente en Data Window.
6. Revisar que `NO SYNC` impide señales si `exigirFractalidadSwing=true`.
7. Revisar legibilidad de EMA50, `SYNC+`, `SYNC-`, `MF+` y `MF-`.
8. Registrar errores exactos si Pine marca problemas de sintaxis.
9. Registrar capturas antes/después si se confirma legibilidad.
