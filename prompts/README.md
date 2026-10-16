# 🤖 Catálogo e Engenharia de Prompts (prompts)

Esta pasta reúne a engenharia de prompts utilizada com Inteligência Artificial para apoiar a elaboração, revisão e validação normativa do **Manual de Processos de Software (CineDoom)**.

O trabalho é dividido em **5 partes (Partes 0 a 4)**, cada qual com seu diretório de prompts dedicados.

---

## 🗂️ Estrutura por Partes

```text
prompts/
├── README.md
├── template-prompt.md                   # Template padrão para novos prompts
├── validador-iso12207.md                # Validador de conformidade contra a ISO 12207
├── parte-00/
│   └── prompt-apresentacao-software.md  # Parte 0: Identificação, escopo e premissas
├── parte-01/
│   └── prompt-processos-acordo.md       # Parte 1: Aquisição e Fornecimento (6.1)
├── parte-02/
│   └── prompt-processos-organizacionais.md # Parte 2: Processos Habilitadores (6.2)
├── parte-03/
│   └── prompt-gerenciamento-tecnico.md  # Parte 3: Gerenciamento Técnico (6.3)
└── parte-04/
    └── prompt-processos-tecnicos.md     # Parte 4: Processos Técnicos (6.4 - Requisitos, Arq., Design)
```

---

## 📌 Guia de Utilização

1. **Elaboração de novas seções:** Consulte o prompt correspondente à parte (`parte-00/` a `parte-04/`).
2. **Novos prompts:** Utilize o modelo padronizado em [`template-prompt.md`](template-prompt.md).
3. **Auditoria e validação:** Aplique o [`validador-iso12207.md`](validador-iso12207.md) para verificar a conformidade das respostas geradas antes de integrá-las ao manual principal.
