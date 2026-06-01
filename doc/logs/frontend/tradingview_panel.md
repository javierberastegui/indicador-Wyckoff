# Log — TradingView / visual

## Estado inicial
No hay Pine Script confirmado en esta base documental.

## Criterios futuros
- inputs claros
- plots explicables
- labels no invasivos
- alerts nacidas de eventos estructurados
- no mezclar toda la lógica visual, señal y validación sin separación documentada

### 2026-06-01 — Pine Script v2.0
- Dominio: `tradingview`.
- Cambio: añadidos indicador overlay, estrategia de backtesting y helper RSI.
- Inputs: presets `15m`, `1h RSI14`, `1h RSI21`, `Manual`, modo EMA, RSI, lateralidad, volumen, divergencias y absorciones.
- Plots: EMA rápida, EMA lenta, EMA media opcional, EMA200, zonas laterales Wyckoff, señales LONG/SHORT, divergencias y absorciones.
- Alerts: JSON con `event_type`, `signal`, `symbol`, `timeframe`, `price`, `sl`, `tp`, `source_module`, `severity`.
- Validación: pendiente de compilación en TradingView.
- Pendiente: probar primero `BTCUSDT.P` BingX 1h con preset `1h RSI14`; después `15m`.
