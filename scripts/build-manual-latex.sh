#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE_DIR="$(cd "${SCRIPT_DIR}/../manual/latex/template" && pwd)"

echo "==> Compilando Manual de Processos de Software (CineSoft Solutions / CineDoom)..."
cd "${TEMPLATE_DIR}"

tectonic main.tex

echo "==> Compilação concluída com sucesso!"
echo "==> Arquivo PDF gerado em: ${TEMPLATE_DIR}/main.pdf"
