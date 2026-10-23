---
name: Auditoria de Qualidade / Nao-Conformidade
about: Registro formal de auditoria interna, nao-conformidade normativa ISO 12207 ou oportunidade de melhoria.
title: 'qa(auditoria): [processo/capitulo auditado]'
labels: ['tipo:docs', 'iso-12207']
assignees: ''
---

## Identificacao da Auditoria
- **Data da Auditoria:** AAAA-MM-DD
- **Auditor Responsavel:** (ex.: @K4yquee, @YuryNog)
- **Capitulo / Processo Auditado:** (ex.: Capitulo 4.2 – Gestao de Riscos / Clausula 6.3.4)

## Evidencia Inspecionada
<!-- Indique o trecho do manual em content/, especificacao em specs/ ou artefato compilado verificado. -->

## Constatacao
- [ ] **Nao-Conformidade Maior:** Contradicao direta com a norma ISO/IEC/IEEE 12207:2021 ou com as especificacoes de engenharia.
- [ ] **Nao-Conformidade Menor:** Falta de clareza tecnica, prolixidade ou ausencia de justificativa formal.
- [ ] **Oportunidade de Melhoria:** Aperfeicoamento visual em diagramas, tabelas ou rastreabilidade.

### Descricao do Problema:
<!-- Explique objetivamente o que foi identificado como inconsistente. -->

## Acao Corretiva Proposta
<!-- O que a equipe precisa fazer para corrigir a nao-conformidade no arquivo de origem em content/ ou specs/? -->

## Criterio de Resolucao
- [ ] Ajuste realizado no arquivo fonte em `content/` ou `specs/`.
- [ ] Script `./scripts/montar-manual.sh` e `./scripts/compilar.sh` executados sem erros.
