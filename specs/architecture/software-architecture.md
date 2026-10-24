---
kind: agent_artifact
feature_id: F-CINEDOOM-PLATAFORMA-B2B-SAAS-C
agent: Software Architect (C4 L3-4)
generated_by:
  run_id: run_2026-10-23T03-58-17_eedeb0ce
  session_id: 2026-09-03T15-33-01-hdb88xzyiu
  model: anthropic:claude-sonnet-4-6
generated_at: 2026-10-23T04:45:03.412Z
regenerative: true
title: "[Software Architect (C4 L3-4)] CineDoom — plataforma B2B SaaS para cinemas independentes e redes de pequeno/méd"
---

# Software Architect (C4 L3-4) — CineDoom — plataforma B2B SaaS para cinemas independentes e redes de pequeno/méd

> Artefato derivado de `.specs/features/F-CINEDOOM-PLATAFORMA-B2B-SAAS-C/spec.md` e gerado pelo agente **Software Architect (C4 L3-4)**
> via AI-4SDLC Platform. **Regenerative work product** (não-canonical SDD).
> Não edite manualmente — re-gere via `sdlc resume`.

## Resumo

Plano arquitetural de software (C4 L3-L4) para o monólito modular CineDoom MVP integrado aos três módulos: Back-Office do Gerente, Bilheteria do Atendente e Portal do Cliente — define módulos internos, contratos entre camadas, estratégia de trava ACID, isolamento multi-tenant via Prisma Extension, proteção PII/LGPD com CPF cifrado AES-256-GCM, auditoria append-only de cancelamentos e pirâmide de testes, respeitando as decisões macro da Solution Architecture (Next.js 14 + Neon + Vercel).

## Decisões arquiteturais

### AD-1. Clean Architecture e Feature-Driven Architecture (Controller-Service-Repository)

- **Reversível:** sim
- **Racional:** Evolução do padrão Ports & Adapters para Clean Architecture organizada por Feature Slices (`src/features/<modulo>/[domain|application|infrastructure]`). Desacopla integralmente as regras de negócio de detalhes de persistência e transporte HTTP através do padrão Controller-Service-Repository com Inversão de Dependência estrita:
  1. **Controllers (Apresentação / HTTP):** Route Handlers enxutos em `src/app/api/**` que tratam requisições, validam autorização NextAuth, RBAC e contexto de Tenancy via headers.
  2. **Services (Aplicação):** Casos de uso e validação de schemas Zod em `application/`, interagindo exclusivamente com interfaces de repositório.
  3. **Repository Interfaces (Domínio):** Contratos abstratos (`ISaleRepository`, `IFilmRepository`, `IUserRepository`, `ICounterRepository`, etc.) em `domain/`.
  4. **Prisma Repositories (Infraestrutura):** Implementações concretas em `infrastructure/` que encapsulam as queries e travas ACID no Neon PostgreSQL.
- **Quality driver (ISO 25010):** maintainability / testability
- **Build vs. buy:** make
- **Alternativas consideradas:**
  - Transaction Script flat em Route Handlers — _rejeitada:_ acopla domínio a HTTP e Prisma, dificultando teste e evolução
  - Monólito em camadas tradicional não-fatiado (`/controllers`, `/services`, `/repositories` globais) — _rejeitada:_ menor coesão por domínio comparado a Feature Slices

### AD-2. Prisma Client Extension para injeção global de WHERE tenant_id

- **Reversível:** não
- **Racional:** garante AC-4 de forma declarativa e centralizada; Client Extension intercepta toda query model antes da execução, eliminando risco de query sem filtro; impede vazamento cross-tenant mesmo em novos módulos adicionados por membros do time
- **Quality driver (ISO 25010):** security
- **Build vs. buy:** make
- **Alternativas consideradas:**
  - Middleware Prisma legado ($use) — _rejeitada:_ deprecated em Prisma 5+, sem tipagem na extensão
  - RLS nativa PostgreSQL — _rejeitada:_ exigiria SET LOCAL por conexão em serverless pooled, complexidade operacional e testabilidade reduzida

### AD-3. SELECT FOR UPDATE dentro de Prisma.$transaction para trava ACID de assentos

- **Reversível:** não
- **Racional:** garante AC-1 — serializa concorrência no nível de linha do assento sem lock de tabela inteira; Neon Serverless suporta SERIALIZABLE/FOR UPDATE em conexões pooladas via pgBouncer em transaction mode; Prisma expõe $queryRaw para emitir o SELECT FOR UPDATE antes do INSERT de ingresso
- **Quality driver (ISO 25010):** reliability
- **Build vs. buy:** make
- **Alternativas consideradas:**
  - Optimistic locking com version field — _rejeitada:_ gera retry loops em carga alta de concorrência, experiência degradada no pico de estreia
  - Redis SETNX distributed lock — _rejeitada:_ adiciona infra externa desnecessária para MVP sem ganho tangível sobre FOR UPDATE em banco único

### AD-4. AES-256-GCM para cifração de CPF no CryptoService com SHA-256 para campo de busca indexado

- **Reversível:** sim
- **Racional:** cumpre AC-6 e LGPD — o campo cpf_cifrado armazena ciphertext (IV + tag + ciphertext concatenados em base64) para exibição/descriptografia; cpf_hash armazena SHA-256 do CPF normalizado para busca por índice sem expor plaintext; chave simétrica via env var no MVP com rotação manual documentada
- **Quality driver (ISO 25010):** security
- **Build vs. buy:** make
- **Alternativas consideradas:**
  - bcrypt para hash — _rejeitada:_ hash unidirecional impede exibição parcial do CPF ao atendente
  - pgcrypto no banco — _rejeitada:_ exige gestão de chaves no PostgreSQL, vaza chave via pg_stat_activity em log de queries

### AD-5. Auditoria de cancelamentos via tabela append-only com trigger PostgreSQL impedindo UPDATE/DELETE

- **Reversível:** não
- **Racional:** cumpre AC-3 — auditoria_cancelamentos recebe INSERT do CancelamentoService antes de liberar o assento; trigger BEFORE UPDATE OR DELETE lança RAISE EXCEPTION com código P0001, tornando a tabela imutável em nível de banco sem depender de disciplina de código
- **Quality driver (ISO 25010):** reliability
- **Build vs. buy:** make
- **Alternativas consideradas:**
  - Log em arquivo imutável — _rejeitada:_ inacessível para queries de auditoria e difícil de correlacionar com IDs de entidades
  - Event store externo — _rejeitada:_ overhead de infra desproporcional para MVP

### AD-6. ESLint import/no-cycle + módulos com barrel index explícito para enforcement de boundary no CI

- **Reversível:** sim
- **Racional:** cumpre NFR Maintainability — cada módulo (bilheteria, backoffice, auth, tenancy, ocupacao, compradores) expõe apenas o que está no index.ts público; imports cruzando boundary passam pelo index e são auditados pelo no-cycle; CI falha em PR com dependência circular
- **Quality driver (ISO 25010):** maintainability
- **Build vs. buy:** reuse
- **Alternativas consideradas:**
  - NX module boundaries — _rejeitada:_ overhead de migração para NX workspace sem ganho claro em monorepo único
  - TypeScript paths sem lint — _rejeitada:_ não detecta ciclos em runtime

### AD-7. Polling client-side com useEffect + setInterval(2000ms) no SeatMapPollingClient em vez de SSE/WebSocket

- **Reversível:** sim
- **Racional:** cumpre AC-2 e NFR Compatibility — polling é stateless, compatível com Vercel Edge e não requer infra de conexões persistentes; Route Handler GET /api/sessoes/[id]/assentos é cacheável com Cache-Control: no-store; custo de 1 req/2s por terminal ativo é aceitável no horizonte MVP
- **Quality driver (ISO 25010):** compatibility
- **Build vs. buy:** make
- **Alternativas consideradas:**
  - Server-Sent Events — _rejeitada:_ Vercel Serverless Functions têm limite de 60s de streaming, instável com cold start Neon
  - WebSocket via Pusher/Ably — _rejeitada:_ adiciona custo e dependência externa desnecessária para MVP

### AD-8. Pirâmide de testes — Jest unitário (core de domínio puro) + Prisma integration (branch Neon real) + Playwright E2E (Chromium + Firefox)

- **Reversível:** sim
- **Racional:** cumpre todos os @test: mapeados nos ACs; testes de integração rodam contra branch Neon isolado via Neon API no CI, garantindo SELECT FOR UPDATE real em AC-1; Playwright valida NFR Compatibility na matriz de browsers
- **Quality driver (ISO 25010):** reliability
- **Build vs. buy:** reuse
- **Alternativas consideradas:**
  - apenas testes unitários com mocks de Prisma — _rejeitada:_ não valida FOR UPDATE real nem isolamento de tenant em nível de banco
  - Cypress em lugar de Playwright — _rejeitada:_ Playwright tem suporte nativo multi-browser e paralelismo superior no CI


### AD-9. Trava ACID de reservas com status RESERVED e expiração Just-in-Time no PostgreSQL

- **Reversível:** não
- **Racional:** garante AC-9 e AC-14 — a criação de reserva utiliza SELECT FOR UPDATE em session_seats atualizando o status para RESERVED e associando reservation_id e reservation_expires_at; consultas de mapa e tentativas de venda de balcão avaliam a expiração sob demanda (status = 'RESERVED' AND reservation_expires_at <= NOW()), liberando assentos automaticamente sem a necessidade de workers Redis/BullMQ.
- **Quality driver (ISO 25010):** reliability / cost
- **Build vs. buy:** make

### AD-10. NotificationService com adaptador de e-mail transacional desacoplado

- **Reversível:** sim
- **Racional:** cumpre AC-11 — interface NotificationService expõe sendReservationVoucher(reservation) desacoplada de provedor externo; utiliza adaptador Resend/Nodemailer em ambiente de produção e ConsoleLogger em desenvolvimento/testes, registrando email_sent_at na base.
- **Quality driver (ISO 25010):** maintainability
- **Build vs. buy:** buy (Resend) / make (Adapter)

### AD-11. Autenticação e perfil CLIENTE para Portal do Espectador

- **Reversível:** sim
- **Racional:** cumpre AC-10 e AC-12 — amplia o NextAuth.js para suportar role CLIENTE, permitindo que espectadores acessem a área 'Minhas Reservas', visualizem histórico e cancelem voluntariamente reservas pendentes com liberação imediata de assentos.
- **Quality driver (ISO 25010):** usability / security
- **Build vs. buy:** make

### AD-12. Gestão de Mídias de Cartazes via Desacoplamento de URLs e CDN Edge

- **Reversível:** sim
- **Racional:** desacopla o banco relacional dos arquivos estáticos, gravando apenas `poster_url` (`VARCHAR(500)`) na entidade `Film` e rejeitando tipos binários (BLOBs/bytea) no PostgreSQL para manter a performance ACID e respeitar a cota de 0.5 GB do Neon. No MVP, as imagens são servidas como assets locais (`/public/posters/`) pela rede de borda (CDN Edge) da Vercel ou via URLs diretas de CDNs públicas. Para produção em escala (cenário não-mockado), a arquitetura especifica o padrão Direct-to-Storage com Pre-signed URLs (AWS S3/Cloudflare R2/Vercel Blob), contornando o limite de payload de 4.5 MB das funções serverless da Vercel, ou integração com APIs públicas de catálogos cinematográficos (The Movie Database — TMDB).
- **Quality driver (ISO 25010):** performance efficiency / maintainability / cost
- **Build vs. buy:** buy (CDN/Storage) / make (URL reference)
- **Alternativas consideradas:**
  - Armazenar binário BLOB/bytea no PostgreSQL — _rejeitada:_ esgota rapidamente o tier gratuito do Neon e degrada índices/queries
  - Upload binário trafegando pelo servidor Next.js — _rejeitada:_ satura conexões serverless e viola limite de payload de 4.5 MB da Vercel

## Componentes

| ID | Nome | Responsabilidade | Depende de |
|----|------|------------------|------------|
| C-1 | AuthModule | Configuração NextAuth.js com CredentialsProvider + callbacks JWT injetando role (ATENDENTE&#124;GERENTE&#124;CLIENTE) e tenant_id no token; exposição de hook useSession tipado e helper getServerSession para Route Handlers | PrismaClientSingleton |
| C-2 | RBACGuard | Next.js Middleware (middleware.ts) interceptando rotas /gestao/** e /api/gestao/** (com redirecionamento automático de rotas legadas /gerente/** e /backoffice/**); valida role no JWT via getToken; retorna 403 JSON para ATENDENTE e CLIENTE; propaga tenant_id via header x-tenant-id | AuthModule |
| C-3 | TenancyContext | Prisma Client Extension ($extends) que wraps model.findMany/findFirst/update/delete injetando where: { tenant_id: currentTenantId }; currentTenantId lido de AsyncLocalStorage populado pelo RBACGuard a cada request | PrismaClientSingleton |
| C-4 | CryptoService | Serviço puro (sem deps externas além de Node crypto): encryptCPF(plaintext) → base64(IV+tag+ciphertext) usando AES-256-GCM; decryptCPF(ciphertext) → plaintext; hashCPF(plaintext) → HMAC-SHA-256 para indexação; chaves lidas de env | — |
| C-5 | BilheteriaModule | Módulo de Bilheteria com Clean Architecture (features/bilheteria): SaleService, CounterService e CancellationService desacoplados via ISaleRepository, ICounterRepository e ICancellationRepository; Route Handlers enxutos em /api/vendas, /api/bilheteria/** e /api/ingressos | PrismaSaleRepository, PrismaCounterRepository, PrismaCancellationRepository, TenancyContext |
| C-6 | VendaTransactionHandler | Executa Prisma.$transaction com trava pessimista SELECT FOR UPDATE NOWAIT no nível de linha em session_seats; cria Ticket atômico e atualiza assento para 'SOLD'; lança ConflitoAssentoError em disputa | PrismaSaleRepository, TenancyContext |
| C-7 | CancelamentoService | Caso de uso de cancelamento: valida tenant; persiste INSERT em auditoria_cancelamentos (id_ingresso, id_usuario, timestamp_utc, tenant_id, motivo) via ICancellationRepository ANTES de liberar o assento para AVAILABLE | ICancellationRepository, TenancyContext |
| C-8 | AuditoriaRepository | Adapter Prisma exclusivo para auditoria_cancelamentos (PrismaCancellationRepository); tabela protegida por trigger PostgreSQL BEFORE UPDATE OR DELETE RAISE EXCEPTION 'registro imutavel' | PrismaClientSingleton, TenancyContext |
| C-9 | SeatMapRouteHandler | Route Handler GET /api/sessoes/[id]/assentos; responde com Cache-Control: no-store; consome SessionSeatsService desacoplado de ISessionSeatsRepository; resposta ultrarrápida com isolamento por tenant | SessionSeatsService, RBACGuard |
| C-10 | GestaoModule | Módulo de Gestão (Back-office) em features/catalogo e features/identidade: CRUD de filmes, salas e sessões com pré-população de assentos e gestão de usuários; acessível via /gestao/** e /api/gestao/** com validação Zod (AC-8) | FilmService, RoomService, SessionService, UserService, RBACGuard |
| C-11 | CompradoresModule | Registra comprador no ato da venda: valida nome/CPF/e-mail; persiste cpf_hash via HMAC-SHA256 e cpf_cifrado via AES-256-GCM com consentimento LGPD gravado com timestamp UTC | CryptoService, TenancyContext, PrismaClientSingleton |
| C-12 | OcupacaoModule | Agrega dados de ocupação por sessão do dia corrente em features/ocupacao: OccupancyService desacoplado de IOccupancyRepository; exposto via Route Handler GET /api/ocupacao/painel | OccupancyService, TenancyContext, PrismaOccupancyRepository |
| C-13 | SeatMapPollingClient | React Client Component ('use client') com useEffect + setInterval(2000ms) chamando fetch('/api/sessoes/[id]/assentos'); atualiza estado visual com polling resiliente a cada 2 segundos | — |
| C-14 | PrismaClientSingleton | Instância singleton de PrismaClient com $extends de TenancyContext; connection pool Neon serverless com pool_timeout=10s | — |
| C-16 | PortalModule | Módulo do Portal do Cliente: rotas públicas e autenticadas para consulta de catálogo, sessões e assentos; orquestra ReservaTransactionHandler e ClientDashboardModule | TenancyContext, PrismaClientSingleton, AuthModule |
| C-17 | ReservaTransactionHandler | Executa Prisma.$transaction com SELECT FOR UPDATE em session_seats; valida janela de antecedência (>60min antes do início); cria Reservation com status PENDING e atualiza assento para RESERVED | PrismaClientSingleton, TenancyContext, NotificationService |
| C-18 | NotificationService | Serviço de envio de e-mail transacional (voucher da reserva com código, assento, valor e instruções de comparecimento presencial); atualiza email_sent_at | PrismaClientSingleton |
| C-19 | ClientDashboardModule | Área 'Minhas Reservas' do cliente autenticado; lista reservas ativas e histórico; executa cancelamento voluntário de reservas PENDING via rota POST /api/portal/reservas/[id]/cancelar liberando assentos para AVAILABLE | PrismaClientSingleton, TenancyContext |
| C-20 | BaixaReservaHandler | Fluxo de bilheteria presencial: busca reserva por código ou CPF, valida vigência e converte em Ticket vendido ('SOLD') com registro do atendente operador | PrismaClientSingleton, TenancyContext, BilheteriaModule |
| C-15 | ProvisionamentoInternalCLI | Script pnpm run provisionar-tenant executado manualmente pela equipe CineDoom; cria registro em tenants (id, nome, slug, created_at) e usuário GERENTE inicial com senha temporária; sem exposição via API pública | PrismaClientSingleton, CryptoService |

## Riscos

| ID | Descrição | Likelihood | Impacto | Mitigação |
|----|-----------|------------|---------|-----------|
| R-1 | Neon Serverless cold start em conexão poolada pode violar SLA p95 <800ms em endpoint de venda sob carga moderada | medium | high | usar @neondatabase/serverless driver com WebSocket pool persistente; configurar min_pool_size=2 no Neon para manter conexões warm; monitorar p95 via Vercel Analytics desde o primeiro deploy em staging |
| R-2 | Prisma Client Extension não intercepta $queryRaw e $executeRaw — queries brutas emitidas por VendaTransactionHandler não recebem filtro automático de tenant_id | high | high | adicionar tenant_id explicitamente em todos os $queryRaw como parâmetro tipado; lint custom rule proibindo $queryRaw sem tenant_id; revisar em code review checklist |
| R-3 | Hash SHA-256 de CPF sem salt é vulnerável a rainbow table attack pré-computado sobre o espaço finito de CPFs brasileiros (~1B combinações) | medium | high | adicionar HMAC-SHA-256 com chave secreta CINEDOOM_CPF_HMAC_KEY em vez de SHA-256 puro; documentar como decisão de segurança no ADR antes do primeiro deploy em produção |
| R-4 | Polling 2s por sessão ativa multiplica queries ao Neon em dias de estreia com múltiplos terminais simultâneos | medium | medium | adicionar índice composto (sessao_id, tenant_id) na tabela assentos; configurar Connection Pool size máximo no Neon dashboard; considerar cache de 1s com stale-while-revalidate no Route Handler se latência crescer |
| R-5 | Trigger PostgreSQL de imutabilidade de auditoria_cancelamentos pode ser removido por migration Prisma acidental (prisma migrate reset em staging) | low | high | marcar migration do trigger como 'manual' com comentário -- @cinedoom-immutable-trigger; adicionar smoke test pós-deploy que tenta DELETE em auditoria_cancelamentos e espera erro; proteger migration de reset em CI com flag |
| R-6 | Implementação de direito ao esquecimento LGPD via processo manual pela equipe CineDoom sem SLA documentado pode gerar não-conformidade legal | medium | high | documentar SLO de 15 dias úteis para atendimento de requisição de exclusão (prazo LGPD); criar runbook de anonimização (cpf_cifrado=NULL, cpf_hash=NULL, email='anonimizado@cinedoom.internal') executável pela equipe interna |
| R-7 | Múltiplas instâncias Vercel Serverless em paralelo podem criar múltiplas instâncias de PrismaClient quebrando o singleton e esgotando connections no Neon | medium | medium | usar pattern global.__prisma com verificação NODE_ENV; limitar max_connections no Neon pool a 10; monitorar connection count via Neon dashboard nas primeiras semanas pós-launch |
| R-8 | SELECT FOR UPDATE NOWAIT lança erro imediato em conflito — se VendaTransactionHandler não mapear corretamente o erro PG P0002/55P03 para ConflitoAssentoError, o cliente recebe 500 em vez de 409 | low | high | unit test cobrindo o mapeamento de erro Prisma raw para ConflitoAssentoError; integration test AC-1 com 2 transações paralelas validando HTTP 409 na segunda |

## Encryption at-rest

AES-256-GCM para PII de compradores (CPF cifrado) implementado no CryptoService em camada de aplicação. Chave simétrica CINEDOOM_CPF_KEY (32 bytes) e CINEDOOM_CPF_HMAC_KEY gerenciadas como Vercel Environment Variables encrypted-at-rest (Vercel usa AES-256 para secrets em repouso). Neon PostgreSQL Serverless armazena dados em volumes com criptografia AES-256 gerenciada pela Neon (provider-managed). Rotação de chave de aplicação: política máxima de 365 dias com rotação documentada em runbook — processo: gerar nova chave, re-cifrar todos os registros cpf_cifrado em batch com nova chave, atualizar env var, invalidar cache. Customer-managed keys (CMK) não disponíveis no plano Neon MVP — avaliar upgrade para Neon Business com BYOK ou migração para RDS+AWS KMS quando tenant count justificar custo.

## Access control & audit log

RBAC need-to-know implementado no RBACGuard (Next.js middleware): ATENDENTE acessa rotas operacionais (/bilheteria/**, /api/bilheteria/** e /api/sessoes/**/assentos); CLIENTE acessa o portal público (/portal/** e rotas de reserva); GERENTE acessa adicionalmente rotas gerenciais (/gestao/**, /api/gestao/**, /api/ocupacao/** e /api/usuarios/**, com aliases de compatibilidade para /gerente/** e /backoffice/**); qualquer acesso fora do escopo do perfil retorna HTTP 403 com body {error: 'FORBIDDEN', code: 'RBAC_DENIED'}. Audit log IMUTÁVEL: tabela auditoria_cancelamentos com trigger PostgreSQL BEFORE UPDATE OR DELETE RAISE EXCEPTION 'registro imutavel' — garante append-only em nível de banco independente de disciplina de aplicação. Campos auditados por cancelamento: id_ingresso, id_usuario_executante, tenant_id, timestamp_utc, motivo (NOT NULL). Acesso a dados sensíveis de comprador (cpf_cifrado, email) restrito a Server Components/Route Handlers autenticados — jamais expostos em logs de aplicação (Vercel Log Drain configurado com sanitização de campos PII). Futura evolução para WORM recomendada: exportar auditoria_cancelamentos para S3 com Object Lock (Compliance Mode, retention 5 anos) via job semanal quando volume de tenants justificar custo operacional.

## Perguntas em aberto

- Qual o SLO de atendimento de requisição de direito ao esquecimento LGPD (exclusão/anonimização de CPF e e-mail)? Necessário para o runbook de compliance — prazo LGPD sugere máximo 15 dias úteis.
- O campo cpf_hash deve ser HMAC-SHA-256 (com chave secreta) em vez de SHA-256 puro para resistir a rainbow table sobre espaço finito de CPFs? Requer decisão antes do primeiro deploy em produção.
- Existe necessidade de exportar logs de auditoria_cancelamentos para sistema externo (SIEM, S3) ou a tabela PostgreSQL é suficiente como registro permanente no MVP?
- Qual o número máximo esperado de terminais simultâneos por sessão em pico de estreia? Necessário para dimensionar o pool Neon e validar a estratégia de polling 2s sob carga real.
- O provisionamento manual de tenants pela equipe CineDoom tem prazo de atendimento (SLA interno) e fluxo de aprovação documentado para o período pós-launch?
