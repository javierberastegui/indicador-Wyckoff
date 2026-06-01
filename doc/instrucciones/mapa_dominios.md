# Mapa de dominios

## core_indicador
Lógica principal del indicador.
Log: `doc/logs/core_modulos/indicador_wyckoff.md`
Relevo: `doc/logs/relevos/core_modulos/indicador_wyckoff.md`

## wyckoff
Fases, spring, upthrust, acumulación, distribución y eventos Wyckoff.
Usa el log de `core_indicador` salvo que crezca y requiera archivo propio.

## emas
Cruces y filtros de medias móviles.
Usa el log de `core_indicador` salvo que crezca.

## rsi
Confirmación estructural RSI, nivel 50, pendiente, divergencias simples y absorción aproximada.
Usa el log de `core_indicador` salvo que crezca y requiera archivo propio.

## senales
Composición de condiciones long/short.
Usa el log de `core_indicador`.

## eventos
Contrato de eventos estructurados.
Log: `doc/logs/core_modulos/alertas_tradingview.md`
Relevo: `doc/logs/relevos/core_modulos/alertas_tradingview.md`

## alertas
Reglas centrales de notificación.
Log: `doc/logs/core_modulos/alertas_tradingview.md`
Relevo: `doc/logs/relevos/core_modulos/alertas_tradingview.md`

## tradingview
Pine Script, inputs, plots, labels y alerts.
Log: `doc/logs/frontend/tradingview_panel.md`
Relevo: `doc/logs/relevos/frontend/tradingview_panel.md`

## validacion
Backtest, demo, forward test y evidencias.
Usa `core_indicador` salvo que se consolide como dominio propio.

## documentacion
Documentación viva, instrucciones y estructura.
Log: `doc/logs/core_modulos/documentacion.md`
Relevo: `doc/logs/relevos/compartidos/documentacion.md`
