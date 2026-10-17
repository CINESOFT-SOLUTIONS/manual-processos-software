# 🤖 Catálogo e Engenharia de Prompts (prompts)

Esta pasta centraliza os **prompts de Inteligência Artificial** usados para redigir e revisar cada etapa do trabalho acadêmico.

---

## 🗂️ Organização das Pastas

- **[`template-prompt.md`](template-prompt.md):** Modelo padrão estruturado para criar novos prompts.
- **[`validador-iso12207.md`](validador-iso12207.md):** Validador formal. Analisa se o texto gerado pela IA cumpre a norma ISO 12207 e o caderno PDW.
- **[`parte-00/`](parte-00/):** Prompts da **Parte 0** (Apresentação, escopo e premissas).
- **[`parte-01/`](parte-01/):** Prompts da **Parte 1** (Processos de Acordo — ISO 6.1).
- **[`parte-02/`](parte-02/):** Prompts da **Parte 2** (Processos Habilitadores — ISO 6.2).
- **[`parte-03/`](parte-03/):** Prompts da **Parte 3** (Gerenciamento Técnico — ISO 6.3).
- **[`parte-04/`](parte-04/):** Prompts da **Parte 4** (Processos Técnicos — ISO 6.4).

---

## 📌 Regra de Validação

Todo prompt de parte possui no final a instrução de **Validação Obrigatória**. Ao submeter um prompt para a IA, ela é instruída a aplicar as regras de [`validador-iso12207.md`](validador-iso12207.md) e salvar o relatório de conformidade gerado dentro de **`docs/validacoes/parte-XX/`**.
