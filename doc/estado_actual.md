# Estado actual

## Proyecto
`indicador-Wyckoff`

## Estado operativo
Documentación viva aplicada y versión funcional v2.4.0 preparada en rama de trabajo con modo automático limpio para indicador overlay y helper RSI, sin cambios en la estrategia ni en el runner ATR manual.

## Arquitectura viva actual
- indicador Wyckoff + EMA + RSI en Pine Script con selección automática de EMAs/RSI por timeframe
- estrategia de backtesting separada con TP parcial configurable, runner a breakeven y trailing manual ATR con ratchet
- helper visual RSI opcional en modo automático RSI14
- reglas Wyckoff simplificadas
- reglas EMAs configurables internamente por timeframe automático
- confirmación RSI estructural
- motor de señales long/short
- eventos estructurados representados como señales candidatas
- capa central de alertas mediante `alertcondition()`
- validación/backtesting pendiente en TradingView; gestión de riesgo v2.2 y modo automático visual v2.4.0 pendientes de compilación en plataforma
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
- El indicador v2.4.0 no muestra preset, modo EMA manual ni RSI manual: `<=15m` usa EMAs 9/21 + RSI14; `>=60m` e intermedios usan EMAs 10/20 + RSI14.
- La configuración técnica de ATR, lateralidad, divergencia, fuerza, retroceso, riesgo visual y S/R avanzado queda como constantes internas para operar rápido.
- La estrategia mantiene entradas existentes y Pine Script v5; las salidas quedan silenciosas sin eventos `risk.*`.
- El TP parcial de estrategia se emite solo mientras el parcial no está hecho; después el runner usa breakeven y trailing manual ATR con `trailDebil=1.2` o `trailFuerte=2.5`.
- La v2.4.0 no añade alertas nuevas ni cambia entradas/salidas salvo la selección automática de EMAs/RSI del indicador/helper.

## Pendiente inmediato
1. Compilar `indicador_wyckoff_ema_rsi_v2.pine` en TradingView y revisar modo AUTO, panel y Data Window.
2. Compilar `rsi_panel_wyckoff_helper.pine` en TradingView y verificar modo AUTO RSI14.
3. Compilar `estrategia_wyckoff_ema_rsi_v2.pine` en TradingView y verificar TP parcial único + runner con breakeven/trailing ATR.
4. Validar `BTCUSDT.P` de BingX en 1h y confirmar EMAs 10/20 + RSI14.
5. Comparar después con 15m y confirmar EMAs 9/21 + RSI14.
6. Registrar capturas, rango temporal, métricas y resultado en logs antes de hablar de rentabilidad.
