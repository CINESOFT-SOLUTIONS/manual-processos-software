---
kind: agent_artifact
feature_id: F-CINEDOOM-MVP
title: "CineDoom — Plataforma SaaS B2B de Bilheteria, Back-Office e Portal do Cliente"
---

# Feature: F-CINEDOOM-MVP: Plataforma SaaS de Gestão de Cinemas, Bilheteria e Portal do Cliente

Digitaliza as operações de exibição cinematográfica para cinemas independentes e redes de pequeno e médio porte no Brasil, integrando três módulos centrais: Back-Office do Gerente (catálogo de filmes, salas, sessões e painel de ocupação), Módulo do Atendente (bilheteria presencial com trava ACID anti-double-booking e baixa presencial de reservas) e Portal do Cliente (consulta de programação, cadastro/login de espectadores, reserva de assentos com trava de concorrência, e-mail transacional com voucher e cancelamento web de reservas pendentes).

## WHAT/HOW
**WHAT.** Sistema SaaS com três módulos integrados: Back-Office do Gerente, Bilheteria do Atendente e Portal do Cliente. Permite consulta pública e autenticada de filmes e sessões, escolha e bloqueio temporário de assentos, autenticação de clientes com proteção LGPD, despacho de e-mail transacional com instruções de pagamento presencial, consulta de histórico pessoal de reservas com opção de cancelamento voluntário pelo cliente e baixa presencial na bilheteria com conversão em venda confirmada ou expiração Just-in-Time (1 hora antes da sessão).
**HOW.** Monólito modular em Next.js 14 (App Router) + TypeScript + Tailwind CSS, com Prisma ORM sobre PostgreSQL Serverless (Neon). Trava atômica de assentos via SELECT FOR UPDATE dentro de transação Prisma com status 'RESERVED'. Expiração Just-in-Time em queries SQL para liberar assentos não pagos 60 minutos antes da sessão sem dependência de daemons externos. Mapa de assentos com polling client-side a cada 2s via Route Handler. Isolamento multi-tenant por tenant_id via middleware de contexto no Prisma Client. Autenticação unificada com NextAuth.js com roles GERENTE, ATENDENTE e CLIENTE. Serviço transacional de e-mails para emissão de comprovantes de reserva. Deploy contínuo na Vercel.

## User Stories
- **US-1.** Como Atendente, quero selecionar um assento disponível no mapa visual e registrar a venda do ingresso vinculando nome, CPF e e-mail do comprador para que a transação seja concluída sem risco de double-booking e o comprador saia com seu assento garantido em tempo de pico.
- **US-2.** Como Atendente, quero cancelar um ingresso vendido e registrar o motivo do cancelamento com meu identificador de usuário para que a operação fique rastreável para auditoria futura e o assento seja liberado imediatamente para nova venda.
- **US-3.** Como Gerente, quero visualizar em tempo real o painel de ocupação de todas as sessões do dia com percentual de assentos vendidos e reservados para que possa tomar decisões operacionais como alocação de equipe e abertura de salas extras em dias de estreia.
- **US-4.** Como Gerente, quero cadastrar e manter filmes, salas com layout de assentos e sessões cinematográficas com data, horário e sala associada para que o back-office reflita a programação real do cinema sem depender de planilhas ou sistemas externos desconectados.
- **US-5.** Como Atendente ou Cliente, quero visualizar o mapa de assentos de uma sessão com atualização automática a cada 2 segundos para que eu tenha feedback imediato sobre assentos recém-vendidos ou reservados por outros usuários e evite conflitos na seleção.
- **US-6.** Como Gerente, quero criar contas de Atendente vinculadas ao meu tenant com permissões restritas ao perfil operacional para que haja controle de acesso granular e responsabilidade rastreável por ação realizada no sistema.
- **US-7.** Como Cliente, quero me cadastrar e realizar login no Portal do Cliente com e-mail e senha, informando meus dados e consentimento LGPD, para ter acesso ao meu painel pessoal de reservas e histórico de ingressos.
- **US-8.** Como Cliente, quero consultar a programação de filmes e sessões e reservar assentos disponíveis no mapa interativo com confirmação de reserva e geração de código identificador (ex: CD-8942), para garantir meus lugares com antecedência para pagamento presencial.
- **US-9.** Como Cliente, quero receber um e-mail transacional e visualizar na tela o comprovante da minha reserva com código, assentos e prazo limite (até 1 hora antes da sessão), para que eu tenha as instruções exatas de comparecimento e pagamento na bilheteria.
- **US-10.** Como Cliente, quero acessar a área "Minhas Reservas" no portal e cancelar uma reserva pendente antes do prazo limite, para liberar imediatamente os assentos caso eu não possa comparecer ao cinema.
- **US-11.** Como Atendente, quero buscar reservas ativas pelo código ou CPF do cliente na bilheteria e registrar o pagamento presencial para converter a reserva em venda confirmada com emissão de ingresso.

## Acceptance Criteria
- **AC-1.** Dado que dois terminais tentam vender o mesmo assento na mesma sessão simultaneamente, apenas um deve ter sucesso e o outro deve receber erro de conflito sem corrupção de estado, garantido por SELECT FOR UPDATE em transação Prisma. @test:tests/integration/venda-atomica-acid.test.ts
- **AC-2.** O mapa de assentos de uma sessão deve refletir mudanças de disponibilidade em no máximo 2 segundos após uma venda, reserva ou cancelamento, via polling de Route Handler GET /api/sessoes/[id]/assentos a cada 2000ms. @test:packages/bilheteria/src/mapa-assentos-polling.test.ts
- **AC-3.** Todo cancelamento de ingresso deve persistir registro imutável na tabela auditoria_cancelamentos com: id do ingresso, id do usuário executante, timestamp UTC, tenant_id e motivo informado, antes de liberar o assento. @test:packages/bilheteria/src/cancelamento-auditavel.test.ts
- **AC-4.** Toda query ao banco de dados que acesse entidades de negócio (filmes, salas, sessões, ingressos, compradores, reservas) deve incluir filtro WHERE tenant_id = :tenantId injetado pelo middleware Prisma, impedindo vazamento de dados entre tenants. @test:packages/tenancy/src/row-level-isolation.test.ts
- **AC-5.** Usuário com perfil ATENDENTE ou CLIENTE não deve conseguir acessar rotas de gerenciamento do back-office, recebendo HTTP 403 ao tentar, enquanto GERENTE tem acesso completo às rotas do seu tenant. @test:packages/auth/src/perfis-rbac.test.ts
- **AC-6.** O cadastro de comprador ou cliente no ato da compra ou reserva deve persistir nome, CPF (armazenado com hash HMAC-SHA256 para busca e valor cifrado AES-256-GCM para exibição) e e-mail, com campo de consentimento LGPD registrado com timestamp. @test:packages/compradores/src/cadastro-lgpd.test.ts
- **AC-7.** O painel de ocupação do Gerente deve exibir, para cada sessão do dia corrente, o percentual de assentos vendidos e reservados sobre o total da sala, atualizando com dados isolados por tenant_id do gerente autenticado. @test:packages/ocupacao/src/painel-gerente.test.ts
- **AC-8.** O catálogo de filmes, o cadastro de salas com layout de assentos e as sessões cinematográficas devem ser criáveis, editáveis e listáveis exclusivamente por usuários com perfil GERENTE, com validação de campos obrigatórios. @test:packages/backoffice/src/catalogo-salas-sessoes.test.ts
- **AC-9.** A solicitação de reserva via Portal do Cliente deve executar transação atômica atualizando o assento para 'RESERVED' e associando o reservation_id, bloqueando-o para outros usuários e rejeitando a operação caso falte menos de 60 minutos para a sessão. @test:tests/integration/reserva-atomica.test.ts
- **AC-10.** O cadastro do cliente final deve persistir credenciais de acesso seguras (senha com hash seguro) com role 'CLIENTE' e dados PII em conformidade com a LGPD, permitindo autenticação e sessão no Portal do Cliente. @test:packages/auth/src/cadastro-cliente-lgpd.test.ts
- **AC-11.** Após a confirmação da reserva, o sistema deve despachar um e-mail transacional com voucher contendo código identificador único, data/hora da sessão, sala, assentos e horário limite para pagamento presencial, gravando o timestamp em email_sent_at. @test:packages/notificacoes/src/email-reserva.test.ts
- **AC-12.** O cliente autenticado deve conseguir visualizar suas reservas e solicitar o cancelamento voluntário de reservas com status 'PENDING', atualizando o status para 'CANCELLED' e liberando imediatamente os assentos para 'AVAILABLE'. @test:packages/portal/src/cancelamento-reserva.test.ts
- **AC-13.** O atendente na bilheteria deve conseguir localizar uma reserva válida pelo código ou CPF e, ao registrar o pagamento presencial no balcão, converter a reserva em ingresso vendido ('SOLD') com registro do atendente operador. @test:packages/bilheteria/src/baixa-reserva-balcao.test.ts
- **AC-14.** Reservas não pagas até 60 minutos antes do início da sessão devem ser consideradas expiradas ('EXPIRED') em tempo de execução através de queries Just-in-Time, liberando os assentos para venda no balcão sem retenção indevida de capacidade. @test:tests/integration/expiracao-reserva-jit.test.ts

## NFRs
- **Performance efficiency.** A resposta do endpoint de venda e reserva de ingresso (incluindo trava atômica e persistência) deve completar em ambiente Neon Serverless com conexão poolada em condição de carga moderada (até 20 req/s simultâneos). (p95 < 800ms, p99 < 1500ms)
- **Reliability.** A trava ACID de assentos deve garantir zero ocorrências de double-booking ou double-reservation sob carga de testes de concorrência com 50 threads simultâneas tentando reservar ou vender o mesmo assento. (0 conflitos em 10.000 tentativas concorrentes simuladas)
- **Security.** Nenhuma requisição autenticada deve retornar dados de clientes/compradores (CPF, e-mail) ou reservas pertencentes a outro tenant ou a outro cliente, validado por suíte de testes de isolamento. (0 vazamentos cross-tenant ou cross-user)
- **Maintainability.** O código-fonte deve manter arquitetura de monólito modular com módulos desacoplados (bilheteria, portal, backoffice, auth, tenancy, notificacoes) sem dependências circulares reportadas pelo ESLint. (0 ciclos de dependência)
- **Compatibility.** As interfaces de bilheteria e do Portal do Cliente devem ser funcionais em navegadores Chromium, Firefox e Safari modernos, com layout responsivo para desktop e dispositivos móveis no portal público. (100% dos fluxos passando em testes Playwright)
- **Portability.** O ambiente de desenvolvimento deve ser reproduzível com um único comando (pnpm dev) após cópia de .env.example, sem serviços externos obrigatórios além do banco Neon Serverless. (Setup validado em checklist < 30min)

## Out of scope
- Gateway de pagamento online (cartão de crédito/débito online ou checkout PIX no portal) — pagamento das reservas é realizado presencialmente na bilheteria física.
- Integração com sistemas de emissão fiscal externos (NFC-e / SAT).
- Aplicativo mobile nativo para Android/iOS (o acesso é via web responsiva).
- Gestão de bomboniere e estoque de alimentos/bebidas.
- Integração com distribuidoras cinematográficas ou serviços de DRM.
- Suporte a múltiplos idiomas (i18n) além do português brasileiro.

## NEEDS_CLARIFICATION
- nenhum.
