# Estrutura e Padroes da Organizacao GitHub — CineDoom
### CineSoft Solutions | Engenharia de Processos de Software (ISO/IEC/IEEE 12207:2021)

Este documento estabelece o modelo de governanca, convencoes de versionamento e a arquitetura de repositorios da organizacao **CineSoft Solutions** no GitHub. A separacao entre o repositorio de **Processos/Manual** e o repositorio de **Software Real** garante rastreabilidade estrita entre a teoria normativa e a evidencia de engenharia executavel.

---

## 1. Visao Geral da Organizacao no GitHub

```text
github.com/CINESOFT-SOLUTIONS/
├── .github                       # Perfil publico da organizacao e templates globais
├── manual-processos-software     # Repositorio de governanca, Manual ISO 12207, LaTeX e Slides
└── cinedoom-app                  # Repositorio do software real (Next.js + Prisma + Neon + Vercel)
```

---

## 2. Repositorio 1: `manual-processos-software` (Docs-as-Code)

Este repositorio e a **fonte da verdade normativa e metodologica**. Ele contem todo o historico de decisoes, documentos formais de processo e os compiladores de PDF academicos em arquitetura Docs-as-Code.

### 2.1 Estrutura de Diretorios

```text
manual-processos-software/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── revisao_capitulo.md          # Template para revisao de capitulo do manual (Cap. 1 a 5)
│   │   ├── auditoria_qualidade.md       # Template para laudos de auditoria interna / conformidade
│   │   └── config.yml                   # Configuracao e links uteis para issues
│   ├── workflows/
│   │   └── compilar-docs.yml            # CI no GitHub Actions que compila os PDFs via Tectonic
│   ├── PULL_REQUEST_TEMPLATE.md         # Checklist de aprovacao com impacto normativo
│   └── CODEOWNERS                       # Governanca de revisores conforme a matriz RACI
├── content/                             # Fonte Unica da Verdade (SSOT) dos capitulos
│   ├── 00-identificacao.md              # Capa, identificacao dos autores e historico de versoes
│   ├── 01-apresentacao-software.md      # Capitulo 1: Apresentacao do software e escopo
│   ├── 02-processos-acordo.md           # Capitulo 2: Aquisicao e fornecimento B2B SaaS
│   ├── 03-processos-organizacionais.md  # Capitulo 3: Ciclo de vida, ferramentas e matriz RACI
│   ├── 04-gerenciamento-tecnico.md      # Capitulo 4: Planejamento, cronograma, riscos e 11 ADRs
│   └── 05-processos-tecnicos.md         # Capitulo 5: Requisitos, C4, Prisma, STRIDE e V&V
├── specs/                               # Especificacoes de Engenharia e Governanca Tecnica
│   ├── adrs/                            # Catalogo formal de 11 Architecture Decision Records
│   ├── architecture/                    # Diagramas C4, arquitetura de software e UX design
│   ├── data-model/                      # Schema relacional Prisma e definicao de entidades
│   ├── planning/                        # Plano do TechLead (20 tasks), cronograma e sprints
│   ├── quality/                         # Estrategia de testes e suite de 50 threads concorrentes
│   └── security-compliance/             # Modelagem STRIDE e Relatorio de Impacto LGPD (DPIA)
├── latex/                               # Compilacao tipografica de alta qualidade
│   ├── report/                          # Relatorio acadêmico formatado nas normas ABNT
│   │   └── manual-processos-software.tex
│   └── presentation/                    # Apresentacao oral da banca (Beamer tema UFG/INF)
│       └── apresentacao-manual.tex
├── references/                          # Documentos de apoio, diretrizes docentes e norma
│   ├── iso-12207/                       # Norma ABNT NBR ISO/IEC/IEEE 12207:2021
│   ├── guidelines/                      # Diretrizes e estrutura minima da Profa. Dra. Juliana
│   └── pdw/                             # Historico auditavel de definicoes de projeto
├── assets/                              # Ativos de marca e diagramas oficiais
│   ├── logos/                           # Logomarcas oficiais CineSoft Solutions e CineDoom
│   └── diagrams/                        # Diagramas exportados
├── scripts/                             # Scripts de automacao local
│   ├── montar-manual.sh                 # Concatena content/ em manual-processos-software.md
│   └── compilar.sh                      # Compilacao unificada com Tectonic (Relatorio + Slides)
├── manual-processos-software.md         # Documento consolidado montado para leitura web
└── README.md                            # Apresentacao do projeto, equipe e instrucoes
```

---

## 3. Repositorio 2: `cinedoom-app` (Software Real)

Este repositorio contem a **implementacao do software**, configurado para deploy continuo na **Vercel** conectado ao banco **Neon (PostgreSQL Serverless)**.

### 3.1 Estrutura de Diretorios Recomendada (Next.js 14 App Router)

```text
cinedoom-app/
├── src/
│   ├── app/                             # Next.js App Router (rotas, layouts e paginas)
│   │   ├── (auth)/login/                # Tela de autenticacao NextAuth.js
│   │   ├── (bilheteria)/                # Ponto de Venda do Atendente (mapa com polling 2s)
│   │   ├── (admin)/                     # Backoffice do Gerente (filmes, salas, sessoes, painel)
│   │   └── api/                         # Route Handlers e Webhooks
│   ├── modules/                         # Modulos de dominio com isolamento estrito
│   │   ├── bilheteria/                  # Logica de venda atomica ACID e cancelamento
│   │   ├── backoffice/                  # Servicos de catalogo, salas e agendamento
│   │   ├── auth/                        # RBAC (ATENDENTE/GERENTE) e JWT com tenant_id
│   │   ├── tenancy/                     # Prisma Client Extension com filtro row-level
│   │   └── ocupacao/                    # Calculo e agregacoes em tempo real
│   ├── components/                      # Componentes visuais Tailwind reutilizaveis
│   └── lib/                             # Clientes de infraestrutura (Prisma, Axiom, Crypto)
├── prisma/
│   ├── schema.prisma                    # Schema relacional oficial com 9 entidades
│   └── migrations/                      # Historico de migrations com trigger append-only
├── tests/                               # Suites de testes automatizados
│   ├── unit/                            # Testes unitarios de dominio
│   ├── integration/                     # Teste de concorrencia ACID (50 threads)
│   └── e2e/                             # Testes ponta a ponta com Playwright
├── .env.example                         # Variaveis de ambiente documentadas
└── README.md                            # Instrucoes de execucao local e badges de CI
```

---

## 4. Regras de Contribuicao e Governanca de Branches

1. **Branch `main`:** Protegida. So recebe merges via Pull Request aprovado e com CI passando.
2. **Branch `develop`:** Branch de integracao continua da equipe.
3. **Branches de Feature:** Padrao `feat/nome-da-feature` ou `docs/cap-XX-descricao`.
4. **Commits Semanticos:** `feat:`, `fix:`, `docs:`, `chore:`, `test:`, `refactor:`.
