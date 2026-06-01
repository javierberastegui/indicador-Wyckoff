# AGENTS.md

# 📈 Indicador Wyckoff

## Propósito del proyecto
Repositorio para construir y mantener un indicador de trading basado en Metodología Wyckoff, cruces de EMAs, RSI y reglas de señalización operativa.

El sistema debe evolucionar como proyecto mantenible, documentado y validable. No se aceptan señales sueltas sin trazabilidad.

Prioridades:
- señales explicables y revisables
- documentación viva por dominio
- modularidad real
- validación antes de cerrar fases
- eventos estructurados antes que avisos sueltos
- capa central de reglas para decidir notificaciones
- compatibilidad con TradingView si se implementa Pine Script
- control estricto de cambios para no romper señales válidas

## Arquitectura base
La arquitectura exacta se respeta según exista en el repo.

Mientras no haya decisión explícita distinta, el proyecto se organiza alrededor de:
- indicador principal
- reglas Wyckoff
- reglas EMAs
- reglas RSI
- motor de señales
- capa de eventos estructurados
- capa central de alertas/notificaciones
- documentación operativa viva
- pruebas o validaciones proporcionales

Si se añade backend, frontend, panel, bot, API, base de datos o integración externa, debe documentarse primero en `doc/estado_actual.md` y en logs/relevos del dominio correspondiente.

## Restricciones obligatorias
- no empezar desde cero si ya existe estructura válida
- no cambiar arquitectura base sin instrucción expresa
- no cambiar rutas base existentes sin necesidad real
- no simplificar artificialmente el proyecto
- no cambiar nomenclatura base ya asentada sin motivo fuerte
- no entregar pseudocódigo
- no dar teoría cuando se pidan cambios aplicables
- entregar siempre archivos completos cuando se propongan cambios de código o documentación
- documentar al final en logs por dominio
- no usar `doc/logs/historico.md` como bitácora principal
- no inventar resultados de backtesting, rentabilidad, winrate o drawdown
- no presentar una señal como rentable si no está validada con evidencias
- no acoplar alertas directamente a cada regla si existe o debe existir una capa central

## Guardarraíles de trading
Este repo puede ayudar a crear señales, indicadores y validaciones, pero no promete rentabilidad.

Reglas:
- toda señal debe explicarse por condiciones verificables
- distinguir señal candidata, señal confirmada y alerta emitida
- toda alerta debe rastrearse hasta un evento estructurado
- los cambios de lógica deben documentar impacto esperado y riesgo de falsas señales
- los resultados de demo, backtest o forward test son evidencia, no garantía
- no mezclar reglas discrecionales con reglas automáticas sin documentarlo

## Eventos estructurados y alertas
Todo módulo relevante debe poder emitir eventos estructurados.

Las notificaciones no se deciden dentro de cada módulo aislado. La decisión de avisar, resumir, ignorar o agrupar eventos pertenece a una capa central de reglas.

Principios:
- primero se genera evento estructurado
- después una capa central decide si hay notificación
- las alertas deben ser trazables, filtrables y configurables
- no duplicar alertas entre indicador, estrategia, webhook o bot
- los eventos deben poder alimentar logs, paneles, TradingView alerts, Telegram u otros canales futuros

Eventos mínimos recomendados:
- `wyckoff.phase_detected`
- `wyckoff.spring_candidate`
- `wyckoff.upthrust_candidate`
- `rsi.divergence_detected`
- `rsi.absorption_candidate`
- `ema.cross_detected`
- `signal.long_candidate`
- `signal.short_candidate`
- `signal.invalidated`
- `alert.rule_matched`
- `validation.backtest_recorded`
- `system.config_changed`

Cada evento debe incluir: `event_type`, `timestamp`, `symbol`, `timeframe`, `source_module`, `severity`, `payload`, `reason`.

## Modularidad y anti-monolitos
Evitar archivos monstruo.

Preferencia:
- módulos pequeños
- reglas separadas por responsabilidad
- constantes separadas de lógica
- helpers puros separados de señales
- eventos separados de alertas
- documentación por dominio

No se permite concentrar reglas Wyckoff, EMAs, RSI, señales, alertas, backtest y documentación en un único archivo si el proyecto crece fuera de Pine Script.

En Pine Script se acepta un archivo completo por artefacto por limitación de TradingView, siempre que la separación lógica quede clara por bloques internos y documentación viva.

Umbrales:
- 300-400 líneas: revisar división
- más de 600 líneas: división obligatoria salvo Pine Script justificado
- más de 3 responsabilidades claras: dividir o documentar separación interna
- señal + alerta + validación en mismo bloque: separar o justificar por limitación Pine

Orden recomendado de extracción:
1. constantes y configuración
2. helpers puros
3. detectores Wyckoff
4. reglas EMAs
5. reglas RSI
6. motor de señales
7. eventos estructurados
8. reglas centrales de alerta
9. validación/backtesting
10. visualización/panel si aplica

## Reglas de diseño para Wyckoff + EMA + RSI
- La detección Wyckoff debe nombrarse como simplificada si no implementa lectura completa de eventos Wyckoff.
- Los modos EMA soportados oficialmente son `9/21`, `10/20` y `5/8/13`.
- La EMA200 es el filtro estructural base de tendencia.
- El RSI se usa como confirmador estructural, no solo como sobrecompra/sobreventa.
- LONG requiere RSI > 50 y pendiente positiva salvo ajuste documentado.
- SHORT requiere RSI < 50 y pendiente negativa salvo ajuste documentado.
- La divergencia RSI simple debe documentarse como heurística, no como prueba de giro.
- La absorción Wyckoff por RSI debe documentarse como aproximación operativa.
- El filtro lateral por rango/ATR es obligatorio para reducir señales en rango.
- El volumen puede ser opcional por diferencias de calidad de datos en cripto.

## Presets vigentes
- `15m`: EMAs 9/21, RSI 14, perfil intermedio reactivo.
- `1h RSI14`: EMAs 10/20, RSI 14, preset inicial recomendado.
- `1h RSI21`: EMAs 10/20, RSI 21, preset más filtrado.
- `Manual`: permite 9/21, 10/20 o 5/8/13.

## Estilo de alertas TradingView
- Las alertas deben exponerse como JSON apto para webhook.
- Campos mínimos: `event_type`, `signal`, `symbol`, `timeframe`, `price`, `sl`, `tp`, `source_module`, `severity`.
- La alerta debe representar `alert.rule_matched`, no un aviso suelto acoplado a un detector.

## Política de pruebas manuales
- Probar compilación en TradingView sin errores.
- Probar presets `15m`, `1h RSI14` y `1h RSI21`.
- Verificar señales en `BTCUSDT.P` de BingX en 15m y 1h.
- Confirmar que no hay exceso de señales en lateral prolongado.
- Confirmar que LONG/SHORT respetan EMA200 y RSI.
- Confirmar Strategy Tester y exportación de operaciones si TradingView lo permite.
- No afirmar rentabilidad sin rango, símbolo, timeframe y evidencia.

## Dominios
Separación obligatoria salvo orden contraria:
- `core_indicador`
- `wyckoff`
- `emas`
- `rsi`
- `senales`
- `eventos`
- `alertas`
- `validacion`
- `tradingview`
- `documentacion`

## Jerarquía operativa
1. `AGENTS.md`
2. `doc/instrucciones/README.md`
3. instrucciones específicas aplicables
4. `doc/estado_actual.md`
5. `doc/protocolo_relevo.md`
6. relevo del dominio afectado
7. logs del dominio afectado
8. incidencias abiertas
9. prompt activo si existe

## Lectura obligatoria antes de tocar nada
Leer: `AGENTS.md`, `doc/instrucciones/README.md`, `doc/instrucciones/mapa_dominios.md`, `doc/estado_actual.md`, `doc/protocolo_relevo.md`, relevo del dominio, log del dominio, incidencias y prompt activo si existe.

No basta con leer `doc/logs/historico.md`.

## Forma de trabajo
1. entender estado real
2. identificar dominio
3. revisar log y relevo
4. tocar solo lo necesario
5. mantener naming y estructura
6. aplicar cambios completos
7. validar proporcionalmente
8. documentar resultado
9. actualizar relevo si queda trabajo abierto
10. dejar siguiente paso claro

## Validación
- Pine Script: revisar sintaxis y compatibilidad TradingView
- Python/scripts: ejecutar tests o script afectado
- documentación viva: ejecutar `python3 scripts/validar_documentacion_viva.py`
- señales: registrar caso de ejemplo
- alertas: comprobar evento estructurado origen
- backtest: indicar fuente, rango, símbolo y timeframe

## Documentación viva
Al cerrar etapa, actualizar si aplica: `doc/estado_actual.md`, log del dominio, relevo, incidencias, deuda técnica, bloqueos y prompt activo.

## Entrega esperada
Indicar archivos nuevos/modificados, instrucciones aplicadas, validaciones, decisiones, pendientes, relevo, siguiente paso y mensaje de commit.

## Regla final
Prioridad: cambios coherentes, trazables, mantenibles y acumulables sin romper lo ya válido.
