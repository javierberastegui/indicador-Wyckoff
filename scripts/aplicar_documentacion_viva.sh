#!/usr/bin/env bash
set -euo pipefail

python3 scripts/validar_documentacion_viva.py

git status --short

echo "Siguiente paso sugerido:"
echo "git add AGENTS.md README.md doc scripts"
echo "git commit -m 'docs: add living documentation protocol'"
echo "git push origin main"
