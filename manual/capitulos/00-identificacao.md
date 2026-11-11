# Manual de Processos de Software

### Estudo de Caso: Sistema CineDoom (Plataforma de Gestão Operacional de Cinemas)

---

## 1. Identificação da Equipe e Instituição (Capa e Folha de Rosto)

**Empresa / Equipe:** CineSoft Solutions  
**Produto:** CineDoom — Plataforma de Gestão Operacional e Bilheteria de Cinemas  

**Membros da Equipe (Engenheiros de Software):**
- **Carlos Eduardo Freire da Silva** — Engenheiro de Backend, Segurança & DevOps
- **Gabriel Henrique Lourenço Dias** — Tech Lead & Arquiteto de Software
- **Kayque Vicente Silva** — Engenheiro de Qualidade (QA) & Gerente de Projetos
- **Yury Nogueira de Oliveira Silva** — Engenheiro de Requisitos, UX & Compliance

**Identificação Acadêmica e Institucional:**
- **Instituição:** Universidade Federal de Goiás (UFG) — Instituto de Informática (INF)
- **Curso:** Bacharelado em Engenharia de Software
- **Disciplina:** Processos de Engenharia de Software
- **Docente Orientadora:** Profa. Dra. Juliana Pereira de Souza Zinader
- **Período Letivo:** 2026/2
- **Local e Data:** Goiânia, Novembro de 2026

**Natureza do Trabalho Acadêmico:**  
*Manual de Processos de Software apresentado à disciplina de Processos de Engenharia de Software do curso de Bacharelado em Engenharia de Software da Universidade Federal de Goiás (UFG), como requisito de avaliação para a obtenção da nota final integral da disciplina, referente ao Projeto Integrador.*

---

<div style="page-break-after: always;"></div>

---

## 2. Histórico de Versões do Documento

> **Documento Controlado:** Qualquer alteração neste manual deve ser formalmente registrada nesta tabela e, quando impactar definições de negócio, arquitetura ou escopo, refletida no catálogo de decisões de arquitetura e especificações do projeto (`specs/`).

| Data | Versão | Descrição Sucinta da Alteração |
| :---: | :---: | :--- |
| 10/09/2026 | Versão 1.0 | Criação do documento, identificação da equipe e elaboração da capa. |
| 16/09/2026 | Versão 1.1 | Elaboração dos itens do Capítulo 1 (Apresentação do Software). |
| 24/09/2026 | Versão 1.2 | Alinhamento dos Capítulos 1, 2 e 3 à norma ISO/IEC/IEEE 12207:2021. |
| 24/09/2026 | Versão 1.3 | Revisão técnica: correção de contradições e justificativas de aquisição. |
| 08/10/2026 | Versão 1.4 | Incremento e estruturação dos processos do Capítulo 4 (Gerenciamento Técnico). |
| 17/10/2026 | Versão 1.5 | Reestruturação da capa e padronização do controle documental. |
| 22/10/2026 | Versão 1.6 | Padronização formal da estrutura editorial dos Capítulos 1 a 5. |
| 23/10/2026 | Versão 1.7 | Incorporação do Portal do Cliente, reserva ACID, e-mail e LGPD (ADR-012). |
| 09/11/2026 | Versão 2.0 | Consolidação em 3 Macroentregas, matrizes Make-or-Buy, Pugh, EAP e Cap. 6 (MPS.BR). |

*Fonte: Elaborado pelos autores (2026).*

---

<div style="page-break-after: always;"></div>

---

## 3. Lista de Figuras

| Identificador | Título da Figura |
| :---: | :--- |
| **Figura 1** | Portal do Cliente: catálogo de filmes e mapa interativo de assentos |
| **Figura 2** | Bilheteria presencial: mapa de assentos e operação de guichê |
| **Figura 3** | Back-office gerencial: programação de sessões e indicadores de ocupação |
| **Figura 4** | Diagrama de Classes do Domínio de Negócios CineDoom |
| **Figura 5** | Diagrama de Sequência UML: Reserva Web e Emissão de Voucher |
| **Figura 6** | Diagrama C4 Nível 2: Contêineres da Plataforma CineDoom |
| **Figura 7** | Diagrama de Máquina de Estados do Ciclo de Vida da Poltrona |
| **Figura 8** | Diagrama Entidade-Relacionamento (DER) do Banco PostgreSQL |

---

<div style="page-break-after: always;"></div>

---

## 4. Lista de Tabelas

| Identificador | Título da Tabela |
| :---: | :--- |
| **Tabela 1** | Matriz de Perfis de Usuários e Permissões de Acesso |
| **Tabela 2** | Análise de Aquisição: Componentes de Software e Domínio (Make or Buy) |
| **Tabela 3** | Análise de Aquisição: Infraestrutura Cloud e Serviços Gerenciados (Make or Buy) |
| **Tabela 4** | Perspectiva de Fornecimento e Ativos Comercializáveis |
| **Tabela 5** | Acordo de Nível de Serviço (SLA) e Suporte Pós-Entrega |
| **Tabela 6** | Identificação dos Fornecedores e Parceiros Relevantes |
| **Tabela 7** | Inventário de Infraestrutura e Ferramentas |
| **Tabela 8** | Composição da Equipe e Competências Técnicas Requeridas |
| **Tabela 9** | Matriz RACI de Responsabilidades por Membro da Equipe |
| **Tabela 10** | Escopo e Marcos Comerciais por Macroentrega (Milestones) |
| **Tabela 11** | Cronograma Executivo e Pacotes de Trabalho por Sprint |
| **Tabela 12** | Plano de Recursos Humanos e Operacionais |
| **Tabela 13** | Matriz de Riscos do Produto e Ações Preventivas (Risk Register) |
| **Tabela 14** | Matriz de Decisão Ponderada (Pugh Matrix) — Arquitetura Base |
| **Tabela 15** | Quadro Sinóptico de Decisões de Arquitetura: Stack e Persistência (ADR-001 a ADR-006) |
| **Tabela 16** | Quadro Sinóptico de Decisões de Arquitetura: Concorrência e Resiliência (ADR-007 a ADR-012) |
| **Tabela 17** | Indicadores e Métricas de Monitoramento do Projeto |
| **Tabela 18** | Catálogo Formal de Requisitos Funcionais: Domínio e Bilheteria (RF-01 a RF-09) |
| **Tabela 19** | Catálogo Formal de Requisitos Funcionais: Governança, Portal e Notificações (RF-10 a RF-18) |
| **Tabela 20** | Catálogo Formal de Requisitos Não Funcionais (ISO/IEC 25010) |
| **Tabela 21** | Matriz de Rastreabilidade Bidirecional de Requisitos |
| **Tabela 22** | Mapeamento de Stakeholders e Técnicas de Elicitação |
| **Tabela 23** | Distinção Conceitual entre Verificação e Validação |
| **Tabela 24** | Critérios Formais de Entrada e Saída de V&V |
| **Tabela 25** | Relatório de Testes de Aceitação e Homologação em Produção |
| **Tabela 26** | Diagnóstico de Avaliação e Maturidade de Processo (Versão 1.7) |
| **Tabela 27** | Plano de Melhoria de Processo de Software (PMP) |
| **Tabela 28** | Quadro Comparativo: Antes vs. Depois da Revisão de Processos |
| **Tabela 29** | Reavaliação Pós-Melhoria da Conformidade do Manual (Versão 2.0) |

---

<div style="page-break-after: always;"></div>

---

## 5. Lista de Abreviaturas e Siglas

| Sigla | Significado Completo | Sigla | Significado Completo |
| :---: | :--- | :---: | :--- |
| **ABNT** | Associação Brasileira de Normas Técnicas | **MPS.BR** | Melhoria de Processo do Software Brasileiro |
| **ADR** | *Architecture Decision Record* | **MTTR** | *Mean Time To Recovery* |
| **API** | *Application Programming Interface* | **MVP** | *Minimum Viable Product* |
| **B2B / B2C** | *Business-to-Business / Consumer* | **NFC-e** | Nota Fiscal de Consumidor Eletrônica |
| **CI / CD** | *Continuous Integration / Deployment* | **ORM** | *Object-Relational Mapping* |
| **DoD / DoR** | *Definition of Done / Definition of Ready* | **PaaS** | *Platform as a Service* |
| **GPP** | Gerência de Portfólio de Projetos | **PIX** | Pagamento Instantâneo Brasileiro |
| **GPR** | Gerência de Projetos (MPS.BR — Nível G) | **PMP** | Plano de Melhoria de Processo |
| **GQM** | *Goal-Question-Metric* | **PPR** | Processo Padrão de Requisitos |
| **GQA** | Garantia da Qualidade (MPS.BR — Nível F) | **QA** | *Quality Assurance* |
| **GCO** | Gerência de Configuração (MPS.BR — Nível F) | **RBAC** | *Role-Based Access Control* |
| **IEC** | *International Electrotechnical Commission* | **SaaS** | *Software as a Service* |
| **IEEE** | *Institute of Electrical and Electronics Engineers* | **SLA / SLO** | *Service Level Agreement / Objective* |
| **ISO** | *International Organization for Standardization* | **SPICE** | ISO/IEC 15504 Process Improvement |
| **JWT** | *JSON Web Token* (RFC 7519) | **UFG** | Universidade Federal de Goiás |
| **LGPD** | Lei Geral de Proteção de Dados (Lei 13.709/2018) | **UI / UX** | *User Interface / User Experience* |
| **MED** | Medição (MPS.BR — Nível F) | **V&V** | Verificação e Validação |
| **WBS / EAP** | *Work Breakdown Structure* (Estrutura Analítica do Projeto) | | |

---

<div style="page-break-after: always;"></div>

---

## 6. Sumário

- [Capítulo 1 – Apresentação do software](#capítulo-1--apresentação-do-software)
  - [1.1 Nome e descrição do software](#11-nome-e-descrição-do-software)
  - [1.2 Qual é o software? O que ele faz? Qual problema resolve?](#12-qual-é-o-software-o-que-ele-faz-qual-problema-resolve)
    - [O que ele faz?](#o-que-ele-faz)
    - [Qual problema resolve?](#qual-problema-resolve)
    - [Proposta de valor](#proposta-de-valor)
  - [1.3 Público-alvo e contexto de uso](#13-público-alvo-e-contexto-de-uso)
  - [1.4 Quem vai usar? Em que situação? Qual o ambiente de operação esperado?](#14-quem-vai-usar-em-que-situação-qual-o-ambiente-de-operação-esperado)
    - [Perfis de Usuários](#perfis-de-usuários)
    - [Ambiente de Operação Esperado](#ambiente-de-operação-esperado)
  - [1.5 Escopo e principais funcionalidades](#15-escopo-e-principais-funcionalidades)
    - [Escopo Central e Módulos do Sistema](#escopo-central-e-módulos-do-sistema)
    - [Fora do escopo imediato da Macroentrega 1](#fora-do-escopo-imediato-da-macroentrega-1)
  - [1.6 Restrições e premissas](#16-restrições-e-premissas)
    - [Restrições](#restrições)
    - [Premissas](#premissas)
- [Capítulo 2 – Processos de Acordo](#capítulo-2--processos-de-acordo)
  - [2.1 Descrição do processo de aquisição](#21-descrição-do-processo-de-aquisição)
    - [Fronteira e Justificativa de Aquisição](#fronteira-e-justificativa-de-aquisição)
    - [Análise de Aquisição (Make or Buy)](#análise-de-aquisição-make-or-buy)
    - [As Cinco Atividades do Processo de Aquisição (ISO 12207)](#as-cinco-atividades-do-processo-de-aquisição-iso-12207)
  - [2.2 Descrição do processo de fornecimento](#22-descrição-do-processo-de-fornecimento)
    - [Perspectiva de Fornecimento e Ativos Comercializáveis](#perspectiva-de-fornecimento-e-ativos-comercializáveis)
    - [Termos do Acordo, Entregáveis e Evolução por Macroentregas](#termos-do-acordo-entregáveis-e-evolução-por-macroentregas)
    - [Critérios de Aceite Formal pelo Cliente Adquirente](#critérios-de-aceite-formal-pelo-cliente-adquirente)
    - [Acordo de Nível de Serviço (SLA) e Suporte Pós-Entrega](#acordo-de-nível-de-serviço-sla-e-suporte-pós-entrega)
  - [2.3 Identificação dos fornecedores e parceiros relevantes](#23-identificação-dos-fornecedores-e-parceiros-relevantes)
- [Capítulo 3 – Processos Organizacionais Habilitadores](#capítulo-3--processos-organizacionais-habilitadores)
  - [3.1 Modelo de ciclo de vida adotado e justificado](#31-modelo-de-ciclo-de-vida-adotado-e-justificado)
    - [Estrutura das Fases, Cerimônias e Macroentregas](#estrutura-das-fases-cerimônias-e-macroentregas)
    - [Justificativa da Escolha do Modelo](#justificativa-da-escolha-do-modelo)
  - [3.2 Inventário de infraestrutura e ferramentas necessárias](#32-inventário-de-infraestrutura-e-ferramentas-necessárias)
  - [3.3 Justificativa estratégica e viabilidade do projeto](#33-justificativa-estratégica-e-viabilidade-do-projeto)
  - [3.4 Papéis, competências e plano de capacitação (RACI)](#34-papéis-competências-e-plano-de-capacitação-raci)
    - [Composição da Equipe e Competências Requeridas](#composição-da-equipe-e-competências-requeridas)
    - [Matriz RACI Consolidada por Membro da Equipe](#matriz-raci-consolidada-por-membro-da-equipe)
    - [Plano de Capacitação Técnica Contínua](#plano-de-capacitação-técnica-contínua)
  - [3.5 Plano de qualidade com critérios e métricas](#35-plano-de-qualidade-com-critérios-e-métricas)
  - [3.6 Estratégia de gestão do conhecimento](#36-estratégia-de-gestão-do-conhecimento)
- [Capítulo 4 – Processos de Gerenciamento Técnico](#capítulo-4--processos-de-gerenciamento-técnico)
  - [4.1 Plano de projeto: escopo, cronograma, recursos e entregas](#41-plano-de-projeto-escopo-cronograma-recursos-e-entregas)
    - [Estrutura Analítica do Projeto (EAP / WBS em 3 Níveis)](#estrutura-analítica-do-projeto-eap--wbs-em-3-níveis)
    - [Escopo e Marcos Comerciais por Macroentrega (Milestones)](#escopo-e-marcos-comerciais-por-macroentrega-milestones)
    - [Cronograma Detalhado de Execução da Macroentrega 1 (v1.0.0)](#cronograma-detalhado-de-execução-da-macroentrega-1-v100)
    - [Recursos](#recursos)
    - [Rotina de Acompanhamento e Tratamento de Desvios e Atrasos](#rotina-de-acompanhamento-e-tratamento-de-desvios-e-atrasos)
  - [4.2 Plano de gestão de riscos: identificação, probabilidade, impacto e respostas](#42-plano-de-gestão-de-riscos-identificação-probabilidade-impacto-e-respostas)
    - [Critérios de Classificação e Reavaliação Contínua](#critérios-de-classificação-e-reavaliação-contínua)
    - [Matriz de Riscos do Produto (Risk Register)](#matriz-de-riscos-do-produto-risk-register)
  - [4.3 Plano de gestão de configuração: controle de versões, branches e releases](#43-plano-de-gestão-de-configuração-controle-de-versões-branches-e-releases)
  - [4.4 Registro de decisões técnicas relevantes (ADRs)](#44-registro-de-decisões-técnicas-relevantes-adrs)
    - [Contextualização e Padrão Adotado (MADR)](#contextualização-e-padrão-adotado-madr)
    - [Matriz de Decisão Ponderada (Pugh Matrix) — Escolha da Arquitetura Base (ADR-001)](#matriz-de-decisão-ponderada-pugh-matrix--escolha-da-arquitetura-base-adr-001)
    - [Fichas Estruturadas de Decisões Arquiteturais (ADR-001 a ADR-012)](#fichas-estruturadas-de-decisões-arquiteturais-adr-001-a-adr-012)
  - [4.5 Métricas de acompanhamento do projeto](#45-métricas-de-acompanhamento-do-projeto)
- [Capítulo 5 – Processos Técnicos](#capítulo-5--processos-técnicos)
  - [5.1 Requisitos](#51-requisitos)
    - [5.1.1 Catálogo formal de requisitos](#511-catálogo-formal-de-requisitos)
    - [5.1.2 Matriz de rastreabilidade bidirecional de requisitos](#512-matriz-de-rastreabilidade-bidirecional-de-requisitos)
    - [5.1.3 Critérios de aceitação (CA-01 a CA-14)](#513-critérios-de-aceitação-ca-01-a-ca-14)
    - [5.1.4 Mapeamento de partes interessadas e técnicas de elicitação](#514-mapeamento-de-partes-interessadas-e-técnicas-de-elicitação)
  - [5.2 Arquitetura e Design](#52-arquitetura-e-design)
    - [5.2.1 Visão Geral e Princípios Arquiteturais](#521-visão-geral-e-princípios-arquiteturais)
    - [5.2.2 Diagramas Arquiteturais e de Domínio](#522-diagramas-arquiteturais-e-de-domínio)
  - [5.3 Implementação e Integração](#53-implementação-e-integração)
  - [5.4 Verificação, Validação e Transição](#54-verificação-validação-e-transição)
    - [5.4.1 Distinção formal entre Verificação e Validação](#541-distinção-formal-entre-verificação-e-validação)
    - [5.4.2 Critérios de aceitação por stakeholder](#542-critérios-de-aceitação-por-stakeholder)
    - [5.4.3 Relatório de testes de aceitação (Homologação e Produção)](#543-relatório-de-testes-de-aceitação-homologação-e-produção)
  - [5.5 Operação, Manutenção e Descontinuação](#55-operação-manutenção-e-descontinuação)
- [Capítulo 6 – Avaliação e melhoria dos processos de software](#capítulo-6--avaliação-e-melhoria-dos-processos-de-software)
  - [6.1 Referencial e recorte](#61-referencial-e-recorte)
  - [6.2 Diagnóstico do manual](#62-diagnóstico-do-manual)
  - [6.3 Plano de uma melhoria](#63-plano-de-uma-melhoria)
  - [6.4 Atualização e verificação](#64-atualização-e-verificação)
  - [6.5 Acompanhamento da execução](#65-acompanhamento-da-execução)

---

## 7. Documentos de Referência e Controle

- **Base Normativa Internacional:** ABNT NBR ISO/IEC/IEEE 12207:2021 (*Systems and software engineering — Software life cycle processes*), disponível no acervo local: [`referencias/normas/iso-12207/abnt-iso-iec-12207-2021.pdf`](referencias/normas/iso-12207/abnt-iso-iec-12207-2021.pdf) e transcrição em [`referencias/normas/iso-12207/abnt-iso-iec-12207-2021.md`](referencias/normas/iso-12207/abnt-iso-iec-12207-2021.md).
- **Modelo de Referência Nacional:** Guia Geral MPS de Software (MR-MPS-SW:2024 — SOFTEX), níveis G (Gerência de Projetos e Requisitos) e F (Medição, Configuração e Garantia da Qualidade).
- **Decisões Técnicas e Arquiteturais:** Catálogo Formal de Architecture Decision Records (ADRs, ADR-001 a ADR-012, disponíveis em [`specs/adrs/`](specs/adrs/)).
- **Diretrizes Acadêmicas da Disciplina:** [`referencias/diretrizes/instrucoes-disciplina.md`](referencias/diretrizes/instrucoes-disciplina.md) e [`referencias/diretrizes/criterios-avaliacao-projeto-integrador.md`](referencias/diretrizes/criterios-avaliacao-projeto-integrador.md).

---

## 8. Índice de Aderência à ISO/IEC/IEEE 12207:2021 e MPS.BR

Este índice relaciona cada capítulo e processo deste manual ao processo normativo correspondente da ABNT NBR ISO/IEC/IEEE 12207:2021 e aos processos do modelo MR-MPS-SW:2024:

| Capítulo do Manual | Processo Normativo de Referência | Cláusula / Processo |
|---|---|---|
| **Capítulo 1** | Insumo de Negócio e Elicitação de Stakeholders | ISO 12207 — Cláusulas 6.4.1 e 6.4.2 |
| **Capítulo 2.1** | *Acquisition Process* (Processo de Aquisição) | ISO 12207 — Cláusula 6.1.1 |
| **Capítulo 2.2** | *Supply Process* (Processo de Fornecimento) | ISO 12207 — Cláusula 6.1.2 |
| **Capítulo 2.3** | *Supplier and Partner Management* | ISO 12207 — Cláusulas 6.1.1 e 6.1.2 |
| **Capítulo 3.1** | *Life Cycle Model Management* (Gestão do Modelo de Ciclo de Vida) | ISO 12207 — Cláusula 6.2.1 |
| **Capítulo 3.2** | *Infrastructure Management* (Gestão de Infraestrutura) | ISO 12207 — Cláusula 6.2.2 |
| **Capítulo 3.3** | *Portfolio Management* (Gestão de Portfólio e Viabilidade) | ISO 12207 — Cláusula 6.2.3 |
| **Capítulo 3.4** | *Human Resource Management* (Gestão de RH e RACI) | ISO 12207 — Cláusula 6.2.4 |
| **Capítulo 3.5** | *Quality Management* (Gestão da Qualidade) | ISO 12207 — Cláusula 6.2.5 |
| **Capítulo 3.6** | *Knowledge Management* (Gestão do Conhecimento) | ISO 12207 — Cláusula 6.2.6 |
| **Capítulo 4.1** | *Project Planning Process* (Planejamento do Projeto) | ISO 12207 — Cláusula 6.3.1 (MPS.BR: GPR) |
| **Capítulo 4.2** | *Risk Management Process* (Gestão de Riscos) | ISO 12207 — Cláusula 6.3.4 (MPS.BR: GPR) |
| **Capítulo 4.3** | *Configuration Management Process* (Gestão de Configuração) | ISO 12207 — Cláusula 6.3.5 (MPS.BR: GCO) |
| **Capítulo 4.4** | *Decision Management Process* (Gestão de Decisões / ADRs) | ISO 12207 — Cláusula 6.3.3 |
| **Capítulo 4.5** | *Project Assessment and Control Process* (Medição e Avaliação) | ISO 12207 — Cláusula 6.3.2 (MPS.BR: MED) |
| **Capítulo 5.1** | *Stakeholder & System Requirements Definition* (Requisitos) | ISO 12207 — Cláusulas 6.4.2 e 6.4.3 (MPS.BR: GPR/REQ) |
| **Capítulo 5.2** | *Architecture Definition & Design Definition* (Arquitetura e Design) | ISO 12207 — Cláusulas 6.4.4 e 6.4.5 |
| **Capítulo 5.3** | *Implementation & Integration Processes* (Implementação e Integração) | ISO 12207 — Cláusulas 6.4.7 e 6.4.8 |
| **Capítulo 5.4** | *Verification, Validation and Transition* (V&V e Transição) | ISO 12207 — Cláusulas 6.4.9, 6.4.10 e 6.4.11 (MPS.BR: GQA) |
| **Capítulo 5.5** | *Operation, Maintenance and Disposal* (Operação e Manutenção) | ISO 12207 — Cláusulas 6.4.12, 6.4.13 e 6.4.14 |
| **Capítulo 6** | Avaliação e Melhoria de Processos (Gerência de Projetos) | MR-MPS-SW:2024 — Nível G (GPR) e Nível F (GQA) |

---

## 9. Terminologia Adotada

Para garantir consistência interna e rigor normativo conforme a ISO/IEC/IEEE 12207:2021 e a legislação vigente, este manual adota os seguintes termos formais padronizados:

| Termo | Significado e Contexto de Aplicação |
|---|---|
| **Cliente (*Tenant* B2B)** | Organização proprietária ou administradora de cinema que contrata o CineDoom sob assinatura SaaS multi-tenant (adquirente do serviço). |
| **Operador Interno** | Funcionário autorizado do cinema cliente que opera os módulos de gestão ou bilheteria física (perfis `GERENTE` e `ATENDENTE`). |
| **Espectador (`CLIENTE` B2C)** | Consumidor final que utiliza o Portal do Cliente para consultar filmes, reservar poltronas online ou realizar compra presencial no guichê. |
| **CineSoft Solutions** | Organização desenvolvedora responsável pela engenharia, evolução em macroentregas, infraestrutura gerenciada e sustentação do CineDoom. |
| **Produto (CineDoom)** | Plataforma web integrada com isolamento lógico multi-tenant fornecida no modelo B2B2C. |
| **Fornecedor Externo** | Provedor de computação em nuvem, banco de dados ou APIs especializadas contratado pela CineSoft (ex.: Vercel, Supabase/Neon, Resend, Axiom, Stripe). |
| **Reserva Atômica (ACID)** | Bloqueio transitório de assento sob concorrência simultânea via `SELECT FOR UPDATE` determinístico, imune a venda dupla (*double-booking*). |
| **Expiração JIT (*Just-in-Time*)** | Invalidação automática em tempo de consulta/transação de reservas não confirmadas a menos de 60 minutos da sessão. |
| **Anonimização *In-Place*** | Sobrescrita criptográfica irreversível de dados pessoais (Art. 18 da LGPD), preservando a integridade dos registros contábeis e fiscais. |
