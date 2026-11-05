# Orientações para o Capítulo 3: Processos Organizacionais Habilitadores de Projeto

Documento de diretrizes e requisitos para a elaboração do **Capítulo 3** do Manual de Processos de Software, baseado na **Seção 6.2 da ABNT NBR ISO/IEC/IEEE 12207:2021** e no material das **Aulas 3 e 4**.

---

## 3.1 Objetivo do Capítulo

Estabelecer os processos em nível organizacional que fornecem a infraestrutura, as políticas de ciclo de vida, as competências humanas, a governança de portfólio, a qualidade e a gestão de conhecimento para que o projeto atenda às necessidades de todos os stakeholders.

---

## 3.2 Conteúdo Exigido na Atividade (Aulas 3 e 4)

Conforme os slides de fechamento da **Aula 3-4 (Slide 33)** e a estrutura mínima, a equipe deve documentar os 6 processos organizacionais:

### 3.1 Modelo de Ciclo de Vida Adotado e Justificado (ISO 6.2.1)
- Identificar o modelo de processo escolhido (ex.: *Scrum adaptado, Sprints de 1 semana, abordagem iterativa e incremental*).
- Justificar a escolha com base nas características do produto, incertezas e prazo da disciplina.

### 3.2 Inventário de Infraestrutura e Ferramentas Necessárias (ISO 6.2.2)
- Mapear a infraestrutura de desenvolvimento, homologação e produção:
  - Repositórios e esteira: GitHub, GitHub Actions.
  - Hospedagem e computação: Vercel Serverless.
  - Banco de dados gerenciado: Neon Serverless PostgreSQL.
  - Ferramentas de design e prototipação: Figma.
  - Ambientes de teste e métricas: Vitest, Node.js.

### 3.3 Justificativa Estratégica e Viabilidade do Projeto (Portfólio - ISO 6.2.3)
- Análise de viabilidade do projeto: alinhamento com a estratégia da organização CineSoft Solutions e critérios de priorização do investimento.

### 3.4 Papéis, Competências e Plano de Capacitação / Matriz RACI (Recursos Humanos - ISO 6.2.4)
- Mapeamento das competências técnicas necessárias (Next.js 15, Prisma ORM, Tailwind CSS, TypeScript, ISO 12207).
- Matriz RACI relacionando membros da equipe e principais entregáveis/processos.
- Plano de capacitação para suprir eventuais lacunas da equipe.

### 3.5 Plano de Qualidade com Critérios e Métricas (ISO 6.2.5)
- Políticas de garantia da qualidade organizacional:
  - Padrões de código (ESLint, Prettier).
  - Cobertura de testes unitários e de integração.
  - Política rigorosa de code review (aprovação de PRs).

### 3.6 Estratégia de Gestão do Conhecimento (ISO 6.2.6)
- Como a organização documenta e preserva o conhecimento técnico:
  - Uso de ADRs (Architecture Decision Records) para decisões técnicas irreversíveis.
  - Wikis, documentação em Markdown no próprio repositório (`manual/`, `specs/`).
  - Histórico de lições aprendidas e revisões de sprint.

---

## 3.3 Critérios de Qualidade da Professora

> **📌 Referência:** Seção 6.2 da ISO 12207:2017  
> **⚠️ Atenção:** Os artefatos não precisam ser extensos — precisam ser consistentes, justificados e aplicados ao seu projeto real. Qualidade > quantidade.
