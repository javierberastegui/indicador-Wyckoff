# indicador-Wyckoff

Repositorio para desarrollar un indicador basado en Metodología Wyckoff simplificada, cruces de EMAs, RSI, lectura multi-timeframe y generación de señales long/short revisables.

## Estado actual

Versión funcional v2.6.0 en desarrollo: Wyckoff simplificado + EMAs + RSI + alertas JSON + estrategia de backtesting separada, con **modo automático DayTrading** para trabajar con este flujo operativo:

- `1D`: macro / contexto principal.
- `1H`: análisis con lupa / preparación del setup.
- `5m`: pistola de entrada / disparo final.

La estrategia separada sigue sin adaptarse a la puerta DayTrading v2.6.0. No debe usarse para afirmar rendimiento de esta lógica hasta que se actualice y se valide en TradingView.

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

La mejora v2.6.0 no crea alertas sueltas nuevas. Mantiene las alertas LONG/SHORT centralizadas al final del indicador, pero cambia el payload de fractalidad swing W/D/1H a puerta DayTrading 1D/1H/5m.

## Indicador Wyckoff + EMA + RSI v2.6.0 DayTrading

La versión actual implementa una lectura operativa simplificada de Wyckoff combinada con:

- selección automática de EMAs y RSI según timeframe del gráfico,
- filtro de tendencia con EMA200,
- EMA50 como filtro fuerte obligatorio para que la señal tenga estructura operativa,
- puerta multi-timeframe **1D + 1H + 5m** mediante `request.security()`,
- bloqueo opcional de señales si el gráfico no está en 5m,
- cruces EMA y entradas por retroceso a la EMA rápida,
- confirmación RSI por nivel 50 y pendiente,
- divergencia RSI simple como aviso de tendencia débil,
- clasificación de tendencia en **FUERTE** o **DÉBIL**,
- riesgo dinámico interno: tendencia débil → **1×2**, tendencia fuerte → **2×4**,
- detección aproximada de absorción y lectura de **manos fuertes** por esfuerzo/resultado,
- filtro de lateralidad por rango/ATR,
- confirmación opcional por volumen,
- capa visual con señales, cruces EMA, retrocesos, sincronía DayTrading, manos fuertes, divergencias/absorciones y contexto Wyckoff,
- alertas JSON preparadas para TradingView/webhook.

La detección Wyckoff es heurística. No pretende identificar toda la metodología clásica; aproxima fases útiles para ordenar señales y revisar contexto.

## Modo automático DayTrading

El indicador mantiene selección automática por timeframe:

| Timeframe del gráfico | EMAs activas | RSI activo | Lateralidad interna |
|---|---:|---:|---:|
| `5m` o inferior | 5/8/13 | 14 | lookback 14, ratio rango/ATR 3.8 |
| `>5m` y `<=15m` | 9/21 | 14 | lookback 18, ratio rango/ATR 4.5 |
| `>=60m` e intermedios | 10/20 | 14 | lookback 24, ratio rango/ATR 5.5 |

La capa DayTrading añade una segunda lectura fija:

- diario (`D`) como macro,
- 1 hora (`60`) como lupa,
- 5 minutos (`5`) como pistola.

Con `exigirFractalidadDayTrading=true`, activado por defecto, no hay LONG si macro 1D, lupa 1H y pistola 5m no están alineadas a favor. No hay SHORT si no están alineadas a la baja.

Con `exigirGraficoEntrada5m=true`, activado por defecto, el indicador bloquea LONG/SHORT si se carga en un gráfico distinto de 5m. El panel mostrará `CAMBIAR A 5m`.

## Lectura del panel

El panel muestra:

- `Plan`: `BUSCAR LONG 5m`, `BUSCAR SHORT 5m`, `ESPERAR` o `CAMBIAR A 5m`.
- `Comentario`: lectura accionable del estado actual.
- `Macro 1D`: sesgo diario.
- `Lupa 1H`: sesgo de la hora.
- `Pistola 5m`: estado de entrada de 5 minutos.
- `Grafico`: confirma si el gráfico está en 5m.
- `EMA50`, `RSI` y `Wyckoff`: estado local del gráfico.

Interpretación práctica:

- `BUSCAR LONG 5m`: 1D + 1H + 5m favorecen largo; esperar LONG confirmado, no perseguir velas.
- `BUSCAR SHORT 5m`: 1D + 1H + 5m favorecen corto; esperar SHORT confirmado.
- `ESPERAR`: no hay alineación limpia.
- `CAMBIAR A 5m`: el indicador está cargado en otro timeframe y no emitirá señales si el filtro está activo.

## EMA50 como señal fuerte

La EMA200 conserva el papel de filtro estructural base. La EMA50 pasa a ser filtro fuerte operativo.

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

La EMA50 aparece en el panel y en Data Window como `EMA50_FILTER`: `1` alcista, `-1` bajista, `0` neutral.

## Data Window

La v2.6.0 expone:

- `DAYTRADING_SYNC`: `1` sincronía long, `-1` sincronía short, `0` sin sincronía.
- `MACRO_1D`: sesgo del diario.
- `LUPA_1H`: sesgo de 1h.
- `PISTOLA_5M`: dirección estricta de 5m.
- `ENTRY_TF_OK`: `1` si el gráfico puede emitir señales; `0` si debe cambiarse a 5m.
- `EMA50_FILTER`: filtro EMA50 local.
- `MANOS_FUERTES`: lectura aproximada de absorción/manos fuertes.

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

Por defecto `exigirManosFuertes=false` para no bloquear todas las continuaciones. Si se activa, la señal LONG/SHORT exige también manos fuertes favorables.

## Configuración visible mínima

Quedan visibles controles operativos:

- **Filtros opcionales**: confirmación por volumen, media de volumen, exigencia de absorción/divergencia favorable y exigencia de manos fuertes.
- **Fractalidad day trading**: exigir sincronía 1D/1H/5m, exigir gráfico 5m para señales, mostrar etiquetas `DT+`/`DT-` y mostrar manos fuertes.
- **Visualización**: divergencias, absorciones, cinta de tendencia, panel de estado, cruces EMA, zonas Wyckoff, retrocesos, texto DIV/ABS en overlay y nombre de zona Wyckoff al cambiar.
- **Estilo EMAs**: visibilidad, color, grosor y transparencia de EMAs.
- **Soporte/resistencia**: interruptor único, desactivado por defecto; pivots, límite de líneas y filtros anti-duplicado quedan internos.

## Tendencia, fuerza y gestión de riesgo

La tendencia **FUERTE** requiere:

- dirección clara respecto a EMA200,
- EMA50 alineada a favor,
- EMAs rápida/lenta separadas por ATR,
- ausencia de divergencia contraria reciente,
- puerta DayTrading 1D/1H/5m sincronizada si el filtro está activo,
- gráfico 5m si `exigirGraficoEntrada5m=true`.

La tendencia **DÉBIL** conserva contexto direccional, pero falla alguno de los elementos de fuerza. La divergencia contraria no bloquea por sí sola; rebaja la lectura a débil.

| Fuerza | SL (xATR) | TP (xATR) | Ratio |
|---|---:|---:|---:|
| DÉBIL | 1.0 | 2.0 | 1×2 |
| FUERTE | 2.0 | 4.0 | 2×4 |

La estrategia separada mantiene la gestión previa: entrada completa, SL inicial para toda la posición, TP parcial configurable y runner posterior con breakeven + trailing manual ATR tipo chandelier con ratchet. La estrategia todavía no incorpora la puerta DayTrading v2.6.0.

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

- gráfico 5m si `exigirGraficoEntrada5m=true`,
- cruce de EMAs válido o retroceso a la EMA rápida,
- precio por encima de EMA200,
- pendiente de EMA200 positiva,
- precio por encima de EMA50,
- pendiente de EMA50 positiva,
- RSI > 50,
- pendiente RSI positiva,
- fase Wyckoff compatible (`Markup` o ruptura de acumulación),
- sincronía DayTrading alcista si `exigirFractalidadDayTrading=true`,
- mercado fuera de lateralidad,
- volumen válido si el filtro de volumen está activo,
- absorción/divergencia favorable si se exige estructura extra,
- manos fuertes favorables si se activa el filtro `exigirManosFuertes`.

### SHORT

Una señal SHORT requiere:

- gráfico 5m si `exigirGraficoEntrada5m=true`,
- cruce de EMAs válido o retroceso a la EMA rápida,
- precio por debajo de EMA200,
- pendiente de EMA200 negativa,
- precio por debajo de EMA50,
- pendiente EMA50 negativa,
- RSI < 50,
- pendiente RSI negativa,
- fase Wyckoff compatible (`Markdown` o ruptura de distribución),
- sincronía DayTrading bajista si `exigirFractalidadDayTrading=true`,
- mercado fuera de lateralidad,
- volumen válido si el filtro de volumen está activo,
- absorción/divergencia favorable si se exige estructura extra,
- manos fuertes favorables si se activa el filtro `exigirManosFuertes`.

## Alertas JSON

Ejemplo LONG emitido por TradingView:

```json
{"event_type":"signal.long_candidate","signal":"LONG","trend":"ALCISTA","strength":"{{plot(\"FUERZA_LONG\")}}","daytrading_sync":"{{plot(\"DAYTRADING_SYNC\")}}","macro_1d":"{{plot(\"MACRO_1D\")}}","lupa_1h":"{{plot(\"LUPA_1H\")}}","pistola_5m":"{{plot(\"PISTOLA_5M\")}}","entry_tf_ok":"{{plot(\"ENTRY_TF_OK\")}}","ema50_filter":"{{plot(\"EMA50_FILTER\")}}","strong_hands":"{{plot(\"MANOS_FUERTES\")}}","symbol":"{{ticker}}","timeframe":"{{interval}}","price":"{{close}}","sl":"{{plot(\"SL_LONG\")}}","tp":"{{plot(\"TP_LONG\")}}","source_module":"tradingview.indicador_wyckoff_ema_rsi_v2","severity":"info","reason":"wyckoff_ema_rsi_daytrading_1d_1h_5m_long"}
```

Ejemplo SHORT:

```json
{"event_type":"signal.short_candidate","signal":"SHORT","trend":"BAJISTA","strength":"{{plot(\"FUERZA_SHORT\")}}","daytrading_sync":"{{plot(\"DAYTRADING_SYNC\")}}","macro_1d":"{{plot(\"MACRO_1D\")}}","lupa_1h":"{{plot(\"LUPA_1H\")}}","pistola_5m":"{{plot(\"PISTOLA_5M\")}}","entry_tf_ok":"{{plot(\"ENTRY_TF_OK\")}}","ema50_filter":"{{plot(\"EMA50_FILTER\")}}","strong_hands":"{{plot(\"MANOS_FUERTES\")}}","symbol":"{{ticker}}","timeframe":"{{interval}}","price":"{{close}}","sl":"{{plot(\"SL_SHORT\")}}","tp":"{{plot(\"TP_SHORT\")}}","source_module":"tradingview.indicador_wyckoff_ema_rsi_v2","severity":"info","reason":"wyckoff_ema_rsi_daytrading_1d_1h_5m_short"}
```

## Uso recomendado con TradingView y BingX

1. Abrir TradingView.
2. Cargar `BTCUSDT.P` de BingX u otro contrato líquido.
3. Cargar `indicador_wyckoff_ema_rsi_v2.pine`.
4. Abrir primero `1D` para ver macro.
5. Revisar `1H` para leer el setup con lupa.
6. Cambiar a `5m` para usar la pistola de entrada.
7. No buscar entrada si el panel marca `ESPERAR` o `CAMBIAR A 5m`.
8. En 5m, buscar solo LONG/SHORT cuando aparezca señal confirmada.
9. Crear alertas LONG/SHORT desde TradingView.
10. Operar primero en demo manual o demo conectada.
11. Usar `estrategia_wyckoff_ema_rsi_v2.pine` en Strategy Tester solo para validación separada, recordando que aún no incluye la puerta DayTrading v2.6.0.

## Validación documental

```bash
python3 scripts/validar_documentacion_viva.py
```

## Validación funcional pendiente

Pine Script debe validarse dentro de TradingView:

- compilación del indicador,
- revisión de `request.security()` en diario, 1h y 5m,
- revisión del panel DayTrading,
- revisión del bloqueo `CAMBIAR A 5m`,
- revisión de EMA50 y Data Window,
- revisión de marcadores `DT+`, `DT-`, `MF+`, `MF-`,
- revisión de alertas JSON,
- validación visual en `BTCUSDT.P` BingX 1D/1H/5m,
- comparación posterior con otros activos líquidos.

No se debe publicar como rentable sin evidencias de backtest, demo o forward test.

## Enfoque

No se promete rentabilidad. Las señales deben ser explicables, trazables y validadas con evidencias.
