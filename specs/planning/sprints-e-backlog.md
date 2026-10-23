# Planejamento de Sprints, Backlog e Cronograma de Execução

**Projeto:** CineDoom — Plataforma SaaS B2B de Gestão de Cinemas  
**Organização:** CineSoft Solutions (`CINESOFT-SOLUTIONS`)  
**Norma de Referência:** ABNT NBR ISO/IEC/IEEE 12207:2021 (Cláusula 6.3.1 — Processo de Planejamento do Projeto)  
**Período de Execução:** 23 de Outubro de 2026 a 12 de Novembro de 2026 (Data da Defesa Final)  
**Quadro Kanban Oficial:** [GitHub Projects v2 #1 — CineDoom](https://github.com/orgs/CINESOFT-SOLUTIONS/projects/1)

---

## 1. Visão Geral da Metodologia e Ciclo de Vida

O desenvolvimento do **CineDoom** e a confecção do **Manual de Processos de Software** seguem um modelo de ciclo de vida **iterativo-incremental** estruturado em duas trilhas paralelas e integradas:

1. **Trilha A — Engenharia de Produto (`cinedoom-app`):** Implementação do sistema de bilheteria presencial atômica, mapa de assentos com polling de 2s, cancelamento auditável por trigger PostgreSQL, catálogo, sessões e painel gerencial de ocupação.
2. **Trilha B — Processos e Governança (`manual-processos-software`):** Consolidação dos 5 capítulos normativos do manual em Docs-as-Code (Markdown $\to$ LaTeX/Tectonic), confecção do relatório técnico ABNT e elaboração dos slides Beamer oficiais INF/UFG para a defesa perante a banca examinadora.

---

## 2. Matriz de Atribuição de Responsabilidades da Equipe (RACI)

A equipe é composta por 4 engenheiros de software, com atribuições divididas conforme especialidade técnica e governança:

| Membro | Usuário GitHub | Papel no Projeto | Foco Principal | Responsabilidade Primária |
| :--- | :--- | :--- | :--- | :---: |
| **Gabriel Lourenço** | `@gabrlou` | TechLead & Lead Software Architect | Núcleo do app, motor ACID de bilheteria, isolamento multi-tenant, segurança e testes de concorrência. | 12 issues (`app`) |
| **Carlos Eduardo** | `@carloseduduu` | Backend Engineer & DevOps Lead | Criptografia PII/LGPD, CRUDs de backoffice (filmes, salas, sessões), observabilidade Axiom e pipeline CI/CD. | 11 issues (`app`) |
| **Kayque Vicente** | `@K4yquee` | Process Engineer & QA Lead | Processos organizacionais (RACI), gerenciamento técnico (riscos e 11 ADRs), V&V e diagramação LaTeX/Beamer. | 5 issues (`docs`) |
| **Yury Nogueira** | `@YuryNog` | Requirements Engineer & Compliance | Apresentação do software, acordos de aquisição/fornecimento, engenharia de requisitos, arquitetura C4 e STRIDE/LGPD. | 5 issues (`docs`) |

---

## 3. Estrutura Temporal das Sprints (Roadmap)

O cronograma total compreende 21 dias corridos, divididos em 3 Sprints funcionais e 1 Marco de Apresentação:

```
2026-10-23                 2026-10-28                 2026-11-04                 2026-11-11     2026-11-12
    |--------- Sprint 1 --------|--------- Sprint 2 --------|--------- Sprint 3 --------|--- Marco ---|
       Fundação & Modelagem        Core Business & Backoffice   Auditoria, QA & LaTeX        Defesa
```

- **Sprint 1 (23/10 a 28/10):** Fundação técnica, setup Next.js/Tailwind, banco Prisma/Neon, observabilidade Axiom, apresentação inicial e governança ISO (Cap. 1 a 3).
- **Sprint 2 (28/10 a 04/11):** Multi-tenancy, autenticação RBAC, criptografia PII, CRUDs de catálogo/salas/sessões, bilheteria atômica ACID (AC-1) e engenharia de requisitos/arquitetura C4 (Cap. 4 e 5.1/5.2).
- **Sprint 3 (04/11 a 11/11):** Cancelamento auditável (AC-3), painel gerencial (AC-7), suíte cross-tenant (AC-4), testes de concorrência com 50 threads, V&V, relatório ABNT LaTeX e slides Beamer.
- **Marco Final (12/11/2026):** Apresentação oral e defesa perante a banca examinadora da Profa. Dra. Juliana Pereira de Souza Zinader.

---

## 4. Backlog Detalhado por Trilha de Execução

### 4.1. Trilha A: Engenharia de Software (`cinedoom-app`) — 23 Issues

| Issue | Título da Tarefa | Responsável | Data Início | Data Término | Dependência | Critério de Aceite |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| **#1** | `[FEAT(INFRA)] Project scaffolding & monorepo setup (Next.js 14, Tailwind, TypeScript)` | `@gabrlou` | 2026-10-23 | 2026-10-25 | Nenhuma (Kickoff) | TASK-1 |
| **#2** | `[FEAT(DB)] Database schema Prisma, migrations e setup Neon DB com trigger append-only` | `@gabrlou` | 2026-10-25 | 2026-10-27 | Issue #1 | TASK-2, AC-3 |
| **#15** | `[FEAT(DEVOPS)] Observability — Axiom Log Drain + estrutura de auditoria e mascaramento PII` | `@carloseduduu` | 2026-10-24 | 2026-10-26 | Issue #1 | TASK-15, AC-3 |
| **#16** | `[FEAT(DEVOPS)] CI/CD pipeline, ESLint no-cycle e preview environments com Neon branching` | `@carloseduduu` | 2026-10-26 | 2026-10-28 | Issue #1 | TASK-16 |
| **#17** | `[FEAT(UI)] Design system, componentes Tailwind e mapa interativo de assentos responsivo` | `@gabrlou` | 2026-10-26 | 2026-10-29 | Issue #1 | TASK-17, AC-1, AC-2 |
| **#3** | `[FEAT(CORE)] Multi-tenancy — Prisma Client Extension com isolamento estrito por tenant_id` | `@gabrlou` | 2026-10-28 | 2026-10-30 | Issue #2 | TASK-3, AC-4 |
| **#4** | `[FEAT(AUTH)] NextAuth.js credentials, JWT com tenant_id e middleware RBAC por role` | `@gabrlou` | 2026-10-29 | 2026-11-01 | Issue #3 | TASK-4, AC-5 |
| **#5** | `[FEAT(SEC)] PII/LGPD — Módulo CPF com HMAC-SHA256 indexado e AES-256-GCM cifrado` | `@carloseduduu` | 2026-10-29 | 2026-10-31 | Issue #2 | TASK-5, AC-6 |
| **#6** | `[FEAT(ADMIN)] Backoffice — CRUD catálogo de filmes com validação Zod e isolamento tenant` | `@carloseduduu` | 2026-11-01 | 2026-11-03 | Issues #3, #4 | TASK-6, AC-5, AC-8 |
| **#7** | `[FEAT(ADMIN)] Backoffice — CRUD salas e layout de assentos com criação em lote` | `@carloseduduu` | 2026-11-01 | 2026-11-04 | Issues #3, #4 | TASK-7, AC-5, AC-8 |
| **#8** | `[FEAT(ADMIN)] Backoffice — CRUD sessões e pré-população atômica de SessionSeat` | `@carloseduduu` | 2026-11-03 | 2026-11-05 | Issues #6, #7 | TASK-8, AC-5, AC-8 |
| **#9** | `[FEAT(CHECKOUT)] Bilheteria — Mapa de assentos com polling HTTP leve a cada 2s` | `@gabrlou` | 2026-11-01 | 2026-11-03 | Issues #8, #17 | TASK-9, AC-2 |
| **#10** | `[FEAT(CHECKOUT)] Bilheteria — Venda atômica ACID com SELECT FOR UPDATE anti-double-booking` | `@gabrlou` | 2026-11-03 | 2026-11-06 | Issues #5, #9 | TASK-10, AC-1, AC-6 |
| **#11** | `[FEAT(CHECKOUT)] Bilheteria — Cancelamento síncrono com trigger de auditoria imutável` | `@gabrlou` | 2026-11-05 | 2026-11-07 | Issue #10 | TASK-11, AC-3, AC-5 |
| **#12** | `[FEAT(ADMIN)] Painel gerencial com cálculo de taxa de ocupação por sessão/sala` | `@gabrlou` | 2026-11-06 | 2026-11-08 | Issues #4, #8 | TASK-12, AC-5, AC-7 |
| **#13** | `[FEAT(AUTH)] Gestão de usuários Atendente pelo Gerente do tenant autenticado` | `@carloseduduu` | 2026-11-05 | 2026-11-07 | Issue #4 | TASK-13, AC-5 |
| **#14** | `[FEAT(SEC)] Compliance LGPD — Anonimização Art. 18, elaboração de DPIA e checklist DPO` | `@carloseduduu` | 2026-11-06 | 2026-11-08 | Issue #5 | TASK-14, AC-6 |
| **#18** | `[FEAT(SEC)] Suíte automatizada de isolamento cross-tenant (500 cenários de teste)` | `@gabrlou` | 2026-11-07 | 2026-11-09 | Issues #3, #10 | TASK-18, AC-4 |
| **#19** | `[FEAT(QA)] Testes de integração concorrente (50 threads), E2E e matriz de navegadores` | `@gabrlou` | 2026-11-08 | 2026-11-10 | Issues #10, #11, #12 | TASK-19, AC-1..7 |
| **#20** | `[FEAT(OPS)] Tenant provisioning manual, onboarding checklist e runbooks de operação` | `@carloseduduu` | 2026-11-08 | 2026-11-10 | Issues #4, #13 | TASK-20 |
| **#21** | `[FEAT(PORTAL)] Portal do Cliente — Catálogo público, mapa interativo e reserva com trava atômica` | `@gabrlou` | 2026-10-31 | 2026-11-03 | Issues #8, #17 | TASK-21, AC-9, AC-14 |
| **#22** | `[FEAT(PORTAL-AUTH)] Autenticação de cliente, painel 'Minhas Reservas' e cancelamento voluntário web` | `@carloseduduu` | 2026-11-01 | 2026-11-04 | Issues #4, #5, #21 | TASK-22, AC-10, AC-12 |
| **#23** | `[FEAT(NOTIFICATION)] Notificação por e-mail transacional e tela de baixa presencial de reserva no balcão` | `@carloseduduu` | 2026-11-04 | 2026-11-07 | Issues #10, #21 | TASK-23, AC-11, AC-13 |

---

### 4.2. Trilha B: Processos e Documentação (`manual-processos-software`) — 10 Issues

| Issue | Título da Tarefa | Responsável | Data Início | Data Término | Base Normativa ISO 12207 |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **#1** | `[DOCS(CAP-1)] Consolidar apresentação do software, escopo e identidade visual` | `@YuryNog` | 2026-10-23 | 2026-10-26 | Cláusula 6.4.1 (Requisitos dos Stakeholders) |
| **#2** | `[DOCS(CAP-2)] Formalizar processos de acordo (aquisição de nuvem e fornecimento B2B SaaS)` | `@YuryNog` | 2026-10-26 | 2026-10-29 | Cláusulas 6.1.1 (Aquisição) e 6.1.2 (Fornecimento) |
| **#3** | `[DOCS(CAP-3)] Estruturar processos organizacionais habilitadores, matriz RACI e gestão da qualidade` | `@K4yquee` | 2026-10-24 | 2026-10-28 | Cláusula 6.2 (Processos Habilitadores) |
| **#4** | `[DOCS(CAP-4)] Mapear plano de gerenciamento técnico, matriz de riscos e as 11 ADRs` | `@K4yquee` | 2026-10-28 | 2026-11-01 | Cláusula 6.3 (Gerenciamento Técnico) |
| **#5** | `[DOCS(CAP-5.1)] Consolidar engenharia de requisitos, critérios de aceite e matriz de rastreabilidade` | `@YuryNog` | 2026-10-29 | 2026-11-02 | Cláusulas 6.4.2 e 6.4.3 (Requisitos) |
| **#6** | `[DOCS(CAP-5.2)] Documentar arquitetura em modelo C4 (Contexto, Contêiner, Componentes) e banco relacional` | `@YuryNog` | 2026-11-02 | 2026-11-05 | Cláusulas 6.4.4 e 6.4.5 (Arquitetura e Design) |
| **#7** | `[DOCS(CAP-5.3)] Elaborar modelagem de ameaças STRIDE e conformidade LGPD` | `@YuryNog` | 2026-11-05 | 2026-11-08 | Cláusula 7.1 e 6.4.8 (Implementação e Segurança) |
| **#8** | `[DOCS(CAP-5.4)] Definir processos de verificação e validação (V&V), transição e descontinuação` | `@K4yquee` | 2026-11-01 | 2026-11-05 | Cláusulas 6.4.9, 6.4.11 e 6.4.14 |
| **#9** | `[DOCS(LATEX)] Diagramar relatório técnico ABNT NBR ISO/IEC/IEEE 12207:2021` | `@K4yquee` | 2026-11-05 | 2026-11-09 | Diretrizes Docentes INF/UFG |
| **#10** | `[DOCS(SLIDES)] Confeccionar apresentação Beamer oficial INF/UFG para a defesa` | `@K4yquee` | 2026-11-08 | 2026-11-11 | Diretrizes Docentes INF/UFG |

---

## 5. Critérios de Qualidade e Definition of Done (DoD)

Para que qualquer issue seja movida para `Done` no Kanban, os seguintes critérios são mandatários:

1. **Código (`cinedoom-app`):**
   - Cobertura de testes unitários e de integração validada no Vitest.
   - Zero dependências circulares (`eslint-plugin-import` com regra `no-cycle`).
   - Tipagem TypeScript estrita sem suppressions (`any` proibido).
   - Teste de concorrência aprovado com 0 double-bookings para fluxos de bilheteria.
   - Review de código aprovado por ao menos 1 par antes do merge em `main`.

2. **Documentação (`manual-processos-software`):**
   - Conformidade estrita com as seções do modelo da Profa. Dra. Juliana Zinader.
   - Vocabulário técnico alinhado à terminologia padronizada das especificações de engenharia e à ISO 12207.
   - Script `./scripts/montar-manual.sh` compila e gera `manual-processos-software.md` sem warnings.
   - Script `./scripts/compilar.sh` compila com sucesso o PDF do relatório ABNT e a apresentação Beamer.

---

## 6. Links e Acesso Rápido

- **Kanban da Organização:** [https://github.com/orgs/CINESOFT-SOLUTIONS/projects/1](https://github.com/orgs/CINESOFT-SOLUTIONS/projects/1)
- **Repositório da Aplicação:** [https://github.com/CINESOFT-SOLUTIONS/cinedoom-app](https://github.com/CINESOFT-SOLUTIONS/cinedoom-app)
- **Repositório do Manual:** [https://github.com/CINESOFT-SOLUTIONS/manual-processos-software](https://github.com/CINESOFT-SOLUTIONS/manual-processos-software)
- **Especificações de Engenharia:** `specs/cinedoom-spec.md`
- **Catálogo de Decisões de Arquitetura:** `specs/adrs/README.md`
