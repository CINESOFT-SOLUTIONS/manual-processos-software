# Manual de Processos de Software — CineDoom

> 📘 **Guia Prático do Repositório (PDF):** Consulte o [Guia de Colaboração (PDF)](referencias/diretrizes/guia-colaboracao-repositorio.pdf) para entender o fluxo de trabalho da equipe, a organização de pastas e o checklist de 50 artefatos e evidências exigidos pela banca.

<table width="100%">
  <thead>
    <tr>
      <th width="50%" align="left">Identificação Acadêmica</th>
      <th width="50%" align="left">Integrantes da Equipe</th>
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

## Visão Geral do Projeto

Este repositório contém o **Manual de Processos de Software** e o pacote de governança e engenharia desenvolvido para o sistema **CineDoom** (plataforma de bilheteria presencial, totem de autoatendimento, gestão de catálogo e controle de ocupação de salas de cinema), estruturado em estrita conformidade com a norma **ABNT NBR ISO/IEC/IEEE 12207:2021**.

### Fontes Normativas e Diretrizes
1. **Base Normativa:** Normas internacionais e nacionais de ciclo de vida de software (`referencias/normas/`).
2. **Especificações e Decisões de Engenharia:** Requisitos funcionais, regras de negócio, modelagem de dados e decisões arquiteturais vigentes (`specs/`).
3. **Diretrizes Pedagógicas:** Critérios de pontuação, estrutura mínima e guias de redação de cada capítulo definidos pela Profa. Dra. Juliana Zinader (`referencias/diretrizes/`).

---

## Arquitetura do Repositório (Docs-as-Code)

O repositório adota o modelo **Docs-as-Code**, separando a escrita do manual, as especificações técnicas, os arquivos de consulta e os scripts de automação:

```text
manual-processos/
├── manual/                            # Publicações e módulos do Manual de Processos
│   ├── capitulos/                     # Capítulos modulares fonte (Fonte Canônica / SSOT)
│   ├── latex/                         # Publicação diagramada em padrão ABNT
│   └── manual-processos-software.md   # Manual consolidado contínuo para leitura
│
├── specs/                             # Especificações Formais de Engenharia e Governança
│   ├── adrs/                          # Catálogo de Architecture Decision Records
│   ├── architecture/                  # Diagramas C4 e especificações arquiteturais
│   ├── data-model/                    # Esquema de dados e dicionário relacional
│   ├── security-compliance/           # Modelagem de Ameaças (STRIDE) e Privacidade (LGPD)
│   ├── quality/                       # Estratégia de testes e matriz de rastreabilidade
│   └── planning/                      # Backlog, cronograma de sprints e planejamento técnico
│
├── referencias/                       # Fontes de Consulta e Diretrizes
│   ├── normas/                        # Textos integrais e resumos de normas técnicas
│   ├── diretrizes/                    # Instruções da disciplina e guias de redação por capítulo
│   └── aulas/                         # Slides oficiais, transcrições e diagramas das aulas
│
├── assets/                            # Ativos Visuais e Identidade de Marca
│   ├── logos/                         # Logomarcas oficiais CineSoft Solutions e CineDoom
│   └── diagrams/                      # Diagramas arquiteturais e fluxos visuais
│
└── scripts/                           # Automação de Montagem e Build
    ├── montar-manual.sh               # Concatena os capítulos no documento consolidado
    └── compilar.sh                    # Pipeline de compilação dos documentos
```

---

## Guia de Navegação do Repositório

* **[`manual/manual-processos-software.md`](manual/manual-processos-software.md):** Manual unificado em arquivo único para leitura direta no GitHub.
* **[`manual/capitulos/`](manual/capitulos/):** Módulos individuais dos capítulos para edição isolada e revisões via Pull Request.
* **[`manual/latex/`](manual/latex/):** Código-fonte e PDF do manual diagramado conforme a ABNT NBR 14724.
* **[`specs/`](specs/):** Especificações de engenharia detalhadas (ADRs, C4, Prisma, STRIDE, DPIA, QA).
* **[`referencias/`](referencias/):** Documentos de apoio, normas técnicas, diretrizes e material de aulas.
* **[`assets/`](assets/):** Logos e diagramas visuais do sistema.

---

## Ambiente e Organização de Repositórios

A solução CineDoom divide-se em dois repositórios na organização GitHub:
1. `manual-processos`: Processos de software, documentação ABNT e governança ISO 12207.
2. `cinedoom-app`: Implementação real do software (Next.js 15, Prisma ORM, PostgreSQL Neon).
