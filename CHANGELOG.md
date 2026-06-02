# Changelog

## [2.4.0] - 2026-06-02

### Added
- Modo automático limpio en `indicador_wyckoff_ema_rsi_v2.pine`: el timeframe actual se detecta con `timeframe.in_seconds() / 60` y selecciona EMAs/RSI sin inputs de preset.
- Panel de estado y Data Window muestran `AUTO`, timeframe actual, EMAs activas y RSI activo.
- `rsi_panel_wyckoff_helper.pine` pasa a modo automático RSI14 sin preset visible y añade mini panel/Data Window con modo y timeframe.

### Changed
- Se ocultan como constantes internas los ajustes técnicos de ATR, lateralidad, divergencia, pendiente RSI, pendiente EMA200, fuerza, retroceso, SL/TP y S/R avanzado.
- La configuración visible queda reducida a visualización, filtros opcionales y el interruptor limpio de soporte/resistencia.
- La selección automática conserva los valores vigentes: `<=15m` usa EMAs 9/21 + RSI14; `>=60m` e intermedios usan EMAs 10/20 + RSI14.
- No se tocó `estrategia_wyckoff_ema_rsi_v2.pine`, el runner ATR manual, las alertas ni la lógica de entrada/salida salvo la selección automática de EMAs/RSI.

### Tests
- Validación documental mediante `python3 scripts/validar_documentacion_viva.py`.
- Revisión de espacios mediante `git diff --check`.
- Compilación real de Pine Script sigue pendiente en TradingView.

## [2.3.1] - 2026-06-02

### Changed
- Limpieza visual del overlay: soporte/resistencia mantiene `mostrarSoporteResistencia=false` por defecto, baja `maxLineasSR` a 4 por lado y añade filtro de duplicados con `distanciaMinimaSrAtr`.
- Las líneas S/R son más transparentes y pueden ocultarse si están lejos del precio con `mostrarSoloSrCercano` y `distanciaSrVisibleAtr`, evitando efecto persiana.
- Divergencias y absorciones del overlay mantienen iconos pequeños sin texto por defecto y añaden `mostrarTextoDivAbsOverlay=false` para activar texto solo si se necesita.
- Zonas Wyckoff mantienen fondo suave y añaden etiqueta compacta de cambio de fase (`ACUM`, `DIST`, `MARKUP`, `MARKDOWN`) mediante `mostrarNombreZonaWyckoff`.
- README documenta `PB+`/`PB-` y la lectura del panel de estado.

### Tests
- Validación documental mediante `python3 scripts/validar_documentacion_viva.py`.
- Revisión de espacios mediante `git diff --check`.
- Compilación real de Pine Script sigue pendiente en TradingView.

## [2.3.0] - 2026-06-02

### Added
- Mejora visual del indicador overlay con inputs `mostrarCrucesEma`, `mostrarZonasWyckoff`, `mostrarRetrocesos`, `mostrarSoporteResistencia`, `pivotLen`, `maxLineasSR` y `modoEtiquetas`.
- Marcadores independientes `EMA+`/`EMA-` para cruces EMA y `PB+`/`PB-` para retrocesos a EMA rápida, sin añadir alertas nuevas.
- Zonas Wyckoff de fondo para acumulación, distribución, markup y markdown con colores suaves.
- Soporte/resistencia opcional por pivots con arrays de líneas, extensión a la derecha y límite configurable de líneas.
- Panel RSI v2.3 con inputs para divergencias, absorciones y fondo operativo RSI.

### Changed
- LONG/SHORT usan `modoEtiquetas` para separar modo compacto, detallado y solo flechas; por defecto se evita la etiqueta grande con SL/TP/fase.
- Divergencias y absorciones del overlay pasan a iconos sin texto con offset por ATR para reducir solapamientos; el texto operativo queda en el helper RSI.
- La mejora visual no cambia lógica de entrada/salida, no toca la estrategia ni el runner ATR manual, y mantiene la capa central de alertas al final del indicador.

### Tests
- Validación documental mediante `python3 scripts/validar_documentacion_viva.py`.
- Revisión de espacios mediante `git diff --check`.
- Compilación real de Pine Script sigue pendiente en TradingView.

## [2.2.0] - 2026-06-02

### Added
- Inputs `trailDebil` (1.2) y `trailFuerte` (2.5) en el grupo `Riesgo dinamico` de la estrategia para trailing manual ATR tipo chandelier.

### Changed
- La estrategia mantiene la lógica de entrada v2.1, Pine Script v5 y la capa central de alertas sin añadir eventos `risk.*`.
- La gestión de salidas pasa a entrada completa con SL inicial para toda la posición, TP parcial configurable (`cierreParcialPct`, 80% por defecto) y runner con breakeven + trailing ATR manual con ratchet.
- El TP parcial deja de emitirse cuando el parcial ya fue marcado como ejecutado, evitando cierres repetidos del runner en el precio del TP parcial.
- Al cerrar o girar posición se limpian SL/TP fijos, estado del parcial, stop del runner y máximo/mínimo desde entrada.

### Tests
- Validación documental mediante `python3 scripts/validar_documentacion_viva.py`.
- Compilación real de Pine Script sigue pendiente en TradingView.

## [2.1.0] - 2026-06-02

### Added
- Clasificación de tendencia en **FUERTE** / **DÉBIL** (separación de EMAs por ATR + ausencia de divergencia contraria reciente).
- Cinta de color entre EMA rápida y lenta y panel de estado (dirección, fuerza, fase, RSI) para ver la tendencia con claridad.
- Entradas por **retroceso** (pullback) a la EMA rápida, además del cruce de EMAs (`usarRetroceso`).
- Riesgo dinámico según fuerza: tendencia débil → **1×2**, tendencia fuerte → **2×4** (inputs `slDebil/tpDebil/slFuerte/tpFuerte`).
- Gestión de trade en la estrategia: al alcanzar el TP se cierra el `cierreParcialPct` (80% por defecto) y el resto pasa a breakeven.
- Campos `trend` y `strength` en las alertas JSON; plots `FUERZA_LONG`/`FUERZA_SHORT` (2=fuerte, 1=débil).

### Changed
- La divergencia RSI deja de **bloquear** entradas LONG/SHORT y pasa a ser un **aviso** que marca la tendencia como débil.
- SL/TP dejan de depender del preset y pasan a depender de la fuerza de la tendencia (1×2 / 2×4).
- `README.md` documenta tendencia/fuerza, riesgo dinámico, gestión 80%+breakeven y entradas por retroceso.

## [2.0.0] - 2026-06-01

### Added
- Nuevo indicador `indicador_wyckoff_ema_rsi_v2.pine`.
- Nueva estrategia `estrategia_wyckoff_ema_rsi_v2.pine`.
- Helper opcional `rsi_panel_wyckoff_helper.pine` para panel RSI separado.
- Presets `15m`, `1h RSI14`, `1h RSI21` y `Manual`.
- Filtro de tendencia por EMA200 y pendiente de EMA200.
- Confirmación RSI por nivel 50 y pendiente.
- Divergencia RSI simple.
- Heurística de absorción estilo Wyckoff.
- Filtro lateral por ratio rango/ATR.
- Confirmación opcional por volumen.
- Alertas JSON para webhook con `event_type`, señal, símbolo, timeframe, precio, SL, TP, módulo origen y severidad.

### Changed
- La metodología pasa de enfoque inicial documental a primera versión funcional Wyckoff + EMA + RSI.
- `README.md` documenta uso, presets, alertas y validación pendiente.
- `AGENTS.md` incorpora reglas específicas para RSI y presets operativos.
- `doc/instrucciones/mapa_dominios.md` incorpora el dominio `rsi`.

### Docs
- Estado actual actualizado a v2.0 en rama de trabajo.
- Logs y relevos actualizados por dominios `core_indicador`, `tradingview`, `alertas` y `documentacion`.

### Tests
- Validación documental prevista mediante `python3 scripts/validar_documentacion_viva.py`.
- Validación funcional pendiente en TradingView sobre `BTCUSDT.P` de BingX en 1h y 15m.
- No se registran resultados de rentabilidad, winrate ni drawdown hasta backtest o demo con evidencia.
