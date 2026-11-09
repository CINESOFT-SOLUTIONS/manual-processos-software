# Capítulo 6 – Avaliação e melhoria dos processos de software

## 6.1 Referencial e recorte

Para avaliar e aprimorar continuamente a qualidade de sua governança de engenharia, a **CineSoft Solutions** adota o modelo **MPS.BR** como referência conceitual, com foco específico no processo de **Gerência de Projetos (`GPR`)** definido no *Guia Geral MPS de Software (MR-MPS-SW:2024)*. A análise conduzida neste capítulo fica estritamente delimitada ao planejamento, à gestão de riscos e ao acompanhamento do projeto documentados nas seções **4.1** (*Plano de projeto: escopo, cronograma, recursos e entregas*), **4.2** (*Plano de gestão de riscos: riscos identificados, probabilidade, impacto e respostas*) e **4.5** (*Métricas de acompanhamento do projeto*) deste Manual de Processos de Software. As questões avaliadas a seguir constituem adaptações didáticas orientadas à melhoria contínua do processo da equipe, não atribuindo nível formal de maturidade MPS.BR nem atestando conformidade integral com todos os resultados esperados do modelo.

---

## 6.2 Diagnóstico do manual

Antes da execução do ciclo de melhoria (sobre a linha de base documental da versão `1.7` do manual), a equipe realizou uma auditoria interna examinando as seções **4.1, 4.2 e 4.5** frente às quatro questões de diagnóstico. Cada item foi classificado como **Descrito** (informação explícita e suficiente), **Parcialmente Descrito** (informação existente, porém incompleta) ou **Não Descrito** (informação ausente):

| Pergunta de avaliação | Seção | Situação e evidência (Diagnóstico Inicial — Versão 1.7) |
| :--- | :---: | :--- |
| **1. O escopo e as entregas do projeto estão claros?** | `4.1` | **Parcialmente Descrito.** A seção 4.1 listava uma tabela resumida de 5 incrementos internos, mas não apresentava a Estrutura Analítica do Projeto (EAP/WBS) nem estruturava o ciclo de evolução comercial do produto nas **3 Macroentregas** (`v1.0` MVP, `v2.0` Escala/Pagamentos e `v3.0` Enterprise/Fiscal). |
| **2. As atividades possuem responsáveis e prazos?** | `4.1` | **Parcialmente Descrito.** O cronograma da seção 4.1 apresentava janelas de datas gerais (ex.: *"25/10 a 31/10"*), mas **não atribuía nominalmente os responsáveis diretos** por cada pacote de trabalho/Sprint dentro da própria tabela do plano de projeto, além de misturar tarefas acadêmicas externas ao produto. |
| **3. Os riscos e suas respostas estão definidos?** | `4.2` | **Parcialmente Descrito.** A tabela da seção 4.2 continha 5 itens, porém **não possuía a coluna de Prioridade** (Crítico / Alto / Médio), não explicitava os critérios de classificação/reavaliação e misturava riscos escolares (*"falha de rede na apresentação"*) em vez de focar integralmente nos riscos reais de engenharia e operação do SaaS. |
| **4. Está definido como acompanhar o andamento e tratar atrasos?** | `4.5` e `4.1` | **Não Descrito.** A seção 4.5 listava três indicadores conceituais sem metas numéricas nem valores aferidos, e a seção 4.1 **não definia a rotina de acompanhamento diário/semanal nem o protocolo de ação corretiva** para destravar tarefas atrasadas ou bloqueadas. |

---

## 6.3 Plano de uma melhoria

Com base nas lacunas identificadas no diagnóstico da seção 6.2 — especialmente a ausência de atribuição nominal de responsáveis por entrega/Sprint, a falta de um protocolo claro para monitoramento e tratamento de atrasos e a incompletude da matriz de riscos —, a equipe estruturou e executou o seguinte plano de ação:

| Campo do plano | Resposta da equipe (CineSoft Solutions) |
| :--- | :--- |
| **Lacuna e justificativa** | As seções `4.1`, `4.2` e `4.5` careciam de atribuição nominal de responsáveis nos pacotes do cronograma, não definiam a rotina prática para detectar e tratar desvios/atrasos (com metas e limites objetivos) e não classificavam a prioridade dos riscos reais do produto. Isso gerava ambiguidade sobre quem deveria agir quando uma tarefa atrasava no quadro Kanban. |
| **Ação** | Reestruturar integralmente as seções `4.1`, `4.2` e `4.5` para: (1) incorporar a EAP de 3 níveis e o roadmap corporativo nas **3 Macroentregas** com responsáveis nominais e prazos por Sprint; (2) instituir o protocolo formal de acompanhamento e tratamento de desvios (alerta de bloqueio em 48h, limite WIP $\le 2$ e pareamento técnico); (3) adicionar a coluna **Prioridade** e critérios de reavaliação no *Risk Register*; e (4) estabelecer metas quantitativas e resultados aferidos nas métricas de acompanhamento. |
| **Responsável e prazo** | **Responsável:** Kayque Vicente Silva (Gerente de Projeto & QA Lead), com revisão de Gabriel Henrique Lourenço Dias (Tech Lead). **Prazo de conclusão:** 09/11/2026. |
| **Evidência da revisão** | Atualização documental das seções `4.1`, `4.2` e `4.5` no arquivo `manual/capitulos/04-gerenciamento-tecnico.md` (registrada na versão `2.0` do Histórico de Versões) e sincronização dos cards no quadro GitHub Projects v2 (`CINESOFT-SOLUTIONS`). |
| **Resultado esperado** | Eliminar dúvidas sobre a responsabilidade de cada pacote de trabalho, detectar gargalos em menos de 48 horas e garantir 100% de previsibilidade na entrega dos 18 requisitos funcionais da Macroentrega 1 (`v1.0.0`). |

---

## 6.4 Atualização e verificação

A melhoria planejada foi efetivamente aplicada no Capítulo 4 deste manual. O quadro comparativo a seguir confronta diretamente o trecho que constava antes (Versão `1.7`) com a nova redação implementada (Versão `2.0`):

### Quadro Comparativo: Antes vs. Depois da Revisão (Seções 4.1, 4.2 e 4.5)

```diff
--- a/manual/capitulos/04-gerenciamento-tecnico.md (Versão 1.7 - Antes da Melhoria)
+++ b/manual/capitulos/04-gerenciamento-tecnico.md (Versão 2.0 - Após a Melhoria)
@@ Seção 4.1: Escopo, Cronograma e Rotina de Acompanhamento @@
- ### Cronograma de Execução
- - 22/10 a 24/10: Congelamento do escopo do MVP, modelagem do Prisma e configuração do CI.
- - 25/10 a 31/10: Implementação das rotas de filmes, salas, sessões e do mapa de assentos.
- - 05/11 a 08/11: Integração total na Vercel e congelamento da release v1.0.0-mvp.
- (Sem EAP, sem divisão em Macroentregas, sem responsáveis nominais nas entregas e sem rotina de tratamento de atrasos)
+ ### Estrutura Analítica do Projeto (EAP / WBS em 3 Níveis) e Roadmap em 3 Macroentregas
+ - Macroentrega 1 (v1.0.0 - MVP Operacional): Gabriel Lourenço | Out–Nov/2026 | Concluído
+ - Macroentrega 2 (v2.0.0 - Escala & Pagamentos Stripe/Resend Pro): Carlos Eduardo | Dez/2026–Jan/2027
+ - Macroentrega 3 (v3.0.0 - Enterprise, Fiscal NFC-e & Billing SaaS): Kayque Vicente & Yury Nogueira | Fev–Abr/2027
+ - Cronograma por Sprint (Sprints 1, 2 e 3) com Responsáveis Diretos nominais e datas de início/término.
+ ### Rotina de Acompanhamento e Tratamento de Desvios e Atrasos
+ - Monitoramento diário no GitHub Projects (responsável, deadline e critério de aceite obrigatórios).
+ - Gatilho de 48h para tarefas sem avanço: realocação em Pair Programming (desvio leve <= 24h)
+   ou fatiamento MoSCoW protegendo os requisitos Must Have (desvio crítico).

@@ Seção 4.2 e 4.5: Risk Register e Métricas Quantitativas @@
- | ID | Risco Identificado | Categoria | Prob. | Impacto | Estratégia de Mitigação | Responsável |
- (Sem coluna Prioridade, sem critérios de reavaliação e sem metas nas métricas da Seção 4.5)
+ | ID | Risco identificado | Categoria | Probabilidade | Impacto | Prioridade | Resposta / Mitigação | Responsável |
+ (Incluídos 7 riscos reais de produto/engenharia classificados em Crítico/Alto/Médio + critérios formais)
+ (Seção 4.5 atualizada com metas numéricas: Lead Time <= 48h, WIP <= 2, 770 testes verdes e 18/18 RFs entregues)
```

### Reavaliação Pós-Melhoria (Verificação da Eficácia Documental)

Reavaliando as seções **4.1, 4.2 e 4.5** sob as mesmas quatro questões do diagnóstico inicial, comprova-se a superação integral das lacunas:

| Pergunta de avaliação | Seção Revisada | Nova Situação e Evidência Verificável (Versão 2.0) |
| :--- | :---: | :--- |
| **1. O escopo e as entregas do projeto estão claros?** | `4.1` | **Descrito.** A seção 4.1 agora inclui o diagrama da EAP em 3 níveis e a tabela das **3 Macroentregas** (`v1.0.0`, `v2.0.0` e `v3.0.0`), detalhando exatamente os pacotes entregues em produção e a evolução comercial. |
| **2. As atividades possuem responsáveis e prazos?** | `4.1` | **Descrito.** Tanto a tabela de Marcos Comerciais quanto a tabela das 3 Sprints de execução especificam nominalmente os engenheiros responsáveis (`Gabriel Lourenço`, `Carlos Eduardo`, `Kayque Vicente`, `Yury Nogueira`) e as datas de início e término. |
| **3. Os riscos e suas respostas estão definidos?** | `4.2` | **Descrito.** A seção 4.2 explicita os critérios de Probabilidade, Impacto e Prioridade, o ciclo de reavaliação por Sprint e a matriz com 7 riscos reais de engenharia/negócio, respostas técnicas e responsáveis nominais. |
| **4. Está definido como acompanhar o andamento e tratar atrasos?** | `4.1` e `4.5` | **Descrito.** A seção 4.1 formaliza a subseção *"Rotina de Acompanhamento e Tratamento de Desvios e Atrasos"* (gatilho de 48h e pareamento técnico), complementada na seção 4.5 por métricas com metas objetivas e resultados aferidos (`Lead Time <= 48h`, `WIP <= 2`, `770 testes`). |

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
