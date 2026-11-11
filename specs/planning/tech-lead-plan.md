---
document_id: SPEC-CINEDOOM-TECHLEAD-PLAN-001
version: "2.0.0"
date: "2026-11-05"
status: "Aprovado e Consolidado"
standard: "ABNT NBR ISO/IEC/IEEE 12207:2021 (Cláusulas 6.3.1 e 6.3.2 — Planejamento e Controle do Projeto)"
title: "Plano Técnico de Implementação (TechLead) — Decomposição em 23 Tarefas — CineDoom"
---

# Plano Técnico de Implementação (TechLead) — Decomposição em 23 Tarefas — CineDoom

> **Documento Técnico Oficial — CineSoft Solutions (UFG/INF — Processos de Software 2026/1)**
> Rastreabilidade direta com [`cinedoom-spec.md`](../cinedoom-spec.md) (`RF-01` a `RF-18`, `RNF-01` a `RNF-06`, `RN-01` a `RN-12`, `CA-01` a `CA-14`) e [`sprints-e-backlog.md`](sprints-e-backlog.md).

## 1. Resumo Executivo

Decomposição técnica da implementação da plataforma **CineDoom** em **23 tarefas de engenharia (`TASK-1` a `TASK-23`)**, totalizando **116 horas estimadas**. O plano cobre a configuração do monorepo, esquema relacional ACID multi-tenant no Supabase PostgreSQL, autenticação e autorização RBAC (`ATENDENTE`, `GERENTE` e `CLIENTE`), proteção criptográfica de PII/LGPD (`HMAC-SHA256` + `AES-256-GCM`), módulos de Gestão (Back-office), Bilheteria com trava atômica (`SELECT FOR UPDATE`), cancelamento auditável *append-only*, Painel de Ocupação, Portal do Cliente com reservas online e expiração *Just-in-Time*, observabilidade no Axiom e pirâmide de testes automatizados (Vitest + Playwright).

---

## 2. Métricas de Engenharia

- **Total de Tarefas Técnicas:** 23 (`TASK-1` a `TASK-23`)
- **Esforço Total Estimado:** 116,0 horas
- **Caminho Crítico:** `TASK-1` $\to$ `TASK-2` $\to$ `TASK-3` $\to$ `TASK-7` $\to$ `TASK-8` $\to$ `TASK-9` $\to$ `TASK-10` $\to$ `TASK-11` $\to$ `TASK-19`
- **Grupos de Execução Paralela:** 5 grupos

---

## 3. Catálogo de Tarefas Técnicas (`TASK-1` a `TASK-23`)

| ID | Título da Tarefa | Papel / Especialidade | Estimativa (h) | Depende de | Requisitos (`RF`/`RNF`) | Critérios de Aceite (`CA` / `AC`) |
|----|------------------|-----------------------|----------------|------------|-------------------------|-----------------------------------|
| **TASK-1** | Estruturação do projeto (*scaffolding*), Clean Architecture e configuração de monorepo | DevOps | 4 | — | `RNF-06` | — |
| **TASK-2** | Modelagem do esquema de dados e migrações Prisma (Supabase PostgreSQL) | DataArchitect | 6 | TASK-1 | `RNF-02`, `RNF-03` | `CA-04 (AC-4)`, `CA-08 (AC-8)` |
| **TASK-3** | Extensão Prisma multi-tenant — isolamento lógico por linha (`tenant_id`) | SoftwareArchitect | 5 | TASK-2 | `RNF-03`, `RN-12` | `CA-04 (AC-4)` |
| **TASK-4** | Autenticação e controle de acesso RBAC via NextAuth.js | Security | 6 | TASK-2 | `RF-01`, `RN-01` | `CA-05 (AC-5)` |
| **TASK-5** | Proteção de PII/LGPD — módulo de CPF com `HMAC-SHA256` + `AES-256-GCM` | Security | 5 | TASK-2 | `RF-09`, `RNF-03`, `RN-07` | `CA-06 (AC-6)` |
| **TASK-6** | Gestão (Back-office) — CRUD de catálogo de filmes | SoftwareArchitect | 5 | TASK-3, TASK-4 | `RF-02`, `RN-02` | `CA-05 (AC-5)`, `CA-08 (AC-8)` |
| **TASK-7** | Gestão (Back-office) — CRUD de salas e layout físico de poltronas | SoftwareArchitect | 6 | TASK-3, TASK-4 | `RF-03`, `RN-02` | `CA-05 (AC-5)`, `CA-08 (AC-8)` |
| **TASK-8** | Gestão (Back-office) — CRUD de sessões e pré-população de `SessionSeat` | SoftwareArchitect | 5 | TASK-6, TASK-7 | `RF-04`, `RN-03`, `RN-04` | `CA-05 (AC-5)`, `CA-08 (AC-8)` |
| **TASK-9** | Bilheteria — Mapa de assentos interativo com polling a cada 2s | SoftwareArchitect | 5 | TASK-8, TASK-17 | `RF-05`, `RNF-01` | `CA-02 (AC-2)` |
| **TASK-10** | Bilheteria — Venda presencial ACID anti-double-booking (`SELECT FOR UPDATE`) | SoftwareArchitect | 8 | TASK-5, TASK-9 | `RF-06`, `RF-07`, `RNF-02`, `RN-05` | `CA-01 (AC-1)`, `CA-06 (AC-6)` |
| **TASK-11** | Bilheteria — Cancelamento auditável com tabela *append-only* | SoftwareArchitect | 4 | TASK-10 | `RF-08`, `RN-06` | `CA-03 (AC-3)`, `CA-05 (AC-5)` |
| **TASK-12** | Gestão — Painel de ocupação em tempo real do Gerente | SoftwareArchitect | 4 | TASK-8, TASK-4 | `RF-10` | `CA-05 (AC-5)`, `CA-07 (AC-7)` |
| **TASK-13** | Identidade — Gestão de usuários Atendentes pelo Gerente | SoftwareArchitect | 4 | TASK-4 | `RF-01`, `RN-01` | `CA-05 (AC-5)` |
| **TASK-14** | Conformidade LGPD — Endpoint de anonimização *in-place*, DPIA e DPO | Compliance | 4 | TASK-5 | `RF-09`, `RNF-03` | `CA-06 (AC-6)` |
| **TASK-15** | Observabilidade — Axiom Log Drain, retenção de 365 dias e sanitização de PII | DevOps | 3 | TASK-1 | `RF-11`, `RNF-03` | `CA-03 (AC-3)` |
| **TASK-16** | Pipeline CI/CD GitHub Actions, `ESLint import/no-cycle` e *preview environments* | DevOps | 4 | TASK-1 | `RNF-05`, `RNF-06` | — |
| **TASK-17** | Interface (UI) — Sistema de design, mapa interativo e fluxos responsivos | UI | 6 | TASK-1 | `RNF-04`, `RNF-05` | `CA-01 (AC-1)`, `CA-02 (AC-2)` |
| **TASK-18** | Segurança — Suíte automatizada de isolamento cross-tenant (500 cenários) | Security | 4 | TASK-3, TASK-10 | `RNF-03`, `RN-12` | `CA-04 (AC-4)` |
| **TASK-19** | Qualidade (QA) — Testes de integração concorrente (50 threads), E2E e matriz de navegadores | QA | 6 | TASK-10, TASK-11, TASK-12, TASK-17 | `RNF-01`, `RNF-02`, `RNF-05` | `CA-01 (AC-1)`, `CA-02 (AC-2)`, `CA-03 (AC-3)`, `CA-07 (AC-7)` |
| **TASK-20** | Provisionamento controlado de tenants e documentação de *onboarding* | DevOps | 2 | TASK-4, TASK-13 | `RES-03` | — |
| **TASK-21** | Portal do Cliente — Catálogo público, grade de sessões e reserva atômica ACID | SoftwareArchitect | 5 | TASK-8, TASK-17 | `RF-12`, `RF-13`, `RF-18`, `RN-08`, `RN-11` | `CA-09 (AC-9)`, `CA-14 (AC-14)` |
| **TASK-22** | Portal do Cliente — Autenticação `CLIENTE`, área "Minhas Reservas" e cancelamento web | Security | 4 | TASK-4, TASK-5, TASK-21 | `RF-14`, `RF-16`, `RN-09` | `CA-10 (AC-10)`, `CA-12 (AC-12)` |
| **TASK-23** | Notificação por e-mail transacional e baixa presencial de reservas no balcão | SoftwareArchitect | 5 | TASK-10, TASK-21 | `RF-15`, `RF-17`, `RN-10` | `CA-11 (AC-11)`, `CA-13 (AC-13)` |

---

## 4. Detalhamento das Tarefas Técnicas

### TASK-1. Estruturação do projeto (*scaffolding*), Clean Architecture e configuração de monorepo
- **Especialidade:** DevOps | **Estimativa:** 4 h | **Requisitos:** `RNF-06`
- Configuração do Next.js 14 App Router com `pnpm`, estrutura de diretórios em *Feature Slices* (`bilheteria`, `catalogo`, `identidade`, `ocupacao`, `portal`, `compradores`, `tenancy`), `.env.example` documentado, Tailwind CSS, TypeScript em modo estrito (`strict: true`) e regra `ESLint import/no-cycle` para garantir zero dependências circulares entre módulos.

### TASK-2. Modelagem do esquema de dados e migrações Prisma (Supabase PostgreSQL)
- **Especialidade:** DataArchitect | **Estimativa:** 6 h | **Depende de:** TASK-1 | **Critérios:** `CA-04 (AC-4)`, `CA-08 (AC-8)`
- Modelagem completa do esquema Prisma com as 11 entidades (`Tenant`, `User`, `Film`, `Room`, `Seat`, `Session`, `SessionSeat`, `Reservation`, `Ticket`, `Buyer`, `CancellationAudit`); coluna `tenant_id` em todas as entidades de domínio; trigger PostgreSQL `BEFORE UPDATE OR DELETE` em `cancellation_audits` para garantir imutabilidade; migração inicial para o Supabase PostgreSQL.

### TASK-3. Extensão Prisma multi-tenant — isolamento lógico por linha (`tenant_id`)
- **Especialidade:** SoftwareArchitect | **Estimativa:** 5 h | **Depende de:** TASK-2 | **Critérios:** `CA-04 (AC-4)`
- Implementação da *Prisma Client Extension* que injeta `WHERE tenant_id = :tenantId` automaticamente em todas as consultas de entidades de negócio; propagação do contexto de locatário via `AsyncLocalStorage` a partir do middleware Next.js; testes unitários de isolamento por módulo (`RN-12`).

### TASK-4. Autenticação e controle de acesso RBAC via NextAuth.js
- **Especialidade:** Security | **Estimativa:** 6 h | **Depende de:** TASK-2 | **Critérios:** `CA-05 (AC-5)`
- Configuração do NextAuth.js com `CredentialsProvider`; inclusão de `role` (`ATENDENTE`, `GERENTE`, `CLIENTE`) e `tenant_id` no JWT; middleware Next.js protegendo rotas por perfil e retornando `HTTP 403 Forbidden` para acessos não autorizados (`RF-01`, `RN-01`).

### TASK-5. Proteção de PII/LGPD — módulo de CPF com `HMAC-SHA256` + `AES-256-GCM`
- **Especialidade:** Security | **Estimativa:** 5 h | **Depende de:** TASK-2 | **Critérios:** `CA-06 (AC-6)`
- Implementação do `CryptoService`: `HMAC-SHA256` com chave secreta server-side (`CINEDOOM_CPF_HMAC_KEY`) para busca indexada de CPF; `AES-256-GCM` (`CPF_ENCRYPTION_KEY`) para armazenamento cifrado; validação obrigatória do carimbo de consentimento LGPD (`lgpd_consent_at`); testes unitários de cifragem, decifragem e determinismo de hash (`RF-09`, `RN-07`).

### TASK-6. Gestão (Back-office) — CRUD de catálogo de filmes
- **Especialidade:** SoftwareArchitect | **Estimativa:** 5 h | **Depende de:** TASK-3, TASK-4 | **Critérios:** `CA-05 (AC-5)`, `CA-08 (AC-8)`
- Route Handlers e serviços para criar, editar e listar filmes (`RF-02`, `RN-02`); validação Zod com erros descritivos por campo (`HTTP 422`); acesso restrito ao perfil `GERENTE` e isolamento por `tenant_id`.

### TASK-7. Gestão (Back-office) — CRUD de salas e layout físico de poltronas
- **Especialidade:** SoftwareArchitect | **Estimativa:** 6 h | **Depende de:** TASK-3, TASK-4 | **Critérios:** `CA-05 (AC-5)`, `CA-08 (AC-8)`
- CRUD de `Room` e geração automática em lote das poltronas (`Seat`) conforme fileiras e colunas configuradas (`RF-03`, `RN-02`); validação de campos obrigatórios e proteção RBAC para `GERENTE`.

### TASK-8. Gestão (Back-office) — CRUD de sessões e pré-população de `SessionSeat`
- **Especialidade:** SoftwareArchitect | **Estimativa:** 5 h | **Depende de:** TASK-6, TASK-7 | **Critérios:** `CA-05 (AC-5)`, `CA-08 (AC-8)`
- CRUD de `Session` vinculando filme, sala, horário e preço (`RF-04`); transação Prisma que pré-popula `SessionSeat` (`status = 'AVAILABLE'`) para cada poltrona da sala (`RN-04`); validação de conflito de agenda na mesma sala (`RN-03`, `HTTP 409`).

### TASK-9. Bilheteria — Mapa de assentos interativo com polling a cada 2s
- **Especialidade:** SoftwareArchitect | **Estimativa:** 5 h | **Depende de:** TASK-8, TASK-17 | **Critérios:** `CA-02 (AC-2)`
- Endpoint `GET /api/sessoes/[id]/assentos` retornando o estado atualizado das poltronas da sessão; componente React com `setInterval(2000ms)` atualizando visualmente poltronas disponíveis, reservadas e vendidas em até 2 segundos (`RF-05`, `RNF-01`).

### TASK-10. Bilheteria — Venda presencial ACID anti-double-booking (`SELECT FOR UPDATE`)
- **Especialidade:** SoftwareArchitect | **Estimativa:** 8 h | **Depende de:** TASK-5, TASK-9 | **Critérios:** `CA-01 (AC-1)`, `CA-06 (AC-6)`
- Transação Prisma com trava pessimista `SELECT FOR UPDATE` em `SessionSeat` (`RF-06`, `RN-05`); persistência atômica de `Ticket` e `Buyer` (com CPF protegido via `TASK-5`); retorno imediato de `HTTP 409 Conflict` para disputas concorrentes; teste de integração com 50 requisições paralelas disputando a mesma poltrona com zero double-bookings (`RNF-02`).

### TASK-11. Bilheteria — Cancelamento auditável com tabela *append-only*
- **Especialidade:** SoftwareArchitect | **Estimativa:** 4 h | **Depende de:** TASK-10 | **Critérios:** `CA-03 (AC-3)`, `CA-05 (AC-5)`
- Endpoint de cancelamento que grava registro imutável em `cancellation_audits` (ID do ingresso, ID do operador, timestamp UTC, `tenant_id` e motivo obrigatório) **antes** de liberar a poltrona para `AVAILABLE` (`RF-08`, `RN-06`).

### TASK-12. Gestão — Painel de ocupação em tempo real do Gerente
- **Especialidade:** SoftwareArchitect | **Estimativa:** 4 h | **Depende de:** TASK-8, TASK-4 | **Critérios:** `CA-05 (AC-5)`, `CA-07 (AC-7)`
- Painel gerencial listando as sessões do dia corrente com cálculo de poltronas vendidas, reservadas, capacidade total e percentual de ocupação isolado por `tenant_id` (`RF-10`).

### TASK-13. Identidade — Gestão de usuários Atendentes pelo Gerente
- **Especialidade:** SoftwareArchitect | **Estimativa:** 4 h | **Depende de:** TASK-4 | **Critérios:** `CA-05 (AC-5)`
- CRUD para criação, listagem e desativação de contas com perfil `ATENDENTE` vinculadas ao `tenant_id` do Gerente autenticado (`RF-01`, `RN-01`).

### TASK-14. Conformidade LGPD — Endpoint de anonimização *in-place*, DPIA e DPO
- **Especialidade:** Compliance | **Estimativa:** 4 h | **Depende de:** TASK-5 | **Critérios:** `CA-06 (AC-6)`
- Implementação de *soft-anonymization in-place* na entidade `Buyer` (`POST /api/titulares/anonimizar`, Art. 18 da LGPD, `ADR-009`), preservando a integridade referencial dos ingressos emitidos; consolidação do relatório DPIA/RIPD e definição de governança Controlador/Operador.

### TASK-15. Observabilidade — Axiom Log Drain, retenção de 365 dias e sanitização de PII
- **Especialidade:** DevOps | **Estimativa:** 3 h | **Depende de:** TASK-1 | **Critérios:** `CA-03 (AC-3)`
- Configuração de logs estruturados JSON enviados ao Axiom com retenção de 365 dias (`RF-11`); mascaramento automático de CPF e e-mail nos logs (`RNF-03`); alertas para anomalias e tentativas de acesso cross-tenant.

### TASK-16. Pipeline CI/CD GitHub Actions, `ESLint import/no-cycle` e *preview environments*
- **Especialidade:** DevOps | **Estimativa:** 4 h | **Depende de:** TASK-1 | **Requisitos:** `RNF-05`, `RNF-06`
- Configuração do workflow GitHub Actions executando lint (`import/no-cycle`), verificação de tipos TypeScript, suíte Vitest e matriz Playwright (Chromium + Firefox em `1024x768`); integração com ambientes de *preview* da Vercel.

### TASK-17. Interface (UI) — Sistema de design, mapa interativo e fluxos responsivos
- **Especialidade:** UI | **Estimativa:** 6 h | **Depende de:** TASK-1 | **Critérios:** `CA-01 (AC-1)`, `CA-02 (AC-2)`
- Construção dos componentes visuais em Tailwind CSS seguindo os tokens de design e diretrizes WCAG 2.1 AA (`RNF-04`, `RNF-05`): mapa de poltronas interativo, modal de venda com consentimento LGPD, telas de gestão e portal do espectador.

### TASK-18. Segurança — Suíte automatizada de isolamento cross-tenant (500 cenários)
- **Especialidade:** Security | **Estimativa:** 4 h | **Depende de:** TASK-3, TASK-10 | **Critérios:** `CA-04 (AC-4)`
- Implementação da bateria automatizada de **500 cenários de isolamento cross-tenant** (`tests/unit/security-cross-tenant-suite.test.ts`), validando bloqueio de BOLA, falsificação de cabeçalhos, adulteração de parâmetros/payloads, *Prisma Tenancy Extension* e concorrência em `AsyncLocalStorage` (`RNF-03`, `RN-12`).

### TASK-19. Qualidade (QA) — Testes de integração concorrente (50 threads), E2E e matriz de navegadores
- **Especialidade:** QA | **Estimativa:** 6 h | **Depende de:** TASK-10, TASK-11, TASK-12, TASK-17 | **Critérios:** `CA-01` a `CA-07`
- Consolidação dos testes de integração concorrente (50 threads para venda presencial e reserva web), testes de imutabilidade de auditoria, cálculos de ocupação e jornadas E2E no Playwright (`CT-01` a `CT-26`).

### TASK-20. Provisionamento controlado de tenants e documentação de *onboarding*
- **Especialidade:** DevOps | **Estimativa:** 2 h | **Depende de:** TASK-4, TASK-13 | **Restrições:** `RES-03`
- Script CLI interno (`pnpm run provisionar-tenant`) para cadastro controlado de novos cinemas clientes e conta inicial de `GERENTE`; documentação de *onboarding* rápido (< 30 min) e runbooks de operação.

### TASK-21. Portal do Cliente — Catálogo público, grade de sessões e reserva atômica ACID
- **Especialidade:** SoftwareArchitect | **Estimativa:** 5 h | **Depende de:** TASK-8, TASK-17 | **Critérios:** `CA-09 (AC-9)`, `CA-14 (AC-14)`
- Implementação das rotas do Portal do Cliente (`/portal`, `/portal/sessoes/[id]`), fluxo de reserva online com trava `SELECT FOR UPDATE` (`status = 'RESERVED'`), validação de antecedência mínima de 60 minutos (`RN-08`), geração do código `CD-XXXX` (`RF-13`) e expiração *Just-in-Time* (`RF-18`, `RN-11`).

### TASK-22. Portal do Cliente — Autenticação `CLIENTE`, área "Minhas Reservas" e cancelamento web
- **Especialidade:** Security | **Estimativa:** 4 h | **Depende de:** TASK-4, TASK-5, TASK-21 | **Critérios:** `CA-10 (AC-10)`, `CA-12 (AC-12)`
- Expansão do NextAuth.js para o papel `CLIENTE`, cadastro de espectador com proteção LGPD (`RF-14`), painel autenticado "Minhas Reservas" e rota `POST /api/portal/reservas/[id]/cancelar` com proteção anti-IDOR e liberação imediata das poltronas (`RF-16`, `RN-09`).

### TASK-23. Notificação por e-mail transacional e baixa presencial de reservas no balcão
- **Especialidade:** SoftwareArchitect | **Estimativa:** 5 h | **Depende de:** TASK-10, TASK-21 | **Critérios:** `CA-11 (AC-11)`, `CA-13 (AC-13)`
- Implementação do `NotificationService` para disparo do voucher por e-mail (`RF-15`) e do fluxo de balcão (`CounterService`) para busca de reservas por código `CD-XXXX` ou CPF e conversão atômica em ingresso vendido (`SOLD`) (`RF-17`, `RN-10`).

---

## 5. Estratégia de Paralelização de Engenharia

- **Grupo Paralelo 1 (Fundação, UI e CI/CD):** `TASK-15` + `TASK-16` + `TASK-17`
- **Grupo Paralelo 2 (Segurança, Tenancy e Identidade):** `TASK-3` + `TASK-4` + `TASK-5`
- **Grupo Paralelo 3 (Cadastros Base do Back-Office):** `TASK-6` + `TASK-7`
- **Grupo Paralelo 4 (Gestão Operacional e Governança LGPD):** `TASK-12` + `TASK-13` + `TASK-14`
- **Grupo Paralelo 5 (Portal do Cliente, Segurança Cross-Tenant e Onboarding):** `TASK-18` + `TASK-20` + `TASK-21` + `TASK-22` + `TASK-23`
