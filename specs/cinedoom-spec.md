---
id: F-CINEDOOM-PLATAFORMA-B2B-SAAS-C
parent: PROD-001
title: >-
  CineDoom — plataforma B2B SaaS para cinemas independentes e redes de
  pequeno/méd
version: 0.1.0
status: draft
risk_tier: limited
owners:
  - '@CINESOFT-SOLUTIONS'
data_classification: internal
deps: []
constitution_overrides: []
related_adrs: []
SLOs:
  availability: 99.5%
  p95_latency: 500ms
last_updated: '2026-10-23'
classification: internal
audience:
  - dev
language: pt-BR
spec_hash: a6474339d3a90b00a28a24d1ff4c934cd51fef4e61abae138c95e8ea88bf4a72
---
# Feature: F-CINEDOOM-MVP: Plataforma B2B SaaS de Bilheteria e Back-Office para Cinemas Independentes

Digitaliza operações de bilheteria presencial e back-office para cinemas independentes e redes de pequeno/médio porte no Brasil. Entrega catálogo de filmes, gestão de salas/assentos, sessões, mapa interativo com polling 2s, venda ACID sem double-booking, cancelamento auditável, painel de ocupação em tempo real e autenticação por perfil (Atendente/Gerente), com isolamento multi-tenant por row-level e conformidade LGPD.

## WHAT/HOW
**WHAT.** MVP SaaS B2B com módulos de catálogo de filmes, gestão de salas e assentos, sessões cinematográficas, mapa de assentos interativo, venda de ingressos com garantia ACID, cancelamento auditável, painel de ocupação e autenticação com perfis Atendente e Gerente — tudo isolado por tenant_id compartilhando schema PostgreSQL.
**HOW.** Monólito modular em Next.js 14 (App Router) + TypeScript + Tailwind CSS, com Prisma ORM sobre PostgreSQL Serverless (Neon). Trava atômica de assentos via SELECT FOR UPDATE dentro de transação Prisma. Mapa de assentos com polling client-side a cada 2s via Route Handler. Isolamento multi-tenant por tenant_id com middleware de contexto injetando filtro global no Prisma Client. Autenticação stateful com NextAuth.js com roles ATENDENTE/GERENTE. Deploy contínuo na Vercel com preview environments por branch.

## User Stories
- **US-1.** Como Atendente, quero selecionar um assento disponível no mapa visual e registrar a venda do ingresso vinculando nome, CPF e e-mail do comprador para a transação seja concluída sem risco de double-booking e o comprador saia com seu assento garantido em tempo de pico.
- **US-2.** Como Atendente, quero cancelar um ingresso vendido e registrar o motivo do cancelamento com meu identificador de usuário para a operação fique rastreável para auditoria futura e o assento seja liberado imediatamente para nova venda.
- **US-3.** Como Gerente, quero visualizar em tempo real o painel de ocupação de todas as sessões do dia com percentual de assentos vendidos para possa tomar decisões operacionais como alocação de equipe e abertura de salas extras em dias de estreia.
- **US-4.** Como Gerente, quero cadastrar e manter filmes, salas com layout de assentos e sessões cinematográficas com data, horário e sala associada para o back-office reflita a programação real do cinema sem depender de planilhas ou sistemas externos desconectados.
- **US-5.** Como Atendente, quero visualizar o mapa de assentos de uma sessão com atualização automática a cada 2 segundos para eu tenha feedback imediato sobre assentos recém-vendidos por outros terminais e evite conflitos na fila de atendimento.
- **US-6.** Como Gerente, quero criar contas de Atendente vinculadas ao meu tenant com permissões restritas ao perfil operacional para haja controle de acesso granular e responsabilidade rastreável por ação realizada no sistema.

## Acceptance Criteria
- **AC-1.** Dado que dois terminais tentam vender o mesmo assento na mesma sessão simultaneamente, apenas um deve ter sucesso e o outro deve receber erro de conflito sem corrupção de estado, garantido por SELECT FOR UPDATE em transação Prisma. @test:tests/integration/venda-atomica-acid.test.ts
- **AC-2.** O mapa de assentos de uma sessão deve refletir mudanças de disponibilidade em no máximo 2 segundos após uma venda ou cancelamento, via polling de Route Handler GET /api/sessoes/[id]/assentos a cada 2000ms. @test:packages/bilheteria/src/mapa-assentos-polling.test.ts
- **AC-3.** Todo cancelamento de ingresso deve persistir registro imutável na tabela auditoria_cancelamentos com: id do ingresso, id do usuário executante, timestamp UTC, tenant_id e motivo informado, antes de liberar o assento. @test:packages/bilheteria/src/cancelamento-auditavel.test.ts
- **AC-4.** Toda query ao banco de dados que acesse entidades de negócio (filmes, salas, sessões, ingressos, compradores) deve incluir filtro WHERE tenant_id = :tenantId injetado pelo middleware Prisma, impedindo vazamento de dados entre tenants. @test:packages/tenancy/src/row-level-isolation.test.ts
- **AC-5.** Usuário com perfil ATENDENTE não deve conseguir acessar rotas de gerenciamento (cadastro de filmes, salas, sessões, usuários), recebendo HTTP 403 ao tentar, enquanto GERENTE tem acesso completo às rotas do seu tenant. @test:packages/auth/src/perfis-rbac.test.ts
- **AC-6.** O cadastro de comprador no ato da venda deve persistir nome, CPF (armazenado com hash SHA-256 para busca, valor cifrado para exibição) e e-mail, com campo de consentimento LGPD registrado com timestamp, sendo obrigatórios todos os campos antes da confirmação da venda. @test:packages/compradores/src/cadastro-lgpd.test.ts
- **AC-7.** O painel de ocupação do Gerente deve exibir, para cada sessão do dia corrente, o percentual de assentos vendidos (vendidos/total) e atualizar ao recarregar a página, com dados isolados por tenant_id do gerente autenticado. @test:packages/ocupacao/src/painel-gerente.test.ts
- **AC-8.** O catálogo de filmes, o cadastro de salas com layout de assentos e as sessões cinematográficas devem ser criáveis, editáveis e listáveis exclusivamente por usuários com perfil GERENTE, com validação de campos obrigatórios retornando erros descritivos por campo. @test:packages/backoffice/src/catalogo-salas-sessoes.test.ts

## NFRs
- **Performance efficiency.** A resposta do endpoint de venda de ingresso (incluindo trava atômica e persistência) deve completar em ambiente Neon Serverless com conexão poolada em condição de carga moderada (até 20 req/s simultâneos). (p95 < 800ms, p99 < 1500ms)
- **Reliability.** A trava ACID de assentos deve garantir zero ocorrências de double-booking sob carga de testes de concorrência com 50 threads simultâneas tentando vender o mesmo assento, validado por teste de integração com transações paralelas. (0 double-bookings em 10.000 tentativas concorrentes simuladas)
- **Security.** Nenhuma requisição autenticada deve retornar, em qualquer endpoint ou log de aplicação, dados de comprador (CPF, e-mail) ou ingressos pertencentes a tenant_id diferente do token JWT apresentado, verificado por suite de testes de isolamento cross-tenant. (0 vazamentos cross-tenant em suite de 500 cenários de isolamento)
- **Maintainability.** O código-fonte deve manter arquitetura de monólito modular com módulos independentes (bilheteria, backoffice, auth, tenancy, ocupacao) sem dependências circulares entre módulos, verificado por lint de dependências no CI. (0 dependências circulares reportadas pelo ESLint import/no-cycle)
- **Compatibility.** A interface de bilheteria (mapa de assentos, fluxo de venda, painel de ocupação) deve ser funcional em Chromium e Firefox na versão corrente – 1, em resolução mínima de 1024×768 (desktop/tablet landscape), sem polyfills de APIs experimentais. (100% dos fluxos críticos passando em matriz Chromium + Firefox no Playwright CI)
- **Portability.** O ambiente de desenvolvimento deve ser reproduzível com um único comando (pnpm dev) após cópia de .env.example, sem dependências de serviços locais além de conexão à Neon Serverless via URL, possibilitando onboarding de novo dev em menos de 30 minutos. (Tempo de setup documentado e validado em checklist de onboarding < 30min)

## Out of scope
- Processamento de pagamento online (PIX, cartão de crédito/débito) — pagamento é registrado como offline pelo atendente
- Integração com gateways de pagamento ou emissão de comprovantes fiscais (NFC-e, SAT)
- Venda de ingressos pelo canal online/self-service pelo comprador final (B2C)
- Aplicativo mobile nativo (iOS/Android)
- Relatórios financeiros e conciliação de caixa avançada
- Gestão de estoque de alimentos e bebidas (concessionária)
- Integração com distribuidoras de filmes ou sistemas de DRM
- Suporte a múltiplos idiomas (i18n) além do português brasileiro
- Exportação de dados para BI externo ou integração com ERPs

## NEEDS_CLARIFICATION
- nenhum.
