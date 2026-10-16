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
- O documento base com as decisões de negócio e arquitetura é o Project Definition Workbook (PDW).
- Não crie decisões ou tecnologias não previstas no PDW.

[OBJETIVO DA TAREFA]
Descreva o processo [Nome do Processo] em conformidade estrita com a cláusula [X.X] da norma ISO/IEC/IEEE 12207:2021.

[FORMATO DE SAÍDA ESPERADO]
Estruture a resposta com as seguintes seções:
1. Propósito do Processo
2. Resultados Esperados (Outcomes)
3. Atividades e Tarefas detalhadas
4. Entradas e Saídas do Processo
5. Tabela de Responsabilidades (RACI)
```

---

## 3. Avaliação e Validação da Resposta
- **Itens Aprovados:** [O que foi incorporado diretamente no manual]
- **Ajustes Necessários:** [Contradições ou alucinações corrigidas pelo grupo]
- **Status:** [ ] Em análise  [x] Aprovado  [ ] Rejeitado
