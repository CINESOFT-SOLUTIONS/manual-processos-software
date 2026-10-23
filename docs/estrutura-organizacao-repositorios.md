# 🏛️ Estrutura e Padrões da Organização GitHub — CineDoom
### CineSoft Solutions | Engenharia de Processos de Software (ISO/IEC/IEEE 12207:2021)

Este documento estabelece o modelo de governança, convenções de versionamento e a arquitetura de repositórios da organização **CineSoft Solutions** no GitHub. A separação entre o repositório de **Processos/Manual** e o repositório de **Software Real** garante rastreabilidade estrita entre a teoria normativa e a evidência de engenharia executável.

---

## 1. Visão Geral da Organização no GitHub

```text
github.com/cinesoft-solutions/
├── .github                 # (Opcional) Perfil público da organização e templates globais
├── manual-processos        # Repositório de governança, Manual ISO 12207, LaTeX e Slides
└── cinedoom-app            # Repositório do software real (Next.js + Prisma + Neon + Vercel)
```

---

## 2. Repositório 1: `manual-processos` (Repositório Atual)

Este repositório é a **fonte da verdade normativa e metodológica**. Ele contém todo o histórico de decisões, documentos formais de processo e os compiladores de PDF acadêmicos.

### 2.1 Estrutura de Diretórios Recomendada

```text
manual-processos/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── revisao_capitulo.md          # Template para revisão de capítulo do manual (Cap. 1 a 5)
│   │   ├── auditoria_qualidade.md       # Template para laudos de auditoria interna / conformidade
│   │   └── config.yml                   # Configuração e links úteis para issues
│   ├── workflows/
│   │   └── compilar-docs.yml            # CI no GitHub Actions que compila os PDFs via Tectonic
│   ├── PULL_REQUEST_TEMPLATE.md         # Checklist de aprovação com impacto no PDW
│   └── CODEOWNERS                       # Governança de revisores conforme a matriz RACI
├── assets/                              # Diagramas, evidências visuais e modelos
│   ├── diagramas/                       # Fontes .puml, .bpmn e exportações .png/.svg
│   │   ├── c4-contexto.png
│   │   ├── c4-container.png
│   │   └── fluxo-venda-bpmn.png
│   └── evidencias/                      # Prints de testes reais, pipelines verdes e release
│       ├── pipeline-ci-passando.png
│       └── teste-vitest-venda-dupla.png
├── docs/                                # Base de conhecimento e governança
│   ├── constituicao/
│   │   └── project-definition-workbook.md # PDW: Fonte única da verdade das decisões
│   ├── norma-iso/                       # Cópia em PDF e transcrição da ISO/IEC/IEEE 12207
│   ├── validacoes/                      # Laudos formais de auditoria da IA por parte (0 a 4)
│   ├── rascunhos/                       # Versões de trabalho preliminares
│   ├── estrutura-minima-manual.md       # Roteiro oficial cobrado pela Profa. Dra. Juliana
│   └── rastreabilidade-matriz.md        # Matriz geral: Requisito -> ADR -> Código -> Teste -> Release
├── prompts/                             # Catálogo de prompts estruturados por bloco temático
│   ├── auditor-de-qualidade.md
│   └── parte-00/ a parte-04/
├── scripts/                             # Scripts de automação local
│   └── compilar.sh                      # Compilação unificada com Tectonic
├── slides_latex/                        # Apresentação oral da banca (Beamer tema UFG/INF)
│   ├── apresentacao-manual.tex
│   ├── beamerthemeUfg.sty
│   └── lib/
├── trabalho_latex/                      # Relatório acadêmico formatado nas normas ABNT
│   └── manual-processos-software.tex
├── manual-processos-software.md         # Documento consolidado oficial para leitura web
├── fluxo-trabalho.md                    # Guia de contribuição da equipe
├── LICENSE                              # Licença do projeto (ex: MIT ou proprietária CineSoft)
└── README.md                            # Apresentação do projeto, integrantes e links úteis
```

---

## 3. Repositório 2: `cinedoom-app` (Software Real)

Este repositório contém a **implementação do software**, configurado para deploy automático na **Vercel** conectado ao banco **Neon (PostgreSQL)**.

### 3.1 Estrutura de Diretórios Recomendada (Next.js + Prisma)

```text
cinedoom-app/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── feature.md                   # Template com obrigatoriedade de vincular ao RF-XX
│   │   └── bug.md                       # Template de registro de defeito (Cláusula 6.3.5)
│   ├── workflows/
│   │   └── ci.yml                       # Pipeline de Lint, TypeCheck e Testes Automatizados
│   └── PULL_REQUEST_TEMPLATE.md         # Checklist de testes e rastreabilidade ao manual
├── prisma/
│   ├── schema.prisma                    # Modelagem relacional: Movie, Room, Seat, Session, Ticket
│   ├── migrations/                      # Histórico de alterações do banco (PostgreSQL)
│   └── seed.ts                          # Script de carga inicial (filmes, salas e assentos demo)
├── public/
│   ├── posters/                         # Pôsteres dos filmes da demonstração
│   └── favicon.ico
├── src/
│   ├── app/                             # Next.js App Router
│   │   ├── layout.tsx                   # Layout global responsivo com navbar e perfil de usuário
│   │   ├── page.tsx                     # Vitrine: Lista de filmes em cartaz e sessões
│   │   ├── sessions/
│   │   │   └── [id]/
│   │   │       └── page.tsx             # TELA PRINCIPAL: Mapa visual interativo de assentos
│   │   └── api/                         # Backend Serverless REST
│   │       ├── sessions/
│   │       │   └── [id]/
│   │       │       └── route.ts         # GET: Estado dos assentos da sessão (para polling)
│   │       └── tickets/
│   │           ├── buy/route.ts         # POST: Venda atômica com trava de concorrência (RF-07)
│   │           └── cancel/route.ts      # POST: Cancelamento que libera assento (RF-08)
│   ├── components/                      # Componentes visuais modulares
│   │   ├── SeatMap.tsx                  # Grid de assentos interativo (Verde, Vermelho, Amarelo)
│   │   ├── OccupancyBar.tsx             # Barra de ocupação da sessão (% e total de lotação)
│   │   ├── TicketModal.tsx              # Comprovante/ingresso gerado com QR Code fictício
│   │   └── UserRoleSwitcher.tsx         # Alternador rápido de perfil: [Atendente | Gerente]
│   └── lib/
│       ├── prisma.ts                    # Instância singleton do Prisma Client
│       └── ticket-service.ts            # Regra de negócio isolada de transação e auditoria
├── tests/                               # Testes automatizados (Vitest)
│   ├── unit/
│   │   └── seat-calculation.test.ts     # Teste de cálculo de ocupação
│   └── integration/
│       ├── RF07-venda-dupla.test.ts     # TESTE CHAVE: Tenta comprar mesmo assento 2x concorrente
│       └── RF08-cancelamento.test.ts    # Teste de liberação imediata de assento
├── docs/
│   └── adr/                             # Decisões de arquitetura espelhadas
│       ├── ADR-001-monolito-modular.md
│       ├── ADR-004-postgresql-neon.md
│       └── ADR-005-hospedagem-vercel.md
├── .env.example                         # Exemplo com DATABASE_URL do Neon
├── next.config.mjs
├── package.json
├── tailwind.config.ts
├── tsconfig.json
├── vitest.config.ts
└── README.md                            # Guia de execução local, link da Vercel e badges de CI
```

---

## 4. Patterns e Convenções do GitHub (O "Jeito Pro")

Para demonstrar maturidade perante a banca avaliadora, a equipe deve seguir estas convenções universais:

### 4.1 Estratégia de Branches (GitHub Flow com Release Tags)
- **`main`**: Sempre estável e sincronizada com a produção na **Vercel** (`https://cinedoom.vercel.app`).
- **`develop`**: Branch de integração dos 4 desenvolvedores durante os ciclos de sprint.
- **Branches de trabalho**: Criadas a partir de `develop` e nomeadas obrigatoriamente com o identificador do requisito:
  - `feat/RF-05-agendamento-sessoes`
  - `feat/RF-06-mapa-assentos`
  - `feat/RF-07-venda-atomica`
  - `fix/RF-08-status-cancelamento`
  - `docs/capitulo-05-processos-tecnicos`

### 4.2 Convenção de Commits (Conventional Commits + Rastreabilidade)
Todo commit deve explicitar a ação e a referência ao requisito do manual:
```bash
feat(RF-07): implementa transacao atomica contra venda dupla de assento
fix(RF-08): atualiza estado da cadeira para LIVRE apos cancelamento
test(RF-07): cria teste de concorrencia no Vitest simulando 2 compras simultaneas
docs(cap-05): adiciona print do pipeline do GitHub Actions como evidencia de CI
ci(github-actions): adiciona step de execucao do vitest no pull request
```

### 4.3 Padrão de Pull Request Template (`.github/PULL_REQUEST_TEMPLATE.md`)
Ao abrir um PR no repositório de software, o desenvolvedor deve preencher:

```markdown
## 📌 Requisito Associado
- [ ] RF-XX (ex: RF-07 - Registrar Venda)

## 📋 O que foi feito?
- Descrição clara da alteração realizada.

## 🧪 Evidências de Teste
- [ ] Testes unitários/integração implementados no Vitest?
- [ ] Pipeline de CI executou com sucesso (Checks verdes)?
- Print da execução do teste ou comportamento na interface.

## 🔗 Impacto no Manual de Processos
- [ ] Houve mudança na arquitetura ou banco? (Se sim, indicar se requer ADR).
- [ ] O critério de aceitação do requisito foi atingido?
```

### 4.4 Tags e Releases Semânticas
No término da implementação do MVP (previsto para ~04/11):
- Criar a tag e Release no GitHub: `v1.0.0-mvp`.
- **Release Notes:** Listar formalmente os requisitos contemplados (`RF-03`, `RF-04`, `RF-05`, `RF-06`, `RF-07`, `RF-08`), o link de deploy na Vercel e os artefatos de teste gerados.

---

## 5. Como Ligar os Dois Repositórios (Rastreabilidade Perfeita)

A professora vai avaliar a **rastreabilidade entre processos e software**. O elo entre os dois repositórios será feito de forma transparente:

1. **No repositório `manual-processos` (Capítulo 5):**
   - Onde o manual falar de **Implementação (5.3)**: coloca o link direto do GitHub para o arquivo [ticket-service.ts](file:///Users/gabrlou/Desktop/manual-processos) e para o commit correspondente.
   - Onde o manual falar de **Testes e Verificação (5.4)**: insere a tabela com o resumo dos testes do Vitest e o print da execução do GitHub Actions.
   - Onde o manual falar de **Transição/Deploy (5.4.4)**: inclui a URL oficial na Vercel e o registro da release `v1.0.0-mvp`.
2. **No repositório `cinedoom-app` (README.md):**
   - No topo do README, colocar a badge:
     `[![Manual de Processos](https://img.shields.io/badge/Manual_de_Processos-ISO_12207-blue)](https://github.com/cinesoft-solutions/manual-processos)`
   - Link explícito para o PDF do manual e para o PDW.

---

## 6. Pipeline de CI Mínimo Recomendado (`.github/workflows/ci.yml`)

No repositório `cinedoom-app`, basta colocar este arquivo de automação para rodar a cada Pull Request:

```yaml
name: CineDoom CI - Quality & Traceability Gate

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout do Código
        uses: actions/checkout@v4

      - name: Configurar Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'

      - name: Instalar Dependências
        run: npm ci

      - name: Validar Schema do Prisma
        run: npx prisma validate

      - name: Executar Lint e TypeCheck
        run: |
          npm run lint
          npm run typecheck

      - name: Executar Testes Automatizados (Vitest)
        run: npm run test:run

      - name: Gerar Build de Produção
        run: npm run build
```

> **Resultado na Apresentação:** Mostrar esse pipeline verde no GitHub Actions prova cabalmente o atendimento aos processos de **Verificação (6.4.9)**, **Integração de Software (7.1.4)** e **Garantia da Qualidade (6.2.5)** da ISO/IEC/IEEE 12207!
