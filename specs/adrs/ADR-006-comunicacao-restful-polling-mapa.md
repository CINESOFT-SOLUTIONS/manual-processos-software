---
id: ADR-006
title: "Comunicação via API RESTful e Polling de 2s no Mapa de Assentos"
status: "Aprovada"
date: "2026-10-22"
deciders: "Gabriel Lourenço (@gabrlou), Equipe CineSoft"
---

# ADR-006 — Comunicação via API RESTful e Polling de 2s no Mapa de Assentos

## Status
Aprovada

## Data
2026-10-22

## Tomadores de Decisão
Gabriel Lourenço (@gabrlou), Equipe CineSoft

## Contexto
Atualização contínua do mapa de assentos no balcão e no portal com múltiplos usuários e atendentes operando simultaneamente.

## Decisão
Endpoint HTTP RESTful `GET /api/sessoes/[id]/assentos` com polling client-side a cada 2000ms, em vez de WebSockets ou SSE no MVP.

## Consequências
### Positivas
- Atende o requisito RNF-01 (<2s de latência), simplifica a infraestrutura serverless e evita conexões persistentes ociosas.
### Negativas / Mitigações
- Documentadas e tratadas nas suítes de testes e políticas de observabilidade do projeto.
