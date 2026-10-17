# 🤖 Catálogo e Engenharia de Prompts (prompts)

Esta pasta centraliza os **prompts de Inteligência Artificial** usados para redigir e revisar cada etapa do trabalho acadêmico.

---

## 🗂️ Organização das Pastas

- **[`template-prompt.md`](template-prompt.md):** Modelo padrão estruturado para criar novos prompts.
- **[`auditor-de-qualidade.md`](auditor-de-qualidade.md):** Auditor de qualidade e conformidade. Avalia se o texto cumpre a ISO 12207, o PDW e os critérios transversais (qualidade > quantidade, coerência intermódulos e linguagem técnica).
- **[`parte-00/`](parte-00/):** Prompts da **Parte 0** (Apresentação, escopo e premissas).
- **[`parte-01/`](parte-01/):** Prompts da **Parte 1** (Processos de Acordo — ISO 6.1).
- **[`parte-02/`](parte-02/):** Prompts da **Parte 2** (Processos Habilitadores — ISO 6.2).
- **[`parte-03/`](parte-03/):** Prompts da **Parte 3** (Gerenciamento Técnico — ISO 6.3).
- **[`parte-04/`](parte-04/):** Prompts da **Parte 4** (Processos Técnicos — ISO 6.4).

---

## 📌 Regra de Auditoria e Validação

Todo prompt de parte possui no final a instrução de **Validação Obrigatória**. Ao submeter um prompt para a IA, ela é instruída a aplicar as regras de [`auditor-de-qualidade.md`](auditor-de-qualidade.md) e salvar o relatório de conformidade gerado dentro de **`docs/validacoes/parte-XX/`**.
