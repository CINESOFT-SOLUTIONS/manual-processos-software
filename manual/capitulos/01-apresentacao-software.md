# Capítulo 1 – Apresentação do software

## 1.1 Nome e descrição do software

**Nome do software:** CineDoom.

O CineDoom é uma plataforma web integrada, no modelo **SaaS multi-tenant**, de gerenciamento operacional, bilheteria presencial e portal do cliente, voltada para **cinemas de rua, circuitos independentes e redes de pequeno e médio porte**. O sistema permite que os cinemas informatizem seus processos com três módulos centrais:

1. **Módulo do Atendente (Bilheteria Presencial):** Operação ágil de guichê físico, emissão direta de ingressos com trava atômica anti-double-booking e baixa presencial de reservas originadas na web.
2. **Módulo do Gerente (Back-office e Gestão):** Configuração de salas, catálogo de filmes, agendamento de sessões, gestão de operadores e acompanhamento de indicadores de ocupação.
3. **Portal do Cliente (Espectador Final Web):** Canal público e autenticado no qual o público consulta a programação, cadastra-se com proteção de dados LGPD, seleciona assentos no mapa interativo, solicita reservas com emissão de voucher transacional e gerencia suas reservas via web.

A CineSoft Solutions é a organização desenvolvedora (fictícia) do CineDoom, composta pela equipe acadêmica identificada na capa deste manual. O produto posiciona-se como uma solução única para unificar o atendimento digital e a operação física de bilheteria sob o mesmo motor transacional, com isolamento multi-tenant e conformidade com a LGPD. O sistema é desenvolvido como estudo de caso estruturante para a aplicação formal dos processos da norma ABNT NBR ISO/IEC/IEEE 12207:2021.

## 1.2 Qual é o software? O que ele faz? Qual problema resolve?

O CineDoom é um sistema SaaS multi-tenant que integra a operação de bilheteria, o back-office do cinema e o portal do espectador em uma única plataforma transacional.

### O que ele faz?

O CineDoom centraliza e sincroniza todas as etapas da cadeia de atendimento cinematográfico em uma interface web moderna e unificada:

- Mantém o catálogo de filmes em cartaz e suas especificações técnicas.
- Controla a infraestrutura física de salas e layouts bidimensionais de assentos.
- Agenda e disponibiliza sessões cinematográficas com prevenção automática de choques de grade.
- Garante reservas online no Portal do Cliente com bloqueio atômico de assento e expiração lógica Just-in-Time (JIT).
- Despacha vouchers transacionais de reserva por e-mail com instruções para pagamento presencial.
- Permite o cancelamento voluntário de reservas pendentes pelo próprio cliente via web antes do limite de tolerância.
- Opera a venda e a baixa presencial de ingressos na bilheteria com trava atômica ACID (*SELECT FOR UPDATE*), eliminando riscos de venda dupla (*double-booking*).
- Apresenta métricas gerenciais consolidadas sob demanda sobre a taxa de ocupação das salas e a distribuição de assentos vendidos e reservados.

### Qual problema resolve?

Cinemas independentes frequentemente operam com sistemas legados fragmentados ou controles manuais, resultando em:

1. **Conflito de assentos:** Risco crítico de venda simultânea da mesma poltrona em sessões concorridas.
2. **Inacessibilidade para o público:** Dificuldade do espectador em consultar a grade de horários e planejar sua ida ao cinema com antecedência.
3. **Assentos ociosos por no-show:** Falta de regras claras para liberação de lugares não confirmados.
4. **Ausência de rastreabilidade e compliance:** Descumprimento das exigências da LGPD no manuseio de dados de compradores e ausência de trilha auditável de cancelamentos.

O CineDoom elimina esses problemas ao unificar o canal digital do cliente e a bilheteria presencial sob o mesmo motor relacional transacional e auditável.

### Proposta de valor

O CineDoom entrega um único motor transacional e auditável para os canais físico e digital. Na prática, isso reduz o risco de venda dupla, libera assentos não confirmados para reaproveitamento, diminui a dependência de controles manuais e trata os dados pessoais dos compradores conforme a LGPD.

## 1.3 Público-alvo e contexto de uso

O público-alvo é composto por:

- **Público de negócio (B2B):** cinemas de rua, circuitos independentes e redes de pequeno e médio porte que precisam informatizar a bilheteria, a programação e a gestão de salas.
- **Público final (B2C):** espectadores que utilizam o Portal do Cliente para consultar filmes, reservar seus assentos preferidos e gerenciar seus comprovantes antes de comparecer à sessão.
- **Público operacional (usuários diretos):** gerentes e atendentes que operam o back-office e a bilheteria no dia a dia do cinema.
- **Público indireto:** equipe de suporte e operação da CineSoft Solutions e provedores de infraestrutura que sustentam a plataforma.

O contexto de uso abrange:

- **Portal do Cliente (web desktop e mobile):** acesso pelo espectador para consulta de horários, cadastro pessoal e reserva antecipada com voucher digital.
- **Ambiente de bilheteria física:** atendimento presencial ágil para venda direta ou localização e baixa de reservas prévias pelo atendente. Os indicadores de desempenho desse ambiente são definidos e verificados no Capítulo 5.
- **Ambiente administrativo:** planejamento semanal de exibições, cadastro de acervo e monitoramento de lotação pela gerência.

A Figura 1 ilustra a interface do Portal do Cliente, com o catálogo de filmes em cartaz e o mapa interativo de assentos utilizado pelo espectador.

![Figura 1 – Portal do Cliente: catálogo de filmes e mapa interativo de assentos](../assets/prints/print-portal-cliente.png)
    
*Figura 1 – Portal do Cliente: catálogo de filmes em cartaz e mapa interativo de assentos (ART-004).*

## 1.4 Quem vai usar? Em que situação? Qual o ambiente de operação esperado?

### Perfis de Usuários

- **Espectador / Cliente Final:** Acessa o Portal do Cliente para consultar a programação, efetuar cadastro/login com credenciais seguras, selecionar assentos no mapa interativo, reservar ingressos com expiração Just-in-Time, receber comprovante por e-mail transacional, acompanhar seu histórico pessoal em "Minhas Reservas" e cancelar reservas antes do prazo limite.
- **Atendente:** Opera o guichê presencial. Consulta sessões, seleciona assentos, localiza reservas web por código ou CPF, confirma o recebimento presencial, emite ingressos e executa cancelamentos justificados.
- **Gerente:** Administra o back-office (salas, acervo de filmes, sessões de exibição), acompanha os painéis de ocupação e gerencia os usuários com perfil ATENDENTE.
- **Administrador da plataforma (perfil previsto, não disponível no MVP):** Responsável pela parametrização global, auditoria de logs e gestão de tenants. Na versão atual, essas atividades são conduzidas pela operação técnica da CineSoft Solutions; o produto entregue contempla os perfis Gerente, Atendente e Cliente.

### Ambiente de Operação Esperado

- **Hardware:** Computadores e tablets nos pontos de venda físicos; smartphones, notebooks e desktops pessoais para os espectadores no Portal do Cliente.
- **Software:** Navegadores web modernos com suporte a ECMAScript atual (Google Chrome, Mozilla Firefox, Safari, Microsoft Edge).
- **Conectividade:** Conexão estável com a internet, uma vez que a operação é realizada em navegador e o processamento ocorre em nuvem.
- **Pagamento das Reservas:** O pagamento de ingressos reservados via web é concluído exclusivamente de forma presencial no balcão da bilheteria até 1 hora antes da sessão, eliminando a dependência de gateway financeiro online e reduzindo a superfície de fraude em transações digitais.

A Figura 2 apresenta a interface da bilheteria presencial, utilizada pelo atendente para a venda direta de ingressos e a baixa de reservas originadas no portal.

![Figura 2 – Bilheteria presencial: mapa de assentos e operação de guichê](../assets/prints/print-bilheteria-atendente.png)

*Figura 2 – Bilheteria presencial: mapa de assentos, venda direta e baixa de reservas pelo atendente (ART-005).*

## 1.5 Escopo e principais funcionalidades

### Escopo Central e Módulos do Sistema

1. **Módulo de Filmes:** Acervo com título, sinopse, classificação indicativa, duração e material promocional.
2. **Módulo de Salas e Assentos:** Mapeamento bidimensional flexível (fileiras e colunas) e controle de capacidade física.
3. **Módulo de Sessões:** Composição de Filme + Sala + Horário + Preço, com validação de conflitos de horário.
4. **Módulo de Bilheteria Presencial:** Venda atômica direta, cancelamento auditável com trilha append-only protegida por trigger PostgreSQL (ADR-010) e baixa presencial de reservas.
5. **Portal do Cliente:** Consulta de sessões, autenticação com proteção de dados LGPD, mapa interativo de assentos com reserva temporária, despacho de e-mail transacional, painel de reservas e cancelamento voluntário web.
6. **Módulo de Ocupação:** Painel consolidado sob demanda da taxa de lotação por sessão.
7. **Módulo de Autenticação e Controle de Acesso:** Login com sessão JWT de 8 horas, RBAC para os perfis Gerente, Atendente e Cliente e revogação imediata do acesso de usuário inativado.
8. **Módulo de Gestão de Usuários:** Criação, atualização e inativação de atendentes pelo gerente, com e-mail único por tenant.
9. **Módulo de Conformidade e Privacidade (LGPD):** Consentimento explícito, criptografia de CPF, anonimização do titular e auditoria de cancelamentos.
10. **Módulo de Notificações Transacionais:** Envio de voucher de reserva por e-mail, com provedor configurável conforme o ambiente.

A Figura 3 apresenta o painel gerencial do back-office, com a programação de sessões e os indicadores de ocupação acompanhados pela gerência.

![Figura 3 – Back-office gerencial: programação de sessões e indicadores de ocupação](../assets/prints/print-painel-gerencial.png)

*Figura 3 – Back-office gerencial: programação de sessões e indicadores de ocupação das salas (ART-006).*

### Fora do escopo imediato

- Gateway de pagamento online (PIX ou cartão) e checkout financeiro web.
- Emissão fiscal (NFC-e) e integração contábil.
- Programa de fidelidade, cupons e gestão de bomboniere/estoque.
- Aplicativo nativo para iOS ou Android; o acesso é feito por navegador web responsivo.
- Streaming de vídeo e produção de conteúdo promocional audiovisual.
- Console administrativo de tenants e faturamento SaaS (perfil Administrador da plataforma).
- Integrações com distribuidoras, e-commerce externo e marketplaces.
- Relatórios financeiros avançados e BI; o painel de ocupação é operacional.

## 1.6 Restrições e premissas

### Restrições

- **Pagamento Presencial Exclusivo:** O sistema não integra gateway de pagamento online (cartão/PIX web); as reservas efetuadas no portal são pagas presencialmente no guichê do cinema até 1 hora antes do início da sessão.
- **Operação Conectada:** O sistema opera na nuvem sob arquitetura serverless (Vercel + Neon PostgreSQL), exigindo conectividade ativa.
- **Isolamento Multi-tenant Lógico:** O compartilhamento de infraestrutura é controlado por meio do `tenant_id`, aplicado por uma extensão de tenancy do Prisma Client com `AsyncLocalStorage`. O produto não utiliza `ROW LEVEL SECURITY` nativo do PostgreSQL.
- **Sem Aplicativo Nativo:** Acesso via navegador web desktop e mobile responsivo, sem empacotamento para lojas de aplicativos.
- **Conformidade LGPD:** O tratamento de dados pessoais exige consentimento explícito, criptografia de CPF (AES-256-GCM + HMAC-SHA256), minimização, anonimização do titular (Art. 18) e retenção de trilha de auditoria. O CPF não é armazenado em texto puro.
- **Limites de Layout Físico:** As salas suportam até 26 fileiras (A–Z) e 50 assentos por fileira.
- **Trilha de Auditoria Imutável:** Os registros de cancelamento são append-only; a proteção depende da aplicação da trigger `trg_protect_cancellation_audits` no PostgreSQL.
- **Dependência de Provedor de E-mail:** O envio do voucher transacional depende de um provedor configurado; em desenvolvimento, o envio é registrado no console.
- **Funcionalidades Descartadas do MVP:** Streaming de vídeo, emissão fiscal externa (NFC-e), fidelidade por pontos e gestão de bomboniere, conforme detalhado na seção 1.5.

### Premissas

- **Concorrência de Assentos:** A trava pessimista `SELECT FOR UPDATE`, a ordenação prévia dos IDs de assento e a checagem Just-in-Time impedem, por design, conflitos de assentos entre clientes web e atendentes físicos.
- **Antecedência Mínima:** As reservas online realizadas com menos de 1 hora de antecedência em relação ao início da sessão são bloqueadas pelo sistema, reservando o inventário restante para o balcão.
- **Expiração Lógica:** As reservas não quitadas presencialmente até 60 minutos antes do início do filme deixam de ser confirmáveis e seus assentos passam a ser elegíveis para reaproveitamento. A expiração é lógica/Just-in-Time, sem job de varredura automática.
- **Contexto de Tenant:** O tenant é resolvido a partir da sessão autenticada e todas as operações de dados são filtradas por `tenant_id`.
