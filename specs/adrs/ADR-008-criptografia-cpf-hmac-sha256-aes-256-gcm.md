---
id: ADR-008
title: "Criptografia de CPF: HMAC-SHA256 para Busca e AES-256-GCM para Armazenamento"
status: "Aprovada"
date: "2026-10-23"
deciders: "Carlos Eduardo (@carloseduduu), Yury Nogueira (@YuryNog)"
---

# ADR-008 — Criptografia de CPF: HMAC-SHA256 para Busca e AES-256-GCM para Armazenamento

## Status
Aprovada

## Data
2026-10-23

## Tomadores de Decisão
Carlos Eduardo (@carloseduduu), Yury Nogueira (@YuryNog)

## Contexto
O CPF é dado pessoal sensível segundo a LGPD. O espaço finito de CPFs válidos (~900 milhões) torna o SHA-256 puro vulnerável a ataques de pré-imagem por tabela rainbow se o banco for comprometido.

## Decisão
Armazenamento em duas camadas no `CryptoService`: `cpf_encrypted` com AES-256-GCM (chave de 256 bits + IV único) e `cpf_search_hash` com HMAC-SHA256 usando chave secreta do servidor (`CINEDOOM_CPF_HMAC_KEY`).

## Consequências
### Positivas
- Permite busca indexada O(1) no banco sem expor o CPF em texto claro e sem risco de quebra por enumeração ou rainbow table.
### Negativas / Mitigações
- Documentadas e tratadas nas suítes de testes e políticas de observabilidade do projeto.
