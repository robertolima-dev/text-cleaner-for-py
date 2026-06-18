#!/usr/bin/env bash
# Builda o wheel e instala numa venv limpa (sem deps de dev) para pegar
# dependências/entry points que só faltam fora do ambiente de desenvolvimento.
# Teste FUNCIONAL real (clean_text), não só import.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

rm -rf dist build
rm -rf ./*.egg-info 2>/dev/null || true
python -m build

VENV_DIR="$(mktemp -d)/venv"
python -m venv "$VENV_DIR"
"$VENV_DIR/bin/pip" install -q "$(ls dist/*.whl)"

"$VENV_DIR/bin/python" -c "
from text_cleaner_for_py.cleaner import clean_text
result = clean_text('  Olá   Mundo!!  ', case='lower')
assert result, 'esperava um texto limpo não-vazio'
print('IMPORT + FUNCTIONAL OK:', result)
"

rm -rf "$(dirname "$VENV_DIR")"
echo "Smoke test passou."
