# Project Definition Workbook - CineDoom
### Decisões para o Manual de Processos de Software

**Versão:** 1.0  
**Status:** Documento-base para decisão do grupo  
**Produto:** CineDoom  
**Objetivo:** estabelecer uma fonte única de verdade para o estudo de caso e impedir contradições entre as partes do manual durante a aplicação da ISO/IEC/IEEE 12207.

---

## Sumário

- [1. IDENTIDADE E CONTEXTO DO PRODUTO](#1-identidade-e-contexto-do-produto)
  - [1.1 Identidade do software](#11-identidade-do-software)
- [2. ORGANIZAÇÃO FICTÍCIA](#2-organização-fictícia)
  - [2.1 Organização responsável](#21-organização-responsável)
- [3. CLIENTE, MERCADO E STAKEHOLDERS](#3-cliente-mercado-e-stakeholders)
  - [3.1 Segmento de mercado](#31-segmento-de-mercado)
  - [3.2 Stakeholders](#32-stakeholders)
- [4. MODELO DE NEGÓCIO E FORNECIMENTO](#4-modelo-de-negócio-e-fornecimento)
  - [4.1 Modelo de comercialização](#41-modelo-de-comercialização)
- [5. FRONTEIRA DO SISTEMA](#5-fronteira-do-sistema)
  - [5.1 O que está dentro do CineDoom?](#51-o-que-está-dentro-do-cinedoom)
  - [5.2 O que fica fora do CineDoom?](#52-o-que-fica-fora-do-cinedoom)
- [6. USUÁRIOS E CONTROLE DE ACESSO](#6-usuários-e-controle-de-acesso)
  - [6.1 Perfis](#61-perfis)
- [7. ESCOPO FUNCIONAL DETALHADO](#7-escopo-funcional-detalhado)
  - [7.1 Filmes](#71-filmes)
  - [7.2 Salas](#72-salas)
  - [7.3 Sessões](#73-sessões)
  - [7.4 Ingressos](#74-ingressos)
  - [7.5 Clientes](#75-clientes)
  - [7.6 Relatórios](#76-relatórios)
- [8. REGRAS DE NEGÓCIO](#8-regras-de-negócio)
  - [8.1 Sessões](#81-sessões)
  - [8.2 Assentos](#82-assentos)
  - [8.3 Ingressos](#83-ingressos)
  - [8.4 Dados](#84-dados)
- [9. REQUISITOS](#9-requisitos)
  - [9.1 Requisitos funcionais](#91-requisitos-funcionais)
  - [9.2 Requisitos não funcionais](#92-requisitos-não-funcionais)
- [10. ARQUITETURA](#10-arquitetura)
  - [10.1 Estilo arquitetural](#101-estilo-arquitetural)
  - [10.2 Camadas](#102-camadas)
  - [10.3 Frontend](#103-frontend)
  - [10.4 Backend](#104-backend)
  - [10.5 Banco de dados](#105-banco-de-dados)
  - [10.6 API](#106-api)
  - [10.7 Comunicação](#107-comunicação)
- [11. INFRAESTRUTURA E NUVEM](#11-infraestrutura-e-nuvem)
  - [11.1 Provedor](#111-provedor)
  - [11.2 Componentes](#112-componentes)
  - [11.3 Ambientes](#113-ambientes)
  - [11.4 Separação de dados](#114-separação-de-dados)
- [12. AQUISIÇÃO](#12-aquisição)
  - [12.1 O que será adquirido?](#121-o-que-será-adquirido)
  - [12.2 Critérios de seleção](#122-critérios-de-seleção)
  - [12.3 Gestão do fornecedor](#123-gestão-do-fornecedor)
- [13. FORNECIMENTO](#13-fornecimento)
  - [13.1 Modelo](#131-modelo)
  - [13.2 Entregáveis](#132-entregáveis)
  - [13.3 Aceite](#133-aceite)
  - [13.4 Pós-entrega](#134-pós-entrega)
- [14. CICLO DE VIDA](#14-ciclo-de-vida)
  - [14.1 Modelo](#141-modelo)
  - [14.2 Incrementos](#142-incrementos)
  - [14.3 Critério de conclusão de incremento](#143-critério-de-conclusão-de-incremento)
- [15. PLANEJAMENTO DO PROJETO](#15-planejamento-do-projeto)
  - [15.1 Cronograma](#151-cronograma)
  - [15.2 Recursos](#152-recursos)
  - [15.3 Restrições](#153-restrições)
- [16. RECURSOS HUMANOS](#16-recursos-humanos)
  - [16.1 Papéis](#161-papéis)
  - [16.2 Competências](#162-competências)
- [17. RACI](#17-raci)
  - [17.1 Atividades](#171-atividades)
- [18. CAPACITAÇÃO](#18-capacitação)
  - [18.1 Treinamentos obrigatórios](#181-treinamentos-obrigatórios)
  - [18.2 Processo](#182-processo)
- [19. QUALIDADE](#19-qualidade)
  - [19.1 Política](#191-política)
  - [19.2 Critérios](#192-critérios)
  - [19.3 Métricas](#193-métricas)
  - [19.4 Metas sugeridas](#194-metas-sugeridas)
- [20. VERIFICAÇÃO E VALIDAÇÃO](#20-verificação-e-validação)
  - [20.1 Verificação](#201-verificação)
  - [20.2 Validação](#202-validação)
- [21. CONFIGURAÇÃO](#21-configuração)
  - [21.1 Itens de configuração](#211-itens-de-configuração)
  - [21.2 Versionamento](#212-versionamento)
  - [21.3 Mudanças](#213-mudanças)
- [22. GESTÃO DE MUDANÇAS](#22-gestão-de-mudanças)
  - [22.1 Origem de mudanças](#221-origem-de-mudanças)
  - [22.2 Processo](#222-processo)
- [23. RISCOS](#23-riscos)
  - [23.1 Riscos técnicos](#231-riscos-técnicos)
  - [23.2 Riscos organizacionais](#232-riscos-organizacionais)
  - [23.3 Riscos de negócio](#233-riscos-de-negócio)
  - [23.4 Para cada risco registrar](#234-para-cada-risco-registrar)
- [24. GESTÃO DE INFORMAÇÃO](#24-gestão-de-informação)
  - [24.1 Documentos controlados](#241-documentos-controlados)
  - [24.2 Regras](#242-regras)
- [25. GESTÃO DO CONHECIMENTO](#25-gestão-do-conhecimento)
  - [25.1 Fontes](#251-fontes)
  - [25.2 Preservação](#252-preservação)
  - [25.3 Transferência](#253-transferência)
- [26. DECISÕES ARQUITETURAIS](#26-decisões-arquiteturais)
  - [26.1 ADR](#261-adr)
  - [26.2 Exemplos de ADRs esperados](#262-exemplos-de-adrs-esperados)
- [27. IMPLANTAÇÃO](#27-implantação)
  - [27.1 Estratégia](#271-estratégia)
  - [27.2 Rollback](#272-rollback)
- [28. OPERAÇÃO](#28-operação)
  - [28.1 Responsabilidades](#281-responsabilidades)
  - [28.2 Monitoramento](#282-monitoramento)
  - [28.3 Incidentes](#283-incidentes)
- [29. BACKUP E RECUPERAÇÃO](#29-backup-e-recuperação)
  - [29.1 Backup](#291-backup)
  - [29.2 Recuperação](#292-recuperação)
- [30. MANUTENÇÃO](#30-manutenção)
  - [30.1 Corretiva](#301-corretiva)
  - [30.2 Adaptativa](#302-adaptativa)
  - [30.3 Evolutiva](#303-evolutiva)
  - [30.4 Preventiva](#304-preventiva)
- [31. SUPORTE E SLA](#31-suporte-e-sla)
  - [31.1 Canais](#311-canais)
  - [31.2 Severidade](#312-severidade)
  - [31.3 SLA](#313-sla)
- [32. CONTINUIDADE DO NEGÓCIO](#32-continuidade-do-negócio)
  - [32.1 Cenários](#321-cenários)
  - [32.2 Plano de continuidade](#322-plano-de-continuidade)
- [33. AUDITORIA E CONFORMIDADE](#33-auditoria-e-conformidade)
  - [33.1 Auditorias internas](#331-auditorias-internas)
  - [33.2 Objetivos](#332-objetivos)
  - [33.3 Frequência](#333-frequência)
  - [33.4 Normas e referências](#334-normas-e-referências)
- [34. DADOS PESSOAIS E PRIVACIDADE](#34-dados-pessoais-e-privacidade)
  - [34.1 Dados pessoais](#341-dados-pessoais)
  - [34.2 Princípios](#342-princípios)
- [35. TESTES](#35-testes)
  - [35.1 Níveis](#351-níveis)
  - [35.2 Tipos](#352-tipos)
  - [35.3 Artefatos](#353-artefatos)
- [36. MEDIÇÃO](#36-medição)
  - [36.1 Projeto](#361-projeto)
  - [36.2 Produto](#362-produto)
  - [36.3 Processo](#363-processo)
  - [36.4 Regra](#364-regra)
- [37. GESTÃO DE CONFIGURAÇÃO](#37-gestão-de-configuração)
  - [37.1 Itens de configuração](#371-itens-de-configuração)
  - [37.2 Baselines](#372-baselines)
  - [37.3 Releases](#373-releases)
- [38. RASTREABILIDADE](#38-rastreabilidade)
  - [38.1 Cadeia mínima](#381-cadeia-mínima)
  - [38.2 Cobertura](#382-cobertura)
- [39. GESTÃO DE DEFEITOS](#39-gestão-de-defeitos)
  - [39.1 Registro](#391-registro)
  - [39.2 Estados](#392-estados)
- [40. GESTÃO DE PORTFÓLIO](#40-gestão-de-portfólio)
  - [40.1 Posição do CineDoom](#401-posição-do-cinedoom)
  - [40.2 Decisões de portfólio](#402-decisões-de-portfólio)
- [41. GESTÃO DE FORNECEDORES E PARCEIROS](#41-gestão-de-fornecedores-e-parceiros)
  - [41.1 Parceiros potenciais](#411-parceiros-potenciais)
  - [41.2 Avaliação periódica](#412-avaliação-periódica)
- [42. ENCERRAMENTO DO PRODUTO](#42-encerramento-do-produto)
  - [42.1 Descontinuação](#421-descontinuação)
  - [42.2 Portabilidade](#422-portabilidade)
- [43. POLÍTICA DE DECISÃO E GOVERNANÇA](#43-política-de-decisão-e-governança)
  - [43.1 Quem decide?](#431-quem-decide)
- [44. ARTEFATOS DO MANUAL](#44-artefatos-do-manual)
  - [44.1 Artefatos esperados ao longo do ciclo de vida](#441-artefatos-esperados-ao-longo-do-ciclo-de-vida)
- [45. MATRIZ DE RELAÇÃO ENTRE DECISÕES E FUTURAS PARTES DO MANUAL](#45-matriz-de-relação-entre-decisões-e-futuras-partes-do-manual)
- [46. REGRAS DE CONSISTÊNCIA DO MANUAL](#46-regras-de-consistência-do-manual)
  - [46.1 Regra de escopo](#461-regra-de-escopo)
  - [46.2 Regra tecnológica](#462-regra-tecnológica)
  - [46.3 Regra de terminologia](#463-regra-de-terminologia)
  - [46.4 Regra de rastreabilidade](#464-regra-de-rastreabilidade)
  - [46.5 Regra de mudança](#465-regra-de-mudança)
- [47. DECISÕES QUE AINDA PRECISAM SER FECHADAS](#47-decisões-que-ainda-precisam-ser-fechadas)
- [48. CHECKLIST DE CONGELAMENTO](#48-checklist-de-congelamento)
- [49. BASE RECOMENDADA DO CineDoom APÓS O CONGELAMENTO](#49-base-recomendada-do-cinedoom-após-o-congelamento)
- [50. REGISTRO DE ALTERAÇÕES DE DECISÕES](#50-registro-de-alterações-de-decisões)

---

## Como utilizar este documento

Este workbook deve ser preenchido **antes da expansão do manual para os demais processos da ISO**. Ele não substitui o manual; ele funciona como sua base de decisão.

A regra principal é simples:

> **Se uma decisão for aprovada neste documento, as seções posteriores do manual devem respeitá-la.**

Quando uma decisão precisar mudar, o grupo deverá registrar:

1. a decisão anterior;
2. a nova decisão;
3. o motivo da mudança;
4. quais artefatos do manual serão afetados;
5. quais requisitos, testes, riscos, contratos ou processos precisam ser atualizados.

### Legenda

- `[ ]` Decisão ainda não tomada.
- `[x]` Sugestão recomendada para o CineDoom.
- `[~]` Decisão em análise.
- `[N/A]` Item considerado não aplicável, com justificativa registrada.

As marcações `[x]` são **recomendações de projeto**, não exigências da ISO. O grupo deve aprová-las ou substituí-las conscientemente.

---

# 1. IDENTIDADE E CONTEXTO DO PRODUTO

## 1.1 Identidade do software

### 1.1 Nome

- [x] **CineDoom**
- [ ] Outro: ______________________________

### 1.2 Tipo de produto

- [x] Plataforma de gestão operacional para cinemas.
- [ ] Sistema exclusivamente de venda de ingressos.
- [ ] ERP completo para cinemas.
- [ ] Marketplace de cinemas.
- [ ] Outro: ______________________________

### 1.3 Descrição oficial curta

**Sugestão para congelamento:**

> O CineDoom é uma plataforma web de gerenciamento operacional para cinemas de pequeno e médio porte, destinada a centralizar o cadastro de filmes, salas, sessões, assentos, ingressos e clientes, apoiando as atividades administrativas e operacionais do estabelecimento.

- [x] Aprovar a descrição.
- [ ] Alterar a descrição: ______________________________

### 1.4 Problema principal

- [x] Informações operacionais descentralizadas.
- [x] Dependência de controles manuais.
- [x] Dificuldade de acompanhar ocupação e sessões.
- [x] Falta de rastreabilidade das operações.
- [ ] Outro: ______________________________

### 1.5 Benefício principal

- [x] Centralização das informações.
- [x] Maior rastreabilidade.
- [x] Redução de erros operacionais.
- [x] Apoio à tomada de decisão.
- [ ] Outro: ______________________________

---

# 2. ORGANIZAÇÃO FICTÍCIA

## 2.1 Organização responsável

### 2.1 Existe uma empresa fictícia?

- [x] Sim.
- [ ] Não.

### 2.2 Nome

- [x] **CineSoft Solutions**
- [ ] Outro: ______________________________

### 2.3 A empresa desenvolve apenas o CineDoom?

- [x] Não; o CineDoom é um produto do portfólio.
- [ ] Sim.

### 2.4 Missão

- [ ] Definir.
- [x] Sugestão:

> Desenvolver soluções de software que apoiem a digitalização e a eficiência operacional de empresas do setor de entretenimento.

### 2.5 Visão

- [ ] Definir.
- [x] Sugestão:

> Tornar-se uma referência nacional em soluções de gestão para operações de entretenimento.

### 2.6 Objetivos estratégicos

- [x] Criar produto comercializável.
- [x] Desenvolver solução escalável.
- [x] Manter qualidade e confiabilidade.
- [x] Criar capacidade de manutenção e evolução.
- [ ] Outro: ______________________________

---

# 3. CLIENTE, MERCADO E STAKEHOLDERS

## 3.1 Segmento de mercado

### 3.1 Público-alvo empresarial

- [x] Cinemas de pequeno porte.
- [x] Cinemas de médio porte.
- [ ] Grandes redes nacionais.
- [ ] Grandes redes internacionais.
- [ ] Cinemas universitários.
- [ ] Cinemas comunitários.
- [ ] Outro: ______________________________

### 3.2 Região inicial de atuação

- [ ] Local.
- [x] Nacional.
- [ ] Internacional.

### 3.3 Perfil do cliente

- [x] Organização que precisa controlar sessões e ingressos.
- [x] Organização sem sistema operacional integrado.
- [x] Organização que prefere solução hospedada.
- [ ] Outro: ______________________________

---

## 3.2 Stakeholders

### 4.1 Stakeholders externos

- [x] Proprietário do cinema.
- [x] Gerente do cinema.
- [x] Funcionários da bilheteria.
- [x] Usuários administrativos.
- [x] Fornecedores de infraestrutura.
- [x] Empresa desenvolvedora.
- [ ] Cliente final do cinema como usuário direto.
- [ ] Órgãos reguladores.
- [ ] Parceiros comerciais.

### 4.2 Stakeholders internos da CineSoft

- [x] Diretoria.
- [x] Gerente de projeto.
- [x] Analista de requisitos.
- [x] Arquiteto.
- [x] Desenvolvedores.
- [x] Testadores.
- [x] DevOps/infraestrutura.
- [x] Suporte.
- [x] Responsável pela qualidade.

### 4.3 Stakeholder com autoridade sobre aceite

- [x] Representante formal do cliente.
- [ ] Gerente do projeto.
- [ ] Usuário final.
- [ ] Outro: ______________________________

### 4.4 Matriz de influência

Para cada stakeholder, decidir:

| Stakeholder | Interesse | Influência | Responsabilidade |
|---|---|---|---|
| Proprietário | Alta | Alta | Aprovação estratégica |
| CineSoft | Alta | Alta | Desenvolvimento e manutenção |


- [x] Validar matriz.
- [ ] Alterar: ______________________________

---

# 4. MODELO DE NEGÓCIO E FORNECIMENTO

## 4.1 Modelo de comercialização

### 5.1 Forma de fornecimento

- [x] Software as a Service (SaaS).
- [ ] Licença perpétua.
- [ ] Instalação local.
- [ ] Híbrido.

### 5.2 Forma de cobrança

- [x] Assinatura mensal por estabelecimento.
- [ ] Assinatura anual.
- [ ] Por usuário.
- [ ] Por transação.
- [ ] Outro: ______________________________

### 5.3 Existe período de avaliação?

- [ ] Sim.
- [x] Não na primeira versão.
- [ ] A definir.

### 5.4 Existe contrato?

- [x] Sim.
- [ ] Não.

### 5.5 O contrato define

- [x] Escopo.
- [x] Preço.
- [x] Prazo.
- [x] Critérios de aceite.
- [x] Responsabilidades.
- [x] Suporte.
- [x] Níveis de serviço.
- [x] Tratamento de mudanças.
- [x] Encerramento do serviço.
- [x] Tratamento dos dados do cliente.

---

# 5. FRONTEIRA DO SISTEMA

## 5.1 O que está dentro do CineDoom?

- [x] Cadastro de filmes.
- [x] Cadastro de salas.
- [x] Configuração de assentos.
- [x] Gerenciamento de sessões.
- [x] Controle de disponibilidade.
- [x] Venda de ingressos.
- [x] Cancelamento de ingressos.
- [x] Cadastro de clientes.
- [x] Registro de interesse em lançamentos.
- [x] Relatórios operacionais.
- [x] Controle de usuários.
- [x] Controle de perfis.
- [x] Auditoria das operações relevantes.

## 5.2 O que fica fora do CineDoom?

- [x] Streaming.
- [x] Produção de filmes.
- [x] Distribuição cinematográfica.
- [x] Processamento financeiro próprio.
- [x] Gateway de pagamento na primeira versão.
- [x] Aplicativo móvel.
- [x] Programa de fidelidade.
- [x] Publicidade.
- [x] Gestão de estoque de alimentos.
- [x] Gestão de folha de pagamento.
- [x] Contabilidade.
- [x] Integração governamental.
- [x] Inteligência artificial na primeira versão.

### 7.1 Regra de expansão

Novas funcionalidades fora do escopo não deverão ser adicionadas diretamente ao produto. Deverão passar por análise de mudança, avaliação de impacto, priorização e atualização dos requisitos e artefatos afetados.

- [x] Aprovar regra.

---

# 6. USUÁRIOS E CONTROLE DE ACESSO

## 6.1 Perfis

### Administrador

- [x] Gerencia usuários.
- [x] Gerencia permissões.
- [x] Configura o sistema.
- [x] Consulta auditoria.

### Gerente

- [x] Gerencia filmes.
- [x] Gerencia salas.
- [x] Gerencia sessões.
- [x] Consulta relatórios.
- [x] Consulta operações.

### Atendente

- [x] Consulta sessões.
- [x] Realiza vendas.
- [x] Realiza cancelamentos autorizados.
- [ ] Gerencia configurações.

### 8.1 Cliente final

- [x] Não terá acesso direto ao sistema administrativo na primeira versão.

---

# 7. ESCOPO FUNCIONAL DETALHADO

## 7.1 Filmes

Decidir:

- [x] Cadastro.
- [x] Consulta.
- [x] Alteração.
- [x] Inativação.
- [x] Gênero.
- [x] Duração.
- [x] Classificação indicativa.
- [x] Sinopse.
- [x] Data de lançamento.
- [x] Upload de trailer.
- [x] Capa do Filme.

## 7.2 Salas

- [x] Cadastro.
- [x] Identificação.
- [x] Capacidade.
- [x] Configuração de assentos.
- [x] Status da sala.
- [x] Recursos especiais.

## 7.3 Sessões

- [x] Associar filme.
- [x] Associar sala.
- [x] Definir data.
- [x] Definir horário.
- [x] Consultar disponibilidade.
- [x] Cancelar sessão.


## 7.4 Ingressos

- [x] Venda.
- [x] Cancelamento.
- [x] Associação com sessão.
- [x] Associação com assento.
- [x] Registro de usuário responsável.
- [x] Reserva nos primeiros 20 minutos.
- [x] Reembolso financeiro automático.
- [x] Pagamento integrado.

## 7.5 Clientes

- [x] Cadastro.
- [x] Atualização.
- [x] Consulta.
- [x] Registro de interesse.

## 7.6 Relatórios

- [x] Ocupação.
- [x] Ingressos vendidos.
- [x] Sessões realizadas.
- [x] Filmes exibidos.
- [x] Indicadores operacionais.

---

# 8. REGRAS DE NEGÓCIO

## 8.1 Sessões

- [x] Uma sessão deve estar associada a um filme.
- [x] Uma sessão deve estar associada a uma sala.
- [x] Não deve haver duas sessões conflitantes na mesma sala.
- [x] Uma sessão cancelada não pode receber novas vendas.
- [ ] Definir antecedência mínima para criação de sessão.
- [ ] Definir antecedência mínima para cancelamento.

## 8.2 Assentos

- [x] Cada assento pertence a uma sala.
- [x] Um assento não pode ser vendido duas vezes para a mesma sessão.
- [x] Assentos indisponíveis não podem ser selecionados.
- [ ] Definir estados adicionais do assento.

## 8.3 Ingressos

- [x] Cada ingresso pertence a uma sessão.
- [x] Cada ingresso possui assento.
- [x] Cancelamento deve ser registrado.
- [x] Operações relevantes devem possuir usuário responsável.

## 8.4 Dados

- [x] Identificadores únicos.
- [x] Validação de campos obrigatórios.
- [x] Integridade referencial.
- [x] Registro de data e hora para operações relevantes.

---

# 9. REQUISITOS

## 9.1 Requisitos funcionais

Os requisitos deverão ser identificados por código único.

Sugestão:

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

### Para cada RF decidir

- [ ] Origem.
- [ ] Stakeholder relacionado.
- [ ] Prioridade.
- [ ] Descrição.
- [ ] Pré-condições.
- [ ] Pós-condições.
- [ ] Critérios de aceite.
- [ ] Casos de teste.
- [ ] Status.

---

## 9.2 Requisitos não funcionais

### Desempenho

- [ ] Tempo máximo de resposta.
- [ ] Usuários simultâneos.
- [ ] Volume de dados.
- [ ] Volume de transações.

### Sugestão

- [x] Operações comuns devem responder em até 2 segundos em condições normais.
- [x] A primeira versão será dimensionada para até 100 usuários simultâneos por cliente.

### Disponibilidade

- [x] Meta inicial de 95%.
- [ ] Definir janela de medição.
- [ ] Definir exclusões da métrica.

### Segurança

- [x] HTTPS.
- [x] Senhas armazenadas com hash seguro.
- [x] Controle de acesso por perfil.
- [x] Registro de eventos relevantes.
- [x] Sessões autenticadas.
- [ ] MFA na primeira versão.

### Usabilidade

- [x] Interface web responsiva para desktop.
- [x] Mensagens claras de erro.
- [x] Fluxos operacionais consistentes.

### Manutenibilidade

- [x] Código versionado.
- [x] Padrões de codificação.
- [x] Revisão de código.
- [x] Testes automatizados para componentes relevantes.
- [x] Documentação técnica.

---

# 10. ARQUITETURA

## 10.1 Estilo arquitetural

- [x] Monólito modular.
- [ ] Microsserviços.
- [ ] Serverless.
- [ ] Outro.

### Justificativa recomendada

O monólito modular reduz a complexidade operacional da primeira versão e permite separar responsabilidades internamente sem introduzir a sobrecarga de uma arquitetura distribuída. A solução poderá evoluir futuramente caso requisitos de escala ou independência de implantação justifiquem a decomposição de módulos.

---

## 10.2 Camadas

- [x] Controller.
- [x] Service.
- [x] Repository.
- [x] Model.

## 10.3 Frontend

- [x] React.
- [ ] Angular.
- [ ] Vue.

## 10.4 Backend

- [ ] Spring Boot.
- [ ] .NET.
- [x] Node.js.
- [ ] Outro.

## 10.5 Banco de dados

- [x] PostgreSQL.
- [ ] MySQL.
- [ ] SQL Server.
- [ ] Outro.

## 10.6 API

- [x] REST.
- [ ] GraphQL.
- [ ] Outro.

## 10.7 Comunicação

- [x] HTTPS.
- [x] JSON.
- [x] API REST versionada.

---

# 11. INFRAESTRUTURA E NUVEM

## 11.1 Provedor

- [x] AWS.
- [ ] Azure.
- [ ] Google Cloud.

## 11.2 Componentes

- [x] Computação.
- [x] Banco de dados.
- [x] Armazenamento de backup.
- [x] Monitoramento.
- [x] Logs.
- [x] Controle de acesso.

## 11.3 Ambientes

- [x] Desenvolvimento.
- [x] Testes.
- [x] Homologação.
- [x] Produção.

## 11.4 Separação de dados

- [x] Dados de teste separados dos dados de produção.
- [x] Dados reais não devem ser utilizados diretamente em testes.

---

# 12. AQUISIÇÃO

## 12.1 O que será adquirido?

- [x] Infraestrutura cloud.
- [x] Banco gerenciado ou infraestrutura equivalente.
- [x] Monitoramento.
- [x] Backup.
- [ ] Serviço de e-mail, caso notificações sejam incluídas.
- [ ] Consultoria especializada, caso necessária.

## 12.2 Critérios de seleção

- [x] Custo.
- [x] Segurança.
- [x] Disponibilidade.
- [x] Escalabilidade.
- [x] Compatibilidade.
- [x] Suporte.
- [x] Condições contratuais.
- [x] Portabilidade.
- [x] Dependência do fornecedor.

## 12.3 Gestão do fornecedor

- [x] Contrato.
- [x] SLA quando aplicável.
- [x] Registro de desempenho.
- [x] Revisão periódica.
- [x] Tratamento de incidentes.

---

# 13. FORNECIMENTO

## 13.1 Modelo

- [x] SaaS.
- [x] Implantação realizada pela CineSoft.
- [x] Operação realizada pelo cliente.
- [x] Manutenção realizada pela CineSoft.

## 13.2 Entregáveis

- [x] Aplicação.
- [x] Ambiente configurado.
- [x] Documentação.
- [x] Manual do usuário.
- [x] Manual técnico.
- [x] Relatório de testes.
- [x] Registro de versão.
- [x] Orientação inicial aos usuários.

## 13.3 Aceite

- [x] Testes de homologação.
- [x] Verificação dos requisitos.
- [x] Ausência de defeitos críticos.
- [x] Aprovação formal do representante do cliente.

## 13.4 Pós-entrega

- [x] Suporte.
- [x] Correção de defeitos.
- [x] Monitoramento.
- [x] Atualizações.
- [x] Manutenção.

---

# 14. CICLO DE VIDA

## 14.1 Modelo

- [x] Incremental.

## 14.2 Incrementos

### Incremento 1

- [x] Autenticação.
- [x] Usuários.
- [x] Filmes.
- [x] Salas.

### Incremento 2

- [x] Sessões.
- [x] Assentos.
- [x] Disponibilidade.

### Incremento 3

- [x] Venda.
- [x] Cancelamento.
- [x] Auditoria.

### Incremento 4

- [x] Clientes.
- [x] Interesses.

### Incremento 5

- [x] Relatórios.
- [x] Refinamentos.
- [x] Preparação para produção.

## 14.3 Critério de conclusão de incremento

- [x] Requisitos do incremento implementados.
- [x] Verificação concluída.
- [x] Testes executados.
- [x] Defeitos críticos corrigidos.
- [x] Documentação atualizada.
- [x] Revisão de qualidade realizada.

---

# 15. PLANEJAMENTO DO PROJETO

## 15.1 Cronograma

Definir:

- [ ] Data de início.
- [ ] Data de término.
- [ ] Marcos.
- [ ] Duração dos incrementos.
- [ ] Dependências.

## 15.2 Recursos

- [ ] Horas de equipe.
- [ ] Infraestrutura.
- [ ] Licenças.
- [ ] Serviços externos.
- [ ] Orçamento.

## 15.3 Restrições

- [x] Prazo.
- [x] Capacidade da equipe.
- [x] Orçamento controlado.
- [x] Escopo inicial limitado.

---

# 16. RECURSOS HUMANOS

## 16.1 Papéis

- [x] Gerente de Projeto.
- [x] Analista de Requisitos.
- [x] Arquiteto de Software.
- [x] Desenvolvedor Frontend.
- [x] Desenvolvedor Backend.
- [x] Engenheiro de Testes.
- [x] DevOps.
- [x] Analista de Qualidade.
- [x] Suporte.

## 16.2 Competências

### Gerente

- [x] Planejamento.
- [x] Comunicação.
- [x] Gestão de riscos.
- [x] Gestão de stakeholders.

### Analista

- [x] Elicitação.
- [x] Modelagem.
- [x] Documentação.
- [x] Rastreabilidade.

### Arquiteto

- [x] Arquitetura.
- [x] Integração.
- [x] Segurança.
- [x] Decisões técnicas.

### Desenvolvedor

- [x] Linguagem definida.
- [x] Git.
- [x] Testes.
- [x] Padrões de código.

### Testador

- [x] Testes funcionais.
- [x] Testes de integração.
- [x] Testes de regressão.
- [x] Gestão de defeitos.

### DevOps

- [x] CI/CD.
- [x] Infraestrutura.
- [x] Monitoramento.
- [x] Backup.

---

# 17. RACI

## 17.1 Atividades

| Atividade | GP | AR | AS | DEV | TEST | OPS | QA |
|---|---|---|---|---|---|---|---|
| Planejamento | A/R | C | C | I | I | C | C |
| Requisitos | A | R | C | I | C | I | C |
| Arquitetura | C | C | R/A | C | C | C | I |
| Implementação | I | I | A | R | C | C | I |
| Testes | I | C | C | C | R/A | I | C |
| Implantação | A | I | C | C | C | R | C |
| Qualidade | A | C | C | C | C | C | R |
| Aceite | A | C | C | I | R | I | C |

---

# 18. CAPACITAÇÃO

## 18.1 Treinamentos obrigatórios

- [x] ISO/IEC/IEEE 12207.
- [x] Engenharia de Requisitos.
- [x] Git.
- [x] Testes.
- [x] Segurança.
- [x] Padrões arquiteturais.
- [x] Ferramentas do projeto.

## 18.2 Processo

- [x] Identificar lacunas de competência.
- [x] Planejar treinamento.
- [x] Executar capacitação.
- [x] Registrar participação.
- [x] Avaliar necessidade de reciclagem.

---

# 19. QUALIDADE

## 19.1 Política

A qualidade será tratada como responsabilidade compartilhada e será incorporada ao processo de desenvolvimento, evitando que a avaliação de qualidade ocorra somente ao final do projeto.

## 19.2 Critérios

- [x] Conformidade com requisitos.
- [x] Confiabilidade.
- [x] Segurança.
- [x] Usabilidade.
- [x] Manutenibilidade.
- [x] Desempenho.

## 19.3 Métricas

- [x] Requisitos rastreados.
- [x] Cobertura de testes.
- [x] Defeitos por severidade.
- [x] Defeitos reabertos.
- [x] Tempo de correção.
- [x] Taxa de aprovação.

## 19.4 Metas sugeridas

- [x] 100% dos requisitos possuem rastreabilidade.
- [x] Cobertura mínima de testes de 80% para componentes definidos como críticos.
- [x] Zero defeitos críticos no aceite.
- [x] 100% dos requisitos críticos validados.

---

# 20. VERIFICAÇÃO E VALIDAÇÃO

## 20.1 Verificação

A verificação deverá avaliar se os produtos de trabalho foram construídos de acordo com seus requisitos e especificações.

- [x] Revisão de requisitos.
- [x] Revisão de arquitetura.
- [x] Revisão de código.
- [x] Testes unitários.
- [x] Testes de integração.
- [x] Testes funcionais.

## 20.2 Validação

A validação deverá avaliar se o produto atende ao uso pretendido e às necessidades do cliente.

- [x] Testes de aceitação.
- [x] Homologação.
- [x] Cenários reais de uso.
- [x] Participação de representante do cliente.

---

# 21. CONFIGURAÇÃO

## 21.1 Itens de configuração

- [x] Código-fonte.
- [x] Requisitos.
- [x] Arquitetura.
- [x] Diagramas.
- [x] Casos de teste.
- [x] Scripts de infraestrutura.
- [x] Documentação.
- [x] Configurações relevantes.

## 21.2 Versionamento

- [x] Git.
- [x] Repositório remoto.
- [x] Branches.
- [x] Pull Requests.
- [x] Tags de versão.

## 21.3 Mudanças

Nenhuma mudança relevante deverá ser incorporada sem avaliação de impacto e atualização dos artefatos afetados.

---

# 22. GESTÃO DE MUDANÇAS

## 22.1 Origem de mudanças

- [x] Cliente.
- [x] Usuário.
- [x] Equipe técnica.
- [x] Requisito regulatório.
- [x] Incidente.
- [x] Melhoria identificada.

## 22.2 Processo

1. Registrar solicitação.
2. Classificar.
3. Avaliar impacto.
4. Estimar esforço.
5. Avaliar riscos.
6. Aprovar ou rejeitar.
7. Planejar.
8. Implementar.
9. Testar.
10. Atualizar documentação.
11. Encerrar.

---

# 23. RISCOS

## 23.1 Riscos técnicos

- [x] Falha de infraestrutura.
- [x] Indisponibilidade de fornecedor.
- [x] Vulnerabilidade.
- [x] Erro de integração.
- [x] Corrupção de dados.
- [x] Problema de desempenho.

## 23.2 Riscos organizacionais

- [x] Rotatividade.
- [x] Falta de competência.
- [x] Atrasos.
- [x] Comunicação inadequada.
- [x] Mudança de escopo.

## 23.3 Riscos de negócio

- [x] Baixa adesão.
- [x] Mudança de necessidade do cliente.
- [x] Custo operacional maior que o previsto.
- [x] Dependência de fornecedor.

## 23.4 Para cada risco registrar

- [ ] Identificador.
- [ ] Descrição.
- [ ] Causa.
- [ ] Consequência.
- [ ] Probabilidade.
- [ ] Impacto.
- [ ] Exposição.
- [ ] Responsável.
- [ ] Mitigação.
- [ ] Plano de contingência.
- [ ] Status.

---

# 24. GESTÃO DE INFORMAÇÃO

## 24.1 Documentos controlados

- [x] Manual de processos.
- [x] Requisitos.
- [x] Arquitetura.
- [x] Plano de projeto.
- [x] Plano de testes.
- [x] Relatórios.
- [x] Registros de risco.
- [x] Registros de mudança.
- [x] Registros de qualidade.

## 24.2 Regras

Cada documento controlado deverá possuir:

- [x] Identificação.
- [x] Responsável.
- [x] Versão.
- [x] Data.
- [x] Status.
- [x] Histórico de alterações.

---

# 25. GESTÃO DO CONHECIMENTO

## 25.1 Fontes

- [x] Repositório Git.
- [x] Wiki.
- [x] Documentação.
- [x] ADRs.
- [x] Atas.
- [x] Lições aprendidas.
- [x] Registros de incidentes.

## 25.2 Preservação

- [x] Controle de versão.
- [x] Backup.
- [x] Acesso controlado.
- [x] Registro de decisões.

## 25.3 Transferência

- [x] Onboarding.
- [x] Documentação.
- [x] Revisões técnicas.
- [x] Reuniões de compartilhamento.

---

# 26. DECISÕES ARQUITETURAIS

## 26.1 ADR

Toda decisão arquitetural relevante deverá possuir registro contendo:

- [x] Contexto.
- [x] Problema.
- [x] Alternativas.
- [x] Decisão.
- [x] Consequências.
- [x] Data.
- [x] Responsável.

## 26.2 Exemplos de ADRs esperados

- [x] Monólito modular.
- [x] React.
- [x] Node.js.
- [x] PostgreSQL.
- [x] AWS.
- [x] REST.
- [x] Estratégia de autenticação.

---

# 27. IMPLANTAÇÃO

## 27.1 Estratégia

- [x] Implantação controlada.
- [x] Ambiente de homologação antes de produção.
- [x] Checklist de implantação.
- [x] Validação pós-implantação.

## 27.2 Rollback

- [x] Deve existir estratégia de rollback.
- [ ] Definir tempo máximo.
- [ ] Definir responsáveis.
- [ ] Definir critérios para acionamento.

---

# 28. OPERAÇÃO

## 28.1 Responsabilidades

- [x] Cliente opera o sistema.
- [x] CineSoft fornece suporte.
- [x] CineSoft monitora infraestrutura sob sua responsabilidade.

## 28.2 Monitoramento

- [x] Disponibilidade.
- [x] Erros.
- [x] Desempenho.
- [x] Recursos de infraestrutura.
- [x] Banco de dados.

## 28.3 Incidentes

Definir:

- [ ] Severidade.
- [ ] Prioridade.
- [ ] Tempo de resposta.
- [ ] Tempo de solução.
- [ ] Responsável.
- [ ] Escalonamento.

---

# 29. BACKUP E RECUPERAÇÃO

## 29.1 Backup

- [x] Diário.
- [ ] Incremental.
- [ ] Completo.
- [ ] Retenção definida.

## 29.2 Recuperação

- [ ] RTO.
- [ ] RPO.
- [ ] Procedimento de restauração.
- [ ] Testes periódicos de restauração.

### Sugestão inicial

- [x] RTO de até 4 horas.
- [x] RPO de até 24 horas.

Esses valores são premissas do estudo de caso e deverão ser tratados como requisitos operacionais, caso aprovados.

---

# 30. MANUTENÇÃO

## 30.1 Corretiva

- [x] Correção de defeitos.
- [x] Priorização por severidade.
- [x] Teste de regressão.
- [x] Registro da solução.

## 30.2 Adaptativa

- [x] Alterações de infraestrutura.
- [x] Atualizações de dependências.
- [x] Mudanças de requisitos externos.

## 30.3 Evolutiva

- [x] Novas funcionalidades mediante solicitação e aprovação.

## 30.4 Preventiva

- [x] Atualização de dependências.
- [x] Refatoração.
- [x] Revisão de segurança.
- [x] Revisão de desempenho.

---

# 31. SUPORTE E SLA

## 31.1 Canais

- [x] Sistema de chamados.
- [ ] E-mail.
- [ ] Telefone.
- [ ] Chat.

## 31.2 Severidade

### Crítica

Indisponibilidade total ou perda de função essencial.

### Alta

Função importante indisponível sem alternativa adequada.

### Média

Falha que permite operação alternativa.

### Baixa

Problema cosmético ou impacto reduzido.

## 31.3 SLA

Definir:

- [ ] Tempo de primeira resposta.
- [ ] Tempo de solução.
- [ ] Horário de atendimento.
- [ ] Escalonamento.

---

# 32. CONTINUIDADE DO NEGÓCIO

## 32.1 Cenários

- [x] Falha de servidor.
- [x] Falha de banco.
- [x] Indisponibilidade de fornecedor.
- [x] Perda de dados.
- [x] Ataque de segurança.
- [x] Falha de implantação.

## 32.2 Plano de continuidade

- [ ] Responsáveis.
- [ ] Procedimentos.
- [ ] Comunicação.
- [ ] Priorização de serviços.
- [ ] Recuperação.
- [ ] Testes periódicos.

---

# 33. AUDITORIA E CONFORMIDADE

## 33.1 Auditorias internas

- [x] Sim.
- [ ] Não.

## 33.2 Objetivos

- [x] Verificar aderência ao manual.
- [x] Verificar registros.
- [x] Identificar não conformidades.
- [x] Propor ações corretivas.

## 33.3 Frequência

- [x] Ao final de cada incremento.
- [ ] Mensal.
- [ ] Trimestral.

## 33.4 Normas e referências

- [x] ISO/IEC/IEEE 12207 como referência principal de processos.
- [ ] ISO/IEC 25010 para características de qualidade.
- [ ] ISO/IEC 27001 para gestão de segurança.
- [x] LGPD para tratamento de dados pessoais, quando aplicável.

A adoção de outras normas deverá ser declarada explicitamente no manual e não deve ser confundida com requisito da ISO 12207.

---

# 34. DADOS PESSOAIS E PRIVACIDADE

## 34.1 Dados pessoais

Decidir se o sistema armazenará:

- [x] Nome.
- [x] E-mail.
- [x] Telefone, se necessário.
- [x] Dados de autenticação.
- [ ] Dados de pagamento.
- [ ] Dados biométricos.
- [ ] Dados sensíveis.

## 34.2 Princípios

- [x] Minimização.
- [x] Controle de acesso.
- [x] Proteção dos dados.
- [x] Retenção definida.
- [x] Exclusão quando aplicável.
- [x] Registro de operações relevantes.

---

# 35. TESTES

## 35.1 Níveis

- [x] Unitário.
- [x] Integração.
- [x] Sistema.
- [x] Aceitação.

## 35.2 Tipos

- [x] Funcional.
- [x] Regressão.
- [x] Segurança.
- [x] Desempenho.
- [x] Usabilidade.

## 35.3 Artefatos

- [x] Plano de testes.
- [x] Casos de teste.
- [x] Evidências.
- [x] Relatório.
- [x] Registro de defeitos.

---

# 36. MEDIÇÃO

## 36.1 Projeto

- [x] Prazo.
- [x] Esforço.
- [x] Custo.
- [x] Progresso.

## 36.2 Produto

- [x] Defeitos.
- [x] Desempenho.
- [x] Disponibilidade.
- [x] Cobertura de testes.

## 36.3 Processo

- [x] Cumprimento de etapas.
- [x] Retrabalho.
- [x] Não conformidades.
- [x] Tempo de resolução.

## 36.4 Regra

Cada métrica deverá possuir:

- [ ] Nome.
- [ ] Objetivo.
- [ ] Fórmula.
- [ ] Fonte.
- [ ] Responsável.
- [ ] Frequência.
- [ ] Meta.
- [ ] Ação quando fora da meta.

---

# 37. GESTÃO DE CONFIGURAÇÃO

## 37.1 Itens de configuração

- [x] Código.
- [x] Documentos.
- [x] Requisitos.
- [x] Testes.
- [x] Infraestrutura.
- [x] Configurações.
- [x] Releases.

## 37.2 Baselines

- [ ] Baseline de requisitos.
- [ ] Baseline arquitetural.
- [ ] Baseline de release.

## 37.3 Releases

- [x] Versionamento semântico ou política equivalente.
- [x] Notas de versão.
- [x] Registro de alterações.
- [x] Aprovação antes da produção.

---

# 38. RASTREABILIDADE

## 38.1 Cadeia mínima

O manual deverá permitir relacionar:

**Necessidade → Stakeholder → Requisito → Arquitetura → Implementação → Teste → Aceite → Release**

- [x] Adotar essa cadeia.

## 38.2 Cobertura

- [x] Todo requisito importante deve possuir teste.
- [x] Todo teste importante deve possuir requisito ou objetivo.
- [x] Mudanças devem permitir identificar artefatos afetados.

---

# 39. GESTÃO DE DEFEITOS

## 39.1 Registro

Cada defeito deverá possuir:

- [x] Identificador.
- [x] Descrição.
- [x] Ambiente.
- [x] Severidade.
- [x] Prioridade.
- [x] Evidência.
- [x] Responsável.
- [x] Status.
- [x] Correção.
- [x] Teste de regressão.

## 39.2 Estados

- [x] Aberto.
- [x] Em análise.
- [x] Em correção.
- [x] Em teste.
- [x] Resolvido.
- [x] Reaberto.
- [x] Rejeitado.

---

# 40. GESTÃO DE PORTFÓLIO

## 40.1 Posição do CineDoom

- [x] Produto estratégico.
- [x] Produto comercial.
- [x] Produto sujeito a evolução.

## 40.2 Decisões de portfólio

Avaliar:

- [ ] Valor esperado.
- [ ] Custo.
- [ ] Risco.
- [ ] Capacidade da organização.
- [ ] Demanda do mercado.
- [ ] Evolução tecnológica.

---

# 41. GESTÃO DE FORNECEDORES E PARCEIROS

## 41.1 Parceiros potenciais

- [x] Provedor de nuvem.
- [x] Serviço de monitoramento.
- [x] Serviço de backup.
- [x] Serviço de e-mail.
- [ ] Consultoria.

## 41.2 Avaliação periódica

- [x] Disponibilidade.
- [x] Segurança.
- [x] Cumprimento contratual.
- [x] Custo.
- [x] Qualidade do suporte.

---

# 42. ENCERRAMENTO DO PRODUTO

## 42.1 Descontinuação

Decidir como ocorrerá:

- [ ] Comunicação ao cliente.
- [ ] Prazo de encerramento.
- [ ] Exportação dos dados.
- [ ] Exclusão dos dados.
- [ ] Encerramento de contratos.
- [ ] Desligamento de infraestrutura.
- [ ] Preservação de registros obrigatórios.

## 42.2 Portabilidade

- [x] O cliente deverá receber seus dados em formato acordado no encerramento.

---

# 43. POLÍTICA DE DECISÃO E GOVERNANÇA

## 43.1 Quem decide?

### Escopo

- [x] Gerente de Projeto + representante do cliente.

### Arquitetura

- [x] Arquiteto + equipe técnica.

### Qualidade

- [x] Responsável pela qualidade + equipe.

### Release

- [x] Gerente de Projeto + responsáveis técnicos.

### Segurança

- [x] Responsável técnico/segurança.

---

# 44. ARTEFATOS DO MANUAL

## 44.1 Artefatos esperados ao longo do ciclo de vida

- [x] Documento de visão.
- [x] Requisitos.
- [x] Casos de uso.
- [x] Backlog.
- [x] Arquitetura.
- [x] ADRs.
- [x] Plano de projeto.
- [x] Plano de qualidade.
- [x] Plano de testes.
- [x] Casos de teste.
- [x] Matriz de rastreabilidade.
- [x] Registro de riscos.
- [x] Registro de mudanças.
- [x] Registro de configuração.
- [x] Relatórios.
- [x] Manual do usuário.
- [x] Manual técnico.
- [x] Relatório de aceite.
- [x] Registro de lições aprendidas.

---

# 45. MATRIZ DE RELAÇÃO ENTRE DECISÕES E FUTURAS PARTES DO MANUAL

| Decisão | Impacta principalmente |
|---|---|
| Tipo Web/SaaS | Aquisição, fornecimento, arquitetura, operação |
| Público-alvo | Requisitos, validação, qualidade |
| Perfis | Requisitos, segurança, testes |
| Escopo | Requisitos, arquitetura, implementação, testes |
| Arquitetura | Implementação, integração, implantação, manutenção |
| AWS | Aquisição, infraestrutura, operação |
| PostgreSQL | Arquitetura, implementação, backup, recuperação |
| Incremental | Planejamento, desenvolvimento, testes, releases |
| RACI | Recursos humanos, gestão, qualidade |
| Metas de qualidade | Qualidade, medição, validação |
| RTO/RPO | Operação, continuidade, infraestrutura |
| Suporte | Fornecimento, operação, manutenção |
| Rastreabilidade | Requisitos, verificação, validação, configuração |

---

# 46. REGRAS DE CONSISTÊNCIA DO MANUAL

## 46.1 Regra de escopo

Nenhuma seção futura poderá introduzir uma funcionalidade que esteja explicitamente fora do escopo sem registrar uma mudança formal.

## 46.2 Regra tecnológica

Tecnologias aprovadas neste documento deverão ser utilizadas nas seções técnicas posteriores, salvo decisão formal de alteração.

## 46.3 Regra de terminologia

Os mesmos termos deverão ser usados em todo o manual.

Exemplo:

- **Filme** não deve posteriormente ser chamado de "obra".
- **Sessão** não deve posteriormente ser chamada de "exibição" se ambos não forem conceitos distintos.
- **Ingresso** não deve ser confundido com "reserva".
- **Usuário** deve ser diferenciado de **cliente**.

## 46.4 Regra de rastreabilidade

Toda decisão importante deverá possuir relação com os artefatos que serão afetados.

## 46.5 Regra de mudança

Alterações nas decisões congeladas deverão ser analisadas antes de serem incorporadas ao manual.

---

# 47. DECISÕES QUE AINDA PRECISAM SER FECHADAS

Esta seção deve ser preenchida pelo grupo antes da consolidação da versão oficial.

## Produto

- [ ] Slogan.
- [ ] Versão inicial.
- [ ] Identidade visual.
- [ ] Descrição definitiva.

## Organização

- [ ] Nome definitivo da empresa.
- [ ] Missão.
- [ ] Visão.
- [ ] Valores.
- [ ] Estrutura organizacional.

## Negócio

- [ ] Preço.
- [ ] Modelo de assinatura.
- [ ] SLA.
- [ ] Contrato.
- [ ] Política de encerramento.

## Requisitos

- [ ] Lista final de RFs.
- [ ] Lista final de RNFs.
- [ ] Regras de negócio.
- [ ] Critérios de aceite.

## Arquitetura

- [ ] Confirmar React.
- [ ] Confirmar Node.js.
- [ ] Confirmar PostgreSQL.
- [ ] Confirmar AWS.
- [ ] Confirmar monólito modular.
- [ ] Confirmar REST.

## Segurança

- [ ] Política de senha.
- [ ] Expiração de sessão.
- [ ] MFA.
- [ ] Auditoria.
- [ ] Retenção de logs.

## Infraestrutura

- [ ] Serviços AWS específicos.
- [ ] Dimensionamento.
- [ ] Backup.
- [ ] Monitoramento.
- [ ] Recuperação.

## Operação

- [ ] SLA.
- [ ] Horário de suporte.
- [ ] Severidade.
- [ ] Escalonamento.

## Qualidade

- [ ] Métricas definitivas.
- [ ] Metas definitivas.
- [ ] Frequência das medições.
- [ ] Responsáveis.

## Continuidade

- [ ] RTO.
- [ ] RPO.
- [ ] Plano de recuperação.
- [ ] Testes de recuperação.

---

# 48. CHECKLIST DE CONGELAMENTO

Antes de utilizar este documento como base oficial do manual, verificar:

## Identidade

- [ ] Nome definido.
- [ ] Empresa definida.
- [ ] Produto definido.
- [ ] Problema definido.
- [ ] Benefício definido.

## Negócio

- [ ] Cliente definido.
- [ ] Usuários definidos.
- [ ] Modelo de negócio definido.
- [ ] Forma de fornecimento definida.
- [ ] Stakeholders definidos.

## Escopo

- [ ] Funcionalidades definidas.
- [ ] Fora do escopo definido.
- [ ] Entidades definidas.
- [ ] Regras de negócio definidas.

## Técnico

- [ ] Tipo de aplicação definido.
- [ ] Arquitetura definida.
- [ ] Frontend definido.
- [ ] Backend definido.
- [ ] Banco definido.
- [ ] Infraestrutura definida.

## Processos

- [ ] Ciclo de vida definido.
- [ ] Aquisição definida.
- [ ] Fornecimento definido.
- [ ] Recursos humanos definidos.
- [ ] Qualidade definida.
- [ ] Conhecimento definido.

## Gerência

- [ ] Planejamento definido.
- [ ] Riscos definidos.
- [ ] Configuração definida.
- [ ] Mudanças definidas.
- [ ] Medição definida.
- [ ] Informação definida.

## Técnico-operacional

- [ ] Verificação definida.
- [ ] Validação definida.
- [ ] Implantação definida.
- [ ] Operação definida.
- [ ] Manutenção definida.
- [ ] Continuidade definida.

## Governança

- [ ] Responsabilidades definidas.
- [ ] Autoridades definidas.
- [ ] Auditoria definida.
- [ ] Critérios de aceite definidos.
- [ ] Processo de decisão definido.

---

# 49. BASE RECOMENDADA DO CineDoom APÓS O CONGELAMENTO

A configuração recomendada para o estudo de caso é:

| Dimensão | Decisão recomendada |
|---|---|
| Produto | CineDoom |
| Organização | CineSoft Solutions |
| Domínio | Gestão operacional de cinemas |
| Público | Pequenos e médios cinemas |
| Região | Brasil |
| Tipo | Plataforma web |
| Modelo | SaaS |
| Arquitetura | Monólito modular |
| Frontend | React |
| Backend | Node.js |
| Banco | PostgreSQL |
| Cloud | AWS |
| API | REST |
| Ciclo de vida | Incremental |
| Usuários | Administrador, gerente e atendente |
| Cliente final | Fora do sistema administrativo na primeira versão |
| Pagamentos | Fora do escopo inicial |
| Mobile | Fora do escopo inicial |
| Streaming | Fora do escopo |
| IA | Fora do escopo inicial |
| Suporte | CineSoft |
| Operação | Cliente |
| Manutenção | CineSoft |
| Backup | Diário |
| Disponibilidade | 95% inicialmente |
| RTO | Até 4 horas, sujeito à aprovação |
| RPO | Até 24 horas, sujeito à aprovação |
| Testes | Unitário, integração, sistema e aceitação |
| Controle de versão | Git |
| Repositório | GitHub |
| Qualidade | Métricas e revisões por incremento |
| Rastreabilidade | Requisito → arquitetura → implementação → teste → aceite |
| Configuração | Controle formal dos artefatos |
| Mudança | Avaliação de impacto e aprovação |

---

# 50. REGISTRO DE ALTERAÇÕES DE DECISÕES

| Versão | Data | Decisão alterada | Motivo | Impactos identificados | Responsável |
|---|---|---|---|---|---|
| 1.0 | ____/____/______ | Documento inicial | Definição do projeto | A definir | __________ |
| | | | | | |
| | | | | | |

---

# Encerramento

Este workbook deve permanecer associado ao Manual de Processos de Software durante todo o projeto. Ele funciona como referência para manter a coerência entre o estudo de caso e os processos que serão documentados posteriormente.

A principal finalidade não é preencher a maior quantidade possível de campos, mas garantir que as decisões relevantes sejam tomadas conscientemente, registradas e utilizadas de maneira consistente.

As recomendações marcadas neste documento devem ser entendidas como uma **linha de projeto sugerida** para tornar o CineDoom um estudo de caso suficientemente realista para aplicação da ISO/IEC/IEEE 12207, mas sem introduzir complexidade que não contribua para o objetivo acadêmico do manual.

Após o congelamento desta base, os processos posteriores deverão ser derivados dela. Assim, requisitos, arquitetura, implementação, verificação, validação, operação, manutenção, qualidade, riscos, configuração e demais processos passarão a representar diferentes perspectivas do **mesmo produto**, e não sistemas diferentes surgindo em cada capítulo.
