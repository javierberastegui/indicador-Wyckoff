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

### 2026-06-02 — v2.3.1 limpieza de ruido visual
- Dominio: `tradingview`.
- Cambio: soporte/resistencia sigue desactivado por defecto, limita 4 líneas por lado, evita pivots duplicados cercanos por ATR y permite ocultar líneas alejadas del precio actual.
- Cambio: divergencias/absorciones en overlay quedan como iconos pequeños sin texto por defecto; `mostrarTextoDivAbsOverlay` permite reactivar texto si se necesita.
- Cambio: zonas Wyckoff añaden etiquetas compactas solo en cambios de fase (`ACUM`, `DIST`, `MARKUP`, `MARKDOWN`) para que el fondo no se perciba solo como rojo/verde.
- Cambio: README explica `PB+`/`PB-` y la interpretación del panel de estado.
- Validación: documentación viva y revisión de diff ejecutadas localmente; TradingView debe confirmar compilación y legibilidad real.
- Pendiente: revisar en TradingView que S/R ya no genere efecto persiana y registrar capturas en 1h/15m.

### 2026-06-02 — v2.4.0 modo AUTO para operar rápido
- Dominio: `tradingview`.
- Cambio: la configuración visible se reduce a visualización, filtros opcionales y el interruptor de soporte/resistencia; se eliminan presets y ajustes técnicos visibles del indicador.
- Cambio: el overlay muestra en panel y Data Window `AUTO`, timeframe actual, EMAs activas y RSI activo.
- Cambio: `rsi_panel_wyckoff_helper.pine` elimina preset visible y muestra `AUTO RSI14` con timeframe actual.
- Cambio: la selección automática conserva 15m con EMAs 9/21 + RSI14 y 1h/intermedios con EMAs 10/20 + RSI14.
- Validación: documentación viva y revisión de diff ejecutadas localmente; TradingView debe confirmar compilación y legibilidad real.
- Pendiente: validar en TradingView que el panel refleje correctamente 15m y 1h, y registrar capturas.

### 2026-06-22 — v2.5.0 panel swing fractal
- Dominio: `tradingview`, `core_indicador`, `senales`, `eventos`, `alertas`.
- Cambio: el panel cambia a `AUTO SWING` y añade filas para `Fractal W/D/1H`, dirección `W / D / 1H`, EMA50, manos fuertes y fases local/MTF.
- Cambio: el overlay añade EMA50 visible, marcadores `SYNC+`/`SYNC-` al sincronizar fractalidad y marcadores `MF+`/`MF-` para manos fuertes.
- Cambio: Data Window añade plots invisibles para `FRACTAL_SYNC`, `FRACTAL_W`, `FRACTAL_D`, `FRACTAL_1H`, `EMA50_FILTER` y `MANOS_FUERTES`.
- Cambio: las alertas LONG/SHORT conservan `alertcondition()` central, pero su JSON incorpora fractalidad, EMA50, manos fuertes y `reason`.
- Validación: pendiente de compilación real en TradingView; no hay backtest ni forward test registrado.
- Pendiente: revisar legibilidad del panel en 1h, confirmar que `NO SYNC` bloquea señales y capturar payload real de alerta.
