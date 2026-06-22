# Estado actual

## Proyecto
`indicador-Wyckoff`

## Estado operativo
Documentación viva aplicada y versión funcional v2.5.0 preparada en `main`: indicador overlay con modo automático swing, fractalidad semanal/diario/1h, EMA50 como filtro fuerte, lectura de manos fuertes y alertas JSON enriquecidas. La estrategia separada sigue en lógica v2.2 y no se tocó en esta fase.

## Arquitectura viva actual
- indicador Wyckoff + EMA + RSI en Pine Script con selección automática de EMAs/RSI por timeframe
- capa swing multi-timeframe con `request.security()` para semanal (`W`), diario (`D`) y 1h (`60`)
- EMA200 como filtro estructural base
- EMA50 como filtro fuerte operativo obligatorio para señales
- estrategia de backtesting separada con TP parcial configurable, runner a breakeven y trailing manual ATR con ratchet
- helper visual RSI opcional en modo automático RSI14
- reglas Wyckoff simplificadas
- lectura aproximada de manos fuertes por absorción, barrida, volumen y esfuerzo/resultado
- reglas EMAs configurables internamente por timeframe automático
- confirmación RSI estructural
- motor de señales long/short
- eventos estructurados representados como señales candidatas
- capa central de alertas mediante `alertcondition()`
- validación/backtesting pendiente en TradingView; v2.5.0 pendiente de compilación en plataforma
- documentación operativa viva

## Archivos funcionales vigentes
- `indicador_wyckoff_ema_rsi_v2.pine`
- `estrategia_wyckoff_ema_rsi_v2.pine`
- `rsi_panel_wyckoff_helper.pine`

## Decisiones activas
- No empezar desde cero si aparece código válido.
- No cambiar rutas base sin necesidad.
- No prometer rentabilidad.
- Eventos estructurados primero; notificaciones después mediante capa central.
- Logs por dominio como bitácora principal.
- `doc/logs/historico.md` no es bitácora principal.
- La detección Wyckoff queda documentada como simplificada.
- El RSI se usa como confirmador estructural: nivel 50, pendiente, divergencia simple y absorción aproximada.
- El indicador v2.5.0 mantiene modo automático: `<=15m` usa EMAs 9/21 + RSI14; `>=60m` e intermedios usan EMAs 10/20 + RSI14.
- Para swing trading, `exigirFractalidadSwing=true` bloquea señales si semanal, diario y 1h no están sincronizados a favor.
- La EMA50 es filtro fuerte obligatorio junto a EMA200: precio y pendiente deben ir a favor.
- La lectura de manos fuertes se muestra con `MF+`/`MF-` y puede exigirse con `exigirManosFuertes`, pero queda desactivada por defecto para no bloquear continuaciones limpias.
- Las alertas siguen centralizadas en `alertcondition()` y añaden campos de fractalidad, EMA50, manos fuertes y `reason`.
- La estrategia mantiene entradas/salidas previas y no incorpora todavía la puerta fractal v2.5.0.

## Pendiente inmediato
1. Compilar `indicador_wyckoff_ema_rsi_v2.pine` en TradingView y revisar modo AUTO SWING, panel y Data Window.
2. Validar que `request.security()` no marca errores en semanal, diario y 1h.
3. Verificar en `BTCUSDT.P` BingX semanal/diario/1h que `FRACTAL_SYNC`, `FRACTAL_W`, `FRACTAL_D` y `FRACTAL_1H` cambian correctamente.
4. Revisar que EMA50 aparece en overlay y que `EMA50_FILTER` devuelve `1`, `-1` o `0`.
5. Revisar marcadores `SYNC+`, `SYNC-`, `MF+` y `MF-`.
6. Confirmar que no hay señales LONG/SHORT si `exigirFractalidadSwing=true` y el panel marca `NO SYNC`.
7. Crear alerta real en TradingView y capturar payload JSON con campos de fractalidad.
8. Decidir en otra fase si se adapta `estrategia_wyckoff_ema_rsi_v2.pine` a v2.5.0 para backtest exacto.
9. Registrar capturas, rango temporal, métricas y resultado en logs antes de hablar de rentabilidad.
