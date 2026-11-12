---
document_id: SPEC-CINEDOOM-DEVOPS-001
version: "2.0.0"
date: "2026-11-05"
status: "Aprovado e Consolidado"
standard: "ABNT NBR ISO/IEC/IEEE 12207:2021 (Cláusulas 6.4.8, 6.4.12 e 6.4.13)"
title: "Especificação de DevOps, Infraestrutura, Observabilidade e SLOs — CineDoom"
---

# Especificação de DevOps, Infraestrutura, Observabilidade e SLOs — CineDoom

> **Documento Técnico Oficial — CineSoft Solutions (UFG/INF — Processos de Software 2026/1)**
> Rastreabilidade direta com [`cinedoom-spec.md`](../cinedoom-spec.md) (`RF-08`, `RF-11`, `RNF-01` a `RNF-06`, `CA-01` a `CA-15`, `RES-01` a `RES-06`), [`ADR-004`](../adrs/ADR-004-banco-postgresql-prisma-orm.md), [`ADR-005`](../adrs/ADR-005-hospedagem-vercel-supabase-github-actions.md) e [`ADR-011`](../adrs/ADR-011-log-drain-gerenciado-axiom-retencao-365-dias.md).

## Resumo Executivo

Especificação de DevOps, Engenharia de Confiabilidade de Sites (SRE) e Infraestrutura para o **CineDoom**. Define a topologia de implantação em **Vercel + Supabase PostgreSQL**, os Objetivos e Indicadores de Nível de Serviço (**SLOs** e **SLIs**) de disponibilidade, latência, integridade ACID e isolamento multi-tenant, a especificação de observabilidade com logs estruturados no **Axiom** e os procedimentos operacionais padrão (*runbooks*) para resposta a incidentes.

---

## 1. Topologia de Implantação e Ambientes

### 1.1 Ambiente de Desenvolvimento (`dev`)
- Aplicação Next.js 14 executando localmente via `pnpm dev`.
- Instância ou projeto de banco dedicado no Supabase (ou fallback local Docker/PostgreSQL resiliente).
- Variáveis de ambiente carregadas via `.env.local` (baseado em `.env.example` documentado).
- Seed automatizado de dados de demonstração via `npx prisma db seed`.

### 1.2 Ambiente de Homologação por Pull Request (`preview` / staging)
- Ambientes *Vercel Preview* provisionados automaticamente para cada Pull Request / branch.
- Ambiente de pré-visualização isolado da Vercel conectado a banco de testes dedicado/isolado no Supabase, populado exclusivamente com dados sintéticos.
- Domínio efêmero: `cinedoom-<branch>.vercel.app`.
- O pipeline de CI no GitHub Actions executa verificação de tipos (`tsc --noEmit`), linting (`ESLint import/no-cycle`), os **711 testes unitários/integração (Vitest)** e a suíte E2E (**Playwright** em Chromium e Firefox) como *gate* obrigatório antes do merge.

### 1.3 Ambiente de Produção (`prod`)
- **Hospedagem:** Vercel Production (região primária de execução: `gru1` — São Paulo via Vercel Edge Network).
- **Banco de Dados:** PostgreSQL 16 gerenciado no Supabase com pool de conexões (`DATABASE_URL`) para operações de aplicação/polling e conexão direta (`DIRECT_URL`) para migrações Prisma e transações ACID.
- **CDN:** Vercel Edge Network global para distribuição de assets estáticos e cartazes (`poster_url`).
- **Gestão de Segredos:** *Vercel Environment Variables* cifradas em repouso (`DATABASE_URL`, `DIRECT_URL`, `NEXTAUTH_SECRET`, `CPF_ENCRYPTION_KEY`, `CINEDOOM_CPF_HMAC_KEY`, `RESEND_API_KEY`, `NEXTAUTH_URL`).
- **Migrações de Esquema:** `prisma migrate deploy` executado como etapa bloqueante no pipeline de CI/CD antes da promoção do deploy.
- **Implantação Zero-Downtime e Rollback:** Deploys atômicos na Vercel com capacidade de *rollback* instantâneo para a versão estável anterior via painel ou CLI.
- **Backups e Recuperação:** *Point-in-Time Recovery* (PITR) e backups físicos diários nativos do Supabase + snapshots periódicos da tabela imutável `cancellation_audits`.
- **Retenção de Logs (`RF-11`):** Drenagem via *Vercel Log Drains* para o **Axiom** com retenção de **365 dias** para trilhas de auditoria LGPD e cancelamentos (`CA-03`).

---

## 2. Objetivos de Nível de Serviço (SLOs)

| ID | Métrica | Meta (Target) | Justificativa e Rastreabilidade |
|---|---|---|---|
| **SLO-1** | `api_availability` | $\ge$ 99.5% mensal | Disponibilidade operacional da plataforma SaaS em produção (excluindo janelas programadas). |
| **SLO-2** | `latency_p95_venda` | $<$ 800 ms | Atende ao **`RNF-01`** — endpoint de venda presencial (`POST /api/vendas`) e reserva online (`POST /api/portal/reservas`) incluindo trava `SELECT FOR UPDATE` sob carga de até 20 req/s. |
| **SLO-3** | `latency_p99_venda` | $<$ 1.500 ms | Atende ao **`RNF-01`** — limite superior para o percentil 99 sob contenção de trava ACID em horários de estreia. |
| **SLO-4** | `latency_p95_polling` | $<$ 300 ms | Atende ao **`RF-05`** e **`CA-02`** — consulta do mapa de assentos (`GET /api/sessoes/[id]/assentos`) a cada 2 segundos. |
| **SLO-5** | `error_rate_5xx` | $<$ 0.5% das requisições | Taxa máxima de erros internos do servidor (`HTTP 5xx`) em janelas móveis de 5 minutos. |
| **SLO-6** | `double_booking_rate` | `0 ocorrências` | Atende ao **`RNF-02`**, **`CA-01`** e **`CA-09`** — tolerância zero a vendas ou reservas duplas para a mesma poltrona. |
| **SLO-7** | `cross_tenant_leak_rate` | `0 ocorrências` | Atende ao **`RNF-03`**, **`RN-12`** e **`CA-04`** — tolerância zero a vazamento de dados entre cinemas concorrentes. |

---

## 3. Indicadores de Nível de Serviço (SLIs)

| ID | Indicador | Fórmula de Medição | Fonte de Coleta |
|---|---|---|---|
| **SLI-1** | `api_availability` | $\text{Requisições HTTP (2xx + 4xx)} / \text{Total de Requisições}$ em janela de 5 min | Vercel Analytics + Axiom Log Drain |
| **SLI-2** | `latency_p95_venda` | Percentil 95 de duração das requisições de venda/reserva em milissegundos | Axiom Log Drain |
| **SLI-3** | `latency_p99_venda` | Percentil 99 de duração das requisições de venda/reserva em milissegundos | Axiom Log Drain |
| **SLI-4** | `latency_p95_polling` | Percentil 95 de duração do endpoint `GET /api/sessoes/{id}/assentos` em ms | Axiom Log Drain |
| **SLI-5** | `error_rate_5xx` | $\text{Contagem}(\text{status\_code} \ge 500) / \text{Contagem}(\text{total de requisições})$ em 5 min | Axiom Log Drain |
| **SLI-6** | `double_booking_detected` | Contagem de eventos de inconsistência de assento duplicado nos logs de auditoria | Auditoria de Aplicação / Banco |
| **SLI-7** | `cross_tenant_leak_detected` | Contagem de violações detectadas pela *Prisma Tenancy Extension* (`TenantContextError`) | Axiom Log Drain |

---

## 4. Especificação de Observabilidade (`RF-11`)

### 4.1 Estrutura de Logs em Formato JSON
Todo registro de log emitido pela aplicação deve conter obrigatoriamente:
- `timestamp`: Data e hora em formato ISO 8601 UTC
- `level`: `DEBUG` | `INFO` | `WARN` | `ERROR`
- `service`: `'cinedoom-api'`
- `env`: `dev` | `preview` | `prod`
- `tenant_id`: UUID do cinema tenant (**Proibido registrar CPF, e-mail ou nome de comprador em texto claro**)
- `user_id`: UUID do operador ou cliente autenticado
- `request_id`: UUID de correlação da requisição (`x-request-id`)
- `module`: `bilheteria` | `catalogo` | `identidade` | `ocupacao` | `portal` | `tenancy`

**Campos específicos por evento de domínio:**
- **Venda Confirmada (`RF-06`):** `session_id`, `seat_id`, `ticket_id`, `action: 'ticket_sold'`
- **Cancelamento Auditável (`RF-08`, `CA-03`):** `ticket_id`, `cancellation_audit_id`, `action: 'ticket_cancelled'`
- **Conflito de Concorrência ACID (`CA-01`, `CA-09`):** `action: 'double_booking_conflict_blocked'`, `session_id`, `seat_id`, `status_code: 409`
- **Autenticação e RBAC (`RF-01`, `CA-05`):** `action: 'login_success' | 'login_failure' | 'rbac_denied'`, `role`, `route`
- **Tentativa de Violação Cross-Tenant (`CA-04`):** `action: 'cross_tenant_query_attempt'`, `expected_tenant_id`, `attempted_tenant_id` (`level: ERROR`)

### 4.2 Rastreamento e Correlação de Requisições por `request_id`
A aplicação propaga um `request_id` único gerado no logger em cada requisição, permitindo correlacionar os eventos de ponta a ponta no painel do Axiom:
- **Transação de Venda e Reserva (`POST /api/vendas`, `POST /api/portal/reservas`):**
  - Trava atômica de assento (`SELECT FOR UPDATE`)
  - Registro de ingresso ou voucher (`action: 'ticket_sold'` ou `'reservation_created'`)
  - Persistência com proteção criptográfica de comprador (`action: 'buyer_created'`)
- **Polling de Assentos (`GET /api/sessoes/{id}/assentos`):** Leitura leve e indexada do mapa de ocupação
- **Cancelamento Auditável (`POST /api/ingressos/{id}/cancelar`):** Gravação imutável em `cancellation_audits` e liberação do assento
- **Validação de Locatário:** Injeção do filtro `tenant_id` via Prisma Client Extension

### 4.3 Matriz de Alertas Operacionais

| Alerta | Condição de Disparo | Severidade | Canal de Notificação |
|--------|---------------------|------------|----------------------|
| `HighErrorRate5xx` | `error_rate_5xx > 1%` por 5 minutos | **P1** | Axiom Monitor + E-mail da Equipe |
| `VendaLatencyHigh` | `p95` de venda/reserva $> 1.000\text{ ms}$ por 3 minutos | **P2** | Axiom Monitor |
| `PollingLatencyHigh` | `p95` do polling de assentos $> 500\text{ ms}$ por 5 minutos | **P2** | Axiom Monitor |
| `DoubleBookingDetected` | Qualquer tentativa de conflito de assento duplicado | **P0** | Alerta Imediato (E-mail Equipe + Log Crítico) |
| `CrossTenantLeakDetected` | `cross_tenant_query_attempt > 0` em produção | **P0** | Alerta Imediato (E-mail Equipe + DPO LGPD) |
| `DatabasePoolExhausted` | Erros de saturação de conexões ao PostgreSQL $> 10/\text{min}$ | **P1** | Painel Supabase + Axiom Monitor |

---

## 5. Monitoramento Contínuo Pós-Implantação

### 5.1 Detecção de Anomalias e Desvios (*Drift Detection*)
- **Desvio de Volume Operacional (*Data Drift*):** Monitoramento semanal do volume de vendas e reservas por tenant; quedas abruptas ($> 50\%$) sem feriado ou fim de cartaz disparam verificação de saúde das rotas.
- **Anomalia de Cancelamentos (*Behavioral Drift*):** Aumento $> 3\times$ na taxa média de cancelamentos de um cinema em 7 dias aciona alerta gerencial para auditoria de caixa na tabela `cancellation_audits`.
- **Desvio de Esquema (*Schema Drift*):** O pipeline de CI valida `prisma migrate status`; qualquer divergência entre o esquema versionado e o banco bloqueia o deploy.

### 5.2 Governança de SLOs
- Revisão periódica do orçamento de erros (*error budget*) pelo Líder Técnico (TechLead).
- Incidentes de severidade **P0** exigem resposta em até 15 minutos, relatório *post-mortem* em até 48 horas e, se envolverem dados pessoais, acionamento do plano de resposta LGPD (notificação à ANPD em até 72h conforme [`compliance-assessment.md`](../security-compliance/compliance-assessment.md)).

---

## 6. Procedimentos Operacionais Padrão (Runbooks)

1. **Pico de Erros `HTTP 5xx`:** Inspecionar os logs no Axiom filtrando por `status_code >= 500` $\to$ identificar a rota afetada $\to$ verificar o painel de métricas do Supabase $\to$ se as conexões estiverem saturadas, avaliar sobrecarga de requisições ou executar *rollback* imediato na Vercel caso decorra de deploy recente.
2. **Latência Elevada na Venda/Reserva (`> 800ms p95`):** Inspecionar os logs de venda no Axiom $\to$ verificar se há contenção excessiva de `SELECT FOR UPDATE` na mesma sessão de estreia $\to$ validar se o erro `HTTP 409` está sendo retornado rapidamente sem espera em fila longa.
3. **Polling do Mapa de Assentos Lento (`> 300ms p95`):** Verificar o plano de execução (`EXPLAIN ANALYZE`) da consulta em `session_seats` $\to$ confirmar uso do índice composto `idx_session_seats_session_status` $\to$ validar se a consulta opera com tempo de resposta dentro da meta.
4. **Suspeita de Violação Cross-Tenant (P0):** Rotacionar imediatamente `NEXTAUTH_SECRET`, `CPF_ENCRYPTION_KEY` e `CINEDOOM_CPF_HMAC_KEY` na Vercel $\to$ auditar os registros de `tenant_id` e eventos `'cross_tenant_query_attempt'` no Axiom $\to$ aplicar correção emergencial, executar a bateria de 500 cenários (`security-cross-tenant-suite.test.ts`) e acionar o DPO conforme o plano de resposta a incidentes.
5. **Rotação Anual da Chave `CPF_ENCRYPTION_KEY` (`ADR-008`):** Gerar nova chave AES-256-GCM de 32 bytes $\to$ executar script autenticado de re-cifragem em lote sobre `Buyer.cpf_encrypted` e `Reservation.buyer_cpf_encrypted` $\to$ atualizar a variável no cofre da Vercel e validar a integridade em staging antes de produção.
6. **Atendimento a Solicitação de Anonimização LGPD (Art. 18 — `ADR-009`):** Executar chamada autenticada com perfil `GERENTE` ao endpoint `POST /api/titulares/anonimizar` informando o CPF do titular solicitante $\to$ verificar o retorno de confirmação da anonimização *in-place* $\to$ registrar o protocolo de atendimento e responder formalmente ao titular em até 15 dias.
5. **Rotação Anual da Chave `CPF_ENCRYPTION_KEY` (`ADR-008`):** Gerar nova chave AES-256-GCM de 32 bytes $\to$ executar script autenticado de re-cifragem em lote sobre `Buyer.cpf_encrypted` e `Reservation.buyer_cpf_encrypted` $\to$ atualizar a variável no cofre da Vercel e validar a integridade em staging antes de produção.
6. **Atendimento a Solicitação de Anonimização LGPD (Art. 18 — `ADR-009`):** Executar chamada autenticada com perfil `GERENTE` ao endpoint `POST /api/titulares/anonimizar` informando o CPF do titular solicitante $\to$ verificar o retorno de confirmação da anonimização *in-place* $\to$ registrar o protocolo de atendimento e responder formalmente ao titular em até 15 dias.
