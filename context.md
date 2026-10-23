# CONTEXTO DO PROJETO: TRANSIÇÃO DO MANUAL DE PROCESSOS PARA SOFTWARE REAL (CineDoom)

## 1. VISÃO GERAL E OBJETIVO DESTE PROMPT
Somos uma equipe de 4 estudantes do curso de Bacharelado em Engenharia de Software da Universidade Federal de Goiás (UFG/INF).
Estamos cursando a disciplina de **Processos de Engenharia de Software** (período letivo 2026/2), ministrada pela **Profa. Dra. Juliana Pereira de Souza Zinader**.

Até o momento, o trabalho tem como foco a elaboração de um **Manual de Processos de Software** baseado na norma **ABNT NBR ISO/IEC/IEEE 12207:2021**, aplicado a um estudo de caso chamado **CineDoom** (sistema de gestão de salas e bilheteria de cinema).

### A Ideia Nova
Queremos sair da simulação puramente teórica ("suponha que você vai testar...") e **implementar o CineDoom de forma real e funcional**, separando a estrutura em uma organização no GitHub com dois repositórios:
1. `manual-processos` (manual em Markdown/LaTeX, slides em Beamer, evidências de auditoria e processos ISO 12207);
2. `cinedoom-app` (o software real funcionando, testado, versionado e demonstrável).

Nosso objetivo é fazer uma **demonstração ao vivo no dia da apresentação final** (lotando uma sessão de cinema na tela para a banca).

---

## 2. DADOS CRÍTICOS E RESTRIÇÕES DE CALENDÁRIO
- **Data atual:** 22 de outubro de 2026.
- **Data da entrega e apresentação final:** 12 de novembro de 2026.
- **Janela de execução:** **Exatamente 3 semanas (21 dias corridos)**.
- **Equipe (4 integrantes):**
  - Carlos Eduardo Freire da Silva
  - Gabriel Henrique Lourenço Dias
  - Kayque Vicente Silva
  - Yury Nogueira de Oliveira Silva
- **Formato da avaliação:**
  - Apresentação oral simulando uma auditoria/avaliação de maturidade de processos perante uma banca avaliadora.
  - Critérios de avaliação da professora: Aplicação dos conceitos da ISO 12207, contextualização com a empresa fictícia (CineSoft Solutions), qualidade e utilidade dos artefatos, rastreabilidade ponta a ponta (requisito -> ADR -> código -> teste -> release), consistência entre módulos e reflexão crítica.

---

## 3. O QUE TEMOS ATÉ AGORA NO REPOSITÓRIO (ESTADO ATUAL)

### 3.1. Código de Software
- **Zero (0) linhas de código implementadas até o momento.** O repositório atual contém exclusivamente documentos de engenharia de requisitos, governança, decisões arquiteturais e processos.

### 3.2. Artefatos de Documentação Prontos e Estruturados
1. **`docs/constituicao/project-definition-workbook.md` (PDW - ~2.000 linhas):**
   - É a "constituição" e fonte única da verdade do projeto.
   - Define a empresa fictícia **CineSoft Solutions** (B2B SaaS para cinemas de pequeno/médio porte).
   - Mapeia 12 Requisitos Funcionais originais (`RF-01` a `RF-12`), Requisitos Não-Funcionais (tempo de resposta ≤ 2s, PostgreSQL, Node.js, React, monólito modular), papéis, matriz RACI, modelo de ciclo de vida incremental (5 incrementos) e 11 riscos mapeados (`R-01` a `R-11`).
2. **`manual-processos-software.md` (~600 linhas consolidadas):**
   - **Capa e Contracapa:** Histórico de revisões formal (versões 1.0 a 1.6).
   - **Capítulo 1 (Apresentação do Software):** Problema, público-alvo, contexto de uso, ambiente de operação, escopo e premissas.
   - **Capítulo 2 (Processos de Acordo - Cláusula 6.1 ISO 12207):** Processo de Aquisição (nuvem, banco), Processo de Fornecimento (SaaS, entregáveis, aceite) e Identificação de Fornecedores/Parceiros.
   - **Capítulo 3 (Processos Organizacionais Habilitadores - Cláusula 6.2 ISO 12207):** Ciclo de vida incremental, inventário de infraestrutura, viabilidade, RH/capacitação (RACI), qualidade (métricas e metas) e gestão do conhecimento.
   - **Capítulo 4 (Processos de Gerenciamento Técnico - Cláusula 6.3 ISO 12207):** Planejamento dos incrementos, matriz de riscos (`R-01` a `R-05`), gestão de configuração (branches `main`/`develop`/`feature`, tags semânticas, baselines), governança de decisões arquiteturais com ADRs (ADR-001 a ADR-006) e métricas.
   - **Capítulo 5 (Processos Técnicos - Cláusulas 6.4 e 7.1 ISO 12207):** Estrutura completa de Requisitos, Arquitetura/Design (C4/UML), Implementação/Integração, V&V/Transição e Operação/Manutenção.
3. **`docs/estrutura-minima-manual.md`:**
   - Roteiro oficial cobrado pela professora em 5 capítulos:
     - Cap 1: Apresentação do software.
     - Cap 2: Processos de Acordo.
     - Cap 3: Processos Organizacionais Habilitadores.
     - Cap 4: Processos de Gerenciamento Técnico.
     - Cap 5: Processos Técnicos (5.1 Requisitos, 5.2 Arquitetura e Design com ≥ 2 diagramas, 5.3 Implementação e Integração, 5.4 V&V e Transição, 5.5 Operação e Manutenção).
4. **Infraestrutura de compilação e slides:**
   - Script `./scripts/compilar.sh` via Tectonic compilando o documento ABNT em `trabalho_latex/` e a apresentação Beamer em `slides_latex/`.
   - Sistema de prompts estruturados (`prompts/parte-00` a `parte-04`) com roteiro de auditoria de qualidade (`auditor-de-qualidade.md`).

---

## 4. RESPOSTA À PERGUNTA: USAR/REFATORAR OU GERAR NOVO?

| Frente | Situação | Diretriz de Decisão |
|---|---|---|
| **Manual de Processos & PDW** | Já possui ~70% da estrutura normativa escrita e consistente. | **Usar e refatorar/adaptar.** Não jogar fora o que já foi feito. Manter os Capítulos 1, 2, 3 e 4, apenas sincronizando o escopo com o que será de fato construído, de modo que o manual descreva o processo que a equipe executou na prática. |
| **Capítulo 5 (Processos Técnicos)** | Ainda não redigido. | **Gerar alinhado à implementação real.** Esse capítulo será enriquecido com dados reais: diagramas de arquitetura reais, padrões de código reais do repo, prints e relatórios de testes unitários/integração do Jest/Vitest, e pipeline de CI do GitHub Actions. |
| **Software CineDoom** | Não existe código. | **Gerar novo do zero, com escopo radicalmente enxuto (MVP Vertical).** |

---

## 5. A DEMONSTRAÇÃO ALVO (THE "SHOW" NO DIA DA BANCA)
No dia 12/11, durante a apresentação de maturidade para a Profa. Juliana:
1. Apresentar os processos do manual e a governança.
2. Abrir o CineDoom em tempo real no projetor:
   - Exibir uma sessão cadastrada para um filme (ex: "Sessão das 20h - Sala 1 - 30 assentos").
   - Mostrar o mapa de assentos da sala (Grid visual).
   - Simular ou executar compras simultâneas até **lotar a sessão** (100% dos assentos ocupados, ficando vermelhos).
   - Tentar vender um assento já ocupado e comprovar a regra de negócio disparando a rejeição/bloqueio atômico.
   - Mostrar a emissão de comprovante/ingresso e o resumo de ocupação da sessão.
3. Mostrar no repositório de software as evidências reais de engenharia de software:
   - Pipeline de CI passando no GitHub Actions (lint + testes automáticos).
   - Commits rastreando tarefas/requisitos (`feat(RF-05): implementa agendamento de sessões`).
   - Release com tag semântica (ex: `v1.0.0-mvp`) associada ao incremento final.

---

## 6. O DESAFIO DO ESCOPO (O QUE CORTAR VS O QUE MANTER EM 3 SEMANAS)

O PDW original contemplava muitas coisas complexas. Para 4 pessoas entregarem tudo em 21 dias (código + manual completo + slides + ensaio), **o escopo de software precisa ser cortado cirurgicamente**:

### O que deve ser CORTADO do software inicial:
- ❌ Gateway de pagamento real externo (Stripe/webhooks) -> Simular apenas método de pagamento aprovado ("Dinheiro / PIX Teste / Cartão Balcão").
- ❌ Cadastro complexo de clientes e "Registro de interesse em lançamentos".
- ❌ Múltiplos cinemas / Multi-tenancy isolado complexo em nuvem AWS paga.
- ❌ Relatórios avançados em PDF/Excel (apenas indicador na tela de ocupação da sessão).
- ❌ Upload de arquivos pesados (trailers/vídeos) -> Usar URLs de imagens de pôster ou placeholders estáticos.

### O que é o CORE INEGOCIÁVEL (Must Have do MVP):
- ✅ **Filmes:** Cadastro mínimo (título, classificação, duração, pôster URL).
- ✅ **Salas & Assentos:** 1 ou 2 salas com matriz/grid de assentos (ex: Fileiras A-E, 1-6 = 30 assentos).
- ✅ **Sessões:** Associação Filme + Sala + Data/Hora.
- ✅ **Bilheteria (Venda de Ingressos):**
  - Seleção visual de assentos na sala.
  - Bloqueio de venda dupla (concorrência e integridade referencial).
  - Confirmação de venda com emissão de identificador/ingresso.
  - Cancelamento de ingresso liberando o assento novamente.
- ✅ **Visão de Ocupação:** Painel/tela mostrando a taxa de ocupação da sessão (ex: 30/30 assentos vendidos - Sessão Esgotada).

---

## 7. O QUE PRECISAMOS QUE VOCÊ (LLM) PLANEJE E SUGIRA:

Com base em todo o contexto acima:

1. **Plano de Corte de Escopo Formal:**
   - Como reclassificar os requisitos do PDW (`RF-01` a `RF-12`) entre o que entra no MVP real e o que fica documentado no manual como "Requisitos das Próximas Releases (Backlog Futuro)", mantendo a nota 10 com a professora.
2. **Stack Tecnológica Recomendada para Velocidade Máxima:**
   - Qual arquitetura e stack permitirão a 4 pessoas construírem esse MVP visualmente incrível (com mapa de assentos interativo) em menos de 10 a 12 dias de desenvolvimento? (Ex: React + Node/Express com SQLite/Prisma, ou Next.js fullstack, ou Vite + Tailwind/CSS puro + backend simples?).
3. **Divisão de Trabalho e Cronograma Semana a Semana (22/10 a 12/11):**
   - Como dividir os 4 integrantes (Carlos, Gabriel, Kayque, Yury) para que o manual avance junto com o software e nada atrase?
4. **Estratégia de Rastreabilidade e Evidências:**
   - Como vincular o repositório `cinedoom-app` ao `manual-processos` para que as evidências exigidas pela ISO 12207 no Capítulo 5 (testes, diagramas, releases, ADRs, CI) sejam geradas automaticamente a partir do código real?
5. **Roteiro da Apresentação Final (Demonstração da Sessão Lotada):**
   - Como estruturar os 15-20 minutos da apresentação perante a banca para demonstrar os processos teóricos e o clímax da sessão ao vivo funcionando.
