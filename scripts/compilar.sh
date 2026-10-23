#!/bin/bash
set -e

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

# Paleta CLI Vitest/pnpm (ativa por padrão, respeita NO_COLOR)
if [ -z "$NO_COLOR" ]; then
    BG_CYAN='\033[46;30;1m'
    BG_GREEN='\033[42;30;1m'
    BG_BLUE='\033[44;37;1m'
    BG_YELLOW='\033[43;30;1m'
    BG_RED='\033[41;37;1m'
    CYAN='\033[36m'
    GREEN='\033[32m'
    YELLOW='\033[33m'
    RED='\033[31m'
    DIM='\033[2m'
    BOLD='\033[1m'
    RESET='\033[0m'
else
    BG_CYAN=''
    BG_GREEN=''
    BG_BLUE=''
    BG_YELLOW=''
    BG_RED=''
    CYAN=''
    GREEN=''
    YELLOW=''
    RED=''
    DIM=''
    BOLD=''
    RESET=''
fi

# -----------------------------------------------------------------------------
# 1. Verificação e instalação do Tectonic
# -----------------------------------------------------------------------------
ensure_tectonic() {
    if command -v tectonic >/dev/null 2>&1; then
        return 0
    fi

    if [ -x "$ROOT_DIR/scripts/bin/tectonic" ]; then
        export PATH="$ROOT_DIR/scripts/bin:$PATH"
        return 0
    fi

    printf " ${BG_YELLOW} WARN ${RESET} ${YELLOW}Tectonic compiler not found in environment.${RESET}\n"
    OS="$(uname -s)"
    printf "  ${DIM}• OS:${RESET} %s\n" "$OS"
    printf "  ${DIM}• Attempting automatic installation...${RESET}\n"

    case "$OS" in
        Darwin*)
            if command -v brew >/dev/null 2>&1; then
                printf "  ${DIM}• Installing tectonic via Homebrew...${RESET}\n"
                brew install tectonic || true
            else
                printf "  ${DIM}• Downloading standalone binary...${RESET}\n"
                mkdir -p "$ROOT_DIR/scripts/bin"
                (cd "$ROOT_DIR/scripts/bin" && curl --proto '=https' --tlsv1.2 -fsSL https://drop-sh.fullyjustified.net | sh) || true
            fi
            ;;
        Linux*)
            printf "  ${DIM}• Downloading standalone binary...${RESET}\n"
            mkdir -p "$ROOT_DIR/scripts/bin"
            (cd "$ROOT_DIR/scripts/bin" && curl --proto '=https' --tlsv1.2 -fsSL https://drop-sh.fullyjustified.net | sh) || true
            ;;
        CYGWIN*|MINGW*|MSYS*)
            if command -v winget.exe >/dev/null 2>&1; then
                winget.exe install Tectonic.Tectonic --accept-source-agreements --accept-package-agreements || true
            elif command -v scoop >/dev/null 2>&1; then
                scoop install tectonic || true
            elif command -v choco >/dev/null 2>&1; then
                choco install tectonic -y || true
            fi
            ;;
        *)
            printf "  ${YELLOW}Unsupported platform for automated setup: %s${RESET}\n" "$OS"
            ;;
    esac

    if [ -x "$ROOT_DIR/scripts/bin/tectonic" ]; then
        export PATH="$ROOT_DIR/scripts/bin:$PATH"
    fi

    if command -v tectonic >/dev/null 2>&1; then
        printf "  ${GREEN}✓${RESET} Tectonic installed and ready.\n"
        return 0
    fi

    printf " ${BG_YELLOW} WARN ${RESET} ${YELLOW}Could not install Tectonic automatically. Falling back to system LaTeX...${RESET}\n"
    return 1
}

# -----------------------------------------------------------------------------
# 2. Compilação de documento LaTeX
# -----------------------------------------------------------------------------
compile_document() {
    local target_dir="$1"
    local tex_file="$2"
    local badge="$3"
    local pdf_name="${tex_file%.tex}.pdf"
    local rel_target="${target_dir#$ROOT_DIR/}"

    if [ ! -f "$target_dir/$tex_file" ]; then
        return 0
    fi

    cd "$target_dir"
    printf " %b %s/%s\n" "$badge" "$rel_target" "$tex_file"

    if command -v tectonic >/dev/null 2>&1; then
        tectonic "$tex_file" >/dev/null 2>&1 || tectonic "$tex_file"
        printf "  ${GREEN}✓${RESET} ${DIM}engine: tectonic ->${RESET} ${BOLD}%s/%s${RESET}\n\n" "$rel_target" "$pdf_name"
    elif command -v latexmk >/dev/null 2>&1; then
        latexmk -pdf -interaction=nonstopmode "$tex_file" >/dev/null 2>&1
        printf "  ${GREEN}✓${RESET} ${DIM}engine: latexmk ->${RESET} ${BOLD}%s/%s${RESET}\n\n" "$rel_target" "$pdf_name"
    elif command -v xelatex >/dev/null 2>&1; then
        xelatex -interaction=nonstopmode "$tex_file" >/dev/null 2>&1
        xelatex -interaction=nonstopmode "$tex_file" >/dev/null 2>&1
        printf "  ${GREEN}✓${RESET} ${DIM}engine: xelatex ->${RESET} ${BOLD}%s/%s${RESET}\n\n" "$rel_target" "$pdf_name"
    elif command -v pdflatex >/dev/null 2>&1; then
        pdflatex -interaction=nonstopmode "$tex_file" >/dev/null 2>&1
        pdflatex -interaction=nonstopmode "$tex_file" >/dev/null 2>&1
        printf "  ${GREEN}✓${RESET} ${DIM}engine: pdflatex ->${RESET} ${BOLD}%s/%s${RESET}\n\n" "$rel_target" "$pdf_name"
    else
        printf " ${BG_RED} FAIL ${RESET} ${RED}No LaTeX compiler found (tectonic, latexmk, xelatex, pdflatex).${RESET}\n"
        printf "        Install tectonic: 'brew install tectonic' (macOS) or 'winget install Tectonic.Tectonic'\n"
        exit 1
    fi
}

# -----------------------------------------------------------------------------
# 3. Execução Principal
# -----------------------------------------------------------------------------
START_TIME=$(date +%s)
printf "\n${BG_CYAN} DOCS ${RESET} ${BOLD}cinedoom-docs${RESET} ${DIM}v1.0.0${RESET}\n\n"

# Etapa 0: Monta o manual Markdown consolidado a partir de content/
if [ -f "$ROOT_DIR/scripts/montar-manual.sh" ]; then
    "$ROOT_DIR/scripts/montar-manual.sh"
    printf "\n"
fi

ensure_tectonic || true

# Etapa 1: Compilação do Relatório ABNT
if [ -f "$ROOT_DIR/latex/report/manual-processos-software.tex" ]; then
    compile_document "$ROOT_DIR/latex/report" "manual-processos-software.tex" "${BG_BLUE} LATEX ${RESET}"
elif [ -f "$ROOT_DIR/trabalho_latex/manual-processos-software.tex" ]; then
    compile_document "$ROOT_DIR/trabalho_latex" "manual-processos-software.tex" "${BG_BLUE} LATEX ${RESET}"
fi

# Etapa 2: Compilação dos Slides Beamer
if [ -f "$ROOT_DIR/latex/presentation/apresentacao-manual.tex" ]; then
    compile_document "$ROOT_DIR/latex/presentation" "apresentacao-manual.tex" "${BG_YELLOW} SLIDES ${RESET}"
elif [ -f "$ROOT_DIR/slides_latex/apresentacao-manual.tex" ]; then
    compile_document "$ROOT_DIR/slides_latex" "apresentacao-manual.tex" "${BG_YELLOW} SLIDES ${RESET}"
fi

END_TIME=$(date +%s)
ELAPSED=$((END_TIME - START_TIME))

printf "${BG_GREEN} SUCCESS ${RESET} ${GREEN}${BOLD}Build completed in %ss${RESET}\n\n" "$ELAPSED"
printf "${BOLD}Artifacts:${RESET}\n"
printf "  ${CYAN}•${RESET} manual-processos-software.md ${DIM}(Markdown)${RESET}\n"
[ -f "$ROOT_DIR/latex/report/manual-processos-software.pdf" ] && printf "  ${CYAN}•${RESET} latex/report/manual-processos-software.pdf ${DIM}(ABNT NBR 14724)${RESET}\n"
[ -f "$ROOT_DIR/latex/presentation/apresentacao-manual.pdf" ] && printf "  ${CYAN}•${RESET} latex/presentation/apresentacao-manual.pdf ${DIM}(Beamer UFG/INF)${RESET}\n\n"
