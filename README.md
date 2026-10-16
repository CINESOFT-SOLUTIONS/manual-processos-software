# Manual de Processos de Software — CineDoom

<table width="100%">
  <thead>
    <tr>
      <th width="50%" align="left">🎓 Identificação Acadêmica</th>
      <th width="50%" align="left">👥 Integrantes do Grupo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td valign="top">
        <strong>Instituição:</strong> Universidade Federal de Goiás (UFG)<br>
        <strong>Unidade:</strong> Instituto de Informática (INF)<br>
        <strong>Curso:</strong> Bacharelado em Engenharia de Software<br>
        <strong>Disciplina:</strong> Processos de Engenharia de Software<br>
        <strong>Período Letivo:</strong> 2026/2
      </td>
      <td valign="top">
        • Carlos Eduardo Freire da Silva<br>
        • Gabriel Henrique Lourenço Dias<br>
        • Kayque Vicente Silva<br>
        • Luiz Pedro Pereira Mendes Saraiva<br>
        • Yury Nogueira de Oliveira Silva
      </td>
    </tr>
  </tbody>
</table>

---

## 📌 Visão Geral

Este repositório contém o **Manual de Processos de Software** e os artefatos de engenharia desenvolvidos para o sistema **CineDoom** (gestão de salas de cinema e bilheteria).

O trabalho adota como premissas:
1. **Base Normativa:** [ABNT NBR ISO/IEC/IEEE 12207:2021](docs/abnt-iso-iec-12207-2021.md) (referência formal em PDF: [abnt-iso-iec-12207-2021.pdf](docs/abnt-iso-iec-12207-2021.pdf)).
2. **Fonte de Decisões:** [Project Definition Workbook (PDW)](docs/project-definition-workbook.md) — Fonte única da verdade das decisões de produto, arquitetura e negócio.

---

## 🗂️ Estrutura do Repositório

```text
manual-processos/
├── assets/                                      # Diagramas, fluxos BPMN e artefatos visuais
│   └── README.md
├── docs/                                        # Documentações de apoio, normas e especificações
│   ├── README.md
│   ├── abnt-iso-iec-12207-2021.pdf              # Cópia integral oficial da norma em PDF
│   ├── abnt-iso-iec-12207-2021.md               # Transcrição da norma em Markdown para leitura rápida
│   ├── project-definition-workbook.md           # Project Definition Workbook (PDW)
│   ├── diretrizes-parte-04.md                   # Orientações de aula e tópicos para a Parte 4
│   └── rascunho-parte-03.md                     # Rascunho preliminar da Parte 3 (com itens 3.5 a 3.7)
├── prompts/                                     # Catálogo e templates de prompts utilizados com IA
│   ├── README.md
│   ├── templates/
│   │   └── template-prompt.md                   # Template padrão para novos prompts
│   └── validacoes/
│       ├── validador-iso12207.md                # Validador de conformidade com a ISO 12207
│       └── analise-ia-parte-03.md               # Auditoria da sugestão de IA da Parte 3
├── scripts/                                     # Scripts utilitários e de automação
│   └── compilar.sh                              # Compilação unificada com Tectonic
├── slides_latex/                                # Apresentação em slides (Beamer UFG/INF)
│   ├── apresentacao-manual.tex
│   ├── beamerthemeUfg.sty
│   └── lib/
├── trabalho_latex/                              # Relatório oficial ABNT em LaTeX
│   └── manual-processos.tex
├── .gitignore
├── manual-processos-software.md                 # Manual principal consolidado
└── README.md
```

---

## 🧭 Guia de Navegação

- 📄 **[manual-processos-software.md](manual-processos-software.md):** Manual consolidado para leitura direta no GitHub.
- 📋 **[docs/project-definition-workbook.md](docs/project-definition-workbook.md):** Caderno de premissas e decisões do CineDoom (PDW).
- 📚 **[docs/abnt-iso-iec-12207-2021.md](docs/abnt-iso-iec-12207-2021.md):** Norma ABNT NBR ISO/IEC/IEEE 12207:2021 ([PDF](docs/abnt-iso-iec-12207-2021.pdf)).
- 📝 **[docs/diretrizes-parte-04.md](docs/diretrizes-parte-04.md):** Diretrizes de aula e requisitos para a Parte 4.
- 🤖 **[prompts/](prompts/):** Pasta com templates e validadores de IA.
- 📑 **[trabalho_latex/manual-processos.tex](trabalho_latex/manual-processos.tex):** Código-fonte LaTeX formatado conforme as normas ABNT.
- 📽️ **[slides_latex/apresentacao-manual.tex](slides_latex/apresentacao-manual.tex):** Slides da apresentação no template Beamer UFG/INF.
- 🖼️ **[assets/](assets/):** Diagramas de processos e artefatos gráficos.

---

## 🛠️ Como Compilar os Documentos

Para compilar o manual em LaTeX e os slides da apresentação com o [Tectonic](https://tectonic-typesetting.github.io/):

```bash
./scripts/compilar.sh
```
