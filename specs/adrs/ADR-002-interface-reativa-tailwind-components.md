---
id: ADR-002
title: "Interface Reativa com Tailwind CSS e React Server/Client Components"
status: "Aprovada"
date: "2026-10-22"
deciders: "Gabriel Lourenço (@gabrlou), Equipe CineSoft"
---

# ADR-002 — Interface Reativa com Tailwind CSS e React Server/Client Components

## Status
Aprovada

## Data
2026-10-22

## Tomadores de Decisão
Gabriel Lourenço (@gabrlou), Equipe CineSoft

## Contexto
O mapa de assentos da sala precisa ser interativo, de resposta imediata (<2s) e cromática intuitiva para o Atendente de bilheteria e espectadores.

## Decisão
Tailwind CSS para estilização utilitária consistente e React Client Components apenas nos componentes com estado interativo (ex: SeatingGrid), mantendo catálogo em Server Components.

## Consequências
### Positivas
- Bundle JS otimizado, renderização rápida e experiência fluida tanto no guichê presencial quanto no Portal do Cliente.
### Negativas / Mitigações
- Documentadas e tratadas nas suítes de testes e políticas de observabilidade do projeto.
