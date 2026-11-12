# Manual de Processos de Software

## Capa

**Manual de Processos de Software**

**Grupo:** Doomscoders

- Carlos Eduardo Freire da Silva
- Gabriel Henrique Lourenço Dias
- Kayque Vicente Silva
- Yury Nogueira de Oliveira Silva

**Orientadora:** Profa. Dra. Juliana Pereira de Souza Zinader  
**Referência:** ABNT NBR ISO/IEC/IEEE 12207:2021

---

<div style="page-break-after: always;"></div>

---

## Folha de Rosto

- Carlos Eduardo Freire da Silva
- Gabriel Henrique Lourenço Dias
- Kayque Vicente Silva
- Yury Nogueira de Oliveira Silva

**Manual de Processos de Software**

Manual de Processos de Software apresentado à disciplina de Processos de Engenharia de Software do curso de Bacharelado em Engenharia de Software da Universidade Federal de Goiás (UFG), como requisito de avaliação para a obtenção da nota final integral da disciplina, referente ao Projeto Integrador.

**Orientadora:** Profª. Dra. Juliana Pereira de Souza Zinader  
**Local e Ano:** Goiânia, 2026

---

<div style="page-break-after: always;"></div>

---

## Histórico de Versões do Documento

| Data | Versão | Descrição Sucinta da Alteração |
| :---: | :---: | :--- |
| 10/09/2026 | Versão 1.0 | Criação do documento, identificação da equipe, elaboração da capa e estruturação inicial dos Capítulos 1 e 2. |
| 16/09/2026 | Versão 1.1 | Elaboração e estruturação inicial do Capítulo 3. |
| 24/09/2026 | Versão 1.2 | Revisão e adequação dos Capítulos 1 a 3 à norma ABNT NBR ISO/IEC/IEEE 12207:2021. |
| 01/10/2026 | Versão 1.3 | Elaboração e estruturação inicial do Capítulo 4. |
| 07/10/2026 | Versão 1.4 | Elaboração e estruturação inicial do Capítulo 5. |
| 17/10/2026 | Versão 1.5 | Reestruturação da capa e padronização do controle documental. |
| 22/10/2026 | Versão 1.6 | Padronização formal da estrutura editorial dos Capítulos 1 a 5. |
| 23/10/2026 | Versão 1.7 | Consolidação do conteúdo dos Capítulos 1 a 5 e organização dos artefatos. |
| 05/11/2026 | Versão 1.8 | Elaboração e estruturação inicial do Capítulo 6. |
| 09/11/2026 | Versão 2.0 | Revisão das seções 4.1, 4.2 e 4.5 conforme o plano de melhoria e consolidação do Capítulo 6. |
| 09/11/2026 | Versão 2.1 | Revisão e adequação dos elementos dos capítulos e integração à estrutura geral do manual. |
| 12/11/2026 | Versão 2.2 | Revisão. |

*Fonte: Elaborado pelos autores (2026).*

---

<div style="page-break-after: always;"></div>

---

## Lista de Figuras

| Identificador | Título da Figura |
| :---: | :--- |
| **Figura 1** | Portal do Cliente: catálogo de filmes e mapa interativo de assentos |
| **Figura 2** | Bilheteria presencial: mapa de assentos e operação de guichê |
| **Figura 3** | Back-office gerencial: programação de sessões e indicadores de ocupação |
| **Figura 4** | Ciclo Iterativo de Desenvolvimento e Roadmap de Evolução do Produto |
| **Figura 5** | Organização corporativa CINESOFT-SOLUTIONS no GitHub e repositórios oficiais |
| **Figura 6** | Quadro Kanban corporativo no GitHub Projects v2 |
| **Figura 7** | Estrutura Analítica do Projeto (EAP) do CineDoom |
| **Figura 8** | Cronograma macro das macroentregas |
| **Figura 9** | Quadro Kanban do projeto no GitHub Projects |
| **Figura 10** | Estratégia de branches |
| **Figura 11** | Fluxo de release, reversão e correção urgente |
| **Figura 12** | Execução do pipeline de integração contínua |
| **Figura 13** | Baseline da versão `v1.0.0` no GitHub |
| **Figura 14** | Ciclo de vida de um ADR |
| **Figura 15** | Registro dos ADRs no repositório |
| **Figura 16** | Ciclo de medição e decisão |
| **Figura 17** | Evidência do fluxo de trabalho |
| **Figura 18** | Cadeia de Rastreabilidade: da Macroentrega 1 ao Teste de Código (exemplo real: Issues #9 e #10) |
| **Figura 19** | Diagrama C4 Nível 2: Contêineres da Plataforma CineDoom |
| **Figura 20** | Diagrama de Sequência UML: Reserva Online Atômica e Baixa Presencial no Balcão |
| **Figura 21** | Diagrama de Classes UML: Modelo de Domínio do CineDoom |
| **Figura 22** | Formulário da Pesquisa de Experiência do Usuário (Google Forms) |

---

<div style="page-break-after: always;"></div>

---

## Lista de Tabelas

| Identificador | Título da Tabela |
| :---: | :--- |
| **Tabela 1** | Matriz de Perfis de Usuários e Permissões de Acesso |
| **Tabela 2** | Análise de Aquisição: Componentes de Software e Domínio (Make or Buy) |
| **Tabela 3** | Análise de Aquisição: Infraestrutura Cloud e Serviços Gerenciados (Make or Buy) |
| **Tabela 4** | Perspectiva de Fornecimento e Ativos Comercializáveis |
| **Tabela 5** | Acordo de Nível de Serviço (SLA) e Suporte Pós-Entrega |
| **Tabela 6** | Identificação dos Fornecedores e Parceiros Relevantes |
| **Tabela 7** | Inventário de infraestrutura e ferramentas organizacionais |
| **Tabela 8** | Composição da Equipe e Especialidades Técnicas |
| **Tabela 9** | Matriz de Responsabilidades por Atividade (RACI) |
| **Tabela 10** | Competências Requeridas, Lacunas e Ações |
| **Tabela 11** | Plano de Capacitação |
| **Tabela 12** | Diretrizes e Princípios de Engenharia Adotados |
| **Tabela 13** | Métricas de Qualidade |
| **Tabela 14** | Ativos de Conhecimento |
| **Tabela 15** | Macroentregas, escopo e critérios de aceite |
| **Tabela 16** | Execução das Sprints da Macroentrega 1 |
| **Tabela 17** | Recursos de infraestrutura e custo estimado |
| **Tabela 18** | Protocolo de tratamento de desvios |
| **Tabela 19** | Escalas de probabilidade e impacto |
| **Tabela 20** | Matriz de prioridade (probabilidade × impacto) |
| **Tabela 21** | Identificação e análise dos riscos |
| **Tabela 22** | Tratamento e monitoramento dos riscos |
| **Tabela 23** | Itens de configuração controlados |
| **Tabela 24** | Branches e regras de proteção |
| **Tabela 25** | Versionamento semântico e convenção de commits |
| **Tabela 26** | Matriz de decisão ponderada da arquitetura base |
| **Tabela 27** | Ficha do ADR-001 |
| **Tabela 28** | Índice dos ADRs |
| **Tabela 29** | Plano de medição |
| **Tabela 30** | Resultados na Macroentrega 1 (`v1.0.0`) e ação em caso de desvio |
| **Tabela 31** | Catálogo Formal de Requisitos Funcionais (RF-01 a RF-18) |
| **Tabela 32** | Catálogo Formal de Requisitos Não Funcionais (RNF-01 a RNF-06 — ISO/IEC 25010) |
| **Tabela 33** | Matriz de Rastreabilidade — Visão Compacta |
| **Tabela 34** | Mapeamento de Stakeholders e Técnicas de Elicitação |
| **Tabela 35** | Identificação e Escopo do Documento de Arquitetura |
| **Tabela 36** | Zonas Internas da Arquitetura e Regras de Dependência |
| **Tabela 37** | Catálogo de Componentes (Módulos de Domínio) |
| **Tabela 38** | Decisões Arquiteturais (ADRs) e Efeito Verificável |
| **Tabela 39** | Critérios Formais de Entrada e Saída de V&V |
| **Tabela 40** | Relatório de Testes de Aceitação e Homologação em Produção |
| **Tabela 41** | Planejamento da Transição por Branch e Ambiente |
| **Tabela 42** | Modalidades de Manutenção |
| **Tabela 43** | Etapas da Descontinuação e Migração de Dados |
| **Tabela 44** | Diagnóstico de Avaliação e Maturidade de Processo (Versão 1.7) |
| **Tabela 45** | Plano de Melhoria de Processo de Software (PMP) |
| **Tabela 46** | Quadro Comparativo: Antes vs. Depois da Revisão de Processos |
| **Tabela 47** | Reavaliação Pós-Melhoria da Conformidade do Manual (Versão 2.0) |

---

<div style="page-break-after: always;"></div>

---

## Lista de Abreviaturas e Siglas

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

## Sumário

- [Capítulo 1 – Apresentação do Software](#capítulo-1--apresentação-do-software)
  - [1.1 Nome e Descrição do Software](#11-nome-e-descrição-do-software)
  - [1.2 Qual é o Software? O que ele faz? Qual problema resolve?](#12-qual-é-o-software-o-que-ele-faz-qual-problema-resolve)
    - [O que ele faz?](#o-que-ele-faz)
    - [Qual problema resolve?](#qual-problema-resolve)
    - [Proposta de valor](#proposta-de-valor)
  - [1.3 Público-alvo e Contexto de Uso](#13-público-alvo-e-contexto-de-uso)
    - [Contextos de uso típicos](#contextos-de-uso-típicos)
  - [1.4 Quem vai usar? Em que situação? Qual o ambiente de operação esperado?](#14-quem-vai-usar-em-que-situação-qual-o-ambiente-de-operação-esperado)
    - [Perfis de Usuários e Situações de Uso](#perfis-de-usuários-e-situações-de-uso)
    - [Ambiente de Operação Esperado](#ambiente-de-operação-esperado)
  - [1.5 Escopo e principais funcionalidades](#15-escopo-e-principais-funcionalidades)
    - [Funcionalidades Incluídas (Escopo Atual)](#funcionalidades-incluídas-escopo-atual)
    - [Fora do Escopo Imediato](#fora-do-escopo-imediato)
  - [1.6 Restrições e premissas](#16-restrições-e-premissas)
    - [Restrições do Projeto](#restrições-do-projeto)
    - [Premissas Adotadas](#premissas-adotadas)
- [Capítulo 2 – Processos de Acordo](#capítulo-2--processos-de-acordo)
  - [2.1 Processo de Aquisição: Decisões e Gestão de Provedores](#21-processo-de-aquisição-decisões-e-gestão-de-provedores)
    - [O que construímos e o que contratamos (Make or Buy)](#o-que-construímos-e-o-que-contratamos-make-or-buy)
    - [O Ciclo Prático de Aquisição de Provedores](#o-ciclo-prático-de-aquisição-de-provedores)
  - [2.2 Processo de Fornecimento: Comercialização, Entrega e Operação](#22-processo-de-fornecimento-comercialização-entrega-e-operação)
    - [Modelos de Negócio e Ativos Disponíveis](#modelos-de-negócio-e-ativos-disponíveis)
    - [Jornada do Cliente: Da Contratação ao Pós-Venda](#jornada-do-cliente-da-contratação-ao-pós-venda)
    - [Entregáveis da Implantação e Evolução Funcional](#entregáveis-da-implantação-e-evolução-funcional)
    - [Critérios de Aceite Formal](#critérios-de-aceite-formal)
    - [Níveis de Serviço (SLA) e Atendimento](#níveis-de-serviço-sla-e-atendimento)
  - [2.3 Fornecedores e Parceiros de Tecnologia](#23-fornecedores-e-parceiros-de-tecnologia)
- [Capítulo 3 – Processos Organizacionais Habilitadores](#capítulo-3--processos-organizacionais-habilitadores)
  - [3.1 Modelo de Ciclo de Vida do Projeto](#31-modelo-de-ciclo-de-vida-do-projeto)
    - [Fases de Engenharia e Evolução em Três Macroentregas](#fases-de-engenharia-e-evolução-em-três-macroentregas)
    - [Fluxo de Trabalho no Git (Política Corporativa de Branches)](#fluxo-de-trabalho-no-git-política-corporativa-de-branches)
    - [Organização das Iterações e Práticas de Trabalho](#organização-das-iterações-e-práticas-de-trabalho)
    - [Governança, Avaliação e Melhoria Contínua do Ciclo de Vida](#governança-avaliação-e-melhoria-contínua-do-ciclo-de-vida)
  - [3.2 Infraestrutura e Ferramentas Organizacionais](#32-infraestrutura-e-ferramentas-organizacionais)
    - [Critérios de Seleção e Requisitos](#critérios-de-seleção-e-requisitos)
    - [A Organização no GitHub (CINESOFT-SOLUTIONS)](#a-organização-no-github-cinesoft-solutions)
    - [Inventário de Ferramentas Disponibilizadas](#inventário-de-ferramentas-disponibilizadas)
    - [Ambientes de Execução e Manutenção Contínua](#ambientes-de-execução-e-manutenção-contínua)
  - [3.3 Justificativa Estratégica e Viabilidade do Projeto](#33-justificativa-estratégica-e-viabilidade-do-projeto)
    - [Oportunidade e Alinhamento Estratégico](#oportunidade-e-alinhamento-estratégico)
    - [Identificação e Autorização do Projeto](#identificação-e-autorização-do-projeto)
    - [Dimensões de Viabilidade](#dimensões-de-viabilidade)
    - [Alocação de Recursos](#alocação-de-recursos)
    - [Avaliação, Sustentação e Encerramento](#avaliação-sustentação-e-encerramento)
  - [3.4 Papéis, Competências e Plano de Capacitação (RACI)](#34-papéis-competências-e-plano-de-capacitação-raci)
    - [Composição da Equipe e Atribuição de Papéis](#composição-da-equipe-e-atribuição-de-papéis)
    - [Matriz de Responsabilidades (RACI)](#matriz-de-responsabilidades-raci)
    - [Competências Requeridas e Lacunas](#competências-requeridas-e-lacunas)
    - [Plano de Capacitação Contínua](#plano-de-capacitação-contínua)
    - [Avaliação, Registros e Riscos da Equipe](#avaliação-registros-e-riscos-da-equipe)
  - [3.5 Plano de Qualidade: Diretrizes, Critérios e Métricas](#35-plano-de-qualidade-diretrizes-critérios-e-métricas)
    - [Política e Objetivos de Qualidade](#política-e-objetivos-de-qualidade)
    - [Responsabilidades](#responsabilidades)
    - [Diretrizes e Princípios de Engenharia Adotados](#diretrizes-e-princípios-de-engenharia-adotados)
    - [Critérios de Qualidade e Bloqueios Automatizados (Quality Gates)](#critérios-de-qualidade-e-bloqueios-automatizados-quality-gates)
    - [Métricas e Indicadores de Qualidade](#métricas-e-indicadores-de-qualidade)
    - [Avaliação do Processo e Tratamento de Não Conformidades](#avaliação-do-processo-e-tratamento-de-não-conformidades)
    - [Melhoria Contínua](#melhoria-contínua)
  - [3.6 Estratégia de Gestão do Conhecimento](#36-estratégia-de-gestão-do-conhecimento)
    - [Objetivos](#objetivos)
    - [Ativos de Conhecimento](#ativos-de-conhecimento)
    - [Mecanismos de Registro e Preservação](#mecanismos-de-registro-e-preservação)
    - [Compartilhamento do Conhecimento](#compartilhamento-do-conhecimento)
    - [Manutenção e Controle](#manutenção-e-controle)
    - [Medição da Eficácia](#medição-da-eficácia)
- [Capítulo 4 – Processos de Gerenciamento Técnico](#capítulo-4--processos-de-gerenciamento-técnico)
  - [4.1 Plano de projeto: escopo, cronograma, recursos e entregas](#41-plano-de-projeto-escopo-cronograma-recursos-e-entregas)
    - [Estrutura Analítica do Projeto (EAP)](#estrutura-analítica-do-projeto-eap)
    - [Escopo e Marcos por Macroentrega](#escopo-e-marcos-por-macroentrega)
    - [Cronograma](#cronograma)
    - [Recursos](#recursos)
    - [Premissas e Restrições](#premissas-e-restrições)
    - [Rotina de Acompanhamento e Tratamento de Desvios](#rotina-de-acompanhamento-e-tratamento-de-desvios)
  - [4.2 Plano de gestão de riscos: identificação, probabilidade, impacto e respostas](#42-plano-de-gestão-de-riscos-identificação-probabilidade-impacto-e-respostas)
    - [Critérios de Classificação](#critérios-de-classificação)
    - [Registro de Riscos](#registro-de-riscos)
  - [4.3 Plano de gestão de configuração: controle de versões, branches e releases](#43-plano-de-gestão-de-configuração-controle-de-versões-branches-e-releases)
    - [Itens de Configuração](#itens-de-configuração)
    - [Estratégia de Branches](#estratégia-de-branches)
    - [Baselines, Versionamento e Releases](#baselines-versionamento-e-releases)
    - [Auditoria e Registro de Status](#auditoria-e-registro-de-status)
  - [4.4 Registro de decisões técnicas relevantes (ADRs)](#44-registro-de-decisões-técnicas-relevantes-adrs)
    - [Processo de Decisão](#processo-de-decisão)
    - [Matriz de Decisão Ponderada: Arquitetura Base (ADR-001)](#matriz-de-decisão-ponderada-arquitetura-base-adr-001)
    - [Índice de Decisões (ADR-001 a ADR-012)](#índice-de-decisões-adr-001-a-adr-012)
  - [4.5 Métricas de acompanhamento do projeto](#45-métricas-de-acompanhamento-do-projeto)
- [Capítulo 5 – Processos Técnicos](#capítulo-5--processos-técnicos)
  - [5.1 Requisitos](#51-requisitos)
    - [5.1.1 Documento de requisitos do sistema](#511-documento-de-requisitos-do-sistema)
    - [5.1.2 Rastreabilidade de requisitos](#512-rastreabilidade-de-requisitos)
    - [5.1.3 Critérios de aceitação (CA-01 a CA-15)](#513-critérios-de-aceitação-ca-01-a-ca-15)
    - [5.1.4 Registro de stakeholders e necessidades elicitadas](#514-registro-de-stakeholders-e-necessidades-elicitadas)
  - [5.2 Arquitetura e Design](#52-arquitetura-e-design)
    - [5.2.1 Documento de arquitetura do sistema](#521-documento-de-arquitetura-do-sistema)
    - [5.2.2 Diagramas de design](#522-diagramas-de-design)
    - [5.2.3 Justificativa das escolhas tecnológicas](#523-justificativa-das-escolhas-tecnológicas)
    - [5.2.4 Estratégia de gestão de mídias e desacoplamento de storage](#524-estratégia-de-gestão-de-mídias-e-desacoplamento-de-storage)
  - [5.3 Implementação e Integração](#53-implementação-e-integração)
    - [5.3.1 Padrões de codificação e engenharia adotados](#531-padrões-de-codificação-e-engenharia-adotados)
    - [5.3.2 Plano de integração entre componentes (CI/CD)](#532-plano-de-integração-entre-componentes-cicd)
    - [5.3.3 Registro de testes unitários e de integração](#533-registro-de-testes-unitários-e-de-integração)
    - [5.3.4 Rastreabilidade entre código e requisitos](#534-rastreabilidade-entre-código-e-requisitos)
  - [5.4 Verificação, Validação e Transição](#54-verificação-validação-e-transição)
    - [5.4.1 Plano de verificação e validação](#541-plano-de-verificação-e-validação)
    - [5.4.2 Critérios de aceitação por stakeholder](#542-critérios-de-aceitação-por-stakeholder)
    - [5.4.3 Relatório de testes de aceitação (Homologação e Produção)](#543-relatório-de-testes-de-aceitação-homologação-e-produção)
    - [5.4.4 Plano de transição/implantação do sistema](#544-plano-de-transiçãoimplantação-do-sistema)
  - [5.5 Operação, Manutenção e Descontinuação](#55-operação-manutenção-e-descontinuação)
    - [5.5.1 Procedimentos de operação e monitoramento](#551-procedimentos-de-operação-e-monitoramento)
    - [5.5.2 Plano de manutenção](#552-plano-de-manutenção)
    - [5.5.3 Estratégia de descontinuação e migração de dados](#553-estratégia-de-descontinuação-e-migração-de-dados)
- [Capítulo 6 – Avaliação e melhoria dos processos de software](#capítulo-6--avaliação-e-melhoria-dos-processos-de-software)
  - [6.1 Referencial e recorte](#61-referencial-e-recorte)
  - [6.2 Diagnóstico do manual](#62-diagnóstico-do-manual)
  - [6.3 Plano de uma melhoria](#63-plano-de-uma-melhoria)
  - [6.4 Atualização e verificação](#64-atualização-e-verificação)
    - [Quadro Comparativo: Antes vs. Depois da Revisão (Seções 4.1, 4.2 e 4.5)](#quadro-comparativo-antes-vs-depois-da-revisão-seções-41-42-e-45)
    - [Reavaliação Pós-Melhoria (Verificação da Eficácia Documental)](#reavaliação-pós-melhoria-verificação-da-eficácia-documental)
  - [6.5 Acompanhamento da execução](#65-acompanhamento-da-execução)
    - [Referências Normativas do Capítulo](#referências-normativas-do-capítulo)
- [Referências](#referências)

