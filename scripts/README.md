# Scripts de Compilação e Montagem do Manual

Este diretório contém os scripts utilitários oficiais do projeto:

---

## 1. 📄 Montagem do Manual em Markdown (`montar-manual.sh`)

Concatena e compila todos os capítulos individuais em Markdown (`manual/capitulos/[0-9][0-9]-*.md`) em um único documento consolidado:

```bash
./scripts/montar-manual.sh
```

- **Origem:** `manual/capitulos/00-identificacao.md` até `06-avaliacao-melhoria.md`
- **Destino gerado:** `manual/manual-processos-software.md`

---

## 2. 📑 Compilação do Manual Oficial em LaTeX (`build-manual-latex.sh`)

Compila o documento mestre editorial LaTeX (`main.tex`) diretamente com a engine **Tectonic**, gerando o PDF institucional oficial no padrão visual e ABNT da CineSoft:

```bash
./scripts/build-manual-latex.sh
```

- **Origem:** `manual/latex/template/main.tex` (com seus capítulos `.tex` dedicados)
- **Destino gerado:** `manual/latex/template/main.pdf`

---

## 3. 🛠️ Script Geral de CI/CD (`compilar.sh`)

Executado pelo GitHub Actions para assegurar que a montagem dos capítulos Markdown ocorra sem erros na esteira de integração contínua:

```bash
./scripts/compilar.sh
```
