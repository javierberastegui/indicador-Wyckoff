# Estado actual

## Proyecto
`indicador-Wyckoff`

## Estado operativo
Documentación viva inicial aplicada al repositorio.

## Arquitectura viva inicial
- indicador Wyckoff
- reglas EMAs
- motor de señales long/short
- eventos estructurados
- capa central de alertas
- validación/backtesting o demo
- posible integración TradingView/Pine Script

## Decisiones activas
- No empezar desde cero si aparece código válido.
- No cambiar rutas base sin necesidad.
- No prometer rentabilidad.
- Eventos estructurados primero; notificaciones después mediante capa central.
- Logs por dominio como bitácora principal.
- `doc/logs/historico.md` no es bitácora principal.

## Pendiente inmediato
Crear o revisar la primera versión funcional del indicador respetando la separación de dominios.
