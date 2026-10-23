---
id: ADR-009
title: "Anonimização In-Place para LGPD Art. 18 sem Quebra de FK do CDC"
status: "Aprovada"
date: "2026-10-23"
deciders: "Carlos Eduardo (@carloseduduu), Yury Nogueira (@YuryNog)"
---

# ADR-009 — Anonimização In-Place para LGPD Art. 18 sem Quebra de FK do CDC

## Status
Aprovada

## Data
2026-10-23

## Tomadores de Decisão
Carlos Eduardo (@carloseduduu), Yury Nogueira (@YuryNog)

## Contexto
O titular tem direito ao esquecimento (Art. 18 da LGPD), mas o Código de Defesa do Consumidor (CDC Art. 27) e a legislação contábil exigem guarda do histórico fiscal e de vendas por 5 anos.

## Decisão
Implementação de soft-anonymization no modelo `Buyer`: ao solicitar exclusão, os campos `name`, `email`, `cpf_encrypted` e `cpf_search_hash` são limpos/anonimizados, gravando `anonymized_at = NOW()`.

## Consequências
### Positivas
- O registro `Buyer` permanece com seu ID, mantendo íntegras as foreign keys com `Ticket`, `Reservation` e `CancellationAudit`, satisfazendo ambas as legislações simultaneamente.
### Negativas / Mitigações
- Documentadas e tratadas nas suítes de testes e políticas de observabilidade do projeto.
