# Capítulo 3 – Processos Organizacionais Habilitadores

## 3.1 Modelo de ciclo de vida adotado e justificado

O CineDoom adota o modelo de ciclo de vida **Incremental** (ISO/IEC/IEEE 12207:2021 – Cláusula 6.2.1), complementado por práticas ágeis de integração contínua.

### Justificativa da Escolha
1. **Decomposição Modular:** O domínio de cinema permite isolar módulos estáveis (filmes, salas) de módulos de maior complexidade transacional (sessões, assentos, venda).
2. **Entregas de Valor Frequentes:** Cada incremento produz uma release executável e testada, reduzindo riscos de desalinhamento com o cliente.
3. **Adaptação ao Prazo Acadêmico:** O modelo incremental viabilizou o corte formal de escopo para viabilizar um MVP demonstrável sem comprometer o planejamento dos demais processos.

### Ciclo dos Incrementos
Cada incremento percorre cinco etapas obrigatórias: **Requisito → Design/Arquitetura → Implementação → Teste → Release**.

## 3.2 Inventário de infraestrutura e ferramentas necessárias

A gestão da infraestrutura (Cláusula 6.2.2) assegura os recursos para o ciclo de vida do software:

| Categoria | Recurso / Ferramenta | Finalidade | Responsável |
|---|---|---|---|
| **Ambiente de Desenvolvimento** | VS Code, Node.js v20, npm, Git | Edição de código e execução de servidores locais | Desenvolvedores |
| **Controle de Versão & CI** | GitHub, GitHub Actions, Git | Versionamento, rastreamento de branches e esteira automatizada | DevOps |
| **Persistência de Dados** | PostgreSQL gerenciado (Neon), Prisma ORM | Modelagem de dados, migrações e persistência relacional | Arquiteto / DBA |
| **Hospedagem & Deploy** | Vercel (Produção e Preview) | Disponibilização do software web em ambiente global | DevOps |
| **Documentação & Compilação** | Tectonic, LaTeX, Beamer, Markdown | Geração de relatórios ABNT e slides de defesa | Equipe |
| **Testes Automatizados** | Vitest | Execução de testes unitários e de integração de regras de negócio | Engenheiro de Testes |

## 3.3 Justificativa estratégica e viabilidade do projeto

A gestão de portfólio (Cláusula 6.2.3) comprova a viabilidade do produto:
- **Viabilidade Técnica:** A stack adotada (Next.js, Prisma, PostgreSQL) possui maturidade elevada, ampla documentação e domínio prévio por parte da equipe.
- **Viabilidade Organizacional:** A equipe de 4 integrantes possui papéis claros e processos bem definidos, permitindo desenvolver em paralelo o software executável e a documentação normativa.
- **Viabilidade de Negócio:** Cinemas de pequeno e médio porte representam um nicho desassistido por grandes ERPs de alto custo, validando a proposição de valor do CineDoom como SaaS leve.

## 3.4 Papéis, competências e plano de capacitação (RACI)

### Distribuição de Papéis
- **Gerente de Projeto (GP):** Governança do cronograma, comunicação e controle de riscos.
- **Analista de Requisitos (AR):** Elicitação de necessidades, especificação de RFs e rastreabilidade.
- **Arquiteto de Software (AS):** Definição da stack, ADRs e integridade técnica dos componentes.
- **Desenvolvedores Frontend e Backend (DEV):** Codificação da interface web e das rotas de API.
- **Engenheiro de Testes (TEST):** Planejamento e codificação dos testes no Vitest.
- **DevOps (OPS):** Manutenção dos pipelines de CI, branches e ambiente na Vercel.
- **Analista de Qualidade (QA):** Auditoria de processos, métricas e conformidade com a ISO 12207.

### Matriz RACI Consolidada

| Atividade do Ciclo de Vida | GP | AR | AS | DEV | TEST | OPS | QA |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Planejamento e Cronograma | **A/R** | C | C | I | I | C | C |
| Elicitação e Especificação de Requisitos | A | **R** | C | I | C | I | C |
| Decisões de Arquitetura (ADRs) | C | C | **A/R** | C | C | C | I |
| Implementação do Código-Fonte | I | I | A | **R** | C | C | I |
| Execução de Testes Automatizados | I | C | C | C | **A/R** | I | C |
| Implantação e Deploy na Vercel | A | I | C | C | C | **R** | C |
| Auditoria de Qualidade e Processos | A | C | C | C | C | C | **R** |
| Aceite Formal de Releases | **A** | C | C | I | R | I | C |

*Legenda:* **R** = Responsável pela execução; **A** = Aprovador final; **C** = Consultado; **I** = Informado.

### Plano de Capacitação
A equipe executou nivelamento técnico em: Gitflow colaborativo, convenções de commits, modelagem relacional com Prisma ORM, elaboração de testes automatizados com Vitest e compilação de artefatos LaTeX via Tectonic.

## 3.5 Plano de qualidade com critérios e métricas

A gestão da qualidade (Cláusula 6.2.5) define critérios objetivos para assegurar a excelência dos entregáveis:
1. **Rastreabilidade Bidirecional:** 100% dos requisitos funcionais do MVP devem estar mapeados a testes e commits.
2. **Qualidade de Código:** Validação obrigatória por linter sem erros nos Pull Requests.
3. **Taxa de Sucesso em Testes:** 100% de aprovação na suíte de testes do Vitest para que o PR possa ser mesclado em `main`.
4. **Resiliência a Falhas de Concorrência:** Zero ocorrências de venda dupla em testes de estresse de compra concorrente.

## 3.6 Estratégia de gestão do conhecimento

A gestão do conhecimento (Cláusula 6.2.6) assegura que ativos intelectuais sejam preservados e reutilizados:
- **Fonte Única da Verdade:** O PDW (`docs/constituicao/project-definition-workbook.md`) centraliza todas as decisões do produto.
- **Versionamento Centralizado:** Todos os artefatos de processo, templates de prompt e códigos residem no repositório GitHub.
- **Decisões Documentadas:** Mudanças estruturais exigem o registro de ADRs com contexto, opções e consequências.
- **Lições Aprendidas:** Registradas ao final de cada incremento para aperfeiçoar os processos subsequentes.

---
