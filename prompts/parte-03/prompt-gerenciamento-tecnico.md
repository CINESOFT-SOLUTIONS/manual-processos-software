# Prompt — Parte 3: Processos de Gerenciamento Técnico

## 1. Identificação
- **Código:** `PR-P03_Gerenciamento_Tecnico`
- **Parte do Trabalho:** Parte 3 – Processos de Gerenciamento Técnico
- **Norma / Cláusula de Referência:** ISO/IEC/IEEE 12207:2021 — Cláusulas 6.3.1 a 6.3.7
- **Documento-base:** `docs/constituicao/project-definition-workbook.md` (Seções 21 a 38) e `docs/rascunhos-partes/rascunho-parte-03.md`

---

## 2. Prompt Estruturado (Input)

```markdown
Atue como Gerente de Projetos e Engenheiro de Processos de Software especialista na ABNT NBR ISO/IEC/IEEE 12207:2021.

Elabore os processos do grupo 6.3 (Technical Management Processes) para o projeto CineDoom:

1. 3.1 Planejamento do Projeto (6.3.1):
   - Escopo, marcos de entrega por incremento (M1 a M5), cronograma e estimativa de esforço.
2. 3.2 Avaliação e Controle do Projeto (6.3.2):
   - Pontos de controle, relatórios de status por incremento e ações corretivas/preventivas.
3. 3.3 Gestão de Decisões Técnicas (6.3.3):
   - Política de ADRs (Architecture Decision Records) e lista inicial de decisões arquiteturais.
4. 3.4 Gestão de Riscos (6.3.4):
   - Critérios de probabilidade x impacto e matriz de riscos técnicos/negócio.
5. 3.5 Gestão de Configuração (6.3.5):
   - Itens de Configuração (CIs), linhas de base (baselines), fluxo Git (branches/tags) e controle de mudanças.
6. 3.6 Gestão da Informação (6.3.6):
   - Lista de documentos controlados, regras de versionamento e repositório oficial.
7. 3.7 Medição (6.3.7):
   - Plano de medição com indicadores de processo e de produto (fórmulas, fontes, metas e responsáveis).

[FORMATO DE SAÍDA]
Markdown detalhado, com tabelas para o plano de medição, matriz de riscos e lista de ADRs.

[VALIDAÇÃO OBRIGATÓRIA]
Ao finalizar a proposta, execute uma autoavaliação rigorosa utilizando o auditor em `prompts/auditor-de-qualidade.md`.
Gere o laudo de auditoria e salve-o em `docs/validacoes/parte-03/analise-validacao-parte-03.md`:
1. Valide a conformidade com as 7 cláusulas do grupo 6.3 (Technical Management Processes: 6.3.1 a 6.3.7) da ISO/IEC/IEEE 12207:2021.
2. Certifique-se de que nenhum processo obrigatório da norma foi omitido (atenção especial para 6.3.6 Gestão da Informação e separação entre 6.3.2 Controle e 6.3.7 Medição).
3. Verifique o alinhamento com as seções 21 a 38 do PDW (`docs/constituicao/project-definition-workbook.md`).
4. Avalie os critérios transversais (qualidade > quantidade, linguagem técnica e coerência intermódulos).
5. Anexe no relatório a tabela comparativa de conformidade do processo (Processo, Cláusula, Cobertura e Ajustes).
```
