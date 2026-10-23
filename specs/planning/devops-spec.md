---
kind: agent_artifact
feature_id: F-CINEDOOM-PLATAFORMA-B2B-SAAS-C
agent: DevOps
generated_by:
  run_id: run_2026-10-23T03-58-17_eedeb0ce
  session_id: 2026-09-03T15-33-01-hdb88xzyiu
  model: anthropic:claude-sonnet-4-6
generated_at: 2026-10-23T04:46:54.821Z
regenerative: true
title: "[DevOps] CineDoom — plataforma B2B SaaS para cinemas independentes e redes de pequeno/méd"
---

# DevOps — CineDoom — plataforma B2B SaaS para cinemas independentes e redes de pequeno/méd

> Artefato derivado de `.specs/features/F-CINEDOOM-PLATAFORMA-B2B-SAAS-C/spec.md` e gerado pelo agente **DevOps**
> via AI-4SDLC Platform. **Regenerative work product** (não-canonical SDD).
> Não edite manualmente — re-gere via `sdlc resume`.

## Resumo

DevOps spec para CineDoom MVP — plataforma B2B SaaS bilheteria. Cobre topologia Vercel+Neon Serverless, SLOs de availability/latency/error_rate/ACID, observabilidade OTel estruturada, runbooks para incidentes críticos (double-booking, polling degradado, vazamento cross-tenant).

## Deployment topology

## Ambientes

### dev
- Next.js 14 rodando local via `pnpm dev`
- Neon Serverless branch dedicado por dev (branch feature via Neon CLI)
- Variáveis via `.env.local` (cópia de `.env.example`)
- Sem CDN; hot-reload padrão Next.js
- Seed de dados via `prisma db seed`

### preview (staging por branch)
- Vercel Preview Environments automáticos por PR/branch
- Neon branch isolado por preview (criado via Vercel-Neon integration)
- Variáveis de ambiente injetadas pelo Vercel (DATABASE_URL por branch)
- Domínio: `cinedoom-<branch>.vercel.app`
- Sem CDN de produção; edge network Vercel padrão
- Testes de integração (ACID, isolamento, RBAC) rodam no CI apontando para este branch

### prod
- Vercel Production (região primária: GRU — São Paulo via Vercel Edge Network)
- Next.js App Router com RSC + Route Handlers como API
- Neon Serverless PostgreSQL — pool de conexões via Neon pooler (pgBouncer gerenciado), connection string via `DATABASE_URL` (pooled) e `DATABASE_URL_UNPOOLED` para migrações
- Réplica de leitura Neon: 1 réplica read-only para queries do painel de ocupação (US-3/AC-7) — aliviando write-primary
- CDN: Vercel Edge Network global para assets estáticos (JS, CSS, imagens de poster via `poster_url`)
- Secrets: Vercel Environment Variables (criptografadas em repouso) — `DATABASE_URL`, `NEXTAUTH_SECRET`, `CPF_ENCRYPTION_KEY` (AES-256-GCM), `NEXTAUTH_URL`
- Rotação de secrets: manual pela equipe CineDoom via Vercel dashboard + Neon console
- Migrações: `prisma migrate deploy` executado em CI/CD step pré-deploy (blocking gate)
- Zero-downtime deploy: Vercel atomic deployments (swap instantâneo)
- Rollback: Vercel instant rollback para deployment anterior via dashboard/CLI
- Backups: Neon point-in-time recovery (PITR) — retenção 7 dias no plano padrão; snapshot diário manual recomendado para dados de auditoria (CancellationAudit)
- Retenção de logs de aplicação: Vercel Log Drains → destino externo (ex: Axiom ou Datadog) com retenção 90 dias para logs operacionais, 365 dias para logs de auditoria LGPD/cancelamentos
- Multi-tenancy: row-level isolation via Prisma Client Extension (AD-2) — nenhum dado traversa tenant_id boundary
- LGPD: exclusão/anonimização de PII executada manualmente pela equipe CineDoom via script interno autenticado; CPF cifrado AES-256-GCM com chave rotacionável

## SLOs

| ID | Metric | Target | Rationale |
|---|---|---|---|
| SLO-1 | `api_availability` | 99.5% mensal | Baseline conservador SaaS B2B single-region Vercel+Neon; exclui janelas de manutenção Neon programadas |
| SLO-2 | `latency_p95_venda` | 800ms | NFR Performance — endpoint POST /api/ingressos incluindo SELECT FOR UPDATE + persistência em Neon poolado sob até 20 req/s |
| SLO-3 | `latency_p99_venda` | 1500ms | NFR Performance — cauda longa aceitável para trava ACID em pico de concorrência |
| SLO-4 | `latency_p95_polling` | 300ms | Mapa de assentos GET /api/sessoes/[id]/assentos — polling 2s requer resposta rápida para UX adequada |
| SLO-5 | `error_rate_5xx` | <0.5% das requisições | Erros de servidor não devem exceder 0.5% do total de requests em janela de 5min |
| SLO-6 | `double_booking_rate` | 0 ocorrências | NFR Reliability — zero double-bookings garantido por ACID; qualquer ocorrência é P0 imediato |
| SLO-7 | `cross_tenant_leak_rate` | 0 ocorrências | NFR Security — nenhum vazamento cross-tenant tolerado; qualquer ocorrência é P0 com notificação LGPD |

## SLIs

| ID | Metric | Measurement | Source |
|---|---|---|---|
| SLI-1 | `api_availability` | Porcentagem de requisições HTTP com status 2xx ou 4xx | excluindo 5xx) / total de requisições em janela 5min (Vercel Analytics + Log Drain |
| SLI-2 | `latency_p95_venda` | Percentil 95 de duração do OTel span 'POST /api/ingressos' em ms | otel-collector → Axiom/Datadog |
| SLI-3 | `latency_p99_venda` | Percentil 99 de duração do OTel span 'POST /api/ingressos' em ms | otel-collector |
| SLI-4 | `latency_p95_polling` | Percentil 95 de duração do OTel span 'GET /api/sessoes/{id}/assentos' em ms | otel-collector |
| SLI-5 | `error_rate_5xx` | count | http.response.status_code >= 500) / count(total requests) em janela 5min (Vercel Log Drain + métrica derivada |
| SLI-6 | `double_booking_detected` | count | eventos 'double_booking_conflict' no log estruturado) — deve ser 0 em produção (application log audit |
| SLI-7 | `cross_tenant_leak_detected` | count | alertas 'cross_tenant_query_attempt' disparados pelo Prisma Extension) — deve ser 0 (application log audit |

## Observability spec

## Logs Estruturados (JSON)

Campos obrigatórios em todo log:
- `timestamp`: ISO 8601 UTC
- `level`: DEBUG | INFO | WARN | ERROR
- `service`: 'cinedoom-api'
- `env`: dev | preview | prod
- `tenant_id`: UUID do tenant (NUNCA logar CPF, e-mail ou nome de comprador em claro)
- `user_id`: UUID do usuário autenticado
- `request_id`: UUID por request (header x-request-id propagado)
- `module`: bilheteria | backoffice | auth | tenancy | ocupacao

Campos adicionais por evento:
- Venda: `session_id`, `seat_id`, `ticket_id`, `action: 'ticket_sold'`
- Cancelamento: `ticket_id`, `cancellation_audit_id`, `motivo_hash` (não logar motivo PII em claro), `action: 'ticket_cancelled'`
- Conflict ACID: `action: 'double_booking_conflict'`, `session_id`, `seat_id`, `competing_request_id`
- Auth: `action: 'login_success'|'login_failure'|'authz_denied'`, `role`, `route`
- Tenant isolation violation: `action: 'cross_tenant_query_attempt'`, `expected_tenant_id`, `attempted_tenant_id` — level ERROR

## OTel Spans (Traces)

- `POST /api/ingressos` — span raiz venda; child spans:
  - `prisma.transaction.seat_lock` (SELECT FOR UPDATE)
  - `prisma.insert.ticket`
  - `prisma.insert.buyer`
- `GET /api/sessoes/{id}/assentos` — span raiz polling mapa
  - `prisma.query.session_seats`
- `DELETE /api/ingressos/{id}` — span cancelamento
  - `prisma.insert.cancellation_audit`
  - `prisma.update.session_seat_release`
- `POST /api/auth/[...nextauth]` — span autenticação
- `prisma.extension.tenant_filter` — span injetado pela Prisma Extension em toda query (valida tenant_id)

## Métricas RED

- **Rate**: `http_requests_total{method, route, status_code, tenant_id}` — counter
- **Errors**: `http_errors_total{route, status_code, error_type}` — counter; `double_booking_total{session_id}` — counter
- **Duration**: `http_request_duration_ms{route, method}` — histogram (buckets: 50, 100, 200, 500, 800, 1500, 3000ms)
- Polling específico: `seat_map_poll_duration_ms` — histogram separado para GET /api/sessoes/*/assentos
- Audit: `cancellation_audit_written_total{tenant_id}` — counter

## Alertas

| Alerta | Condição | Severidade | Canal |
|--------|----------|------------|-------|
| HighErrorRate5xx | error_rate_5xx > 1% por 5min | P1 | Slack #cinedoom-alerts + PagerDuty |
| VendaLatencyHigh | p95 latency POST /api/ingressos > 1000ms por 3min | P2 | Slack #cinedoom-alerts |
| PollingLatencyHigh | p95 GET assentos > 500ms por 5min | P2 | Slack #cinedoom-alerts |
| DoubleBookingDetected | double_booking_total incremento > 0 | P0 | PagerDuty + Slack #cinedoom-p0 |
| CrossTenantLeakDetected | cross_tenant_query_attempt count > 0 | P0 | PagerDuty + Slack #cinedoom-p0 + equipe LGPD |
| NeonConnectionPoolExhausted | pg connection errors > 10/min | P1 | Slack #cinedoom-alerts |

## Post-market monitoring

## Post-Market Monitoring Plan (EU AI Act Art. 72 / NIST AI RMF MEASURE 2)

### Escopo
CineDoom MVP não contém modelos de IA/ML, mas opera com dados PII sensíveis (CPF, e-mail) e lógica crítica ACID. O plano cobre monitoramento contínuo de comportamento do sistema em produção.

### Drift Detection
- **Data drift**: monitorar distribuição de volume de vendas por tenant/sessão semanalmente — alertar se volume cair >50% sem evento programado (indica possível falha silenciosa de persistência ou tenant abandonado)
- **Concept drift (comportamental)**: monitorar taxa de cancelamentos por tenant — aumento >3x da média histórica em 7 dias dispara revisão manual (possível fraude ou bug de UI)
- **Schema drift**: pipeline CI valida `prisma migrate status` em produção; qualquer drift entre schema esperado e real bloqueia deploy e dispara alerta P1

### Performance Degradation Alerts
- SLO breach automático: qualquer SLO fora de target por >10min dispara revisão de incidente
- Trend alert: latência p95 de venda crescendo >20% semana-a-semana por 2 semanas consecutivas → revisão de índices Neon e pool sizing
- Neon cold start monitoring: rastrear frequência de cold starts via span `prisma.connect` duration >500ms; >5% das requests com cold start dispara revisão de pool warmup

### SLOs em Produção — Revisão Periódica
- Revisão mensal de SLOs pelo tech lead CineDoom
- Relatório de error budget consumption enviado para stakeholders mensalmente
- Revisão semestral de política de retenção LGPD (compradores, audit logs)

### Processo de Resposta
- P0 (double-booking, cross-tenant leak): resposta em <15min, postmortem em 48h, notificação aos tenants afetados em <24h, avaliação de obrigação LGPD de notificação à ANPD

## Runbook hints

- 5xx spike: verificar Vercel Function logs via Log Drain → identificar rota com maior error_rate → checar Neon connection pool (dashboard Neon) → se pool exhausted, aumentar pool_size no connection string ou throttle de requests
- Double-booking detectado (P0): imediatamente pausar sessão afetada via admin script → auditar tabela SessionSeat para o session_id → identificar ticket duplicado → remover ticket inválido mantendo auditoria → notificar tenant → postmortem obrigatório
- Latência alta em POST /api/ingressos: checar OTel trace do span prisma.transaction.seat_lock → se lock wait >500ms, investigar concorrência na sessão (muitos SELECT FOR UPDATE simultâneos) → considerar retry com backoff ou fila de venda para pico
- Polling de mapa lento (>500ms p95): checar span prisma.query.session_seats → verificar índice em SessionSeat(session_id, tenant_id, status) no Neon → EXPLAIN ANALYZE na query → se Neon cold start, avaliar connection warmup
- Cross-tenant leak detectado (P0): rotacionar NEXTAUTH_SECRET e CPF_ENCRYPTION_KEY imediatamente → suspender tenants potencialmente afetados → auditar logs do span prisma.extension.tenant_filter → identificar query sem filtro → patch emergencial + notificação LGPD à ANPD se dados expostos
- Neon connection pool exhausted: aumentar pool_size na DATABASE_URL (parâmetro ?pgbouncer=true&connection_limit=N) → verificar queries longas via Neon query insights → matar sessions idle >30s → avaliar réplica de leitura para queries de painel de ocupação
- CPF_ENCRYPTION_KEY rotation: gerar nova chave AES-256-GCM → script de re-encrypt em batch sobre Buyer.cpf_encrypted com tenant_id filtrado → deploy com nova chave → validar decryptabilidade em staging antes de prod
- Rollback de deploy: via Vercel dashboard → Deployments → selecionar deployment anterior → Promote to Production → verificar se migration foi aplicada (se sim, avaliar migration reversa via prisma migrate resolve)
- Tenant data deletion request (LGPD): executar script interno autenticado de anonimização → setar Buyer.name='ANONIMIZADO', Buyer.email=hash, Buyer.cpf_hash=DELETED, Buyer.cpf_encrypted=NULL → registrar execução em log de auditoria interno → confirmar para solicitante em <15 dias úteis
