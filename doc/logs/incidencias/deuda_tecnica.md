# Deuda técnica

## Pendiente inicial
Cuando exista código funcional, añadir validaciones específicas para señales, alertas y compatibilidad TradingView/Pine Script.

### 2026-06-02 — validación visual Pine v2.3 pendiente en TradingView
- Dominio: `tradingview`, `core_indicador`, `rsi`.
- Deuda: no existe validador local completo para confirmar compilación Pine Script v5 ni legibilidad visual real del overlay/helper RSI.
- Impacto: la mejora v2.3 queda revisada documentalmente y por diff, pero debe compilarse en TradingView y validarse con capturas en `BTCUSDT.P` BingX 1h/15m antes de cerrar evidencia operativa.
- Siguiente acción: compilar `indicador_wyckoff_ema_rsi_v2.pine` y `rsi_panel_wyckoff_helper.pine` en TradingView, registrar errores exactos si aparecen y guardar capturas de la jerarquía visual.

### 2026-06-02 — seguimiento limpieza visual v2.3.1 pendiente en TradingView
- Dominio: `tradingview`, `core_indicador`.
- Deuda: los ajustes anti-persiana de S/R, etiquetas de fase y texto opcional DIV/ABS no pueden confirmarse solo con validación local.
- Impacto: queda pendiente revisar compilación Pine y capturas reales para cerrar la deuda visual detectada en TradingView.
- Siguiente acción: validar `indicador_wyckoff_ema_rsi_v2.pine` en TradingView con S/R apagado y encendido, verificando que no se acumulen líneas cercanas ni textos montados.
