# Relevo — alertas y TradingView

## Estado actual
Regla documental definida: eventos estructurados primero, notificaciones después.

La v2.0 añade alertas JSON desde TradingView para señales candidatas LONG/SHORT.

## Decisiones activas
- Las alertas nacen de eventos estructurados.
- La capa central decide qué se notifica.
- Evitar duplicación entre TradingView, webhook y Telegram futuro.
- Durante demo usar un único canal operativo para evitar doble ejecución.

## Eventos vigentes
- `signal.long_candidate`
- `signal.short_candidate`

## Campos JSON mínimos
- `event_type`
- `signal`
- `symbol`
- `timeframe`
- `price`
- `sl`
- `tp`
- `source_module`
- `severity`

## Siguiente paso
Crear alerta real en TradingView, capturar payload y registrar evidencia antes de usar ejecución conectada a BingX.
