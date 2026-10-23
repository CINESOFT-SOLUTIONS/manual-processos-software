# Referências Normativas e Diretrizes (references)

Este diretório armazena as fontes canônicas de consulta, premissas de negócio e diretrizes pedagógicas que regem a elaboração do Manual de Processos de Software e o desenvolvimento do CineDoom.

Nenhuma regra ou arquitetura é definida sem respaldo nestas referências.

---

## Estrutura de Diretórios

### 1. Norma Internacional de Ciclo de Vida de Software (`iso-12207/`)
* **[`iso-12207/abnt-iso-iec-12207-2021.pdf`](iso-12207/abnt-iso-iec-12207-2021.pdf):** Texto integral oficial da norma ABNT NBR ISO/IEC/IEEE 12207:2021 (Engenharia de sistemas e software — Processos de ciclo de vida de software).
* **[`iso-12207/abnt-iso-iec-12207-2021.md`](iso-12207/abnt-iso-iec-12207-2021.md):** Síntese estruturada das cláusulas, grupos de processos (Acordo, Organizacionais Habilitadores, Gerenciamento Técnico e Processos Técnicos) e entregáveis exigidos.

### 2. Constituição do CineDoom (`pdw/`)
* **[`pdw/project-definition-workbook.md`](pdw/project-definition-workbook.md):** O Project Definition Workbook (PDW) atua como a constituição do projeto. Define:
  * Problema de negócio, modelo de monetização B2B SaaS e proposta de valor.
  * Regras estritas de reserva de assentos e integridade transacional.
  * Perfis de acesso: Atendente de bilheteria e Gerente de cinema.
  * Delimitação estrita do escopo do MVP (100% presencial, sem gateways de pagamento online ou app mobile).

### 3. Diretrizes Acadêmicas da Disciplina (`guidelines/`)
* **[`guidelines/instrucoes-disciplina.md`](guidelines/instrucoes-disciplina.md):** Requisitos oficiais da disciplina de Processos de Engenharia de Software (UFG/INF), critérios de pontuação da Profa. Dra. Juliana Zinader e padrão de 7 seções por processo.
* **[`guidelines/estrutura-minima-manual.md`](guidelines/estrutura-minima-manual.md):** Sumário analítico obrigatório em 5 capítulos exigido para a avaliação formal.
* **[`guidelines/estrutura-organizacao-repositorios.md`](guidelines/estrutura-organizacao-repositorios.md):** Racional sobre a separação da organização GitHub em repositórios complementares (`manual-processos` e `cinedoom-app`).
