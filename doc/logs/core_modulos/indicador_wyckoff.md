# Log — indicador Wyckoff

## Entrada inicial
- Motivo: alta de documentación viva para `indicador-Wyckoff`.
- Decisión: separar Wyckoff, EMAs, señales, eventos, alertas y validación.
- Validación: `python3 scripts/validar_documentacion_viva.py` ejecutado localmente antes del push.
- Resultado: estructura documental base lista.

### 2026-06-01 — v2.0 Wyckoff + EMA + RSI
- Dominio: `core_indicador`, `wyckoff`, `emas`, `rsi`, `senales`.
- Cambio: añadida primera versión funcional del indicador y estrategia Pine Script con presets `15m`, `1h RSI14`, `1h RSI21` y `Manual`.
- Cambio: incorporado filtro EMA200, cruces 9/21, 10/20 y modo 5/8/13, RSI estructural, divergencia simple, absorción aproximada, lateralidad rango/ATR y volumen opcional.
- Validación: revisión estructural del código y actualización de documentación viva; compilación real en TradingView queda pendiente porque solo puede validarse en la plataforma.
- Evidencia: archivos `indicador_wyckoff_ema_rsi_v2.pine`, `estrategia_wyckoff_ema_rsi_v2.pine`, `rsi_panel_wyckoff_helper.pine` añadidos en rama `feat/wyckoff-ema-rsi-v2`.
- Pendiente: probar `BTCUSDT.P` BingX en 1h preset `1h RSI14`; después comparar con `15m`.

### 2026-06-02 — v2.2 gestion parcial + runner ATR
- Dominio: `core_indicador`, `senales`, `validacion`.
- Cambio: mantenida la lógica de entrada actual y Pine Script v5; ajustada solo la gestión de salidas de `estrategia_wyckoff_ema_rsi_v2.pine`.
- Cambio: añadidos `trailDebil=1.2` y `trailFuerte=2.5` en `Riesgo dinamico`; el TP parcial usa `cierreParcialPct` 80% por defecto y deja runner con el resto.
- Cambio: SL inicial cubre toda la posición; tras tocar TP parcial el runner pasa a breakeven y luego usa trailing manual ATR tipo chandelier con ratchet, sin retroceder.
- Cambio: el TP parcial ya no se emite si `parcialLongHecho`/`parcialShortHecho` es verdadero, evitando cierres repetidos del runner en el precio del TP.
- Validación: `python3 scripts/validar_documentacion_viva.py` ejecutado correctamente; compilación real de Pine queda pendiente en TradingView.
- Evidencia: cambios en `estrategia_wyckoff_ema_rsi_v2.pine`, `README.md`, `CHANGELOG.md` y documentación viva.
- Pendiente: compilar en TradingView y validar en Strategy Tester sobre `BTCUSDT.P` BingX 1h con preset `1h RSI14`.

## Plantilla
```md
### YYYY-MM-DD — título
- Dominio:
- Cambio:
- Validación:
- Evidencia:
- Pendiente:
```
