# Pipeline de Sincronização Automatizada: Markdown → LaTeX

Este repositório possui uma pipeline automatizada para garantir que o **conteúdo dos arquivos Markdown em `manual-processos/manual/capitulos/*.md` seja a referência absoluta de verdade do projeto**, eliminando qualquer *drift* (divergência ou defasagem de conteúdo) em relação ao código LaTeX em `manual-processos/manual/latex/template/capitulos/*.tex`.

---

## 🚀 Como Executar a Sincronização

Sempre que qualquer capítulo em Markdown (`.md`) for editado, basta rodar o comando:

```bash
python3 manual-processos/scripts/sync-md-to-latex.py
```

E em seguida compilar o documento LaTeX via `tectonic`:

```bash
cd manual-processos/manual/latex/template
tectonic main.tex
```

---

## ⚙️ O Que o Script `sync-md-to-latex.py` Faz Automaticamente

1. **Leitura dos Arquivos Markdown Oficiais:** Lê `01-apresentacao-software.md` até `06-avaliacao-melhoria.md`.
2. **Substituição de Imagens Markdown por Figuras Oficiais:** Detecta chamadas de prints e screenshots e as substitui pelo comando editorial `\figuracomfonte{...}` com dimensões padronizadas e fontes bibliográficas.
3. **Mapeamento de Diagramas Mermaid para Vetores Oficiais:** Converte automaticamente os blocos ````mermaid```` para a inclusão dos diagramas vetoriais gerados a partir do PlantUML (`.pdf` e `.svg`), apontando para a estrutura centralizada em `manual-processos/assets/`.
4. **Injeção de Tabelas Estruturadas:** Mapeia tabelas de requisitos, riscos, Make or Buy e RACI para os arquivos padronizados em `manual-processos/assets/capitulo-XX/tabelas/*.tex`.
5. **Conversão Automatizada de Texto com Pandoc:** Processa todo o texto, listas, citações e blocos de código com alta fidelidade semântica.
6. **Sanitização Tipográfica para XeTeX:** Trata símbolos matemáticos e tabelas dinâmicas com `tabularx`, garantindo compilação limpa e perfeita sem dependências de rede.

