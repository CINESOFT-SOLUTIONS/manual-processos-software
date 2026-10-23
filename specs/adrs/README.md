# Architecture Decision Records (ADRs) — CineDoom

Registro formal de decisões técnicas e arquiteturais (ISO/IEC/IEEE 12207:2021 – Cláusula 6.3.3) tomadas para a plataforma CineDoom.

---

## Sumário de Decisões

| ID | Título | Status | Data | Impacto Principal |
| :---: | :--- | :---: | :---: | :--- |
| **[ADR-001](#adr-001---arquitetura-monólito-modular-em-nextjs-14)** | Arquitetura Monólito Modular em Next.js 14 | Aprovada | 2026-10-22 | Redução de sobrecarga operacional e coesão de domínio |
| **[ADR-002](#adr-002---interface-reativa-com-tailwind-css-e-react-serverclient-components)** | Interface Reativa com Tailwind CSS e React Server/Client Components | Aprovada | 2026-10-22 | Renderização otimizada do mapa de assentos |
| **[ADR-003](#adr-003---backend-em-typescript-com-route-handlers)** | Backend em TypeScript com Route Handlers | Aprovada | 2026-10-22 | Tipagem unificada ponta a ponta |
| **[ADR-004](#adr-004---banco-de-dados-relacional-postgresql-com-prisma-orm)** | Banco de Dados Relacional PostgreSQL com Prisma ORM | Aprovada | 2026-10-22 | Garantia de transações ACID para bilheteria |
| **[ADR-005](#adr-005---hospedagem-na-vercel-com-neon-serverless-e-github-actions)** | Hospedagem na Vercel com Neon Serverless e GitHub Actions | Aprovada | 2026-10-22 | Deploy automatizado e escalabilidade serverless |
| **[ADR-006](#adr-006---comunicação-via-api-restful-e-polling-de-2s-no-mapa)** | Comunicação via API RESTful e Polling de 2s no Mapa | Aprovada | 2026-10-22 | Simplicidade operacional sem complexidade de WebSockets |
| **[ADR-007](#adr-007---pré-população-de-sessionseat-para-trava-pessimista-select-for-update)** | Pré-população de SessionSeat para Trava Pessimista SELECT FOR UPDATE | Aprovada | 2026-10-23 | Zero double-booking e eliminação de race conditions |
| **[ADR-008](#adr-008---estratégia-criptográfica-de-cpf-hmac-sha256-para-busca-e-aes-256-gcm-para-armazenamento)** | Criptografia de CPF: HMAC-SHA256 para Busca e AES-256-GCM para Armazenamento | Aprovada | 2026-10-23 | Proteção contra rainbow tables no espaço finito de CPFs |
| **[ADR-009](#adr-009---anonimização-in-place-para-lgpd-art-18-sem-quebra-de-fk-do-cdc)** | Anonimização *In-Place* para LGPD Art. 18 sem Quebra de FK do CDC | Aprovada | 2026-10-23 | Conformidade LGPD com integridade referencial contábil (5 anos) |
| **[ADR-010](#adr-010---auditoria-de-cancelamentos-append-only-via-trigger-postgresql)** | Auditoria de Cancelamentos Append-Only via Trigger PostgreSQL | Aprovada | 2026-10-23 | Imutabilidade em nível de banco de dados sem custo de S3 WORM |
| **[ADR-011](#adr-011---log-drain-gerenciado-axiom-para-retenção-de-365-dias-lgpd)** | Log Drain Gerenciado (Axiom) para Retenção de 365 Dias (LGPD) | Aprovada | 2026-10-23 | Observabilidade e retenção legal fora do limite de 1h da Vercel |
| **[ADR-012](#adr-012---portal-do-cliente-autenticação-de-espectador-expiração-just-in-time-e-notificação-transacional)** | Portal do Cliente, Autenticação de Espectador, Expiração Just-in-Time e Notificação Transacional | Aprovada | 2026-10-23 | Reserva online sem gateway com baixa presencial no balcão e expiração atômica |

---

### ADR-001 - Arquitetura Monólito Modular em Next.js 14
* **Contexto:** Necessidade de desenvolver uma aplicação robusta com prazo restrito de 3 semanas (até 12/11/2026), unificando frontend e backend.
* **Decisão:** Adotar Monólito Modular usando Next.js 14 (App Router) em TypeScript. Módulos de catálogo, bilheteria, ocupação e auditoria compartilham infraestrutura com isolamento claro de serviços.
* **Consequências:** Elimina sobrecarga de orquestração de microsserviços, simplifica transações de banco locais e viabiliza a entrega no prazo.

### ADR-002 - Interface Reativa com Tailwind CSS e React Server/Client Components
* **Contexto:** O mapa de assentos da sala precisa ser interativo, de resposta imediata (<2s) e cromática intuitiva para o Atendente de bilheteria.
* **Decisão:** Tailwind CSS para estilização utilitária consistente e React Client Components apenas nos componentes com estado interativo (ex: SeatingGrid), mantendo catálogo em Server Components.
* **Consequências:** Bundle JS otimizado, renderização rápida e experiência fluida no balcão de atendimento.

### ADR-003 - Backend em TypeScript com Route Handlers
* **Contexto:** Garantir tipagem estática e segurança de tipos entre o banco, as validações de schema e as rotas HTTP.
* **Decisão:** Utilizar Route Handlers do Next.js 14 (`app/api/**/route.ts`) com TypeScript estrito (`strict: true`) e validação via Zod.
* **Consequências:** Detecção de erros em tempo de compilação e contratos de API auto-documentados.

### ADR-004 - Banco de Dados Relacional PostgreSQL com Prisma ORM
* **Contexto:** Venda de ingressos de cinema exige estrita consistência transacional (ACID) para impedir conflito de assentos (*double-booking*).
* **Decisão:** PostgreSQL 16+ gerenciado no Neon Serverless com Prisma ORM para modelagem, migrações tipadas e consultas parametrizadas.
* **Consequências:** Garantia matemática de atomicidade e isolamento, prevenindo venda duplicada sob concorrência.

### ADR-005 - Hospedagem na Vercel com Neon Serverless e GitHub Actions
* **Contexto:** Necessidade de ambiente de staging e produção com deploy contínuo e custo operacional zero no MVP.
* **Decisão:** Vercel integrada ao repositório GitHub via GitHub Actions CI/CD e banco de dados hospedado no Neon Serverless.
* **Consequências:** Deploy automático a cada push na branch `main`, pré-visualizações de pull request e zero manutenção de servidores.

### ADR-006 - Comunicação via API RESTful e Polling de 2s no Mapa
* **Contexto:** Atualização do mapa de assentos no balcão com múltiplos terminais abertos simultaneamente.
* **Decisão:** Endpoint HTTP RESTful `GET /api/sessoes/[id]/assentos` com polling a cada 2000ms pelo cliente, em vez de WebSockets ou SSE no MVP.
* **Consequências:** Atende o requisito RNF-01 (<2s de latência), simplifica a infraestrutura serverless e evita conexões persistentes ociosas.

### ADR-007 - Pré-população de SessionSeat para Trava Pessimista SELECT FOR UPDATE
* **Contexto:** Concorrência entre múltiplos atendentes tentando selecionar e comprar o mesmo assento no mesmo milissegundo.
* **Decisão:** Ao criar uma `Session`, o sistema pré-popula uma linha em `session_seats` para cada `Seat` da sala. A transação de venda executa `$queryRaw` com `SELECT id, status FROM session_seats WHERE id = $1 FOR UPDATE`.
* **Consequências:** A linha já existe no banco, garantindo que o lock pessimista do PostgreSQL funcione deterministicamente, retornando `HTTP 409 Conflict` imediatamente para a segunda requisição.

### ADR-008 - Criptografia de CPF: HMAC-SHA256 para Busca e AES-256-GCM para Armazenamento
* **Contexto:** O CPF é dado pessoal sensível segundo a LGPD. O espaço finito de CPFs válidos (~900 milhões) torna o SHA-256 puro vulnerável a ataques de pré-imagem por tabela rainbow se o banco for comprometido.
* **Decisão:** Armazenamento em duas camadas no `CryptoService`:
  1. `cpf_encrypted`: Criptografado com **AES-256-GCM** (chave secreta de 256 bits + IV único).
  2. `cpf_search_hash`: Calculado com **HMAC-SHA256** usando uma chave secreta do servidor (`CINEDOOM_CPF_HMAC_KEY`).
* **Consequências:** Permite busca O(1) indexada no banco sem expor o CPF em texto claro e sem risco de quebra por enumeração ou rainbow table.

### ADR-009 - Anonimização *In-Place* para LGPD Art. 18 sem Quebra de FK do CDC
* **Contexto:** O titular tem direito ao esquecimento (Art. 18 da LGPD), mas o Código de Defesa do Consumidor (CDC Art. 27) e a legislação contábil exigem guarda do histórico fiscal e de vendas por 5 anos.
* **Decisão:** Implementação de soft-anonymization no modelo `Buyer`: ao solicitar exclusão, os campos `name`, `email`, `cpf_encrypted` e `cpf_search_hash` são limpos/anonimizados, e preenche-se `anonymized_at = NOW()`.
* **Consequências:** O registro `Buyer` permanece com seu ID, mantendo íntegras as foreign keys com `Ticket` e `CancellationAudit`, satisfazendo ambas as legislações simultaneamente.

### ADR-010 - Auditoria de Cancelamentos Append-Only via Trigger PostgreSQL
* **Contexto:** A auditoria de cancelamento de ingressos deve ser estritamente imutável (Art. 37 LGPD e auditoria contábil interna).
* **Decisão:** Criação de trigger PostgreSQL em `cancellation_audits` disparado em `BEFORE UPDATE OR DELETE` que lança uma exceção imediata (`RAISE EXCEPTION 'Registros de auditoria são imutáveis'`).
* **Consequências:** Nem mesmo a aplicação com credenciais normais consegue alterar ou expurgar o log de auditoria, garantindo conformidade regulatória sem o custo de um bucket S3 Object Lock no MVP.

### ADR-011 - Log Drain Gerenciado (Axiom) para Retenção de 365 Dias (LGPD)
* **Contexto:** A retenção legal de logs de auditoria e segurança exigida pela LGPD é de no mínimo 365 dias, enquanto a Vercel retém apenas 1 hora no plano básico.
* **Decisão:** Integração do Log Drain da Vercel com a plataforma Axiom (plano generoso e ingestão OpenTelemetry nativa).
* **Consequências:** Logs operacionais e eventos de auditoria são despachados em tempo real e armazenados com retenção de 1 ano, cumprindo os requisitos de auditoria externa.

### ADR-012 - Portal do Cliente, Autenticação de Espectador, Expiração Just-in-Time e Notificação Transacional
* **Contexto:** Necessidade de incorporar o Portal do Cliente para reserva pública de assentos com pagamento presencial no balcão até 1 hora antes da sessão, cadastro/login de cliente, e-mail transacional e cancelamento web.
* **Decisão:** Trava ACID via `session_seats.status = 'RESERVED'`, expiração Just-in-Time no PostgreSQL Neon (`reservation_expires_at > NOW()`), autenticação unificada via NextAuth.js (role `CLIENTE`), envio de voucher por `NotificationService` e endpoint de cancelamento pelo cliente.
* **Consequências:** Solução viável dentro do prazo de 21 dias sem gateway financeiro externo e sem necessidade de daemons/filas assíncronas dedicadas.
