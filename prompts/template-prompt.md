# Template de Prompt — Modelagem de Processos

## 1. Identificação
- **Código/Nome do Prompt:** `PR-XX_NomeDoPrompt`
- **Objetivo:** [Breve descrição do objetivo, ex: gerar atividades do processo de medição]
- **Norma / Cláusula de Referência:** ISO/IEC/IEEE 12207:2021 — Cláusula [ex: 6.3.7]
- **Documento Relacionado:** [ex: Parte 3 do Manual de Processos de Software]
- **Data / Versão:** [DD/MM/AAAA - v1.0]

---

## 2. Prompt Estruturado (Input)

```markdown
Você é um Engenheiro de Processos de Software especialista na norma ABNT NBR ISO/IEC/IEEE 12207:2021.
Estamos elaborando o Manual de Processos de Software para o sistema "CineDoom" (sistema de gestão de cinema e bilheteria).

[CONTEXTO E PREMISSAS]
- O documento base com as decisões de negócio e arquitetura é o Project Definition Workbook (`docs/constituicao/project-definition-workbook.md`).
- Siga estritamente as diretrizes da disciplina estabelecidas pela Profa. Dra. Juliana Zinader (`docs/instrucoes-disciplina.md`).
- PROIBIDO reproduzir literalmente o texto da norma ISO 12207. Aplique e contextualize os conceitos ao sistema CineDoom.
- Não crie decisões ou tecnologias não previstas no PDW.

[OBJETIVO DA TAREFA]
Descreva o processo [Nome do Processo] em conformidade estrita com a cláusula [X.X] da norma ISO/IEC/IEEE 12207:2021.

[FORMATO DE SAÍDA ESPERADO — ESTRUTURA OFICIAL DA DISCIPLINA]
Estruture a resposta com as 7 seções obrigatórias definidas pela docente:
1. Identificação do Processo: Nome, propósito e justificativa no contexto do CineDoom.
2. Aplicação ao Sistema: Objetivos específicos, participantes, entradas, atividades/tarefas detalhadas, saídas e recursos necessários.
3. Papéis e Responsabilidades: Distribuição de atribuições em formato de Matriz RACI (Executa, Aprova, Consultado, Informado).
4. Artefatos Produzidos: Lista de documentos, registros, modelos ou evidências geradas pelo processo.
5. Critérios de Avaliação: Indicadores e mecanismos para verificar se o processo atingiu seus resultados esperados.
6. Relacionamento com Outros Processos: Processos da ISO 12207 que fornecem entradas ou consomem as saídas deste processo.
7. Decisões e Justificativas: Escolhas técnicas e organizacionais justificadas com base nas premissas e riscos do CineDoom.

[VALIDAÇÃO OBRIGATÓRIA]
Ao finalizar a proposta, execute uma autoavaliação rigorosa utilizando o validador em `prompts/validador-iso12207.md`.
Gere o relatório completo da validação e salve-o em `docs/validacoes/parte-XX/analise-validacao-parte-XX.md`:
1. Valide a conformidade com a cláusula [X.X] da ISO/IEC/IEEE 12207:2021.
2. Cheque a fidelidade às decisões registradas no PDW (`docs/constituicao/project-definition-workbook.md`).
3. Confirme que todas as 7 seções obrigatórias foram contempladas e que não há cópia literal da norma.
4. Apresente no relatório a tabela comparativa de conformidade (Processo, Cláusula, Cobertura e Ajustes aplicados).
```

---

## 3. Avaliação e Validação da Resposta
- **Itens Aprovados:** [O que foi incorporado diretamente no manual]
- **Ajustes Necessários:** [Contradições ou alucinações corrigidas pelo grupo]
- **Status:** [ ] Em análise  [x] Aprovado  [ ] Rejeitado
