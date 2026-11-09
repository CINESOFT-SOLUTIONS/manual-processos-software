# Manual de Processos de Software

### Estudo de Caso: Sistema CineDoom (Plataforma de Gestão Operacional de Cinemas)

---

**Equipe:** CineSoft Solutions  

**Membros da Equipe:**
- Carlos Eduardo Freire da Silva
- Gabriel Henrique Lourenço Dias
- Kayque Vicente Silva
- Yury Nogueira de Oliveira Silva

**Identificação Acadêmica:**
- **Instituição:** Universidade Federal de Goiás (UFG) — Instituto de Informática (INF)
- **Curso:** Bacharelado em Engenharia de Software
- **Disciplina:** Processos de Engenharia de Software
- **Docente:** Profa. Dra. Juliana Pereira de Souza Zinader
- **Período Letivo:** 2026/2

---

<div style="page-break-after: always;"></div>

---

# Histórico de Versões do Documento

> **Documento Controlado:** Qualquer alteração neste manual deve ser formalmente registrada nesta tabela e, quando impactar definições de negócio, arquitetura ou escopo, refletida no catálogo de decisões de arquitetura e especificações do projeto (`specs/`).

| Data | Versão | Alteração Realizada |
| :---: | :---: | :--- |
| 10/09/2026 | 1.0 | Criação do documento e elaboração da capa. |
| 16/09/2026 | 1.1 | Elaboração dos itens do Capítulo 1 (Apresentação do Software). |
| 24/09/2026 | 1.2 | Alinhamento dos Capítulos 1, 2 e 3 às especificações de engenharia e à norma ABNT NBR ISO/IEC/IEEE 12207:2021. |
| 24/09/2026 | 1.3 | Revisão técnica: correção de contradições, terminologia, justificativas de aquisição e índice de aderência. |
| 08/10/2026 | 1.4 | Incremento e estruturação dos processos do Capítulo 4 (Gerenciamento Técnico). |
| 17/10/2026 | 1.5 | Reestruturação da capa e padronização do histórico de versões conforme diretrizes docentes. |
| 22/10/2026 | 1.6 | Padronização formal da estrutura em Capítulos 1 a 5 e incorporação das diretrizes de `referencias/diretrizes/estrutura-minima-manual.md`. |
| 23/10/2026 | 1.7 | Incorporação do Portal do Cliente (3º módulo), autenticação de cliente LGPD, reserva ACID, e-mail transacional e cancelamento web (ADR-012). |
| 09/11/2026 | 2.0 | Consolidação corporativa da CineSoft Solutions em 3 Macroentregas evolutivas, inclusão das matrizes Make-or-Buy, Pugh Matrix, EAP, diagramas UML/C4/DER e Capítulo 6 (Avaliação e Melhoria MPS.BR). |

---

<div style="page-break-after: always;"></div>

## Documentos de Referência e Controle

- **Base Normativa:** ABNT NBR ISO/IEC/IEEE 12207:2021 (referência local: [`referencias/normas/iso-12207/abnt-iso-iec-12207-2021.pdf`](referencias/normas/iso-12207/abnt-iso-iec-12207-2021.pdf) e transcrição em [`referencias/normas/iso-12207/abnt-iso-iec-12207-2021.md`](referencias/normas/iso-12207/abnt-iso-iec-12207-2021.md)) e Guia Geral MPS de Software (MR-MPS-SW:2024 — SOFTEX).
- **Fonte de Decisões Técnicas:** Especificações Formais de Engenharia e Catálogo de Decisões de Arquitetura (ADRs, disponíveis em [`specs/`](specs/)).
- **Diretrizes Estruturais:** [`referencias/diretrizes/instrucoes-disciplina.md`](referencias/diretrizes/instrucoes-disciplina.md) e [`referencias/diretrizes/estrutura-minima-manual.md`](referencias/diretrizes/estrutura-minima-manual.md).

---

## Sumário

- [Capítulo 1 – Apresentação do software](#capítulo-1--apresentação-do-software)
  - [1.1 Nome e descrição do software](#11-nome-e-descrição-do-software)
  - [1.2 Qual é o software? O que ele faz? Qual problema resolve?](#12-qual-é-o-software-o-que-ele-faz-qual-problema-resolve)
  - [1.3 Público-alvo e contexto de uso](#13-público-alvo-e-contexto-de-uso)
  - [1.4 Quem vai usar? Em que situação? Qual o ambiente de operação esperado?](#14-quem-vai-usar-em-que-situação-qual-o-ambiente-de-operação-esperado)
  - [1.5 Escopo e principais funcionalidades](#15-escopo-e-principais-funcionalidades)
  - [1.6 Restrições e premissas](#16-restrições-e-premissas)
- [Capítulo 2 – Processos de Acordo](#capítulo-2--processos-de-acordo)
  - [2.1 Descrição do processo de aquisição](#21-descrição-do-processo-de-aquisição)
  - [2.2 Descrição do processo de fornecimento](#22-descrição-do-processo-de-fornecimento)
  - [2.3 Identificação dos fornecedores e parceiros relevantes](#23-identificação-dos-fornecedores-e-parceiros-relevantes)
- [Capítulo 3 – Processos Organizacionais Habilitadores](#capítulo-3--processos-organizacionais-habilitadores)
  - [3.1 Modelo de ciclo de vida adotado e justificado](#31-modelo-de-ciclo-de-vida-adotado-e-justificado)
  - [3.2 Inventário de infraestrutura e ferramentas necessárias](#32-inventário-de-infraestrutura-e-ferramentas-necessárias)
  - [3.3 Justificativa estratégica e viabilidade do projeto](#33-justificativa-estratégica-e-viabilidade-do-projeto)
  - [3.4 Papéis, competências e plano de capacitação (RACI)](#34-papéis-competências-e-plano-de-capacitação-raci)
  - [3.5 Plano de qualidade com critérios e métricas](#35-plano-de-qualidade-com-critérios-e-métricas)
  - [3.6 Estratégia de gestão do conhecimento](#36-estratégia-de-gestão-do-conhecimento)
- [Capítulo 4 – Processos de Gerenciamento Técnico](#capítulo-4--processos-de-gerenciamento-técnico)
  - [4.1 Plano de projeto: escopo, cronograma, recursos e entregas](#41-plano-de-projeto-escopo-cronograma-recursos-e-entregas)
  - [4.2 Plano de gestão de riscos: identificação, probabilidade, impacto e respostas](#42-plano-de-gestão-de-riscos-identificação-probabilidade-impacto-e-respostas)
  - [4.3 Plano de gestão de configuração: controle de versões, branches e releases](#43-plano-de-gestão-de-configuração-controle-de-versões-branches-e-releases)
  - [4.4 Registro de decisões técnicas relevantes (ADRs)](#44-registro-de-decisões-técnicas-relevantes-adrs)
  - [4.5 Métricas de acompanhamento do projeto](#45-métricas-de-acompanhamento-do-projeto)
- [Capítulo 5 – Processos Técnicos](#capítulo-5--processos-técnicos)
  - [5.1 Requisitos](#51-requisitos)
  - [5.2 Arquitetura e Design](#52-arquitetura-e-design)
  - [5.3 Implementação e Integração](#53-implementação-e-integração)
  - [5.4 Verificação, Validação e Transição](#54-verificação-validação-e-transição)
  - [5.5 Operação, Manutenção e Descontinuação](#55-operação-manutenção-e-descontinuação)
- [Capítulo 6 – Avaliação e melhoria dos processos de software](#capítulo-6--avaliação-e-melhoria-dos-processos-de-software)
  - [6.1 Referencial e recorte](#61-referencial-e-recorte)
  - [6.2 Diagnóstico do manual](#62-diagnóstico-do-manual)
  - [6.3 Plano de uma melhoria](#63-plano-de-uma-melhoria)
  - [6.4 Atualização e verificação](#64-atualização-e-verificação)
  - [6.5 Acompanhamento da execução](#65-acompanhamento-da-execução)

---

## Índice de aderência à ISO/IEC/IEEE 12207:2021 e MPS.BR

Este índice relaciona cada capítulo do manual ao processo normativo correspondente da ABNT NBR ISO/IEC/IEEE 12207:2021 e do MR-MPS-SW:2024:

| Capítulo do manual | Processo Normativo de Referência | Cláusula / Processo |
|---|---|---|
| **Capítulo 1** | Insumo de Negócio e Elicitação de Stakeholders | ISO 12207 — 6.4.1 e 6.4.2 |
| **Capítulo 2.1** | Acquisition Process (Processo de Aquisição) | ISO 12207 — 6.1.1 |
| **Capítulo 2.2** | Supply Process (Processo de Fornecimento) | ISO 12207 — 6.1.2 |
| **Capítulo 2.3** | Supplier and Partner Management | ISO 12207 — 6.1.1 e 6.1.2 |
| **Capítulo 3.1** | Life Cycle Model Management (Gestão do Modelo de Ciclo de Vida) | ISO 12207 — 6.2.1 |
| **Capítulo 3.2** | Infrastructure Management (Gestão de Infraestrutura) | ISO 12207 — 6.2.2 |
| **Capítulo 3.3** | Portfolio Management (Gestão de Portfólio e Viabilidade) | ISO 12207 — 6.2.3 |
| **Capítulo 3.4** | Human Resource Management (Gestão de Recursos Humanos e RACI) | ISO 12207 — 6.2.4 |
| **Capítulo 3.5** | Quality Management (Gestão da Qualidade) | ISO 12207 — 6.2.5 |
| **Capítulo 3.6** | Knowledge Management (Gestão do Conhecimento) | ISO 12207 — 6.2.6 |
| **Capítulo 4.1** | Project Planning Process (Planejamento do Projeto) | ISO 12207 — 6.3.1 |
| **Capítulo 4.2** | Risk Management Process (Gestão de Riscos) | ISO 12207 — 6.3.4 |
| **Capítulo 4.3** | Configuration Management Process (Gestão de Configuração) | ISO 12207 — 6.3.5 |
| **Capítulo 4.4** | Decision Management Process (Gestão de Decisões / ADRs) | ISO 12207 — 6.3.3 |
| **Capítulo 4.5** | Project Assessment and Control Process (Medição e Avaliação) | ISO 12207 — 6.3.2 |
| **Capítulo 5.1** | Stakeholder & System Requirements Definition (Requisitos) | ISO 12207 — 6.4.2 e 6.4.3 |
| **Capítulo 5.2** | Architecture Definition & Design Definition (Arquitetura e Design) | ISO 12207 — 6.4.4 e 6.4.5 |
| **Capítulo 5.3** | Implementation & Integration Processes (Implementação e Integração) | ISO 12207 — 6.4.7 e 6.4.8 |
| **Capítulo 5.4** | Verification, Validation and Transition (V&V e Transição) | ISO 12207 — 6.4.9, 6.4.10 e 6.4.11 |
| **Capítulo 5.5** | Operation, Maintenance and Disposal (Operação, Manutenção e Descontinuação) | ISO 12207 — 6.4.12, 6.4.13 e 6.4.14 |
| **Capítulo 6** | Avaliação e Melhoria de Processos (Gerência de Projetos) | MR-MPS-SW:2024 — GPR |

---

## Terminologia adotada

Para garantir consistência interna e rigor normativo conforme a ISO/IEC/IEEE 12207:2021, este manual adota os seguintes termos padronizados:

| Termo | Significado |
|---|---|
| **Cliente (Tenant B2B)** | Organização proprietária ou administradora de cinema que contrata o CineDoom sob assinatura SaaS (adquirente). |
| **Operador Interno** | Funcionário autorizado do cinema cliente que opera o back-office ou guichê físico (perfis `GERENTE` e `ATENDENTE`). |
| **Espectador (`CLIENTE` B2C)** | Consumidor final que utiliza o Portal do Cliente para consultar sessões, reservar assentos online ou adquirir ingressos na bilheteria. |
| **CineSoft Solutions** | Empresa de engenharia de software responsável pelo desenvolvimento, evolução em macroentregas, hospedagem gerenciada e suporte do CineDoom. |
| **Produto** | Plataforma web multi-tenant CineDoom fornecida no modelo SaaS B2B2C. |
| **Fornecedor** | Provedor externo contratado pela CineSoft Solutions para infraestrutura em nuvem, banco de dados ou APIs especializadas (ex.: Vercel, Supabase/Neon, Resend, Axiom, Stripe). |

---
