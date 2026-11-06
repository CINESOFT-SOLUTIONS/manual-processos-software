# Mapa Completo de Artefatos, Diagramas e Evidências do Manual

Este documento consolida a **matriz completa de rastreabilidade de todos os artefatos (visuais, tabulares, documentais e de código)** exigidos pela professora, pela norma **ABNT NBR ISO/IEC/IEEE 12207:2021** e pelo modelo **MPS.BR (MR-MPS-SW:2024)** para o *Manual de Processos de Software* do **CineDoom / CineSoft Solutions**.

---

## 🎯 Matriz Geral de Artefatos e Entregáveis por Capítulo

| Capítulo | Código | Artefato / Entregável Formal | Natureza do Artefato | Obrigatoriedade | Localização / Caminho no Repositório |
| :--- | :---: | :--- | :---: | :---: | :--- |
| **0. Identificação** | ART-001 | Logotipo Oficial da CineSoft Solutions | Imagem / Vetor | **Obrigatório** | `assets/logos/cinesoft-logo-horizontal-color.png` |
| **0. Identificação** | ART-002 | Logotipo Oficial do CineDoom | Imagem / Vetor | **Obrigatório** | `assets/logos/cinedoom-logo-horizontal-color.png` |
| **0. Identificação** | ART-003 | Tabela de Histórico de Versões do Manual | Tabela Estruturada | **Obrigatório** | `manual/capitulos/00-identificacao.md` |
| **1. Apresentação** | ART-004 | Print do Portal do Cliente (Filmes e Assentos) | Screenshot / Asset | Recomendado | `assets/prints/print-portal-cliente.png` |
| **1. Apresentação** | ART-005 | Print da Bilheteria / Operação de Guichê | Screenshot / Asset | Recomendado | `assets/prints/print-bilheteria-atendente.png` |
| **1. Apresentação** | ART-006 | Print do Painel Administrativo / Back-office | Screenshot / Asset | Recomendado | `assets/prints/print-painel-gerencial.png` |
| **1. Apresentação** | ART-007 | Especificação de Escopo e Funcionalidades Centrais | Documental / Tópico | **Obrigatório** | `manual/capitulos/01-apresentacao-software.md` |
| **1. Apresentação** | ART-008 | Registro de Restrições Técnicas e Premissas (LGPD) | Documental / Tópico | **Obrigatório** | `manual/capitulos/01-apresentacao-software.md` |
| **2. Processos Acordo** | ART-009 | Tabela de Análise Make or Buy (Aquisição) | Tabela Estruturada | **Obrigatório** | `manual/capitulos/02-processos-acordo.md` |
| **2. Processos Acordo** | ART-010 | Tabela de Perspectiva de Fornecimento / Monetização | Tabela Estruturada | **Obrigatório** | `manual/capitulos/02-processos-acordo.md` |
| **2. Processos Acordo** | ART-011 | Matriz de Identificação de Fornecedores e Parceiros | Tabela / Tópico | **Obrigatório** | `manual/capitulos/02-processos-acordo.md` |
| **2. Processos Acordo** | ART-012 | Minuta de SLA e Termo de Aceite do Fornecimento | Tabela / Contratual | **Obrigatório** | `manual/capitulos/02-processos-acordo.md` |
| **2. Processos Acordo** | ART-013 | Print de Console de Serviços em Nuvem (Neon/Vercel) | Screenshot / Asset | Opcional | `assets/prints/print-console-servico-nuvem.png` |
| **3. Organizacionais** | ART-014 | Diagrama do Ciclo de Vida do Projeto (Sprints Ágeis) | Diagrama Técnico | Recomendado | `assets/diagrams/diagrama-ciclo-de-vida.png` ou Mermaid |
| **3. Organizacionais** | ART-015 | Tabela de Inventário de Ferramentas e Infraestrutura | Tabela Estruturada | **Obrigatório** | `manual/capitulos/03-processos-organizacionais.md` |
| **3. Organizacionais** | ART-016 | Estudo de Justificativa Estratégica e Viabilidade | Documental / Tópico | **Obrigatório** | `manual/capitulos/03-processos-organizacionais.md` |
| **3. Organizacionais** | ART-017 | Matriz RACI de Responsabilidades e Capacitação | Tabela Estruturada | **Obrigatório** | `manual/capitulos/03-processos-organizacionais.md` |
| **3. Organizacionais** | ART-018 | Plano de Qualidade Organizacional e Métricas | Documental / Tópico | **Obrigatório** | `manual/capitulos/03-processos-organizacionais.md` |
| **3. Organizacionais** | ART-019 | Política e Estratégia de Gestão do Conhecimento | Documental / Tópico | **Obrigatório** | `manual/capitulos/03-processos-organizacionais.md` |
| **4. Gerenc. Técnico** | ART-020 | **EAP / WBS (Estrutura Analítica do Projeto de 3 Níveis)** | Diagrama Estrutural | **Obrigatório** *(Aula 05)* | `assets/diagrams/eap-projeto-3-niveis.png` ou Mermaid |
| **4. Gerenc. Técnico** | ART-021 | **Print do Quadro Kanban / GitHub Projects Board** | Screenshot / Evidência | **Obrigatório** | `assets/prints/print-kanban-board.png` |
| **4. Gerenc. Técnico** | ART-022 | Tabela Risk Register ($\ge 5$ riscos com probabilidade/impacto) | Tabela Estruturada | **Obrigatório** *(Aula 05)* | `manual/capitulos/04-gerenciamento-tecnico.md` |
| **4. Gerenc. Técnico** | ART-023 | Diagrama de Fluxo de Branches Git (Git Flow / Trunk) | Diagrama Técnico | Recomendado | `assets/diagrams/fluxo-git-branches.png` ou Mermaid |
| **4. Gerenc. Técnico** | ART-024 | Matriz de Decisão Ponderada (Pugh Matrix para ADRs) | Tabela Estruturada | **Obrigatório** *(Aula 05)* | `manual/capitulos/04-gerenciamento-tecnico.md` |
| **4. Gerenc. Técnico** | ART-025 | Fichas de Decisões Arquiteturais (ADR-001 a ADR-012) | Fichas / Markdown | **Obrigatório** | `specs/adrs/` e Cap. 4.4 |
| **4. Gerenc. Técnico** | ART-026 | Gráfico / Dashboard de Métricas (Throughput / Lead Time) | Screenshot / Gráfico | Recomendado | `assets/prints/print-metricas-projeto.png` |
| **5. Processos Técnicos** | ART-027 | Catálogo Formal de Requisitos do Sistema (RF e RNF) | Tabela Estruturada | **Obrigatório** | `manual/capitulos/05-processos-tecnicos.md` |
| **5. Processos Técnicos** | ART-028 | Matriz de Rastreabilidade Ponta a Ponta (RF $\leftrightarrow$ Código $\leftrightarrow$ Teste) | Matriz Tabular | **Obrigatório** | `manual/capitulos/05-processos-tecnicos.md` |
| **5. Processos Técnicos** | ART-029 | Especificação de Critérios de Aceitação por Requisito | Tabela / Regras | **Obrigatório** | `manual/capitulos/05-processos-tecnicos.md` |
| **5. Processos Técnicos** | ART-030 | Registro de Stakeholders e Técnicas de Elicitação | Documental / Tópico | **Obrigatório** | `manual/capitulos/05-processos-tecnicos.md` |
| **5. Processos Técnicos** | ART-031 | Documento de Arquitetura do Sistema (Visão Geral/Camadas) | Documental / SAD | **Obrigatório** | `manual/capitulos/05-processos-tecnicos.md` |
| **5. Processos Técnicos** | ART-032 | **Diagrama C4 Nível 2 (Contêineres da Aplicação)** | Diagrama Arquitetura | **Obrigatório** *(Aula 06)* | `assets/diagrams/c4-containers.png` ou Mermaid |
| **5. Processos Técnicos** | ART-033 | **Diagrama de Classes UML (Modelo de Domínio CineDoom)** | Diagrama UML | **Obrigatório** *(Aula 06)* | `assets/diagrams/diagrama-classes-dominio.png` ou Mermaid |
| **5. Processos Técnicos** | ART-034 | **Diagrama de Sequência UML (Reserva Atômica e Baixa)** | Diagrama UML | **Obrigatório** *(Aula 06)* | `assets/diagrams/diagrama-sequencia-reserva.png` ou Mermaid |
| **5. Processos Técnicos** | ART-035 | **Diagrama de Casos de Uso UML (Atores e Ações)** | Diagrama UML | Recomendado | `assets/diagrams/diagrama-casos-de-uso.png` ou Mermaid |
| **5. Processos Técnicos** | ART-036 | **Diagrama de Máquina de Estados UML (Ciclo da Poltrona)** | Diagrama UML | Recomendado | `assets/diagrams/diagrama-estados-assento.png` ou Mermaid |
| **5. Processos Técnicos** | ART-037 | **Diagrama Entidade-Relacionamento (DER PostgreSQL)** | Diagrama Dados | **Obrigatório** *(Aula 06)* | `assets/diagrams/diagrama-er-banco.png` ou Mermaid |
| **5. Processos Técnicos** | ART-038 | Guia de Padrões de Codificação (TypeScript/ESLint/Prettier) | Documental / Tópico | **Obrigatório** | `manual/capitulos/05-processos-tecnicos.md` |
| **5. Processos Técnicos** | ART-039 | Plano de Integração Contínua e Procedimento de Rollback | Documental / Fluxo | **Obrigatório** *(Aula 06)* | `manual/capitulos/05-processos-tecnicos.md` |
| **5. Processos Técnicos** | ART-040 | **Print da Suíte de Testes Automatizados (Vitest 748 verdes)** | Screenshot / Evidência | **Obrigatório** | `assets/prints/print-testes-unitarios-vitest.png` |
| **5. Processos Técnicos** | ART-041 | **Print da Pipeline de CI/CD (GitHub Actions aprovada)** | Screenshot / Evidência | Recomendado | `assets/prints/print-pipeline-ci-cd.png` |
| **5. Processos Técnicos** | ART-042 | Quadro Comparativo de Verificação vs. Validação | Tabela Estruturada | **Obrigatório** *(Aula 06)* | `manual/capitulos/05-processos-tecnicos.md` |
| **5. Processos Técnicos** | ART-043 | Tabela de Critérios de Entrada e Saída de V&V | Tabela Estruturada | **Obrigatório** *(Aula 06)* | `manual/capitulos/05-processos-tecnicos.md` |
| **5. Processos Técnicos** | ART-044 | Relatório de Testes de Aceitação / UAT por Stakeholder | Tabela Estruturada | **Obrigatório** | `manual/capitulos/05-processos-tecnicos.md` |
| **5. Processos Técnicos** | ART-045 | Plano de Transição / Procedimentos de Deploy em Produção | Documental / Tópico | **Obrigatório** | `manual/capitulos/05-processos-tecnicos.md` |
| **5. Processos Técnicos** | ART-046 | Procedimentos de Operação, Manutenção e Descontinuação | Documental / Tópico | **Obrigatório** | `manual/capitulos/05-processos-tecnicos.md` |
| **6. Avaliação Processo**| ART-047 | Referencial e Recorte MPS.BR (Processo Gerência de Projetos)| Documental / Tópico | **Obrigatório** *(Aula 07)* | `referencias/diretrizes/capitulos/orientacoes-capitulo-6.md` |
| **6. Avaliação Processo**| ART-048 | Tabela de Diagnóstico do Manual (4 Perguntas Didáticas) | Tabela Estruturada | **Obrigatório** *(Aula 07)* | `referencias/diretrizes/capitulos/orientacoes-capitulo-6.md` |
| **6. Avaliação Processo**| ART-049 | Tabela do Plano de Melhoria de Processo (5 Campos) | Tabela Estruturada | **Obrigatório** *(Aula 07)* | `referencias/diretrizes/capitulos/orientacoes-capitulo-6.md` |
| **6. Avaliação Processo**| ART-050 | Bloco Comparativo Antes vs. Depois da Seção Revisada | Bloco de Código/Diff | **Obrigatório** *(Aula 07)* | `referencias/diretrizes/capitulos/orientacoes-capitulo-6.md` |
| **6. Avaliação Processo**| ART-051 | **Print do Kanban / Issue com a Melhoria Aplicada** | Screenshot / Evidência | **Obrigatório** *(Aula 07)* | `assets/prints/print-evidencia-melhoria-kanban.png` |

---

## 📋 Checklist de Execução para a Equipe

- [x] **ART-001 / ART-002:** Identidade visual e logotipos oficiais (`assets/logos/`)
- [x] **ART-003:** Histórico de versões estruturado no cabeçalho do manual
- [ ] **ART-004:** Print do Portal do Cliente (catálogo e assentos)
- [ ] **ART-005:** Print da Bilheteria presencial (guichê do atendente)
- [ ] **ART-006:** Print do Painel Administrativo do gerente
- [x] **ART-007 / ART-008:** Escopo, funcionalidades, restrições e premissas LGPD
- [x] **ART-009 / ART-010:** Tabelas de Aquisição (Make/Buy) e Fornecimento
- [x] **ART-011 / ART-012:** Matriz de Parceiros e Minuta de SLA/Termo de Aceite
- [ ] **ART-013:** Print de console em nuvem (Neon/Vercel)
- [ ] **ART-014:** Diagrama visual do Ciclo de Vida (Sprints)
- [x] **ART-015 / ART-016:** Inventário de Ferramentas e Justificativa de Viabilidade
- [x] **ART-017:** Matriz RACI de responsabilidades
- [x] **ART-018 / ART-019:** Plano de Qualidade e Gestão do Conhecimento
- [ ] **ART-020:** **Diagrama EAP / WBS de 3 Níveis** *(Slide 08 Aula 05)*
- [ ] **ART-021:** **Print do Quadro Kanban / GitHub Projects**
- [x] **ART-022:** Tabela Risk Register com $\ge 5$ riscos mapeados
- [ ] **ART-023:** Diagrama de fluxo de branches Git
- [x] **ART-024:** Matriz de Decisão Ponderada (Pugh Matrix para a ADR principal)
- [x] **ART-025:** Fichas formais de ADRs (ADR-001 a ADR-012 em `specs/adrs/`)
- [ ] **ART-026:** Gráfico ou print de métricas do projeto
- [x] **ART-027 / ART-028:** Catálogo RF/RNF e Matriz de Rastreabilidade Ponta a Ponta
- [x] **ART-029 / ART-030:** Critérios de Aceitação e Registro de Stakeholders
- [x] **ART-031:** Documento de Arquitetura do Sistema (Clean Architecture / Monólito Modular)
- [ ] **ART-032:** **Diagrama C4 Nível 2 (Contêineres)** *(Slide 24 Aula 06)*
- [ ] **ART-033:** **Diagrama de Classes UML (Modelo de Domínio)** *(Slide 24 Aula 06)*
- [ ] **ART-034:** **Diagrama de Sequência UML da Reserva Atômica** *(Slide 24 Aula 06)*
- [ ] **ART-035:** **Diagrama de Casos de Uso UML**
- [ ] **ART-036:** **Diagrama de Máquina de Estados UML da Poltrona**
- [ ] **ART-037:** **Diagrama Entidade-Relacionamento (DER PostgreSQL)** *(Slide 19 Aula 06)*
- [x] **ART-038 / ART-039:** Padrões de código, Plano de Integração e Procedimento de Rollback
- [ ] **ART-040:** **Print do Terminal de Testes Vitest (748 testes verdes)**
- [ ] **ART-041:** **Print do GitHub Actions (Pipeline verde)**
- [x] **ART-042 / ART-043:** Quadro comparativo V vs V e Critérios de Entrada/Saída
- [x] **ART-044 / ART-045:** Relatório de Testes de Aceitação e Plano de Transição
- [x] **ART-046:** Procedimentos de Operação, Manutenção e Descontinuação
- [ ] **ART-047 / ART-048:** Referencial MPS.BR e Diagnóstico das 4 perguntas do manual
- [ ] **ART-049 / ART-050:** Plano de Melhoria e Bloco Diff Antes vs. Depois
- [ ] **ART-051:** **Print do Kanban / Issue comprovando a aplicação prática da melhoria** *(Slide 25 Aula 07)*
