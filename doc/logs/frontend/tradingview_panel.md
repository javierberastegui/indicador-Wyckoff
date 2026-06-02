# Log — TradingView / visual

## Estado inicial
No hay Pine Script confirmado en esta base documental.

## Criterios futuros
- inputs claros
- plots explicables
- labels no invasivos
- alerts nacidas de eventos estructurados
- no mezclar toda la lógica visual, señal y validación sin separación documentada

### 2026-06-01 — Pine Script v2.0
- Dominio: `tradingview`.
- Cambio: añadidos indicador overlay, estrategia de backtesting y helper RSI.
- Inputs: presets `15m`, `1h RSI14`, `1h RSI21`, `Manual`, modo EMA, RSI, lateralidad, volumen, divergencias y absorciones.
- Plots: EMA rápida, EMA lenta, EMA media opcional, EMA200, zonas laterales Wyckoff, señales LONG/SHORT, divergencias y absorciones.
- Alerts: JSON con `event_type`, `signal`, `symbol`, `timeframe`, `price`, `sl`, `tp`, `source_module`, `severity`.
- Validación: pendiente de compilación en TradingView.
- Pendiente: probar primero `BTCUSDT.P` BingX 1h con preset `1h RSI14`; después `15m`.

### 2026-06-02 — estrategia con runner ATR manual
- Dominio: `tradingview`.
- Cambio: `estrategia_wyckoff_ema_rsi_v2.pine` mantiene entradas y alertas existentes, pero separa TP parcial y runner para que el TP solo se emita antes de marcar el parcial como hecho.
- Cambio: añadido trailing manual ATR estilo chandelier: LONG usa máximo desde entrada menos ATR por multiplicador; SHORT usa mínimo desde entrada más ATR por multiplicador; el stop runner aplica ratchet a favor.
- Cambio: limpieza de estado al quedar flat o girar posición: SL/TP fijos, parcial hecho, stop runner y máximo/mínimo desde entrada.
- Validación: documentación viva validada con script local; TradingView debe confirmar compilación y comportamiento del Strategy Tester.
- Pendiente: probar presets `15m`, `1h RSI14` y `1h RSI21`, empezando por `BTCUSDT.P` BingX 1h.

### 2026-06-02 — v2.3 jerarquía visual overlay y panel RSI
- Dominio: `tradingview`.
- Cambio: añadido `modoEtiquetas` con modos `Compacto`, `Detallado` y `Solo flechas`; el modo compacto evita por defecto etiquetas grandes con SL/TP/fase sobre la vela.
- Cambio: añadidos marcadores visibles para cruces EMA (`EMA+`/`EMA-`) y retrocesos (`PB+`/`PB-`) separados de LONG/SHORT.
- Cambio: zonas de contexto Wyckoff ahora diferencian acumulación, distribución, markup y markdown con fondos suaves; soporte/resistencia por pivots queda opcional y desactivado por defecto.
- Cambio: divergencias/absorciones en overlay se reducen a iconos sin texto y con separación por ATR; el panel RSI muestra textos claros `DIV+`, `DIV-`, `ABS+`, `ABS-`.
- Validación: documentación viva y revisión de diff ejecutadas localmente; TradingView debe confirmar compilación y legibilidad real.
- Pendiente: capturar ejemplos visuales en `BTCUSDT.P` BingX para presets `1h RSI14`, `1h RSI21` y `15m`.
