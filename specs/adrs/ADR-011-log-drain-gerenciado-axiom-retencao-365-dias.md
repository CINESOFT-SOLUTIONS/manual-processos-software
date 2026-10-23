---
id: ADR-011
title: "Log Drain Gerenciado (Axiom) para Retenção de 365 Dias (LGPD)"
status: "Aprovada"
date: "2026-10-23"
deciders: "Carlos Eduardo (@carloseduduu), Kayque Vicente (@K4yquee)"
---

# ADR-011 — Log Drain Gerenciado (Axiom) para Retenção de 365 Dias (LGPD)

## Status
Aprovada

## Data
2026-10-23

## Tomadores de Decisão
Carlos Eduardo (@carloseduduu), Kayque Vicente (@K4yquee)

## Contexto
A retenção legal de logs de auditoria e segurança exigida pela LGPD é de no mínimo 365 dias, enquanto a Vercel retém apenas 1 hora no plano básico.

## Decisão
Integração do Log Drain da Vercel com a plataforma Axiom para ingestão OpenTelemetry nativa de eventos estruturados.

## Consequências
### Positivas
- Logs operacionais e eventos de auditoria são despachados em tempo real e armazenados com retenção de 1 ano, cumprindo os requisitos de auditoria externa.
### Negativas / Mitigações
- Documentadas e tratadas nas suítes de testes e políticas de observabilidade do projeto.
