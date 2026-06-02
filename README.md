# indicador-Wyckoff

Repositorio para desarrollar un indicador basado en Metodología Wyckoff, cruces de EMAs, RSI y generación de señales long/short revisables.

## Estado actual

Versión funcional v2.4.0 en desarrollo: Wyckoff simplificado + EMAs + RSI + alertas JSON + estrategia de backtesting, con **modo automático limpio** para elegir EMAs/RSI según el timeframe del gráfico y con panel RSI helper separado.

Antes de tocar código, leer:
1. `AGENTS.md`
2. `doc/instrucciones/README.md`
3. `doc/estado_actual.md`
4. `doc/protocolo_relevo.md`
5. logs y relevos del dominio afectado

## Regla clave

Los módulos relevantes deben emitir eventos estructurados. Las notificaciones se deciden en una capa central de reglas, evitando avisos sueltos acoplados módulo a módulo.

En Pine Script la separación se expresa así:
- condiciones internas como eventos candidatos (`signal.long_candidate`, `signal.short_candidate`),
- reglas centrales mediante `alertcondition()`,
- mensajes JSON trazables para webhook.

La mejora v2.4.0 no añade alertas nuevas: el modo automático solo selecciona EMAs/RSI y parámetros internos por timeframe; las alertas LONG/SHORT siguen centralizadas al final del indicador.

## Indicador Wyckoff + EMA + RSI v2.4.0

La versión actual implementa una lectura operativa simplificada de Wyckoff combinada con:
- selección automática de EMAs y RSI según timeframe del gráfico,
- cruces EMA y entradas por retroceso (pullback) a la EMA rápida,
- filtro de tendencia con EMA200,
- confirmación RSI por nivel 50 y pendiente,
- divergencia RSI simple como **aviso de tendencia débil** (no bloquea entradas),
- clasificación de tendencia en **FUERTE** o **DÉBIL** (cinta de color + panel de estado),
- riesgo dinámico interno: tendencia débil → **1×2**, tendencia fuerte → **2×4**,
- gestión de trade en estrategia separada: entrada completa, SL inicial para toda la posición, TP parcial configurable y runner posterior con breakeven + trailing manual ATR tipo chandelier con ratchet,
- detección aproximada de absorción,
- filtro de lateralidad por rango/ATR,
- confirmación opcional por volumen,
- capa visual limpia con jerarquía entre señales, cruces EMA, retrocesos, divergencias/absorciones y contexto Wyckoff,
- alertas JSON preparadas para TradingView/webhook,
- estrategia separada para backtesting.

La detección Wyckoff es heurística. No pretende identificar toda la metodología clásica; aproxima fases útiles para operar y validar señales.

### Modo automático limpio

El indicador ya no muestra inputs de preset, modo EMA manual ni RSI manual. Detecta el timeframe actual con `timeframe.in_seconds() / 60` y aplica:

| Timeframe del gráfico | EMAs activas | RSI activo | Lateralidad interna |
|---|---:|---:|---:|
| `<= 15m` | 9/21 | 14 | lookback 18, ratio rango/ATR 4.5 |
| `>= 60m` | 10/20 | 14 | lookback 24, ratio rango/ATR 5.5 |
| intermedio | 10/20 | 14 | lookback 24, ratio rango/ATR 5.5 |

Los valores técnicos quedan como constantes internas para reducir configuración visible: ATR 14, pendiente RSI 3, divergencia 8, pendiente EMA200 10, separación EMA/ATR 0.5, aviso de divergencia 5 barras y SL/TP internos iguales a v2.3.x.

El panel de estado y el Data Window muestran información del modo automático: `AUTO`, timeframe actual, EMAs activas y RSI activo.

### Configuración visible mínima

Quedan visibles solo controles operativos:

- **Filtros opcionales**: confirmación por volumen, media de volumen y exigencia de absorción/divergencia favorable.
- **Visualización**: divergencias, absorciones, cinta de tendencia, panel de estado, cruces EMA, zonas Wyckoff, retrocesos, texto DIV/ABS en overlay y nombre de zona Wyckoff al cambiar.
- **Soporte/resistencia**: interruptor único, desactivado por defecto; los pivots, límite de líneas y filtros anti-duplicado quedan internos para evitar efecto persiana.

### Mejora visual vigente

El overlay principal prioriza lectura rápida y menos ruido:

- LONG/SHORT usa modo compacto interno por defecto: marcador visible y limpio, sin SL/TP/fase sobre la vela.
- `mostrarCrucesEma` activa marcas `EMA+` / `EMA-` separadas de LONG/SHORT.
- `mostrarRetrocesos` activa marcas `PB+` / `PB-` para pullbacks a EMA rápida sin confundirlos con señal confirmada.
- `mostrarZonasWyckoff` pinta fondos suaves para acumulación, distribución, markup y markdown, sin tapar velas ni EMAs; `mostrarNombreZonaWyckoff` muestra una etiqueta compacta solo cuando cambia la fase (`ACUM`, `DIST`, `MARKUP`, `MARKDOWN`).
- `mostrarSoporteResistencia` dibuja S/R por pivots con líneas transparentes, limitadas a 4 por lado, sin duplicados cercanos por ATR y con ocultación interna de líneas lejanas.
- Divergencias y absorciones en overlay se muestran como iconos pequeños sin texto y con offset por ATR. `mostrarTextoDivAbsOverlay` viene desactivado; el texto claro queda en el panel RSI.

### Panel RSI operativo

`rsi_panel_wyckoff_helper.pine` es un helper separado (`overlay=false`) para leer RSI sin ensuciar el gráfico principal:

- Modo automático RSI14 sin preset visible.
- RSI visible con línea 50 destacada y niveles 70/30.
- Fondo suave cuando RSI > 50 con pendiente positiva o RSI < 50 con pendiente negativa.
- Inputs `mostrarDivergenciasRsi`, `mostrarAbsorcionesRsi` y `mostrarFondoRsi`.
- Divergencias (`DIV+` / `DIV-`) y absorciones (`ABS+` / `ABS-`) con texto claro dentro del panel RSI.
- Mini panel/Data Window con `AUTO RSI14` y timeframe actual.

### Tendencia, fuerza y gestión de riesgo

El indicador prioriza que la tendencia se vea **clara**:

- **Cinta de color** entre la EMA rápida y la lenta: verde (alcista) o roja (bajista). Más opaca = tendencia **FUERTE**; más tenue = tendencia **DÉBIL**.
- **Panel de estado** (esquina superior derecha): modo AUTO, timeframe, EMAs, RSI activo, dirección, fuerza, fase Wyckoff y RSI actual.

Interpretación del panel de estado:
- **Modo/TF/EMAs/RSI** = configuración automática activa según timeframe del gráfico.
- **Tendencia** = dirección estructural según precio, EMA200 y pendiente de EMA200.
- **Fuerza** = clasificación fuerte/débil y ratio sugerido según separación de EMAs y divergencia contraria reciente.
- **Fase** = lectura Wyckoff simplificada del contexto, no una fase clásica completa validada.
- **RSI** = confirmador estructural; no debe leerse como señal aislada.

Una **tendencia FUERTE** requiere: dirección clara respecto a EMA200, EMAs rápida/lenta bien separadas (≥ `sepMinAtr` × ATR) y **sin divergencia contraria reciente**. En caso contrario la tendencia es **DÉBIL**.

La divergencia ya **no impide** abrir LONG/SHORT: solo marca la tendencia como débil y, por tanto, fuerza el riesgo conservador **1×2**.

| Fuerza | SL (xATR) | TP (xATR) | Ratio |
|---|---:|---:|---:|
| DÉBIL | 1.0 | 2.0 | 1×2 |
| FUERTE | 2.0 | 4.0 | 2×4 |

Gestión en la estrategia: la entrada abre la posición completa con un **SL inicial efectivo para toda la posición**. Al tocar el TP parcial se cierra solo el porcentaje configurado en `cierreParcialPct` (**80% por defecto**) y el runner conserva el resto de la posición. Tras ejecutarse el parcial, el runner pasa primero a **breakeven** y después usa trailing manual ATR estilo chandelier con ratchet: en LONG guarda el máximo desde entrada y calcula `máximo - ATR × multiplicador`; en SHORT guarda el mínimo desde entrada y calcula `mínimo + ATR × multiplicador`. El stop del runner solo avanza a favor y nunca retrocede.

Inputs de trailing en la estrategia: tendencia débil usa `trailDebil = 1.2` (más corto) y tendencia fuerte usa `trailFuerte = 2.5` (más amplio). Las salidas del runner quedan silenciosas; no se añaden eventos `risk.*` en esta iteración.

### Entradas por retroceso

Con `usarRetroceso` activo internamente se generan señales cuando el precio retrocede a la EMA rápida y rebota en la dirección de la tendencia. Así no se pierden tramos largos de tendencia entre cruces.

Lectura visual de retrocesos:
- `PB+` = retroceso en tendencia alcista hacia la EMA rápida.
- `PB-` = retroceso en tendencia bajista hacia la EMA rápida.
- `PB+`/`PB-` no son una entrada por sí solos; ayudan a identificar una posible continuación dentro del contexto, mientras la señal confirmada sigue siendo LONG/SHORT.

## Archivos principales

- `indicador_wyckoff_ema_rsi_v2.pine`: indicador overlay para señales visuales y alertas.
- `estrategia_wyckoff_ema_rsi_v2.pine`: estrategia con la misma lógica para Strategy Tester.
- `rsi_panel_wyckoff_helper.pine`: panel RSI opcional separado.

## Cómo interpreta señales

### LONG

Una señal LONG requiere:
- cruce de EMAs válido **o** retroceso a la EMA rápida,
- precio por encima de EMA200,
- pendiente de EMA200 positiva,
- RSI > 50,
- pendiente RSI positiva,
- mercado fuera de lateralidad,
- volumen válido si el filtro de volumen está activo,
- absorción/divergencia favorable si se exige estructura extra.

La divergencia bajista **ya no bloquea** la señal: solo marca la tendencia como débil (riesgo 1×2).

### SHORT

Una señal SHORT requiere:
- cruce de EMAs válido **o** retroceso a la EMA rápida,
- precio por debajo de EMA200,
- pendiente de EMA200 negativa,
- RSI < 50,
- pendiente RSI negativa,
- mercado fuera de lateralidad,
- volumen válido si el filtro de volumen está activo,
- absorción/divergencia favorable si se exige estructura extra.

La divergencia alcista **ya no bloquea** la señal: solo marca la tendencia como débil (riesgo 1×2).

## Alertas JSON

Ejemplo LONG emitido por TradingView:

```json
{"event_type":"signal.long_candidate","signal":"LONG","symbol":"{{ticker}}","timeframe":"{{interval}}","price":"{{close}}","sl":"{{plot(\"SL_LONG\")}}","tp":"{{plot(\"TP_LONG\")}}","source_module":"tradingview.indicador_wyckoff_ema_rsi_v2","severity":"info"}
```

Ejemplo SHORT:

```json
{"event_type":"signal.short_candidate","signal":"SHORT","symbol":"{{ticker}}","timeframe":"{{interval}}","price":"{{close}}","sl":"{{plot(\"SL_SHORT\")}}","tp":"{{plot(\"TP_SHORT\")}}","source_module":"tradingview.indicador_wyckoff_ema_rsi_v2","severity":"info"}
```

## Uso recomendado con TradingView y BingX

1. Abrir TradingView.
2. Cargar `BTCUSDT.P` de BingX.
3. Cargar `indicador_wyckoff_ema_rsi_v2.pine`; el indicador selecciona automáticamente EMAs/RSI según el timeframe.
4. Validar primero 1h; después comparar 15m.
5. Cargar `rsi_panel_wyckoff_helper.pine` si se quiere panel RSI separado.
6. Crear alertas LONG/SHORT desde TradingView.
7. Operar primero en demo manual o demo conectada.
8. Usar `estrategia_wyckoff_ema_rsi_v2.pine` en Strategy Tester solo para validación separada.

## Validación documental

```bash
python3 scripts/validar_documentacion_viva.py
```

## Validación funcional pendiente

Pine Script debe validarse dentro de TradingView:
- compilación del indicador,
- compilación del helper RSI,
- compilación de la estrategia,
- Strategy Tester en BTCUSDT.P BingX 1h,
- comparación con BTCUSDT.P BingX 15m,
- revisión de señales en lateral,
- revisión de jerarquía visual en overlay y panel RSI,
- revisión de alertas JSON.

No se debe publicar como rentable sin evidencias de backtest, demo o forward test.

## Enfoque

No se promete rentabilidad. Las señales deben ser explicables, trazables y validadas con evidencias.
