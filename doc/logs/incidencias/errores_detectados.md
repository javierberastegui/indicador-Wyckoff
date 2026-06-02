# Errores detectados

No hay errores abiertos sin corrección documentados; las incidencias corregidas quedan registradas abajo con validación pendiente cuando aplique.

## Plantilla
```md
### YYYY-MM-DD — error
- Dominio:
- Síntoma:
- Causa:
- Evidencia:
- Corrección:
- Estado:
```

### 2026-06-02 — TP parcial repetido en estrategia
- Dominio: `tradingview`, `validacion`.
- Síntoma: la orden de TP parcial podía seguir emitiéndose después de marcarse el parcial, con riesgo de que el runner se cerrase repetidamente en el precio del TP parcial.
- Causa: la gestión anterior emitía `strategy.exit` de TP parcial en cada barra mientras la posición seguía abierta.
- Evidencia: revisión de `estrategia_wyckoff_ema_rsi_v2.pine` antes de v2.2.
- Corrección: el TP parcial se emite solo mientras `parcialLongHecho`/`parcialShortHecho` es falso; después se deja de emitir el TP parcial y el runner queda con breakeven + trailing manual ATR ratchet.
- Estado: corregido en código; pendiente validar compilación y ejecución real en TradingView.
