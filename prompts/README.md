# 🤖 Catálogo e Engenharia de Prompts (prompts)

Esta pasta centraliza os **prompts de Inteligência Artificial** usados para redigir e revisar cada etapa do trabalho acadêmico.

---

## 🗂️ Organização das Pastas

- **[`template-prompt.md`](template-prompt.md):** Modelo padrão estruturado para criar novos prompts.
- **[`validador-iso12207.md`](validador-iso12207.md):** Validador formal. Analisa se o texto gerado pela IA cumpre a norma ISO 12207 e o caderno PDW.
- **[`parte-00/`](parte-00/):** Prompts para a **Parte 0** (Apresentação do CineDoom, escopo e premissas).
- **[`parte-01/`](parte-01/):** Prompts para a **Parte 1** (Processos de Acordo: Aquisição e Fornecimento — ISO 6.1).
- **[`parte-02/`](parte-02/):** Prompts para a **Parte 2** (Processos Organizacionais: Ciclo de vida, RH, infraestrutura e qualidade — ISO 6.2).
- **[`parte-03/`](parte-03/):** Prompts para a **Parte 3** (Gerenciamento Técnico: Planejamento, riscos, medição e configuração — ISO 6.3).
- **[`parte-04/`](parte-04/):** Prompts para a **Parte 4** (Processos Técnicos: Requisitos, arquitetura e design — ISO 6.4).

---

## 📌 Regra de Validação

Todo prompt de parte possui no final a instrução de **Validação Obrigatória**. Ao submeter um prompt para a IA, ela é instruída a aplicar as regras de [`validador-iso12207.md`](validador-iso12207.md) e retornar uma tabela de conformidade antes de incorporar o conteúdo ao manual.
