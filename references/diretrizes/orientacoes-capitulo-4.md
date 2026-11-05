# Orientações para o Capítulo 4: Processos de Gerenciamento Técnico

Documento de diretrizes e requisitos para a elaboração do **Capítulo 4** do Manual de Processos de Software, baseado na **Seção 6.3 da ABNT NBR ISO/IEC/IEEE 12207:2021** e no material da **Aula 5**.

---

## 4.1 Objetivo do Capítulo

Estruturar a aplicação dos recursos administrativos e técnicos para planejar, monitorar, controlar os riscos e governar os artefatos técnicos de software ao longo do ciclo de vida do projeto.

---

## 4.2 Conteúdo Exigido na Atividade (Aula 5 - Slide 19)

Conforme os slides de fechamento da **Aula 5**, a equipe deve documentar 5 tópicos centrais:

### 4.1 Plano de Projeto: Escopo, Cronograma, Recursos e Entregas (ISO 6.3.1 e 6.3.2)
- **Escopo e Marcos:** Definição clara dos marcos do projeto integrador (M1, M2, M3).
- **Cronograma e Sprints:** Estrutura temporal de execução (sprints semanais, datas-chave de entrega).
- **Alocação de Recursos e Responsáveis:** Quem é responsável pelo quê e prazos acordados.
- **Mecanismos de Controle:** Como acompanhar o andamento da equipe e tratar eventuais desvios/atrasos.

### 4.2 Plano de Gestão de Riscos: Risk Register (ISO 6.3.4)
Identificar, quantificar e propor ações de mitigação contínuas em uma tabela padronizada (*Risk Register*):

| Risco Identificado | Probabilidade | Impacto | Prioridade | Resposta / Estratégia de Mitigação |
| :--- | :---: | :---: | :---: | :--- |
| *Ex: Concorrência e bloqueio duplo de assentos* | *Alta* | *Alto* | *Crítico* | *Lock de banco `SELECT FOR UPDATE` + expiração em 10 min* |
| *Ex: Sobrecarga em sessões de estreia* | *Média* | *Alto* | *Alto* | *Caching em borda na Vercel e índices no PostgreSQL* |
| *Ex: Saída ou ausência de membro da equipe* | *Média* | *Médio* | *Médio* | *Pair programming, PRs com 2 revisores e documentação contínua* |

### 4.3 Plano de Gestão de Configuração (ISO 6.3.5)
- **Estratégia de Branches:** Branching model (ex.: GitFlow ou GitHub Flow com `main` protegida, branches de feature e `develop`).
- **Política de Pull Requests:** Regras para merge (testes automatizados passando no CI, aprovação por code review).
- **Versionamento e Releases:** Política de tags e Semantic Versioning (SemVer: `vX.Y.Z`).

### 4.4 Registro de Decisões Técnicas Relevantes - ADRs (ISO 6.3.3)
- Apresentar o catálogo de ADRs (Architecture Decision Records) estruturadas:
  - Contexto e problema técnico.
  - Alternativas consideradas e critérios de avaliação.
  - Decisão tomada e justificativa.
  - Consequências técnicas (positivas e negativas).

### 4.5 Métricas de Acompanhamento do Projeto (ISO 6.3.7)
- Indicadores objetivos para monitorar a saúde do projeto:
  - *Lead time* / *Cycle time* de Pull Requests e Issues.
  - Cobertura de testes unitários e de integração (alvo percentual).
  - Velocidade da sprint (histórias concluídas vs. planejadas).
  - Taxa de defeitos reabertos ou bugs pós-deploy.

---

## 4.3 Critérios de Qualidade da Professora

> **📌 Referência:** Seção 6.3 da ISO 12207:2017  
> **⚠️ Atenção:** Os artefatos não precisam ser extensos — precisam ser consistentes, justificados e aplicados ao seu projeto real. Qualidade > quantidade.
