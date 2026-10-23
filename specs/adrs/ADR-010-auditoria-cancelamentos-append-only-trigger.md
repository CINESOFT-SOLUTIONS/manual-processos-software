---
id: ADR-010
title: "Auditoria de Cancelamentos Append-Only via Trigger PostgreSQL"
status: "Aprovada"
date: "2026-10-23"
deciders: "Gabriel Lourenço (@gabrlou), Kayque Vicente (@K4yquee)"
---

# ADR-010 — Auditoria de Cancelamentos Append-Only via Trigger PostgreSQL

## Status
Aprovada

## Data
2026-10-23

## Tomadores de Decisão
Gabriel Lourenço (@gabrlou), Kayque Vicente (@K4yquee)

## Contexto
A auditoria de cancelamento de ingressos deve ser estritamente imutável para compliance com o Art. 37 da LGPD e auditoria contábil interna.

## Decisão
Criação de trigger PostgreSQL em `cancellation_audits` disparado em `BEFORE UPDATE OR DELETE` que lança exceção imediata (`RAISE EXCEPTION 'Registros de auditoria são imutáveis'`).

## Consequências
### Positivas
- Nem mesmo a aplicação com credenciais normais consegue alterar ou expurgar o log de auditoria, garantindo conformidade regulatória sem o custo de um bucket S3 Object Lock no MVP.
### Negativas / Mitigações
- Documentadas e tratadas nas suítes de testes e políticas de observabilidade do projeto.
