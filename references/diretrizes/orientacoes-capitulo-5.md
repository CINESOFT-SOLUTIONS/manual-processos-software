# Orientações para o Capítulo 5: Processos Técnicos

Documento de diretrizes e requisitos para a elaboração do **Capítulo 5** do Manual de Processos de Software, baseado na **Seção 6.4 da ABNT NBR ISO/IEC/IEEE 12207:2021** e no material da **Aula 6**.

---

## 5.1 Objetivo do Capítulo

Detalhar todas as atividades técnicas de engenharia do ciclo de vida: desde a elicitação de requisitos, modelagem de arquitetura e design, até a implementação, verificação, validação, transição, operação e manutenção do software.

---

## 5.2 Conteúdo Exigido na Atividade (Aula 6 - Slides 14, 24 e 41)

Conforme a **Aula 6**, o capítulo reúne os seguintes blocos temáticos:

### 5.1 Requisitos do Sistema e do Software (ISO 6.4.2 e 6.4.3)
- **Documento de Requisitos do Sistema:**
  - Requisitos Funcionais (RFs) completos e numerados (ex.: RF-01 a RF-18).
  - Requisitos Não Funcionais (RNFs) de desempenho, segurança e usabilidade.
  - Restrições técnicas e de negócio.
- **Elicitação e Necessidades dos Stakeholders:**
  - Registro dos stakeholders e técnicas de elicitação aplicadas (entrevistas, análise de domínio, prototipação).
- **Rastreabilidade e Critérios de Aceitação:**
  - Matriz vinculando necessidades de negócio ➡️ requisitos ➡️ casos de teste.
  - Critérios de aceitação objetivos para cada funcionalidade.

### 5.2 Arquitetura e Design de Software (ISO 6.4.4 e 6.4.5)
- **Visão Geral da Arquitetura:**
  - Padrão arquitetural adotado (ex.: Monólito Modular em Next.js com App Router e Route Handlers).
  - Diagramas arquiteturais (C4 Model: Nível 1 - Contexto, Nível 2 - Contêineres, Nível 3 - Componentes).
- **Design Detalhado:**
  - Modelo de dados relacional e diagramas entidade-relacionamento (ERD).
  - Especificação das interfaces de API e contratos de comunicação (RESTful JSON).
- **Justificativas Tecnológicas:** Racional da escolha do stack (Next.js, Tailwind, Prisma, PostgreSQL).

### 5.3 Implementação e Integração de Software (ISO 6.4.7 e 6.4.8)
- **Padrões de Codificação:** Guia de estilo, tipagem estrita com TypeScript, nomenclatura e convenções de commit.
- **Rastreabilidade Código-Requisito:** Padrão de vinculação de branches, commits e PRs aos IDs de requisitos (`feat: RF-07 - seleção de assentos`).
- **Plano de Integração:** Estratégia de integração contínua (CI) e esteira de automação.

### 5.4 Verificação e Validação - V&V (ISO 6.4.11 e 6.4.12)
- **Diferenciação Conceitual:**
  - *Verificação ("Estamos construindo o produto corretamente?"):* Análise estática, linting, testes unitários automatizados.
  - *Validação ("Estamos construindo o produto certo?"):* Testes de aceitação com usuários/stakeholders, fluxos fim a fim (E2E).
- **Plano e Relatório de Testes:** Casos de teste prioritários, cobertura e evidências de execução.

### 5.5 Transição, Operação, Manutenção e Descontinuação (ISO 6.4.13 a 6.4.16)
- **Transição:** Procedimento de implantação/deploy automatizado na Vercel e migrations de banco no Neon.
- **Operação e Monitoramento:** Monitoramento de saúde, logging e rastreio de erros.
- **Manutenção:** Política para tratamento de bugs críticos (hotfixes) e melhorias evolutivas.
- **Descontinuação:** Procedimentos previstos para migração segura de dados e encerramento responsável de serviços.

---

## 5.3 Critérios de Qualidade da Professora

> **📌 Referência:** Seção 6.4 da ISO 12207:2017  
> **⚠️ Atenção:** Os artefatos não precisam ser extensos — precisam ser consistentes, justificados e aplicados ao seu projeto real. Qualidade > quantidade.
