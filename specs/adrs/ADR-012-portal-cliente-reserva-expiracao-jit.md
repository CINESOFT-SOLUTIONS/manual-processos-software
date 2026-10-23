---
id: ADR-012
title: "Portal do Cliente, Autenticação de Espectador, Expiração Just-in-Time e Notificação Transacional"
status: "Aprovada"
date: "2026-10-23"
deciders: "Gabriel Lourenço (@gabrlou), Equipe CineSoft"
---

# ADR-012 — Portal do Cliente, Autenticação de Espectador, Expiração Just-in-Time e Notificação Transacional

## Status
Aprovada

## Data
2026-10-23

## Tomadores de Decisão
Gabriel Lourenço (@gabrlou), Equipe CineSoft

## Contexto
Necessidade de incorporar o Portal do Cliente para reserva pública de assentos com pagamento presencial no balcão até 1 hora antes da sessão, cadastro/login de cliente, e-mail transacional e cancelamento web.

## Decisão
Trava ACID via `session_seats.status = 'RESERVED'`, expiração Just-in-Time no PostgreSQL Neon (`reservation_expires_at > NOW()`), autenticação unificada via NextAuth.js (role `CLIENTE`), envio de voucher por `NotificationService` e endpoint de cancelamento voluntário pelo próprio cliente via web.

## Consequências
### Positivas
- Solução viável no prazo de 21 dias sem gateway financeiro externo, com risco zero de assentos duplicados e sem necessidade de daemons/filas assíncronas dedicadas.
### Negativas / Mitigações
- Documentadas e tratadas nas suítes de testes e políticas de observabilidade do projeto.
