# Matriz Completa de Rastreabilidade de Artefatos, Diagramas e Evidências

Este documento consolida a **matriz completa de rastreabilidade de todos os artefatos (visuais, tabulares, documentais e de código)** exigidos pela professora, pela norma **ABNT NBR ISO/IEC/IEEE 12207:2021** e pelo modelo **MPS.BR (MR-MPS-SW:2024)** para o *Manual de Processos de Software* do **CineDoom / CineSoft Solutions**.

Todos os artefatos estão centralizados e organizados por capítulo em `manual-processos/assets/`.

---

## 🎯 Matriz Geral de Artefatos e Entregáveis por Capítulo

| Capítulo | Código | Artefato / Entregável Formal | Natureza do Artefato | Status | Localização Central em `assets/` |
| :--- | :---: | :--- | :---: | :---: | :--- |
| **0. Identificação** | ART-001 | Logotipo Oficial da CineSoft Solutions | Imagem / Vetor | ✅ Concluído | `assets/logos/cinesoft-logo-horizontal-color.png` |
| **0. Identificação** | ART-002 | Logotipo Oficial do CineDoom | Imagem / Vetor | ✅ Concluído | `assets/logos/cinedoom-logo-horizontal-color.png` |
| **0. Identificação** | ART-003 | Tabela de Histórico de Versões do Manual | Tabela Estruturada | ✅ Concluído | `assets/capitulo-00/tabelas/historico-versoes.tex` |
| **1. Apresentação** | ART-004 | Print do Portal do Cliente (Filmes e Assentos) | Screenshot / Asset | ✅ Concluído | `assets/capitulo-01/prints/print-portal-cliente.png` |
| **1. Apresentação** | ART-005 | Print da Bilheteria / Operação de Guichê | Screenshot / Asset | ✅ Concluído | `assets/capitulo-01/prints/print-bilheteria-atendente.png` |
| **1. Apresentação** | ART-006 | Print do Painel Administrativo / Back-office | Screenshot / Asset | ✅ Concluído | `assets/capitulo-01/prints/print-painel-gerencial.png` |
| **1. Apresentação** | ART-007 | Tabela de Perfis de Usuários e Permissões | Tabela Estruturada | ✅ Concluído | `assets/capitulo-01/tabelas/perfis-usuarios-permissoes.tex` |
| **2. Processos Acordo** | ART-008 | Tabela de Análise Make or Buy (Aquisição) | Tabela Estruturada | ✅ Concluído | `assets/capitulo-02/tabelas/analise-make-or-buy.tex` |
| **2. Processos Acordo** | ART-009 | Tabela de Perspectiva de Fornecimento / Monetização | Tabela Estruturada | ✅ Concluído | `assets/capitulo-02/tabelas/perspectiva-fornecimento.tex` |
| **3. Organizacionais** | ART-010 | Diagrama do Ciclo de Vida do Projeto (Sprints Ágeis) | Diagrama PlantUML/SVG | ✅ Concluído | `assets/capitulo-03/diagramas/diagrama-ciclo-de-vida.*` |
| **3. Organizacionais** | ART-011 | Tabela de Inventário de Ferramentas e Infraestrutura | Tabela Estruturada | ✅ Concluído | `assets/capitulo-03/tabelas/inventario-ferramental.tex` |
| **3. Organizacionais** | ART-012 | Matriz RACI de Responsabilidades e Competências | Tabela Estruturada | ✅ Concluído | `assets/capitulo-03/tabelas/matriz-raci.tex` |
| **4. Gerenc. Técnico** | ART-013 | **EAP / WBS (Estrutura Analítica do Projeto de 3 Níveis)** | Diagrama PlantUML/SVG | ✅ Concluído | `assets/capitulo-04/diagramas/eap-projeto-3-niveis.*` |
| **4. Gerenc. Técnico** | ART-014 | **Print do Quadro Kanban / GitHub Projects Board** | Screenshot / Evidência | ✅ Concluído | `assets/capitulo-04/prints/print-kanban-board.png` |
| **4. Gerenc. Técnico** | ART-015 | Tabela Risk Register ($\ge 5$ riscos com respostas) | Tabela Estruturada | ✅ Concluído | `assets/capitulo-04/tabelas/registro-riscos.tex` |
| **4. Gerenc. Técnico** | ART-016 | Diagrama de Fluxo de Branches Git (GitFlow) | Diagrama PlantUML/SVG | ✅ Concluído | `assets/capitulo-04/diagramas/fluxo-git-branches.*` |
| **4. Gerenc. Técnico** | ART-017 | Matriz de Decisão Ponderada (Pugh Matrix para ADRs) | Tabela Estruturada | ✅ Concluído | `assets/capitulo-04/tabelas/matriz-pugh-decisao.tex` |
| **4. Gerenc. Técnico** | ART-018 | Tabela de Cronograma de Entregas e Marcos | Tabela Estruturada | ✅ Concluído | `assets/capitulo-04/tabelas/cronograma-marcos.tex` |
| **4. Gerenc. Técnico** | ART-019 | Gráfico / Dashboard de Métricas (Throughput / Lead Time) | Screenshot / Vetor | ✅ Concluído | `assets/capitulo-04/prints/print-metricas-projeto.png` |
| **5. Processos Técnicos** | ART-020 | Catálogo Formal de Requisitos do Sistema (RF e RNF) | Tabela Estruturada | ✅ Concluído | `assets/capitulo-05/tabelas/catalogo-requisitos.tex` |
| **5. Processos Técnicos** | ART-021 | Matriz de Rastreabilidade Ponta a Ponta | Tabela Estruturada | ✅ Concluído | `assets/capitulo-05/tabelas/matriz-rastreabilidade.tex` |
| **5. Processos Técnicos** | ART-022 | Especificação de Critérios de Aceitação Formal | Tabela Estruturada | ✅ Concluído | `assets/capitulo-05/tabelas/criterios-aceitacao.tex` |
| **5. Processos Técnicos** | ART-023 | **Diagrama C4 Nível 2 (Contêineres da Aplicação)** | Diagrama PlantUML/PDF | ✅ Concluído | `assets/capitulo-05/diagramas/c4-containers.*` |
| **5. Processos Técnicos** | ART-024 | **Diagrama de Classes UML (Modelo de Domínio CineDoom)** | Diagrama PlantUML/PDF | ✅ Concluído | `assets/capitulo-05/diagramas/diagrama-classes-dominio.*` |
| **5. Processos Técnicos** | ART-025 | **Diagrama de Sequência UML (Reserva Atômica e Baixa no Balcão)** | Diagrama PlantUML/PDF | ✅ Concluído | `assets/capitulo-05/diagramas/diagrama-sequencia.*` |
| **5. Processos Técnicos** | ART-026 | **Print da Suíte de Testes Automatizados (Vitest 748)** | Screenshot / Evidência | ✅ Concluído | `assets/capitulo-05/prints/print-testes-unitarios-vitest.png` |
| **5. Processos Técnicos** | ART-027 | Quadro Comparativo de Verificação vs. Validação | Tabela Estruturada | ✅ Concluído | `assets/capitulo-05/tabelas/verificacao-validacao.tex` |
| **5. Processos Técnicos** | ART-028 | **Diagrama de Cadeia de Rastreabilidade (Macroentrega → Sprint → Necessidade → RF → CA → Código → Teste)** | Diagrama PlantUML/PDF | ✅ Concluído | `assets/capitulo-05/diagramas/diagrama-rastreabilidade.*` |
| **6. Avaliação Processo**| ART-029 | Tabela de Diagnóstico do Manual (4 Perguntas MPS.BR) | Tabela Estruturada | ✅ Concluído | `assets/capitulo-06/tabelas/diagnostico-processo.tex` |
| **6. Avaliação Processo**| ART-030 | Tabela do Plano de Melhoria de Processo (PMP 5 Campos)| Tabela Estruturada | ✅ Concluído | `assets/capitulo-06/tabelas/plano-melhoria-pmp.tex` |
| **6. Avaliação Processo**| ART-031 | **Print do Kanban com a Melhoria Aplicada** | Screenshot / Evidência | ✅ Concluído | `assets/capitulo-06/prints/print-evidencia-melhoria-kanban.png` |
