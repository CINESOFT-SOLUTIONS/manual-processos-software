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
| **2. Processos de Acordo** | Print de Console de Serviço Externo (Neon/Vercel) | Screenshot | Opcional | `assets/prints/print-console-servico-nuvem.png` |
| **3. Processos Organizacionais** | Diagrama do Ciclo de Vida do Projeto (Sprints) | Diagrama | Recomendado | `assets/diagrams/diagrama-ciclo-de-vida.png` ou Mermaid |
| **3. Processos Organizacionais** | Tabela de Inventário de Ferramentas | Tabela | Obrigatório | Embutida no texto (`03-processos-organizacionais.md`) |
| **3. Processos Organizacionais** | Matriz RACI de Responsabilidades da Equipe | Tabela | Obrigatório | Embutida no texto (`03-processos-organizacionais.md`) |
| **4. Gerenciamento Técnico** | **Print do Quadro Kanban / GitHub Projects** | Screenshot | **Obrigatório** | `assets/prints/print-kanban-board.png` |
| **4. Gerenciamento Técnico** | Tabela Risk Register (Matriz de Riscos) | Tabela | Obrigatório | Embutida no texto (`04-gerenciamento-tecnico.md`) |
| **4. Gerenciamento Técnico** | Diagrama de Fluxo de Branches Git | Diagrama | Recomendado | `assets/diagrams/fluxo-git-branches.png` ou Mermaid |
| **4. Gerenciamento Técnico** | Fichas Estruturadas de ADRs | Cards | Obrigatório | Embutida no texto e em `specs/adrs/` |
| **4. Gerenciamento Técnico** | Print / Gráfico de Métricas de Projeto | Screenshot | Recomendado | `assets/prints/print-metricas-projeto.png` |
| **5. Processos Técnicos** | **Diagrama C4 Nível 2 (Contêineres)** | Diagrama | **Obrigatório** | `assets/diagrams/c4-containers.png` ou Mermaid |
| **5. Processos Técnicos** | **Diagrama de Sequência UML da Reserva** | Diagrama | **Obrigatório** | `assets/diagrams/diagrama-sequencia-reserva.png` ou Mermaid |
| **5. Processos Técnicos** | Tabela de Catálogo de Requisitos (RF/RNF) | Tabela | Obrigatório | Embutida no texto (`05-processos-tecnicos.md`) |
| **5. Processos Técnicos** | Matriz de Rastreabilidade Ponta a Ponta | Tabela | Obrigatório | Embutida no texto (`05-processos-tecnicos.md`) |
| **5. Processos Técnicos** | Print da Suíte de Testes Unitários (`vitest`) | Screenshot | **Obrigatório** | `assets/prints/print-testes-unitarios-vitest.png` |
| **5. Processos Técnicos** | Print da Pipeline de CI/CD (GitHub Actions) | Screenshot | Recomendado | `assets/prints/print-pipeline-ci-cd.png` |
| **5. Processos Técnicos** | Tabela Comparativa Verificação vs. Validação | Tabela | Obrigatório | Embutida no texto (`05-processos-tecnicos.md`) |
| **5. Processos Técnicos** | Relatório de Testes de Aceitação | Tabela | Obrigatório | Embutida no texto (`05-processos-tecnicos.md`) |
| **6. Avaliação e Melhoria** | Tabela de Diagnóstico MPS.BR (4 perguntas) | Tabela | Obrigatório | Embutida no texto (`orientacoes-capitulo-6.md`) |
| **6. Avaliação e Melhoria** | Tabela do Plano de Ação de Melhoria | Tabela | Obrigatório | Embutida no texto (`orientacoes-capitulo-6.md`) |
| **6. Avaliação e Melhoria** | Bloco Diff "Antes vs. Depois" do Trecho Revisado | Bloco Código | Obrigatório | Embutida no texto (`orientacoes-capitulo-6.md`) |
| **6. Avaliação e Melhoria** | **Print do Kanban / Issue com a Melhoria Aplicada** | Screenshot | **Obrigatório** | `assets/prints/print-evidencia-melhoria-kanban.png` |

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
- [ ] (Opcional) Screenshot do console do Neon PostgreSQL ou Vercel

### Capítulo 3 — Processos Organizacionais Habilitadores (ISO 12207 §6.2)
- [ ] Diagrama de fluxo do ciclo de vida iterativo (Sprints de 2 semanas)
- [x] Tabela de inventário de ferramentas por categorias
- [x] Matriz RACI com atribuição por membro da equipe

### Capítulo 4 — Gerenciamento Técnico (ISO 12207 §6.3)
- [ ] **Print do GitHub Projects / Kanban:** Capturar quadro com tarefas em colunas e responsáveis atribuídos
- [x] Tabela de Gestão de Riscos (*Risk Register*) com probabilidade e impacto
- [ ] Diagrama do fluxo de branches Git (`main`, `develop`, `feat/`)
- [x] Fichas de ADRs (ADR-001 a ADR-005)
- [ ] Print ou gráfico de métricas de acompanhamento (Lead time / Issues)

### Capítulo 5 — Processos Técnicos (ISO 12207 §6.4)
- [ ] **Diagrama 1 (Obrigatório):** C4 Model Nível 2 (Contêineres)
- [ ] **Diagrama 2 (Obrigatório):** Sequência UML da reserva atômica (*SELECT FOR UPDATE*)
- [x] Catálogo de Requisitos Funcionais e Não Funcionais
- [x] Matriz de Rastreabilidade Requisito $\to$ Código $\to$ Testes
- [ ] **Print do Terminal de Testes:** Executar `npm test` no `cinedoom-app` e capturar a suíte 100% verde
- [ ] **Print do GitHub Actions:** Capturar pipeline de CI/CD bem-sucedida
- [x] Tabela comparativa Verificação vs. Validação
- [x] Tabela de homologação de testes de aceitação por stakeholder

### Capítulo 6 — Avaliação e Melhoria (MPS.BR / MR-MPS-SW)
- [ ] Tabela de diagnóstico das 4 perguntas preenchida
- [ ] Plano de melhoria formalizado (5 campos)
- [ ] Bloco de texto comparativo Antes vs. Depois
- [ ] **Print de evidência prática:** Capturar quadro Kanban atualizado ou PR comprovando que a melhoria foi adotada

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
3. **Inclusão nos Capítulos:** Sempre acompanhar a imagem de uma legenda explicativa no texto:
   ```markdown
   ![Figura X: Diagrama C4 Nível 2 - Contêineres da Aplicação CineDoom](assets/diagrams/c4-containers.png)
   ```
