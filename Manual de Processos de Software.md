# Manual de Processos de Software – CineDoom

**Tipo de documento:** documento controlado. Qualquer alteração deve ser registrada no Histórico de Versões e, quando afetar decisões, no registro de alterações do workbook (seção 50).

**Base normativa:** ABNT NBR ISO/IEC/IEEE 12207:2021 (referência local: `ABNT ISO IEC 12207 2021.pdf`).

**Fonte de decisões:** Project Definition Workbook (PDW). Este documento é o produto mais recente das decisões do grupo; em caso de conflito entre este manual e o PDW, prevalece o PDW, e a divergência deve ser explicitamente registrada.

---

**Histórico de Versões**

| Data | Versão | Alteração Realizada |
| :---: | :---: | :---: |
| 10/09/2026 | 1.0 | Criação do documento e elaboração da capa. |
| 16/09/2026 | 1.1 | Elaboração dos itens da Parte 0. |
| 24/09/2026 | 1.2 | Alinhamento das Partes 0, 1 e 2 ao PDW e à ISO/IEC/IEEE 12207. |
| 24/09/2026 | 1.3 | Revisão técnica: correção de contradições, inclusão de terminologia, justificativas de aquisição e índice de aderência à norma. |
| xxx | xx | xxx |

**Sumário**

- Parte 0 – Apresentação do Software
  - 0.1. Identificação e Descrição
  - 0.2. Público-Alvo e Contexto de Uso
  - 0.3. Escopo e Funcionalidades
  - 0.4. Restrições e Premissas
- Parte 1 – Processos de Acordo
  - 1.1. Processo de Aquisição
  - 1.2. Processo de Fornecimento
- Parte 2 – Processos Organizacionais Habilitadores
  - 2.1. Gestão do Modelo de Ciclo de Vida
  - 2.2. Gestão da Infraestrutura
  - 2.3. Gestão de Portfólio e Viabilidade
  - 2.4. Gestão de Recursos Humanos
  - 2.5. Gestão da Qualidade
  - 2.6. Gestão do Conhecimento
- Considerações Finais e Decisões em Aberto

---

## Índice de aderência à ISO/IEC/IEEE 12207

Este item relaciona cada parte do manual ao processo da norma, permitindo acompanhar a evolução do documento ao longo do semestre e dar origem a novas partes sem contradição.

| Parte do manual | Processo da ISO/IEC/IEEE 12207 | Referência |
|---|---|---|
| Parte 0 | Insumo para definição de requisitos e stakeholders | 6.4.2 e 6.4.3 (futuras) |
| Parte 1.1 | Acquisition (Aquisição) | 6.1.1 |
| Parte 1.2 | Supply (Fornecimento) | 6.1.2 |
| Parte 2.1 | Life cycle model management | 6.2.1 |
| Parte 2.2 | Infrastructure management | 6.2.2 |
| Parte 2.3 | Portfolio management | 6.2.3 |
| Parte 2.4 | Human resource management | 6.2.4 |
| Parte 2.5 | Quality management | 6.2.5 |
| Parte 2.6 | Knowledge management | 6.2.6 |
| Partes 3+ (planejadas) | Technical management, Technical processes, Software implementation | 6.3, 6.4 e 7 |

## Terminologia adotada

Para garantir consistência interna (regra de terminologia do PDW, seção 46.3), este manual adota os seguintes termos, que devem ser usados de forma idêntica em todas as partes:

| Termo | Significado |
|---|---|
| Cliente | Organização proprietária de um cinema que contrata o CineDoom (adquirente). |
| Usuário | Funcionário autorizado do cliente que opera o sistema (perfis Administrador, Gerente e Atendente). |
| Espectador | Consumidor final que compra ingresso no cinema. Não acessa o sistema na primeira versão. |
| CineSoft Solutions | Organização fictícia desenvolvedora do CineDoom. |
| Produto | CineDoom: plataforma web SaaS. |
| Fornecedor | Organização que presta infraestrutura ou serviços à CineSoft (ex.: provedor de nuvem, gateway de pagamento). |

---

# Parte 0 – Apresentação do Software

## 0.1. Identificação e Descrição

**Nome do software:** CineDoom.

O CineDoom é um produto de software comercial, na forma de plataforma web de **gerenciamento operacional para cinemas de pequeno e médio porte**. É um sistema administrativo de retaguarda (back-office) fornecido em modelo SaaS: o cliente não instala software, acessando o sistema por navegador web em instância própria na nuvem.

O problema que motiva o produto é a dispersão das informações operacionais de um cinema — filmes, salas, sessões, disponibilidade de assentos, venda de ingressos e clientes — em controles manuais ou sistemas isolados. Essa situação dificulta o acompanhamento da ocupação das salas, provoca retrabalho no controle de assentos e limita a geração de informação para a tomada de decisão.

O CineDoom resolve esse problema ao concentrar essas informações em um único ambiente, com regras de negócio que impedem vendas conflitantes, registro de responsável pelas operações e relatórios de ocupação e vendas. Com isso, o produto entrega três benefícios centrais: centralização das informações, rastreabilidade das operações e apoio à decisão gerencial.

O sistema é desenvolvido e mantido pela organização fictícia **CineSoft Solutions** e é tratado neste manual como um produto real, servindo de estudo de caso para aplicação dos processos da ISO/IEC/IEEE 12207.

O posicionamento do CineDoom é de produto B2B (venda para organizações, e não para o espectador final), com escopo inicial de uma única versão web. Essa posição orienta as decisões de arquitetura (monólito modular, API REST, PostgreSQL) e define limites para requisitos e testes nas partes seguintes do manual.

## 0.2. Público-Alvo e Contexto de Uso

O público-alvo é o **cliente**: organizações que operam cinemas de pequeno e médio porte no mercado nacional (Brasil). A primeira versão do produto é dimensionada para atender um estabelecimento por assinatura; múltiplas organizações compartilhando a mesma instância não fazem parte do escopo inicial.

Os usuários do sistema são funcionários autorizados do cliente, nos perfis definidos no PDW (seção 6):

- **Administrador** – configura o ambiente, gerencia usuários e permissões e consulta a auditoria.
- **Gerente** – gerencia filmes, salas e sessões e consulta relatórios e operações.
- **Atendente** – consulta sessões, realiza vendas e cancelamentos autorizados na bilheteria.

O espectador (cliente final do cinema) não terá acesso direto ao sistema administrativo na primeira versão; eventuais funcionalidades para o público, como venda online, não fazem parte do escopo inicial.

O contexto de uso é corporativo: o sistema é operado em navegadores web modernos, com interface responsiva para desktop, durante o horário de funcionamento do cinema e com conexão estável com a internet. Os usuários devem possuir conhecimentos básicos de informática e receber treinamento inicial fornecido pela CineSoft.

## 0.3. Escopo e Funcionalidades

O escopo cobre as operações administrativas de um cinema, organizadas em módulos que serão desdobrados em requisitos, arquitetura e testes nas partes seguintes deste manual:

- **Filmes** – cadastro e gerenciamento de filmes (gênero, duração, classificação indicativa, sinopse, data de lançamento, trailer e capa). Requisitos: RF-03.
- **Salas** – cadastro e configuração de salas, incluindo identificação, capacidade, configuração de assentos e recursos especiais. Requisitos: RF-04.
- **Sessões** – programação de sessões associadas a filme e sala, com validação de conflitos de horário, consulta de disponibilidade e cancelamento. Requisitos: RF-05 e RF-06.
- **Ingressos** – venda e cancelamento de ingressos, com associação a sessão e assento, registro do usuário responsável, reserva por 20 minutos, reembolso automático e pagamento integrado por gateway externo (Stripe). Requisitos: RF-07 e RF-08.
- **Clientes** – cadastro de clientes (espectadores) e registro de interesse em lançamentos futuros. Requisitos: RF-09 e RF-10.
- **Relatórios** – relatórios operacionais de ocupação, ingressos vendidos, sessões realizadas, filmes exibidos e indicadores básicos. Requisito: RF-11.
- **Usuários e controle de acesso** – autenticação, gerenciamento de usuários, perfis e permissões. Requisitos: RF-01 e RF-02.
- **Auditoria** – registro e consulta das operações relevantes, com identificação do usuário responsável. Requisito: RF-12.

### Requisitos Funcionais Principais

Os requisitos funcionais são identificados por código único, conforme o PDW (seção 9.1):

- RF-01 – Autenticar usuário.
- RF-02 – Gerenciar usuários.
- RF-03 – Cadastrar filme.
- RF-04 – Gerenciar salas.
- RF-05 – Gerenciar sessões.
- RF-06 – Consultar disponibilidade.
- RF-07 – Registrar venda.
- RF-08 – Cancelar ingresso.
- RF-09 – Gerenciar clientes.
- RF-10 – Registrar interesse.
- RF-11 – Gerar relatórios.
- RF-12 – Registrar auditoria.

Nas partes seguintes, cada requisito receberá origem, stakeholder relacionado, prioridade, descrição, pré-condições, pós-condições, critérios de aceite, casos de teste e status, compondo a cadeia de rastreabilidade definida no PDW (seção 38): Necessidade → Stakeholder → Requisito → Arquitetura → Implementação → Teste → Aceite → Release.

## 0.4. Restrições e Premissas

### Restrições

Estão fora do escopo da primeira versão:

- Plataformas de streaming, produção e distribuição de filmes.
- Aplicativos móveis e venda online para o espectador.
- Programa de fidelidade, publicidade e gestão de estoque de alimentos.
- Gestão de folha de pagamento e contabilidade.
- Integração com sistemas governamentais.
- Inteligência artificial.
- Operação offline.
- Múltiplas organizações na mesma instância.
- Processamento financeiro próprio: a CineSoft não manipula diretamente meios de pagamento nem detém certificação financeira; o processamento é delegado ao gateway Stripe, e o sistema registra apenas transações autorizadas pelo gateway.

### Premissas

A primeira versão assume que:

- Os usuários receberam treinamento e possuem conhecimentos básicos de informática.
- Existe conexão estável com a internet nos locais de operação.
- Os dados de filmes, salas, sessões, clientes e ingressos são cadastrados e mantidos por usuários autorizados e atualizados.
- O acesso ao sistema é restrito a usuários autenticados e autorizados.
- As metas iniciais de desempenho (resposta em até 2 s em condições normais), capacidade (até 100 usuários simultâneos por cliente) e disponibilidade (95%) são premissas de dimensionamento que serão confirmadas nos requisitos não funcionais.
- O cliente possui infraestrutura mínima (computadores com navegador moderno) para operação do sistema.

---

# Parte 1 – Processos de Acordo

## 1.1. Processo de Aquisição

### Objetivo e fronteira

O processo de aquisição (ISO/IEC/IEEE 12207 – 6.1.1) identifica, avalia e contrata produtos e serviços externos necessários ao desenvolvimento, implantação, operação e manutenção do CineDoom.

A CineSoft desenvolve internamente o núcleo de valor do produto — a aplicação CineDoom (API, regras de negócio e interface web). São adquiridos externamente apenas serviços de infraestrutura e componentes que não fazem parte da competência central da organização ou cujo desenvolvimento interno não se justifica técnica ou economicamente. Cada aquisição requer justificativa documentada, análise de impacto sobre o ciclo de vida e aprovação gerencial.

### Itens passíveis de aquisição e justificativa

| Item | Fornecedor pretendido | Justificativa |
|---|---|---|
| Computação em nuvem | AWS | Evita investimento de capital em infraestrutura própria, permite elasticidade e reduz responsabilidade de administração física de servidores. |
| Banco de dados gerenciado (PostgreSQL) | AWS RDS (ou equivalente) | Elimina a necessidade de um DBA dedicado em equipe enxuta; fornece backup, replicação e atualizações gerenciadas. |
| Monitoramento | AWS CloudWatch (ou SaaS equivalente) | Observabilidade para sustentar as metas de disponibilidade e operação (seções 2.2 e 2.5). |
| Backup e recuperação | AWS S3 + snapshots | Apoia os objetivos de recuperação (RTO/RPO) definidos no PDW (seção 29). |
| Gateway de pagamento | Stripe | Processamento de pagamentos exige conformidade (PCI-DSS) e operação financeira fora da competência da CineSoft; a integração reduz risco e acelera a entrega. |
| E-mail transacional | Amazon SES ou similar | Cobertura condicionada à decisão sobre notificações automáticas (decisão em aberto, seção 47 do PDW). |
| Consultoria especializada | A definir | Apenas se houver lacuna de competência identificada em área específica (ex.: segurança). |

### Critérios de seleção

Os fornecedores serão avaliados com base nos critérios aprovados no PDW (seção 12.2), com o seguinte entendimento:

- **Custo** – custo total de contratação e operação.
- **Segurança** – conformidade com padrões de segurança e LGPD quando aplicável.
- **Disponibilidade** – compromisso de disponibilidade do serviço (SLA).
- **Escalabilidade** – capacidade de crescer com a demanda.
- **Compatibilidade** – aderência à tecnologia do produto (Node.js, PostgreSQL, REST).
- **Suporte** – qualidade e rapidez do atendimento técnico.
- **Condições contratuais** – clareza e previsibilidade do contrato.
- **Portabilidade** – facilidade de substituição ou migração.
- **Dependência do fornecedor** – risco de aprisionamento tecnológico.

### Etapas do processo

1. Identificação da necessidade e justificativa.
2. Levantamento de alternativas e fornecedores qualificados.
3. Avaliação técnica (critérios acima).
4. Avaliação financeira e de orçamento.
5. Aprovação gerencial.
6. Contratação (contrato formal).
7. Monitoramento e avaliação do fornecedor.

### Avaliação e gestão de fornecedores

O desempenho de cada fornecedor será monitorado por meio de SLA quando aplicável, registro de desempenho (indicadores de disponibilidade, tempo de resposta e cumprimento de prazos), revisão periódica e tratamento formal de incidentes. Fornecedores que descumprirem o acordo serão alvo de ação corretiva e, em caso de reincidência, de plano de substituição. O resultado dessas avaliações deve compor a gestão de informação do projeto (seção 2.6 e futura parte de gestão da informação).

## 1.2. Processo de Fornecimento

### Modelo de fornecimento

O processo de fornecimento (ISO/IEC/IEEE 12207 – 6.1.2) define como o CineDoom é disponibilizado ao cliente. O produto é fornecido como **SaaS**, com assinatura mensal por estabelecimento, instância própria hospedada na nuvem da CineSoft, e com as seguintes responsabilidades:

- **CineSoft:** implanta, opera a infraestrutura, monitora, mantém e presta suporte.
- **Cliente:** opera o sistema no dia a dia (cadastro de filmes, programação de sessões, vendas na bilheteria) e mantém a qualidade dos dados.

O fornecimento é formalizado por contrato que define escopo, preço, prazo, critérios de aceite, responsabilidades das partes, níveis de serviço, condições de suporte, tratamento de mudanças, encerramento do serviço e tratamento dos dados do cliente (LGPD).

### Preparação do fornecimento

Antes de cada contratação, a CineSoft elabora proposta contendo plano de implantação (etapas de desenvolvimento e implantação), responsabilidades, prazos, estimativa de custo e identificação do representante do cliente autorizado a aprovar o aceite.

### Entregáveis

A entrega da primeira versão ao cliente contempla:

- Ambiente de produção configurado e aplicação implantada.
- Banco de dados inicializado e configurado com os dados do estabelecimento (salas, características).
- Código-fonte versionado e registrado (entrega da versão) e relatório de testes.
- Manual do usuário e manual técnico.
- Documento de implantação (configurações, versão, acessos).
- Orientação inicial e treinamento dos usuários do cliente.

### Critérios de aceite

O aceite da primeira versão ocorre mediante:

- Validação das funcionalidades previstas e verificação dos requisitos do escopo contratado.
- Execução da homologação no ambiente do cliente.
- Ausência de defeitos críticos.
- Aprovação formal do representante do cliente.

O aceite é condição para início da operação acompanhada e para a contagem da assinatura.

### Suporte pós-entrega

Após a entrega, a CineSoft mantém os seguintes tipos de manutenção:

- **Corretiva** – correção de defeitos identificados em operação, priorizada por severidade, com teste de regressão e registro da solução.
- **Adaptativa** – adequação a mudanças externas que impactem o funcionamento (atualizações de dependências, mudanças de ambiente ou de requisitos externos).
- **Evolutiva** – novas funcionalidades solicitadas pelo cliente, mediante solicitação formal, análise de impacto e aprovação.
- **Preventiva** – ações proativas de atualização de dependências, refatoração e revisões de segurança e desempenho.

Todos os atendimentos são registrados em sistema de gestão de chamados, com severidade, prioridade e prazos (SLA) definidos na parte de operação deste manual. A responsabilidade pela execução da manutenção é da CineSoft; a responsabilidade pela autorização de mudanças e pela aceitação das correções é do cliente.

---

# Parte 2 – Processos Organizacionais Habilitadores

## 2.1. Gestão do Modelo de Ciclo de Vida

O CineDoom adota o modelo de ciclo de vida **incremental** (ISO/IEC/IEEE 12207 – 6.2.1), conforme decidido no PDW (seção 14.1). A escolha se justifica por três razões: o sistema é decomposto em módulos relativamente independentes; cada incremento entrega funcionalidade executável e potencialmente utilizável; e a validação frequente reduz o risco de divergência entre o produto e as necessidades do cliente, inclusive em um contexto de equipe enxuta e semestre letivo.

O modelo é operado por incrementos, em que cada incremental percorre as etapas de requisito, design, implementação, teste e release, sempre produzindo funcionalidade pronta para uso. Ao final de cada incremento, são executadas atividades de verificação, validação e auditoria de conformidade com este manual.

### Incrementos

- **Incremento 1** – Autenticação, usuários, filmes e salas.
- **Incremento 2** – Sessões, assentos e disponibilidade.
- **Incremento 3** – Venda, cancelamento e auditoria.
- **Incremento 4** – Clientes e interesses.
- **Incremento 5** – Relatórios, refinamentos e preparação para produção.

### Critério de conclusão de incremento

Um incremento é considerado concluído somente quando todos os critérios do PDW (seção 14.3) forem atendidos: requisitos do incremento implementados, verificação concluída, testes executados, defeitos críticos corrigidos, documentação atualizada e revisão de qualidade realizada.

A governança do ciclo de vida é responsabilidade do Gerente de Projeto, que mantém o modelo atualizado e registra ajustes motivados por mudanças de escopo ou de contexto.

## 2.2. Gestão da Infraestrutura

A gestão da infraestrutura (ISO/IEC/IEEE 12207 – 6.2.2) garante recursos tecnológicos adequados aos ambientes de desenvolvimento, testes, homologação e produção.

### Ambientes

- **Desenvolvimento** – máquinas da equipe (VS Code, Git/GitHub), com a aplicação rodando localmente e acesso a dados de desenvolvimento.
- **Testes** – ambiente isolado para execução de testes funcionais, de integração e de regressão.
- **Homologação** – ambiente pré-produção para validação com clientes, controlado e com dados de teste.
- **Produção** – ambiente na nuvem (AWS) com mecanismos de backup, monitoramento, segurança e recuperação de falhas, suportando as metas de disponibilidade do produto.

### Ferramentas

Git e GitHub para versionamento e revisão, GitHub Projects para gestão de tarefas, Visual Studio Code como IDE, ferramenta de modelagem UML para diagramas de arquitetura, GitHub Actions para integração e entrega contínuas, e os serviços AWS contratados (seção 1.1) em produção.

### Separação de dados e segurança

Dados de teste são mantidos separados dos dados de produção; dados reais não são utilizados em ambientes não produtivos. O acesso aos ambientes é controlado por perfil e por menor privilégio, sob responsabilidade do DevOps.

### Inventário

A CineSoft mantém inventário atualizado de hardware, softwares, licenças, ambientes, ferramentas e serviços contratados, compondo a gestão de configuração nas partes seguintes do manual.

## 2.3. Gestão de Portfólio e Viabilidade

O CineDoom é tratado como produto estratégico e comercial do portfólio da CineSoft (ISO/IEC/IEEE 12207 – 6.2.3). A seleção do projeto considerou a viabilidade técnica (aderência às competências atuais da equipe), organizacional (capacidade de entrega incremental) e de negócio (existência de um segmento de pequenos e médios cinemas sem solução integrada).

A viabilidade é reavaliada periodicamente por meio de indicadores de desempenho do produto (faturamento, adesão, custo operacional), oportunidades de melhoria e expansão funcional. Decisões de continuar, expandir ou encerrar o investimento são tomadas segundo a política de decisão do PDW (seção 43), com participação da diretoria e do gerente de projeto.

## 2.4. Gestão de Recursos Humanos

A gestão de recursos humanos (ISO/IEC/IEEE 12207 – 6.2.4) garante que os profissionais possuam as competências necessárias às suas responsabilidades. Os papéis abaixo podem ser exercidos de forma acumulada por um mesmo profissional em função do dimensionamento da equipe; essa condição é registrada explicitamente para evitar que o manual presuma uma organização fictícia maior do que a realidade do estudo de caso.

### Papéis e responsabilidades

- **Gerente de Projeto** – planejamento, acompanhamento, coordenação da equipe e comunicação com stakeholders.
- **Analista de Requisitos** – elicitação, análise, documentação e gerenciamento dos requisitos.
- **Arquiteto de Software** – decisões arquiteturais e definição da estrutura técnica do produto.
- **Desenvolvedor Frontend** – implementação da interface web (React).
- **Desenvolvedor Backend** – implementação da API, regras de negócio e integração com o banco (Node.js, PostgreSQL).
- **Engenheiro de Testes** – elaboração, execução e acompanhamento dos testes.
- **DevOps** – infraestrutura, CI/CD, monitoramento e backup.
- **Analista de Qualidade** – critérios, métricas e metas de qualidade.
- **Suporte** – atendimento a chamados e suporte pós-entrega.

### Matriz RACI

A matriz RACI (responsável, aprovador, consultado, informado) é a aprovada no PDW (seção 17.1), aplicada às principais atividades do ciclo de vida:

| Atividade | GP | AR | AS | DEV | TEST | OPS | QA |
|-----------|----|----|----|-----|------|-----|----|
| Planejamento | A/R | C | C | I | I | C | C |
| Requisitos | A | R | C | I | C | I | C |
| Arquitetura | C | C | R/A | C | C | C | I |
| Implementação | I | I | A | R | C | C | I |
| Testes | I | C | C | C | R/A | I | C |
| Implantação | A | I | C | C | C | R | C |
| Qualidade | A | C | C | C | C | C | R |
| Aceite | A | C | C | I | R | I | C |

Legenda: R = Responsável, A = Aprovador, C = Consulta, I = Informado.

### Capacitação

A organização promove capacitação em Engenharia de Requisitos, Testes de Software, UML, Git e GitHub, Segurança de Aplicações, Qualidade de Software, Padrões Arquiteturais, Ferramentas do Projeto e ISO/IEC/IEEE 12207. O processo de capacitação inclui identificação de lacunas de competência, planejamento, execução, registro de participação e avaliação de necessidades de reciclagem (PDW, seção 18).

## 2.5. Gestão da Qualidade

A gestão da qualidade (ISO/IEC/IEEE 12207 – 6.2.5) assegura que produtos e processos estejam em conformidade com os padrões da organização. A qualidade é responsabilidade compartilhada e incorporada ao desenvolvimento, não sendo avaliada apenas ao final do projeto.

### Critérios de qualidade

O produto deve apresentar conformidade com requisitos, confiabilidade, segurança, usabilidade, manutenibilidade e desempenho (PDW, seção 19.2).

### Métricas e metas

As métricas definidas no PDW (seção 19.3) serão coletadas e analisadas pelo Analista de Qualidade, com reporte ao Gerente de Projeto. As metas aprovadas são: 100% dos requisitos com rastreabilidade; cobertura mínima de 80% de testes nos componentes críticos; zero defeitos críticos no aceite; e 100% dos requisitos críticos validados.

### Mecanismos de acompanhamento

A qualidade é monitorada no encerramento de cada incremento, por meio de auditoria que verifica a aderência aos processos deste manual, identifica não conformidades e propõe ações corretivas. A tratativa de não conformidades e o acompanhamento de ações corretivas são registrados para compor a gestão da informação. A definição da fórmula, fonte, responsável e frequência de cada métrica será detalhada na parte de medição deste manual (seção 36 do PDW).

## 2.6. Gestão do Conhecimento

A gestão do conhecimento (ISO/IEC/IEEE 12207 – 6.2.6) preserva o conhecimento gerado ao longo do ciclo de vida do produto e o disponibiliza para a equipe, inclusive para novos integrantes.

### Fontes e artefatos

São fontes oficiais de conhecimento os requisitos, diagramas UML, decisões arquiteturais (ADRs), casos de teste, planos de projeto, atas de reunião, registros de riscos, registros de mudanças e lições aprendidas. Todos os artefatos são versionados no repositório Git ou armazenados nas ferramentas de colaboração adotadas (GitHub, Wiki do Projeto, Google Drive Corporativo, sistema de gestão de chamados).

### Preservação e compartilhamento

Todo artefato possui identificação, versão, responsável e histórico de alterações. As decisões relevantes são registradas com sua justificativa (ADRs), garantindo rastreabilidade e apoio à manutenção futura. O conhecimento é transferido por meio de onboarding de novos membros, revisões técnicas e reuniões de compartilhamento de lições aprendidas ao final de cada incremento.

---

# Considerações Finais e Decisões em Aberto

As Partes 0, 1 e 2 estabelecem a base de contexto, contratual e organizacional do CineDoom, em conformidade com a ABNT NBR ISO/IEC/IEEE 12207 e com as decisões do PDW. As próximas partes do manual (requisitos, arquitetura, implementação, verificação, validação, implantação, operação, manutenção e gerência técnica) devem derivar destas decisões, respeitando a cadeia de rastreabilidade definida no PDW.

Para que a continuação do manual ocorra sem contradições, as seguintes decisões ainda precisam ser fechadas (PDW, seções 47 e 48):

1. **Congelamento do PDW**: preencher o checklist de congelamento (seção 48) e aprovar oficialmente a base do produto.
2. **Pagamentos**: confirmar formalmente o escopo do Stripe, inclusive o item contraditório da seção 5.2 do PDW (gateway listado como fora do escopo versus decisões 7.4 e 49 que o incluem).
3. **Notificações**: decidir se a primeira versão envia e-mails/notificações automáticas (impacta a aquisição de serviço de e-mail).
4. **Cronograma**: definir datas de início/término, marcos e duração dos incrementos (seção 15 do PDW).
5. **Detalhamento dos requisitos**: descrever cada RF e RNF com origem, prioridade, critérios de aceite e casos de teste.
6. **Operação**: definir SLA de suporte, severidade, escalonamento e horários de atendimento (seção 31 do PDW).
7. **RTO/RPO e continuidade**: aprovar os valores propostos e definir plano de recuperação e testes periódicos.
8. **Medição**: definir fórmula, fonte, responsável e frequência de cada métrica de qualidade.