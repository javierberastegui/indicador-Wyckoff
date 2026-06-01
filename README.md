# indicador-Wyckoff

Repositorio para desarrollar un indicador basado en Metodología Wyckoff, cruces de EMAs y generación de señales long/short revisables.

## Estado actual
Documentación viva inicial aplicada.

Antes de tocar código, leer:
1. `AGENTS.md`
2. `doc/instrucciones/README.md`
3. `doc/estado_actual.md`
4. `doc/protocolo_relevo.md`
5. logs y relevos del dominio afectado

## Regla clave
Los módulos relevantes deben emitir eventos estructurados. Las notificaciones se deciden en una capa central de reglas, evitando avisos sueltos acoplados módulo a módulo.

## Validación documental
```bash
python3 scripts/validar_documentacion_viva.py
```

## Enfoque
No se promete rentabilidad. Las señales deben ser explicables, trazables y validadas con evidencias.
