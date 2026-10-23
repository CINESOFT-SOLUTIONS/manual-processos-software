---
kind: agent_artifact
feature_id: F-CINEDOOM-PLATAFORMA-B2B-SAAS-C
agent: Security
generated_by:
  run_id: run_2026-10-23T03-58-17_eedeb0ce
  session_id: 2026-09-03T15-33-01-hdb88xzyiu
  model: anthropic:claude-sonnet-4-6
generated_at: 2026-10-23T04:49:25.048Z
regenerative: true
title: "[Security] CineDoom — plataforma B2B SaaS para cinemas independentes e redes de pequeno/méd"
---

# Security — CineDoom — plataforma B2B SaaS para cinemas independentes e redes de pequeno/méd

> Artefato derivado de `.specs/features/F-CINEDOOM-PLATAFORMA-B2B-SAAS-C/spec.md` e gerado pelo agente **Security**
> via AI-4SDLC Platform. **Regenerative work product** (não-canonical SDD).
> Não edite manualmente — re-gere via `sdlc resume`.

## Resumo

Análise STRIDE+supply_chain do MVP CineDoom B2B SaaS. Dois blockers críticos identificados: (1) hash SHA-256 sem HMAC/salt para CPF é reversível por rainbow table dado espaço finito de CPFs brasileiros (~900M), violando LGPD; (2) gerenciamento da chave AES-256-GCM para CPF cifrado não está especificado — vazamento simultâneo de DB+chave expõe 100% da PII de compradores. Demais ameaças cobertas por mitigações implementáveis, mas exigem ação antes do go-live.

## Veredito

- **Decisão:** `block`
- **Secrets check:** passou
- **SBOM hash:** `not-generated`
- **Blockers:** 2

## Threat model

| ID | Categoria | Likelihood | Impacto | Descrição | Mitigação | Controle |
|----|-----------|------------|---------|-----------|-----------|----------|
| T-1 | info_disclosure | high | high | CPF armazenado como SHA-256 hash puro (sem HMAC/salt) é vulnerável a rainbow table e brute-force dado espaço finito de CPFs brasileiros (~900M combinações com dígitos verificadores), permitindo reverter hash para CPF real de qualquer comprador | substituir SHA-256 por HMAC-SHA256 com chave secreta server-side (ou bcrypt/argon2 com salt) para hash de busca de CPF; rainbow table inviabilizada pela chave HMAC | — |
| T-2 | info_disclosure | high | high | Chave AES-256-GCM usada para cifrar CPF dos compradores não tem estratégia de gerenciamento especificada — se armazenada em variável de ambiente sem secret manager, vazamento de dump de DB junto com .env compromete toda a base PII de compradores | armazenar chave AES exclusivamente em secret manager dedicado (Vercel Env Secrets cifrado, AWS KMS ou similar); nunca em .env comitado; rotação anual com re-cifragem | — |
| T-3 | secret_leak | high | high | DATABASE_URL (Neon), NEXTAUTH_SECRET e chave AES-256-GCM-CPF podem ser comitados acidentalmente em .env não ignorado ou expostos via logs de build/preview Vercel | pre-commit hook com detect-secrets/gitleaks; .env* no .gitignore verificado por CI; secrets exclusivamente via Vercel Env Vars interface; rotação trimestral | — |
| T-4 | info_disclosure | medium | high | Preview environments Vercel gerados por branch podem apontar para banco staging com dados reais de tenants, expondo PII de compradores para desenvolvedores sem necessidade | preview envs apontam exclusivamente para banco de dados isolado de preview com dados sintéticos; política documentada; verificação automatizada de DATABASE_URL em CI | — |
| T-5 | elevation_of_privilege | medium | high | Role ATENDENTE/GERENTE validada apenas no middleware Next.js (edge) sem revalidação na camada de Route Handler/Server Action permite bypass via requisição direta à API sem passar pelo middleware | validar role e tenant_id do token em cada Route Handler e Server Action na camada de serviço; testes de penetração cobrindo bypass de middleware | — |
| T-6 | elevation_of_privilege | medium | high | tenant_id extraído do JWT NextAuth sem validação cruzada com banco permite que sessão de usuário de tenant A, se token manipulado ou NEXTAUTH_SECRET fraco, acesse dados de tenant B | NEXTAUTH_SECRET >= 256-bit random; revalidar tenant_id do session token contra DB em operações sensíveis; assinar todos os claims | — |
| T-7 | spoofing | medium | high | Cookie de sessão NextAuth roubado (XSS, network sniff em HTTP) pode ser reutilizado até expiração sem mecanismo de revogação imediata, permitindo spoofing de Atendente ou Gerente | cookie HttpOnly+Secure+SameSite=Strict; HTTPS enforced; session rotation após login; TTL máximo 8h; logout invalida sessão no DB | — |
| T-8 | tampering | medium | high | Tabela auditoria_cancelamentos sem proteção DDL no nível de banco pode ter registros deletados ou alterados pelo app DB user se permissões não forem restritas, quebrando imutabilidade da auditoria | app DB user sem GRANT DELETE/UPDATE em auditoria_cancelamentos; trigger PostgreSQL bloqueando UPDATE/DELETE; backup point-in-time do Neon habilitado | — |
| T-9 | repudiation | medium | medium | Vendas de ingressos não possuem registro de auditoria equivalente ao de cancelamentos — atendente pode vender e manipular ticket sem rastro auditável, dificultando investigação de fraude interna | criar tabela ticket_audit_log append-only registrando criação e alterações de tickets com user_id, timestamp UTC, tenant_id e IP de origem | — |
| T-10 | denial_of_service | medium | high | Polling de 2s por N terminais simultâneos em GET /api/sessoes/[id]/assentos pode saturar o connection pool serverless do Neon (limite de conexões por branch), causando timeout em cascata nas vendas | connection pooling via Neon Pooler (PgBouncer mode); rate-limit por tenant no endpoint de polling (ex: 1 req/2s por sessão por terminal); monitorar conexões ativas | — |
| T-11 | denial_of_service | low | medium | SELECT FOR UPDATE em alta concorrência (50+ threads no mesmo assento) pode causar lock wait timeout ou deadlock no Neon Serverless, degradando disponibilidade do endpoint de venda em dias de estreia | lock_timeout explícito na transação (ex: SET LOCAL lock_timeout = '3s'); retry com backoff exponencial no cliente; alertas de deadlock via pg_stat_activity | — |
| T-12 | info_disclosure | medium | medium | Logs de aplicação Next.js e Vercel Functions podem capturar PII (CPF plaintext em erro de validação, email em stack trace) via request logging automático ou error tracking (Sentry) sem sanitização | sanitizar campos PII antes de logar; configurar Sentry com scrubbing rules para cpf/email/name; auditoria de log output como parte do CI | — |
| T-13 | tampering | low | medium | layout_metadata JSONB da entidade Room sem schema validation no nível de aplicação pode receber payload malformado ou com campos inesperados que corrompem o mapa de assentos renderizado no frontend | validar layout_metadata com Zod schema antes de persistir; rejeitar campos não declarados; testes de fuzzing no endpoint de cadastro de sala | — |
| T-14 | supply_chain | medium | medium | Dependências Next.js 14, Prisma, NextAuth.js e transitivas podem introduzir CVEs não detectados sem processo de varredura contínua, especialmente em ambiente de deploy contínuo Vercel | Dependabot habilitado com auto-merge para patch; npm audit --audit-level=high no CI gate; SBOM gerado e revisado a cada release de produção | — |
| T-15 | spoofing | low | medium | Provisionamento manual de tenants pela equipe CineDoom sem processo formal de verificação de identidade do cinema pode ser explorado via engenharia social para criar tenant fraudulento com acesso à plataforma | checklist de verificação de identidade B2B (CNPJ, contrato assinado); aprovação dupla interna antes de provisionar; log de provisionamento auditável | — |

## Blockers

- **T-1.** hash SHA-256 sem HMAC/salt para CPF é reversível por rainbow table dado espaço finito (~900M CPFs) — violação LGPD bloqueia go-live até substituição por HMAC-SHA256 com chave secreta ou bcrypt
- **T-2.** key management da chave AES-256-GCM para CPF cifrado não especificado — ausência de secret manager implica risco de comprometimento total de PII compradores em caso de vazamento de DB+env
