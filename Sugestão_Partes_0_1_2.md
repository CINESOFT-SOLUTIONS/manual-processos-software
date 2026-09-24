# Manual de Processos de Software – CineDoom
## Partes 0, 1 e 2 (Versão Base)

---

# Parte 0 – Apresentação do Software

## 0.1 Identificação e Descrição

O CineDoom é uma plataforma web de gerenciamento operacional para cinemas de pequeno e médio porte. O sistema tem como objetivo centralizar informações relacionadas a filmes, salas, sessões, ingressos e clientes, fornecendo suporte às atividades administrativas realizadas durante a operação do cinema.

O principal problema abordado pelo sistema é a dispersão de informações operacionais em diferentes controles manuais ou sistemas isolados. Essa situação pode dificultar o acompanhamento da ocupação das salas, a gestão das sessões em exibição, o controle da disponibilidade de assentos e a geração de informações para tomada de decisão.

O CineDoom busca oferecer um ambiente único para gerenciamento das operações do cinema, promovendo maior organização dos dados, rastreabilidade das operações e padronização dos processos administrativos.

O sistema é tratado neste manual como um produto comercial desenvolvido e mantido por uma organização fictícia de software, sendo utilizado como estudo de caso para aplicação dos processos definidos pela ISO/IEC/IEEE 12207.

---

## 0.2 Público-Alvo e Contexto de Uso

O público-alvo do CineDoom é composto por organizações responsáveis pela operação de cinemas, especialmente estabelecimentos de pequeno e médio porte que necessitam controlar suas atividades administrativas de forma integrada.

Os principais usuários do sistema são gerentes de cinema, supervisores operacionais, atendentes de bilheteria e administradores responsáveis pela configuração e manutenção dos dados do ambiente.

O sistema será utilizado em ambiente corporativo por meio de navegadores web modernos conectados à internet. A utilização ocorrerá principalmente durante o horário de funcionamento do cinema, sendo considerada uma ferramenta de apoio às atividades operacionais e administrativas.

Espera-se que os usuários possuam conhecimentos básicos de informática e tenham recebido treinamento inicial para utilização das funcionalidades disponibilizadas pelo sistema.

---

## 0.3 Escopo e Funcionalidades

O escopo do CineDoom contempla funcionalidades relacionadas ao gerenciamento administrativo da operação de um cinema.

### Módulo de Filmes

Permite o cadastro, consulta, atualização e remoção de filmes disponíveis para exibição.

### Módulo de Salas

Permite o gerenciamento das salas de exibição, incluindo capacidade máxima, identificação da sala e configuração dos assentos.

### Módulo de Sessões

Permite a criação, consulta, alteração e cancelamento de sessões associadas aos filmes e salas cadastrados.

### Módulo de Ingressos

Permite o registro da venda e cancelamento de ingressos, bem como o controle da disponibilidade de assentos para cada sessão.

### Módulo de Clientes

Permite o cadastro de clientes e o registro de interesse em futuros lançamentos.

### Módulo de Relatórios

Permite a geração de relatórios operacionais relacionados à ocupação das salas, quantidade de ingressos vendidos, sessões realizadas e indicadores básicos de operação.

### Requisitos Funcionais Principais

- RF-01 – Cadastrar filme.
- RF-02 – Consultar filme.
- RF-03 – Atualizar filme.
- RF-04 – Remover filme.
- RF-05 – Cadastrar sala.
- RF-06 – Gerenciar sessões.
- RF-07 – Vender ingresso.
- RF-08 – Cancelar ingresso.
- RF-09 – Cadastrar cliente.
- RF-10 – Registrar interesse em lançamento.
- RF-11 – Gerar relatórios operacionais.

---

## 0.4 Restrições e Premissas

### Restrições

O escopo atual do projeto não contempla:

- Processamento real de pagamentos.
- Integração com instituições financeiras.
- Aplicativos móveis.
- Integração com plataformas de streaming.
- Integração com sistemas governamentais.
- Inteligência artificial para tomada de decisão.
- Operação offline.
- Múltiplas organizações compartilhando a mesma instância do sistema.

### Premissas

Assume-se que:

- Os usuários receberam treinamento básico.
- Existe conexão estável com a internet.
- Os dados cadastrados são válidos e atualizados.
- A organização possui infraestrutura mínima para operação do sistema.
- O acesso ao sistema é realizado apenas por usuários autorizados.

---

# Parte 1 – Processos de Acordo

## 1.1 Processo de Aquisição

O processo de aquisição tem como objetivo identificar, avaliar e contratar produtos ou serviços externos necessários para o desenvolvimento, implantação, operação e manutenção do CineDoom.

A organização responsável pelo sistema poderá adquirir infraestrutura, ferramentas e serviços especializados sempre que a utilização de recursos externos representar benefícios técnicos, econômicos ou operacionais.

As aquisições poderão incluir serviços de computação em nuvem, hospedagem, banco de dados gerenciado, monitoramento, envio de e-mails, ferramentas de colaboração, licenças de software e serviços de consultoria técnica.

Os fornecedores serão avaliados considerando critérios de custo, desempenho, disponibilidade, segurança, suporte técnico, escalabilidade, compatibilidade tecnológica e aderência aos requisitos do projeto.

O processo de aquisição seguirá as seguintes etapas:

1. Identificação da necessidade.
2. Levantamento de alternativas.
3. Avaliação técnica.
4. Avaliação financeira.
5. Aprovação gerencial.
6. Contratação.
7. Monitoramento do fornecedor.

### Possíveis Fornecedores

- Serviços de nuvem (AWS, Azure ou Google Cloud).
- Serviços de e-mail transacional.
- Ferramentas de monitoramento.
- Ferramentas de gestão de projetos.
- Serviços de backup e recuperação.

Toda aquisição deverá possuir justificativa documentada e análise de impacto sobre o ciclo de vida do sistema.

---

## 1.2 Processo de Fornecimento

O processo de fornecimento estabelece como o CineDoom será disponibilizado ao cliente.

O produto será fornecido no modelo Software as a Service (SaaS), permitindo acesso ao sistema por meio de navegadores web sem necessidade de instalação local pelos usuários finais.

O fornecimento será iniciado após a formalização de contrato contendo escopo, critérios de aceite, responsabilidades das partes, níveis de serviço, condições de suporte e cronograma de implantação.

### Entregáveis

A entrega do sistema deverá contemplar:

- Ambiente de produção configurado.
- Aplicação implantada.
- Banco de dados inicializado.
- Manual do usuário.
- Manual técnico.
- Código-fonte versionado.
- Relatório de testes.
- Registro das configurações de implantação.

### Critérios de Aceite

O aceite do produto será realizado mediante:

- Validação das funcionalidades previstas.
- Execução dos testes de homologação.
- Ausência de defeitos críticos.
- Aprovação formal do cliente.

### Suporte Pós-Entrega

#### Manutenção Corretiva

Correção de defeitos identificados após a implantação.

#### Manutenção Adaptativa

Adequação a mudanças externas que impactem o funcionamento do sistema.

#### Manutenção Evolutiva

Desenvolvimento de novas funcionalidades solicitadas pelo cliente.

Todos os atendimentos deverão ser registrados e acompanhados por meio de ferramenta de gestão de chamados.

---

# Parte 2 – Processos Organizacionais Habilitadores

## 2.1 Gestão do Modelo de Ciclo de Vida

O CineDoom adota um modelo de ciclo de vida incremental.

A escolha desse modelo ocorre devido à possibilidade de dividir o sistema em módulos relativamente independentes, permitindo entregas progressivas, validações frequentes e redução dos riscos associados ao desenvolvimento.

Cada incremento deverá resultar em funcionalidades executáveis e potencialmente entregáveis ao cliente.

### Planejamento dos Incrementos

#### Incremento 1

- Filmes
- Salas

#### Incremento 2

- Sessões

#### Incremento 3

- Ingressos

#### Incremento 4

- Clientes

#### Incremento 5

- Relatórios

Ao final de cada incremento serão realizadas atividades de verificação, validação e revisão de conformidade com os processos definidos neste manual.

---

## 2.2 Gestão da Infraestrutura

A organização deverá manter infraestrutura adequada para execução das atividades de desenvolvimento, testes, implantação e manutenção do sistema.

### Ambiente de Desenvolvimento

- Computadores corporativos.
- Git.
- GitHub.
- Visual Studio Code.
- Ferramentas de modelagem UML.

### Ambiente de Testes

Ambiente isolado utilizado para execução de testes funcionais, integração, homologação e validação.

### Ambiente de Produção

Ambiente hospedado em nuvem com mecanismos de backup, monitoramento, segurança e recuperação de falhas.

### Inventário de Infraestrutura

A organização deverá manter registro atualizado de:

- Hardware.
- Softwares.
- Licenças.
- Ambientes.
- Ferramentas.
- Serviços contratados.

---

## 2.3 Gestão de Portfólio

A organização considera o CineDoom um produto estratégico dentro de seu portfólio de soluções voltadas para automação de processos administrativos.

A seleção do projeto foi realizada considerando viabilidade técnica, potencial de mercado, aderência às competências da equipe e possibilidade de evolução futura.

A gestão de portfólio deverá avaliar periodicamente o desempenho do produto, identificando oportunidades de melhoria, expansão funcional e adequação às necessidades dos clientes.

---

## 2.4 Gestão de Recursos Humanos

A organização deverá garantir que os profissionais envolvidos possuam competências compatíveis com suas responsabilidades.

### Papéis Organizacionais

#### Gerente de Projeto

Responsável pelo planejamento, acompanhamento, coordenação da equipe e comunicação com stakeholders.

#### Analista de Requisitos

Responsável pela elicitação, análise, documentação e gerenciamento dos requisitos.

#### Arquiteto de Software

Responsável pelas decisões arquiteturais e pela definição da estrutura técnica do sistema.

#### Desenvolvedor

Responsável pela implementação das funcionalidades e correção de defeitos.

#### Testador

Responsável pela elaboração, execução e acompanhamento das atividades de teste.

### Matriz RACI

| Atividade | GP | AR | AS | DEV | TEST |
|-----------|----|----|----|-----|------|
| Requisitos | A | R | C | I | I |
| Arquitetura | C | C | R/A | I | I |
| Implementação | I | I | C | R/A | I |
| Testes | I | I | C | C | R/A |
| Entrega | A | I | I | C | C |

Legenda:

- R = Responsible
- A = Accountable
- C = Consulted
- I = Informed

### Plano de Capacitação

A organização manterá ações de capacitação relacionadas a:

- Engenharia de Requisitos.
- Testes de Software.
- UML.
- Git e GitHub.
- Segurança de Aplicações.
- Qualidade de Software.
- ISO/IEC/IEEE 12207.

---

## 2.5 Gestão da Qualidade

A gestão da qualidade tem como objetivo assegurar que os produtos e processos estejam em conformidade com os padrões definidos pela organização.

A qualidade será tratada como responsabilidade compartilhada entre todos os participantes do projeto.

### Critérios de Qualidade

O produto deverá apresentar:

- Conformidade com requisitos.
- Confiabilidade.
- Manutenibilidade.
- Usabilidade.
- Consistência dos dados.

### Métricas

Serão monitorados os seguintes indicadores:

- Percentual de requisitos rastreados.
- Cobertura de testes.
- Quantidade de defeitos encontrados.
- Quantidade de defeitos corrigidos.
- Taxa de aprovação dos testes.
- Tempo médio de resolução de defeitos.

### Metas

- 100% dos requisitos rastreados.
- Cobertura mínima de testes de 80%.
- Zero defeitos críticos em produção.
- Aprovação formal na homologação.

### Auditorias

Ao final de cada incremento será realizada revisão para verificar a aderência aos processos descritos neste manual.

---

## 2.6 Gestão do Conhecimento

A organização deverá preservar o conhecimento gerado ao longo do ciclo de vida do produto.

Todas as informações relevantes deverão ser registradas, armazenadas e compartilhadas de forma controlada.

### Artefatos Mantidos

- Requisitos.
- Diagramas UML.
- Casos de teste.
- Relatórios.
- Atas de reunião.
- Planos de projeto.
- Decisões arquiteturais.
- Registros de riscos.
- Lições aprendidas.

### Ferramentas

- GitHub.
- Wiki do Projeto.
- Google Drive Corporativo.
- Sistema de Gestão de Chamados.

### Estratégia de Preservação

Todo artefato deverá possuir identificação, versão, responsável e histórico de alterações.

As decisões relevantes deverão ser registradas juntamente com suas justificativas, garantindo rastreabilidade e apoio à manutenção futura do sistema.

---

## Considerações Finais

As Partes 0, 1 e 2 estabelecem a base organizacional e operacional para o ciclo de vida do CineDoom. As seções posteriores do manual deverão utilizar as definições aqui estabelecidas como referência para os processos técnicos, de gerenciamento e de suporte previstos pela ISO/IEC/IEEE 12207.
