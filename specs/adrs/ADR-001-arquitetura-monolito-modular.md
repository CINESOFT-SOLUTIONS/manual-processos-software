---
id: ADR-001
title: "Arquitetura Monólito Modular em Next.js 14"
status: "Aprovada"
date: "2026-10-22"
deciders: "Gabriel Lourenço (@gabrlou), Equipe CineSoft"
---

# ADR-001 — Arquitetura Monólito Modular em Next.js 14

## Status
Aprovada

## Data
2026-10-22

## Tomadores de Decisão
Gabriel Lourenço (@gabrlou), Equipe CineSoft

## Contexto
Necessidade de desenvolver uma aplicação robusta com prazo restrito de 3 semanas (até 12/11/2026), unificando frontend e backend.

## Decisão
Adotar Monólito Modular usando Next.js 14 (App Router) em TypeScript organizado em Clean Architecture (Controller -> Service -> Repository) com Feature Slices verticais (`src/features/*`). Os módulos de catálogo, bilheteria, ocupação, reserva e auditoria operam com inversão de dependência via interfaces de domínio, enquanto `src/modules/*` fornece re-exportações canônicas para garantia de integridade arquitetural (ISO/IEC/IEEE 12207).

## Consequências
### Positivas
- Elimina sobrecarga de orquestração de microsserviços, simplifica transações de banco locais e viabiliza a entrega no prazo.
- Desacopla regras de negócio e casos de uso de detalhes de persistência (Prisma ORM) através do padrão Repository.
- Testabilidade unitária aprimorada por injeção de dependência e mocks de repositório.
### Negativas / Mitigações
- Documentadas e tratadas nas suítes de testes e políticas de observabilidade do projeto.

