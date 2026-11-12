#!/usr/bin/env bash
# =============================================================================
# GERAÇÃO DOS DIAGRAMAS VETORIAIS (PlantUML -> PDF)
#
# Renderiza todos os arquivos .puml de assets/capitulo-*/diagramas/ para .pdf
# vetorial no mesmo diretório, garantindo que o LaTeX sempre embute a versão mais
# recente do diagrama (evita o descompasso entre .puml, .md e .pdf).
#
# Dependência: Java (JDK 8+) + plantuml.jar
#
# Para obter o plantuml.jar (versão oficial com suporte a PDF via OpenPDF):
#   curl -L -o scripts/lib/plantuml.jar \
#     https://github.com/plantuml/plantuml/releases/latest/download/plantuml.jar
#
# Uso:
#   ./scripts/gerar-diagramas.sh
#
# Variáveis de ambiente opcionais:
#   PLANTUML_JAR  -> caminho para o plantuml.jar (se não definido, o script
#                    procura em scripts/lib/ e em locais padrão do sistema)
#   JAVA_BIN      -> caminho para o executável java
# =============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
ASSETS_DIR="${ROOT_DIR}/assets"

JAVA_BIN="${JAVA_BIN:-java}"

# --- Localização do executável java --------------------------------------------
find_java() {
  if [[ -n "${JAVA_BIN:-}" && -x "${JAVA_BIN}" ]]; then
    echo "${JAVA_BIN}"
    return 0
  fi
  if command -v java >/dev/null 2>&1; then
    command -v java
    return 0
  fi
  # JDKs instalados no Windows (comum em maquinas de desenvolvimento)
  local candidates=(
    "/c/Program Files/jdk-27.0.1.0.3/bin/java"
    "/c/Program Files/Microsoft/jdk-*/bin/java"
    "/c/Program Files/Java/jdk*/bin/java"
    "/c/Program Files/Eclipse Adoptium/jdk-*/bin/java"
  )
  local found
  for found in "${candidates[@]}"; do
    # resolve padroes glob
    local resolved
    resolved="$(compgen -G "${found}" 2>/dev/null | head -n 1 || true)"
    if [[ -n "${resolved}" && -x "${resolved}" ]]; then
      echo "${resolved}"
      return 0
    fi
  done
  # JRE embarcado em extensoes do VS Code
  found="$(find "${HOME}/.vscode/extensions" -maxdepth 4 -path '*/bin/java' -type f 2>/dev/null | head -n 1 || true)"
  if [[ -n "${found}" ]]; then
    echo "${found}"
    return 0
  fi
  return 1
}

# --- Localização do plantuml.jar ------------------------------------------------
find_plantuml_jar() {
  if [[ -n "${PLANTUML_JAR:-}" && -f "${PLANTUML_JAR}" ]]; then
    echo "${PLANTUML_JAR}"
    return 0
  fi
  local candidates=(
    "${ROOT_DIR}/scripts/lib/plantuml.jar"
    "${HOME}/.vscode/extensions/jebbs.plantuml-2.18.1/plantuml.jar"
    "/usr/share/plantuml/plantuml.jar"
    "/opt/plantuml/plantuml.jar"
  )
  local found
  for found in "${candidates[@]}"; do
    [[ -f "${found}" ]] && { echo "${found}"; return 0; }
  done
  # Busca generica no diretorio do usuario
  found="$(find "${HOME}" -maxdepth 6 -name 'plantuml.jar' -type f 2>/dev/null | head -n 1 || true)"
  [[ -n "${found}" ]] && { echo "${found}"; return 0; }
  return 1
}

if ! JAVA_BIN="$(find_java)"; then
  echo "AVISO: Java não encontrado (JAVA_BIN). Diagramas não serão regenerados." >&2
  exit 0
fi

if ! PLANTUML="$(find_plantuml_jar)"; then
  echo "AVISO: plantuml.jar não encontrado. Defina PLANTUML_JAR para regenerar os diagramas." >&2
  exit 0
fi

echo "==> PlantUML: ${PLANTUML}"
echo "==> Java     : ${JAVA_BIN}"

shopt -s nullglob
PUML_FILES=("${ASSETS_DIR}"/capitulo-*/diagramas/*.puml)

if [[ ${#PUML_FILES[@]} -eq 0 ]]; then
  echo "==> Nenhum arquivo .puml encontrado em assets/capitulo-*/diagramas/"
  exit 0
fi

for puml in "${PUML_FILES[@]}"; do
  dir="$(dirname "${puml}")"
  echo "    - $(basename "${puml}")"
  if ! "${JAVA_BIN}" -jar "${PLANTUML}" -tpdf -charset UTF-8 -o "${dir}" "${puml}" 2>/dev/null; then
    echo "ERRO: falha ao gerar $(basename "${puml}")." >&2
    echo "      Verifique se o plantuml.jar suporta exportacao PDF (use a versao oficial)." >&2
    exit 1
  fi
done

echo "==> ${#PUML_FILES[@]} diagrama(s) regenerado(s) em PDF vetorial."
