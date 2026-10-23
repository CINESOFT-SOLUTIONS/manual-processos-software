---
id: ADR-005
title: "Hospedagem na Vercel com Neon Serverless e GitHub Actions"
status: "Aprovada"
date: "2026-10-22"
deciders: "Carlos Eduardo (@carloseduduu), Gabriel Lourenço (@gabrlou)"
---

# ADR-005 — Hospedagem na Vercel com Neon Serverless e GitHub Actions

## Status
Aprovada

## Data
2026-10-22

## Tomadores de Decisão
Carlos Eduardo (@carloseduduu), Gabriel Lourenço (@gabrlou)

## Contexto
Necessidade de ambiente de staging e produção com deploy contínuo automatizado e custo operacional zero no MVP.

## Decisão
Vercel integrada ao repositório GitHub via GitHub Actions CI/CD e banco de dados hospedado no Neon Serverless com suporte a database branching.

## Consequências
### Positivas
- Deploy automático a cada push na branch main, pré-visualizações isoladas de pull request e zero sobrecarga de manutenção de servidores físicos.
### Negativas / Mitigações
- Documentadas e tratadas nas suítes de testes e políticas de observabilidade do projeto.
