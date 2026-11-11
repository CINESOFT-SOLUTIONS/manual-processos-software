---
kind: estrategia_testes_qa
feature_id: F-CINEDOOM-MVP
title: "Estratégia de Qualidade, Verificação, Validação e Casos de Teste — CineDoom"
norma_referencia: "ABNT NBR ISO/IEC/IEEE 12207:2021 (Seções 6.4.9 e 6.4.11)"
---

# Estratégia de Qualidade e Especificação de Casos de Teste (QA) — CineDoom

> Artefato derivado de [`specs/cinedoom-spec.md`](../cinedoom-spec.md) para atendimento às seções **5.1.2 (Rastreabilidade)**, **5.3.3 (Testes Unitários e de Integração)** e **5.4 (Verificação e Validação)** do Manual de Processos de Software.

---

## 1. Resumo da Cobertura de Verificação e Validação

A suíte de qualidade cobre **100% dos 14 Critérios de Aceite (`CA-01` a `CA-14`)** e dos **18 Requisitos Funcionais (`RF-01` a `RF-18`)** por meio de **26 Casos de Teste formais (`CT-01` a `CT-26`)** implementados no repositório `cinedoom-app` (totalizando 770 testes automatizados na suíte Vitest).

### Cobertura por Critério de Aceite (`CA-01` a `CA-14`)

| Critério de Aceite (`CA`) | Equivalência no Código (`AC`) | Requisito Principal (`RF` / `RNF`) | Regra de Negócio (`RN`) | Cobertura (%) |
| :---: | :---: | :---: | :---: | :---: |
| **`CA-01`** | `AC-1` | `RF-07`, `RNF-02` | `RN-01` | 100% |
| **`CA-02`** | `AC-2` | `RF-06`, `RNF-01` | `RN-02` | 100% |
| **`CA-03`** | `AC-3` | `RF-08`, `RF-11` | `RN-07` | 100% |
| **`CA-04`** | `AC-4` | `RNF-03` | `RN-12` | 100% |
| **`CA-05`** | `AC-5` | `RF-01`, `RF-02` | `RN-08`, `RN-09` | 100% |
| **`CA-06`** | `AC-6` | `RF-09`, `RNF-03` | `RN-10`, `RN-11` | 100% |
| **`CA-07`** | `AC-7` | `RF-10` | `RN-08`, `RN-12` | 100% |
| **`CA-08`** | `AC-8` | `RF-03`, `RF-04`, `RF-05` | `RN-05`, `RN-06` | 100% |
| **`CA-09`** | `AC-9` | `RF-12`, `RF-13` | `RN-01`, `RN-02`, `RN-03` | 100% |
| **`CA-10`** | `AC-10` | `RF-01`, `RF-14` | `RN-09`, `RN-10` | 100% |
| **`CA-11`** | `AC-11` | `RF-11`, `RF-15` | `RN-03` | 100% |
| **`CA-12`** | `AC-12` | `RF-16` | `RN-02`, `RN-04` | 100% |
| **`CA-13`** | `AC-13` | `RF-17` | `RN-02`, `RN-03` | 100% |
| **`CA-14`** | `AC-14` | `RF-06`, `RF-18` | `RN-02`, `RN-04` | 100% |

---

## 2. Catálogo Geral de Casos de Teste (`CT-01` a `CT-26`)

| ID (`CT`) | Ref. Código (`TC`) | Critério (`CA`) | Requisito (`RF`) | Nível de Teste | Título do Caso de Teste | Arquivo de Teste (`cinedoom-app`) |
| :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **`CT-01`** | `TC-1` | `CA-01` | `RF-07` | Integração | Dois terminais simultâneos: apenas um vende o mesmo assento | `tests/unit/venda-atomica.test.ts` |
| **`CT-02`** | `TC-2` | `CA-02` | `RF-06` | Integração | Mapa de assentos reflete venda em no máximo 2 segundos via polling | `tests/unit/session-seats-polling.test.ts` |
| **`CT-03`** | `TC-3` | `CA-03` | `RF-08` | Integração | Cancelamento persiste registro imutável em `auditoria_cancelamentos` com todos os campos obrigatórios | `tests/unit/cancelamento-auditavel.test.ts` |
| **`CT-04`** | `TC-4` | `CA-04` | `RF-03` | Integração | Prisma Extension injeta `tenant_id` automaticamente em query de filmes | `tests/unit/tenancy-isolation.test.ts` |
| **`CT-05`** | `TC-5` | `CA-05` | `RF-01` | Integração | `ATENDENTE` recebe `HTTP 403` ao tentar acessar rota de cadastro de filmes | `tests/unit/auth-rbac.test.ts` |
| **`CT-06`** | `TC-6` | `CA-06` | `RF-09` | Unitário | Persiste comprador com CPF em hash (`HMAC-SHA256`), CPF cifrado (`AES-256-GCM`), e-mail e consentimento LGPD com timestamp | `tests/unit/cryptoservice.test.ts` |
| **`CT-07`** | `TC-7` | `CA-07` | `RF-10` | Integração | Painel gerencial exibe percentual correto de assentos vendidos por sessão do dia | `tests/unit/session-seats-polling.test.ts` |
| **`CT-08`** | `TC-8` | `CA-08` | `RF-03` | Integração | `GERENTE` cria filme com campos obrigatórios válidos e recebe `HTTP 201` | `tests/unit/catalog-filmes.test.ts` |
| **`CT-09`** | `TC-9` | `CA-01` | `RF-07` | Integração | Trava `SELECT FOR UPDATE` impede leitura de assento como disponível durante transação ativa (50 threads) | `tests/unit/concurrency-acid-50-threads.test.ts` |
| **`CT-10`** | `TC-10` | `CA-02` | `RF-06` | Integração | Mapa de assentos reflete cancelamento em no máximo 2 segundos via polling | `tests/unit/session-seats-polling.test.ts` |
| **`CT-11`** | `TC-11` | `CA-03` | `RF-08` | Integração | Cancelamento falha atomicamente se inserção em `auditoria_cancelamentos` falhar — assento permanece vendido | `tests/unit/cancelamento-auditavel.test.ts` |
| **`CT-12`** | `TC-12` | `CA-04` | `RNF-03` | Segurança | Isolamento *cross-tenant* em query de ingressos — `tenant-B` não vaza para `tenant-A` | `tests/unit/security-cross-tenant-suite.test.ts` |
| **`CT-13`** | `TC-13` | `CA-05` | `RF-02` | Integração | `ATENDENTE` recebe `HTTP 403` ao tentar acessar rotas de salas, sessões e usuários | `tests/unit/auth-rbac.test.ts` |
| **`CT-14`** | `TC-14` | `CA-06` | `RF-09` | Unitário | Rejeita cadastro de comprador quando qualquer campo obrigatório ou consentimento LGPD está ausente | `tests/unit/compliance-anonymization.test.ts` |
| **`CT-15`** | `TC-15` | `CA-07` | `RF-10` | Segurança | Painel de ocupação não retorna sessões de outro *tenant* (isolamento *cross-tenant*) | `tests/unit/security-cross-tenant-suite.test.ts` |
| **`CT-16`** | `TC-16` | `CA-08` | `RF-03` | Unitário | Criação de filme com campo obrigatório ausente retorna `HTTP 422` com erro descritivo por campo | `tests/unit/catalog-filmes.test.ts` |
| **`CT-17`** | `TC-17` | `CA-02` | `RF-06` | Segurança | Endpoint de polling de assentos aplica isolamento `tenant_id` e retorna apenas assentos do *tenant* | `tests/unit/session-seats-polling.test.ts` |
| **`CT-18`** | `TC-18` | `CA-03` | `RF-08` | Segurança | Registro de auditoria de cancelamento é isolado por `tenant_id` — `tenant-B` não vê cancelamentos de `tenant-A` | `tests/unit/cancelamento-auditavel.test.ts` |
| **`CT-19`** | `TC-19` | `CA-04` | `RNF-03` | Unitário | Query sem contexto de *tenant* lança erro (`TenantContextMissingError`) antes de atingir o banco | `tests/unit/tenancy-isolation.test.ts` |
| **`CT-20`** | `TC-20` | `CA-05` | `RF-01` | Integração | `GERENTE` tem acesso completo às rotas de gerenciamento do seu *tenant* | `tests/unit/auth-rbac.test.ts` |
| **`CT-21`** | `TC-21` | `CA-09` | `RF-13` | Integração | Reserva atômica bloqueia assento com status `RESERVED` e impede venda ou reserva simultânea | `tests/integration/reserva-atomica.test.ts` |
| **`CT-22`** | `TC-22` | `CA-10` | `RF-14` | Unitário | Cadastro de cliente final com perfil `CLIENTE`, senha hash e proteção LGPD (`HMAC-SHA256` e `AES-256-GCM`) | `tests/unit/users-management.test.ts` |
| **`CT-23`** | `TC-23` | `CA-11` | `RF-15` | Integração | `NotificationService` dispara voucher por e-mail com código da reserva e grava `email_sent_at` | `tests/unit/observability-logger.test.ts` |
| **`CT-24`** | `TC-24` | `CA-12` | `RF-16` | Integração | Cancelamento voluntário pelo cliente via web atualiza reserva para `CANCELLED` e libera assento para `AVAILABLE` | `tests/integration/reserva-atomica.test.ts` |
| **`CT-25`** | `TC-25` | `CA-13` | `RF-17` | Integração | Atendente localiza reserva no balcão e confirma pagamento presencial convertendo em `Ticket` vendido (`SOLD`) | `tests/integration/reserva-atomica.test.ts` |
| **`CT-26`** | `TC-26` | `CA-14` | `RF-18` | Integração | Reserva não paga até 60 minutos antes da sessão é considerada expirada (`EXPIRED`) *Just-in-Time* liberando assento | `tests/integration/reserva-atomica.test.ts` |

---

## 3. Especificação Detalhada dos Casos de Teste (Dado que / Quando / Então)

### CT-01 (`TC-1`). Dois terminais simultâneos: apenas um vende o mesmo assento
* **Critério coberto:** `CA-01` (`AC-1`) | **Requisito:** `RF-07` | **Regra:** `RN-01`
* **Nível:** Integração | **Arquivo:** `tests/unit/venda-atomica.test.ts`
* **Dado que:** Dois terminais autenticados no mesmo *tenant* tentam vender o mesmo `SessionSeat` (`AVAILABLE`) na mesma sessão simultaneamente, com transações Prisma iniciadas em paralelo usando `SELECT FOR UPDATE`.
* **Quando:** Ambas as requisições `POST /api/vendas` são disparadas concorrentemente (`Promise.all` com 2 threads).
* **Então:** Exatamente uma transação retorna `HTTP 201` com `Ticket` criado e `SessionSeat.status = SOLD`; a outra retorna `HTTP 409 Conflict`; nenhuma corrupção de estado ocorre (0 *double-bookings*).

### CT-02 (`TC-2`). Mapa de assentos reflete venda em no máximo 2 segundos via polling
* **Critério coberto:** `CA-02` (`AC-2`) | **Requisito:** `RF-06` | **Regra:** `RN-02`
* **Nível:** Integração | **Arquivo:** `tests/unit/session-seats-polling.test.ts`
* **Dado que:** Uma sessão existente com assento `A1` disponível e um cliente fazendo *polling* em `GET /api/sessoes/[id]/assentos` a cada `2000ms`.
* **Quando:** Uma venda é concluída com sucesso para o assento `A1`.
* **Então:** Na próxima resposta do *polling* (dentro de `2000ms`), o assento `A1` deve aparecer com status `SOLD` na resposta JSON do Route Handler.

### CT-03 (`TC-3`). Cancelamento persiste registro imutável em `auditoria_cancelamentos` com todos os campos obrigatórios
* **Critério coberto:** `CA-03` (`AC-3`) | **Requisito:** `RF-08` | **Regra:** `RN-07`
* **Nível:** Integração | **Arquivo:** `tests/unit/cancelamento-auditavel.test.ts`
* **Dado que:** Um ingresso vendido existe para a sessão do `tenant-A`, e o usuário autenticado como `ATENDENTE` possui `id`, `tenant_id` e fornece motivo válido de cancelamento.
* **Quando:** O serviço de cancelamento é invocado com `ticket_id`, `user_id`, motivo e `tenant_id`.
* **Então:** Um registro é inserido em `auditoria_cancelamentos` contendo `ticket_id`, `user_id`, `timestamp` UTC, `tenant_id` e motivo **antes** de o `SessionSeat` ter o status alterado para `AVAILABLE`, sendo protegido por *trigger* *append-only* no PostgreSQL contra `UPDATE` e `DELETE`.

### CT-04 (`TC-4`). Prisma Extension injeta `tenant_id` em query de filmes
* **Critério coberto:** `CA-04` (`AC-4`) | **Requisito:** `RF-03` | **Regra:** `RN-12`
* **Nível:** Integração | **Arquivo:** `tests/unit/tenancy-isolation.test.ts`
* **Dado que:** O middleware Prisma está configurado com `tenantId = 'tenant-A'` e existem filmes de `tenant-A` e `tenant-B` no banco.
* **Quando:** O serviço de catálogo executa `findMany` em `Film` sem filtro explícito.
* **Então:** Retorna apenas filmes com `tenant_id = 'tenant-A'`; nenhum filme de `tenant-B` é retornado.

### CT-05 (`TC-5`). `ATENDENTE` recebe `HTTP 403` ao tentar acessar rota de cadastro de filmes
* **Critério coberto:** `CA-05` (`AC-5`) | **Requisito:** `RF-01` | **Regra:** `RN-08`
* **Nível:** Integração | **Arquivo:** `tests/unit/auth-rbac.test.ts`
* **Dado que:** Usuário autenticado com perfil `ATENDENTE` e token JWT válido do *tenant*.
* **Quando:** Realiza `GET` ou `POST` em `/api/filmes` (rota exclusiva de `GERENTE`).
* **Então:** A API retorna `HTTP 403 Forbidden` sem executar lógica de negócio.

### CT-06 (`TC-6`). Persiste comprador com CPF hasheado (`HMAC-SHA256`), CPF cifrado (`AES-256-GCM`), e-mail e consentimento LGPD
* **Critério coberto:** `CA-06` (`AC-6`) | **Requisito:** `RF-09` | **Regra:** `RN-10`
* **Nível:** Unitário | **Arquivo:** `tests/unit/cryptoservice.test.ts`
* **Dado que:** Um payload de cadastro de comprador com nome, CPF válido, e-mail e `lgpd_consent = true` é submetido ao caso de uso de criação de `Buyer`.
* **Quando:** O caso de uso executa a persistência chamando o repositório de `Buyer`.
* **Então:** O registro salvo deve conter `cpf_hash = HMAC-SHA256(cpf, SECRET)`, `cpf_encrypted = AES-256-GCM(cpf, KEY)`, `email`, `nome`, `consent_at` como `timestamp` UTC não-nulo e `tenant_id` correto; o CPF em texto claro jamais deve constar no registro.

### CT-07 (`TC-7`). Painel exibe percentual correto de assentos vendidos por sessão do dia
* **Critério coberto:** `CA-07` (`AC-7`) | **Requisito:** `RF-10` | **Regra:** `RN-08`
* **Nível:** Integração | **Arquivo:** `tests/unit/session-seats-polling.test.ts`
* **Dado que:** Uma sessão do dia corrente pertencente ao `tenant-A` com 10 assentos totais e 4 ingressos vendidos (`SOLD`).
* **Quando:** `GET /api/ocupacao/painel` é chamado com token JWT do Gerente do `tenant-A`.
* **Então:** A resposta inclui a sessão com percentual `40%` (`4/10`), `total = 10`, `vendidos = 4` e `HTTP 200`.

### CT-08 (`TC-8`). `GERENTE` cria filme com campos obrigatórios válidos e recebe `HTTP 201`
* **Critério coberto:** `CA-08` (`AC-8`) | **Requisito:** `RF-03` | **Regra:** `RN-05`
* **Nível:** Integração | **Arquivo:** `tests/unit/catalog-filmes.test.ts`
* **Dado que:** Usuário autenticado com perfil `GERENTE` e `tenant_id` válido; campos obrigatórios `title` e `durationMinutes` preenchidos.
* **Quando:** Envia `POST /api/filmes` com payload válido.
* **Então:** Resposta `HTTP 201` com corpo contendo o filme criado vinculado ao `tenant_id` do Gerente.

### CT-09 (`TC-9`). Trava `SELECT FOR UPDATE` impede leitura de assento como disponível durante transação ativa
* **Critério coberto:** `CA-01` (`AC-1`) | **Requisito:** `RF-07`, `RNF-02` | **Regra:** `RN-01`
* **Nível:** Integração | **Arquivo:** `tests/unit/concurrency-acid-50-threads.test.ts`
* **Dado que:** Uma bateria de 50 requisições concorrentes disputa o mesmo `SessionSeat` (`AVAILABLE`).
* **Quando:** As 50 transações são disparadas simultaneamente.
* **Então:** Exatamente 1 transação efetiva a venda (`SOLD`) e as outras 49 recebem `HTTP 409 Conflict`, mantendo integridade referencial absoluta.

### CT-10 (`TC-10`). Mapa de assentos reflete cancelamento em no máximo 2 segundos via polling
* **Critério coberto:** `CA-02` (`AC-2`) | **Requisito:** `RF-06` | **Regra:** `RN-02`
* **Nível:** Integração | **Arquivo:** `tests/unit/session-seats-polling.test.ts`
* **Dado que:** Uma sessão com assento `B3` com status `SOLD` e um cliente fazendo *polling* a cada `2000ms`.
* **Quando:** O cancelamento do ingresso do assento `B3` é processado com sucesso.
* **Então:** Na próxima resposta do *polling* (dentro de `2000ms`), o assento `B3` aparece com status `AVAILABLE`.

### CT-11 (`TC-11`). Cancelamento falha atomicamente se inserção em `auditoria_cancelamentos` falhar
* **Critério coberto:** `CA-03` (`AC-3`) | **Requisito:** `RF-08` | **Regra:** `RN-07`
* **Nível:** Integração | **Arquivo:** `tests/unit/cancelamento-auditavel.test.ts`
* **Dado que:** Um ingresso vendido existe e a inserção em `auditoria_cancelamentos` falha por violação de *constraint*.
* **Quando:** O serviço de cancelamento é invocado dentro de transação Prisma.
* **Então:** A transação sofre *rollback* integral e o assento permanece com status `SOLD`.

### CT-12 (`TC-12`). Isolamento *cross-tenant* em query de ingressos
* **Critério coberto:** `CA-04` (`AC-4`) | **Requisito:** `RNF-03` | **Regra:** `RN-12`
* **Nível:** Segurança | **Arquivo:** `tests/unit/security-cross-tenant-suite.test.ts`
* **Dado que:** Dois *tenants* (`A` e `B`) possuem ingressos distintos e o contexto Prisma está em `tenant-A`.
* **Quando:** O atendente de `tenant-A` consulta `GET /api/ingressos`.
* **Então:** A resposta contém exclusivamente ingressos de `tenant-A`; zero registros de `tenant-B` são expostos.

### CT-13 (`TC-13`). `ATENDENTE` recebe `HTTP 403` ao tentar acessar rotas de salas, sessões e usuários
* **Critério coberto:** `CA-05` (`AC-5`) | **Requisito:** `RF-02`, `RF-04`, `RF-05` | **Regra:** `RN-08`
* **Nível:** Integração | **Arquivo:** `tests/unit/auth-rbac.test.ts`
* **Dado que:** Usuário autenticado com perfil `ATENDENTE`.
* **Quando:** Tenta acessar `/api/salas`, `/api/sessoes` (`POST`/`DELETE`) e `/api/gestao/usuarios`.
* **Então:** Todas as rotas retornam `HTTP 403 Forbidden` e nenhuma mutação ocorre no banco.

### CT-14 (`TC-14`). Rejeita cadastro de comprador quando qualquer campo obrigatório está ausente
* **Critério coberto:** `CA-06` (`AC-6`) | **Requisito:** `RF-09` | **Regra:** `RN-10`
* **Nível:** Unitário | **Arquivo:** `tests/unit/compliance-anonymization.test.ts`
* **Dado que:** Payloads de cadastro de comprador omitem nome, CPF, e-mail ou consentimento LGPD.
* **Quando:** O caso de uso de validação é executado.
* **Então:** Retorna erro de validação descritivo sem persistir registros e sem concluir a venda.

### CT-15 (`TC-15`). Painel não retorna sessões de outro *tenant*
* **Critério coberto:** `CA-07` (`AC-7`) | **Requisito:** `RF-10` | **Regra:** `RN-12`
* **Nível:** Segurança | **Arquivo:** `tests/unit/security-cross-tenant-suite.test.ts`
* **Dado que:** `tenant-A` e `tenant-B` possuem sessões ativas no dia e o Gerente pertence ao `tenant-A`.
* **Quando:** `GET /api/ocupacao/painel` é invocado.
* **Então:** Apenas sessões do `tenant-A` são retornadas (`HTTP 200`).

### CT-16 (`TC-16`). Criação de filme com campo obrigatório ausente retorna `HTTP 422`
* **Critério coberto:** `CA-08` (`AC-8`) | **Requisito:** `RF-03` | **Regra:** `RN-05`
* **Nível:** Unitário | **Arquivo:** `tests/unit/catalog-filmes.test.ts`
* **Dado que:** Usuário `GERENTE` envia payload de filme omitindo `durationMinutes`.
* **Quando:** `POST /api/filmes` é processado.
* **Então:** Retorna `HTTP 422 Unprocessable Entity` detalhando a violação no campo `durationMinutes`.

### CT-17 (`TC-17`). Endpoint de polling de assentos aplica isolamento `tenant_id`
* **Critério coberto:** `CA-02` (`AC-2`) | **Requisito:** `RF-06` | **Regra:** `RN-12`
* **Nível:** Segurança | **Arquivo:** `tests/unit/session-seats-polling.test.ts`
* **Dado que:** Dois *tenants* distintos possuem sessões e assentos cadastrados.
* **Quando:** `GET /api/sessoes/[id]/assentos` é chamado para uma sessão de `tenant-A`.
* **Então:** Retorna exclusivamente os assentos pertencentes ao `tenant-A`.

### CT-18 (`TC-18`). Registro de auditoria de cancelamento é isolado por `tenant_id`
* **Critério coberto:** `CA-03` (`AC-3`) | **Requisito:** `RF-08` | **Regra:** `RN-07`, `RN-12`
* **Nível:** Segurança | **Arquivo:** `tests/unit/cancelamento-auditavel.test.ts`
* **Dado que:** `tenant-A` e `tenant-B` possuem cancelamentos registrados em `auditoria_cancelamentos`.
* **Quando:** Uma consulta é executada no contexto de `tenant-B`.
* **Então:** Apenas os registros de cancelamento de `tenant-B` são retornados.

### CT-19 (`TC-19`). Query sem contexto de *tenant* lança erro antes de atingir banco
* **Critério coberto:** `CA-04` (`AC-4`) | **Requisito:** `RNF-03` | **Regra:** `RN-12`
* **Nível:** Unitário | **Arquivo:** `tests/unit/tenancy-isolation.test.ts`
* **Dado que:** O Prisma Client Extension é chamado sem `tenantId` definido no contexto.
* **Quando:** Qualquer query sobre entidade de negócio é invocada.
* **Então:** Lança `TenantContextMissingError` antes de executar SQL no banco.

### CT-20 (`TC-20`). `GERENTE` tem acesso completo às rotas de gerenciamento do seu *tenant*
* **Critério coberto:** `CA-05` (`AC-5`) | **Requisito:** `RF-01` | **Regra:** `RN-08`
* **Nível:** Integração | **Arquivo:** `tests/unit/auth-rbac.test.ts`
* **Dado que:** Usuário autenticado com perfil `GERENTE` e `tenant_id` válido.
* **Quando:** Acessa rotas de filmes, salas, sessões e usuários.
* **Então:** A API retorna `HTTP 2xx` para todas as operações autorizadas do seu *tenant*.

### CT-21 (`TC-21`). Reserva atômica bloqueia assento com status `RESERVED` e valida antecedência mínima
* **Critério coberto:** `CA-09` (`AC-9`) | **Requisito:** `RF-13` | **Regra:** `RN-01`, `RN-03`
* **Nível:** Integração | **Arquivo:** `tests/integration/reserva-atomica.test.ts`
* **Dado que:** Um cliente solicita reserva online de um assento `AVAILABLE` para uma sessão que inicia em mais de 60 minutos.
* **Quando:** `POST /api/portal/reservas` é processado em transação atômica.
* **Então:** O assento muda para `RESERVED`, a reserva recebe código `CD-XXXX` e qualquer tentativa concorrente de venda ou reserva sobre o mesmo assento recebe `HTTP 409 Conflict`.

### CT-22 (`TC-22`). Cadastro de cliente final com perfil `CLIENTE`, senha hash e proteção LGPD
* **Critério coberto:** `CA-10` (`AC-10`) | **Requisito:** `RF-14` | **Regra:** `RN-09`, `RN-10`
* **Nível:** Unitário | **Arquivo:** `tests/unit/users-management.test.ts`
* **Dado que:** Um espectador preenche o formulário de cadastro no portal com nome, e-mail, senha, CPF e aceite LGPD.
* **Quando:** `POST /api/portal/cadastro` é executado.
* **Então:** O usuário é salvo com `role = 'CLIENTE'`, senha em hash `bcrypt` (custo 12) e CPF protegido com `HMAC-SHA256` e `AES-256-GCM`.

### CT-23 (`TC-23`). `NotificationService` dispara voucher por e-mail com código da reserva e grava `email_sent_at`
* **Critério coberto:** `CA-11` (`AC-11`) | **Requisito:** `RF-15` | **Regra:** `RN-03`
* **Nível:** Integração | **Arquivo:** `tests/unit/observability-logger.test.ts`
* **Dado que:** Uma reserva online foi criada com status `PENDING`.
* **Quando:** O `NotificationService` processa o envio do comprovante transacional.
* **Então:** O e-mail contendo código localizador, sala, poltronas e prazo limite (60 min antes da sessão) é despachado e o campo `email_sent_at` é atualizado com o `timestamp` UTC.

### CT-24 (`TC-24`). Cancelamento voluntário pelo cliente via web libera assento imediatamente
* **Critério coberto:** `CA-12` (`AC-12`) | **Requisito:** `RF-16` | **Regra:** `RN-02`, `RN-04`
* **Nível:** Integração | **Arquivo:** `tests/integration/reserva-atomica.test.ts`
* **Dado que:** O cliente autenticado possui uma reserva ativa com status `PENDING`.
* **Quando:** Aciona `POST /api/portal/reservas/[id]/cancelar` no painel *"Minhas Reservas"*.
* **Então:** A reserva transita para `CANCELLED` e os respectivos `SessionSeat` retornam imediatamente ao status `AVAILABLE`.

### CT-25 (`TC-25`). Atendente localiza reserva no balcão e confirma pagamento presencial convertendo em `Ticket` (`SOLD`)
* **Critério coberto:** `CA-13` (`AC-13`) | **Requisito:** `RF-17` | **Regra:** `RN-02`, `RN-03`
* **Nível:** Integração | **Arquivo:** `tests/integration/reserva-atomica.test.ts`
* **Dado que:** Uma reserva `PENDING` válida é localizada pelo atendente via código `CD-XXXX` ou CPF na bilheteria.
* **Quando:** O atendente confirma o recebimento presencial em `POST /api/bilheteria/reservas/confirmar`.
* **Então:** O status da reserva muda para `CONFIRMED`, os assentos mudam para `SOLD` e os registros de `Ticket` são emitidos com o identificador do atendente.

### CT-26 (`TC-26`). Reserva não paga até 60 minutos antes da sessão expira *Just-in-Time* liberando assento
* **Critério coberto:** `CA-14` (`AC-14`) | **Requisito:** `RF-18` | **Regra:** `RN-02`, `RN-04`
* **Nível:** Integração | **Arquivo:** `tests/integration/reserva-atomica.test.ts`
* **Dado que:** Uma reserva permanece com status `PENDING` quando faltam menos de 60 minutos para o início da sessão.
* **Quando:** O mapa de assentos é consultado ou uma venda de balcão é realizada para aquela poltrona.
* **Então:** O sistema avalia a expiração *Just-in-Time*, marca a reserva como `EXPIRED` e libera o assento como `AVAILABLE`, permitindo a venda imediata no balcão.
