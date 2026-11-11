# CLAUDE.md — Diretrizes e Princípios Fundamentais de Engenharia

Este documento consolida as decisões arquiteturais, regras normativas e convenções obrigatórias que qualquer agente de Inteligência Artificial deve conhecer e respeitar estritamente antes de realizar qualquer alteração neste repositório.

---

## 1. Regra de Ouro: Fonte Única da Verdade

1. **Os arquivos Markdown em `manual-processos/manual/capitulos/[0-9][0-9]-*.md` são a ÚNICA fonte de verdade do projeto.**
2. **NUNCA edite diretamente o arquivo consolidado `manual/manual-processos-software.md`.** Ele é gerado automaticamente pelo script `manual-processos/scripts/montar-manual.sh`.
3. **Workflow obrigatório de atualização:**
   - Qualquer modificação textual deve ser feita **no respectivo arquivo modular** em `manual/capitulos/`.
   - Imediatamente após alterar os capítulos, execute `./scripts/montar-manual.sh` para reconstruir o manual consolidado.
   - Quando aplicável ao documento PDF, reflita fielmente as alterações nos arquivos correspondentes do template LaTeX (`manual/latex/template/capitulos/`) e valide a compilação com `./scripts/build-manual-latex.sh`.

---

## 2. Diretrizes Acadêmicas e Normas ABNT (UFG / INF)

* **Instituição:** Universidade Federal de Goiás (UFG) — Instituto de Informática (INF)
* **Curso:** Bacharelado em Engenharia de Software
* **Disciplina:** Processos de Engenharia de Software
* **Docente Orientadora:** Profª. Dra. Juliana Pereira de Souza Zinader
* **Normas Aplicadas:** ABNT NBR 14724 (Trabalhos Acadêmicos), NBR 6023 (Referências), NBR 6027 (Sumário), NBR 6028 (Resumo), além dos referenciais normativos ISO/IEC/IEEE 12207:2021 e MR-MPS-SW:2024.

### Estrutura Pré-Textual Rígida (ABNT NBR 14724)
A ordem canônica dos elementos pré-textuais é obrigatória e sequencial:
1. **Capa**
2. **Folha de Rosto**
3. **Histórico de Versões do Documento**
4. **Lista de Figuras**
5. **Lista de Tabelas**
6. **Lista de Abreviaturas e Siglas**
7. **Sumário**

> **ATENÇÃO CRÍTICA:**
> - O **Sumário é o ÚLTIMO elemento pré-textual**.
> - Imediatamente após o Sumário, inicia-se obrigatoriamente o **Capítulo 1 (Elementos Textuais)**.
> - **NUNCA insira seções, tópicos numerados (ex.: 7, 8, 9) ou glossários entre o Sumário e o Capítulo 1.**
> - Referências bibliográficas pertencem estritamente aos **Elementos Pós-Textuais** (`99-pos-textuais.md` / `99-pos-textuais.tex`), posicionados ao final do trabalho.

---

## 3. Identidade da Equipe, Organização e Produto

* **Grupo Acadêmico Oficial:** `Doomscoders`
* **Membros da Equipe (Ordem Alfabética Canônica):**
  1. Carlos Eduardo Freire da Silva
  2. Gabriel Henrique Lourenço Dias
  3. Kayque Vicente Silva
  4. Yury Nogueira de Oliveira Silva
* **Regra de Nomes e Cargos:**
  - Na **Capa**, **Folha de Rosto** e cabeçalhos pré-textuais, constam **apenas os nomes dos autores**. NUNCA invente ou anexe cargos/papéis (como *"Tech Lead & Arquiteto"*) nesses locais.
  - Cargos funcionais e atribuições da equipe pertencem exclusivamente à **Matriz RACI e ao Inventário de Recursos Humanos** na Seção 3.4 do Capítulo 3.
* **Organização Fictícia:** **CineSoft Solutions** (empresa de engenharia de software B2B).
* **Produto:** **CineDoom** (plataforma web SaaS multi-tenant de gestão operacional e bilheteria de cinemas).

---

## 4. Princípios de Engenharia de Software Adotados

O projeto adota três pilares metodológicos formais, documentados no Capítulo 5 (seções 5.2.1 e 5.3.1) e no Capítulo 3 (seção 3.5):

1. **Domain-Driven Design (DDD):**
   - **Linguagem Ubíqua (*Ubiquitous Language*):** Termos determinísticos adotados uniformemente em código, banco e manuais (`Tenant`, `SessionSeat`, `ReservationStatus: PENDING | CONFIRMED | CANCELLED | EXPIRED`, `Ticket: SOLD`, `Double-booking`).
   - **Contextos Delimitados (*Bounded Contexts*):** Fatias verticais por domínio (`features/bilheteria`, `features/catalogo`, `features/sessoes`, `features/reserva`, `features/governanca-lgpd`).
   - **Invariantes no Domínio:** Regras de negócio vitais blindadas no núcleo da aplicação (bloqueio ACID com `SELECT FOR UPDATE`, antecedência mínima de 60 min para reservas e expiração JIT).

2. **SOLID:**
   - **S (Single Responsibility):** Serviços especializados com propósito único (`SaleService`, `ReservationService`, `CancellationService`, `CryptoService`).
   - **O (Open/Closed):** Provedores desacoplados via interfaces (ex.: `NotificationService` suportando `ResendProvider` e `ConsoleLogger`).
   - **L (Liskov Substitution):** Contratos de repositório e serviços respeitados estritamente.
   - **I (Interface Segregation):** DTOs e validações `Zod` específicas por operação.
   - **D (Dependency Inversion):** Route Handlers dependem de abstrações de serviço, não de implementações acopladas.

3. **Test-Driven Development (TDD):**
   - Ciclo **Red $\to$ Green $\to$ Refactor** aplicado prioritariamente nas transações críticas de concorrência e isolamento.
   - Base de testes sólida: **26 arquivos e 770 testes automatizados no Vitest** passando com 100% de sucesso (incluindo corrida concorrente com 50 threads e 509 cenários de invasão *cross-tenant*).

---

## 5. Regras Editoriais e Design System (LaTeX e Markdown)

1. **Tabelas:**
   - Adotar o padrão visual do GitHub: cabeçalho escuro (`BrandTableHeader`), bordas superior e inferior sólidas (`GithubTableBorder`), e linhas divisórias horizontais interiores mais claras (`BrandGrayRule`) separando cada linha de dados.
   - Conteúdo de células: texto centralizado e justificado, sem quebras artificiais de linha nem espaçamentos excessivos.
   - **Sem overflow:** Nenhuma tabela, figura, imagem ou diagrama pode ultrapassar a largura útil da folha A4.
2. **Títulos e Identidade Visual no LaTeX:**
   - Todos os títulos principais (pré-textuais, aberturas de capítulo e pós-textuais) devem ser padronizados com a macro `\tituloSecaoPrincipal{...}`, que inclui o filete horizontal rosa (`BrandCrimson`).
   - As macros nativas do LaTeX `\listoffigures`, `\listoftables` e `\tableofcontents` devem obrigatoriamente chamar `\tituloSecaoPrincipal` para manter uniformidade visual estrita.

---

## 6. Scripts Operacionais

Todos os scripts estão localizados em `manual-processos/scripts/`:

* `./scripts/montar-manual.sh`: Concatena os capítulos de `manual/capitulos/[0-9][0-9]-*.md` gerando o arquivo consolidado `manual/manual-processos-software.md`.
* `./scripts/build-manual-latex.sh`: Compila o manual oficial em LaTeX usando o motor **Tectonic**, gerando o PDF final em `manual/latex/template/main.pdf`.
* `./scripts/compilar.sh`: Script auxiliar de compilação por capítulos.

---

## 7. Proibições Estritas para a IA

- **NUNCA invente dados, nomes ou seções.** Se uma informação não consta no Markdown oficial ou nas orientações da professora, questione antes de adicionar.
- **NUNCA altere a ordem dos elementos pré-textuais da ABNT.**
- **NUNCA edite `manual-processos-software.md` diretamente.** Sempre edite os módulos individuais em `manual/capitulos/` e rode o script de montagem.
- **NUNCA remova a sincronia entre Markdown e LaTeX.** Sempre mantenha ambos em estrita paridade.
