# Capítulo 6 – Avaliação e melhoria dos processos de software

## 6.1 Referencial e recorte

Para avaliar e aprimorar continuamente a qualidade de sua governança de engenharia, a **CineSoft Solutions** adota o modelo **MPS.BR** como referência conceitual, com foco específico no processo de **Gerência de Projetos (`GPR`)** definido no *Guia Geral MPS de Software (MR-MPS-SW:2024)*. A análise conduzida neste capítulo fica estritamente delimitada ao planejamento, à gestão de riscos e ao acompanhamento do projeto documentados nas seções **4.1** (*Plano de projeto: escopo, cronograma, recursos e entregas*), **4.2** (*Plano de gestão de riscos: riscos identificados, probabilidade, impacto e respostas*) e **4.5** (*Métricas de acompanhamento do projeto*) deste Manual de Processos de Software. As questões avaliadas a seguir constituem adaptações didáticas orientadas à melhoria contínua do processo da equipe, não atribuindo nível formal de maturidade MPS.BR nem atestando conformidade integral com todos os resultados esperados do modelo.

---

## 6.2 Diagnóstico do manual

Antes da execução do ciclo de melhoria (sobre a linha de base documental da versão `1.7` do manual), a equipe realizou uma auditoria interna examinando as seções **4.1, 4.2 e 4.5** frente às quatro questões de diagnóstico. Cada item foi classificado como **Descrito** (informação explícita e suficiente), **Parcialmente Descrito** (informação existente, porém incompleta) ou **Não Descrito** (informação ausente):

**Tabela 44 – Diagnóstico de Avaliação e Maturidade de Processo (Versão 1.7)**

| Pergunta de avaliação | Seção | Situação e evidência (Diagnóstico Inicial — Versão 1.7) |
| :--- | :---: | :--- |
| **1. O escopo e as entregas do projeto estão claros?** | `4.1` | **Parcialmente Descrito.** A seção 4.1 listava uma tabela resumida de 5 incrementos internos, mas não apresentava a Estrutura Analítica do Projeto (EAP/WBS) nem estruturava o ciclo de evolução comercial do produto nas **3 Macroentregas** (`v1.0` MVP, `v2.0` Escala/Pagamentos e `v3.0` Enterprise/Fiscal). |
| **2. As atividades possuem responsáveis e prazos?** | `4.1` | **Parcialmente Descrito.** O cronograma da seção 4.1 apresentava janelas de datas gerais (ex.: *"25/10 a 31/10"*), mas **não atribuía nominalmente os responsáveis diretos** por cada pacote de trabalho/Sprint dentro da própria tabela do plano de projeto, além de misturar tarefas acadêmicas externas ao produto. |
| **3. Os riscos e suas respostas estão definidos?** | `4.2` | **Parcialmente Descrito.** A tabela da seção 4.2 continha 5 itens, porém **não possuía a coluna de Prioridade** (Crítico / Alto / Médio), não explicitava os critérios de classificação/reavaliação e misturava riscos escolares (*"falha de rede na apresentação"*) em vez de focar integralmente nos riscos reais de engenharia e operação do SaaS. |
| **4. Está definido como acompanhar o andamento e tratar atrasos?** | `4.5` e `4.1` | **Não Descrito.** A seção 4.5 listava três indicadores conceituais sem metas numéricas nem valores aferidos, e a seção 4.1 **não definia a rotina de acompanhamento diário/semanal nem o protocolo de ação corretiva** para destravar tarefas atrasadas ou bloqueadas. |

*Fonte: CineSoft Solutions (2026).*

---

## 6.3 Plano de uma melhoria

Com base nas lacunas identificadas no diagnóstico da seção 6.2 — especialmente a ausência de atribuição nominal de responsáveis por entrega/Sprint, a falta de um protocolo claro para monitoramento e tratamento de atrasos e a incompletude da matriz de riscos —, a equipe estruturou e executou o seguinte plano de ação:

**Tabela 45 – Plano de Melhoria de Processo de Software (PMP)**

| Campo do plano | Resposta da equipe (CineSoft Solutions) |
| :--- | :--- |
| **Lacuna e justificativa** | As seções `4.1`, `4.2` e `4.5` careciam de atribuição nominal de responsáveis nos pacotes do cronograma, não definiam a rotina prática para detectar e tratar desvios/atrasos (com metas e limites objetivos) e não classificavam a prioridade dos riscos reais do produto. Isso gerava ambiguidade sobre quem deveria agir quando uma tarefa atrasava no quadro Kanban. |
| **Ação** | Reestruturar integralmente as seções `4.1`, `4.2` e `4.5` para: (1) incorporar a EAP de 3 níveis e o roadmap corporativo nas **3 Macroentregas** com responsáveis nominais e prazos por Sprint; (2) instituir o protocolo formal de acompanhamento e tratamento de desvios (alerta de bloqueio em 48h, limite WIP $\le 2$ e pareamento técnico); (3) adicionar a coluna **Prioridade** e critérios de reavaliação no *Risk Register*; e (4) estabelecer metas quantitativas e resultados aferidos nas métricas de acompanhamento. |
| **Responsável e prazo** | **Responsável:** Kayque Vicente Silva (Gerente de Projeto & QA Lead), com revisão de Gabriel Henrique Lourenço Dias (Tech Lead). **Prazo de conclusão:** 09/11/2026. |
| **Evidência da revisão** | Atualização documental das seções `4.1`, `4.2` e `4.5` no arquivo `manual/capitulos/04-gerenciamento-tecnico.md` (registrada na versão `2.0` do Histórico de Versões) e sincronização dos cards no quadro GitHub Projects v2 (`CINESOFT-SOLUTIONS`). |
| **Resultado esperado** | Eliminar dúvidas sobre a responsabilidade de cada pacote de trabalho, detectar gargalos em menos de 48 horas e garantir 100% de previsibilidade na entrega dos 18 requisitos funcionais da Macroentrega 1 (`v1.0.0`). |

*Fonte: CineSoft Solutions (2026).*

---

## 6.4 Atualização e verificação

A melhoria planejada foi efetivamente aplicada no Capítulo 4 deste manual. O quadro comparativo a seguir confronta diretamente o trecho que constava antes (Versão `1.7`) com a nova redação implementada (Versão `2.0`):

### Quadro Comparativo: Antes vs. Depois da Revisão (Seções 4.1, 4.2 e 4.5)

**Tabela 46 – Quadro Comparativo: Antes vs. Depois da Revisão de Processos**

| Seção / Dimensão | Versão 1.7 (Antes da Melhoria) | Versão 2.0 (Após a Melhoria) |
| :--- | :--- | :--- |
| **Seção 4.1: Escopo e Cronograma** | Cronograma empírico sem divisão formal de entregas e sem responsáveis nominais. | EAP em 3 níveis, 3 Macroentregas definidas e responsáveis nominais por Sprint. |
| **Seção 4.1: Tratamento de Desvios** | Sem procedimento documentado para acompanhamento e contingência de atrasos. | Protocolo claro de 48h no GitHub Projects com pareamento técnico ou fatiamento MoSCoW. |
| **Seção 4.2: Matriz de Riscos** | Registro de riscos resumido, sem severidade quantitativa (P×I) e sem ações reativas. | Risk Register com 7 riscos reais quantificados, mitigação preventiva e contingência. |
| **Seção 4.5: Métricas de Projeto** | Ausência de tabela formal de indicadores, metas e ações corretivas de desvio. | 6 métricas objetivas (Lead Time, WIP, testes, taxa de defeitos, escopo e custos). |

*Fonte: CineSoft Solutions (2026).*

O Código 1 registra a alteração efetiva do texto das seções 4.1, 4.2 e 4.5 no arquivo `manual/capitulos/04-gerenciamento-tecnico.md`, entre a Versão 1.7 (commit `02edc29`, linha de base do diagnóstico) e a Versão 2.0 (commit `bb40194`, de 09/11/2026, em que a melhoria foi aplicada). Linhas iniciadas por `-` foram removidas e linhas iniciadas por `+` foram incluídas. O mesmo conteúdo está em [`assets/capitulo-06/diffs/melhoria-cap04-v1.7-v2.0.diff`](../../assets/capitulo-06/diffs/melhoria-cap04-v1.7-v2.0.diff), e o diff completo do arquivo pode ser consultado com `git diff 02edc29 bb40194 -- manual/capitulos/04-gerenciamento-tecnico.md`.

**Código 1 – Diff das seções 4.1, 4.2 e 4.5 entre a Versão 1.7 e a Versão 2.0**

````diff
diff --git a/manual/capitulos/04-gerenciamento-tecnico.md b/manual/capitulos/04-gerenciamento-tecnico.md
--- a/manual/capitulos/04-gerenciamento-tecnico.md	(Versão 1.7 — commit 02edc29)
+++ b/manual/capitulos/04-gerenciamento-tecnico.md	(Versão 2.0 — commit bb40194)
@@ -3,21 +3,62 @@ ## 4.1 Plano de projeto: escopo, cronograma, recursos e entregas
 ## 4.1 Plano de projeto: escopo, cronograma, recursos e entregas
 
-O planejamento do projeto (ISO/IEC/IEEE 12207:2021 – Cláusula 6.3.1) organiza a execução e o cronograma do CineDoom:
+O processo de planejamento do projeto (ABNT NBR ISO/IEC/IEEE 12207:2021 – Cláusula 6.3.1) estabelece a Estrutura Analítica do Projeto (EAP/WBS), o roadmap comercial em **três Macroentregas**, o cronograma detalhado de Sprints, a alocação nominal de responsáveis e a rotina formal para monitorar o progresso e corrigir eventuais desvios.
 
-### Escopo por Incremento e Releases
+### Estrutura Analítica do Projeto (EAP / WBS em 3 Níveis)
 
-| Incremento | Escopo Funcional | Requisitos Vinculados | Status |
-|---|---|---|---|
-| **Inc. 1 (Fundação)** | Filmes, Salas e Assentos | RF-03, RF-04 | Concluído no planejamento |
-| **Inc. 2 (Operação)** | Sessões e Mapa de Assentos | RF-05, RF-06 | Em andamento |
-| **Inc. 3 (Transação)** | Venda atômica, Cancelamento e Auditoria | RF-07, RF-08, RF-12 | Prioridade MVP |
-| **Inc. 4 (Clientes)** | Cadastro de Clientes e Interesses | RF-09, RF-10 | Backlog Release 1.1 |
-| **Inc. 5 (Fechamento)** | Indicadores de Ocupação e Release Demo | RF-11 | Prioridade MVP |
+O diagrama abaixo decompõe o produto **CineDoom** em três níveis hierárquicos (Nível 1: Produto; Nível 2: Macroentregas e Governança; Nível 3: Pacotes de Trabalho e Entregáveis verificáveis):
 
-### Cronograma de Execução (Foco na Entrega de 12/11/2026)
-- **22/10 a 24/10:** Congelamento do escopo do MVP, modelagem do Prisma e configuração do CI no GitHub Actions.
-- **25/10 a 31/10:** Implementação das rotas de filmes, salas, sessões e do mapa de assentos interativo.
-- **01/11 a 04/11:** Implementação da trava transacional de venda, testes no Vitest e cancelamento.
-- **05/11 a 08/11:** Integração total na Vercel com banco Neon, consolidação dos Capítulos 4 e 5 do Manual.
-- **09/11 a 11/11:** Ensaios da apresentação oral com slides Beamer e congelamento da release `v1.0.0-mvp`.
-- **12/11/2026:** Apresentação final perante a banca avaliadora.
+```mermaid
+flowchart TD
+    Root["1.0 Plataforma SaaS CineDoom\n(CineSoft Solutions)"]
+
+    Root --> M1["1.1 Macroentrega 1 (v1.0 - MVP Operacional)\nBilheteria, Back-office & Portal Web"]
+    Root --> M2["1.2 Macroentrega 2 (v2.0 - Escala Comercial)\nPagamentos Online, Mensageria & Cloud Pro"]
+    Root --> M3["1.3 Macroentrega 3 (v3.0 - Enterprise & Fiscal)\nNFC-e/SEFAZ, Bomboniere & SaaS Self-Service"]
+    Root --> GOV["1.4 Governança, Qualidade & Segurança\nContínua (ISO 12207 / LGPD)"]
+
+    M1 --> M1_1["1.1.1 Fundação Multi-Tenant,\nAuth RBAC & Criptografia CPF"]
+    M1 --> M1_2["1.1.2 Back-office Gerencial:\nFilmes, Salas, Sessões & Ocupação"]
+    M1 --> M1_3["1.1.3 Bilheteria Presencial ACID\n(SELECT FOR UPDATE) & Auditoria"]
+    M1 --> M1_4["1.1.4 Portal do Cliente: Reserva Web,\nExpiração JIT & Baixa no Balcão"]
+
+    M2 --> M2_1["1.2.1 Checkout Transparente\nStripe / Pagar.me (PIX & Cartão)"]
+    M2 --> M2_2["1.2.2 Mensageria Dedicada Resend Pro\n(Domínio Próprio DKIM/SPF)"]
+    M2 --> M2_3["1.2.3 Migração DBaaS Pro (PITR,\nRéplicas & Pooler Expandido)"]
+
+    M3 --> M3_1["1.3.1 Integração Fiscal SEFAZ\n(Emissão Automática NFC-e)"]
+    M3 --> M3_2["1.3.2 Módulo de Bomboniere,\nCombos & Controle de Estoque"]
+    M3 --> M3_3["1.3.3 Console Admin Global:\nSelf-Service Onboarding & Billing SaaS"]
+
+    GOV --> GOV_1["1.4.1 Pipeline CI/CD, Linter\ne 770 Testes Automatizados"]
+    GOV --> GOV_2["1.4.2 Telemetria Axiom (365 dias)\ne Anonimização LGPD Art. 18"]
+```
+
+### Escopo e Marcos Comerciais por Macroentrega (Milestones)
+
+A estratégia de produto da CineSoft Solutions divide o ciclo de vida do CineDoom em três grandes marcos contratuais de entrega:
+
+| Marco (Milestone) | Versão Alvo | Escopo Funcional e Infraestrutura Associada | Responsável Geral | Prazo / Janela | Status |
+| :--- | :---: | :--- | :---: | :---: | :---: |
+| **Macroentrega 1 (MVP Operacional)** | `v1.0.0` | Núcleo Multi-tenant, RBAC (`GERENTE`, `ATENDENTE`, `CLIENTE`), criptografia CPF (`HMAC-SHA256` + `AES-256-GCM`), CRUDs de filmes/salas/sessões, bilheteria presencial atômica, portal de reservas web com expiração JIT, painel de ocupação, anonimização LGPD e deploy em produção (`RF-01` a `RF-18`). | **Gabriel Lourenço** | Out/2026 – Nov/2026 | **Concluído (Em Produção)** |
+| **Macroentrega 2 (Escala & Pagamentos)** | `v2.0.0` | Integração de gateway financeiro online (PIX QR Code dinâmico e cartão de crédito via Stripe PCI-DSS), ativação do **Resend Pro** com domínio corporativo próprio (`@cinedoom.com.br`), upgrade para **Supabase/Neon Pro** (backups PITR e réplicas) e **Vercel Pro**. | **Carlos Eduardo** | Dez/2026 – Jan/2027 | **Planejado (Próxima Fase)** |
+| **Macroentrega 3 (Enterprise & Fiscal)** | `v3.0.0` | Emissão fiscal eletrônica automatizada (**NFC-e / SAT** via API Focus NFe integrada à SEFAZ), módulo de bomboniere e estoque, programa de fidelidade, **Console Global de Administração de Tenants** (*Self-Service Billing*) e BI financeiro avançado. | **Kayque Vicente & Yury Nogueira** | Fev/2027 – Abr/2027 | **Backlog Evolutivo** |
+
+### Cronograma Detalhado de Execução da Macroentrega 1 (`v1.0.0`)
+
+A construção da Macroentrega 1 foi executada em 3 Sprints intensivas de engenharia com pacotes de trabalho atribuídos nominalmente aos engenheiros da CineSoft Solutions:
+
+| Sprint / Iteração | Pacotes de Trabalho e Requisitos Entregues | Responsáveis Diretos | Início | Término | Status |
+| :--- | :--- | :--- | :---: | :---: | :---: |
+| **Sprint 1 — Fundação, Arquitetura e Segurança** | Setup Next.js 14/TypeScript (`#1`), modelagem Prisma/PostgreSQL e trigger append-only (`#2`), extensão Multi-tenant (`#3`), autenticação NextAuth/RBAC (`#4`), criptografia PII de CPF (`#5`), Log Drain Axiom (`#15`) e pipeline CI/CD (`#16`). | **Gabriel Lourenço** & **Carlos Eduardo** (Apoio: **Yury Nogueira**) | 23/10/2026 | 29/10/2026 | **100% Concluído** |
+| **Sprint 2 — Back-office, Salas e Bilheteria ACID** | Design System e mapa interativo 2D (`#17`), CRUDs de filmes, salas e sessões com pré-população (`#6`, `#7`, `#8`), polling a 2s (`#9`), venda atômica com `SELECT FOR UPDATE` (`#10`) e gestão de atendentes (`#13`). | **Gabriel Lourenço** & **Carlos Eduardo** (QA: **Kayque Vicente**) | 30/10/2026 | 04/11/2026 | **100% Concluído** |
+| **Sprint 3 — Portal do Cliente, Governança LGPD e QA** | Portal público e reserva web com expiração JIT (`#21`), autenticação de espectador e *"Minhas Reservas"* (`#22`), `NotificationService` e baixa de reserva no balcão (`#23`), cancelamento auditado (`#11`), painel de ocupação (`#12`), anonimização Art. 18 (`#14`) e suíte de 770 testes / 500 cenários *cross-tenant* (`#18`, `#19`). | **Gabriel Lourenço**, **Carlos Eduardo**, **Kayque Vicente** & **Yury Nogueira** | 05/11/2026 | 09/11/2026 | **100% Concluído** |
+
+### Rotina de Acompanhamento e Tratamento de Desvios e Atrasos
+
+Para garantir o cumprimento dos prazos e a previsibilidade das entregas, a CineSoft Solutions aplica a seguinte rotina de controle:
+1. **Monitoramento Diário no Quadro Kanban (GitHub Projects):** Todo cartão de tarefa deve conter obrigatoriamente **responsável nominal**, **data-limite (deadline)**, **estimativa** e **critério de aceite**. Tarefas paradas na coluna *In Progress* por mais de **48 horas** sem commits ou atualização de status acionam um alerta automático de impedimento (*blocker*).
+2. **Revisão Semanal de Sprint e Burndown:** Ao final de cada semana, o Gerente de Projeto (**Kayque Vicente**) e o Tech Lead (**Gabriel Lourenço**) auditam o percentual de pacotes concluídos versus planejados.
+3. **Protocolo de Tratamento de Desvios e Atrasos:**
+   - **Desvio Leve (atraso $\le 24\text{h}$ em tarefa não crítica):** Realocação de par técnico (*pair programming*) entre os desenvolvedores de backend e frontend para destravar a entrega dentro da mesma Sprint.
+   - **Desvio Moderado/Crítico (bloqueio em caminho crítico ou dependência externa):** Aplicação imediata de re-priorização MoSCoW (protegendo os requisitos *Must Have* de integridade transacional e segurança LGPD) e fatiamento da funcionalidade secundária para a iteração seguinte, registrando a decisão em ata de revisão.
@@ -25,11 +68,22 @@ ## 4.2 Plano de gestão de riscos: identificação, probabilidade, impacto e respostas
 ## 4.2 Plano de gestão de riscos: identificação, probabilidade, impacto e respostas
 
-A gestão de riscos (Cláusula 6.3.4) monitora incertezas que possam comprometer o cronograma ou a qualidade do sistema:
+O processo de gestão de riscos (Cláusula 6.3.4) identifica continuamente ameaças técnicas, operacionais, de segurança e de fornecedores externos que possam afetar a disponibilidade ou a integridade financeira e legal do CineDoom.
 
-| ID | Risco Identificado | Categoria | Prob. | Impacto | Estratégia de Mitigação | Responsável |
-|---|---|---|:---:|:---:|---|---|
-| **R-01** | Indisponibilidade de banco na nuvem | Técnico | Baixa | Alto | Uso de provedor com SLA comprovado (Neon) e script local de fallback com SQLite | DevOps |
-| **R-02** | Conflito de venda concorrente de assentos | Técnico | Média | Alto | Restrição única `@@unique([sessionId, seatId])` no banco e transações atômicas | Arquiteto |
-| **R-03** | Estouro de prazo para a apresentação | Organizacional | Média | Alto | Corte formal de escopo (foco estrito no MVP de bilheteria e ocupação) | Gerente de Projeto |
-| **R-04** | Falha de rede durante a demonstração | Operacional | Média | Alto | Gravação prévia de vídeo de contingência com o fluxo ponta a ponta | Analista de QA |
-| **R-05** | Inconsistência entre código e manual | Metodológico | Média | Médio | Matriz de rastreabilidade contínua ligando RFs a commits e testes | Analista de Requisitos |
+### Critérios de Classificação e Reavaliação Contínua
+
+- **Probabilidade de Ocorrência:** **Alta** (forte tendência de ocorrer em operação normal ou picos de estreia), **Média** (pode ocorrer sob condições específicas de carga ou falha de terceiros) ou **Baixa** (evento raro ou já contido por barreiras nativas).
+- **Impacto no Negócio:** **Alto** (indisponibilidade da bilheteria, venda dupla de poltronas, perda financeira ou violação da LGPD), **Médio** (degradação parcial de funcionalidade secundária com contorno disponível) ou **Baixo** (inconveniência visual sem bloqueio operacional).
+- **Matriz de Prioridade:** A combinação de Probabilidade $\times$ Impacto define a prioridade de tratamento como **Crítico** (exige barreira arquitetural imediata e teste automatizado obrigatório), **Alto** (exige mitigação ativa e monitoramento) ou **Médio** (monitorado com plano de contingência).
+- **Ciclo de Reavaliação:** O *Risk Register* é revisado formalmente ao final de cada Sprint e antes do início de cada nova Macroentrega.
+
+### Matriz de Riscos do Produto (*Risk Register*)
+
+| ID | Risco identificado | Categoria | Probabilidade | Impacto | Prioridade | Resposta / Mitigação | Responsável |
+| :---: | :--- | :---: | :---: | :---: | :---: | :--- | :---: |
+| **R-01** | **Conflito de concorrência (*double-booking*)** entre compras simultâneas no portal web e nos guichês físicos em estreias de alta demanda. | Técnico / Core | Média | Alto | **Crítico** | Pré-população determinística de `SessionSeat`, ordenação de IDs anti-deadlock e bloqueio pessimista `SELECT ... FOR UPDATE` em transação ACID, validado por teste automatizado com 50 threads simultâneas. | **Gabriel Lourenço** |
+| **R-02** | **Exaustão do pool de conexões ou indisponibilidade do banco PostgreSQL** devido à criação efêmera de instâncias serverless em picos de acesso. | Infraestrutura / Externa | Média | Alto | **Crítico** | Uso obrigatório de *Connection Pooler* transacional (*Supavisor* porta `6543` com `pgbouncer=true`), índices compostos por `tenant_id` e migração para plano **Pro com réplicas e PITR** na Macroentrega 2. | **Carlos Eduardo** |
+| **R-03** | **Exposição de dados pessoais (CPF) ou vazamento de dados entre cinemas concorrentes (*cross-tenant leak*)**. | Segurança / Legal (LGPD) | Baixa | Alto | **Crítico** | Proibição de CPF em texto puro (uso de `HMAC-SHA256` + `AES-256-GCM`), extensão Prisma que injeta `WHERE tenant_id` automaticamente e suíte automatizada com **500 cenários de ataque cross-tenant**. | **Carlos Eduardo & Yury Nogueira** |
+| **R-04** | **Retenção ociosa de poltronas (*no-show*)** por espectadores que reservam online e não comparecem para pagar no balcão. | Negócio / Operacional | Alta | Médio | **Alto** | Bloqueio de novas reservas web a menos de 60 minutos da sessão e **Expiração Just-in-Time (JIT)** automática, liberando os assentos instantaneamente para venda presencial na bilheteria (`ADR-012`). | **Gabriel Lourenço** |
+| **R-05** | **Falha na entrega de e-mails transacionais de vouchers** ou retenção em filtros anti-spam sem domínio próprio verificado. | Dependência Externa | Média | Médio | **Alto** | Desacoplamento via interface `EmailProvider`, exibição imediata do voucher com código localizador na tela de confirmação e na área *"Minhas Reservas"*, e contratação do **Resend Pro com domínio DKIM/SPF** na Macroentrega 2. | **Carlos Eduardo** |
+| **R-06** | **Atraso na integração de dependências entre módulos** (ex.: acoplamento entre refatorações de UI responsiva e contratos de API). | Organizacional / Projeto | Média | Médio | **Médio** | Contratos de validação estritos via schemas `Zod`, esteira de CI bloqueante a cada Pull Request e protocolo de realocação em pares (*pair programming*) quando uma tarefa excede 48h. | **Kayque Vicente** |
+| **R-07** | **Instabilidade nos webservices estaduais da SEFAZ ou gateway de pagamento** durante o horário de pico noturno dos cinemas (Macroentregas 2 e 3). | Dependência Externa | Média | Alto | **Alto** | Processamento fiscal em fila assíncrona com emissão em contingência offline (Focus NFe) e fallback imediato para recebimento presencial no guichê caso o gateway online oscile. | **Gabriel Lourenço & Kayque Vicente** |
@@ -71,6 +169,11 @@ ## 4.5 Métricas de acompanhamento do projeto
 ## 4.5 Métricas de acompanhamento do projeto
 
-A medição e controle (Cláusula 6.3.2) subsidiam o acompanhamento do avanço do projeto:
-- **Velocidade de Entrega:** Percentual de requisitos funcionais com status *Done*.
-- **Cobertura de Testes de Regra Crítica:** 100% de cobertura nos métodos do serviço de venda e cancelamento de ingressos.
-- **Densidade de Defeitos:** Número de bugs abertos versus resolvidos no GitHub Issues antes da release.
+O processo de medição e avaliação (Cláusula 6.3.2) utiliza indicadores quantitativos coletados do GitHub, da pipeline de CI e do Vitest para monitorar a saúde técnica da entrega:
+
+| Categoria de Métrica | Indicador Objetivo | Meta Organizacional | Resultado Aferido na Macroentrega 1 (`v1.0.0`) | Como é Monitorado e Ação em Caso de Desvio |
+| :--- | :--- | :---: | :---: | :--- |
+| **Métrica de Fluxo** | **Lead Time de Issues e PRs** (tempo entre abertura da tarefa e merge em `main`) | $\le 48\text{ horas}$ por pacote de trabalho | Média de **18 a 32 horas** por issue | Monitorado via GitHub Projects. Se exceder 48h, o GP aciona pareamento técnico imediato. |
+| **Métrica de Fluxo** | **Work in Progress (WIP Limit)** por engenheiro | Máximo de **2 tarefas** simultâneas em *In Progress* | Respeitado ($\le 2$ por membro) | Conferido na revisão diária do quadro Kanban para evitar gargalos de troca de contexto. |
+| **Métrica de Qualidade** | **Suíte de Testes Automatizados e Cobertura Crítica** | **100% de aprovação** e 100% nos serviços críticos | **26 suítes / 770 testes passando (100%)** em ~4,9s | Bloqueio automático no GitHub Actions; PRs com qualquer teste quebrado são impedidos de merge. |
+| **Métrica de Qualidade** | **Densidade de Defeitos em Produção** (bugs críticos pós-deploy) | **0 defeitos críticos** (venda dupla ou perda de dados) | **0 defeitos críticos** (ajustes apenas cosméticos/mobile) | Monitorado via telemetria e testes de usuários reais; defeitos P1 acionam rollback em < 5 min. |
+| **Métrica de Progresso** | **Cumprimento do Escopo da Macroentrega (Throughput)** | **100% dos requisitos `RF-01` a `RF-18`** entregues no marco | **18/18 RFs (100%)** e **14/14 Critérios de Aceite** concluídos | Auditado ao final de cada Sprint na Matriz de Rastreabilidade (Capítulo 5.1.2). |
````

*Fonte: Histórico de versões do repositório `manual-processos-software` no GitHub (2026).*

### Reavaliação Pós-Melhoria (Verificação da Eficácia Documental)

Reavaliando as seções **4.1, 4.2 e 4.5** sob as mesmas quatro questões do diagnóstico inicial, comprova-se a superação integral das lacunas:

**Tabela 47 – Reavaliação Pós-Melhoria da Conformidade do Manual (Versão 2.0)**

| Pergunta de avaliação | Seção Revisada | Nova Situação e Evidência Verificável (Versão 2.0) |
| :--- | :---: | :--- |
| **1. O escopo e as entregas do projeto estão claros?** | `4.1` | **Descrito.** A seção 4.1 agora inclui o diagrama da EAP em 3 níveis e a tabela das **3 Macroentregas** (`v1.0.0`, `v2.0.0` e `v3.0.0`), detalhando exatamente os pacotes entregues em produção e a evolução comercial. |
| **2. As atividades possuem responsáveis e prazos?** | `4.1` | **Descrito.** Tanto a tabela de Marcos Comerciais quanto a tabela das 3 Sprints de execução especificam nominalmente os engenheiros responsáveis (`Gabriel Lourenço`, `Carlos Eduardo`, `Kayque Vicente`, `Yury Nogueira`) e as datas de início e término. |
| **3. Os riscos e suas respostas estão definidos?** | `4.2` | **Descrito.** A seção 4.2 explicita os critérios de Probabilidade, Impacto e Prioridade, o ciclo de reavaliação por Sprint e a matriz com 7 riscos reais de engenharia/negócio, respostas técnicas e responsáveis nominais. |
| **4. Está definido como acompanhar o andamento e tratar atrasos?** | `4.1` e `4.5` | **Descrito.** A seção 4.1 formaliza a subseção *"Rotina de Acompanhamento e Tratamento de Desvios e Atrasos"* (gatilho de 48h e pareamento técnico), complementada na seção 4.5 por métricas com metas objetivas e resultados aferidos (`Lead Time <= 48h`, `WIP <= 2`, `770 testes`). |

*Fonte: CineSoft Solutions (2026).*

---

## 6.5 Acompanhamento da execução

Para assegurar que a melhoria incorporada ao manual continue sendo praticada de forma sustentável nas próximas iterações e ao longo das Macroentregas 2 e 3, a CineSoft Solutions estabeleceu a seguinte sistemática de verificação operacional:

1. **Quem realiza a conferência:** **Kayque Vicente Silva** (Gerente de Projeto & QA Lead), em conjunto com **Gabriel Henrique Lourenço Dias** (Tech Lead).
2. **Quando ocorre a verificação:** Semanalmente, durante a cerimônia de *Sprint Planning / Review*, e continuamente a cada abertura de Pull Request no repositório do GitHub.
3. **Qual registro e medida são observados:**
   - **Indicador de Conformidade do Quadro Kanban:** Percentual de cartões ativos nas colunas *Sprint Backlog* e *In Progress* do GitHub Projects que possuem simultaneamente **responsável atribuído (`Assignee`)**, **prazo estipulado (`Iteration / Milestone`)** e **requisitos vinculados** (Meta: **100% dos cartões conformes**).
   - **Registro de Auditoria:** Caso seja identificado qualquer cartão sem responsável ou acima do limite de 48h sem atualização, a pendência é registrada e corrigida imediatamente na abertura da reunião semanal, acionando o protocolo de pareamento descrito na seção 4.1.

---

### Referências Normativas do Capítulo

- **SOFTEX.** *Guia Geral MPS de Software: 2024 (MR-MPS-SW)*. Associação para Promoção da Excelência do Software Brasileiro. Disponível em: https://softex.br/download/guia-geral-mps-de-software2024/.
- **ABNT.** *NBR ISO/IEC/IEEE 12207:2021 — Engenharia de sistemas e software — Processos de ciclo de vida de software*. Rio de Janeiro: ABNT, 2021.
