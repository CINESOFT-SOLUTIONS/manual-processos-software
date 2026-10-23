# Manual de Processos de Software — CineDoom

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

Este repositório contém o **Manual de Processos de Software** e o pacote de governança e engenharia desenvolvido para o sistema **CineDoom** (plataforma de bilheteria presencial, gestão de catálogo e controle de ocupação de salas de cinema), estruturado em estrita conformidade com a norma **ABNT NBR ISO/IEC/IEEE 12207:2021**.

### Fontes Normativas e Diretrizes
1. **Base Normativa:** [ABNT NBR ISO/IEC/IEEE 12207:2021](references/iso-12207/abnt-iso-iec-12207-2021.md) (referência formal em PDF: [abnt-iso-iec-12207-2021.pdf](references/iso-12207/abnt-iso-iec-12207-2021.pdf)).
2. **Fonte da Verdade de Engenharia e Negócio:** [Especificação do CineDoom](specs/cinedoom-spec.md) e [Catálogo de ADRs](specs/adrs/README.md) — Requisitos, regras de negócio, modelo de dados e decisões arquiteturais do sistema.
3. **Diretrizes Pedagógicas:** [Instruções da Disciplina](references/guidelines/instrucoes-disciplina.md) e [Estrutura Mínima](references/guidelines/estrutura-minima-manual.md) estabelecidas pela Profa. Dra. Juliana Zinader.

---

## Arquitetura do Repositório (Docs-as-Code)

O repositório adota o modelo **Docs-as-Code**, separando a escrita modular de conteúdo, o repositório de especificações técnicas, os templates de editoração tipográfica (LaTeX e Beamer) e as referências canônicas:

```text
manual-processos/
├── content/                           # Capítulos modulares do manual (Fonte Canônica)
│   ├── 00-identificacao.md            # Folha de rosto e histórico de revisões
│   ├── 01-apresentacao-software.md    # Cap. 1: Identificação, problema, escopo e restrições
│   ├── 02-processos-acordo.md         # Cap. 2: Aquisição, fornecimento e parceiros
│   ├── 03-processos-organizacionais.md# Cap. 3: Ciclo de vida, infraestrutura, viabilidade, RACI e qualidade
│   ├── 04-gerenciamento-tecnico.md    # Cap. 4: Plano de projeto, riscos, configuração e métricas
│   └── 05-processos-tecnicos.md       # Cap. 5: Requisitos (AC-1..14), C4, Prisma, STRIDE, DPIA e testes
│
├── specs/                             # Especificações Formais de Engenharia e Governança
│   ├── adrs/                          # 12 Architecture Decision Records (ADR-001 a ADR-012)
│   ├── architecture/                  # Diagramas C4, especificações de componentes e wireframes UX/UI
│   ├── data-model/                    # Prisma Schema e dicionário relacional de dados
│   ├── security-compliance/           # Modelagem de Ameaças STRIDE e Avaliação de Impacto LGPD (DPIA)
│   ├── quality/                       # Matriz de rastreabilidade e suíte de concorrência ACID (50 threads)
│   ├── planning/                      # Plano de tarefas do TechLead (23 tarefas) e DevOps CI/CD
│   ├── cinedoom-spec.md               # Especificação funcional formal (PM)
│   └── cinedoom-spec.json             # Metadados estruturados
│
├── latex/                             # Publicação Tipográfica (Relatório ABNT e Apresentação)
│   ├── report/                        # Relatório do Manual formatado na ABNT NBR 14724
│   │   ├── manual-processos-software.tex
│   │   └── manual-processos-software.pdf
│   └── presentation/                  # Apresentação de slides Beamer (Identidade UFG/INF)
│       ├── apresentacao-manual.tex
│       ├── beamerthemeUfg.sty
│       └── lib/                       # Logos e layouts
│
├── references/                        # Referências Normativas e Diretrizes
│   ├── iso-12207/                     # Norma ABNT NBR ISO/IEC/IEEE 12207:2021
│   ├── pdw/                           # Registro histórico de premissas iniciais
│   └── guidelines/                    # Instruções e estrutura mínima docente
│
├── assets/                            # Ativos Visuais e Identidade de Marca
│   ├── logos/                         # Logomarcas oficiais CineSoft Solutions e CineDoom
│   └── diagrams/                      # Diagramas arquiteturais C4 e fluxos BPMN
│
├── scripts/                           # Automação de Build e Compilação
│   ├── montar-manual.sh               # Concatena content/ em manual-processos-software.md
│   └── compilar.sh                    # Pipeline completo de build (Markdown + LaTeX + Beamer)
│
├── manual-processos-software.md       # Documento consolidado contínuo para leitura web
└── README.md
```

---

## Guia de Navegação do Repositório

* **[manual-processos-software.md](manual-processos-software.md):** Manual unificado em arquivo único para leitura direta no GitHub.
* **[content/](content/):** Módulos individuais dos capítulos para edição isolada e revisões via Pull Request.
* **[specs/](specs/):** Especificações de engenharia detalhadas (ADRs, C4, Prisma, STRIDE, DPIA, QA).
* **[specs/adrs/](specs/adrs/):** Catálogo formal de Architecture Decision Records (ADR-001 a ADR-012).
* **[latex/report/](latex/report/):** Código-fonte e PDF do manual conforme a ABNT NBR 14724.
* **[latex/presentation/](latex/presentation/):** Código-fonte e PDF dos slides Beamer para apresentação perante a banca.
* **[references/](references/):** Documentos de apoio, norma ISO 12207 e diretrizes da disciplina.

---

## Ambiente e Organização de Repositórios

A solução CineDoom divide-se em dois repositórios na organização GitHub:
1. `manual-processos`: Processos de software, documentação ABNT, slides e governança ISO 12207.
2. `cinedoom-app`: Implementação real do software (Next.js 14, Prisma ORM, PostgreSQL Neon).

### Clonando ambos os projetos localmente:
```bash
# 1. Cria a pasta raiz do projeto
mkdir cinedoom && cd cinedoom

# 2. Clona o repositório de documentação e processos
git clone https://github.com/CINESOFT-SOLUTIONS/manual-processos.git

# 3. Clona o repositório da aplicação real
git clone https://github.com/CINESOFT-SOLUTIONS/cinedoom-app.git
```

### Abertura unificada no VS Code:
```bash
code cinedoom-app manual-processos
```

---

## Compilação e Build de Documentos

O projeto utiliza um pipeline automatizado que integra a concatenação modular do Markdown e a compilação tipográfica via motor **Tectonic**:

### Compilação completa (Markdown + Relatório ABNT + Slides Beamer):
```bash
./scripts/compilar.sh
```

### Atualização apenas do Markdown consolidado:
```bash
./scripts/montar-manual.sh
```

### Artefatos de saída gerados:
* `manual-processos-software.md` — Documento Markdown consolidado na raiz.
* `latex/report/manual-processos-software.pdf` — Relatório diagramado conforme ABNT NBR 14724 / 6024.
* `latex/presentation/apresentacao-manual.pdf` — Slides oficiais de defesa perante a banca no tema UFG/INF.
