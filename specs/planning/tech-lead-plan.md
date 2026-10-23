---
kind: agent_artifact
feature_id: F-CINEDOOM-PLATAFORMA-B2B-SAAS-C
agent: TechLead
generated_by:
  run_id: run_2026-10-23T03-58-17_eedeb0ce
  session_id: 2026-09-03T15-33-01-hdb88xzyiu
  model: anthropic:claude-sonnet-4-6
generated_at: 2026-10-23T04:57:17.638Z
regenerative: true
title: "[TechLead] CineDoom — plataforma B2B SaaS para cinemas independentes e redes de pequeno/méd"
---

# TechLead — CineDoom — plataforma B2B SaaS para cinemas independentes e redes de pequeno/méd

> Artefato derivado de `.specs/features/F-CINEDOOM-PLATAFORMA-B2B-SAAS-C/spec.md` e gerado pelo agente **TechLead**
> via AI-4SDLC Platform. **Regenerative work product** (não-canonical SDD).
> Não edite manualmente — re-gere via `sdlc resume`.

## Resumo

Decomposição do MVP CineDoom em 23 tasks cobrindo infra/CI, schema ACID multi-tenant, auth RBAC, PII/LGPD (HMAC-SHA256+AES-256-GCM via Vercel Secrets), módulos de backoffice, bilheteria com trava atômica, cancelamento auditável, painel de ocupação, observabilidade Axiom e pirâmide de testes (integração concorrente + E2E Playwright).

## Métricas

- **Total de tasks:** 23
- **Estimativa total:** 116.0 h
- **Caminho crítico:** TASK-1 → TASK-2 → TASK-3 → TASK-7 → TASK-8 → TASK-9 → TASK-10 → TASK-11 → TASK-19
- **Grupos paralelizáveis:** 5

## Tasks

| ID | Título | Agente | Estimativa (h) | Depende de | ACs |
|----|--------|--------|----------------|------------|-----|
| TASK-1 | Project scaffolding & monorepo setup | DevOps | 4 | — | — |
| TASK-2 | Database schema design & Prisma migrations (Neon) | DataArchitect | 6 | TASK-1 | AC-4, AC-8 |
| TASK-3 | Multi-tenant Prisma middleware — row-level isolation | SoftwareArchitect | 5 | TASK-2 | AC-4 |
| TASK-4 | Authentication & RBAC via NextAuth.js | Security | 6 | TASK-2 | AC-5 |
| TASK-5 | PII/LGPD — módulo CPF HMAC-SHA256 + AES-256-GCM | Security | 5 | TASK-2 | AC-6 |
| TASK-6 | Backoffice — CRUD de catálogo de filmes | SoftwareArchitect | 5 | TASK-3, TASK-4 | AC-5, AC-8 |
| TASK-7 | Backoffice — CRUD de salas e layout de assentos | SoftwareArchitect | 6 | TASK-3, TASK-4 | AC-5, AC-8 |
| TASK-8 | Backoffice — CRUD de sessões e pré-população de SessionSeat | SoftwareArchitect | 5 | TASK-6, TASK-7 | AC-5, AC-8 |
| TASK-9 | Bilheteria — mapa de assentos com polling 2s | SoftwareArchitect | 5 | TASK-8, TASK-17 | AC-2 |
| TASK-10 | Bilheteria — venda ACID anti-double-booking | SoftwareArchitect | 8 | TASK-5, TASK-9 | AC-1, AC-6 |
| TASK-11 | Bilheteria — cancelamento auditável | SoftwareArchitect | 4 | TASK-10 | AC-3, AC-5 |
| TASK-12 | Painel de ocupação do Gerente | SoftwareArchitect | 4 | TASK-8, TASK-4 | AC-5, AC-7 |
| TASK-13 | Auth — gestão de usuários Atendente pelo Gerente | SoftwareArchitect | 4 | TASK-4 | AC-5 |
| TASK-14 | Compliance LGPD — anonimização, DPIA e DPO | Compliance | 4 | TASK-5 | AC-6 |
| TASK-15 | Observability — Axiom Log Drain + estrutura de logs | DevOps | 3 | TASK-1 | AC-3 |
| TASK-16 | CI/CD pipeline, ESLint no-cycle e preview environments | DevOps | 4 | TASK-1 | — |
| TASK-17 | UI — design system, mapa interativo e fluxos de bilheteria | UI | 6 | TASK-1 | AC-1, AC-2 |
| TASK-18 | Security — suite de isolamento cross-tenant (500 cenários) | Security | 4 | TASK-3, TASK-10 | AC-4 |
| TASK-19 | QA — integração concorrente, E2E e matriz de browsers | QA | 6 | TASK-10, TASK-11, TASK-12, TASK-17 | AC-1, AC-2, AC-3, AC-7 |
| TASK-20 | Tenant provisioning manual e documentação de onboarding | DevOps | 2 | TASK-4, TASK-13 | — |
| TASK-21 | Portal do Cliente — catálogo de filmes, sessões e reserva ACID | SoftwareArchitect | 5 | TASK-8, TASK-17 | AC-9, AC-14 |
| TASK-22 | Portal do Cliente — autenticação de cliente, 'Minhas Reservas' e cancelamento | Security | 4 | TASK-4, TASK-5, TASK-21 | AC-10, AC-12 |
| TASK-23 | Notificação transacional & baixa presencial de reservas no balcão | SoftwareArchitect | 5 | TASK-10, TASK-21 | AC-11, AC-13 |

## Detalhamento das tasks

### TASK-1. Project scaffolding & monorepo setup

- **Agente:** DevOps
- **Estimativa:** 4 h

Setup Next.js 14 App Router com pnpm workspaces, estrutura de pastas por módulo (bilheteria, backoffice, auth, tenancy, ocupacao, compradores), .env.example documentado, Tailwind CSS, TypeScript strict mode, ESLint import/no-cycle configurado para enforce 0 dependências circulares entre módulos

### TASK-2. Database schema design & Prisma migrations (Neon)

- **Agente:** DataArchitect
- **Estimativa:** 6 h
- **Depende de:** TASK-1
- **Cobre ACs:** AC-4, AC-8

Modelar schema Prisma completo: Tenant, User(roles), Film, Room, Seat, Session, SessionSeat(pré-populada na criação de Session), Ticket, Buyer(PII cifrado), auditoria_cancelamentos(append-only); tenant_id em todas entidades de negócio; trigger PostgreSQL BEFORE DELETE/UPDATE em auditoria_cancelamentos para garantir imutabilidade; migration inicial para Neon

### TASK-3. Multi-tenant Prisma middleware — row-level isolation

- **Agente:** SoftwareArchitect
- **Estimativa:** 5 h
- **Depende de:** TASK-2
- **Cobre ACs:** AC-4

Implementar Prisma Extension/middleware que injeta WHERE tenant_id = :tenantId automaticamente em todas queries de entidades de negócio; context de tenant via AsyncLocalStorage propagado do middleware Next.js; impede acesso cross-tenant por omissão de filtro; testes unitários de isolamento por módulo

### TASK-4. Authentication & RBAC via NextAuth.js

- **Agente:** Security
- **Estimativa:** 6 h
- **Depende de:** TASK-2
- **Cobre ACs:** AC-5

Configurar NextAuth.js com providers credentials; roles ATENDENTE/GERENTE e tenant_id no JWT; middleware Next.js protegendo rotas por role; retorno HTTP 403 para ATENDENTE tentando rotas de gerenciamento; testes unitários de acesso e bloqueio por perfil (AC-5)

### TASK-5. PII/LGPD — módulo CPF HMAC-SHA256 + AES-256-GCM

- **Agente:** Security
- **Estimativa:** 5 h
- **Depende de:** TASK-2
- **Cobre ACs:** AC-6

Implementar módulo compradores: HMAC-SHA256 com chave server-side (Vercel Env Secret) para busca indexada de CPF; AES-256-GCM para armazenamento cifrado para exibição; campo consentimento LGPD com timestamp obrigatório; integração com Vercel Env Secrets para rotação de chave sem redeploy; testes de round-trip encrypt/decrypt e HMAC collision resistance

### TASK-6. Backoffice — CRUD de catálogo de filmes

- **Agente:** SoftwareArchitect
- **Estimativa:** 5 h
- **Depende de:** TASK-3, TASK-4
- **Cobre ACs:** AC-5, AC-8

Route Handlers + Server Actions para criar, editar e listar filmes; validação Zod com erros descritivos por campo; acesso exclusivo a GERENTE via middleware RBAC; isolamento por tenant_id via Prisma Extension; testes unitários de validação e autorização

### TASK-7. Backoffice — CRUD de salas e layout de assentos

- **Agente:** SoftwareArchitect
- **Estimativa:** 6 h
- **Depende de:** TASK-3, TASK-4
- **Cobre ACs:** AC-5, AC-8

CRUD de Room e Seat com layout configurável (fileiras/colunas); criação em bulk de Seat records ao salvar sala; validação de campos obrigatórios com erros por campo; somente GERENTE; isolamento tenant_id; testes unitários de criação de layout e RBAC

### TASK-8. Backoffice — CRUD de sessões e pré-população de SessionSeat

- **Agente:** SoftwareArchitect
- **Estimativa:** 5 h
- **Depende de:** TASK-6, TASK-7
- **Cobre ACs:** AC-5, AC-8

CRUD de Session associando Film+Room+data/horário; ao criar Session, transação Prisma pré-popula SessionSeat (status=DISPONIVEL) para cada Seat da Room; validação de conflito de horário por sala; somente GERENTE; testes de pré-população e conflito

### TASK-9. Bilheteria — mapa de assentos com polling 2s

- **Agente:** SoftwareArchitect
- **Estimativa:** 5 h
- **Depende de:** TASK-8, TASK-17
- **Cobre ACs:** AC-2

Route Handler GET /api/sessoes/[id]/assentos retornando array SessionSeat com status; useEffect com setInterval 2000ms no componente React; renderização visual de estados (disponível/ocupado/selecionado) no mapa; testes de polling e atualização de estado em até 2s após mudança

### TASK-10. Bilheteria — venda ACID anti-double-booking

- **Agente:** SoftwareArchitect
- **Estimativa:** 8 h
- **Depende de:** TASK-5, TASK-9
- **Cobre ACs:** AC-1, AC-6

Transação Prisma com SELECT FOR UPDATE em SessionSeat para trava atômica; persistência de Ticket + Buyer (PII cifrado via TASK-5) em transação única; retorno de erro de conflito (HTTP 409) para segundo comprador; validação de todos campos obrigatórios (nome, CPF, e-mail, consentimento LGPD) antes de confirmar; teste integração 50 threads concorrentes mesmo assento (0 double-bookings)

### TASK-11. Bilheteria — cancelamento auditável

- **Agente:** SoftwareArchitect
- **Estimativa:** 4 h
- **Depende de:** TASK-10
- **Cobre ACs:** AC-3, AC-5

Endpoint de cancelamento que persiste registro imutável em auditoria_cancelamentos (ticket_id, user_id, timestamp UTC, tenant_id, motivo) via trigger append-only ANTES de liberar SessionSeat; somente ATENDENTE/GERENTE do mesmo tenant; testes de auditoria e liberação de assento pós-cancelamento

### TASK-12. Painel de ocupação do Gerente

- **Agente:** SoftwareArchitect
- **Estimativa:** 4 h
- **Depende de:** TASK-8, TASK-4
- **Cobre ACs:** AC-5, AC-7

Page Server-Side para GERENTE listando sessões do dia corrente com percentual vendidos/total por sessão; query agregada isolada por tenant_id do JWT; atualização ao recarregar; testes de cálculo de percentual e isolamento cross-tenant no painel

### TASK-13. Auth — gestão de usuários Atendente pelo Gerente

- **Agente:** SoftwareArchitect
- **Estimativa:** 4 h
- **Depende de:** TASK-4
- **Cobre ACs:** AC-5

CRUD de User com role ATENDENTE criados pelo GERENTE e vinculados ao tenant_id do gerente; listagem, desativação e redefinição de senha; somente GERENTE acessa; testes de criação de conta e isolamento de tenant

### TASK-14. Compliance LGPD — anonimização, DPIA e DPO

- **Agente:** Compliance
- **Estimativa:** 4 h
- **Depende de:** TASK-5
- **Cobre ACs:** AC-6

Implementar soft-anonymize em Buyer (Art. 18 LGPD): zeragem de campos PII mantendo id para integridade referencial; processo interno documentado para equipe CineDoom; DPIA simplificado interno documentado; registro de designação de DPO interno antes do go-live; checklist de conformidade LGPD para MVP

### TASK-15. Observability — Axiom Log Drain + estrutura de logs

- **Agente:** DevOps
- **Estimativa:** 3 h
- **Depende de:** TASK-1
- **Cobre ACs:** AC-3

Configurar Vercel Log Drain apontando para Axiom com retenção 365 dias (conformidade LGPD); estrutura de logs de auditoria (cancelamentos, autenticações, erros de concorrência); política de mascaramento de PII em logs (CPF nunca em plaintext); alertas de anomalia de acesso cross-tenant

### TASK-16. CI/CD pipeline, ESLint no-cycle e preview environments

- **Agente:** DevOps
- **Estimativa:** 4 h
- **Depende de:** TASK-1

GitHub Actions: lint (ESLint import/no-cycle — 0 dependências circulares), type-check TypeScript, testes unitários com cobertura mínima; Vercel preview environments por branch com Neon DB branching automático; Playwright CI matrix Chromium+Firefox (versão corrente-1) em resolução 1024×768; badge de status no README

### TASK-17. UI — design system, mapa interativo e fluxos de bilheteria

- **Agente:** UI
- **Estimativa:** 6 h
- **Depende de:** TASK-1
- **Cobre ACs:** AC-1, AC-2

Componentes Tailwind CSS: mapa de assentos interativo com estados visuais (disponível/ocupado/selecionado), fluxo de venda (seleção→cadastro comprador com consentimento LGPD→confirmação), formulários de backoffice com erro por campo; funcional em 1024×768 desktop/tablet landscape; sem polyfills experimentais; acessível em Chromium/Firefox

### TASK-18. Security — suite de isolamento cross-tenant (500 cenários)

- **Agente:** Security
- **Estimativa:** 4 h
- **Depende de:** TASK-3, TASK-10
- **Cobre ACs:** AC-4

Implementar suite automatizada de 500 cenários de isolamento cross-tenant cobrindo todos endpoints autenticados; validar 0 vazamentos de PII (CPF, e-mail, ingressos) entre tenants distintos; testes de bypass de tenant_id via header/param manipulation; integração ao CI como gate obrigatório

### TASK-19. QA — integração concorrente, E2E e matriz de browsers

- **Agente:** QA
- **Estimativa:** 6 h
- **Depende de:** TASK-10, TASK-11, TASK-12, TASK-17
- **Cobre ACs:** AC-1, AC-2, AC-3, AC-7

Testes de integração: venda ACID com 50 threads concorrentes (0 double-bookings validado), polling mapa 2s após venda/cancelamento, auditoria de cancelamento com campos obrigatórios, painel de ocupação percentual correto; E2E Playwright cobrindo fluxos críticos em Chromium+Firefox na matrix CI; relatório de cobertura de ACs

### TASK-20. Tenant provisioning manual e documentação de onboarding

- **Agente:** DevOps
- **Estimativa:** 2 h
- **Depende de:** TASK-4, TASK-13

Documentar processo manual de provisionamento de novo tenant (whitelist CineDoom): criação de Tenant record + GERENTE inicial via script interno; checklist de onboarding de novo dev com pnpm dev + .env.example em menos de 30min; runbook de operações de produção (rollback, rotação de chave AES, processo de anonimização LGPD)

## Paralelização sugerida

- **Grupo 1:** TASK-15+TASK-16+TASK-17
- **Grupo 2:** TASK-3+TASK-4+TASK-5
- **Grupo 3:** TASK-6+TASK-7
- **Grupo 4:** TASK-12+TASK-13+TASK-14
- **Grupo 5:** TASK-18+TASK-20

### TASK-21. Portal do Cliente — catálogo de filmes, sessões e reserva ACID

- **Agente:** SoftwareArchitect
- **Estimativa:** 5 h
- **Depende de:** TASK-8, TASK-17
- **Cobre ACs:** AC-9, AC-14

Implementar rotas públicas `/filmes`, `/sessoes/[id]` e fluxo de reserva de assento com trava atômica no banco (`session_seats.status = 'RESERVED'`), validação de antecedência (>60 min antes do início da sessão) e geração de código de reserva único (ex: CD-8942) com valor total e data limite de pagamento presencial.

### TASK-22. Portal do Cliente — autenticação de cliente, 'Minhas Reservas' e cancelamento

- **Agente:** Security
- **Estimativa:** 4 h
- **Depende de:** TASK-4, TASK-5, TASK-21
- **Cobre ACs:** AC-10, AC-12

Expandir o NextAuth.js com perfil `CLIENTE`, cadastro com hash seguro de senha, proteção LGPD (HMAC-SHA256 e AES-256-GCM para CPF com consentimento registrado), painel autenticado "Minhas Reservas" exibindo histórico e rota `POST /api/portal/reservas/[id]/cancelar` para cancelamento voluntário antes de 1 hora da sessão com liberação imediata dos assentos.

### TASK-23. Notificação transacional & baixa presencial de reservas no balcão

- **Agente:** SoftwareArchitect
- **Estimativa:** 5 h
- **Depende de:** TASK-10, TASK-21
- **Cobre ACs:** AC-11, AC-13

Implementar o `NotificationService` para envio de e-mail com voucher da reserva contendo instruções para pagamento presencial e registrar `email_sent_at`. No módulo do atendente, implementar tela de consulta de reserva por código ou CPF, com validação de status e confirmação de recebimento presencial, convertendo a reserva em `Ticket` vendido (`SOLD`).
