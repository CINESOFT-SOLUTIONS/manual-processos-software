# Orientações para o Capítulo 4: Processos de Gerenciamento Técnico

Neste capítulo, a equipe definirá os processos que planejam, organizam, monitoram e controlam os recursos técnicos do projeto: plano de projeto, gestão de riscos, controle de configuração, decisões arquiteturais e métricas. A atividade é fundamentada na Seção 6.3 da ABNT NBR ISO/IEC/IEEE 12207:2021.

# **4.1 Plano de projeto: escopo, cronograma, recursos e entregas**

Definam o plano formal de projeto da equipe. Dividam a execução em marcos de entrega claros (milestones) e sprints de desenvolvimento.

Especifiquem as atividades, os responsáveis diretos por cada frente, os prazos estipulados e a rotina adotada para acompanhar o andamento diário/semanal e tratar eventuais desvios e atrasos.

# **4.2 Plano de gestão de riscos: riscos identificados, probabilidade, impacto e respostas**

Apresentem o plano contínuo de gestão de riscos do projeto. Identifiquem os riscos técnicos, organizacionais, de dependência externa e de negócio na matriz *Risk Register*:

| Risco identificado | Probabilidade | Impacto | Prioridade | Resposta / Mitigação |
| :--- | :---: | :---: | :---: | :--- |
| [Descrição do risco] | [Alta / Média / Baixa] | [Alto / Médio / Baixo] | [Crítico / Alto / Médio] | [Ação preventiva ou corretiva] |

Expliquem os critérios utilizados para classificar a probabilidade e o impacto, e como os riscos serão reavaliados ao longo das iterações.

# **4.3 Plano de gestão de configuração: controle de versões, branches e releases**

Definam a política formal de gerenciamento de configuração do software:
- Estratégia de branches no repositório (ex.: branch principal protegida, branches de desenvolvimento/feature, releases).
- Regras de Pull Request: obrigatoriedade de testes automatizados passando e aprovação de pares (code review).
- Padrão de versionamento semântico (SemVer: `MAJOR.MINOR.PATCH`) e convenção de mensagens de commit.

# **4.4 Registro de decisões técnicas relevantes (ADRs)**

Estruturem o registro formal das decisões técnicas e arquiteturais de alto impacto adotadas no projeto (*Architecture Decision Records*).

Para cada decisão relevante, apresentem:
- **Título e Status:** (ex.: ADR-001 — Aprovada).
- **Contexto:** Qual problema precisava de solução?
- **Alternativas consideradas:** Quais opções técnicas foram avaliadas?
- **Decisão e Justificativa:** O que foi escolhido e por quê?
- **Consequências:** Quais os trade-offs e impactos gerados no sistema?

# **4.5 Métricas de acompanhamento do projeto**

Definam os indicadores objetivos que a equipe observará para acompanhar o desempenho técnico e a saúde da entrega:
- Métricas de fluxo: tempo de ciclo de issues e PRs (lead time).
- Métricas de qualidade: percentual de cobertura de testes automatizados e densidade de bugs.
- Métricas de progresso: itens entregues por sprint e cumprimento do cronograma planejado.

# **Critérios de avaliação**

Apresentem as seções 4.1 a 4.5 no Manual de Processos de Software. A avaliação considerará a viabilidade do cronograma, o rigor do Risk Register, a robustez da política de branches/PRs e a consistência técnica das ADRs e métricas.
