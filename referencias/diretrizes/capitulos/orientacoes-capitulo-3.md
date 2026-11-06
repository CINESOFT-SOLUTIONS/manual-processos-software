# Orientações para o Capítulo 3: Processos Organizacionais Habilitadores

Neste capítulo, a equipe definirá os processos de nível organizacional que sustentam os projetos da empresa: ciclo de vida, infraestrutura, estratégia de portfólio, competências humanas, qualidade e gestão do conhecimento. A atividade é fundamentada na Seção 6.2 da ABNT NBR ISO/IEC/IEEE 12207:2021.

# **3.1 Modelo de ciclo de vida adotado e justificado**

Definam o modelo de ciclo de vida adotado pela equipe (ex.: iterativo e incremental, Scrum adaptado, Kanban). Expliquem as fases, as cerimônias ou iterações previstas e justifiquem a escolha com base na natureza do software e nos prazos do projeto.

# **3.2 Inventário de infraestrutura e ferramentas necessárias**

Apresentem o inventário completo da infraestrutura tecnológica e das ferramentas que viabilizam o desenvolvimento, a automação e a execução do software:

| Categoria | Ferramenta / Infraestrutura | Finalidade no Projeto |
| :--- | :--- | :--- |
| Gestão e Código | [Ex: GitHub] | [Controle de versão, issues, PRs] |
| CI/CD e Automação | [Ex: GitHub Actions] | [Pipeline de testes e deploy contínuo] |
| Hospedagem e Computação | [Ex: Vercel Serverless] | [Ambiente de execução e edge delivery] |
| Banco de Dados | [Ex: Neon PostgreSQL] | [Persistência relacional gerenciada] |
| Design e Prototipação | [Ex: Figma] | [Prototipação de telas e design system] |
| Testes e Qualidade | [Ex: Vitest / ESLint] | [Execução de testes unitários e linter] |

# **3.3 Justificativa estratégica e viabilidade do projeto**

Expliquem o alinhamento do software com a estratégia da organização desenvolvedora. Apresentem a análise de viabilidade técnica, econômica e operacional do projeto, demonstrando por que o investimento faz sentido para o portfólio da equipe.

# **3.4 Papéis, competências e plano de capacitação (RACI)**

Identifiquem a composição da equipe, as competências requeridas para cada tecnologia do stack e a atribuição de responsabilidades. Apresentem a matriz RACI relacionando membros e principais macroatividades do projeto:

| Macroatividade / Entregável | [Membro 1] | [Membro 2] | [Membro 3] | [Membro 4] |
| :--- | :---: | :---: | :---: | :---: |
| [Atividade ou Processo] | [R / A / C / I] | [R / A / C / I] | [R / A / C / I] | [R / A / C / I] |

Descrevam o plano de capacitação para suprir eventuais lacunas técnicas identificadas na equipe.

# **3.5 Plano de qualidade com critérios e métricas**

Definam os critérios e as métricas de qualidade adotados no nível organizacional: padrões de codificação, cobertura mínima de testes, critérios de aprovação de código (code review) e políticas de estabilidade antes do deploy em produção.

# **3.6 Estratégia de gestão do conhecimento**

Expliquem como a equipe registra, preserva e dissemina o conhecimento técnico e de negócio. Detalhem a política de documentação arquitetural (ADRs), lições aprendidas e documentação em repositório.

# **Critérios de avaliação**

Apresentem as seções 3.1 a 3.6 no Manual de Processos de Software. A avaliação considerará a consistência da justificativa do ciclo de vida, a completude do inventário, a coerência da matriz RACI e o rigor das políticas de qualidade e conhecimento.
