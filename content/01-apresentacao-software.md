# Capítulo 1 – Apresentação do software

## 1.1 Nome e descrição do software

**Nome do software:** CineDoom.

O CineDoom é uma plataforma web comercial de gerenciamento operacional e bilheteria voltada para **cinemas de pequeno e médio porte**. Trata-se de um sistema administrativo de retaguarda (*back-office*) concebido para fornecimento no modelo **SaaS (Software as a Service)**, no qual o cliente acessa o sistema por meio de navegadores web modernos, sem necessidade de instalação local em seus computadores.

O sistema é desenvolvido pela organização **CineSoft Solutions** e atua como estudo de caso estruturante para a aplicação formal dos processos da norma ABNT NBR ISO/IEC/IEEE 12207:2021.

## 1.2 Qual é o software? O que ele faz? Qual problema resolve?

### O que ele faz?
O CineDoom centraliza as operações diárias de um cinema em uma interface web única e intuitiva:
- Mantém o catálogo de filmes em cartaz e suas especificações técnicas.
- Controla a infraestrutura de salas e seus respectivos mapas de assentos.
- Agenda e publica sessões cinematográficas com validação automática de conflitos de horários.
- Opera a venda e o cancelamento de ingressos na bilheteria com reserva visual de assentos e proteção atômica contra venda dupla (*double-booking*).
- Apresenta indicadores em tempo real sobre a taxa de ocupação das salas e o faturamento operacional.

### Qual problema resolve?
O setor de cinemas de pequeno e médio porte frequentemente gerencia suas operações com controles manuais (planilhas descentralizadas, bilhetes de papel) ou softwares legados e desconectados. Esse cenário acarreta:
1. **Conflito de assentos:** Risco de venda dupla da mesma cadeira em horários de pico.
2. **Descentralização da informação:** Dificuldade em cruzar disponibilidade de salas com a programação de lançamentos.
3. **Ausência de rastreabilidade:** Falta de registro auditável sobre quem realizou cada cancelamento ou venda.
4. **Decisão sem dados:** Incapacidade de mensurar a taxa de ocupação das salas para planejamento de grade.

O CineDoom elimina esses gargalos ao prover um ambiente único, transacional e rastreável, com regras de negócio rígidas e feedback operacional instantâneo.

## 1.3 Público-alvo e contexto de uso

O público-alvo prioritário é composto por **cinemas independentes e redes de pequeno e médio porte** atuantes no mercado nacional. A solução é B2B (*Business-to-Business*), atendendo estabelecimentos que demandam controle operacional informatizado com baixo custo inicial de implantação.

O contexto de uso abrange:
- **Ambiente de bilheteria:** Atendimento presencial rápido ao espectador, exigindo tempos de resposta inferiores a 2 segundos para seleção de assentos e conclusão da venda.
- **Ambiente administrativo:** Planejamento semanal de grades de exibição, cadastro de filmes e acompanhamento de relatórios de desempenho operacional por parte da gerência.

## 1.4 Quem vai usar? Em que situação? Qual o ambiente de operação esperado?

### Perfis de Usuários
- **Atendente:** Opera a tela de bilheteria durante o atendimento presencial. Consulta sessões, seleciona assentos no mapa visual, emite ingressos e executa cancelamentos mediante confirmação.
- **Gerente:** Configura salas, cadastra e inativa filmes, cria e cancela sessões de exibição e analisa a ocupação das salas.
- **Administrador:** Gerencia os perfis de acesso, parametriza regras globais do sistema e audita logs operacionais.

### Ambiente de Operação Esperado
- **Hardware:** Computadores desktop ou notebooks convencionais operados pelos funcionários do cinema.
- **Software:** Navegadores web modernos com suporte a padrões ECMAScript atuais (Google Chrome, Mozilla Firefox, Microsoft Edge, Safari).
- **Conectividade:** Conexão contínua com a internet (mínimo de 5 Mbps estável para troca de payloads JSON via HTTPS).
- **Espectador final:** Não possui acesso direto ao sistema administrativo nesta versão; o atendimento ocorre integralmente mediado pelo atendente na bilheteria.

## 1.5 Escopo e principais funcionalidades

### Escopo Central e Funcionalidades Incluídas
O escopo cobre as atividades centrais da cadeia de exibição cinematográfica:
1. **Módulo de Filmes:** Cadastro de título, sinopse, duração, classificação indicativa e pôster.
2. **Módulo de Salas e Assentos:** Cadastro de salas com capacidade configurável e mapeamento bidimensional de assentos (ex.: fileiras A–E, assentos 1–6).
3. **Módulo de Sessões:** Associação de Filme + Sala + Horário de início + Preço base do ingresso.
4. **Módulo de Bilheteria (Venda e Cancelamento):** Mapa interativo de assentos (livre, selecionado, vendido), reserva atômica contra venda simultânea e cancelamento com liberação imediata.
5. **Módulo de Ocupação:** Painel visual com percentual de lotação da sala por sessão.

### Requisitos Funcionais do Sistema (RF-01 a RF-12)

| Código | Nome do Requisito | Escopo no Ciclo de Vida |
|---|---|---|
| **RF-01** | Autenticar usuário | MVP (Simplificado via seleção de perfil de balcão) |
| **RF-02** | Gerenciar usuários e acessos | Backlog Futuro (Carga inicial via migração) |
| **RF-03** | Cadastrar e gerenciar filmes | MVP (Must Have) |
| **RF-04** | Cadastrar e gerenciar salas | MVP (Must Have) |
| **RF-05** | Agendar e gerenciar sessões | MVP (Must Have) |
| **RF-06** | Consultar disponibilidade de assentos | MVP (Must Have / Core da Demonstração) |
| **RF-07** | Registrar venda de ingresso | MVP (Must Have / Trava Transacional Atômica) |
| **RF-08** | Cancelar ingresso e liberar assento | MVP (Must Have) |
| **RF-09** | Gerenciar cadastro de clientes | Backlog Futuro (Release 1.1) |
| **RF-10** | Registrar interesse em lançamentos | Fora do Escopo Inicial |
| **RF-11** | Gerar relatórios e métricas de ocupação | MVP (Parcial: Painel de Ocupação da Sessão) |
| **RF-12** | Registrar trilha de auditoria | MVP (Log de operações de venda/cancelamento) |

## 1.6 Restrições e premissas

### Restrições
- **Processamento Financeiro Próprio:** A CineSoft não armazena dados de cartão nem executa liquidação bancária própria (vendas balcão registradas em dinheiro/PIX/cartão simulado).
- **Operação Exclusivamente Online:** O sistema requer conexão ativa; não há modo de contingência offline na primeira versão.
- **Multitenancy Isolado:** A primeira versão atende uma empresa/instância por implantação.
- **Sem Aplicativo Mobile Nativo:** Acesso via navegador web desktop responsivo.
- **Funcionalidades Descartadas:** Streaming de vídeo, vendas online voltadas ao consumidor final, programas de fidelidade, controle de estoque de bomboniere e contabilidade fiscal.

### Premissas
- A equipe do cliente possui competência básica em navegação web e receberá treinamento operacional.
- As salas possuem configuração física de assentos fixa e pré-determinada.
- O tempo máximo de resposta para operações comuns em condições de pico não deve ultrapassar 2 segundos.
- As regras de negócio de venda de assentos são validadas de forma estrita no servidor e no banco de dados relacional.

---
