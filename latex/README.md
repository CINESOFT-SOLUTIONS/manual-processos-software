# Publicação Tipográfica (latex)

Este diretório contém o código-fonte em LaTeX para a editoração oficial dos documentos acadêmicos da disciplina de Processos de Engenharia de Software (UFG/INF).

A diagramação está subdividida em dois produtos editoriais: o **Relatório Técnico em conformidade com as normas ABNT** e a **Apresentação de Slides em Beamer com a identidade visual da UFG/INF**.

---

## Estrutura de Diretórios

### 1. Relatório Técnico ABNT (`report/`)
* **[`report/manual-processos-software.tex`](report/manual-processos-software.tex):** Código-fonte principal formatado segundo as normas:
  * **ABNT NBR 14724:** Estrutura de trabalhos acadêmicos (capa, folha de rosto, elementos pré-textuais, textuais e pós-textuais).
  * **ABNT NBR 6024:** Numeração progressiva das seções de um documento.
  * **ABNT NBR 6027:** Sumário e formatação de cabeçalhos.
  * **Margens:** 3 cm superior e esquerda; 2 cm inferior e direita; entrelinha 1,5; parágrafo com recuo de 1,25 cm.
* **`report/manual-processos-software.pdf`:** Documento compilado final pronto para entrega e impressão.

### 2. Apresentação em Slides Beamer (`presentation/`)
* **[`presentation/apresentacao-manual.tex`](presentation/apresentacao-manual.tex):** Código-fonte dos slides para a defesa oral perante a banca avaliadora.
* **`presentation/beamerthemeUfg.sty`:** Tema oficial da Universidade Federal de Goiás com suporte a cabeçalhos e rodapés institucionais.
* **`presentation/lib/`:** Layouts de fundo e logomarcas em alta definição da UFG e do Instituto de Informática.
* **`presentation/apresentacao-manual.pdf`:** Slides compilados para projeção.

---

## Como Compilar Localmente

A compilação é automatizada pelo script na raiz do repositório, que utiliza preferencialmente o motor **Tectonic** (sem necessidade de gerenciar pacotes manuais):

```bash
./scripts/compilar.sh
```

### Compiladores Suportados (em ordem de fallback):
1. **Tectonic** (instalado automaticamente em `scripts/bin/` se ausente)
2. **latexmk** (`latexmk -pdf ...`)
3. **xelatex**
4. **pdflatex**
