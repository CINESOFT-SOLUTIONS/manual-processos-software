# Conteúdo Canônico Modular (content)

Este diretório é a **Fonte Canônica da Verdade (Single Source of Truth - SSOT)** de todo o conteúdo textual do Manual de Processos de Software.

O conteúdo está particionado em módulos independentes alinhados aos capítulos da norma **ABNT NBR ISO/IEC/IEEE 12207:2021** e à estrutura mínima pedagógica da disciplina.

---

## Módulos por Capítulo

| Arquivo | Capítulo Correspondente | Escopo Principal |
| :--- | :--- | :--- |
| **[`00-identificacao.md`](00-identificacao.md)** | Pré-textual | Capa, folha de rosto, identificação da equipe e histórico formal de versões. |
| **[`01-apresentacao-software.md`](01-apresentacao-software.md)** | Capítulo 1 | Nome, descrição, problema de negócio, público-alvo, escopo do MVP e restrições. |
| **[`02-processos-acordo.md`](02-processos-acordo.md)** | Capítulo 2 | Processos de aquisição (nuvem, APIs), fornecimento (SaaS, SLA) e parceiros. |
| **[`03-processos-organizacionais.md`](03-processos-organizacionais.md)** | Capítulo 3 | Modelo de ciclo de vida, infraestrutura, viabilidade, matriz RACI e gestão da qualidade. |
| **[`04-gerenciamento-tecnico.md`](04-gerenciamento-tecnico.md)** | Capítulo 4 | Plano de projeto, gestão de riscos, controle de configuração, ADRs e métricas. |
| **[`05-processos-tecnicos.md`](05-processos-tecnicos.md)** | Capítulo 5 | Requisitos (US-1..6, AC-1..8), C4, Prisma, STRIDE, DPIA LGPD e suíte de testes. |

---

## Diretrizes de Contribuição para a Equipe

1. **Edição Exclusiva em `content/`:**
   * Nunca edite o arquivo `manual-processos-software.md` na raiz do repositório manualmente. Ele é um artefato compilado e sobregravado automaticamente pelo pipeline de build.
2. **Pull Requests Atômicos:**
   * Crie branches específicas por capítulo (ex: `feat/capitulo-04-riscos`) para evitar conflitos de merge entre os integrantes.
3. **Recompilação do Documento Unificado:**
   * Após editar qualquer módulo, gere o documento consolidado da raiz executando:
     ```bash
     ./scripts/montar-manual.sh
     ```
   * Ou execute o pipeline completo (Markdown + LaTeX + Beamer):
     ```bash
     ./scripts/compilar.sh
     ```
