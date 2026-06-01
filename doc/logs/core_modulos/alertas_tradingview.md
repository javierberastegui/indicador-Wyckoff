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
