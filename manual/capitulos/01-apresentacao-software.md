# Capítulo 1 – Apresentação do software

## 1.1 Nome e descrição do software

**Nome do software:** CineDoom.

O CineDoom é uma plataforma web integrada de gerenciamento operacional, bilheteria presencial e portal do cliente voltada para **cinemas de pequeno e médio porte**. O sistema é estruturado no modelo **SaaS (Software as a Service)**, permitindo que cinemas informatizem seus processos com três módulos centrais:

1. **Módulo do Atendente (Bilheteria Presencial):** Operação ágil de guichê físico, emissão direta de ingressos com trava atômica anti-double-booking e baixa presencial de reservas originadas na web.
2. **Módulo do Gerente (Back-office e Gestão):** Configuração de salas, catálogo de filmes, agendamento de sessões e acompanhamento de indicadores de ocupação em tempo real.
3. **Portal do Cliente (Espectador Final Web):** Canal público e autenticado no qual o público consulta a programação, cadastra-se com proteção de dados LGPD, seleciona assentos no mapa interativo, solicita reservas com emissão de voucher transacional e gerencia suas reservas via web.

O sistema é desenvolvido pela organização **CineSoft Solutions** e atua como estudo de caso estruturante para a aplicação formal dos processos da norma ABNT NBR ISO/IEC/IEEE 12207:2021.

## 1.2 Qual é o software? O que ele faz? Qual problema resolve?

### O que ele faz?
O CineDoom centraliza e sincroniza todas as etapas da cadeia de atendimento cinematográfico em uma interface web moderna e unificada:
- Mantém o catálogo de filmes em cartaz e suas especificações técnicas.
- Controla a infraestrutura física de salas e layouts bidimensionais de assentos.
- Agenda e publica sessões cinematográficas com prevenção automática de choques de grade.
- Garante reservas online no Portal do Cliente com bloqueio atômico de assento e expiração inteligente Just-in-Time.
- Despacha vouchers transacionais de reserva por e-mail com instruções para pagamento presencial.
- Permite o cancelamento voluntário de reservas pendentes pelo próprio cliente via web antes do limite de tolerância.
- Opera a venda e a baixa presencial de ingressos na bilheteria com trava atômica ACID (*SELECT FOR UPDATE*), eliminando riscos de venda dupla (*double-booking*).
- Apresenta métricas gerenciais em tempo real sobre a taxa de ocupação das salas e a distribuição de assentos vendidos e reservados.

### Qual problema resolve?
Cinemas independentes frequentemente operam com sistemas legados fragmentados ou controles manuais, resultando em:
1. **Conflito de assentos:** Risco crítico de venda simultânea da mesma poltrona em sessões concorridas.
2. **Inacessibilidade para o público:** Dificuldade do espectador em consultar a grade de horários e planejar sua ida ao cinema com antecedência.
3. **Assentos ociosos por no-show:** Falta de regras claras para liberação de lugares não confirmados.
4. **Ausência de rastreabilidade e compliance:** Descumprimento das exigências da LGPD no manuseio de dados de compradores e ausência de trilha auditável de cancelamentos.

O CineDoom elimina esses problemas ao unificar o canal digital do cliente e a bilheteria presencial sob o mesmo motor relacional transacional e auditável.

## 1.3 Público-alvo e contexto de uso

O público-alvo compreende:
- **Cinemas independentes e redes regionais (B2B):** Estabelecimentos que demandam controle operacional confiável e centralizado com baixo custo inicial de implantação.
- **Público espectador (B2C mediado):** Clientes do cinema que utilizam o Portal do Cliente para consultar filmes, reservar seus assentos preferidos e gerenciar seus comprovantes antes de comparecer à sessão.

O contexto de uso abrange:
- **Portal do Cliente (Web Desktop e Mobile):** Acesso pelo espectador para consulta de horários, cadastro pessoal e reserva antecipada com voucher digital.
- **Ambiente de bilheteria física:** Atendimento presencial ágil com tempo de resposta inferior a 2 segundos para venda direta ou localização e baixa de reservas prévias pelo atendente.
- **Ambiente administrativo:** Planejamento semanal de exibições, cadastro de acervo e monitoramento de lotação pela gerência.

## 1.4 Quem vai usar? Em que situação? Qual o ambiente de operação esperado?

### Perfis de Usuários
- **Espectador / Cliente Final:** Acessa o Portal do Cliente para consultar a programação, efetuar cadastro/login com credenciais seguras, selecionar assentos no mapa interativo, reservar ingressos com expiração Just-in-Time, receber comprovante por e-mail transacional, acompanhar seu histórico pessoal em "Minhas Reservas" e cancelar reservas antes do prazo limite.
- **Atendente:** Opera o guichê presencial. Consulta sessões, seleciona assentos, localiza reservas web por código ou CPF, confirma o recebimento presencial, emite ingressos e executa cancelamentos justificados.
- **Gerente:** Administra o back-office (salas, acervo de filmes, sessões de exibição), acompanha os painéis de ocupação e gerencia os operadores do sistema.
- **Administrador:** Parametriza regras globais, audita logs operacionais e gerencia os tenants da plataforma.

### Ambiente de Operação Esperado
- **Hardware:** Computadores e tablets nos pontos de venda físicos; smartphones, notebooks e desktops pessoais para os espectadores no Portal do Cliente.
- **Software:** Navegadores web modernos com suporte a ECMAScript atual (Google Chrome, Mozilla Firefox, Safari, Microsoft Edge).
- **Conectividade:** Conexão estável com a internet (mínimo de 5 Mbps para bilheteria e banda padrão 4G/5G/Wi-Fi para os clientes).
- **Pagamento das Reservas:** O pagamento de ingressos reservados via web é concluído exclusivamente de forma presencial no balcão da bilheteria até 1 hora antes da sessão, eliminando fricção de gateways financeiros externos e fraudes de cartão.

## 1.5 Escopo e principais funcionalidades

### Escopo Central e Módulos do Sistema
1. **Módulo de Filmes:** Acervo com título, sinopse, classificação indicativa, duração e material promocional.
2. **Módulo de Salas e Assentos:** Mapeamento bidimensional flexível (fileiras e colunas) e controle de capacidade física.
3. **Módulo de Sessões:** Composição de Filme + Sala + Horário + Preço, com validação de conflitos de horário.
4. **Módulo de Bilheteria Presencial:** Venda atômica direta, cancelamento auditável por trigger PostgreSQL e baixa presencial de reservas.
5. **Portal do Cliente:** Consulta de sessões, autenticação com proteção de dados LGPD, mapa interativo de assentos com trava temporária, despacho de e-mail transacional, painel de reservas e cancelamento voluntário web.
6. **Módulo de Ocupação:** Painel consolidado da taxa de lotação por sessão em tempo real.

### Requisitos Funcionais do Sistema (RF-01 a RF-18)

| Código | Nome do Requisito | Escopo no Ciclo de Vida |
|---|---|---|
| **RF-01** | Autenticar usuário por perfil (Gerente, Atendente e Cliente) | MVP (Must Have / NextAuth.js com RBAC) |
| **RF-02** | Gerenciar usuários e operadores de guichê | MVP (Gestão de atendentes pelo gerente) |
| **RF-03** | Cadastrar e gerenciar acervo de filmes | MVP (Must Have) |
| **RF-04** | Cadastrar e gerenciar salas e layouts de assentos | MVP (Must Have) |
| **RF-05** | Agendar e publicar sessões cinematográficas | MVP (Must Have) |
| **RF-06** | Consultar disponibilidade de assentos com polling de 2s | MVP (Must Have / Core Visual) |
| **RF-07** | Registrar venda de ingresso presencial com trava ACID | MVP (Must Have / SELECT FOR UPDATE) |
| **RF-08** | Cancelar ingresso e liberar assento com auditoria imutável | MVP (Must Have / Trigger PostgreSQL) |
| **RF-09** | Proteger dados pessoais de compradores conforme a LGPD | MVP (Must Have / HMAC-SHA256 + AES-256-GCM) |
| **RF-10** | Monitorar indicadores e taxas de ocupação em tempo real | MVP (Must Have / Painel Gerencial) |
| **RF-11** | Registrar trilha de auditoria e retenção legal (Axiom) | MVP (Must Have / Retenção 365 dias) |
| **RF-12** | Consultar programação e sessões no Portal do Cliente | MVP (Must Have / Consulta Pública) |
| **RF-13** | Reservar assento online com trava atômica temporária | MVP (Must Have / Status RESERVED) |
| **RF-14** | Cadastrar e autenticar cliente com consentimento LGPD | MVP (Must Have / Área pessoal segura) |
| **RF-15** | Despachar voucher de reserva via e-mail transacional | MVP (Must Have / NotificationService) |
| **RF-16** | Cancelar reserva pelo próprio cliente via web | MVP (Must Have / Painel Minhas Reservas) |
| **RF-17** | Localizar e dar baixa em reserva presencial no balcão | MVP (Must Have / Conversão em Ticket) |
| **RF-18** | Expirar reservas não pagas a 1 hora do início da sessão | MVP (Must Have / Avaliação Just-in-Time) |

## 1.6 Restrições e premissas

### Restrições
- **Pagamento Presencial Exclusivo:** O sistema não integra gateway de pagamento online (cartão/PIX web); as reservas efetuadas no portal são pagas presencialmente no guichê do cinema até 1 hora antes do início da sessão.
- **Operação Conectada:** O sistema opera na nuvem sob arquitetura serverless (Vercel + Neon PostgreSQL), exigindo conectividade ativa.
- **Multitenancy Isolado por Row-Level:** Compartilhamento de infraestrutura gerenciada com isolamento estrito via tenant_id garantido por middleware Prisma.
- **Sem Aplicativo Nativo:** Acesso via navegador web desktop e mobile responsivo sem empacotamento para lojas de aplicativos.
- **Funcionalidades Descartadas do MVP:** Streaming de vídeo, emissão fiscal externa (NFC-e), fidelidade por pontos e gestão de bomboniere.

### Premissas
- A trava pessimista SELECT FOR UPDATE e a checagem Just-in-Time impedem matematicamente qualquer conflito de assentos entre clientes web e atendentes físicos.
- As reservas realizadas com menos de 1 hora de antecedência em relação ao início da sessão são bloqueadas pelo sistema, reservando o inventário restante para o balcão.
- As reservas não quitadas presencialmente até 60 minutos antes do início do filme expiram automaticamente, liberando as poltronas para venda direta.
