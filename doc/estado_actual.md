# Estado actual

## Proyecto
`indicador-Wyckoff`

## Estado operativo
Documentación viva inicial aplicada y versión funcional v2.2 preparada en rama de trabajo con gestión de riesgo de estrategia ajustada.

## Arquitectura viva actual
- indicador Wyckoff + EMA + RSI en Pine Script
- estrategia de backtesting separada con TP parcial configurable, runner a breakeven y trailing manual ATR con ratchet
- helper visual RSI opcional
- reglas Wyckoff simplificadas
- reglas EMAs configurables
- confirmación RSI estructural
- motor de señales long/short
- eventos estructurados representados como señales candidatas
- capa central de alertas mediante `alertcondition()`
- validación/backtesting pendiente en TradingView; gestión de riesgo v2.2 pendiente de compilación en plataforma
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
- Para perfil intermedio se prioriza `1h RSI14` como validación inicial y `15m` como preset más reactivo.
- La estrategia mantiene entradas existentes y Pine Script v5; las salidas quedan silenciosas sin eventos `risk.*`.
- El TP parcial de estrategia se emite solo mientras el parcial no está hecho; después el runner usa breakeven y trailing manual ATR con `trailDebil=1.2` o `trailFuerte=2.5`.

## Pendiente inmediato
1. Compilar `indicador_wyckoff_ema_rsi_v2.pine` en TradingView.
2. Compilar `estrategia_wyckoff_ema_rsi_v2.pine` en TradingView y verificar TP parcial único + runner con breakeven/trailing ATR.
3. Validar `BTCUSDT.P` de BingX en 1h con preset `1h RSI14`.
4. Comparar después con `15m`.
5. Registrar capturas, rango temporal, métricas y resultado en logs antes de hablar de rentabilidad.
