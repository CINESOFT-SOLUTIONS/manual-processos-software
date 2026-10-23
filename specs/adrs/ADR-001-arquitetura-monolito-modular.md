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
Adotar Monólito Modular usando Next.js 14 (App Router) em TypeScript. Módulos de catálogo, bilheteria, ocupação e auditoria compartilham infraestrutura com isolamento claro de serviços.

## Consequências
### Positivas
- Elimina sobrecarga de orquestração de microsserviços, simplifica transações de banco locais e viabiliza a entrega no prazo.
### Negativas / Mitigações
- Documentadas e tratadas nas suítes de testes e políticas de observabilidade do projeto.
