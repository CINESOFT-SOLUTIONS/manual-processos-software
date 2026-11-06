# Mapa de Artefatos Visuais e Evidências do Manual

Este documento consolida o **checklist e mapa de rastreabilidade de todos os artefatos visuais, diagramas técnicos, prints de ferramentas e tabelas estruturadas** necessários para a composição do *Manual de Processos de Software* da **CineSoft Solutions / CineDoom**.

A equipe pode usar esta página para acompanhar o status de produção e inserção de cada asset visual.

---

## 🎯 Quadro Resumo de Artefatos por Capítulo

| Capítulo | Artefato / Asset Visual | Tipo | Obrigatoriedade | Caminho Recomendado no Repositório |
| :--- | :--- | :---: | :---: | :--- |
| **0. Capa / Identificação** | Logotipo da CineSoft Solutions | Imagem | Obrigatório | `assets/logos/cinesoft-logo-horizontal-color.png` |
| **0. Capa / Identificação** | Logotipo do CineDoom | Imagem | Obrigatório | `assets/logos/cinedoom-logo-horizontal-color.png` |
| **0. Capa / Identificação** | Tabela de Histórico de Versões | Tabela | Obrigatório | Embutida no texto (`00-identificacao.md`) |
| **1. Apresentação do Software** | Print do Portal do Cliente (Filmes e Assentos) | Screenshot | Recomendado | `assets/prints/print-portal-cliente.png` |
| **1. Apresentação do Software** | Print da Bilheteria / Operação de Guichê | Screenshot | Recomendado | `assets/prints/print-bilheteria-atendente.png` |
| **1. Apresentação do Software** | Print do Painel Administrativo / Back-office | Screenshot | Recomendado | `assets/prints/print-painel-gerencial.png` |
| **2. Processos de Acordo** | Tabela de Análise Make or Buy | Tabela | Obrigatório | Embutida no texto (`02-processos-acordo.md`) |
| **2. Processos de Acordo** | Tabela de Perspectiva de Fornecimento | Tabela | Obrigatório | Embutida no texto (`02-processos-acordo.md`) |
| **2. Processos de Acordo** | Cláusula de SLA e Termo de Aceite | Tabela / Texto | Obrigatório | Embutida no texto (`02-processos-acordo.md`) |
| **2. Processos de Acordo** | Print de Console de Serviço Externo (Neon/Vercel) | Screenshot | Opcional | `assets/prints/print-console-servico-nuvem.png` |
| **3. Processos Organizacionais** | Diagrama do Ciclo de Vida do Projeto (Sprints) | Diagrama | Recomendado | `assets/diagrams/diagrama-ciclo-de-vida.png` ou Mermaid |
| **3. Processos Organizacionais** | Tabela de Inventário de Ferramentas | Tabela | Obrigatório | Embutida no texto (`03-processos-organizacionais.md`) |
| **3. Processos Organizacionais** | Matriz RACI de Responsabilidades da Equipe | Tabela | Obrigatório | Embutida no texto (`03-processos-organizacionais.md`) |
| **4. Gerenciamento Técnico** | **EAP (Estrutura Analítica do Projeto / WBS de 3 Níveis)** | Diagrama | **Obrigatório** *(Slide 08 Aula 05)* | `assets/diagrams/eap-projeto-3-niveis.png` ou Mermaid |
| **4. Gerenciamento Técnico** | **Print do Quadro Kanban / GitHub Projects** | Screenshot | **Obrigatório** | `assets/prints/print-kanban-board.png` |
| **4. Gerenciamento Técnico** | Tabela Risk Register ($\ge 5$ riscos com probabilidade/impacto) | Tabela | Obrigatório *(Slide 13 Aula 05)* | Embutida no texto (`04-gerenciamento-tecnico.md`) |
| **4. Gerenciamento Técnico** | Diagrama de Fluxo de Branches Git | Diagrama | Recomendado | `assets/diagrams/fluxo-git-branches.png` ou Mermaid |
| **4. Gerenciamento Técnico** | Matriz de Decisão Ponderada (Pugh Matrix para ADRs) | Tabela | Recomendado *(Slide 13 Aula 05)* | Embutida no texto (`04-gerenciamento-tecnico.md`) |
| **4. Gerenciamento Técnico** | Fichas Estruturadas de ADRs (ADR-001 a ADR-005) | Cards | Obrigatório | Embutida no texto e em `specs/adrs/` |
| **4. Gerenciamento Técnico** | Print / Gráfico de Métricas de Projeto (Throughput/Lead Time) | Screenshot | Recomendado | `assets/prints/print-metricas-projeto.png` |
| **5. Processos Técnicos** | **Diagrama C4 Nível 2 (Contêineres)** | Diagrama | **Obrigatório** *(Slide 24 Aula 06)* | `assets/diagrams/c4-containers.png` ou Mermaid |
| **5. Processos Técnicos** | **Diagrama de Classes UML (Modelo de Domínio)** | Diagrama | **Obrigatório** *(Slide 24 Aula 06)* | `assets/diagrams/diagrama-classes-dominio.png` ou Mermaid |
| **5. Processos Técnicos** | **Diagrama de Sequência UML da Reserva de Assentos** | Diagrama | **Obrigatório** *(Slide 24 Aula 06)* | `assets/diagrams/diagrama-sequencia-reserva.png` ou Mermaid |
| **5. Processos Técnicos** | **Diagrama de Casos de Uso UML (Atores e Ações)** | Diagrama | Recomendado | `assets/diagrams/diagrama-casos-de-uso.png` ou Mermaid |
| **5. Processos Técnicos** | **Diagrama de Estados UML (Ciclo do Assento)** | Diagrama | Recomendado | `assets/diagrams/diagrama-estados-assento.png` ou Mermaid |
| **5. Processos Técnicos** | **Diagrama de Modelo de Dados / DER (Banco de Dados)** | Diagrama | **Obrigatório** *(Slide 19 Aula 06)* | `assets/diagrams/diagrama-er-banco.png` ou Mermaid |
| **5. Processos Técnicos** | Tabela de Catálogo de Requisitos (RF/RNF com IDs únicos) | Tabela | Obrigatório | Embutida no texto (`05-processos-tecnicos.md`) |
| **5. Processos Técnicos** | Matriz de Rastreabilidade Ponta a Ponta | Tabela | Obrigatório | Embutida no texto (`05-processos-tecnicos.md`) |
| **5. Processos Técnicos** | **Print da Suíte de Testes Unitários (`vitest`)** | Screenshot | **Obrigatório** | `assets/prints/print-testes-unitarios-vitest.png` |
| **5. Processos Técnicos** | Print da Pipeline de CI/CD (GitHub Actions verde) | Screenshot | Recomendado | `assets/prints/print-pipeline-ci-cd.png` |
| **5. Processos Técnicos** | Tabela Comparativa Verificação vs. Validação | Tabela | Obrigatório *(Slide 33 Aula 06)* | Embutida no texto (`05-processos-tecnicos.md`) |
| **5. Processos Técnicos** | Critérios de Entrada e Saída de V&V (Entry/Exit Criteria) | Tabela | Obrigatório *(Slide 37 Aula 06)* | Embutida no texto (`05-processos-tecnicos.md`) |
| **5. Processos Técnicos** | Procedimento de Rollback no Plano de Implantação | Texto / Fluxo | Obrigatório *(Slide 31 Aula 06)* | Embutida no texto (`05-processos-tecnicos.md`) |
| **5. Processos Técnicos** | Relatório de Testes de Aceitação / UAT por Stakeholder | Tabela | Obrigatório | Embutida no texto (`05-processos-tecnicos.md`) |
| **6. Avaliação e Melhoria** | Tabela de Diagnóstico MPS.BR (4 perguntas) | Tabela | Obrigatório *(Slide 24 Aula 07)* | Embutida no texto (`orientacoes-capitulo-6.md`) |
| **6. Avaliação e Melhoria** | Tabela do Plano de Ação de Melhoria (5 campos) | Tabela | Obrigatório *(Slide 24 Aula 07)* | Embutida no texto (`orientacoes-capitulo-6.md`) |
| **6. Avaliação e Melhoria** | Bloco Diff "Antes vs. Depois" do Trecho Revisado | Bloco Código | Obrigatório *(Slide 24 Aula 07)* | Embutida no texto (`orientacoes-capitulo-6.md`) |
| **6. Avaliação e Melhoria** | **Print do Kanban / Issue com a Melhoria Aplicada** | Screenshot | **Obrigatório** *(Slide 25 Aula 07)* | `assets/prints/print-evidencia-melhoria-kanban.png` |

---

## 📋 Checklist Detalhado para a Equipe

### Capítulo 0 — Identificação e Versões
- [x] Logotipos oficiais em alta resolução (`assets/logos/`)
- [x] Tabela de histórico de versões estruturada

### Capítulo 1 — Apresentação do Software
- [ ] Screenshot 1: Portal do Cliente com catálogo de filmes e seleção de assentos
- [ ] Screenshot 2: Ponto de venda presencial (balcão da bilheteria)
- [ ] Screenshot 3: Painel de gestão do cinema (salas e sessões)

### Capítulo 2 — Processos de Acordo (ISO 12207 §6.1)
- [x] Tabela Make or Buy com classificação *Sim / Não / Parcial*
- [x] Tabela de Fornecimento com modelos de licenciamento (SaaS/API)
- [x] Especificação de SLA e modelo de Termo de Aceite do serviço
- [ ] (Opcional) Screenshot do console do Neon PostgreSQL ou Vercel

### Capítulo 3 — Processos Organizacionais Habilitadores (ISO 12207 §6.2)
- [ ] Diagrama de fluxo do ciclo de vida iterativo (Sprints de 2 semanas)
- [x] Tabela de inventário de ferramentas por categorias
- [x] Matriz RACI com atribuição por membro da equipe

### Capítulo 4 — Gerenciamento Técnico (ISO 12207 §6.3)
- [ ] **EAP / WBS visual com pelo menos 3 níveis** (definindo macrofases, pacotes de trabalho e entregáveis) *(Aula 05 Slide 08)*
- [ ] **Print do GitHub Projects / Kanban:** Capturar quadro com tarefas em colunas e responsáveis atribuídos
- [x] Tabela de Gestão de Riscos (*Risk Register*) com $\ge 5$ riscos e plano de resposta para os 3 críticos *(Aula 05 Slide 13)*
- [ ] Diagrama do fluxo de branches Git (`main`, `develop`, `feat/`)
- [x] Matriz de Decisão Ponderada (Pugh Matrix com critérios, pesos e notas para respaldar a ADR principal) *(Aula 05 Slide 13)*
- [x] Fichas de ADRs (ADR-001 a ADR-005)
- [ ] Print ou gráfico de métricas de acompanhamento (Lead time / Issues / Burndown)

### Capítulo 5 — Processos Técnicos (ISO 12207 §6.4)
- [ ] **Diagrama 1 (Obrigatório):** C4 Model Nível 2 (Contêineres da aplicação)
- [ ] **Diagrama 2 (Obrigatório):** Diagrama de Classes UML (Modelo de Domínio: `User`, `Movie`, `Session`, `Reservation`, `Ticket`, etc.)
- [ ] **Diagrama 3 (Obrigatório):** Sequência UML da reserva atômica (*SELECT FOR UPDATE*)
- [ ] **Diagrama 4 (Recomendado):** Diagrama de Casos de Uso UML (Atores: Espectador, Atendente, Gerente)
- [ ] **Diagrama 5 (Recomendado):** Diagrama de Estados UML (Máquina de estados da poltrona: `AVAILABLE`, `RESERVED`, `SOLD`)
- [ ] **Diagrama 6 (Obrigatório):** Modelo Entidade-Relacionamento (DER do PostgreSQL) *(Aula 06 Slide 19)*
- [x] Catálogo de Requisitos Funcionais e Não Funcionais com IDs únicos
- [x] Matriz de Rastreabilidade Requisito $\to$ Código $\to$ Testes
- [ ] **Print do Terminal de Testes:** Executar `npm test` no `cinedoom-app` e capturar a suíte 100% verde
- [ ] **Print do GitHub Actions:** Capturar pipeline de CI/CD bem-sucedida
- [x] Tabela comparativa Verificação vs. Validação
- [x] Critérios de Entrada e Saída (Entry/Exit Criteria) para o processo de V&V *(Aula 06 Slide 37)*
- [x] Procedimento formal de Rollback para o plano de transição/deploy *(Aula 06 Slide 31)*
- [x] Tabela de homologação de testes de aceitação (UAT) por stakeholder

### Capítulo 6 — Avaliação e Melhoria (MPS.BR / MR-MPS-SW)
- [ ] Tabela de diagnóstico das 4 perguntas preenchida
- [ ] Plano de melhoria formalizado (5 campos)
- [ ] Bloco de texto comparativo Antes vs. Depois
- [ ] **Print de evidência prática:** Capturar quadro Kanban atualizado ou PR comprovando que a melhoria foi adotada *(Aula 07 Slide 25)*

---

## 📐 Padrões Técnicos para os Assets

1. **Formatos de Imagem:**
   - Prints de tela: `.png` nítido em resolução padrão desktop (1920x1080 ou janela ajustada), sem cortes de informações essenciais.
   - Diagramas: salvar em `.png` (ou `.svg`) em `assets/diagrams/` **OU** embutir o código Mermaid diretamente no Markdown com o bloco:
     ````markdown
     ```mermaid
     flowchart TD
     ...
     ```
     ````
2. **Nomenclatura Padrão:** Usar nomes descritivos em minúsculas com hífen:
   - Exemplo: `assets/prints/print-kanban-board.png`
   - Exemplo: `assets/diagrams/c4-containers.png`
   - Exemplo: `assets/diagrams/eap-projeto-3-niveis.png`
3. **Inclusão nos Capítulos:** Sempre acompanhar a imagem de uma legenda explicativa no texto:
   ```markdown
   ![Figura X: Diagrama C4 Nível 2 - Contêineres da Aplicação CineDoom](assets/diagrams/c4-containers.png)
   ```
