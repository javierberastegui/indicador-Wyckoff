#!/usr/bin/env python3
"""Valida la estructura mínima de documentación viva del repo indicador-Wyckoff."""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "AGENTS.md",
    "README.md",
    "doc/estado_actual.md",
    "doc/protocolo_relevo.md",
    "doc/instrucciones/README.md",
    "doc/instrucciones/mapa_dominios.md",
    "doc/instrucciones/leyes_documentacion_operativa.md",
    "doc/instrucciones/micro-refactor.md",
    "doc/instrucciones/eventos_estructurados.md",
    "doc/logs/README.md",
    "doc/logs/core_modulos/indicador_wyckoff.md",
    "doc/logs/core_modulos/alertas_tradingview.md",
    "doc/logs/core_modulos/documentacion.md",
    "doc/logs/backend_modulos/README.md",
    "doc/logs/frontend/tradingview_panel.md",
    "doc/logs/incidencias/errores_detectados.md",
    "doc/logs/incidencias/deuda_tecnica.md",
    "doc/logs/incidencias/bloqueos_actuales.md",
    "doc/logs/relevos/INDEX.md",
    "doc/logs/relevos/core_modulos/indicador_wyckoff.md",
    "doc/logs/relevos/core_modulos/alertas_tradingview.md",
    "doc/logs/relevos/frontend/tradingview_panel.md",
    "doc/logs/relevos/compartidos/documentacion.md",
    "doc/logs/relevos/siguiente_prompt_codex.md",
    "doc/logs/plantillas/log_core_modulo_base.md",
    "doc/logs/plantillas/log_frontend_superficie_base.md",
    "doc/logs/plantillas/relevo_modulo_base.md",
    "doc/prompts/README.md",
    "doc/prompts/prompt_activo.md",
]

REQUIRED_SNIPPETS = {
    "AGENTS.md": [
        "eventos estructurados",
        "capa central de reglas",
        "no empezar desde cero",
        "doc/logs/historico.md",
    ],
    "doc/instrucciones/eventos_estructurados.md": [
        "event_type",
        "source_module",
        "severity",
    ],
    "doc/instrucciones/mapa_dominios.md": [
        "core_indicador",
        "tradingview",
        "alertas",
    ],
}


def main() -> int:
    errors: list[str] = []

    for relative_path in REQUIRED_FILES:
        path = ROOT / relative_path
        if not path.exists():
            errors.append(f"Falta archivo requerido: {relative_path}")
        elif path.is_file() and path.stat().st_size == 0:
            errors.append(f"Archivo vacío: {relative_path}")

    for relative_path, snippets in REQUIRED_SNIPPETS.items():
        path = ROOT / relative_path
        if not path.exists():
            continue
        content = path.read_text(encoding="utf-8")
        for snippet in snippets:
            if snippet not in content:
                errors.append(f"Falta texto clave en {relative_path}: {snippet}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"VALIDACION_DOCUMENTACION_VIVA=FAIL total_errores={len(errors)}")
        return 1

    print("VALIDACION_DOCUMENTACION_VIVA=OK")
    print(f"archivos_requeridos={len(REQUIRED_FILES)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
