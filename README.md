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
        <strong>Docente:</strong> Profa. Dra. Juliana Pereira de Souza Zinader<br>
        <strong>Período Letivo:</strong> 2026/2
      </td>
      <td valign="top">
        • Carlos Eduardo Freire da Silva<br>
        • Gabriel Henrique Lourenço Dias<br>
        • Kayque Vicente Silva<br>
        • Yury Nogueira de Oliveira Silva
      </td>
    </tr>
  </tbody>
</table>

---

## 📌 Visão Geral

Este repositório contém o **Manual de Processos de Software** e os artefatos de engenharia desenvolvidos para o sistema **CineDoom** (gestão de salas de cinema e bilheteria).

O trabalho adota como premissas:
1. **Base Normativa:** [ABNT NBR ISO/IEC/IEEE 12207:2021](docs/norma-iso/abnt-iso-iec-12207-2021.md) (referência formal em PDF: [abnt-iso-iec-12207-2021.pdf](docs/norma-iso/abnt-iso-iec-12207-2021.pdf)).
2. **Fonte de Decisões:** [Project Definition Workbook (PDW)](docs/constituicao/project-definition-workbook.md) — Fonte única da verdade das decisões de produto, arquitetura e negócio.

---

## 🗂️ Estrutura do Repositório

```text
manual-processos/
├── assets/                                      # Diagramas, fluxos BPMN e artefatos visuais por parte (0 a 4)
│   └── README.md
├── docs/                                        # Documentações de apoio, normas e validações
│   ├── README.md
│   ├── constituicao/                            # Project Definition Workbook (PDW)
│   ├── norma-iso/                               # Cópia em PDF e transcrição em Markdown da ISO 12207
│   ├── validacoes/                              # Relatórios de auditoria e validação por parte (0 a 4)
│   └── rascunhos/                               # Rascunhos preliminares de trabalho por parte (0 a 4)
├── prompts/                                     # Catálogo de prompts organizado pelas 5 partes
│   ├── README.md
│   ├── template-prompt.md                       # Template padrão de novos prompts
│   ├── validador-iso12207.md                    # Validador de conformidade contra a ISO 12207
│   ├── parte-00/                                # Prompts da Parte 0 (Apresentação do Software)
│   ├── parte-01/                                # Prompts da Parte 1 (Processos de Acordo)
│   ├── parte-02/                                # Prompts da Parte 2 (Processos Habilitadores)
│   ├── parte-03/                                # Prompts da Parte 3 (Gerenciamento Técnico)
│   └── parte-04/                                # Prompts da Parte 4 (Processos Técnicos)
├── scripts/                                     # Scripts utilitários e de automação
│   └── compilar.sh                              # Compilação unificada com Tectonic
├── slides_latex/                                # Apresentação em slides (Beamer UFG/INF)
│   ├── apresentacao-manual.tex
│   ├── beamerthemeUfg.sty
│   └── lib/
├── trabalho_latex/                              # Relatório oficial ABNT em LaTeX
│   └── manual-processos-software.tex
├── .gitignore
├── manual-processos-software.md                 # Manual principal consolidado
└── README.md
```

### 📂 O que faz cada pasta do repositório

| Pasta / Arquivo | Descrição Objetiva |
|---|---|
| [`manual-processos-software.md`](manual-processos-software.md) | **Documento Principal:** Texto consolidado de todo o manual de processos do CineDoom. |
| [`fluxo-trabalho.md`](fluxo-trabalho.md) | **Guia de Colaboração:** Passo a passo para criar prompts, validar e incorporar conteúdo. |
| [`prompts/`](prompts/) | **Engenharia de Prompts:** Prompts de IA separados por parte (0 a 4), template e validador de conformidade. |
| [`docs/`](docs/) | **Base de Conhecimento:** Norma ISO 12207, caderno de decisões do projeto (PDW), validações e rascunhos. |
| [`assets/`](assets/) | **Artefatos Visuais:** Diagramas de processos, modelos BPMN/PlantUML e figuras. |
| [`trabalho_latex/`](trabalho_latex/) | **Relatório em LaTeX:** Versão formatada segundo as normas da ABNT (NBR 14724). |
| [`slides_latex/`](slides_latex/) | **Apresentação:** Slides para defesa oral no tema oficial da UFG/INF (Beamer). |
| [`scripts/`](scripts/) | **Automação:** Script `compilar.sh` para compilar os PDFs localmente. |

---

## 🧭 Guia de Navegação

- 🚀 **[fluxo-trabalho.md](fluxo-trabalho.md):** Guia de fluxo de trabalho para colaboração no repositório.
- 📄 **[manual-processos-software.md](manual-processos-software.md):** Manual consolidado para leitura direta no GitHub.
- 🤖 **[prompts/](prompts/):** Catálogo de prompts divididos por partes (**0 a 4**), com template e validador.
- 📋 **[docs/constituicao/project-definition-workbook.md](docs/constituicao/project-definition-workbook.md):** Caderno de premissas e decisões do CineDoom (PDW).
- 📚 **[docs/norma-iso/](docs/norma-iso/):** Norma ABNT NBR ISO/IEC/IEEE 12207:2021 ([PDF](docs/norma-iso/abnt-iso-iec-12207-2021.pdf) e [Markdown](docs/norma-iso/abnt-iso-iec-12207-2021.md)).
- 📑 **[trabalho_latex/manual-processos-software.tex](trabalho_latex/manual-processos-software.tex):** Código-fonte LaTeX formatado conforme as normas ABNT.
- 📽️ **[slides_latex/apresentacao-manual.tex](slides_latex/apresentacao-manual.tex):** Slides da apresentação no template Beamer UFG/INF.
- 🖼️ **[assets/](assets/):** Diagramas de processos e artefatos gráficos.

---

## 🛠️ Como Compilar os Documentos

Para compilar o manual em LaTeX e os slides da apresentação com o [Tectonic](https://tectonic-typesetting.github.io/):

```bash
./scripts/compilar.sh
```
