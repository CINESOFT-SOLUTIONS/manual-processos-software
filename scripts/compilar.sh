#!/bin/bash
set -e

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

# Compila relatório ABNT em LaTeX se existir
if [ -f "$ROOT_DIR/trabalho_latex/manual-processos-software.tex" ]; then
    cd "$ROOT_DIR/trabalho_latex"
    echo "Compilando manual-processos-software.pdf com Tectonic..."
    tectonic manual-processos-software.tex
    echo "Sucesso! Manual em: trabalho_latex/manual-processos-software.pdf"
elif [ -f "$ROOT_DIR/trabalho_latex/manual-processos.tex" ]; then
    cd "$ROOT_DIR/trabalho_latex"
    echo "Compilando manual-processos.pdf com Tectonic..."
    tectonic manual-processos.tex
    echo "Sucesso! Manual em: trabalho_latex/manual-processos.pdf"
elif [ -f "$ROOT_DIR/latex/manual-processos.tex" ]; then
    cd "$ROOT_DIR/latex"
    echo "Compilando manual-processos.pdf com Tectonic..."
    tectonic manual-processos.tex
    echo "Sucesso! Manual em: latex/manual-processos.pdf"
fi

# Compila slides da apresentação se existirem
if [ -f "$ROOT_DIR/slides_latex/apresentacao-manual.tex" ]; then
    cd "$ROOT_DIR/slides_latex"
    echo "Compilando apresentacao-manual.pdf com Tectonic..."
    tectonic apresentacao-manual.tex
    echo "Sucesso! Slides em: slides_latex/apresentacao-manual.pdf"
elif [ -f "$ROOT_DIR/slides/apresentacao-manual.tex" ]; then
    cd "$ROOT_DIR/slides"
    echo "Compilando apresentacao-manual.pdf com Tectonic..."
    tectonic apresentacao-manual.tex
    echo "Sucesso! Slides em: slides/apresentacao-manual.pdf"
fi
