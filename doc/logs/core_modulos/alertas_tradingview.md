# Log — alertas y eventos

## Entrada inicial
- Motivo: definir regla de eventos estructurados antes de notificaciones.
- Decisión: las alertas deben salir de una capa central de reglas.
- Impacto: evita avisos sueltos acoplados módulo a módulo.

### 2026-06-01 — alertas JSON v2.0
- Evento: `signal.long_candidate` y `signal.short_candidate`.
- Regla: la capa central en Pine queda representada por `alertcondition()` después de componer condiciones Wyckoff, EMAs, RSI, lateralidad y volumen opcional.
- Canal: TradingView alerts / webhook JSON.
- Validación: pendiente de crear alerta real en TradingView y comprobar payload recibido.
- Riesgo: no duplicar ejecución entre indicador, estrategia, BingX manual y futuros bots; usar un único canal operativo durante demo.

## Plantilla
```md
### YYYY-MM-DD — título
- Evento:
- Regla:
- Canal:
- Validación:
- Riesgo:
```

### 2026-06-22 — alertas JSON v2.5.0 con fractalidad
- Evento: `signal.long_candidate` y `signal.short_candidate`.
- Regla: la capa central sigue representada por `alertcondition()` al final de `indicador_wyckoff_ema_rsi_v2.pine`; no se añaden alertas sueltas para fractalidad, EMA50 ni manos fuertes.
- Canal: TradingView alerts / webhook JSON.
- Cambio: el payload añade `fractal_sync`, `fractal_w`, `fractal_d`, `fractal_1h`, `ema50_filter`, `strong_hands` y `reason`.
- Validación: pendiente crear alerta real en TradingView y capturar payload recibido.
- Riesgo: la estrategia separada aún no replica la puerta fractal v2.5.0; no mezclar resultados del Strategy Tester v2.2 con señales overlay v2.5.0 sin documentarlo.
