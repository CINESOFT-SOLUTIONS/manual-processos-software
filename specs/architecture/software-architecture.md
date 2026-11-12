---
document_id: SPEC-CINEDOOM-SOFTWARE-ARCH-001
version: "2.0.0"
date: "2026-11-05"
status: "Aprovado e Consolidado"
standard: "ABNT NBR ISO/IEC/IEEE 12207:2021 (Cláusula 6.4.4 / 6.4.5 — Arquitetura e Design de Software)"
title: "Arquitetura de Software (C4 Níveis 3 e 4) — CineDoom"
---

# Arquitetura de Software (C4 Níveis 3 e 4) — CineDoom

> **Documento Técnico Oficial — CineSoft Solutions (UFG/INF — Processos de Software 2026/1)**
> Rastreabilidade direta com [`cinedoom-spec.md`](../cinedoom-spec.md) (`RF-01` a `RF-18`, `RNF-01` a `RNF-06`, `RN-01` a `RN-12`, `CA-01` a `CA-14`, `RES-01` a `RES-06`) e [`ADR-001` a `ADR-014`](../adr/).

## Resumo Executivo

Especificação detalhada da arquitetura de software (C4 Níveis 3 e 4) para o monólito modular **CineDoom**, abrangendo os três módulos integrados: **Back-Office do Gerente**, **Bilheteria do Atendente** e **Portal do Cliente**. Define a organização interna em *Clean Architecture* orientada a funcionalidades (*Feature-Driven Architecture*), contratos entre camadas (`Controller -> Service -> Repository`), estratégia de trava pessimista ACID (`SELECT FOR UPDATE`), isolamento multi-tenant via *Prisma Client Extension*, proteção criptográfica de PII/LGPD (`HMAC-SHA256` + `AES-256-GCM`), auditoria *append-only* de cancelamentos e pirâmide de testes automatizados com **Vitest** e **Playwright**.

---

## 1. Decisões de Design e Arquitetura de Software

### AD-1. Clean Architecture e Feature-Driven Architecture (Padrão Controller-Service-Repository) (`ADR-001`)

- **Reversível:** Sim
- **Racional:** Organiza o código-fonte em fatias verticais de domínio (`src/features/<modulo>/[domain|application|infrastructure]`), desacoplando integralmente as regras de negócio de detalhes de persistência e transporte HTTP por meio de Inversão de Dependência estrita (`RNF-06`):
  1. **Controllers (Apresentação / HTTP):** Route Handlers enxutos em `src/app/api/**` que tratam requisições HTTP, validam sessão NextAuth, aplicam RBAC e extraem o contexto de Tenancy.
  2. **Services (Aplicação):** Orquestração de casos de uso e validação de esquemas Zod em `application/`, interagindo exclusivamente com interfaces abstratas de repositório.
  3. **Interfaces de Repositório (Domínio):** Contratos puros (`ISaleRepository`, `IFilmRepository`, `IUserRepository`, `ICounterRepository`, etc.) definidos em `domain/`.
  4. **Prisma Repositories (Infraestrutura):** Implementações concretas em `infrastructure/` que encapsulam as consultas SQL e travas ACID no Supabase PostgreSQL.
- **Atributo de Qualidade (ISO/IEC 25010):** Manutenibilidade e Testabilidade (*Maintainability / Testability*)
- **Estratégia (*Build vs. Buy*):** Construção própria (*Make*)
- **Alternativas consideradas:**
  - *Transaction Script* diretamente nos Route Handlers — *rejeitada:* acopla regras de negócio ao protocolo HTTP e ao ORM, prejudicando testes unitários isolados.
  - Monólito em camadas horizontais globais (`/controllers`, `/services`, `/repositories`) — *rejeitada:* menor coesão modular em comparação com *Feature Slices*.

### AD-2. Prisma Client Extension para injeção global de `WHERE tenant_id` (`ADR-003`)

- **Reversível:** Não
- **Racional:** Garante o critério de aceite `CA-04` (`AC-4`), o requisito `RNF-03` e a regra `RN-12` de forma declarativa e centralizada; a *Client Extension* intercepta toda operação de modelo antes da execução no PostgreSQL, eliminando o risco de consultas sem filtro de locatário.
- **Atributo de Qualidade (ISO/IEC 25010):** Segurança (*Security*)
- **Estratégia (*Build vs. Buy*):** Construção própria (*Make*)
- **Alternativas consideradas:**
  - Middleware legado do Prisma (`$use`) — *rejeitada:* depreciado a partir do Prisma 5+.
  - Row-Level Security (RLS) nativa do PostgreSQL via `SET LOCAL` — *rejeitada:* aumenta a complexidade em conexões efêmeras gerenciadas por PgBouncer em modo transacional.

### AD-3. `SELECT FOR UPDATE` dentro de `Prisma.$transaction` para trava ACID de poltronas (`ADR-005`)

- **Reversível:** Não
- **Racional:** Garante `CA-01` (`AC-1`), `RF-06`, `RNF-02` e `RN-05` — serializa disputas concorrentes no nível da linha da poltrona (`session_seats`) sem bloquear a tabela inteira; retorna imediatamente `HTTP 409 Conflict` para transações concorrentes perdedoras.
- **Atributo de Qualidade (ISO/IEC 25010):** Confiabilidade (*Reliability*)
- **Estratégia (*Build vs. Buy*):** Construção própria (*Make*)
- **Alternativas consideradas:**
  - Bloqueio otimista (*Optimistic Locking*) com coluna de versão — *rejeitada:* degrada a experiência em picos de alta concorrência (50 threads simultâneas).
  - Lock distribuído via Redis (`SETNX`) — *rejeitada:* introduz dependência de infraestrutura externa desnecessária quando o próprio PostgreSQL resolve a atomicidade na mesma transação.

### AD-4. Cifragem `AES-256-GCM` e hash `HMAC-SHA256` no `CryptoService` (`ADR-008`)

- **Reversível:** Sim
- **Racional:** Cumpre `CA-06` (`AC-6`), `RF-09`, `RNF-03` e `RN-07` — o campo `cpf_encrypted` armazena o texto cifrado autenticado (`IV + AuthTag + Ciphertext` em Base64) e `cpf_hash` armazena o resumo determinístico `HMAC-SHA256` (com chave secreta `CINEDOOM_CPF_HMAC_KEY`) para busca indexada sem exposição do CPF em texto claro e com resistência total a *rainbow tables*.
- **Atributo de Qualidade (ISO/IEC 25010):** Segurança (*Security*)
- **Estratégia (*Build vs. Buy*):** Construção própria (*Make*)
- **Alternativas consideradas:**
  - `bcrypt` para o CPF — *rejeitada:* algoritmo com salt aleatório por chamada impede busca indexada `O(1)` por igualdade na coluna `cpf_hash`.
  - Extensão `pgcrypto` diretamente no banco — *rejeitada:* exporia o CPF em texto plano no tráfego entre aplicação e banco e nos logs de consultas SQL.

### AD-5. Auditoria de cancelamentos em tabela *append-only* com trigger PostgreSQL (`ADR-006`)

- **Reversível:** Não
- **Racional:** Cumpre `CA-03` (`AC-3`), `RF-08` e `RN-06` — a tabela `cancellation_audits` recebe o `INSERT` do serviço de cancelamento **antes** da liberação do assento para `AVAILABLE`; um trigger `BEFORE UPDATE OR DELETE` no PostgreSQL lança `RAISE EXCEPTION` com código `P0001`, tornando os registros imutáveis no nível do SGBD.
- **Atributo de Qualidade (ISO/IEC 25010):** Confiabilidade (*Reliability*)
- **Estratégia (*Build vs. Buy*):** Construção própria (*Make*)

### AD-6. Fronteiras modulares com `ESLint import/no-cycle` e *barrel exports* (`ADR-011`)

- **Reversível:** Sim
- **Racional:** Cumpre `RNF-06` (Manutenibilidade) — cada módulo expõe apenas sua API pública por meio de um arquivo `index.ts`; a regra `import/no-cycle` no pipeline de CI garante zero dependências circulares entre módulos (`CT-17`).
- **Atributo de Qualidade (ISO/IEC 25010):** Manutenibilidade (*Maintainability*)
- **Estratégia (*Build vs. Buy*):** Reúso (*Reuse*)

### AD-7. Polling client-side a cada 2 segundos no `SeatMapPollingClient` (`ADR-007`)

- **Reversível:** Sim
- **Racional:** Cumpre `CA-02` (`AC-2`), `RF-05`, `RNF-01` e `RNF-05` — utiliza `useEffect` + `setInterval(2000)` consultando `GET /api/sessoes/[id]/assentos` com cabeçalho `Cache-Control: no-store`, garantindo atualização visual em até 2 segundos sem exigir conexões WebSocket persistentes na Vercel.
- **Atributo de Qualidade (ISO/IEC 25010):** Compatibilidade (*Compatibility*)
- **Estratégia (*Build vs. Buy*):** Construção própria (*Make*)

### AD-8. Pirâmide de testes automatizados com Vitest e Playwright (`ADR-011`)

- **Reversível:** Sim
- **Racional:** Cobertura integral dos critérios de aceite `CA-01` a `CA-14` (`AC-1` a `AC-14`) e dos 26 casos de teste (`CT-01` a `CT-26`); utiliza **Vitest** para testes unitários, de segurança (500 cenários cross-tenant) e de integração concorrente (50 threads simultâneas), e **Playwright** para testes fim a fim (E2E) na matriz Chromium e Firefox em resolução `1024x768` (`RNF-05`).
- **Atributo de Qualidade (ISO/IEC 25010):** Confiabilidade e Testabilidade (*Reliability / Testability*)
- **Estratégia (*Build vs. Buy*):** Reúso (*Reuse*)

### AD-9. Reserva online com status `RESERVED` e expiração *Just-in-Time* no PostgreSQL (`ADR-012`)

- **Reversível:** Não
- **Racional:** Garante `CA-09` (`AC-9`), `CA-14` (`AC-14`), `RF-13`, `RF-18`, `RN-08` e `RN-11` — a reserva bloqueia a poltrona com `SELECT FOR UPDATE` atribuindo `status = 'RESERVED'` e `reservation_expires_at = starts_at - 60 min`; consultas ao mapa de assentos e operações de venda avaliam a expiração sob demanda (`status = 'RESERVED' AND reservation_expires_at <= NOW()`), liberando poltronas vencidas automaticamente sem depender de filas em background.
- **Atributo de Qualidade (ISO/IEC 25010):** Confiabilidade e Eficiência de Custos (*Reliability / Cost*)
- **Estratégia (*Build vs. Buy*):** Construção própria (*Make*)

### AD-10. `NotificationService` com adaptador de e-mail transacional desacoplado (`ADR-013`)

- **Reversível:** Sim
- **Racional:** Cumpre `CA-11` (`AC-11`) e `RF-15` — a interface `NotificationService` expõe `sendReservationVoucher(reservation)` desacoplada do provedor de transporte, utilizando Resend/SMTP em produção e logger estruturado em ambiente de testes, gravando o carimbo `email_sent_at`.
- **Atributo de Qualidade (ISO/IEC 25010):** Manutenibilidade (*Maintainability*)
- **Estratégia (*Build vs. Buy*):** Híbrida (*Buy* / *Make*)

### AD-11. Autenticação de espectadores com perfil `CLIENTE` no Portal (`ADR-014`)

- **Reversível:** Sim
- **Racional:** Cumpre `CA-10` (`AC-10`), `CA-12` (`AC-12`), `RF-14`, `RF-16` e `RN-09` — estende o NextAuth.js com o papel `CLIENTE`, permitindo acesso autenticado à área "Minhas Reservas" e cancelamento voluntário com proteção estrita contra IDOR (`user_id === session.user.id`).
- **Atributo de Qualidade (ISO/IEC 25010):** Usabilidade e Segurança (*Usability / Security*)
- **Estratégia (*Build vs. Buy*):** Construção própria (*Make*)

### AD-12. Gestão de mídias de cartazes via desacoplamento de URLs e CDN Edge

- **Reversível:** Sim
- **Racional:** Armazena exclusivamente a referência `poster_url` (`VARCHAR(500)`) na entidade `Film`, rejeitando objetos binários (`BLOB/bytea`) no PostgreSQL para preservar a cota do banco de dados no Supabase (`RES-01`) e a velocidade das consultas; distribui os cartazes estáticos pela CDN Edge da Vercel.
- **Atributo de Qualidade (ISO/IEC 25010):** Eficiência de Desempenho e Custo (*Performance Efficiency / Cost*)
- **Estratégia (*Build vs. Buy*):** Híbrida (*Buy* CDN / *Make* referência URL)

---

## 2. Catálogo de Componentes Internos (C4 Nível 3)

| ID | Componente / Módulo | Responsabilidade Técnica | Depende de |
|----|---------------------|--------------------------|------------|
| **C-1** | `AuthModule` | Configuração do NextAuth.js (`CredentialsProvider`) + callbacks JWT injetando `role` (`ATENDENTE`, `GERENTE`, `CLIENTE`) e `tenant_id` no token; helpers tipados de sessão (`RF-01`, `RF-14`). | `PrismaClientSingleton` |
| **C-2** | `RBACGuard` | Middleware Next.js (`middleware.ts`) interceptando rotas protegidas (`/gestao/**`, `/api/gestao/**`, `/bilheteria/**`, `/portal/minhas-reservas`); valida `role` no JWT e retorna `HTTP 403` para acessos não autorizados (`RN-01`, `CA-05`). | `AuthModule` |
| **C-3** | `TenancyContext` | *Prisma Client Extension* (`$extends`) que intercepta operações CRUD injetando `where: { tenant_id: currentTenantId }` lido de `AsyncLocalStorage` (`RN-12`, `CA-04`). | `PrismaClientSingleton` |
| **C-4** | `CryptoService` | Serviço criptográfico puro (`node:crypto`): `encryptCPF(plaintext)` via `AES-256-GCM`, `decryptCPF(ciphertext)` e `hashCPF(plaintext)` via `HMAC-SHA256` (`RF-09`, `RN-07`, `CA-06`). | — |
| **C-5** | `BilheteriaModule` | Módulo de Bilheteria em `src/features/bilheteria`: `SaleService`, `CounterService` e `CancellationService` desacoplados por interfaces de domínio (`RF-06`, `RF-07`, `RF-08`, `RF-17`). | `PrismaSaleRepository`, `PrismaCounterRepository`, `PrismaCancellationRepository`, `TenancyContext` |
| **C-6** | `VendaTransactionHandler` | Executa `Prisma.$transaction` com trava pessimista `SELECT FOR UPDATE NOWAIT` em `session_seats`; cria `Ticket` atômico e atualiza poltrona para `SOLD`, ou lança `ConflitoAssentoError` (`HTTP 409`) (`RN-05`, `CA-01`). | `PrismaSaleRepository`, `TenancyContext` |
| **C-7** | `CancelamentoService` | Caso de uso de cancelamento presencial: valida tenant, insere registro em `cancellation_audits` **antes** de liberar a poltrona para `AVAILABLE` (`RF-08`, `RN-06`, `CA-03`). | `ICancellationRepository`, `TenancyContext` |
| **C-8** | `AuditoriaRepository` | Adaptador Prisma para `cancellation_audits` (`PrismaCancellationRepository`); tabela protegida por trigger PostgreSQL `BEFORE UPDATE OR DELETE` (`CA-03`). | `PrismaClientSingleton`, `TenancyContext` |
| **C-9** | `SeatMapRouteHandler` | Route Handler `GET /api/sessoes/[id]/assentos` com `Cache-Control: no-store`; consome `SessionSeatsService` e aplica expiração JIT antes de retornar os estados (`RF-05`, `RF-18`, `CA-02`, `CA-14`). | `SessionSeatsService`, `RBACGuard` |
| **C-10** | `GestaoModule` | Módulo de Back-office em `src/features/catalogo` e `src/features/identidade`: CRUD de filmes, salas, sessões (com pré-população de `SessionSeat`) e operadores, validado com Zod (`RF-01` a `RF-04`, `RN-02` a `RN-04`, `CA-08`). | `FilmService`, `RoomService`, `SessionService`, `UserService`, `RBACGuard` |
| **C-11** | `CompradoresModule` | Registra comprador no ato da venda e processa anonimização *in-place* (Art. 18 LGPD) via `/api/titulares/anonimizar` (`RF-09`, `CA-06`, `ADR-009`). | `CryptoService`, `TenancyContext`, `PrismaClientSingleton` |
| **C-12** | `OcupacaoModule` | Calcula indicadores agregados de ocupação por sessão do dia corrente (`OccupancyService` / `GET /api/ocupacao/painel`) isolados por tenant (`RF-10`, `CA-07`). | `OccupancyService`, `TenancyContext`, `PrismaOccupancyRepository` |
| **C-13** | `SeatMapPollingClient` | Client Component React com `useEffect` + `setInterval(2000ms)` atualizando reativamente o mapa de poltronas (`RF-05`, `CA-02`). | — |
| **C-14** | `PrismaClientSingleton` | Instância singleton de `PrismaClient` estendida com `TenancyContext` e conectada ao banco Supabase PostgreSQL via pool de conexões. | — |
| **C-15** | `ProvisionamentoInternalCLI` | Script administrativo (`pnpm run provisionar-tenant`) para criação controlada de novos cinemas tenants e conta inicial de `GERENTE` (`RES-03`). | `PrismaClientSingleton`, `CryptoService` |
| **C-16** | `PortalModule` | Módulo do Portal do Cliente: rotas públicas de catálogo e grade de exibição (`/portal/**`) e orquestração do checkout de reserva (`RF-12`, `RF-13`). | `TenancyContext`, `PrismaClientSingleton`, `AuthModule` |
| **C-17** | `ReservaTransactionHandler` | Executa `Prisma.$transaction` com `SELECT FOR UPDATE` em `session_seats`; valida antecedência mínima (> 60 min), cria `Reservation` (`PENDING`) com código `CD-XXXX` e marca assento como `RESERVED` (`RF-13`, `RN-08`, `CA-09`). | `PrismaClientSingleton`, `TenancyContext`, `NotificationService` |
| **C-18** | `NotificationService` | Serviço de disparo de e-mail transacional contendo o voucher da reserva e instruções de comparecimento presencial; registra `email_sent_at` (`RF-15`, `CA-11`). | `PrismaClientSingleton` |
| **C-19** | `ClientDashboardModule` | Painel autenticado "Minhas Reservas" do espectador; lista reservas e processa cancelamento voluntário em `POST /api/portal/reservas/[id]/cancelar` (`RF-16`, `RN-09`, `CA-12`). | `PrismaClientSingleton`, `TenancyContext` |
| **C-20** | `BaixaReservaHandler` | Caso de uso de bilheteria presencial (`CounterService`): localiza reserva por código `CD-XXXX` ou CPF (`cpf_hash`), valida vigência e converte em `Ticket` vendido (`SOLD`) (`RF-17`, `RN-10`, `CA-13`). | `PrismaClientSingleton`, `TenancyContext`, `BilheteriaModule` |

---

## 3. Riscos Técnicos de Implementação e Mitigações

| ID | Descrição do Risco Técnico | Probabilidade | Impacto | Mitigação Implementada no Código |
|----|----------------------------|---------------|---------|----------------------------------|
| **R-1** | *Cold start* em conexão serverless elevar a latência do endpoint de venda acima de 800ms (`RNF-01`). | Média | Alto | Uso de connection pooling gerenciado no Supabase e queries enxutas dentro da transação ACID. |
| **R-2** | Consultas SQL brutas (`$queryRaw`) não serem interceptadas automaticamente pela *Prisma Client Extension*. | Alta | Alto | Parametrização explícita e obrigatória de `tenant_id` em toda chamada `$queryRaw` do `VendaTransactionHandler`, auditada pela suíte de 500 cenários (`CA-04`). |
| **R-3** | Reversão de hash de CPF por *rainbow table* caso fosse utilizado SHA-256 simples. | Média | Alto | Substituição definitiva por **`HMAC-SHA256`** com segredo `CINEDOOM_CPF_HMAC_KEY` no `CryptoService` (`ADR-008`, `CT-06`). |
| **R-4** | Sobrecarga de leituras pelo polling de 2 segundos em sessões de grande procura. | Média | Médio | Índice composto `(session_id, status)` na tabela `session_seats` e resposta JSON minimalista (`CT-10`). |
| **R-5** | Remoção acidental do trigger de imutabilidade de `cancellation_audits` em migrações futuras. | Baixa | Alto | Teste automatizado específico (`CT-03`, `CT-14`) no pipeline de CI que tenta executar `UPDATE/DELETE` na tabela de auditoria e exige exceção do banco. |
| **R-6** | Solicitação de exclusão de dados (Art. 18 LGPD) violar chaves estrangeiras de ingressos fiscais já vendidos. | Média | Alto | Implementação de *soft-anonymization in-place* (`ADR-009`, `/api/titulares/anonimizar`), sobrescrevendo PII sem apagar a chave primária referenciada por `tickets`. |
| **R-7** | Criação excessiva de instâncias `PrismaClient` em recarregamentos de funções serverless. | Média | Médio | Padrão *Singleton* atrelado a `globalThis.__prisma` em `src/lib/prisma.ts`. |
| **R-8** | Conflito de trava `SELECT FOR UPDATE NOWAIT` retornar erro genérico `HTTP 500` em vez de `HTTP 409`. | Baixa | Alto | Mapeamento explícito de códigos de erro PostgreSQL (`55P03` / `P2034`) para `ConflitoAssentoError` (`HTTP 409 Conflict`), validado em `CT-01` e `CT-09`. |

---

## 4. Criptografia em Repouso e Gestão de Segredos

O módulo `CryptoService` implementa criptografia autenticada **`AES-256-GCM`** para o campo `cpf_encrypted` e resumo criptográfico **`HMAC-SHA256`** para o campo indexado `cpf_hash` (`ADR-008`). As chaves simétricas de 256 bits (`CPF_ENCRYPTION_KEY` e `CINEDOOM_CPF_HMAC_KEY`) são armazenadas exclusivamente como variáveis cifradas em repouso no cofre da Vercel (*Vercel Environment Secrets*). A política de rotação prevê substituição máxima a cada 365 dias por meio de script de re-cifragem em lote sem indisponibilidade.

---

## 5. Controle de Acesso (RBAC) e Trilha de Auditoria

O controle de acesso *need-to-know* é aplicado pelo `RBACGuard` e revalidado nos serviços de aplicação (`RF-01`, `RN-01`, `CA-05`):
- **`ATENDENTE`:** Acessa `/bilheteria/**`, `/api/vendas`, `/api/bilheteria/**`, `/api/ingressos/**` e `/api/sessoes/**/assentos`.
- **`CLIENTE`:** Acessa `/portal/**` e `/api/portal/**`.
- **`GERENTE`:** Acessa todas as rotas operacionais do seu cinema mais `/gestao/**`, `/api/gestao/**`, `/api/ocupacao/**` e `/api/usuarios/**` (incluindo redirecionamento automático de rotas legadas `/gerente/**` e `/backoffice/**`).
- Qualquer tentativa de acesso fora do escopo do perfil retorna `HTTP 403 Forbidden` (`{ error: 'FORBIDDEN', code: 'RBAC_DENIED' }`).
- A tabela `cancellation_audits` mantém trilha *append-only* protegida por trigger PostgreSQL (`RN-06`, `CA-03`), complementada pela exportação de logs estruturados (sem PII em claro) para o Axiom Log Drain com retenção de 365 dias (`RF-11`).
