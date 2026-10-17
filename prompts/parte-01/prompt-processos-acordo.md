# Prompt — Parte 1: Processos de Acordo

## 1. Identificação
- **Código:** `PR-P01_Processos_Acordo`
- **Parte do Trabalho:** Parte 1 – Processos de Acordo (Agreement Processes)
- **Norma / Cláusula de Referência:** ISO/IEC/IEEE 12207:2021 — Cláusulas 6.1.1 (Acquisition Process) e 6.1.2 (Supply Process)
- **Documento-base:** `docs/guia-projeto/project-definition-workbook.md` (Seções 4, 11 e 12)

---

## 2. Prompt Estruturado (Input)

```markdown
Atue como Especialista em Processos de Software conforme a norma ABNT NBR ISO/IEC/IEEE 12207:2021.

Elabore a especificação dos Processos de Acordo para o CineDoom:

1. PROCESSO DE AQUISIÇÃO (ISO 12207 – 6.1.1):
   - Fronteira: o que a equipe do CineDoom adquire de terceiros (ex: infraestrutura de nuvem AWS, gateway de pagamentos, ferramentas de CI/CD).
   - Justificativas técnicas e econômicas de aquisição versus desenvolvimento próprio.
   - Critérios de seleção e etapas formais de aquisição.
   - Avaliação e gestão contínua de fornecedores.

2. PROCESSO DE FORNECIMENTO (ISO 12207 – 6.1.2):
   - Modelo de fornecimento (SaaS para redes exibidoras de cinema).
   - Preparação do fornecimento e catálogo de entregáveis por release.
   - Critérios de aceite e homologação pelo cliente.
   - Suporte pós-entrega, operação assistida e canais de SLA.

[FORMATO DE SAÍDA]
Texto em Markdown técnico com tabelas comparativas para critérios de seleção e matriz de entregáveis.

[VALIDAÇÃO OBRIGATÓRIA]
Ao finalizar a proposta, execute uma autoavaliação rigorosa utilizando o validador em `prompts/validador-iso12207.md`.
Gere o relatório completo e salve-o em `docs/validacoes/parte-01/analise-validacao-parte-01.md`:
1. Valide a conformidade com as cláusulas 6.1.1 (Aquisição) e 6.1.2 (Fornecimento) da ISO/IEC/IEEE 12207:2021.
2. Cheque a consistência com os modelos de comercialização e infraestrutura do PDW (`docs/guia-projeto/project-definition-workbook.md`).
3. Anexe no relatório a tabela comparativa de conformidade do processo (Processo, Cláusula, Cobertura e Ajustes).
```
