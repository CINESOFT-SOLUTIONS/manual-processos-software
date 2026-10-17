#!/bin/bash
set -e

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

# -----------------------------------------------------------------------------
# 1. Função para verificar e auto-instalar o Tectonic caso ausente
# -----------------------------------------------------------------------------
ensure_tectonic() {
    # 1. Já está disponível no PATH?
    if command -v tectonic >/dev/null 2>&1; then
        return 0
    fi

    # 2. Já foi baixado localmente em scripts/bin?
    if [ -x "$ROOT_DIR/scripts/bin/tectonic" ]; then
        export PATH="$ROOT_DIR/scripts/bin:$PATH"
        return 0
    fi

    echo "================================================================="
    echo "⚠️  Compilador Tectonic não encontrado no seu ambiente."
    echo "================================================================="
    
    OS="$(uname -s)"
    echo "🔍 Sistema operacional detectado: $OS"
    echo "🚀 Tentando instalar o Tectonic automaticamente..."
    echo ""

    case "$OS" in
        Darwin*)
            if command -v brew >/dev/null 2>&1; then
                echo "🍺 Homebrew detectado. Instalando Tectonic via Homebrew..."
                brew install tectonic || true
            else
                echo "⬇️  Homebrew não encontrado. Baixando binário oficial standalone do Tectonic..."
                mkdir -p "$ROOT_DIR/scripts/bin"
                (cd "$ROOT_DIR/scripts/bin" && curl --proto '=https' --tlsv1.2 -fsSL https://drop-sh.fullyjustified.net | sh) || true
            fi
            ;;
        Linux*)
            echo "⬇️  Baixando binário oficial standalone do Tectonic..."
            mkdir -p "$ROOT_DIR/scripts/bin"
            (cd "$ROOT_DIR/scripts/bin" && curl --proto '=https' --tlsv1.2 -fsSL https://drop-sh.fullyjustified.net | sh) || true
            ;;
        CYGWIN*|MINGW*|MSYS*)
            if command -v winget.exe >/dev/null 2>&1; then
                echo "🪟 Windows (winget) detectado. Instalando Tectonic..."
                winget.exe install Tectonic.Tectonic --accept-source-agreements --accept-package-agreements || true
            elif command -v scoop >/dev/null 2>&1; then
                echo "🪟 Scoop detectado. Instalando Tectonic..."
                scoop install tectonic || true
            elif command -v choco >/dev/null 2>&1; then
                echo "🪟 Chocolatey detectado. Instalando Tectonic..."
                choco install tectonic -y || true
            fi
            ;;
        *)
            echo "❓ Sistema não mapeado para instalação direta: $OS"
            ;;
    esac

    # Atualiza PATH se baixou em scripts/bin
    if [ -x "$ROOT_DIR/scripts/bin/tectonic" ]; then
        export PATH="$ROOT_DIR/scripts/bin:$PATH"
    fi

    if command -v tectonic >/dev/null 2>&1; then
        echo ""
        echo "✅ Tectonic instalado com sucesso e pronto para uso!"
        echo "================================================================="
        echo ""
        return 0
    fi

    echo ""
    echo "⚠️  Não foi possível instalar o Tectonic automaticamente."
    echo "🔍 Verificando se há outros compiladores LaTeX instalados no sistema..."
    return 1
}

# -----------------------------------------------------------------------------
# 2. Função de compilação flexível (Tectonic com fallback para latexmk/pdflatex)
# -----------------------------------------------------------------------------
compile_document() {
    local target_dir="$1"
    local tex_file="$2"
    local pdf_name="${tex_file%.tex}.pdf"

    if [ ! -f "$target_dir/$tex_file" ]; then
        return 0
    fi

    cd "$target_dir"
    echo "-----------------------------------------------------------------"
    echo "📄 Processando: $target_dir/$tex_file"

    if command -v tectonic >/dev/null 2>&1; then
        echo "⚡ Compilando com Tectonic..."
        tectonic "$tex_file"
        echo "✅ Sucesso! Gerado: $target_dir/$pdf_name"
    elif command -v latexmk >/dev/null 2>&1; then
        echo "🔄 Fallback: Compilando com latexmk..."
        latexmk -pdf -interaction=nonstopmode "$tex_file"
        echo "✅ Sucesso! Gerado: $target_dir/$pdf_name"
    elif command -v xelatex >/dev/null 2>&1; then
        echo "🔄 Fallback: Compilando com xelatex..."
        xelatex -interaction=nonstopmode "$tex_file" >/dev/null
        xelatex -interaction=nonstopmode "$tex_file"
        echo "✅ Sucesso! Gerado: $target_dir/$pdf_name"
    elif command -v pdflatex >/dev/null 2>&1; then
        echo "🔄 Fallback: Compilando com pdflatex..."
        pdflatex -interaction=nonstopmode "$tex_file" >/dev/null
        pdflatex -interaction=nonstopmode "$tex_file"
        echo "✅ Sucesso! Gerado: $target_dir/$pdf_name"
    else
        echo "❌ Erro: Nenhum compilador LaTeX encontrado (Tectonic, latexmk, xelatex, pdflatex)."
        echo ""
        echo "👉 Para compilar este documento, instale o Tectonic com 1 comando:"
        echo "   • macOS:   brew install tectonic"
        echo "   • Windows: winget install Tectonic.Tectonic  (ou 'scoop install tectonic')"
        echo "   • Linux:   curl --proto '=https' --tlsv1.2 -fsSL https://drop-sh.fullyjustified.net | sh"
        echo "================================================================="
        exit 1
    fi
}

# -----------------------------------------------------------------------------
# 3. Execução Principal
# -----------------------------------------------------------------------------
echo "🚀 Iniciando compilação dos documentos do projeto..."

# Tenta garantir o Tectonic antes de tudo
ensure_tectonic || true

# 1. Compila o Relatório ABNT
if [ -f "$ROOT_DIR/trabalho_latex/manual-processos-software.tex" ]; then
    compile_document "$ROOT_DIR/trabalho_latex" "manual-processos-software.tex"
elif [ -f "$ROOT_DIR/trabalho_latex/manual-processos.tex" ]; then
    compile_document "$ROOT_DIR/trabalho_latex" "manual-processos.tex"
elif [ -f "$ROOT_DIR/latex/manual-processos.tex" ]; then
    compile_document "$ROOT_DIR/latex" "manual-processos.tex"
fi

# 2. Compila os Slides da Apresentação
if [ -f "$ROOT_DIR/slides_latex/apresentacao-manual.tex" ]; then
    compile_document "$ROOT_DIR/slides_latex" "apresentacao-manual.tex"
elif [ -f "$ROOT_DIR/slides/apresentacao-manual.tex" ]; then
    compile_document "$ROOT_DIR/slides" "apresentacao-manual.tex"
fi

echo "-----------------------------------------------------------------"
echo "🎉 Compilação concluída com sucesso!"
echo "📁 PDFs disponíveis:"
[ -f "$ROOT_DIR/trabalho_latex/manual-processos-software.pdf" ] && echo "   • $ROOT_DIR/trabalho_latex/manual-processos-software.pdf"
[ -f "$ROOT_DIR/slides_latex/apresentacao-manual.pdf" ] && echo "   • $ROOT_DIR/slides_latex/apresentacao-manual.pdf"
echo "================================================================="
