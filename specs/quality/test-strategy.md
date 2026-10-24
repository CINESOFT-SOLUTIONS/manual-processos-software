---
kind: agent_artifact
feature_id: F-CINEDOOM-PLATAFORMA-B2B-SAAS-C
agent: QA
generated_by:
  run_id: run_2026-10-23T03-58-17_eedeb0ce
  session_id: 2026-09-03T15-33-01-hdb88xzyiu
  model: anthropic:claude-sonnet-4-6
generated_at: 2026-10-23T05:01:34.498Z
regenerative: true
title: "[QA] CineDoom — plataforma B2B SaaS para cinemas independentes e redes de pequeno/méd"
---

# QA — CineDoom — plataforma B2B SaaS para cinemas independentes e redes de pequeno/méd

> Artefato derivado de `.specs/features/F-CINEDOOM-PLATAFORMA-B2B-SAAS-C/spec.md` e gerado pelo agente **QA**
> via AI-4SDLC Platform. **Regenerative work product** (não-canonical SDD).
> Não edite manualmente — re-gere via `sdlc resume`.

## Resumo

Multi-shot QA: 14/14 per-AC calls fulfilled, 26 test_cases total. Multi-shot Turn 2 — foco exclusivo AC-1: venda atômica ACID com SELECT FOR UPDATE anti-double-booking. Gerados 3 test_cases cobrindo cenário de concorrência simultânea, sucesso de um terminal e falha do outro, e integridade de estado pós-conflito.

## Cobertura por AC

| AC | Cobertura (%) |
|----|---------------|
| AC-1 | 100 |
| AC-2 | 100 |
| AC-3 | 100 |
| AC-4 | 100 |
| AC-5 | 100 |
| AC-6 | 100 |
| AC-7 | 100 |
| AC-8 | 100 |
| AC-9 | 100 |
| AC-10 | 100 |
| AC-11 | 100 |
| AC-12 | 100 |
| AC-13 | 100 |
| AC-14 | 100 |

## Casos de teste

| ID | AC | Tipo | Título | Caminho |
|----|----|------|--------|---------|
| TC-1 | AC-1 | integration | Dois terminais simultâneos: apenas um vende o mesmo assento | `tests/unit/venda-atomica.test.ts` |
| TC-2 | AC-2 | integration | Mapa de assentos reflete venda em no máximo 2 segundos via polling | `tests/unit/session-seats-polling.test.ts` |
| TC-3 | AC-3 | integration | Cancelamento persiste registro imutável em auditoria_cancelamentos com todos os campos obrigatórios | `tests/unit/cancelamento-auditavel.test.ts` |
| TC-4 | AC-4 | integration | Prisma Extension injeta tenant_id em query de filmes | `tests/unit/tenancy-isolation.test.ts` |
| TC-5 | AC-5 | integration | ATENDENTE recebe HTTP 403 ao tentar acessar rota de cadastro de filmes | `tests/unit/auth-rbac.test.ts` |
| TC-6 | AC-6 | unit | Persiste comprador com CPF hasheado (HMAC-SHA256), CPF cifrado (AES-256-GCM), e-mail e consentimento LGPD com timestamp | `tests/unit/cryptoservice.test.ts` |
| TC-7 | AC-7 | integration | Painel exibe percentual correto de assentos vendidos por sessão do dia | `tests/unit/session-seats-polling.test.ts` |
| TC-8 | AC-8 | integration | GERENTE cria filme com campos obrigatórios válidos e recebe 201 | `tests/unit/catalog-filmes.test.ts` |
| TC-9 | AC-1 | integration | Trava SELECT FOR UPDATE impede leitura de assento como disponível durante transação ativa | `tests/unit/concurrency-acid-50-threads.test.ts` |
| TC-10 | AC-2 | integration | Mapa de assentos reflete cancelamento em no máximo 2 segundos via polling | `tests/unit/session-seats-polling.test.ts` |
| TC-11 | AC-3 | integration | Cancelamento falha atomicamente se inserção em auditoria_cancelamentos falhar — assento permanece vendido | `tests/unit/cancelamento-auditavel.test.ts` |
| TC-12 | AC-4 | security | Cross-tenant isolation em query de ingressos — tenant-B não vaza para tenant-A | `tests/unit/security-cross-tenant-suite.test.ts` |
| TC-13 | AC-5 | integration | ATENDENTE recebe HTTP 403 ao tentar acessar rotas de salas, sessões e usuários | `tests/unit/auth-rbac.test.ts` |
| TC-14 | AC-6 | unit | Rejeita cadastro de comprador quando qualquer campo obrigatório está ausente antes de confirmar a venda | `tests/unit/compliance-anonymization.test.ts` |
| TC-15 | AC-7 | security | Painel não retorna sessões de outro tenant (isolamento cross-tenant) | `tests/unit/security-cross-tenant-suite.test.ts` |
| TC-16 | AC-8 | unit | Criação de filme com campo obrigatório ausente retorna 422 com erro descritivo por campo | `tests/unit/catalog-filmes.test.ts` |
| TC-17 | AC-2 | security | Endpoint de polling de assentos aplica isolamento tenant_id e retorna apenas assentos do tenant autenticado | `tests/unit/session-seats-polling.test.ts` |
| TC-18 | AC-3 | security | Registro de auditoria de cancelamento é isolado por tenant_id — tenant B não visualiza cancelamentos do tenant A | `tests/unit/cancelamento-auditavel.test.ts` |
| TC-19 | AC-4 | unit | Query sem contexto de tenant lança erro antes de atingir banco | `tests/unit/tenancy-isolation.test.ts` |
| TC-20 | AC-5 | integration | GERENTE tem acesso completo às rotas de gerenciamento do seu tenant | `tests/unit/auth-rbac.test.ts` |
| TC-21 | AC-9 | integration | Reserva atômica bloqueia assento com status RESERVED e impede venda ou reserva simultânea | `tests/integration/reserva-atomica.test.ts` |
| TC-22 | AC-10 | unit | Cadastro de cliente final com role CLIENTE, senha hash e proteção LGPD (HMAC-SHA256 e AES-256-GCM) | `tests/unit/users-management.test.ts` |
| TC-23 | AC-11 | integration | NotificationService dispara voucher por e-mail com código da reserva e grava email_sent_at | `tests/unit/observability-logger.test.ts` |
| TC-24 | AC-12 | integration | Cancelamento voluntário pelo cliente via web atualiza reserva para CANCELLED e libera assento para AVAILABLE | `tests/integration/reserva-atomica.test.ts` |
| TC-25 | AC-13 | integration | Atendente localiza reserva no balcão e confirma pagamento presencial convertendo em Ticket vendido (SOLD) | `tests/integration/reserva-atomica.test.ts` |
| TC-26 | AC-14 | integration | Reserva não paga até 60 minutos antes da sessão é considerada expirada (EXPIRED) Just-in-Time liberando assento | `tests/integration/reserva-atomica.test.ts` |

## Detalhamento dos casos

### TC-1. Dois terminais simultâneos: apenas um vende o mesmo assento

- **AC coberta:** AC-1
- **Tipo:** integration
- **Arquivo:** `tests/unit/venda-atomica.test.ts`
- **Given:** Dois terminais autenticados no mesmo tenant tentam vender o mesmo SessionSeat AVAILABLE na mesma sessão simultaneamente, com transações Prisma iniciadas em paralelo usando SELECT FOR UPDATE
- **When:** Ambas as requisições POST /api/vendas são disparadas concorrentemente (Promise.all com 2 threads)
- **Then:** Exatamente uma transação retorna HTTP 201 com ticket criado e SessionSeat status=SOLD; a outra retorna HTTP 409 com erro de conflito; nenhuma corrupção de estado ocorre (0 double-bookings, SessionSeat.status permanece SOLD com um único Ticket associado)

### TC-2. Mapa de assentos reflete venda em no máximo 2 segundos via polling

- **AC coberta:** AC-2
- **Tipo:** integration
- **Arquivo:** `tests/unit/session-seats-polling.test.ts`
- **Given:** Uma sessão existente com assento A1 disponível e um cliente fazendo polling GET /api/sessoes/[id]/assentos a cada 2000ms
- **When:** Uma venda é concluída com sucesso para o assento A1
- **Then:** Na próxima resposta do polling (dentro de 2000ms), o assento A1 deve aparecer com status SOLD na resposta JSON do Route Handler

### TC-3. Cancelamento persiste registro imutável em auditoria_cancelamentos com todos os campos obrigatórios

- **AC coberta:** AC-3
- **Tipo:** integration
- **Arquivo:** `tests/unit/cancelamento-auditavel.test.ts`
- **Given:** Um ingresso vendido existe para a sessão do tenant A, e o usuário autenticado como ATENDENTE possui id, tenant_id e fornece motivo de cancelamento
- **When:** O serviço de cancelamento é invocado com id do ingresso, id do usuário, motivo e tenant_id
- **Then:** Um registro é inserido em auditoria_cancelamentos contendo ingresso_id, usuario_id, timestamp UTC, tenant_id e motivo ANTES de o SessionSeat ter status alterado para AVAILABLE, e o registro não pode ser deletado ou atualizado (trigger append-only PostgreSQL rejeita UPDATE/DELETE)

### TC-4. Prisma Extension injeta tenant_id em query de filmes

- **AC coberta:** AC-4
- **Tipo:** integration
- **Arquivo:** `tests/unit/tenancy-isolation.test.ts`
- **Given:** Middleware Prisma configurado com tenantId='tenant-A' e existem filmes de tenant-A e tenant-B no banco
- **When:** Service de catálogo executa findMany em Film sem filtro explícito
- **Then:** Retorna apenas filmes com tenant_id='tenant-A'; nenhum filme de tenant-B é retornado

### TC-5. ATENDENTE recebe HTTP 403 ao tentar acessar rota de cadastro de filmes

- **AC coberta:** AC-5
- **Tipo:** integration
- **Arquivo:** `tests/unit/auth-rbac.test.ts`
- **Given:** Usuário autenticado com perfil ATENDENTE e token JWT válido do tenant
- **When:** Realiza GET/POST em /api/filmes (rota de cadastro de filmes, exclusiva de GERENTE)
- **Then:** API retorna HTTP 403 Forbidden sem executar lógica de negócio, sem vazar dados do tenant

### TC-6. Persiste comprador com CPF hasheado (HMAC-SHA256), CPF cifrado (AES-256-GCM), e-mail e consentimento LGPD com timestamp

- **AC coberta:** AC-6
- **Tipo:** unit
- **Arquivo:** `tests/unit/cryptoservice.test.ts`
- **Given:** Um payload de cadastro de comprador com nome, CPF válido, e-mail e flag de consentimento LGPD=true é submetido ao use-case de criação de Buyer
- **When:** O use-case executa persistência chamando o repositório de Buyer
- **Then:** O registro salvo deve conter cpf_hash = HMAC-SHA256(cpf, SERVER_SECRET), cpf_encrypted = AES-256-GCM(cpf, AES_KEY), email, nome, consent_at como timestamp UTC não-nulo e tenant_id correto; CPF em texto claro NÃO deve aparecer no registro

### TC-7. Painel exibe percentual correto de assentos vendidos por sessão do dia

- **AC coberta:** AC-7
- **Tipo:** integration
- **Arquivo:** `tests/unit/session-seats-polling.test.ts`
- **Given:** Uma sessão do dia corrente pertencente ao tenant A com 10 assentos totais e 4 ingressos vendidos (SessionSeat status=SOLD)
- **When:** GET /api/ocupacao/painel é chamado com token JWT do Gerente do tenant A
- **Then:** A resposta inclui a sessão com percentual 40 (4/10), campo total=10, campo vendidos=4, campo percentual=40, HTTP 200

### TC-8. GERENTE cria filme com campos obrigatórios válidos e recebe 201

- **AC coberta:** AC-8
- **Tipo:** integration
- **Arquivo:** `tests/unit/catalog-filmes.test.ts`
- **Given:** Usuário autenticado com perfil GERENTE e tenant_id válido; campos obrigatórios title e duration_minutes preenchidos
- **When:** POST /api/filmes com payload { title, duration_minutes } e JWT GERENTE
- **Then:** Resposta HTTP 201 com body contendo o filme criado com id, tenant_id igual ao do GERENTE e campos persistidos no banco

### TC-9. Trava SELECT FOR UPDATE impede leitura de assento como disponível durante transação ativa

- **AC coberta:** AC-1
- **Tipo:** integration
- **Arquivo:** `tests/unit/concurrency-acid-50-threads.test.ts`
- **Given:** Uma transação Prisma está ativa com SELECT FOR UPDATE no SessionSeat alvo (status=AVAILABLE) e ainda não foi commitada
- **When:** Uma segunda transação tenta ler e reservar o mesmo SessionSeat concorrentemente
- **Then:** A segunda transação aguarda liberação do lock ou recebe erro de timeout/deadlock, nunca lendo o assento como AVAILABLE enquanto a primeira transação está ativa; após commit da primeira (SOLD), a segunda falha com conflito HTTP 409

### TC-10. Mapa de assentos reflete cancelamento em no máximo 2 segundos via polling

- **AC coberta:** AC-2
- **Tipo:** integration
- **Arquivo:** `tests/unit/session-seats-polling.test.ts`
- **Given:** Uma sessão com assento B3 com status SOLD e um cliente fazendo polling GET /api/sessoes/[id]/assentos a cada 2000ms
- **When:** O cancelamento do ingresso do assento B3 é processado com sucesso
- **Then:** Na próxima resposta do polling (dentro de 2000ms), o assento B3 deve aparecer com status AVAILABLE na resposta JSON do Route Handler

### TC-11. Cancelamento falha atomicamente se inserção em auditoria_cancelamentos falhar — assento permanece vendido

- **AC coberta:** AC-3
- **Tipo:** integration
- **Arquivo:** `tests/unit/cancelamento-auditavel.test.ts`
- **Given:** Um ingresso vendido existe e a tabela auditoria_cancelamentos é configurada para rejeitar o insert (constraint violada ou trigger de teste)
- **When:** O serviço de cancelamento é invocado dentro de transação Prisma
- **Then:** A transação é revertida, o assento permanece com status SOLD, nenhum registro parcial existe em auditoria_cancelamentos e o chamador recebe erro indicando falha na auditoria

### TC-12. Cross-tenant isolation em query de ingressos — tenant-B não vaza para tenant-A

- **AC coberta:** AC-4
- **Tipo:** security
- **Arquivo:** `tests/unit/security-cross-tenant-suite.test.ts`
- **Given:** Dois tenants (A e B) com ingressos distintos; contexto Prisma configurado com tenantId='tenant-A'
- **When:** Atendente de tenant-A consulta endpoint GET /api/ingressos sem parâmetro tenant_id adicional
- **Then:** Response contém somente ingressos de tenant-A; nenhum ingresso de tenant-B presente no payload ou nos logs

### TC-13. ATENDENTE recebe HTTP 403 ao tentar acessar rotas de salas, sessões e usuários

- **AC coberta:** AC-5
- **Tipo:** integration
- **Arquivo:** `tests/unit/auth-rbac.test.ts`
- **Given:** Usuário autenticado com perfil ATENDENTE e token JWT válido
- **When:** Tenta acessar sequencialmente /api/salas, /api/sessoes (POST/PUT/DELETE) e /api/gestao/usuarios
- **Then:** Todas as rotas retornam HTTP 403; nenhuma mutação é persistida no banco; resposta não expõe detalhes internos

### TC-14. Rejeita cadastro de comprador quando qualquer campo obrigatório está ausente antes de confirmar a venda

- **AC coberta:** AC-6
- **Tipo:** unit
- **Arquivo:** `tests/unit/compliance-anonymization.test.ts`
- **Given:** Payloads de cadastro de Buyer com cada campo obrigatório omitido individualmente (nome ausente, CPF ausente, e-mail ausente, consentimento LGPD ausente)
- **When:** O use-case de criação de Buyer é invocado para cada payload inválido
- **Then:** Para cada caso deve retornar erro de validação descritivo identificando o campo faltante, sem persistir nenhum registro no banco e sem avançar para a etapa de venda do ingresso

### TC-15. Painel não retorna sessões de outro tenant (isolamento cross-tenant)

- **AC coberta:** AC-7
- **Tipo:** security
- **Arquivo:** `tests/unit/security-cross-tenant-suite.test.ts`
- **Given:** Tenant A possui sessão do dia com 5 assentos vendidos; Tenant B possui sessão do dia com 3 assentos vendidos; Gerente autenticado pertence ao tenant A
- **When:** GET /api/ocupacao/painel é chamado com token JWT do Gerente do tenant A
- **Then:** A resposta contém apenas sessões do tenant A; sessões do tenant B não aparecem na lista; HTTP 200 sem vazamento cross-tenant

### TC-16. Criação de filme com campo obrigatório ausente retorna 422 com erro descritivo por campo

- **AC coberta:** AC-8
- **Tipo:** unit
- **Arquivo:** `tests/unit/catalog-filmes.test.ts`
- **Given:** Usuário GERENTE autenticado; payload de criação de filme omite duration_minutes (campo obrigatório)
- **When:** POST /api/filmes com payload { title } sem duration_minutes
- **Then:** Resposta HTTP 422 com body JSON contendo array de erros onde ao menos um item identifica o campo 'duration_minutes' e descreve a violação de obrigatoriedade

### TC-17. Endpoint de polling de assentos aplica isolamento tenant_id e retorna apenas assentos do tenant autenticado

- **AC coberta:** AC-2
- **Tipo:** security
- **Arquivo:** `tests/unit/session-seats-polling.test.ts`
- **Given:** Dois tenants distintos (tenant-A e tenant-B) com sessões e assentos distintos, e um token JWT de tenant-A
- **When:** GET /api/sessoes/[id]/assentos é chamado com o token JWT de tenant-A para uma sessão de tenant-A
- **Then:** A resposta deve conter somente assentos com tenant_id de tenant-A; nenhum assento de tenant-B deve ser retornado, e o status HTTP deve ser 200

### TC-18. Registro de auditoria de cancelamento é isolado por tenant_id — tenant B não visualiza cancelamentos do tenant A

- **AC coberta:** AC-3
- **Tipo:** security
- **Arquivo:** `tests/unit/cancelamento-auditavel.test.ts`
- **Given:** Dois tenants A e B existem, cada um com um cancelamento registrado em auditoria_cancelamentos
- **When:** Uma query é executada com o Prisma Client Extension injetando WHERE tenant_id = tenantB
- **Then:** Apenas o registro de cancelamento do tenant B é retornado, zero registros do tenant A vazam, confirmando isolamento row-level na tabela de auditoria

### TC-19. Query sem contexto de tenant lança erro antes de atingir banco

- **AC coberta:** AC-4
- **Tipo:** unit
- **Arquivo:** `tests/unit/tenancy-isolation.test.ts`
- **Given:** Prisma Client Extension instanciado sem tenantId no contexto (contexto indefinido/nulo)
- **When:** Qualquer query em entidade de negócio (sessões, salas, compradores) é tentada
- **Then:** Extension lança TenantContextMissingError antes de executar SQL, impedindo vazamento por ausência de filtro

### TC-20. GERENTE tem acesso completo às rotas de gerenciamento do seu tenant

- **AC coberta:** AC-5
- **Tipo:** integration
- **Arquivo:** `tests/unit/auth-rbac.test.ts`
- **Given:** Usuário autenticado com perfil GERENTE e token JWT com tenant_id correto
- **When:** Acessa rotas de cadastro de filmes, salas, sessões e usuários (GET, POST, PUT, DELETE)
- **Then:** API retorna HTTP 2xx para operações válidas; dados retornados pertencem exclusivamente ao tenant_id do GERENTE autenticado; ATENDENTE de outro tenant ainda recebe 403
