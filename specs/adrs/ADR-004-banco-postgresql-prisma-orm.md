---
id: ADR-004
title: "Banco de Dados Relacional PostgreSQL com Prisma ORM"
status: "Aprovada"
date: "2026-10-22"
deciders: "Gabriel Lourenço (@gabrlou), Equipe CineSoft"
---

# ADR-004 — Banco de Dados Relacional PostgreSQL com Prisma ORM

## Status
Aprovada

## Data
2026-10-22

## Tomadores de Decisão
Gabriel Lourenço (@gabrlou), Equipe CineSoft

## Contexto
Venda e reserva de ingressos de cinema exigem estrita consistência transacional (ACID) para impedir conflito de assentos (double-booking).

## Decisão
PostgreSQL 16+ gerenciado no Neon Serverless com Prisma ORM para modelagem, migrações tipadas e consultas parametrizadas seguras.

## Consequências
### Positivas
- Garantia matemática de atomicidade e isolamento, prevenindo reservas e vendas duplicadas sob concorrência paralela.
### Negativas / Mitigações
- Documentadas e tratadas nas suítes de testes e políticas de observabilidade do projeto.
