---
id: ADR-003
title: "Backend em TypeScript com Route Handlers"
status: "Aprovada"
date: "2026-10-22"
deciders: "Gabriel Lourenço (@gabrlou), Carlos Eduardo (@carloseduduu)"
---

# ADR-003 — Backend em TypeScript com Route Handlers

## Status
Aprovada

## Data
2026-10-22

## Tomadores de Decisão
Gabriel Lourenço (@gabrlou), Carlos Eduardo (@carloseduduu)

## Contexto
Garantir tipagem estática e segurança de tipos entre o banco de dados, as validações de schema e os endpoints HTTP.

## Decisão
Utilizar Route Handlers do Next.js 14 (`app/api/**/route.ts`) com TypeScript estrito (`strict: true`) e validação de payloads via Zod.

## Consequências
### Positivas
- Detecção de erros em tempo de compilação, validação declarativa de dados e contratos de API auto-documentados.
### Negativas / Mitigações
- Documentadas e tratadas nas suítes de testes e políticas de observabilidade do projeto.
