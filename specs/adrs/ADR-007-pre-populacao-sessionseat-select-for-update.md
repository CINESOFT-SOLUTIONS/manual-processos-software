---
id: ADR-007
title: "Pré-população de SessionSeat para Trava Pessimista SELECT FOR UPDATE"
status: "Aprovada"
date: "2026-10-23"
deciders: "Gabriel Lourenço (@gabrlou), Equipe CineSoft"
---

# ADR-007 — Pré-população de SessionSeat para Trava Pessimista SELECT FOR UPDATE

## Status
Aprovada

## Data
2026-10-23

## Tomadores de Decisão
Gabriel Lourenço (@gabrlou), Equipe CineSoft

## Contexto
Concorrência entre múltiplos atendentes e clientes tentando selecionar e comprar o mesmo assento no mesmo milissegundo.

## Decisão
Ao criar uma `Session`, o sistema pré-popula uma linha em `session_seats` para cada `Seat` da sala. A transação executa `$queryRaw` com `SELECT id, status FROM session_seats WHERE id = $1 FOR UPDATE`.

## Consequências
### Positivas
- A linha já existe no banco, garantindo que o lock pessimista do PostgreSQL funcione deterministicamente, retornando `HTTP 409 Conflict` imediatamente para requisições concorrentes.
### Negativas / Mitigações
- Documentadas e tratadas nas suítes de testes e políticas de observabilidade do projeto.
