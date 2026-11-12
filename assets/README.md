# Repositório Central de Ativos, Diagramas e Tabelas do Manual (CineDoom)

Este diretório armazena centralizadamente todos os artefatos visuais, diagramas em PlantUML/SVG, capturas de tela e tabelas estruturadas do **Manual de Processos de Software** da CineSoft Solutions / CineDoom.

Todos os artefatos são consumidos tanto pela documentação Markdown quanto pelos capítulos do documento oficial em LaTeX compilado via Tectonic.

---

## 📁 Estrutura de Diretórios por Capítulo

```text
manual-processos/assets/
├── logos/                                    # Identidade visual oficial (Midnight Navy e Crimson)
│   ├── cinesoft-logo-horizontal-white.png
│   ├── cinesoft-logo-horizontal-color.png
│   ├── cinedoom-logo-horizontal-white.png
│   ├── cinedoom-logo-horizontal-color.png
│   └── cinedoom-icon-favicon.png
│
├── capitulo-00/                              # Identificação e Elementos Pré-Textuais
│   └── tabelas/
│       └── historico-versoes.tex             # Histórico de revisões e aprovações
│
├── capitulo-01/                              # Apresentação do Software (CineDoom)
│   ├── prints/
│   │   ├── print-portal-cliente.png          # Portal do cliente (catálogo e assentos)
│   │   ├── print-bilheteria-atendente.png    # Módulo de bilheteria e guichê presencial
│   │   └── print-painel-gerencial.png        # Painel gerencial e back-office
│   └── tabelas/
│       └── perfis-usuarios-permissoes.tex    # Matriz de perfis, módulos e permissões
│
├── capitulo-02/                              # Processos de Acordo (Aquisição e Fornecimento)
│   └── tabelas/
│       ├── analise-make-or-buy.tex           # Matriz Make or Buy (core vs serviços)
│       └── perspectiva-fornecimento.tex      # Planos de fornecimento e SLAs
│
├── capitulo-03/                              # Processos Organizacionais Habilitadores
│   ├── diagramas/
│   │   ├── diagrama-ciclo-de-vida.puml       # Fonte PlantUML do Ciclo de Vida
│   │   ├── diagrama-ciclo-de-vida.svg        # Vetor SVG limpo
│   │   └── diagrama-ciclo-de-vida.pdf        # PDF vetorial de alta definição para LaTeX
│   └── tabelas/
│       ├── inventario-ferramental.tex        # Inventário de ferramentas e infraestrutura
│       └── matriz-raci.tex                   # Matriz RACI de responsabilidades
│
├── capitulo-04/                              # Processos de Gerenciamento Técnico
│   ├── diagramas/
│   │   ├── eap-projeto-3-niveis.puml         # Fonte PlantUML da EAP (3 níveis)
│   │   ├── eap-projeto-3-niveis.svg          # Vetor SVG limpo
│   │   ├── eap-projeto-3-niveis.pdf          # PDF vetorial para LaTeX
│   │   ├── fluxo-git-branches.puml           # Fonte PlantUML de Branches Git
│   │   ├── fluxo-git-branches.svg            # Vetor SVG limpo
│   │   └── fluxo-git-branches.pdf            # PDF vetorial para LaTeX
│   └── tabelas/
│       └── registro-riscos.tex               # Matriz Risk Register (probabilidade e impacto)
│
├── capitulo-05/                              # Processos Técnicos de Engenharia
│   ├── diagramas/
│   │   ├── c4-containers.puml                # Diagrama C4 Nível 2 (Contêineres)
│   │   ├── c4-containers.pdf                 # PDF vetorial C4
│   │   ├── diagrama-sequencia.puml           # Sequência UML da Reserva Atômica e Baixa no Balcão
│   │   ├── diagrama-sequencia.pdf            # PDF vetorial Sequência
│   │   ├── diagrama-classes-dominio.puml     # Diagrama de Classes UML de Domínio
│   │   ├── diagrama-classes-dominio.pdf      # PDF vetorial Classes
│   │   ├── diagrama-rastreabilidade.puml      # Cadeia de Rastreabilidade (Macroentrega → Teste)
│   │   ├── diagrama-rastreabilidade.pdf       # PDF vetorial Cadeia de Rastreabilidade
│   │   ├── diagrama-casos-de-uso.puml         # Diagrama de Casos de Uso (gerado, não publicado no cap. 5)
│   │   └── diagrama-casos-de-uso.pdf          # PDF vetorial Casos de Uso
│   └── tabelas/
│       ├── catalogo-requisitos.tex           # Catálogo formal de RFs e RNFs
│       └── verificacao-validacao.tex         # Matriz de Verificação vs Validação
│
└── capitulo-06/                              # Avaliação e Melhoria dos Processos
    └── tabelas/
        ├── diagnostico-processo.tex          # 4 Perguntas de Diagnóstico MPS.BR
        └── plano-melhoria-pmp.tex            # Tabela do Plano de Melhoria (PMP)
```

---

## 🎨 Padrão Visual dos Diagramas

Todos os diagramas seguem o padrão gráfico técnico corporativo:
- **Código Declarativo:** Código-fonte editável em PlantUML (`.puml`).
- **Exportação Vetorial:** Vetores escaláveis limpos em SVG (`.svg`) e PDF (`.pdf`) via `rsvg-convert`.
- **Estética Editorial:** Fundo branco ou transparente, linhas finas em Midnight Navy (`#1A1A2E`), acentos discretos e tipografia Helvetica/Sans limpa, sem ilustrações infantis ou degradês coloridos saturados.
