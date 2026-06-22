# indicador-Wyckoff

Repositorio para desarrollar un indicador basado en Metodología Wyckoff, cruces de EMAs, RSI, lectura de fractalidad y generación de señales long/short revisables.

## Estado actual

Versión funcional v2.5.0 en desarrollo: Wyckoff simplificado + EMAs + RSI + alertas JSON + estrategia de backtesting separada, con **modo automático swing** para exigir sincronía de fractalidad semanal/diario/1h antes de buscar entrada.

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

La mejora v2.5.0 no crea alertas sueltas nuevas. Mantiene las alertas LONG/SHORT centralizadas al final del indicador, pero enriquece el payload con fractalidad, EMA50 y manos fuertes.

## Indicador Wyckoff + EMA + RSI v2.5.0

La versión actual implementa una lectura operativa simplificada de Wyckoff combinada con:
- selección automática de EMAs y RSI según timeframe del gráfico,
- filtro de tendencia con EMA200,
- **EMA50 como filtro fuerte obligatorio** para que la señal tenga estructura operativa,
- sincronía multi-timeframe **semanal + diario + 1h** mediante `request.security()`,
- cruces EMA y entradas por retroceso a la EMA rápida,
- confirmación RSI por nivel 50 y pendiente,
- divergencia RSI simple como aviso de tendencia débil,
- clasificación de tendencia en **FUERTE** o **DÉBIL**,
- riesgo dinámico interno: tendencia débil → **1×2**, tendencia fuerte → **2×4**,
- detección aproximada de absorción y lectura de **manos fuertes** por esfuerzo/resultado,
- filtro de lateralidad por rango/ATR,
- confirmación opcional por volumen,
- capa visual con señales, cruces EMA, retrocesos, sincronía W/D/1H, manos fuertes, divergencias/absorciones y contexto Wyckoff,
- alertas JSON preparadas para TradingView/webhook,
- estrategia separada para backtesting, todavía sin adaptar a la nueva fractalidad v2.5.0.

La detección Wyckoff es heurística. No pretende identificar toda la metodología clásica; aproxima fases útiles para operar y validar señales.

## Modo automático swing

El indicador mantiene el modo automático de EMAs/RSI del gráfico:

| Timeframe del gráfico | EMAs activas | RSI activo | Lateralidad interna |
|---|---:|---:|---:|
| `<= 15m` | 9/21 | 14 | lookback 18, ratio rango/ATR 4.5 |
| `>= 60m` | 10/20 | 14 | lookback 24, ratio rango/ATR 5.5 |
| intermedio | 10/20 | 14 | lookback 24, ratio rango/ATR 5.5 |

La capa swing añade una segunda lectura fija:
- semanal (`W`),
- diario (`D`),
- 1 hora (`60`).

Cada fractal debe cumplir dirección, RSI estructural, EMA50 y no estar en lateralidad para marcar dirección válida. Con `exigirFractalidadSwing=true`, que viene activado por defecto, no hay LONG si W/D/1H no están sincronizados alcistas y no hay SHORT si W/D/1H no están sincronizados bajistas.

## EMA50 como señal fuerte

La EMA200 conserva el papel de filtro estructural base. La EMA50 pasa a ser filtro fuerte operativo:

### LONG
- precio por encima de EMA200,
- pendiente EMA200 positiva,
- precio por encima de EMA50,
- pendiente EMA50 positiva.

### SHORT
- precio por debajo de EMA200,
- pendiente EMA200 negativa,
- precio por debajo de EMA50,
- pendiente EMA50 negativa.

La EMA50 también aparece en el panel y en Data Window como `EMA50_FILTER`: `1` alcista, `-1` bajista, `0` neutral.

## Fractalidad W/D/1H

El panel muestra:
- `Fractal W/D/1H`: `SYNC LONG`, `SYNC SHORT` o `NO SYNC`.
- `W / D / 1H`: dirección individual de cada fractal.
- `Fase`: fase local y fases simplificadas W/D/1H.

Interpretación:
- `SYNC LONG`: semanal, diario y 1h están alineados alcistas.
- `SYNC SHORT`: semanal, diario y 1h están alineados bajistas.
- `NO SYNC`: no buscar entrada swing si el filtro está activado.

El Data Window expone:
- `FRACTAL_SYNC`: `1` sincronía long, `-1` sincronía short, `0` sin sincronía.
- `FRACTAL_W`, `FRACTAL_D`, `FRACTAL_1H`: dirección individual por fractal.

## Wyckoff y manos fuertes

Wyckoff sigue clasificando el contexto local:
- `ACUM`: acumulación simplificada.
- `DIST`: distribución simplificada.
- `MARKUP`: avance tendencial.
- `MARKDOWN`: caída tendencial.
- `TRANS`: transición.

Las manos fuertes se aproximan con una lectura simple de esfuerzo/resultado:
- volumen superior a media (`volClimaxMult = 1.5`),
- barrida de mínimo/máximo reciente,
- cierre recuperando la mitad de la vela,
- rango comprimido con volumen alto,
- absorción RSI/vela favorable.

Marcadores visuales:
- `MF+`: posible absorción o participación fuerte alcista.
- `MF-`: posible absorción o participación fuerte bajista.

Por defecto `exigirManosFuertes=false` para no bloquear todas las continuaciones swing. Si se activa, la señal LONG/SHORT exige también manos fuertes favorables.

## Configuración visible mínima

Quedan visibles controles operativos:
- **Filtros opcionales**: confirmación por volumen, media de volumen, exigencia de absorción/divergencia favorable y exigencia de manos fuertes.
- **Fractalidad swing**: exigir sincronía semanal/diario/1h, mostrar sincronía W/D/1H y mostrar manos fuertes.
- **Visualización**: divergencias, absorciones, cinta de tendencia, panel de estado, cruces EMA, zonas Wyckoff, retrocesos, texto DIV/ABS en overlay y nombre de zona Wyckoff al cambiar.
- **Soporte/resistencia**: interruptor único, desactivado por defecto; pivots, límite de líneas y filtros anti-duplicado quedan internos.

## Tendencia, fuerza y gestión de riesgo

La tendencia **FUERTE** requiere:
- dirección clara respecto a EMA200,
- EMA50 alineada a favor,
- EMAs rápida/lenta separadas por ATR,
- ausencia de divergencia contraria reciente,
- fractalidad W/D/1H sincronizada si el filtro swing está activo.

La tendencia **DÉBIL** conserva contexto direccional, pero falla alguno de los elementos de fuerza. La divergencia contraria no bloquea por sí sola; rebaja la lectura a débil.

| Fuerza | SL (xATR) | TP (xATR) | Ratio |
|---|---:|---:|---:|
| DÉBIL | 1.0 | 2.0 | 1×2 |
| FUERTE | 2.0 | 4.0 | 2×4 |

La estrategia separada mantiene la gestión previa: entrada completa, SL inicial para toda la posición, TP parcial configurable y runner posterior con breakeven + trailing manual ATR tipo chandelier con ratchet. La estrategia todavía no incorpora la puerta fractal v2.5.0.

## Entradas por retroceso

Con `usarRetroceso` activo internamente se generan señales cuando el precio retrocede a la EMA rápida y rebota en la dirección de la tendencia.

Lectura visual:
- `PB+` = retroceso en tendencia alcista hacia la EMA rápida.
- `PB-` = retroceso en tendencia bajista hacia la EMA rápida.
- `PB+`/`PB-` no son entrada por sí solos; la señal confirmada sigue siendo LONG/SHORT cuando pasan todos los filtros.

## Archivos principales

- `indicador_wyckoff_ema_rsi_v2.pine`: indicador overlay para señales visuales y alertas.
- `estrategia_wyckoff_ema_rsi_v2.pine`: estrategia con la lógica v2.2 para Strategy Tester.
- `rsi_panel_wyckoff_helper.pine`: panel RSI opcional separado.

## Cómo interpreta señales

### LONG

Una señal LONG requiere:
- cruce de EMAs válido o retroceso a la EMA rápida,
- precio por encima de EMA200,
- pendiente de EMA200 positiva,
- precio por encima de EMA50,
- pendiente de EMA50 positiva,
- RSI > 50,
- pendiente RSI positiva,
- fase Wyckoff compatible (`Markup` o ruptura de acumulación),
- sincronía W/D/1H alcista si `exigirFractalidadSwing=true`,
- mercado fuera de lateralidad,
- volumen válido si el filtro de volumen está activo,
- absorción/divergencia favorable si se exige estructura extra,
- manos fuertes favorables si se activa el filtro `exigirManosFuertes`.

### SHORT

Una señal SHORT requiere:
- cruce de EMAs válido o retroceso a la EMA rápida,
- precio por debajo de EMA200,
- pendiente de EMA200 negativa,
- precio por debajo de EMA50,
- pendiente de EMA50 negativa,
- RSI < 50,
- pendiente RSI negativa,
- fase Wyckoff compatible (`Markdown` o ruptura de distribución),
- sincronía W/D/1H bajista si `exigirFractalidadSwing=true`,
- mercado fuera de lateralidad,
- volumen válido si el filtro de volumen está activo,
- absorción/divergencia favorable si se exige estructura extra,
- manos fuertes favorables si se activa el filtro `exigirManosFuertes`.

## Alertas JSON

Ejemplo LONG emitido por TradingView:

```json
{"event_type":"signal.long_candidate","signal":"LONG","trend":"ALCISTA","strength":"{{plot(\"FUERZA_LONG\")}}","fractal_sync":"{{plot(\"FRACTAL_SYNC\")}}","fractal_w":"{{plot(\"FRACTAL_W\")}}","fractal_d":"{{plot(\"FRACTAL_D\")}}","fractal_1h":"{{plot(\"FRACTAL_1H\")}}","ema50_filter":"{{plot(\"EMA50_FILTER\")}}","strong_hands":"{{plot(\"MANOS_FUERTES\")}}","symbol":"{{ticker}}","timeframe":"{{interval}}","price":"{{close}}","sl":"{{plot(\"SL_LONG\")}}","tp":"{{plot(\"TP_LONG\")}}","source_module":"tradingview.indicador_wyckoff_ema_rsi_v2","severity":"info","reason":"wyckoff_ema_rsi_fractal_swing_long"}
```

Ejemplo SHORT:

```json
{"event_type":"signal.short_candidate","signal":"SHORT","trend":"BAJISTA","strength":"{{plot(\"FUERZA_SHORT\")}}","fractal_sync":"{{plot(\"FRACTAL_SYNC\")}}","fractal_w":"{{plot(\"FRACTAL_W\")}}","fractal_d":"{{plot(\"FRACTAL_D\")}}","fractal_1h":"{{plot(\"FRACTAL_1H\")}}","ema50_filter":"{{plot(\"EMA50_FILTER\")}}","strong_hands":"{{plot(\"MANOS_FUERTES\")}}","symbol":"{{ticker}}","timeframe":"{{interval}}","price":"{{close}}","sl":"{{plot(\"SL_SHORT\")}}","tp":"{{plot(\"TP_SHORT\")}}","source_module":"tradingview.indicador_wyckoff_ema_rsi_v2","severity":"info","reason":"wyckoff_ema_rsi_fractal_swing_short"}
```

## Uso recomendado con TradingView y BingX

1. Abrir TradingView.
2. Cargar `BTCUSDT.P` de BingX.
3. Cargar `indicador_wyckoff_ema_rsi_v2.pine`.
4. Revisar primero semanal, diario y 1h con el panel `Fractal W/D/1H`.
5. No buscar entrada swing si el panel marca `NO SYNC`.
6. En 1h, buscar solo LONG/SHORT cuando aparezca señal confirmada.
7. Cargar `rsi_panel_wyckoff_helper.pine` si se quiere panel RSI separado.
8. Crear alertas LONG/SHORT desde TradingView.
9. Operar primero en demo manual o demo conectada.
10. Usar `estrategia_wyckoff_ema_rsi_v2.pine` en Strategy Tester solo para validación separada, recordando que aún no incluye la puerta fractal v2.5.0.

## Validación documental

```bash
python3 scripts/validar_documentacion_viva.py
```

## Validación funcional pendiente

Pine Script debe validarse dentro de TradingView:
- compilación del indicador,
- revisión de `request.security()` en semanal, diario y 1h,
- revisión del panel fractal,
- revisión de EMA50 y Data Window,
- revisión de marcadores `SYNC+`, `SYNC-`, `MF+`, `MF-`,
- revisión de alertas JSON,
- validación visual en `BTCUSDT.P` BingX semanal/diario/1h,
- comparación posterior con otros activos líquidos.

No se debe publicar como rentable sin evidencias de backtest, demo o forward test.

## Enfoque

No se promete rentabilidad. Las señales deben ser explicables, trazables y validadas con evidencias.
