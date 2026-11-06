## Identificacao da Mudanca

- **Capitulo(s) Afetado(s):**
  - [ ] manual/capitulos/00-identificacao.md (Identificacao e Historico)
  - [ ] manual/capitulos/01-apresentacao-software.md (Apresentacao do Software)
  - [ ] manual/capitulos/02-processos-acordo.md (Processos de Acordo)
  - [ ] manual/capitulos/03-processos-organizacionais.md (Processos Organizacionais)
  - [ ] manual/capitulos/04-gerenciamento-tecnico.md (Gerenciamento Tecnico)
  - [ ] manual/capitulos/05-processos-tecnicos.md (Processos Tecnicos)
  - [ ] specs/ (Especificacoes de Engenharia e Decisoes Tecnicas)
  - [ ] latex/ (Templates de Relatorio ABNT ou Apresentacao Beamer)
  - [ ] scripts/ (Automacoes de Compilacao e Montagem)
- **Clausula da ISO/IEC/IEEE 12207:2021:** (ex.: 6.1.1, 6.2.4, 6.3.1, 6.4.2...)
- **Issue Vinculada:** (ex.: Fixes #4, Ref #7)

---

## Descricao das Alteracoes
<!-- Explique de forma sucinta e tecnica o que foi adicionado, alterado ou corrigido. -->

---

## Conformidade com as Diretrizes Docentes e Engenharia

- [ ] **Fonte Unica da Verdade (SSOT):** As alteracoes foram feitas exclusivamente nos arquivos fonte em `manual/capitulos/` ou `specs/` (e nao diretamente em `manual-processos-software.md`).
- [ ] **Rigor Tecnico e Terminologia:** O texto respeita as definicoes formais de Cliente (cinema B2B), Usuario (atendente/gerente) e Espectador (consumidor de balcao).
- [ ] **Diretrizes Pedagogicas:** Segue rigorosamente a estrutura de capitulos exigida pela Profa. Dra. Juliana Zinader (`referencias/diretrizes/estrutura-minima-manual.md`).
- [ ] **Qualidade e Estilo:** Sem emojis, sem jargoes vazios e com justificativas tecnicas ancoradas na norma.

---

## Validacao e Compilacao Local

- [ ] **Montagem Consolidada:** O script `./scripts/montar-manual.sh` foi executado e gerou `manual-processos-software.md` sem divergencias.
- [ ] **Compilacao de PDFs:** O script `./scripts/compilar.sh` executou com sucesso gerando os artefatos:
  - `manual/latex/manual-processos-software.pdf` (Relatorio ABNT)
  - `manual/latex/apresentacao-manual.pdf` (Slides Beamer UFG/INF)
- [ ] **Historico de Versoes:** A tabela de controle de versoes em `manual/capitulos/00-identificacao.md` foi atualizada quando aplicavel.
