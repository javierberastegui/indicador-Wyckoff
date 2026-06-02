# Deuda técnica

## Pendiente inicial
Cuando exista código funcional, añadir validaciones específicas para señales, alertas y compatibilidad TradingView/Pine Script.

### 2026-06-02 — validación visual Pine v2.3 pendiente en TradingView
- Dominio: `tradingview`, `core_indicador`, `rsi`.
- Deuda: no existe validador local completo para confirmar compilación Pine Script v5 ni legibilidad visual real del overlay/helper RSI.
- Impacto: la mejora v2.3 queda revisada documentalmente y por diff, pero debe compilarse en TradingView y validarse con capturas en `BTCUSDT.P` BingX 1h/15m antes de cerrar evidencia operativa.
- Siguiente acción: compilar `indicador_wyckoff_ema_rsi_v2.pine` y `rsi_panel_wyckoff_helper.pine` en TradingView, registrar errores exactos si aparecen y guardar capturas de la jerarquía visual.
