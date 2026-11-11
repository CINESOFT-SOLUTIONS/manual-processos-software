---
kind: especificacao_requisitos
feature_id: F-CINEDOOM-MVP
title: "CineDoom — Especificação de Requisitos, Regras de Negócio, Histórias de Usuário e Critérios de Aceite"
norma_referencia: "ABNT NBR ISO/IEC/IEEE 12207:2021 (Seção 6.4.1 e 6.4.2)"
---

# Especificação de Requisitos do Sistema — CineDoom (SRS)

Este documento consolida formalmente a **Engenharia de Requisitos** da plataforma **CineDoom** (SaaS B2B2C de Bilheteria, Retaguarda Gerencial e Portal do Cliente), estruturada em conformidade com a norma **ABNT NBR ISO/IEC/IEEE 12207:2021 (Seção 6.4 — Processos Técnicos)** e com as diretrizes da disciplina de Processos de Engenharia de Software (INF0449 — UFG).

---

## Padronização Terminológica e Convenção de Identificadores Únicos

Para eliminar ambiguidades e conflitos terminológicos entre a documentação do Manual de Processos e os artefatos de código/testes, toda a especificação adota siglas padronizadas em **língua portuguesa**:

| Sigla Padrão | Termo Oficial em Português | Equivalência em Código/Testes | Finalidade |
| :---: | :--- | :---: | :--- |
| **`STK-XX`** | Stakeholder (Parte Interessada) | — | Identifica atores, órgãos reguladores e partes afetadas pelo sistema (Seção 5.1.4). |
| **`NEC-XX`** | Necessidade Elicitada | — | Declara o problema ou expectativa capturada na elicitação junto aos stakeholders (Seção 5.1.4). |
| **`HU-XX`** | História de Usuário | `US-X` (*User Story*) | Descreve a funcionalidade na perspectiva do usuário final (*Como... Quero... Para que...*). |
| **`RF-XX`** | Requisito Funcional | `RF-XX` | Especifica um comportamento ou função obrigatória do software (Seção 5.1.1). |
| **`RNF-XX`** | Requisito Não Funcional | `RNF-XX` / `NFR` | Define atributos de qualidade, metas de desempenho, segurança e limites técnicos (Seção 5.1.1). |
| **`RN-XX`** | Regra de Negócio | `RN-XX` | Determina políticas operacionais, cálculos, prazos e restrições de domínio cinematográfico. |
| **`CA-XX`** | Critério de Aceite | `AC-X` (*Acceptance Criteria*) | Condição mensurável e verificável (*Dado que / Quando / Então*) para homologação (Seção 5.1.3). |
| **`RES-XX`** | Restrição Técnica / Escopo | `RES-XX` | Limitações tecnológicas, operacionais, orçamentárias e exclusões explícitas de escopo (Seção 5.1.1). |
| **`CT-XX`** | Caso de Teste | `TC-X` (*Test Case*) | Cenário automatizado na suíte Vitest que verifica um Critério de Aceite (Seção 5.3.3 / 5.4.3). |

---

## 1. Visão Geral do Sistema (Conceito de Operação — CONOPS)

* **O Quê (Escopo Funcional):** Plataforma SaaS *multi-tenant* para cinemas independentes e redes regionais composta por três módulos integrados:
  1. **Retaguarda do Gerente (Back-Office):** Gestão do catálogo de filmes, configuração de salas e matrizes de assentos, agendamento de sessões sem colisão de horários, controle de operadores e painel de ocupação em tempo real.
  2. **Bilheteria do Atendente (PDV Presencial):** Venda presencial de ingressos com trava atômica anti-*double-booking*, cancelamento auditável imutável e baixa presencial de reservas feitas na web.
  3. **Portal Público do Cliente (Autosserviço Web):** Consulta pública de programação, cadastro e login de espectadores com consentimento LGPD, reserva antecipada de poltronas com trava de concorrência, recebimento de comprovante (*voucher*) por e-mail transacional e cancelamento voluntário web.
* **Como (Arquitetura Técnica):** Monólito modular desenvolvido em **Next.js 14 (App Router)** + **TypeScript** + **Tailwind CSS**, com persistência relacional em **PostgreSQL (Supabase)** via **Prisma ORM**. A concorrência de assentos é controlada por bloqueio pessimista (`SELECT ... FOR UPDATE`) aliado à avaliação de expiração *Just-in-Time* (60 minutos antes da sessão). O isolamento entre redes de cinema é imposto por extensão do Prisma Client (`tenant_id`), a proteção de CPF utiliza criptografia em dupla camada (`HMAC-SHA256` + `AES-256-GCM`) e a observabilidade de retenção legal (365 dias) opera via *Log Drain* na **Axiom**.

---

## 2. Registro de Stakeholders e Necessidades Elicitadas (Seção 5.1.4)

### 2.1 Catálogo de Stakeholders (`STK-01` a `STK-05`)

| ID | Stakeholder | Categoria | Papel / Interesse no Sistema | Técnica de Elicitação Aplicada |
| :---: | :--- | :---: | :--- | :--- |
| **`STK-01`** | **Gerente de Cinema** | Operacional / Decisor | Administrar a grade de filmes, salas, sessões, equipe de bilheteria e acompanhar a taxa de ocupação. | Entrevistas estruturadas e workshops de fluxo operacional. |
| **`STK-02`** | **Atendente de Bilheteria** | Operacional | Realizar vendas rápidas no balcão, dar baixa em reservas web e efetuar cancelamentos sem erros de poltrona. | Observação direta do ambiente de guichê e prototipação de tela. |
| **`STK-03`** | **Cliente / Espectador** | Usuário Final | Consultar horários de filmes, reservar lugares antecipadamente pela internet e pagar presencialmente no cinema. | Prototipação navegável e análise de jornada do consumidor. |
| **`STK-04`** | **Proprietário / Rede Exibidora (Tenant)** | Patrocinador / Negócio | Reduzir custos com taxas de bilheteria terceirizada, eliminar *overbooking* e manter isolamento dos seus dados comerciais. | Análise de viabilidade de negócio e entrevistas executivas. |
| **`STK-05`** | **Órgãos Reguladores (ANPD / PROCON)** | Regulatório / Legal | Assegurar conformidade com a LGPD (Lei nº 13.709/2018), Marco Civil da Internet e Código de Defesa do Consumidor (CDC). | Análise documental de legislação e normas jurídicas. |

### 2.2 Necessidades Elicitadas (`NEC-01` a `NEC-08`)

| ID | Stakeholder Origem | Necessidade Capturada na Elicitação | Requisitos Derivados |
| :---: | :---: | :--- | :--- |
| **`NEC-01`** | `STK-02`, `STK-03`, `STK-04` | Eliminar completamente a venda ou reserva duplicada do mesmo assento em horários de pico (*double-booking*). | `RF-07`, `RF-13`, `RNF-02`, `RN-01` |
| **`NEC-02`** | `STK-01`, `STK-04` | Ter autonomia para cadastrar filmes, configurar o mapa de poltronas das salas e montar a grade de sessões sem planilhas. | `RF-03`, `RF-04`, `RF-05`, `RN-05`, `RN-06` |
| **`NEC-03`** | `STK-02`, `STK-03` | Visualizar em tempo real no mapa de assentos quais poltronas estão livres, reservadas ou vendidas. | `RF-06`, `RNF-01`, `RN-02` |
| **`NEC-04`** | `STK-01`, `STK-04` | Rastrear quem realizou cada cancelamento de ingresso e o respectivo motivo, impedindo fraudes de caixa no guichê. | `RF-08`, `RN-07` |
| **`NEC-05`** | `STK-03` | Garantir poltronas pela internet com antecedência e pagar diretamente no balcão do cinema sem taxa de conveniência online. | `RF-12`, `RF-13`, `RF-15`, `RF-17`, `RN-03` |
| **`NEC-06`** | `STK-01`, `STK-04` | Impedir que reservas online não comparecidas (*no-show*) bloqueiem assentos até o início do filme e gerem prejuízo. | `RF-16`, `RF-18`, `RN-04` |
| **`NEC-07`** | `STK-01` | Acompanhar em tempo real a lotação de cada sessão e controlar os acessos dos operadores de bilheteria da sua unidade. | `RF-01`, `RF-02`, `RF-10`, `RN-08`, `RN-09` |
| **`NEC-08`** | `STK-04`, `STK-05` | Proteger os dados pessoais (CPF, nome, e-mail) dos espectadores segundo a LGPD e isolar os dados entre diferentes cinemas. | `RF-09`, `RF-11`, `RF-14`, `RNF-03`, `RN-10`, `RN-11`, `RN-12` |

---

## 3. Histórias de Usuário (`HU-01` a `HU-11`)

As Histórias de Usuário descrevem os fluxos sob a ótica de valor para cada ator do sistema:

* **`HU-01` (equiv. `US-1`) — Venda Presencial de Ingresso na Bilheteria:**
  * **Como** Atendente (`STK-02`), **quero** selecionar um assento disponível no mapa visual e registrar a venda do ingresso vinculando nome, CPF e e-mail do comprador, **para que** a transação seja concluída sem risco de *double-booking* e o espectador saia com seu lugar garantido.
  * *Requisitos vinculados:* `RF-06`, `RF-07`, `RF-09` | *Regras:* `RN-01`, `RN-10` | *Critérios:* `CA-01`, `CA-06`.

* **`HU-02` (equiv. `US-2`) — Cancelamento Auditável de Ingresso:**
  * **Como** Atendente (`STK-02`), **quero** cancelar um ingresso vendido informando obrigatoriamente o motivo do cancelamento vinculado ao meu usuário, **para que** a operação fique gravada de forma imutável para auditoria financeira e o assento volte a ficar disponível imediatamente.
  * *Requisitos vinculados:* `RF-08`, `RF-11` | *Regras:* `RN-07` | *Critérios:* `CA-03`.

* **`HU-03` (equiv. `US-3`) — Monitoramento de Ocupação em Tempo Real:**
  * **Como** Gerente (`STK-01`), **quero** visualizar em tempo real o painel de ocupação de todas as sessões do dia com o percentual de assentos vendidos e reservados, **para que** eu possa tomar decisões operacionais rápidas em dias de estreia.
  * *Requisitos vinculados:* `RF-10` | *Regras:* `RN-08`, `RN-12` | *Critérios:* `CA-07`.

* **`HU-04` (equiv. `US-4`) — Gestão de Filmes, Salas e Grade de Sessões:**
  * **Como** Gerente (`STK-01`), **quero** cadastrar e manter filmes, salas com layout matricial de assentos e sessões cinematográficas com data, horário, sala e preço, **para que** o sistema reflita a programação oficial do cinema sem conflitos de agenda.
  * *Requisitos vinculados:* `RF-03`, `RF-04`, `RF-05` | *Regras:* `RN-05`, `RN-06` | *Critérios:* `CA-08`.

* **`HU-05` (equiv. `US-5`) — Mapa Interativo de Assentos em Tempo Real:**
  * **Como** Atendente ou Cliente (`STK-02`, `STK-03`), **quero** visualizar o mapa de assentos de uma sessão com atualização automática a cada 2 segundos, **para que** eu receba feedback visual imediato sobre poltronas recém-vendidas ou reservadas por outros usuários.
  * *Requisitos vinculados:* `RF-06` | *Regras:* `RN-02`, `RN-04` | *Critérios:* `CA-02`.

* **`HU-06` (equiv. `US-6`) — Administração de Contas de Atendentes:**
  * **Como** Gerente (`STK-01`), **quero** criar e gerenciar contas de Atendente vinculadas exclusivamente ao meu cinema (*tenant*) com permissões restritas ao guichê, **para que** haja controle de acesso granular e rastreabilidade individual por operador.
  * *Requisitos vinculados:* `RF-01`, `RF-02` | *Regras:* `RN-08`, `RN-09` | *Critérios:* `CA-05`.

* **`HU-07` (equiv. `US-7`) — Cadastro e Autenticação do Cliente no Portal:**
  * **Como** Cliente (`STK-03`), **quero** me cadastrar e realizar login no Portal do Cliente informando meus dados pessoais e consentimento explícito da LGPD, **para que** eu tenha acesso seguro ao meu painel de reservas e histórico de ingressos.
  * *Requisitos vinculados:* `RF-01`, `RF-09`, `RF-14` | *Regras:* `RN-10`, `RN-11` | *Critérios:* `CA-06`, `CA-10`.

* **`HU-08` (equiv. `US-8`) — Consulta de Programação e Reserva Online de Assentos:**
  * **Como** Cliente (`STK-03`), **quero** consultar a programação de filmes e sessões e reservar assentos disponíveis no mapa interativo gerando um código localizador único (ex.: `CD-8942`), **para que** eu garanta minhas poltronas com antecedência para pagamento presencial.
  * *Requisitos vinculados:* `RF-12`, `RF-13` | *Regras:* `RN-01`, `RN-03` | *Critérios:* `CA-09`.

* **`HU-09` (equiv. `US-9`) — Emissão de Comprovante (Voucher) e E-mail Transacional:**
  * **Como** Cliente (`STK-03`), **quero** visualizar na tela e receber por e-mail o comprovante da minha reserva contendo código localizador, sala, assentos e horário limite para pagamento no balcão, **para que** eu saiba exatamente como retirar meus ingressos.
  * *Requisitos vinculados:* `RF-15` | *Regras:* `RN-03`, `RN-04` | *Critérios:* `CA-11`.

* **`HU-10` (equiv. `US-10`) — Cancelamento Voluntário de Reserva pelo Cliente:**
  * **Como** Cliente (`STK-03`), **quero** acessar a área *"Minhas Reservas"* no portal e cancelar uma reserva pendente antes do prazo limite, **para que** os assentos sejam liberados imediatamente caso eu desista de comparecer.
  * *Requisitos vinculados:* `RF-16` | *Regras:* `RN-04` | *Critérios:* `CA-12`.

* **`HU-11` (equiv. `US-11`) — Localização e Baixa Presencial de Reserva no Balcão:**
  * **Como** Atendente (`STK-02`), **quero** buscar reservas ativas pelo código localizador ou pelo CPF do cliente na bilheteria e registrar o pagamento presencial, **para que** a reserva seja convertida em venda confirmada (`SOLD`) com emissão do ingresso.
  * *Requisitos vinculados:* `RF-17`, `RF-18` | *Regras:* `RN-03`, `RN-04` | *Critérios:* `CA-13`, `CA-14`.

---

## 4. Requisitos Funcionais do Sistema (`RF-01` a `RF-18`) — Seção 5.1.1

Os Requisitos Funcionais estão numerados de `RF-01` a `RF-18` em estrita paridade com o Capítulo 1 (Seção 1.5) e o Capítulo 5 (Seção 5.1.1) do Manual de Processos:

| ID | Nome do Requisito | Módulo | Descrição Funcional Detalhada | Prioridade (MoSCoW) | Regras Associadas | Histórias / Critérios |
| :---: | :--- | :---: | :--- | :---: | :---: | :---: |
| **`RF-01`** | Autenticar usuário por perfil (RBAC) | Auth / Transversal | O sistema deve autenticar usuários via credenciais (e-mail e senha com hash `bcrypt`) e controlar o acesso às rotas segundo os perfis `GERENTE`, `ATENDENTE` e `CLIENTE`. | *Must Have* | `RN-08`, `RN-09` | `HU-06`, `HU-07` / `CA-05`, `CA-10` |
| **`RF-02`** | Gerenciar usuários e operadores de guichê | Retaguarda (Gerente) | O sistema deve permitir ao Gerente criar, listar, editar e inativar contas de operadores com perfil `ATENDENTE` vinculadas ao seu respectivo cinema (*tenant*). | *Must Have* | `RN-08`, `RN-09`, `RN-12` | `HU-06` / `CA-05` |
| **`RF-03`** | Cadastrar e gerenciar acervo de filmes | Retaguarda (Gerente) | O sistema deve permitir ao Gerente cadastrar, editar, listar e remover filmes contendo título, sinopse, diretor, gênero, duração em minutos, classificação indicativa e URL do pôster. | *Must Have* | `RN-05`, `RN-12` | `HU-04` / `CA-08` |
| **`RF-04`** | Cadastrar e gerenciar salas e layouts de assentos | Retaguarda (Gerente) | O sistema deve permitir ao Gerente cadastrar salas de exibição definindo nome, tipo de experiência (Clássica, VIP, IMAX) e dimensões matriciais (fileiras e colunas), gerando automaticamente os assentos físicos da sala. | *Must Have* | `RN-06`, `RN-12` | `HU-04` / `CA-08` |
| **`RF-05`** | Agendar e publicar sessões cinematográficas | Retaguarda (Gerente) | O sistema deve permitir ao Gerente criar sessões vinculando um filme, uma sala, data/hora de início e preço do ingresso, pré-populando os registros de assentos da sessão (`SessionSeat`). | *Must Have* | `RN-05`, `RN-06`, `RN-12` | `HU-04` / `CA-08` |
| **`RF-06`** | Consultar disponibilidade de assentos com polling de 2s | Bilheteria & Portal | O sistema deve exibir o mapa bidimensional de assentos da sessão e atualizar seu estado (`AVAILABLE`, `RESERVED`, `SOLD`, `BLOCKED`) automaticamente a cada 2 segundos via *polling* HTTP. | *Must Have* | `RN-02`, `RN-04` | `HU-01`, `HU-05` / `CA-02`, `CA-14` |
| **`RF-07`** | Registrar venda de ingresso presencial com trava ACID | Bilheteria (Atendente) | O sistema deve processar a venda presencial de um ou mais assentos no balcão utilizando transação atômica com trava pessimista (`SELECT FOR UPDATE`), alterando o status para `SOLD` e emitindo o ingresso. | *Must Have* | `RN-01`, `RN-10` | `HU-01` / `CA-01` |
| **`RF-08`** | Cancelar ingresso e liberar assento com auditoria imutável | Bilheteria (Atendente) | O sistema deve permitir o cancelamento de um ingresso vendido antes do início da sessão, exigindo justificativa textual, gravando registro imutável na tabela de auditoria e revertendo o assento para `AVAILABLE`. | *Must Have* | `RN-07`, `RN-12` | `HU-02` / `CA-03` |
| **`RF-09`** | Proteger dados pessoais de compradores conforme a LGPD | Segurança / LGPD | O sistema deve proteger os dados de compradores e clientes aplicando hash determinístico `HMAC-SHA256` ao CPF para buscas exatas, cifragem autenticada `AES-256-GCM` para armazenamento e função de anonimização (*Art. 18 LGPD*). | *Must Have* | `RN-10`, `RN-11` | `HU-01`, `HU-07` / `CA-06` |
| **`RF-10`** | Monitorar indicadores e taxas de ocupação em tempo real | Retaguarda (Gerente) | O sistema deve disponibilizar um dashboard gerencial exibindo, para cada sessão do dia corrente, a capacidade total da sala, total de assentos vendidos/reservados e percentual de lotação. | *Must Have* | `RN-08`, `RN-12` | `HU-03` / `CA-07` |
| **`RF-11`** | Registrar trilha de auditoria e retenção legal (Axiom) | Observabilidade | O sistema deve emitir logs estruturados em JSON para todas as operações críticas (vendas, reservas, cancelamentos, falhas de autenticação) com envio via *Log Drain* para retenção de 365 dias. | *Must Have* | `RN-07`, `RN-11` | `HU-02`, `HU-09` / `CA-03`, `CA-11` |
| **`RF-12`** | Consultar programação e sessões no Portal do Cliente | Portal do Cliente | O sistema deve apresentar publicamente o catálogo de filmes em cartaz com filtros por data (7 dias da semana), formato de sala (IMAX, VIP, Clássica) e busca textual por título/sinopse. | *Must Have* | `RN-02`, `RN-04` | `HU-08` / `CA-02`, `CA-09` |
| **`RF-13`** | Reservar assento online com trava atômica temporária | Portal do Cliente | O sistema deve permitir ao espectador reservar assentos disponíveis na sessão com trava atômica (`SELECT FOR UPDATE`), atribuindo status `RESERVED` e gerando código localizador único (`CD-XXXX`). | *Must Have* | `RN-01`, `RN-03`, `RN-04` | `HU-08` / `CA-09` |
| **`RF-14`** | Cadastrar e autenticar cliente com consentimento LGPD | Portal do Cliente | O sistema deve permitir o autocadastro de espectadores no portal com validação de CPF, e-mail, senha segura e coleta obrigatória do termo de consentimento LGPD com carimbo de tempo (*timestamp*). | *Must Have* | `RN-09`, `RN-10` | `HU-07` / `CA-06`, `CA-10` |
| **`RF-15`** | Despachar voucher de reserva via e-mail transacional | Notificações / Portal | O sistema deve enviar automaticamente um e-mail transacional após a confirmação da reserva contendo o código localizador, dados da sessão, poltronas e horário limite para pagamento presencial, registrando `email_sent_at`. | *Must Have* | `RN-03`, `RN-04` | `HU-09` / `CA-11` |
| **`RF-16`** | Cancelar reserva pelo próprio cliente via web | Portal do Cliente | O sistema deve permitir ao cliente autenticado consultar a área *"Minhas Reservas"* e cancelar voluntariamente reservas pendentes (`PENDING`), liberando os assentos para `AVAILABLE` imediatamente. | *Must Have* | `RN-04` | `HU-10` / `CA-12` |
| **`RF-17`** | Localizar e dar baixa em reserva presencial no balcão | Bilheteria (Atendente) | O sistema deve permitir ao Atendente localizar reservas ativas pelo código localizador ou CPF do cliente e confirmar o pagamento presencial, convertendo a reserva em ingresso vendido (`SOLD`). | *Must Have* | `RN-03`, `RN-04` | `HU-11` / `CA-13` |
| **`RF-18`** | Expirar reservas não pagas a 1 hora do início da sessão | Bilheteria & Portal | O sistema deve expirar dinamicamente (*Just-in-Time*) reservas pendentes cujo pagamento presencial não tenha sido confirmado até 60 minutos antes do início da sessão, liberando os assentos para venda no balcão. | *Must Have* | `RN-03`, `RN-04` | `HU-11` / `CA-14` |

---

## 5. Requisitos Não Funcionais (`RNF-01` a `RNF-06`) — Seção 5.1.1

Os Requisitos Não Funcionais seguem a taxonomia de qualidade de produto da norma **ISO/IEC 25010**, com métricas objetivas e verificáveis (critério SMART):

| ID | Atributo de Qualidade (ISO 25010) | Título do Requisito | Especificação Técnica e Restrição de Qualidade | Meta / Métrica Verificável |
| :---: | :--- | :--- | :--- | :--- |
| **`RNF-01`** | Eficiência de Desempenho (*Performance Efficiency*) | Latência de Resposta e Atualização do Mapa | Os endpoints críticos de venda (`/api/vendas`), reserva (`/api/portal/reservas`) e consulta de mapa de assentos (`/api/sessoes/[id]/assentos`) devem responder com baixa latência sobre conexão *pooled* no Supabase (*Supavisor* porta 6543) sob carga de até 20 req/s. | Tempo de resposta $p95 < 800\text{ms}$ e $p99 < 1500\text{ms}$; ciclo de *polling* visual a cada $2000\text{ms}$. |
| **`RNF-02`** | Confiabilidade (*Reliability*) | Consistência Transacional ACID Anti-Colisão | O mecanismo de controle de concorrência no banco PostgreSQL deve impedir matematicamente vendas ou reservas duplicadas sobre o mesmo `SessionSeat` em disputas simultâneas entre múltiplos terminais de balcão e clientes web. | **0 ocorrências** de *double-booking* em bateria de estresse com **50 threads simultâneas** (10.000 tentativas concorrentes). |
| **`RNF-03`** | Segurança e Privacidade (*Security*) | Isolamento Multi-Tenant e Criptografia LGPD | Nenhuma consulta ou mutação pode vazar registros entre diferentes cinemas (*tenants*) ou expor CPFs em texto claro no banco de dados ou em logs de aplicação. Senhas devem utilizar `bcrypt` (custo $\ge 10$). | **0 vazamentos** *cross-tenant* ou *cross-user* em suíte de 500 testes de segurança; 100% dos CPFs cifrados com `AES-256-GCM`. |
| **`RNF-04`** | Manutenibilidade (*Maintainability*) | Modularidade Arquitetural e Qualidade de Código | O código-fonte deve seguir arquitetura de Monólito Modular com separação em camadas (*Controller-Service-Repository*) e fatias de domínio (`catalogo`, `bilheteria`, `reserva`, `ocupacao`, `titulares`, `usuarios`), com tipagem estrita TypeScript. | **0 ciclos de dependência** reportados pelo ESLint; cobertura de testes automatizados $\ge 80\%$ nas regras de negócio. |
| **`RNF-05`** | Compatibilidade e Usabilidade (*Compatibility & Usability*) | Responsividade Web e Compatibilidade Cross-Browser | As interfaces do Portal do Cliente e da Bilheteria devem operar sem degradação visual ou funcional nos navegadores modernos e adaptar seu layout para dispositivos móveis e terminais desktop de guichê. | **100% dos fluxos principais** operacionais em Chromium, Firefox e Safari (desktop e mobile responsivo). |
| **`RNF-06`** | Portabilidade (*Portability*) | Reprodutibilidade do Ambiente e Resiliência | O ambiente completo de desenvolvimento e demonstração deve ser inicializável com comando único (`pnpm dev`), contando com *fallback* resiliente em memória caso o banco local não esteja acessível. | Tempo de configuração inicial (*setup*) $< 30\text{ minutos}$ após clonagem do repositório. |

---

## 6. Regras de Negócio (`RN-01` a `RN-12`)

As Regras de Negócio definem as políticas de domínio cinematográfico, restrições legais e invariantes operacionais que governam os requisitos funcionais:

| ID | Nome da Regra de Negócio | Especificação Normativa da Regra | Requisitos Vinculados | Critérios de Aceite |
| :---: | :--- | :--- | :---: | :---: |
| **`RN-01`** | Exclusividade e Atomicidade de Assento por Sessão | Cada poltrona de uma sessão (`SessionSeat`) pode estar associada a no máximo um ingresso ativo (`SOLD`) ou uma reserva ativa (`RESERVED`). Em caso de disputa concorrente pelo mesmo assento, apenas a primeira transação que adquirir o bloqueio `SELECT FOR UPDATE` será efetivada, retornando erro `HTTP 409 Conflict` para as demais. | `RF-07`, `RF-13`, `RNF-02` | `CA-01`, `CA-09` |
| **`RN-02`** | Máquina de Estados do Assento na Sessão | Um assento em uma sessão transita exclusivamente pelos estados: `AVAILABLE` (livre para venda ou reserva), `RESERVED` (bloqueado temporariamente por reserva web pendente), `SOLD` (vendido definitivamente na bilheteria ou após baixa de reserva) e `BLOCKED` (interditado para manutenção). | `RF-06`, `RF-07`, `RF-08`, `RF-13`, `RF-16`, `RF-17`, `RF-18` | `CA-01`, `CA-02`, `CA-09`, `CA-12`, `CA-13`, `CA-14` |
| **`RN-03`** | Antecedência Mínima para Reserva Online (60 Minutos) | Reservas online através do Portal do Cliente só são permitidas quando faltarem **60 minutos ou mais** para o horário de início da sessão (`startsAt`). Quando faltar menos de 60 minutos, a venda ocorre exclusivamente de forma presencial na bilheteria. | `RF-13`, `RF-15`, `RF-17` | `CA-09`, `CA-11`, `CA-13` |
| **`RN-04`** | Expiração Automática Just-in-Time de Reservas Não Pagas | Toda reserva online com status `PENDING` deve ter seu pagamento presencial confirmado na bilheteria até **60 minutos antes do início da sessão**. Caso não seja confirmada até esse limite, a reserva passa automaticamente ao estado `EXPIRED` em tempo de execução (*Just-in-Time*) e suas poltronas voltam imediatamente ao estado `AVAILABLE`. | `RF-06`, `RF-16`, `RF-17`, `RF-18` | `CA-12`, `CA-13`, `CA-14` |
| **`RN-05`** | Integridade do Catálogo e Proteção contra Exclusão Indevida | Um filme só pode ser cadastrado com título e duração positiva ($\ge 1\text{ min}$). Não é permitido excluir um filme ou uma sala que possua sessões cinematográficas vinculadas, nem excluir uma sessão que possua ingressos vendidos. | `RF-03`, `RF-04`, `RF-05` | `CA-08` |
| **`RN-06`** | Prevenção de Conflito de Horários de Sala e Pré-População | Duas sessões não podem ser agendadas na mesma sala se houver sobreposição entre seus intervalos de exibição (considerando `startsAt` + duração do filme). Ao criar uma sessão, todos os assentos da sala devem ser pré-populados na tabela `session_seats` com status inicial `AVAILABLE`. | `RF-04`, `RF-05` | `CA-08` |
| **`RN-07`** | Auditoria Imutável de Cancelamento (Append-Only) | Nenhum ingresso vendido (`SOLD`) pode ser cancelado sem o preenchimento de um motivo válido ($\ge 5\text{ caracteres}$) e identificação do operador executante. O registro em `auditoria_cancelamentos` é protegido por *trigger* PostgreSQL que bloqueia operações de `UPDATE` e `DELETE`. | `RF-08`, `RF-11` | `CA-03` |
| **`RN-08`** | Controle de Acesso Baseado em Papéis (RBAC) | Operações de configuração de retaguarda (gestão de filmes, salas, sessões, operadores, anonimização LGPD e painel gerencial de ocupação) são restritas ao perfil `GERENTE`. O perfil `ATENDENTE` opera exclusivamente nas rotas de bilheteria e baixa de reservas, e o perfil `CLIENTE` opera exclusivamente nas rotas do portal público e de suas próprias reservas. | `RF-01`, `RF-02`, `RF-10` | `CA-05`, `CA-07` |
| **`RN-09`** | Segurança de Credenciais e Proteção contra Auto-Desativação | Todas as senhas de usuários devem possuir no mínimo 6 caracteres e ser persistidas exclusivamente sob hash `bcrypt` (custo 12). Um usuário com perfil `GERENTE` não pode inativar a própria conta autenticada (*Self-Inactivation Prevention*), e operadores inativados perdem acesso imediatamente. | `RF-01`, `RF-02`, `RF-14` | `CA-05`, `CA-10` |
| **`RN-10`** | Criptografia em Dupla Camada e Consentimento LGPD | Para todo comprador ou cliente cadastrado, é obrigatório registrar o aceite explícito de tratamento de dados (`lgpd_consent = true` e `consent_at`). O CPF jamais é salvo em texto claro: armazena-se um *blind index* `HMAC-SHA256` para busca exata e o valor cifrado em `AES-256-GCM` para exibição autorizada. | `RF-07`, `RF-09`, `RF-14`, `RNF-03` | `CA-06`, `CA-10` |
| **`RN-11`** | Anonimização In-Place e Retenção Fiscal (Conflito LGPD vs. CDC) | Quando um titular solicita exclusão/anonimização de dados (Art. 18 da LGPD), o sistema substitui nome, e-mail e CPF por hashes irreversíveis, mantendo os registros financeiros de `Ticket` e `CancellationAudit` íntegros para cumprimento de obrigação legal e fiscal (Art. 16, I da LGPD e CDC). | `RF-09`, `RF-11`, `RNF-03` | `CA-06` |
| **`RN-12`** | Isolamento Estrito Multi-Tenant por Linha (Row-Level) | Toda entidade de negócio (`Film`, `Room`, `Seat`, `Session`, `SessionSeat`, `Buyer`, `Reservation`, `Ticket`, `CancellationAudit`) pertence obrigatoriamente a um único `tenant_id`. Toda query executada sem contexto de `tenant_id` válido ou tentando acessar outro *tenant* é bloqueada na camada de dados. | `RF-02` a `RF-10`, `RNF-03` | `CA-04`, `CA-07` |

---

## 7. Critérios de Aceite (`CA-01` a `CA-14`) — Seção 5.1.3

Os Critérios de Aceite (anteriormente referenciados nos testes como `AC-1` a `AC-14`) especificam as condições formais de verificação em formato **Dado que / Quando / Então**:

* **`CA-01` (equiv. `AC-1`) — Venda Atômica sem Double-Booking:**
  * **Dado que** dois terminais tentam vender o mesmo assento na mesma sessão simultaneamente, **quando** ambas as requisições de venda são processadas em paralelo, **então** apenas uma deve ter sucesso (`HTTP 201`, status `SOLD`) e a outra deve receber erro de conflito (`HTTP 409`) sem corrupção de estado, garantido por `SELECT FOR UPDATE` em transação Prisma.
  * *Rastreabilidade:* `RF-07`, `RN-01`, `RNF-02` | `@test:tests/unit/venda-atomica.test.ts`

* **`CA-02` (equiv. `AC-2`) — Atualização do Mapa de Assentos em até 2 Segundos:**
  * **Dado que** o mapa de assentos de uma sessão está aberto na bilheteria ou no portal, **quando** ocorre uma venda, reserva ou cancelamento de poltrona, **então** o mapa deve refletir a mudança de disponibilidade em no máximo 2 segundos via *polling* do endpoint `GET /api/sessoes/[id]/assentos` a cada `2000ms`.
  * *Rastreabilidade:* `RF-06`, `RN-02`, `RNF-01` | `@test:tests/unit/session-seats-polling.test.ts`

* **`CA-03` (equiv. `AC-3`) — Trilha Imutável de Auditoria de Cancelamento:**
  * **Dado que** um ingresso vendido precisa ser cancelado pelo atendente, **quando** o cancelamento é submetido com o motivo, **então** o sistema deve persistir um registro imutável na tabela `auditoria_cancelamentos` contendo `ticket_id`, `user_id` executante, `timestamp` UTC, `tenant_id` e motivo informado, antes de liberar o assento para `AVAILABLE`.
  * *Rastreabilidade:* `RF-08`, `RF-11`, `RN-07` | `@test:tests/unit/cancelamento-auditavel.test.ts`

* **`CA-04` (equiv. `AC-4`) — Isolamento Multi-Tenant Obrigatório na Camada de Dados:**
  * **Dado que** múltiplas redes de cinema utilizam a plataforma, **quando** qualquer query ao banco de dados acessa entidades de negócio (filmes, salas, sessões, ingressos, compradores, reservas), **então** o middleware do Prisma Client deve injetar obrigatoriamente o filtro `WHERE tenant_id = :tenantId`, bloqueando vazamento de dados entre *tenants*.
  * *Rastreabilidade:* `RNF-03`, `RN-12` | `@test:tests/unit/tenancy-isolation.test.ts`

* **`CA-05` (equiv. `AC-5`) — Restrição de Acesso por Papel (RBAC):**
  * **Dado que** um usuário está autenticado com perfil `ATENDENTE` ou `CLIENTE`, **quando** ele tenta acessar rotas administrativas do Back-Office (gestão de filmes, salas, sessões ou operadores), **então** o sistema deve negar a operação retornando `HTTP 403 Forbidden`, permitindo acesso total apenas ao perfil `GERENTE` do respectivo *tenant*.
  * *Rastreabilidade:* `RF-01`, `RF-02`, `RN-08`, `RN-09` | `@test:tests/unit/auth-rbac.test.ts`

* **`CA-06` (equiv. `AC-6`) — Proteção Criptográfica de CPF e Consentimento LGPD:**
  * **Dado que** um comprador ou cliente é registrado no ato da compra ou reserva, **quando** seus dados pessoais são persistidos, **então** o sistema deve gravar nome, e-mail, CPF com hash `HMAC-SHA256` para busca e valor cifrado `AES-256-GCM` para exibição, além do consentimento LGPD com `timestamp` UTC.
  * *Rastreabilidade:* `RF-09`, `RN-10`, `RN-11`, `RNF-03` | `@test:tests/unit/cryptoservice.test.ts`

* **`CA-07` (equiv. `AC-7`) — Cálculo e Isolamento do Painel Gerencial de Ocupação:**
  * **Dado que** o Gerente acessa o painel de ocupação do dia, **quando** os indicadores são carregados, **então** o sistema deve exibir para cada sessão do dia corrente o percentual exato de assentos vendidos e reservados sobre a capacidade total da sala, exibindo exclusivamente dados do `tenant_id` do gerente autenticado.
  * *Rastreabilidade:* `RF-10`, `RN-08`, `RN-12` | `@test:tests/unit/session-seats-polling.test.ts`

* **`CA-08` (equiv. `AC-8`) — Gestão Validada de Catálogo, Salas e Sessões pelo Gerente:**
  * **Dado que** um usuário com perfil `GERENTE` gerencia a programação, **quando** ele cria, edita ou lista filmes, salas com layout de assentos e sessões cinematográficas, **então** o sistema deve validar todos os campos obrigatórios (`HTTP 422` se ausentes), impedir conflitos de horário na mesma sala e pré-popular os assentos da sessão.
  * *Rastreabilidade:* `RF-03`, `RF-04`, `RF-05`, `RN-05`, `RN-06` | `@test:tests/unit/catalog-filmes.test.ts`

* **`CA-09` (equiv. `AC-9`) — Reserva Atômica Online e Validação de Antecedência (60 min):**
  * **Dado que** um espectador solicita uma reserva no Portal do Cliente, **quando** faltam 60 minutos ou mais para a sessão e o assento está `AVAILABLE`, **então** o sistema deve executar transação atômica alterando o assento para `RESERVED` com o `reservation_id` associado, e deve rejeitar a operação caso falte menos de 60 minutos para o início da sessão.
  * *Rastreabilidade:* `RF-12`, `RF-13`, `RN-01`, `RN-02`, `RN-03` | `@test:tests/integration/reserva-atomica.test.ts`

* **`CA-10` (equiv. `AC-10`) — Cadastro Seguro e Autenticação do Cliente Final:**
  * **Dado que** um novo espectador realiza cadastro no Portal do Cliente, **quando** ele submete dados válidos e aceite da LGPD, **então** o sistema deve persistir credenciais seguras (senha com hash `bcrypt`) com perfil `CLIENTE` e dados PII criptografados, habilitando login e sessão autenticada no portal.
  * *Rastreabilidade:* `RF-01`, `RF-14`, `RN-09`, `RN-10` | `@test:tests/unit/users-management.test.ts`

* **`CA-11` (equiv. `AC-11`) — Emissão de Voucher e Disparo de E-mail Transacional:**
  * **Dado que** uma reserva online foi confirmada com sucesso, **quando** a transação é concluída, **então** o sistema deve despachar um e-mail transacional contendo o código identificador único (`CD-XXXX`), data/hora da sessão, sala, assentos e prazo limite para pagamento presencial, gravando o carimbo de tempo em `email_sent_at`.
  * *Rastreabilidade:* `RF-11`, `RF-15`, `RN-03` | `@test:tests/unit/observability-logger.test.ts`

* **`CA-12` (equiv. `AC-12`) — Cancelamento Voluntário de Reserva pelo Espectador:**
  * **Dado que** o cliente autenticado possui uma reserva com status `PENDING`, **quando** ele solicita o cancelamento voluntário na área *"Minhas Reservas"*, **então** o sistema deve atualizar o status da reserva para `CANCELLED` e liberar imediatamente as poltronas associadas para o status `AVAILABLE`.
  * *Rastreabilidade:* `RF-16`, `RN-02`, `RN-04` | `@test:tests/integration/reserva-atomica.test.ts`

* **`CA-13` (equiv. `AC-13`) — Localização e Conversão de Reserva em Venda no Balcão:**
  * **Dado que** um cliente comparece à bilheteria dentro do prazo de validade da reserva, **quando** o atendente localiza a reserva pelo código localizador ou CPF e confirma o pagamento presencial, **então** o sistema deve converter a reserva em ingresso vendido (`SOLD`), gerando o registro de `Ticket` vinculado ao atendente operador.
  * *Rastreabilidade:* `RF-17`, `RN-02`, `RN-03` | `@test:tests/integration/reserva-atomica.test.ts`

* **`CA-14` (equiv. `AC-14`) — Expiração Just-in-Time de Reservas Não Quitadas (60 min):**
  * **Dado que** existe uma reserva com status `PENDING` não paga e faltam menos de 60 minutos para o início da sessão, **quando** o mapa de assentos é consultado ou uma venda de balcão é solicitada, **então** o sistema deve tratar a reserva como expirada (`EXPIRED`) em tempo de execução (*Just-in-Time*), liberando os assentos para venda imediata na bilheteria.
  * *Rastreabilidade:* `RF-06`, `RF-18`, `RN-02`, `RN-04` | `@test:tests/integration/reserva-atomica.test.ts`

---

## 8. Restrições Técnicas e Limites de Escopo (`RES-01` a `RES-06`) — Seção 5.1.1

Itens explicitamente fora do escopo do MVP e restrições arquiteturais do projeto:

* **`RES-01` — Pagamento Presencial Exclusivo (Sem Gateway Online):** O sistema não processa pagamentos eletrônicos online (cartão de crédito/débito ou checkout PIX web no portal); a liquidação financeira das reservas ocorre exclusivamente no balcão físico da bilheteria até 60 minutos antes da sessão.
* **`RES-02` — Sem Integração de Hardware Fiscal (NFC-e / SAT):** O sistema emite comprovantes operacionais e *vouchers* de reserva/ingresso, não integrando módulos de comunicação direta com SEFAZ para emissão de nota fiscal eletrônica ao consumidor.
* **`RES-03` — Aplicação Web Responsiva (Sem App Nativo Mobile):** O acesso de espectadores, atendentes e gerentes ocorre integralmente via navegadores web (desktop e mobile responsivo), sem distribuição de aplicativos nativos nas lojas Google Play ou Apple App Store.
* **`RES-04` — Exclusão de Bomboniere e Estoque de Alimentos:** O escopo restringe-se à gestão de catálogo cinematográfico, salas, sessões, reservas e bilheteria de ingressos, não abrangendo controle de estoque de pipoca, bebidas ou combos.
* **`RES-05` — Sem Distribuição de Mídia Digital ou DRM:** O sistema gerencia metadados e cartazes dos filmes, não realizando *streaming* de vídeo nem gerenciamento de chaves digitais de projetores (KDM/DCP).
* **`RES-06` — Idioma e Localização Única (`pt-BR`):** A plataforma é projetada e localizada exclusivamente em português brasileiro, operando segundo o fuso horário e a legislação nacional (LGPD e CDC).

---

## 9. Matriz de Rastreabilidade Ponta a Ponta (Seção 5.1.2)

A tabela abaixo consolida o vínculo bidirecional completo entre **Stakeholder $\to$ Necessidade $\to$ História de Usuário $\to$ Requisito Funcional $\to$ Regra de Negócio $\to$ Critério de Aceite $\to$ Caso de Teste $\to$ Código/Teste Automatizado**:

| Requisito (`RF`) | Stakeholder (`STK`) | Necessidade (`NEC`) | História (`HU`) | Regra de Negócio (`RN`) | Critério de Aceite (`CA` / `AC`) | Casos de Teste (`CT` / `TC`) | Suíte de Teste Automatizado (`cinedoom-app`) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **`RF-01`** | `STK-01`, `STK-02`, `STK-03` | `NEC-07`, `NEC-08` | `HU-06`, `HU-07` | `RN-08`, `RN-09` | `CA-05`, `CA-10` | `CT-05`, `CT-13`, `CT-20`, `CT-22` | `tests/unit/auth-rbac.test.ts` |
| **`RF-02`** | `STK-01`, `STK-04` | `NEC-07` | `HU-06` | `RN-08`, `RN-09`, `RN-12` | `CA-05` | `CT-05`, `CT-13`, `CT-20`, `CT-22` | `tests/unit/users-management.test.ts` |
| **`RF-03`** | `STK-01`, `STK-04` | `NEC-02` | `HU-04` | `RN-05`, `RN-12` | `CA-04`, `CA-08` | `CT-04`, `CT-08`, `CT-16` | `tests/unit/catalog-filmes.test.ts` |
| **`RF-04`** | `STK-01`, `STK-04` | `NEC-02` | `HU-04` | `RN-06`, `RN-12` | `CA-08` | `CT-08`, `CT-13` | `tests/unit/rooms-layout.test.ts` |
| **`RF-05`** | `STK-01`, `STK-04` | `NEC-02` | `HU-04` | `RN-05`, `RN-06`, `RN-12` | `CA-08` | `CT-08`, `CT-13` | `tests/unit/sessions-prepopulation.test.ts` |
| **`RF-06`** | `STK-02`, `STK-03` | `NEC-03` | `HU-01`, `HU-05` | `RN-02`, `RN-04` | `CA-02` | `CT-02`, `CT-10`, `CT-17` | `tests/unit/session-seats-polling.test.ts` |
| **`RF-07`** | `STK-02`, `STK-04` | `NEC-01` | `HU-01` | `RN-01`, `RN-10` | `CA-01` | `CT-01`, `CT-09` | `tests/unit/venda-atomica.test.ts`, `tests/unit/concurrency-acid-50-threads.test.ts` |
| **`RF-08`** | `STK-01`, `STK-02` | `NEC-04` | `HU-02` | `RN-07`, `RN-12` | `CA-03` | `CT-03`, `CT-11`, `CT-18` | `tests/unit/cancelamento-auditavel.test.ts` |
| **`RF-09`** | `STK-03`, `STK-05` | `NEC-08` | `HU-01`, `HU-07` | `RN-10`, `RN-11` | `CA-06` | `CT-06`, `CT-14` | `tests/unit/cryptoservice.test.ts`, `tests/unit/compliance-anonymization.test.ts` |
| **`RF-10`** | `STK-01`, `STK-04` | `NEC-07` | `HU-03` | `RN-08`, `RN-12` | `CA-07` | `CT-07`, `CT-15` | `tests/unit/session-seats-polling.test.ts`, `tests/unit/security-cross-tenant-suite.test.ts` |
| **`RF-11`** | `STK-04`, `STK-05` | `NEC-04`, `NEC-08` | `HU-02`, `HU-09` | `RN-07`, `RN-11` | `CA-03`, `CA-11` | `CT-03`, `CT-23` | `tests/unit/observability-logger.test.ts` |
| **`RF-12`** | `STK-03` | `NEC-05` | `HU-08` | `RN-02`, `RN-04` | `CA-02`, `CA-09` | `CT-02`, `CT-21` | `tests/unit/film-modal-sessions.test.ts` |
| **`RF-13`** | `STK-03`, `STK-04` | `NEC-01`, `NEC-05` | `HU-08` | `RN-01`, `RN-03`, `RN-04` | `CA-09` | `CT-21` | `tests/integration/reserva-atomica.test.ts` |
| **`RF-14`** | `STK-03`, `STK-05` | `NEC-08` | `HU-07` | `RN-09`, `RN-10` | `CA-06`, `CA-10` | `CT-06`, `CT-22` | `tests/unit/users-management.test.ts` |
| **`RF-15`** | `STK-03` | `NEC-05` | `HU-09` | `RN-03`, `RN-04` | `CA-11` | `CT-23` | `tests/unit/observability-logger.test.ts` |
| **`RF-16`** | `STK-03`, `STK-04` | `NEC-06` | `HU-10` | `RN-04` | `CA-12` | `CT-24` | `tests/integration/reserva-atomica.test.ts` |
| **`RF-17`** | `STK-02`, `STK-03` | `NEC-05` | `HU-11` | `RN-03`, `RN-04` | `CA-13` | `CT-25` | `tests/integration/reserva-atomica.test.ts` |
| **`RF-18`** | `STK-01`, `STK-04` | `NEC-06` | `HU-11` | `RN-03`, `RN-04` | `CA-14` | `CT-26` | `tests/integration/reserva-atomica.test.ts` |
