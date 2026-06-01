# Eventos estructurados

## Regla base
Todo módulo relevante debe poder emitir eventos estructurados. Las notificaciones se deciden por una capa central de reglas.

## Campos mínimos
- `event_type`
- `timestamp`
- `symbol`
- `timeframe`
- `source_module`
- `severity`
- `payload`
- `reason`

## Severidad
- `debug`
- `info`
- `warning`
- `critical`

## Ejemplos
- `wyckoff.phase_detected`
- `wyckoff.spring_candidate`
- `ema.cross_detected`
- `signal.long_candidate`
- `signal.short_candidate`
- `signal.invalidated`
- `alert.rule_matched`
- `validation.backtest_recorded`

## Prohibido
- alertas directas dispersas
- duplicar avisos entre módulos
- payloads incompatibles
- afirmar rentabilidad desde un evento
