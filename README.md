# indicador-Wyckoff

Repositorio para desarrollar un indicador basado en Metodología Wyckoff, cruces de EMAs, RSI y generación de señales long/short revisables.

## Estado actual

Versión funcional v2.0 en desarrollo: Wyckoff simplificado + EMAs + RSI + alertas JSON + estrategia de backtesting.

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

## Indicador Wyckoff + EMA + RSI v2.0

La v2.0 implementa una lectura operativa simplificada de Wyckoff combinada con:
- cruces EMA configurables y entradas por retroceso (pullback) a la EMA rápida,
- filtro de tendencia con EMA200,
- confirmación RSI por nivel 50 y pendiente,
- divergencia RSI simple como **aviso de tendencia débil** (no bloquea entradas),
- clasificación de tendencia en **FUERTE** o **DÉBIL** (cinta de color + panel de estado),
- riesgo dinámico: tendencia débil → **1×2**, tendencia fuerte → **2×4**,
- gestión de trade: al alcanzar el TP se cierra el 80% y el resto pasa a breakeven,
- detección aproximada de absorción,
- filtro de lateralidad por rango/ATR,
- confirmación opcional por volumen,
- alertas JSON preparadas para TradingView/webhook,
- estrategia separada para backtesting.

La detección Wyckoff es heurística. No pretende identificar toda la metodología clásica; aproxima fases útiles para operar y validar señales.

### Tendencia, fuerza y gestión de riesgo

El indicador prioriza que la tendencia se vea **clara**:

- **Cinta de color** entre la EMA rápida y la lenta: verde (alcista) o roja (bajista). Más opaca = tendencia **FUERTE**; más tenue = tendencia **DÉBIL**.
- **Panel de estado** (esquina superior derecha): dirección, fuerza (con su ratio 1×2 / 2×4), fase Wyckoff y RSI.

Una **tendencia FUERTE** requiere: dirección clara respecto a EMA200, EMAs rápida/lenta bien separadas (≥ `sepMinAtr` × ATR) y **sin divergencia contraria reciente**. En caso contrario la tendencia es **DÉBIL**.

La divergencia ya **no impide** abrir LONG/SHORT: solo marca la tendencia como débil y, por tanto, fuerza el riesgo conservador **1×2**.

| Fuerza | SL (xATR) | TP (xATR) | Ratio |
|---|---:|---:|---:|
| DÉBIL | 1.0 | 2.0 | 1×2 |
| FUERTE | 2.0 | 4.0 | 2×4 |

Gestión al alcanzar el TP: se cierra el **80%** de la posición y el **20% restante** continúa con el Stop movido al **precio de entrada (breakeven)** para dejar correr la tendencia sin riesgo. El porcentaje es configurable (`cierreParcialPct`).

### Entradas por retroceso

Además del cruce de EMAs, con `usarRetroceso` activado se generan señales cuando el precio retrocede a la EMA rápida y rebota en la dirección de la tendencia. Así no se pierden tramos largos de tendencia entre cruces.

## Archivos principales

- `indicador_wyckoff_ema_rsi_v2.pine`: indicador overlay para señales visuales y alertas.
- `estrategia_wyckoff_ema_rsi_v2.pine`: estrategia con la misma lógica para Strategy Tester.
- `rsi_panel_wyckoff_helper.pine`: panel RSI opcional separado.

## Presets operativos

### 15m

- EMAs: 9/21.
- RSI: 14.
- Perfil: intradía intermedio, más reactivo.
- Uso recomendado: probar después de validar 1h, porque genera más señales y más ruido.

### 1h RSI14

- EMAs: 10/20.
- RSI: 14.
- Perfil: equilibrio entre frecuencia y limpieza.
- Uso recomendado: preset inicial para validar estructura.

### 1h RSI21

- EMAs: 10/20.
- RSI: 21.
- Perfil: más filtrado.
- Uso recomendado: reducir ruido si 1h RSI14 genera demasiadas señales.

### Manual

Permite elegir modo EMA `9/21`, `10/20` o `5/8/13`, además del RSI manual.

## Cómo interpreta señales

### LONG

Una señal LONG requiere:
- cruce de EMAs válido **o** retroceso a la EMA rápida (si `usarRetroceso` está activo),
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
- cruce de EMAs válido **o** retroceso a la EMA rápida (si `usarRetroceso` está activo),
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
3. Probar primero `estrategia_wyckoff_ema_rsi_v2.pine` en 1h con preset `1h RSI14`.
4. Comparar después con `1h RSI21`.
5. Pasar a 15m solo si 1h ya tiene comportamiento razonable.
6. Cargar `indicador_wyckoff_ema_rsi_v2.pine` para alertas.
7. Crear alertas LONG/SHORT desde TradingView.
8. Operar primero en demo manual o demo conectada.

## Validación documental

```bash
python3 scripts/validar_documentacion_viva.py
```

## Validación funcional pendiente

Pine Script debe validarse dentro de TradingView:
- compilación del indicador,
- compilación de la estrategia,
- Strategy Tester en BTCUSDT.P BingX 1h,
- comparación con BTCUSDT.P BingX 15m,
- revisión de señales en lateral,
- revisión de alertas JSON.

No se debe publicar como rentable sin evidencias de backtest, demo o forward test.

## Enfoque

No se promete rentabilidad. Las señales deben ser explicables, trazables y validadas con evidencias.
