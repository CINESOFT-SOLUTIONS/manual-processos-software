---
document_id: SPEC-CINEDOOM-THREAT-MODEL-001
version: "2.0.0"
date: "2026-11-05"
status: "Aprovado — Controles Implementados e Verificados"
standard: "ABNT NBR ISO/IEC/IEEE 12207:2021 (Cláusula 6.4.4 / 6.4.10) & STRIDE"
title: "Modelagem de Ameaças (STRIDE e Cadeia de Suprimentos) — CineDoom"
---

# Modelagem de Ameaças (STRIDE e Cadeia de Suprimentos) — CineDoom

> **Documento Técnico Oficial — CineSoft Solutions (UFG/INF — Processos de Software 2026/1)**
> Rastreabilidade direta com [`cinedoom-spec.md`](../cinedoom-spec.md) (`RNF-03`, `RN-01`, `RN-06`, `RN-07`, `RN-12`, `CA-03`, `CA-04`, `CA-05`, `CA-06`) e [`ADR-004` a `ADR-014`](../adr/).

## 1. Resumo Executivo

Modelagem de ameaças utilizando a metodologia **STRIDE** (*Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege*) combinada com análise de cadeia de suprimentos (*Supply Chain*) para a plataforma **CineDoom**.

Durante a fase inicial de arquitetura, duas ameaças críticas (`T-1` e `T-2`) foram identificadas como bloqueadoras de *go-live*:
1. **`T-1` (Hash de CPF vulnerável a *Rainbow Table*):** Mitigada integralmente por meio da substituição do SHA-256 simples por **`HMAC-SHA256`** com chave secreta dedicada (`CINEDOOM_CPF_HMAC_KEY`), conforme formalizado no **[`ADR-008`](../adr/ADR-008-protecao-cpf-hmac-sha256-aes256gcm.md)** e implementado no módulo `CryptoService`.
2. **`T-2` (Gestão de chaves criptográficas de PII):** Mitigada pelo armazenamento exclusivo de `CPF_ENCRYPTION_KEY` (AES-256-GCM) e `CINEDOOM_CPF_HMAC_KEY` no cofre cifrado **Vercel Environment Secrets**, com política documentada de rotação anual em lote (`ADR-008`).

Todas as 17 ameaças mapeadas (`T-1` a `T-17`) possuem controles ativos implementados e validados por testes automatizados na suíte de integração e segurança (`711 testes` aprovados, incluindo a bateria de 500 cenários cross-tenant em [`security-cross-tenant-suite.md`](../quality/security-cross-tenant-suite.md)).

---

## 2. Veredito de Segurança para Go-Live

- **Decisão:** `APROVADO (Controles Mitigados e Verificados em CI)`
- **Verificação de Segredos (*Secrets Check*):** Aprovada (zero segredos em código-fonte)
- **Bloqueadores Pendentes (*Blockers*):** `0` (T-1 e T-2 resolvidos via `ADR-008` e `TASK-5`)
- **Suíte de Isolamento Multi-tenant (`CA-04`):** `500/500 cenários aprovados` (`CT-04`, `CT-18`)

---

## 3. Matriz de Ameaças STRIDE (`T-1` a `T-17`)

| ID | Categoria STRIDE | Probabilidade | Impacto | Descrição da Ameaça | Estratégia de Mitigação Arquitetural | Status / Controle Implementado |
|----|------------------|---------------|---------|---------------------|--------------------------------------|--------------------------------|
| **T-1** | Divulgação de Informação (*Information Disclosure*) | Alta | Alto | CPF armazenado como hash SHA-256 puro (sem HMAC/salt) seria vulnerável a ataque de *rainbow table* e força bruta dado o espaço finito de CPFs brasileiros (~900 milhões de combinações com dígitos verificadores), permitindo reverter o hash para o CPF real. | Substituir SHA-256 puro por **`HMAC-SHA256`** com chave secreta server-side (`CINEDOOM_CPF_HMAC_KEY`), inviabilizando *rainbow tables* pré-computadas. | **Mitigado (`ADR-008`, `RF-09`, `CA-06`, `CT-06`)** — Implementado em `CryptoService.hashCPF()`. |
| **T-2** | Divulgação de Informação (*Information Disclosure*) | Alta | Alto | Chave `AES-256-GCM` usada para cifrar o CPF dos compradores sem gestão de segredos dedicada: vazamento simultâneo de dump do banco e arquivo `.env` comprometeria a base de PII. | Armazenar `CPF_ENCRYPTION_KEY` e `CINEDOOM_CPF_HMAC_KEY` exclusivamente em *Vercel Environment Secrets* cifrados; proibir commit de `.env`; rotação anual documentada em runbook. | **Mitigado (`ADR-008`, `RNF-03`, `CT-06`)** — Chaves isoladas por ambiente e validadas no boot. |
| **T-3** | Vazamento de Segredos (*Secret Leak*) | Média | Alto | `DATABASE_URL` (Neon), `NEXTAUTH_SECRET` e chaves criptográficas podem ser comitados acidentalmente ou expostos em logs de build. | `.env*` estritamente bloqueado no `.gitignore`; variáveis sensíveis injetadas via cofre da Vercel; sanitização de variáveis no pipeline GitHub Actions. | **Mitigado (`ADR-010`)** — Verificado no pipeline de CI. |
| **T-4** | Divulgação de Informação (*Information Disclosure*) | Média | Alto | Ambientes de *preview* da Vercel gerados por branch poderiam apontar para banco de produção/staging contendo dados reais de titulares. | Ambientes de *preview* utilizam exclusivamente branches efêmeros do Neon PostgreSQL populados apenas com dados sintéticos de *seed*. | **Mitigado (`ADR-002`, `ADR-010`)** — Isolamento de branches Neon configurado. |
| **T-5** | Elevação de Privilégio (*Elevation of Privilege*) | Média | Alto | Papel (`ATENDENTE`, `GERENTE`, `CLIENTE`) validado apenas no middleware de borda sem revalidação nos Route Handlers permitiria bypass em chamadas diretas. | Dupla verificação de autorização: validação no `RBACGuard` (middleware Next.js) e revalidação do token JWT e `tenant_id` na camada de Controller/Service. | **Mitigado (`ADR-004`, `RF-01`, `CA-05`, `CT-05`, `CT-16`)** — Validado por testes de RBAC. |
| **T-6** | Elevação de Privilégio (*Elevation of Privilege*) | Média | Alto | Manipulação de `tenant_id` via cabeçalhos HTTP (`x-tenant-id`), query string ou payload JSON para acessar recursos de outro cinema concorrente. | `TenancyContext` extrai `tenant_id` exclusivamente da sessão JWT autenticada e injeta `WHERE tenant_id` via *Prisma Client Extension*, ignorando cabeçalhos ou parâmetros externos. | **Mitigado (`ADR-003`, `RN-12`, `CA-04`, `CT-04`, `CT-18`)** — Validado por 500 cenários automatizados. |
| **T-7** | Falsificação de Identidade (*Spoofing*) | Média | Alto | Roubo de cookie de sessão NextAuth via XSS ou interceptação de rede em conexões não seguras. | Cookies configurados com `HttpOnly`, `Secure` e `SameSite=Lax/Strict`; tráfego HTTPS compulsório na Vercel Edge Network; TTL de sessão limitado a 8 horas. | **Mitigado (`ADR-004`, `RNF-03`)** — Configuração ativa no NextAuth.js. |
| **T-8** | Adulteração (*Tampering*) | Média | Alto | Exclusão ou alteração maliciosa de registros na tabela `cancellation_audits` para ocultar cancelamentos fraudulentos de ingressos no caixa. | Tabela *append-only* protegida por trigger PostgreSQL `BEFORE UPDATE OR DELETE` que lança exceção imediata (`P0001: registro imutavel`), além de restrição no repositório. | **Mitigado (`ADR-006`, `RF-08`, `RN-06`, `CA-03`, `CT-03`, `CT-14`)** — Trigger testado em suíte de integração. |
| **T-9** | Repúdio (*Repudiation*) | Média | Médio | Operador realiza vendas ou cancelamentos contestando posteriormente a autoria da operação. | Todo `Ticket` registra obrigatoriamente `sold_by_user_id` e `sold_at` (UTC); todo cancelamento grava `cancelled_by_user_id`, `cancelled_at` (UTC) e `reason` em tabela imutável, além de log no Axiom por 365 dias. | **Mitigado (`RF-06`, `RF-08`, `RF-11`, `CA-03`)** — Rastreabilidade completa de operador. |
| **T-10** | Negação de Serviço (*Denial of Service*) | Média | Alto | Polling de 2s por múltiplos terminais simultâneos em `GET /api/sessoes/[id]/assentos` pode saturar o pool de conexões do banco serverless. | Roteamento das consultas de leitura pelo *Neon Connection Pooler* (PgBouncer gerenciado) e índice composto `idx_session_seats_session_status`. | **Mitigado (`ADR-002`, `ADR-007`, `RNF-01`, `CT-10`)** — Latência p95 < 300ms no polling. |
| **T-11** | Negação de Serviço (*Denial of Service*) | Baixa | Médio | Contenção de trava pessimista (`SELECT FOR UPDATE`) sob alta concorrência (50+ requisições simultâneas no mesmo assento) gerando *deadlock* ou *lock wait timeout*. | Uso de `SELECT ... FOR UPDATE NOWAIT` (ou timeout determinístico de 3s) dentro de `Prisma.$transaction`, convertendo falhas de bloqueio imediatamente em `HTTP 409 Conflict`. | **Mitigado (`ADR-005`, `RNF-02`, `CA-01`, `CT-01`, `CT-09`)** — Validado com 50 threads simultâneas. |
| **T-12** | Divulgação de Informação (*Information Disclosure*) | Média | Médio | Logs de aplicação e rastreamento de erros capturando CPF em texto plano ou e-mail do comprador durante exceções. | Logger estruturado sanitiza e mascara campos sensíveis (`cpf`, `cpf_encrypted`, `password`) antes do envio ao Axiom Log Drain. | **Mitigado (`RF-11`, `RNF-03`, `CT-15`)** — Política zero-PII em logs. |
| **T-13** | Adulteração (*Tampering*) | Baixa | Médio | Envio de payload malformado no campo `layout_metadata` da entidade `Room` ou nos formulários de sessões e vendas. | Validação estrita com esquemas **Zod** na camada de aplicação antes da persistência, rejeitando payloads inválidos com `HTTP 422` por campo. | **Mitigado (`RF-02`, `RF-03`, `RF-04`, `CA-08`, `CT-08`)** — Schemas Zod em todos os módulos. |
| **T-14** | Cadeia de Suprimentos (*Supply Chain*) | Média | Médio | Introdução de vulnerabilidades (CVEs) em dependências transitivas npm/pnpm. | Lockfile `pnpm-lock.yaml` congelado, verificação de integridade no CI GitHub Actions e revisão periódica de pacotes. | **Mitigado (`ADR-010`, `RNF-06`)** — Pipeline CI ativo. |
| **T-15** | Falsificação de Identidade (*Spoofing*) | Baixa | Médio | Criação não autorizada de cinemas tenants por terceiros caso existisse endpoint público de *self-signup*. | Inexistência de rota pública de criação de tenants (`RES-03`); provisionamento restrito a script interno (`pnpm run provisionar-tenant`) executado pela equipe CineDoom após validação contratual. | **Mitigado (`RES-03`, `TASK-20`)** — Superfície pública eliminada. |
| **T-16** | Negação de Serviço (*Denial of Service*) | Média | Alto | Bloqueio malicioso de poltronas no Portal do Cliente por bots ou usuários sem intenção real de comparecimento ao cinema. | Exigência de autenticação prévia (`CLIENTE`), limite de assentos por reserva, trava de antecedência mínima de 60 minutos (`RN-08`) e expiração automática *Just-in-Time* (`RN-11`, `CA-14`). | **Mitigado (`ADR-012`, `RF-13`, `RF-18`, `CA-09`, `CA-14`, `CT-21`, `CT-26`)** — Testado em integração. |
| **T-17** | Elevação de Privilégio (*Elevation of Privilege* / IDOR) | Média | Alto | Referência Direta Insegura a Objeto (IDOR) em `POST /api/portal/reservas/[id]/cancelar`: cliente autenticado tenta cancelar reserva pertencente a outro espectador. | Verificação obrigatória de propriedade na camada de serviço (`reservation.user_id === session.user.id` e `tenant_id === currentTenantId`), retornando `HTTP 403 Forbidden` em tentativas cruzadas. | **Mitigado (`ADR-014`, `RF-16`, `RN-09`, `CA-12`, `CT-24`)** — Validado por teste automatizado anti-IDOR. |

---

## 4. Resolução Histórica dos Bloqueadores Iniciais

| Bloqueador Inicial (Fase de Concepção) | Decisão Arquitetural Adotada | Evidência de Implementação e Teste |
| :--- | :--- | :--- |
| **Blocker 1 (`T-1`):** Hash SHA-256 simples para CPF vulnerável a *rainbow table* no universo finito de CPFs (~900M). | Adoção de **`HMAC-SHA256`** com segredo de servidor (`CINEDOOM_CPF_HMAC_KEY`) no `CryptoService` (`ADR-008`). | Implementado em `src/modules/crypto/crypto-service.ts` e validado em `tests/unit/cryptoservice.test.ts` (`CT-06`, `CT-15`). |
| **Blocker 2 (`T-2`):** Ausência de especificação para proteção e rotação da chave `AES-256-GCM` do CPF cifrado. | Isolamento das chaves em **Vercel Environment Secrets** e criação de procedimento formal de rotação em lote (`ADR-008`). | Documentado em [`devops-spec.md`](../planning/devops-spec.md) e validado em `tests/unit/cryptoservice.test.ts` (`CT-06`). |
