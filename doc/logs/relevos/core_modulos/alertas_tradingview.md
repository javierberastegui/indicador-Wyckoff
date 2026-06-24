# Relevo — alertas y TradingView

## Estado actual
Regla documental definida: eventos estructurados primero, notificaciones después.

La v2.6.0 mantiene alertas JSON desde TradingView para señales candidatas LONG/SHORT. No se añaden alertas independientes para macro, lupa, pistola, EMA50 ni manos fuertes; esos datos viajan como payload dentro de `signal.long_candidate` y `signal.short_candidate`.

## Decisiones activas
- Las alertas nacen de eventos estructurados.
- La capa central decide qué se notifica.
- Evitar duplicación entre TradingView, webhook y Telegram futuro.
- Durante demo usar un único canal operativo para evitar doble ejecución.
- No ejecutar señales overlay v2.6.0 como si fueran resultados de estrategia v2.2 sin documentar la diferencia.

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

## Campos JSON añadidos en v2.6.0
- `daytrading_sync`
- `macro_1d`
- `lupa_1h`
- `pistola_5m`
- `entry_tf_ok`
- `ema50_filter`
- `strong_hands`
- `reason`

## Siguiente paso
Crear alerta real en TradingView, capturar payload, comprobar que los campos añadidos llegan correctamente y registrar evidencia antes de usar ejecución conectada a BingX.
