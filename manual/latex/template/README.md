# Template Editorial LaTeX — CineSoft Solutions & Plataforma CineDoom

Este diretório contém o **template editorial completo, modular e reutilizável** baseado na identidade visual do material de referência, adaptado especificamente para o contexto da **CineSoft Solutions**, da plataforma **CineDoom** e dos processos **ISO/IEC/IEEE 12207:2021** e **MPS.BR (Níveis G e F)**.

---

## 📁 Estrutura de Arquivos

```text
manual-processos/manual/latex/template/
├── main.tex                    # Arquivo mestre de compilação
├── main.pdf                    # PDF de demonstração compilado
├── README.md                   # Instruções de uso e guia dos componentes
├── references.bib              # Base bibliográfica BibTeX
├── config/
│   ├── colors-fonts.tex        # Paleta de cores oficial e configuração de fontes
│   ├── page-setup.tex          # Margens A4, halftones de fundo e rodapé
│   └── headings-toc.tex        # Ícones TikZ, títulos e sumário com linha ciano
├── components/
│   ├── unit-opening.tex        # Abertura de unidade/capítulo (full-bleed dark) e contracapa
│   └── editorial-elements.tex  # Todos os 12 componentes editoriais reutilizáveis
├── chapters/
│   ├── 00-pre-textuais.tex     # Capa, ficha, siglas, listas, sumário e apresentação
│   ├── 01-demonstracao-componentes.tex # Demonstração de todos os componentes
│   └── 02-pos-textuais.tex     # Referências bibliográficas e colofão
└── images/
    └── capa.png                # Arte da capa oficial em alta resolução
```

---

## 🎨 Paleta de Cores e Tipografia

### Cores Institucionais
- **RefNavy (`#084177`)**: Azul-marinho profundo para títulos principais, seções e entradas do sumário.
- **RefPurple (`#9B1995`)**: Roxo para marcadores de lista `»`, subtítulos, termos de destaque e numerações.
- **RefLavender (`#D29BF0`)**: Lavanda para as fitas curvas vetoriais e detalhes do cubo 3D.
- **RefTeal (`#4FA3B8`)**: Azul-petróleo para as caixas de Curiosidades/Notas Técnicas e Para Relembrar.
- **RefMagentaBox (`#A836B8`)**: Roxo vibrante para as caixas de Saiba Mais / Aprofundamento Normativo.
- **RefDarkBg (`#05060D`)**: Fundo escuro com ondas tecnológicas neon para as páginas divisórias.

### Fontes Selecionadas
1. **Corpo e Títulos**: Família geométrica sem serifa **Montserrat** (ou **Avenir Next** como alternativa nativa no macOS), cobrindo variações *Light, Regular, Medium, SemiBold* e *Bold*.
2. **Notas de Rodapé**: Fonte serifada (**PT Serif / Georgia**) em corpo menor (`8.5pt`), fiel ao design de publicação editorial.
3. **Código-fonte**: Monoespaçada limpa (**Menlo / Courier**) dentro de blocos Dark IDE com realce sintático.

---

## 🧩 Os 12 Componentes Editoriais Reutilizáveis

| Nº | Componente Editorial | Comando Semântico LaTeX |
|---|---|---|
| 1 | **Abertura de Unidade** | `\aberturacapitulo{Unidade I}{Título da Unidade}` |
| 2 | **Títulos e Subseções** | `\secao{...}`, `\subsecao{...}`, `\topico{...}` (com ícones TikZ) |
| 3 | **Texto e Cenários** | `\cenariopratico{Cenário:}{Texto...}` e `\termochave{Termo}` |
| 4 | **Figura com Fonte** | `\figuracomfonte{arquivo}{largura}{título}{fonte}{label}` ou `\figuratikz` |
| 5 | **Tabela e Quadro** | `\tabelaeditorial{...}` e `\quadroeditorial{título}{fonte}{label}{conteúdo}` |
| 6 | **Exercício / Verificação**| `\verificacaoconformidade{título}{questões...}` |
| 7 | **Caixa de Curiosidades** | `\notatecnica{itens...}` ou `\caixacuriosidades{...}` |
| 8 | **Caixa de Saiba Mais** | `\saibamaisnormativo{itens com links ciano...}` |
| 9 | **Caixa Para Relembrar** | `\sintesecapitulo{itens de resumo executivo...}` |
| 10| **Listas e Código Dark** | `\begin{listapontos}`, `\begin{listaetapas}` e `\begin{editoriallisting}` |
| 11| **Notas de Rodapé** | `\notarodape{...}` (com filete fino à esquerda e fonte serifada) |
| 12| **Referências** | `\refitem{...}`, `\subsecaoreferencias{...}` e `\refsite{...}` |

---

## 🚀 Como Compilar o Projeto

No terminal, a partir da pasta do template:

```bash
cd manual-processos/manual/latex/template
tectonic main.tex
```

O comando gerará o arquivo `main.pdf` com paginação, sumário dinâmico, lista de figuras e tabelas e hiperlinks navegáveis.

