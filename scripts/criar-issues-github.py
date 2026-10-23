#!/usr/bin/env python3
import subprocess
import sys
import time

REPOS = {
    "docs": "CINESOFT-SOLUTIONS/manual-processos-software",
    "app": "CINESOFT-SOLUTIONS/cinedoom-app"
}

LABELS = [
    ("prioridade:P0", "b60205", "Prioridade crítica / caminho crítico"),
    ("prioridade:P1", "d93f0b", "Prioridade alta"),
    ("prioridade:P2", "fbca04", "Prioridade média"),
    ("tipo:feat", "1d76db", "Nova funcionalidade"),
    ("tipo:docs", "0052cc", "Documentação e processos ISO"),
    ("tipo:test", "0e8a16", "Testes e qualidade"),
    ("tipo:security", "5319e7", "Segurança e privacidade"),
    ("tipo:infra", "e99695", "Infraestrutura e DevOps"),
    ("tipo:chore", "c5def5", "Tarefas de suporte e configuração"),
    ("modulo:bilheteria", "1f883d", "Módulo de bilheteria e vendas"),
    ("modulo:backoffice", "006b75", "Módulo administrativo e catálogo"),
    ("modulo:auth", "6f42c1", "Autenticação e controle de acesso"),
    ("modulo:tenancy", "0366d6", "Isolamento multi-tenant"),
    ("modulo:ocupacao", "d4c5f9", "Painel de ocupação e métricas"),
    ("modulo:compliance", "d73a4a", "Conformidade LGPD e auditoria"),
    ("iso-12207", "006b75", "Norma ISO/IEC/IEEE 12207:2021")
]

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.returncode, result.stdout.strip(), result.stderr.strip()

def setup_labels():
    print("[setup] Criando labels padronizadas nos repositórios...")
    for repo_key, repo_name in REPOS.items():
        for name, color, desc in LABELS:
            cmd = f'gh label create "{name}" --description "{desc}" --color "{color}" --repo "{repo_name}" 2>/dev/null || true'
            run_cmd(cmd)
    print("  ✓ Labels criadas e sincronizadas.\n")

def create_issue(repo, title, body, labels):
    label_flags = " ".join([f'--label "{l}"' for l in labels])
    # Grava body temporário
    with open("/tmp/issue_body.md", "w") as f:
        f.write(body)
    
    cmd = f'gh issue create --repo "{repo}" --title "{title}" --body-file "/tmp/issue_body.md" {label_flags}'
    ret, out, err = run_cmd(cmd)
    if ret == 0:
        print(f"  ✓ [{repo.split('/')[1]}] {title} -> {out}")
    else:
        print(f"  ❌ Erro em '{title}': {err}")
    time.sleep(0.5)

print("Iniciando cadastro automático de issues...")
setup_labels()


DOCS_ISSUES = [
    {
        "title": "[DOCS(CAP-1)] Consolidar apresentação do software, escopo e identidade visual",
        "labels": ["tipo:docs", "prioridade:P1", "iso-12207"],
        "body": """## 🎯 Objetivo de Negócio
Apresentar formalmente a plataforma CineDoom no Manual de Processos de Software, delimitando com precisão o problema de gestão operacional de cinemas de pequeno e médio porte, os perfis de usuários atendidos (Atendente e Gerente) e as fronteiras estritas do escopo do MVP.

## 📋 Referências Normativas & Técnicas
- **Norma:** ABNT NBR ISO/IEC/IEEE 12207:2021 — Cláusula 6.4.1 (Processo de Definição de Necessidades e Requisitos dos Stakeholders).
- **Diretriz Docente:** `references/guidelines/estrutura-minima-manual.md` — Capítulo 1 (Seções 1.1 a 1.6).
- **Constituição:** `references/pdw/project-definition-workbook.md` — Seção 1 (Visão Geral e Modelo de Negócio).
- **Ativos de Marca:** `assets/logos/` (CineSoft Solutions e CineDoom).

## 🛠️ Atividades de Implementação
- [ ] Revisar e consolidar as seções 1.1 a 1.6 em `content/01-apresentacao-software.md`.
- [ ] Detalhar o problema de negócio: controles manuais descentralizados, risco de double-booking e falta de rastreabilidade auditável.
- [ ] Formalizar o público-alvo e contexto operacional do Atendente de bilheteria e Gerente de cinema.
- [ ] Declarar a matriz de escopo: incluídos (venda presencial atômica, mapa de assentos com polling de 2s, catálogo, ocupação) e excluídos (gateway de pagamento online, e-commerce, app mobile).
- [ ] Incorporar as logomarcas oficiais da CineSoft Solutions e CineDoom no documento.

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] Documento `content/01-apresentacao-software.md` revisado gramatical e tecnicamente.
- [ ] Zero menções a funcionalidades fora de escopo (pagamentos online/Stripe).
- [ ] Script `./scripts/montar-manual.sh` executa e incorpora o capítulo no manual consolidado.
- [ ] Aprovação em revisão por pares da equipe.

## ⏱️ Estimativa & Responsabilidade
- **Estimativa:** 3 horas | **Prioridade:** P1 (Alta)
"""
    },
    {
        "title": "[DOCS(CAP-2)] Formalizar processos de acordo (aquisição de nuvem e fornecimento B2B SaaS)",
        "labels": ["tipo:docs", "prioridade:P2", "iso-12207"],
        "body": """## 🎯 Objetivo de Negócio
Descrever formalmente os processos contratuais e de relacionamento da CineSoft Solutions com fornecedores terceiros de infraestrutura e com os clientes contratantes do CineDoom no modelo B2B SaaS.

## 📋 Referências Normativas & Técnicas
- **Norma:** ABNT NBR ISO/IEC/IEEE 12207:2021 — Cláusula 6.1 (Processos de Acordo: 6.1.1 Aquisição e 6.1.2 Fornecimento).
- **Diretriz Docente:** `references/guidelines/estrutura-minima-manual.md` — Capítulo 2 (Seções 2.1 a 2.3).
- **Decisões Técnicas:** ADR-004 (PostgreSQL Neon), ADR-005 (Vercel Serverless) e ADR-011 (Axiom Log Drain).

## 🛠️ Atividades de Implementação
- [ ] Documentar o processo de aquisição em `content/02-processos-acordo.md`: critérios de seleção e contratação de Neon (banco serverless ACID), Vercel (hosting e CDN) e Axiom (retenção de 365 dias).
- [ ] Elaborar a especificação do processo de fornecimento do SaaS B2B: modelo contratual, SLAs de disponibilidade (99.5%), canais de suporte e política de backups.
- [ ] Definir os critérios formais de aceite para ativação e entrega de novos tenants (cinemas).
- [ ] Mapear matriz de riscos associada a fornecedores terceiros e dependências externas.

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] Seções 2.1, 2.2 e 2.3 completamente detalhadas em `content/02-processos-acordo.md`.
- [ ] Tabela comparativa e justificativa de cada serviço terceiro adquirido.
- [ ] Cláusulas essenciais do contrato de fornecimento B2B devidamente formalizadas.
- [ ] Compilação de `./scripts/montar-manual.sh` validada.

## ⏱️ Estimativa & Responsabilidade
- **Estimativa:** 3 horas | **Prioridade:** P2 (Média)
"""
    },
    {
        "title": "[DOCS(CAP-3)] Estruturar processos organizacionais habilitadores, matriz RACI e gestão da qualidade",
        "labels": ["tipo:docs", "prioridade:P1", "iso-12207"],
        "body": """## 🎯 Objetivo de Negócio
Definir a estrutura organizacional, governança de papéis e capacitação da equipe CineSoft Solutions, justificando o modelo de ciclo de vida adotado e os padrões de garantia de qualidade para a entrega do CineDoom.

## 📋 Referências Normativas & Técnicas
- **Norma:** ABNT NBR ISO/IEC/IEEE 12207:2021 — Cláusula 6.2 (Processos Organizacionais Habilitadores de Projeto: 6.2.1 a 6.2.6).
- **Diretriz Docente:** `references/guidelines/estrutura-minima-manual.md` — Capítulo 3 (Seções 3.1 a 3.6).
- **Governança:** AI-4SDLC Platform (5 Gates HITL de qualidade).

## 🛠️ Atividades de Implementação
- [ ] Redigir a justificativa do ciclo de vida iterativo-incremental com gates de aprovação formal (G1 a G5) em `content/03-processos-organizacionais.md`.
- [ ] Mapear o inventário completo de ferramentas e infraestrutura (Next.js, Prisma, PostgreSQL, Docker, Vitest, Tectonic, GitHub).
- [ ] Construir a matriz RACI de responsabilidades distribuindo Carlos, Gabriel, Kayque e Yury entre os papéis de Engenharia, QA, DevOps e Governança.
- [ ] Definir o Plano de Garantia da Qualidade (QA): métricas de cobertura de código (>80%), tolerância zero a double-booking e critérios de aprovação de PR.
- [ ] Estabelecer a estratégia de gestão do conhecimento e Docs-as-Code.

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] Seções 3.1 a 3.6 completas em `content/03-processos-organizacionais.md`.
- [ ] Matriz RACI cobrindo todos os processos da norma com os 4 integrantes.
- [ ] Critérios de qualidade e métricas objetivas documentados.
- [ ] Documento validado na montagem do manual consolidado.

## ⏱️ Estimativa & Responsabilidade
- **Estimativa:** 4 horas | **Prioridade:** P1 (Alta)
"""
    },
    {
        "title": "[DOCS(CAP-4)] Mapear plano de gerenciamento técnico, matriz de riscos e as 11 ADRs",
        "labels": ["tipo:docs", "prioridade:P0", "iso-12207"],
        "body": """## 🎯 Objetivo de Negócio
Formalizar os processos de gerenciamento técnico do projeto CineDoom, estabelecendo cronograma com caminho crítico até a entrega final (12/11/2026), matriz de gestão de riscos com contingência, política de branches e o catálogo completo de decisões arquiteturais.

## 📋 Referências Normativas & Técnicas
- **Norma:** ABNT NBR ISO/IEC/IEEE 12207:2021 — Cláusula 6.3 (Processos de Gerenciamento Técnico: 6.3.1 a 6.3.8).
- **Diretriz Docente:** `references/guidelines/estrutura-minima-manual.md` — Capítulo 4 (Seções 4.1 a 4.5).
- **Especificações:** `specs/planning/tech-lead-plan.md` (20 tasks, 102h) e `specs/adrs/README.md` (ADR-001 a ADR-011).

## 🛠️ Atividades de Implementação
- [ ] Documentar o plano de projeto e cronograma em `content/04-gerenciamento-tecnico.md`, incorporando o plano de 20 tarefas e o caminho crítico.
- [ ] Mapear a matriz de riscos (R-01 a R-05) com probabilidade, impacto, mitigação e planos de contingência (ex: script de fallback local para a banca).
- [ ] Formalizar o plano de gestão de configuração: estratégia de branches (`main`, `develop`, `feat/`), SemVer e rastreabilidade de commits.
- [ ] Incorporar as 11 Architecture Decision Records formalizadas (ADR-001 a ADR-011) com contexto, decisão e consequências.
- [ ] Definir indicadores e métricas de acompanhamento de engenharia (Lead Time, Burndown, Densidade de Defeitos).

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] Seções 4.1 a 4.5 preenchidas com riqueza técnica em `content/04-gerenciamento-tecnico.md`.
- [ ] Todas as 11 ADRs devidamente registradas e explicadas.
- [ ] Cronograma realista alinhado à data de apresentação (12/11/2026).
- [ ] Sincronização via `./scripts/montar-manual.sh` executada com sucesso.

## ⏱️ Estimativa & Responsabilidade
- **Estimativa:** 5 horas | **Prioridade:** P0 (Crítica)
"""
    },
    {
        "title": "[DOCS(CAP-5.1)] Consolidar engenharia de requisitos, critérios de aceite e matriz de rastreabilidade",
        "labels": ["tipo:docs", "prioridade:P0", "iso-12207"],
        "body": """## 🎯 Objetivo de Negócio
Consolidar a especificação de requisitos do CineDoom no Capítulo 5 do Manual, estabelecendo rastreabilidade bidirecional estrita entre necessidades dos stakeholders, requisitos de negócio, critérios de aceite formais e testes automatizados.

## 📋 Referências Normativas & Técnicas
- **Norma:** ABNT NBR ISO/IEC/IEEE 12207:2021 — Cláusula 6.4.1 (Requisitos dos Stakeholders) e Cláusula 6.4.2 (Análise de Requisitos do Sistema).
- **Diretriz Docente:** `references/guidelines/estrutura-minima-manual.md` — Seção 5.1 (5.1.1 a 5.1.4).
- **Especificações:** `specs/cinedoom-spec.md` (US-1 a US-6 e AC-1 a AC-8).

## 🛠️ Atividades de Implementação
- [ ] Redigir a subseção 5.1 em `content/05-processos-tecnicos.md` documentando os Requisitos Funcionais (RF-01 a RF-12) e Não-Funcionais (RNF-01 a RNF-05).
- [ ] Detalhar as 6 Histórias de Usuário (`US-1` a `US-6`) com cenários `Dado / Quando / Então`.
- [ ] Documentar os 8 Critérios de Aceite formais (`AC-1` a `AC-8`), incluindo a trava atômica ACID e o polling de 2s.
- [ ] Construir a Matriz de Rastreabilidade Bidirecional ligando cada requisito aos seus respectivos testes e commits.

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] Seção 5.1 completa em `content/05-processos-tecnicos.md`.
- [ ] Cobertura 100% de rastreabilidade para os critérios AC-1 a AC-8.
- [ ] Tabela de requisitos classificada formalmente pelo método MoSCoW.
- [ ] Recompilação validada no pipeline.

## ⏱️ Estimativa & Responsabilidade
- **Estimativa:** 4 horas | **Prioridade:** P0 (Crítica)
"""
    },
    {
        "title": "[DOCS(CAP-5.2)] Documentar arquitetura em modelo C4, modelo relacional Prisma e design system",
        "labels": ["tipo:docs", "prioridade:P0", "iso-12207"],
        "body": """## 🎯 Objetivo de Negócio
Formalizar a arquitetura e design de software do CineDoom no Capítulo 5, documentando a visão em camadas C4 (Contexto, Contêineres e Componentes), o dicionário relacional de dados Prisma e as especificações de interface do SeatingGrid.

## 📋 Referências Normativas & Técnicas
- **Norma:** ABNT NBR ISO/IEC/IEEE 12207:2021 — Cláusula 6.4.3 (Processo de Definição da Arquitetura) e Cláusula 6.4.4 (Design).
- **Diretriz Docente:** `references/guidelines/estrutura-minima-manual.md` — Seção 5.2.
- **Especificações:** `specs/architecture/` (C4 & UI Mockups) e `specs/data-model/data-model.md`.

## 🛠️ Atividades de Implementação
- [ ] Inserir os diagramas arquiteturais C4 (Contexto e Contêineres) em `content/05-processos-tecnicos.md`.
- [ ] Documentar a arquitetura em Monólito Modular Next.js 14 com isolamento de serviços de domínio.
- [ ] Apresentar o modelo de dados relacional (9 entidades) com cardinalidades, índices e o racional da pré-população de `session_seats`.
- [ ] Documentar o Design System: paleta cromática (`#1A1A2E`, `#E94560`), tipografia Inter e estados visuais do mapa de assentos.

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] Seção 5.2 preenchida com profundidade técnica e diagramas nítidos.
- [ ] Esquema relacional Prisma e dicionário de dados formalmente documentados.
- [ ] Componente SeatingGrid detalhado com estados cromáticos e acessibilidade.

## ⏱️ Estimativa & Responsabilidade
- **Estimativa:** 4 horas | **Prioridade:** P0 (Crítica)
"""
    },
    {
        "title": "[DOCS(CAP-5.3)] Elaborar modelagem de ameaças STRIDE e avaliação de impacto à privacidade (DPIA LGPD)",
        "labels": ["tipo:docs", "prioridade:P1", "iso-12207"],
        "body": """## 🎯 Objetivo de Negócio
Documentar os requisitos e controles de segurança da informação e privacidade no Capítulo 5, apresentando a modelagem de ameaças pelo método STRIDE e o Relatório de Impacto à Proteção de Dados (DPIA) em conformidade com a LGPD.

## 📋 Referências Normativas & Técnicas
- **Norma:** ABNT NBR ISO/IEC/IEEE 12207:2021 — Processos Técnicos (Segurança e Integridade).
- **Legislação:** Lei Geral de Proteção de Dados (Lei 13.709/2018 - Art. 18, 38 e 41) e CDC (Lei 8.078/1990 - Art. 27).
- **Especificações:** `specs/security-compliance/threat-model.md` e `compliance-assessment.md`.

## 🛠️ Atividades de Implementação
- [ ] Incorporar a matriz de ameaças STRIDE (Spoofing, Tampering, Repudiation, Info Disclosure, DoS, Elevation of Privilege) em `content/05-processos-tecnicos.md`.
- [ ] Documentar o DPIA (Relatório de Impacto) justificando o tratamento de CPF em escala B2B e o papel de DPO interno.
- [ ] Detalhar o mecanismo criptográfico de dupla camada: HMAC-SHA256 (blind index) e AES-256-GCM (armazenamento seguro).
- [ ] Documentar o equilíbrio entre direito ao esquecimento (LGPD Art. 18 via soft-anonymize) e obrigação legal de retenção de 5 anos pelo CDC.

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] Seção de segurança e conformidade LGPD formalizada no manual.
- [ ] Matriz STRIDE completa com todas as categorias e controles de mitigação.
- [ ] Fluxo de anonimização in-place claramente explicado e respaldado juridicamente.

## ⏱️ Estimativa & Responsabilidade
- **Estimativa:** 4 horas | **Prioridade:** P1 (Alta)
"""
    },
    {
        "title": "[DOCS(CAP-5.4)] Definir processos de verificação e validação com suíte de concorrência ACID",
        "labels": ["tipo:docs", "prioridade:P1", "iso-12207"],
        "body": """## 🎯 Objetivo de Negócio
Documentar formalmente os processos de Verificação e Validação do CineDoom, apresentando a estratégia da pirâmide de testes e a comprovação matemática contra double-booking através do teste de estresse de concorrência.

## 📋 Referências Normativas & Técnicas
- **Norma:** ABNT NBR ISO/IEC/IEEE 12207:2021 — Cláusula 6.4.9 (Processo de Verificação) e Cláusula 6.4.10 (Processo de Validação).
- **Diretriz Docente:** `references/guidelines/estrutura-minima-manual.md` — Seção 5 (Verificação e Validação).
- **Especificações:** `specs/quality/test-strategy.md` (Matriz QA e Casos de Teste TC-1 a TC-3).

## 🛠️ Atividades de Implementação
- [ ] Redigir a seção de V&V em `content/05-processos-tecnicos.md`, descrevendo a pirâmide de testes (Unitários, Integração, Concorrência e E2E).
- [ ] Mapear a cobertura dos testes automatizados em relação aos critérios de aceite AC-1 a AC-8.
- [ ] Detalhar o protocolo do teste de estresse de 50 threads simultâneas disparadas via `Promise.allSettled`.
- [ ] Definir o plano de homologação com stakeholders e roteiro de testes de usabilidade no balcão.

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] Seções de Verificação e Validação detalhadas com casos de teste nominais.
- [ ] Critério de sucesso do teste de concorrência formalizado (1 sucesso HTTP 201, 49 conflitos HTTP 409).
- [ ] Matriz de rastreabilidade entre requisitos e suítes de teste.

## ⏱️ Estimativa & Responsabilidade
- **Estimativa:** 3 horas | **Prioridade:** P1 (Alta)
"""
    },
    {
        "title": "[DOCS(LATEX)] Diagramar relatório técnico ABNT NBR 14724 e automatizar compilação Tectonic",
        "labels": ["tipo:docs", "prioridade:P0", "iso-12207"],
        "body": """## 🎯 Objetivo de Negócio
Diagramar o Manual de Processos de Software completo em LaTeX estritamente conforme as normas da ABNT, gerando o PDF final para entrega e avaliação pela banca examinadora.

## 📋 Referências Normativas & Técnicas
- **Normas ABNT:** NBR 14724 (Trabalhos Acadêmicos), NBR 6024 (Numeração Progressiva), NBR 6027 (Sumário) e NBR 6023 (Referências).
- **Arquivos Fonte:** `content/*.md` e `latex/report/manual-processos-software.tex`.
- **Motor de Tipografia:** Tectonic Typesetting Engine (`scripts/compilar.sh`).

## 🛠️ Atividades de Implementação
- [ ] Sincronizar o conteúdo dos capítulos 1 a 5 de `content/` com os arquivos LaTeX em `latex/report/`.
- [ ] Formatar tabelas no padrão booktabs / tabularx com recuos e fontes adequadas.
- [ ] Ajustar margens regulamentares (3cm superior e esquerda, 2cm inferior e direita) e entrelinha de 1.5.
- [ ] Configurar numeração de páginas no cabeçalho superior direito a partir da introdução textual.
- [ ] Validar compilação automática no GitHub Actions e localmente via `./scripts/compilar.sh`.

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] PDF `latex/report/manual-processos-software.pdf` compilado sem erros ou advertências graves.
- [ ] Sumário, listas de figuras/tabelas e referências perfeitamente alinhados.
- [ ] Workflow `.github/workflows/compilar-docs.yml` verde no GitHub Actions.

## ⏱️ Estimativa & Responsabilidade
- **Estimativa:** 4 horas | **Prioridade:** P0 (Crítica)
"""
    },
    {
        "title": "[DOCS(SLIDES)] Confeccionar apresentação Beamer oficial UFG/INF e roteiro da defesa oral",
        "labels": ["tipo:docs", "prioridade:P1", "iso-12207"],
        "body": """## 🎯 Objetivo de Negócio
Desenvolver a apresentação de slides oficial em Beamer utilizando o template institucional da UFG/INF e elaborar o roteiro da defesa oral perante a banca avaliadora da Profa. Dra. Juliana Zinader.

## 📋 Referências Normativas & Técnicas
- **Tema Beamer:** `latex/presentation/beamerthemeUfg.sty` e `latex/presentation/lib/`.
- **Diretriz de Avaliação:** Simulação de auditoria de processos de software e demonstração ao vivo do sistema.
- **Data da Apresentação:** 12 de novembro de 2026.

## 🛠️ Atividades de Implementação
- [ ] Estruturar o deck de 15 a 20 slides em `latex/presentation/apresentacao-manual.tex`.
- [ ] Inserir tópicos essenciais: Contextualização da CineSoft, ISO 12207 aplicada, Governança HITL, Arquitetura C4, Venda Atômica ACID e Lições Aprendidas.
- [ ] Adicionar logomarcas oficiais e capturas de tela/mockups do CineDoom.
- [ ] Redigir o roteiro da demonstração ao vivo (simulação de venda no balcão e preenchimento da sessão no painel do gerente).
- [ ] Testar compilação via `./scripts/compilar.sh` gerando `apresentacao-manual.pdf`.

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] Slides compilando em alta definição com tempo de apresentação calibrado para 20 minutos.
- [ ] Roteiro de demonstração ao vivo documentado com atribuição de fala para os 4 integrantes.
- [ ] PDF final validado e pronto para projeção.

## ⏱️ Estimativa & Responsabilidade
- **Estimativa:** 4 horas | **Prioridade:** P1 (Alta)
"""
    }
]

print(f"Total de issues do Manual: {len(DOCS_ISSUES)}")

APP_ISSUES = [
    {
        "title": "[FEAT(INFRA)] Project scaffolding & monorepo setup (Next.js 14, Tailwind, TypeScript)",
        "labels": ["tipo:infra", "prioridade:P0"],
        "body": """## 🎯 Objetivo do Requisito
Inicializar a estrutura do repositório cinedoom-app com Next.js 14 App Router, TypeScript no modo estrito e Tailwind CSS configurado com os tokens visuais da marca, garantindo modularidade arquitetural e zero dependências circulares.

## 📋 Rastreabilidade & Especificações
- **Task TechLead:** TASK-1 | **Caminho Crítico:** Sim (Etapa 1)
- **ADRs Vinculadas:** ADR-001 (Monólito Modular Next.js 14), ADR-002 (Tailwind CSS) e ADR-003 (TypeScript).
- **Design Tokens:** `assets/logos/cinesoft-cinedoom-brand-guide.png` (Primary: `#1A1A2E`, CTA: `#E94560`, Neutral: `#F5F5F5`).

## 🛠️ Atividades de Desenvolvimento
- [ ] Inicializar projeto Next.js 14 App Router com TypeScript.
- [ ] Configurar Tailwind CSS incluindo a paleta oficial nos tokens `primary`, `cta` e `neutralBg`.
- [ ] Organizar estrutura de pastas por domínios: `src/modules/bilheteria`, `backoffice`, `auth`, `tenancy`, `ocupacao`.
- [ ] Configurar ESLint com regra `import/no-cycle` para impedir dependências circulares entre módulos.
- [ ] Criar arquivo `.env.example` documentando todas as variáveis de ambiente necessárias.

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] `pnpm install` e `pnpm dev` sobem aplicação limpa em `http://localhost:3000`.
- [ ] Zero erros de linter e tipagem estrita validada via `pnpm tsc --noEmit`.
- [ ] Página inicial exibindo branding do CineDoom e botões de navegação.

## ⏱️ Estimativa & Caminho Crítico
- **Estimativa:** 4 horas | **Prioridade:** P0 (Bloqueante) | **Dependências:** Nenhuma
"""
    },
    {
        "title": "[FEAT(DB)] Database schema design, Prisma migrations e trigger append-only de cancelamento",
        "labels": ["tipo:feat", "prioridade:P0", "modulo:backoffice"],
        "body": """## 🎯 Objetivo do Requisito
Implementar o schema relacional no Prisma ORM com as 9 entidades de domínio do CineDoom, conectar ao PostgreSQL gerenciado no Neon e criar a migração contendo a trigger de imutabilidade na tabela de auditoria de cancelamentos.

## 📋 Rastreabilidade & Especificações
- **Task TechLead:** TASK-2 | **Cobre Critérios:** AC-4 (Multi-tenancy), AC-8 (Validações).
- **ADRs Vinculadas:** ADR-004 (PostgreSQL Neon ACID) e ADR-010 (Trigger append-only de cancelamento).
- **Especificação:** `specs/data-model/data-model.md`.

## 🛠️ Atividades de Desenvolvimento
- [ ] Criar arquivo `prisma/schema.prisma` com os modelos: `Tenant`, `User`, `Movie`, `Room`, `Seat`, `Session`, `SessionSeat`, `Ticket`, `Buyer`, `CancellationAudit`.
- [ ] Adicionar campo `tenant_id` indexado em todas as tabelas de negócio.
- [ ] Configurar restrições de integridade referencial e unicidade (`@@unique([sessionId, seatId])`).
- [ ] Criar migration inicial contendo a função e trigger PostgreSQL `BEFORE UPDATE OR DELETE` em `cancellation_audits` para lançar exceção SQL.
- [ ] Conectar ao banco Neon Serverless e executar migração inicial.

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] `pnpm prisma migrate dev` executa com sucesso e gera o Prisma Client tipado.
- [ ] Trigger de banco bloqueia qualquer `UPDATE` ou `DELETE` em `cancellation_audits`.
- [ ] Teste unitário de banco confirmando o lançamento da exceção em tentativas de alteração.

## ⏱️ Estimativa & Caminho Crítico
- **Estimativa:** 6 horas | **Prioridade:** P0 (Bloqueante) | **Depende de:** TASK-1
"""
    },
    {
        "title": "[FEAT(TENANCY)] Multi-tenant Prisma extension para isolamento estrito row-level",
        "labels": ["tipo:security", "prioridade:P0", "modulo:tenancy"],
        "body": """## 🎯 Objetivo do Requisito
Implementar uma extensão do Prisma Client combinada com AsyncLocalStorage para injetar automaticamente o filtro `WHERE tenant_id = :tenantId` em todas as operações de banco, garantindo isolamento estrito entre cinemas diferentes sem depender de cláusulas manuais.

## 📋 Rastreabilidade & Especificações
- **Task TechLead:** TASK-3 | **Cobre Critérios:** AC-4 (Isolamento Multi-tenant).
- **ADRs Vinculadas:** ADR-004 (PostgreSQL Prisma).
- **Especificação:** `specs/architecture/software-architecture.md` (Tenancy Middleware).

## 🛠️ Atividades de Desenvolvimento
- [ ] Implementar middleware Next.js que extrai `tenant_id` da sessão JWT ou subdomínio/header.
- [ ] Armazenar o contexto do tenant em `AsyncLocalStorage` no ciclo de vida da requisição.
- [ ] Desenvolver `Prisma Client Extension` que intercepta `findMany`, `findFirst`, `count`, `update`, `delete`, aplicando `WHERE tenant_id = currentTenantId`.
- [ ] Implementar suíte de testes unitários simulando dois tenants distintos em operações paralelas.

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] Requisição autenticada no Tenant A é incapaz de ler ou modificar registros do Tenant B, mesmo forjando IDs na URL.
- [ ] Testes unitários com 100% de aprovação comprovando zero vazamento cross-tenant.

## ⏱️ Estimativa & Caminho Crítico
- **Estimativa:** 5 horas | **Prioridade:** P0 | **Depende de:** TASK-2
"""
    },
    {
        "title": "[FEAT(AUTH)] Autenticação e controle de acesso RBAC via NextAuth.js (Atendente vs Gerente)",
        "labels": ["tipo:security", "prioridade:P0", "modulo:auth"],
        "body": """## 🎯 Objetivo do Requisito
Configurar autenticação corporativa segura e controle de acesso baseado em papéis (RBAC) através do NextAuth.js, diferenciando os acessos do Atendente de bilheteria e do Gerente de cinema.

## 📋 Rastreabilidade & Especificações
- **Task TechLead:** TASK-4 | **Cobre Critérios:** AC-5 (Controle de Acesso RBAC).
- **ADRs Vinculadas:** ADR-003 (Route Handlers) e ADR-005 (NextAuth).
- **Especificação:** `specs/architecture/software-architecture.md` (Auth Module).

## 🛠️ Atividades de Desenvolvimento
- [ ] Configurar NextAuth.js com Credentials Provider e validação de senha via bcrypt.
- [ ] Injetar `userId`, `tenantId` e `role` (`ATENDENTE` | `GERENTE`) na sessão e no token JWT.
- [ ] Criar middleware de proteção de rotas: Atendente acessa bilheteria e catálogo; rotas `/backoffice/*` e `/api/backoffice/*` respondem com `HTTP 403 Forbidden` para Atendentes.
- [ ] Desenvolver telas de login customizadas no design system do CineDoom.

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] Login e logout funcionais com persistência segura do token em cookie HTTP-only.
- [ ] Atendente tentando acessar rotas gerenciais recebe compulsoriamente status `403`.
- [ ] Gerente autenticado tem acesso irrestrito às rotas administrativas do seu tenant.

## ⏱️ Estimativa & Caminho Crítico
- **Estimativa:** 6 horas | **Prioridade:** P0 | **Depende de:** TASK-2
"""
    },
    {
        "title": "[FEAT(SECURITY)] Módulo CryptoService com HMAC-SHA256 (blind index) e AES-256-GCM para CPF",
        "labels": ["tipo:security", "prioridade:P0", "modulo:compliance"],
        "body": """## 🎯 Objetivo do Requisito
Implementar o módulo criptográfico CryptoService para proteção de dados pessoais (PII) dos compradores, armazenando o CPF com AES-256-GCM e gerando o índice cego de busca via HMAC-SHA256 para prevenir ataques de rainbow table sobre o espaço finito de CPFs.

## 📋 Rastreabilidade & Especificações
- **Task TechLead:** TASK-5 | **Cobre Critérios:** AC-6 (Criptografia de CPF e Busca Blind Index).
- **ADRs Vinculadas:** ADR-008 (Criptografia em Duas Camadas de CPF).
- **Especificação:** `specs/security-compliance/threat-model.md` e `compliance-assessment.md`.

## 🛠️ Atividades de Desenvolvimento
- [ ] Desenvolver `CryptoService` com cifra reversível AES-256-GCM (IV aleatório de 12 bytes + Auth Tag).
- [ ] Implementar cálculo de hash determinístico com HMAC-SHA256 utilizando chave de ambiente secreta `CINEDOOM_CPF_HMAC_KEY`.
- [ ] Criar funções de sanitização de CPF (remoção de pontos e traços antes da cifra/hash).
- [ ] Implementar testes unitários validando cifra, decifra e busca indexada em tempo O(1).

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] O CPF nunca é persistido em texto claro no banco de dados.
- [ ] Busca de comprador por CPF executada via `cpf_search_hash` aproveitando índice único de banco.
- [ ] Testes unitários com 100% de cobertura no `CryptoService`.

## ⏱️ Estimativa & Caminho Crítico
- **Estimativa:** 5 horas | **Prioridade:** P0 | **Depende de:** TASK-2
"""
    },
    {
        "title": "[FEAT(CATALOG)] Backoffice - CRUD de catálogo de filmes e validações de domínio",
        "labels": ["tipo:feat", "prioridade:P1", "modulo:backoffice"],
        "body": """## 🎯 Objetivo do Requisito
Desenvolver as telas de interface e os Route Handlers de API para gerenciamento completo do catálogo de filmes do cinema pelo Gerente.

## 📋 Rastreabilidade & Especificações
- **Task TechLead:** TASK-6 | **Cobre Critérios:** AC-5 (Acesso Gerente), AC-8 (CRUD e Validações).
- **Especificação:** `specs/cinedoom-spec.md` (US-6) e `specs/architecture/ui-mockups.md`.

## 🛠️ Atividades de Desenvolvimento
- [ ] Implementar Route Handlers `/api/filmes` (GET, POST, PUT, DELETE).
- [ ] Configurar validação de schemas com Zod (título obrigatório, duração em minutos > 0, classificação indicativa).
- [ ] Desenvolver telas de listagem com busca e formulário modal de cadastro/edição de filme.
- [ ] Retornar `HTTP 422 Unprocessable Entity` com array detalhado de erros por campo em requisições inválidas.

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] Gerente cadastra, edita e inativa filmes com sucesso.
- [ ] Atendente recebe `HTTP 403` ao tentar criar ou editar filmes.
- [ ] Payload com dados inválidos retorna erro 422 descritivo.

## ⏱️ Estimativa & Caminho Crítico
- **Estimativa:** 5 horas | **Prioridade:** P1 | **Depende de:** TASK-3, TASK-4
"""
    },
    {
        "title": "[FEAT(ROOMS)] Backoffice - CRUD de salas e geração física do mapa de assentos",
        "labels": ["tipo:feat", "prioridade:P0", "modulo:backoffice"],
        "body": """## 🎯 Objetivo do Requisito
Desenvolver o módulo de gerenciamento de salas de cinema pelo Gerente, gerando automaticamente no banco a matriz física de assentos (Seat) ao cadastrar a sala.

## 📋 Rastreabilidade & Especificações
- **Task TechLead:** TASK-7 | **Cobre Critérios:** AC-5, AC-8.
- **Especificação:** `specs/data-model/data-model.md` (Entidades Room e Seat).

## 🛠️ Atividades de Desenvolvimento
- [ ] Implementar Route Handlers `/api/salas` para criação, listagem e detalhamento de salas.
- [ ] Desenvolver lógica transacional que, ao criar uma sala (ex: 10 fileiras x 12 colunas = 120 assentos), insere em lote os 120 registros de `Seat`.
- [ ] Desenvolver interface visual de pré-visualização da disposição das poltronas na sala.
- [ ] Garantir restrição de unicidade em identificadores de assento por sala (`A1`, `A2`, etc.).

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] Criação de sala gera deterministicamente todos os assentos fixos associados.
- [ ] Interface exibe a planta física da sala para conferência do Gerente.

## ⏱️ Estimativa & Caminho Crítico
- **Estimativa:** 6 horas | **Prioridade:** P0 | **Depende de:** TASK-3, TASK-4
"""
    },
    {
        "title": "[FEAT(SESSIONS)] Backoffice - CRUD de sessões cinematográficas com pré-população de SessionSeat",
        "labels": ["tipo:feat", "prioridade:P0", "modulo:backoffice"],
        "body": """## 🎯 Objetivo do Requisito
Implementar o agendamento de sessões de cinema pelo Gerente, vinculando filme, sala, horário e preço, com pré-população obrigatória da tabela `session_seats` para habilitar travas atômicas ACID.

## 📋 Rastreabilidade & Especificações
- **Task TechLead:** TASK-8 | **Cobre Critérios:** AC-5, AC-8.
- **ADRs Vinculadas:** ADR-007 (Pré-população de SessionSeat para SELECT FOR UPDATE).
- **Especificação:** `specs/architecture/software-architecture.md`.

## 🛠️ Atividades de Desenvolvimento
- [ ] Implementar Route Handlers `/api/sessoes` com validação de conflito de horário (sala ocupada).
- [ ] Implementar transação Prisma que cria o registro `Session` e, no mesmo commit, insere N linhas em `session_seats` com status inicial `AVAILABLE`.
- [ ] Desenvolver formulário de agendamento de sessão com seleção de filme, sala, data/hora e valor do ingresso.

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] Toda sessão criada possui exatamente $N$ assentos disponíveis pré-inseridos no banco.
- [ ] Sistema impede agendamento de duas sessões sobrepostas na mesma sala.

## ⏱️ Estimativa & Caminho Crítico
- **Estimativa:** 5 horas | **Prioridade:** P0 | **Depende de:** TASK-6, TASK-7
"""
    },
    {
        "title": "[FEAT(UI)] Design System - Componente SeatingGrid interativo e estados cromáticos",
        "labels": ["tipo:feat", "prioridade:P0", "modulo:bilheteria"],
        "body": """## 🎯 Objetivo do Requisito
Desenvolver o componente visual interativo SeatingGrid para renderização do mapa de assentos da sala, seguindo os tokens oficiais da identidade visual do CineDoom.

## 📋 Rastreabilidade & Especificações
- **Task TechLead:** TASK-17 | **Cobre Critérios:** AC-1, AC-2.
- **Design Tokens:** `assets/logos/cinesoft-cinedoom-brand-guide.png`.
- **Especificação:** `specs/architecture/ui-mockups.md`.

## 🛠️ Atividades de Desenvolvimento
- [ ] Construir componente React `SeatingGrid` em Client Component com renderização rápida (<100ms).
- [ ] Estilizar estados de assento com Tailwind: Disponível (cinza neutro), Selecionado (vermelho `#E94560`), Ocupado/Vendido (cinza escuro desabilitado) e Em Processamento.
- [ ] Incluir representação visual da tela do cinema e legendas de identificação de fileiras (A-Z) e números.
- [ ] Suporte a seleção múltipla de assentos para compra em lote.

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] Clique em assento disponível altera estado para selecionado e recalcula valor total.
- [ ] Assentos vendidos são visualmente bloqueados e não respondem a cliques.
- [ ] Totalmente responsivo e acessível via teclado.

## ⏱️ Estimativa & Caminho Crítico
- **Estimativa:** 6 horas | **Prioridade:** P0 | **Depende de:** TASK-1
"""
    },
    {
        "title": "[FEAT(POLLING)] Bilheteria - Route handler e hook de polling a cada 2s do mapa de assentos",
        "labels": ["tipo:feat", "prioridade:P0", "modulo:bilheteria"],
        "body": """## 🎯 Objetivo do Requisito
Implementar o endpoint de consulta rápida do mapa de assentos e o hook React de polling a cada 2000ms para manter a tela do Atendente atualizada em tempo quase real.

## 📋 Rastreabilidade & Especificações
- **Task TechLead:** TASK-9 | **Cobre Critérios:** AC-2 (Atualização em $\le 2$ segundos).
- **ADRs Vinculadas:** ADR-006 (Polling REST HTTP de 2s).
- **Especificação:** `specs/cinedoom-spec.md` (AC-2).

## 🛠️ Atividades de Desenvolvimento
- [ ] Implementar rota otimizada `GET /api/sessoes/[id]/assentos` retornando array leve com `id`, `seat_id`, `row`, `number` e `status`.
- [ ] Desenvolver hook React `useSessionSeats(sessionId)` com intervalo fixo de 2000ms.
- [ ] Implementar mecanismo de desativação do polling quando a janela ou aba do navegador estiver inativa (Page Visibility API).
- [ ] Atualizar o componente `SeatingGrid` com transições suaves de estado sem recarregar a tela inteira.

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] Uma venda concluída em um terminal reflete no mapa de outro terminal em menos de 2 segundos.
- [ ] Endpoint responde em menos de 100ms sob carga normal de requisições.

## ⏱️ Estimativa & Caminho Crítico
- **Estimativa:** 5 horas | **Prioridade:** P0 | **Depende de:** TASK-8, TASK-17
"""
    },
    {
        "title": "[FEAT(CHECKOUT)] Bilheteria - Venda atômica ACID com SELECT FOR UPDATE anti-double-booking",
        "labels": ["tipo:feat", "prioridade:P0", "modulo:bilheteria"],
        "body": """## 🎯 Objetivo do Requisito
Implementar o fluxo transacional de venda de ingressos com trava pessimista em nível de linha no PostgreSQL, garantindo matematicamente zero ocorrências de double-booking sob concorrência de múltiplos terminais.

## 📋 Rastreabilidade & Especificações
- **Task TechLead:** TASK-10 | **Cobre Critérios:** AC-1 (Venda Atômica ACID), AC-6 (Associação de Comprador).
- **ADRs Vinculadas:** ADR-004 (Transações ACID PostgreSQL) e ADR-007 (SELECT FOR UPDATE).
- **Especificação:** `specs/cinedoom-spec.md` (AC-1) e `specs/architecture/software-architecture.md`.

## 🛠️ Atividades de Desenvolvimento
- [ ] Implementar Route Handler `POST /api/vendas` executando `$transaction` no Prisma.
- [ ] Executar query raw com lock pessimista: `SELECT id, status FROM session_seats WHERE id IN (...) FOR UPDATE`.
- [ ] Validar status de todos os assentos; se qualquer assento já estiver `SOLD`, reverter transação e retornar `HTTP 409 Conflict`.
- [ ] Se todos estiverem disponíveis, atualizar status para `SOLD`, criar registro de `Ticket` e vincular/criar comprador via `CryptoService`.
- [ ] Retornar `HTTP 201 Created` com os identificadores e dados do ingresso emitido.

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] Venda concluída altera estado do assento deterministicamente para `SOLD`.
- [ ] Requisições concorrentes disputando o mesmo assento: exatamente uma obtém sucesso (201) e as demais recebem 409 Conflict.
- [ ] Zero duplicação de bilhetes para o mesmo assento na mesma sessão.

## ⏱️ Estimativa & Caminho Crítico
- **Estimativa:** 8 horas | **Prioridade:** P0 (Coração do MVP) | **Depende de:** TASK-5, TASK-9
"""
    },
    {
        "title": "[FEAT(CANCELLATION)] Bilheteria - Cancelamento auditável com trigger append-only no PostgreSQL",
        "labels": ["tipo:feat", "prioridade:P0", "modulo:bilheteria"],
        "body": """## 🎯 Objetivo do Requisito
Implementar o cancelamento de ingressos com registro obrigatório de auditoria imutável antes da liberação do assento de volta para o status disponível.

## 📋 Rastreabilidade & Especificações
- **Task TechLead:** TASK-11 | **Cobre Critérios:** AC-3 (Cancelamento Auditável com Registro Imutável), AC-5 (Acesso Atendente).
- **ADRs Vinculadas:** ADR-010 (Auditoria Append-Only via Trigger).
- **Especificação:** `specs/cinedoom-spec.md` (AC-3).

## 🛠️ Atividades de Desenvolvimento
- [ ] Implementar rota `POST /api/ingressos/[id]/cancelar` recebendo justificativa textual obrigatória.
- [ ] Validar se a sessão ainda não ocorreu (sessões passadas não permitem cancelamento).
- [ ] Executar transação atômica que insere registro em `cancellation_audits` (com `user_id`, `timestamp UTC`, `motivo`, `tenant_id`) ANTES de alterar o `SessionSeat` para `AVAILABLE`.
- [ ] Garantir que se a inserção da auditoria falhar, o assento permanece vendido (rollback atômico).

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] Registro de cancelamento persistido e impossível de ser deletado ou alterado pelo banco.
- [ ] Assento cancelado volta a aparecer como disponível no polling de 2s para todos os terminais.
- [ ] Cancelamento sem motivo é rejeitado com status `422`.

## ⏱️ Estimativa & Caminho Crítico
- **Estimativa:** 4 horas | **Prioridade:** P0 | **Depende de:** TASK-10
"""
    },
    {
        "title": "[FEAT(DASHBOARD)] Painel gerencial de ocupação de sessões do dia em tempo real",
        "labels": ["tipo:feat", "prioridade:P1", "modulo:ocupacao"],
        "body": """## 🎯 Objetivo do Requisito
Desenvolver o painel de ocupação acessível exclusivamente pelo Gerente, exibindo a taxa de lotação percentual de cada sessão do dia corrente em tempo real.

## 📋 Rastreabilidade & Especificações
- **Task TechLead:** TASK-12 | **Cobre Critérios:** AC-5, AC-7 (Painel de Ocupação do Gerente).
- **Especificação:** `specs/cinedoom-spec.md` (AC-7) e `specs/architecture/ui-mockups.md`.

## 🛠️ Atividades de Desenvolvimento
- [ ] Implementar rota `GET /api/ocupacao/painel` agregando dados de sessões da data atual.
- [ ] Calcular métricas por sessão: capacidade total da sala, assentos vendidos e percentual de ocupação `(vendidos / total) * 100`.
- [ ] Construir tela no Next.js com cards visuais por sessão contendo barra de progresso de lotação e filtros por sala/horário.
- [ ] Garantir isolamento multi-tenant (o painel exibe apenas sessões do cinema do Gerente autenticado).

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] Painel exibe sessões de hoje com contagem e percentual exatos de assentos vendidos.
- [ ] Uma venda efetuada na bilheteria atualiza os números da sessão no painel do Gerente ao recarregar a tela.
- [ ] Atendentes recebem `HTTP 403` ao tentar acessar a rota.

## ⏱️ Estimativa & Caminho Crítico
- **Estimativa:** 4 horas | **Prioridade:** P1 | **Depende de:** TASK-8, TASK-4
"""
    },
    {
        "title": "[FEAT(USERS)] Backoffice - Gestão e ativação de contas de Atendentes pelo Gerente",
        "labels": ["tipo:feat", "prioridade:P1", "modulo:auth"],
        "body": """## 🎯 Objetivo do Requisito
Permitir que o Gerente de um cinema gerencie os usuários operadores de bilheteria (Atendentes) vinculados exclusivamente ao seu tenant.

## 📋 Rastreabilidade & Especificações
- **Task TechLead:** TASK-13 | **Cobre Critérios:** AC-5 (Gestão de Usuários RBAC).
- **Especificação:** `specs/architecture/software-architecture.md`.

## 🛠️ Atividades de Desenvolvimento
- [ ] Implementar rotas `/api/backoffice/usuarios` para criação, listagem e inativação de Atendentes.
- [ ] Formulário modal para cadastro de Atendente com nome, e-mail e senha inicial.
- [ ] Associar compulsoriamente o `tenant_id` do Gerente logado ao novo usuário criado.
- [ ] Bloquear criação de usuários com perfil `GERENTE` ou alteração de usuários de outros cinemas.

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] Gerente cadastra operador e o operador consegue logar imediatamente na bilheteria.
- [ ] Operador inativado perde acesso à aplicação imediatamente.

## ⏱️ Estimativa & Caminho Crítico
- **Estimativa:** 4 horas | **Prioridade:** P1 | **Depende de:** TASK-4
"""
    },
    {
        "title": "[FEAT(COMPLIANCE)] Compliance LGPD - Endpoint de anonimização in-place de compradores (Art. 18)",
        "labels": ["tipo:security", "prioridade:P1", "modulo:compliance"],
        "body": """## 🎯 Objetivo do Requisito
Implementar o fluxo operacional de atendimento aos direitos dos titulares da LGPD (Art. 18), executando a anonimização in-place de dados pessoais sem romper a integridade contábil exigida pelo Código de Defesa do Consumidor (5 anos).

## 📋 Rastreabilidade & Especificações
- **Task TechLead:** TASK-14 | **Cobre Critérios:** AC-6 (Privacidade e Direitos LGPD).
- **ADRs Vinculadas:** ADR-009 (Anonimização In-Place).
- **Especificação:** `specs/security-compliance/compliance-assessment.md`.

## 🛠️ Atividades de Desenvolvimento
- [ ] Implementar rota `POST /api/titulares/anonimizar` acionável pelo Gerente/DPO.
- [ ] Localizar o comprador pelo hash de busca `cpf_search_hash`.
- [ ] Sobrescrever campos PII (`name`, `email`, `cpf_encrypted`, `cpf_search_hash`) com valores nulos/hashes irreconhecíveis e setar `anonymized_at = NOW()`.
- [ ] Manter o ID do comprador intacto para preservar chaves estrangeiras com `Ticket` e auditoria de cancelamentos.

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] Todos os dados identificáveis do comprador são expurgados do banco.
- [ ] Ingressos vendidos permanecem associados ao ID anônimo sem quebra de integridade referencial.

## ⏱️ Estimativa & Caminho Crítico
- **Estimativa:** 4 horas | **Prioridade:** P1 | **Depende de:** TASK-5
"""
    },
    {
        "title": "[FEAT(OBSERVABILITY)] Observabilidade - Integração do Vercel Log Drain com Axiom para retenção de 365 dias",
        "labels": ["tipo:infra", "prioridade:P2", "modulo:compliance"],
        "body": """## 🎯 Objetivo do Requisito
Configurar a exportação contínua de logs da Vercel para o serviço gerenciado Axiom, garantindo retenção de logs operacionais e de cancelamento por 365 dias conforme exigido pela LGPD.

## 📋 Rastreabilidade & Especificações
- **Task TechLead:** TASK-15 | **Cobre Critérios:** AC-3 (Retenção de Auditoria).
- **ADRs Vinculadas:** ADR-011 (Log Drain Gerenciado Axiom).
- **Especificação:** `specs/planning/devops-spec.md`.

## 🛠️ Atividades de Desenvolvimento
- [ ] Criar dataset `cinedoom-production-logs` no Axiom.
- [ ] Configurar Vercel Log Drain apontando para o endpoint OpenTelemetry/Axiom com API Token seguro.
- [ ] Padronizar logs da aplicação com formato JSON estruturado contendo `timestamp`, `tenant_id`, `route`, `status_code` e `duration_ms`.
- [ ] Configurar política de retenção de 365 dias no painel do Axiom.

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] Eventos de venda, cancelamento e erros aparecem no console do Axiom em tempo real.
- [ ] Retenção legal configurada para 365 dias sem risco de expurgo no plano básico da Vercel.

## ⏱️ Estimativa & Caminho Crítico
- **Estimativa:** 3 horas | **Prioridade:** P2 | **Depende de:** TASK-1
"""
    },
    {
        "title": "[CHORE(CI)] CI/CD Pipeline - GitHub Actions com typecheck, ESLint no-cycle e preview Vercel",
        "labels": ["tipo:infra", "prioridade:P0"],
        "body": """## 🎯 Objetivo do Requisito
Configurar o pipeline automatizado de integração contínua (CI/CD) no GitHub Actions do repositório cinedoom-app, assegurando validação de tipos, linting e deploy automático de preview em cada Pull Request.

## 📋 Rastreabilidade & Especificações
- **Task TechLead:** TASK-16 | **Cobre Critérios:** Governança e Qualidade Contínua.
- **ADRs Vinculadas:** ADR-005 (GitHub Actions e Vercel).
- **Especificação:** `specs/planning/devops-spec.md`.

## 🛠️ Atividades de Desenvolvimento
- [ ] Criar workflow `.github/workflows/ci.yml` disparado em push e PRs para `main` e `develop`.
- [ ] Adicionar etapas: Checkout, Setup Node.js 20, Cache pnpm, Validação TypeScript (`pnpm tsc --noEmit`), Linter (`pnpm eslint`) e Execução de Testes Unitários (`pnpm test`).
- [ ] Configurar Vercel GitHub Integration para deploy automático de ambientes de Preview para cada PR.

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] Pipeline roda em menos de 2 minutos no GitHub Actions.
- [ ] PRs com erros de tipagem ou testes quebrados são impedidos de merge.

## ⏱️ Estimativa & Caminho Crítico
- **Estimativa:** 4 horas | **Prioridade:** P0 | **Depende de:** TASK-1
"""
    },
    {
        "title": "[TEST(SECURITY)] Suíte de testes automatizados de isolamento cross-tenant (500 cenários)",
        "labels": ["tipo:test", "prioridade:P0", "modulo:tenancy"],
        "body": """## 🎯 Objetivo do Requisito
Implementar uma bateria exaustiva de testes automatizados de segurança no Vitest, simulando 500 requisições entre tenants distintos para certificar matematicamente a ausência de vazamento de dados entre cinemas.

## 📋 Rastreabilidade & Especificações
- **Task TechLead:** TASK-18 | **Cobre Critérios:** AC-4 (Isolamento Multi-tenant).
- **Especificação:** `specs/quality/test-strategy.md` (Security Test Suite).

## 🛠️ Atividades de Desenvolvimento
- [ ] Criar cenários de teste automatizados para todos os endpoints REST (`filmes`, `salas`, `sessoes`, `vendas`, `ocupacao`).
- [ ] Testar requisições autenticadas com JWT do Tenant A tentando acessar IDs de recursos pertencentes ao Tenant B.
- [ ] Testar injeção de parâmetros cross-tenant via headers e query parameters.
- [ ] Validar que 100% das requisições ilegais resultam em status `403` ou `404` sem exibir dados confidenciais.

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] 500 cenários de teste automatizados passando com 100% de sucesso no Vitest.
- [ ] Zero dados vazados entre cinemas concorrentes.

## ⏱️ Estimativa & Caminho Crítico
- **Estimativa:** 4 horas | **Prioridade:** P0 | **Depende de:** TASK-3, TASK-10
"""
    },
    {
        "title": "[TEST(CONCURRENCY)] Suíte de carga concorrente com 50 threads simultâneas e 0 double-booking",
        "labels": ["tipo:test", "prioridade:P0", "modulo:bilheteria"],
        "body": """## 🎯 Objetivo do Requisito
Implementar o teste de estresse automatizado de concorrência disparando 50 requisições simultâneas contra o mesmo assento na mesma sessão, comprovando a tolerância zero a double-booking da arquitetura ACID.

## 📋 Rastreabilidade & Especificações
- **Task TechLead:** TASK-19 | **Cobre Critérios:** AC-1 (Trava ACID Anti-double-booking).
- **ADRs Vinculadas:** ADR-007 (SELECT FOR UPDATE).
- **Especificação:** `specs/quality/test-strategy.md` (Caso de Teste TC-3).

## 🛠️ Atividades de Desenvolvimento
- [ ] Construir script de teste de carga em TypeScript/Vitest utilizando `Promise.allSettled`.
- [ ] Disparar 50 requisições concorrentes no mesmo milissegundo tentando comprar o assento `A1` da mesma sessão.
- [ ] Coletar e validar as respostas HTTP de todas as 50 requisições.
- [ ] Executar query direta no banco conferindo: `SELECT COUNT(*) FROM tickets WHERE session_seat_id = ...`.

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] Exatamente 1 requisição retorna status `201 Created` com o ingresso emitido.
- [ ] Exatamente 49 requisições retornam status `409 Conflict`.
- [ ] O banco de dados registra apenas 1 ticket emitido e o assento permanece `SOLD`.
- [ ] Zero duplicação de vendas comprovada matematicamente.

## ⏱️ Estimativa & Caminho Crítico
- **Estimativa:** 6 horas | **Prioridade:** P0 (Prova de Fogo da Banca) | **Depende de:** TASK-10, TASK-11
"""
    },
    {
        "title": "[CHORE(ONBOARDING)] Seed com dados realistas, provisionamento de tenant e roteiro da demo",
        "labels": ["tipo:chore", "prioridade:P1"],
        "body": """## 🎯 Objetivo do Requisito
Desenvolver script de seed com dados realistas para inicialização do sistema, provisionar os tenants de demonstração e estruturar o roteiro passo a passo para a apresentação ao vivo perante a banca.

## 📋 Rastreabilidade & Especificações
- **Task TechLead:** TASK-20 | **Cobre Critérios:** Apresentação Final e Demonstração.
- **Data da Apresentação:** 12 de novembro de 2026.

## 🛠️ Atividades de Desenvolvimento
- [ ] Implementar script `prisma/seed.ts` populando 2 cinemas (Tenants), 4 filmes com pôsteres em alta resolução, 2 salas configuradas e sessões para o dia corrente.
- [ ] Criar usuários de teste padrão: `atendente@cinedoom.com` e `gerente@cinedoom.com`.
- [ ] Configurar uma sessão pré-lotada com 90% de ocupação (para demonstrar a venda do último assento e a lotação completa ao vivo perante a banca).
- [ ] Redigir roteiro cronometrado de 5 minutos para a demonstração da bilheteria e do painel de ocupação.

## ✅ Critérios de Aceite (Definition of Done - DoD)
- [ ] Comando `pnpm prisma db seed` executa em menos de 5 segundos populando ambiente limpo.
- [ ] Roteiro de demonstração ao vivo validado e ensaiado pela equipe.

## ⏱️ Estimativa & Caminho Crítico
- **Estimativa:** 2 horas | **Prioridade:** P1 | **Depende de:** TASK-4, TASK-13
"""
    }
]

print(f"Total de issues do App: {len(APP_ISSUES)}")

def main():
    print("=" * 60)
    print("CADASTRO AUTOMÁTICO DE ISSUES NO GITHUB (ORGANIZATION)")
    print("=" * 60)
    
    print("\n--- 1. Cadastrando 10 Issues em manual-processos-software ---")
    for item in DOCS_ISSUES:
        create_issue(REPOS["docs"], item["title"], item["body"], item["labels"])
        
    print("\n--- 2. Cadastrando 20 Issues em cinedoom-app ---")
    for item in APP_ISSUES:
        create_issue(REPOS["app"], item["title"], item["body"], item["labels"])
        
    print("\n" + "=" * 60)
    print("✅ TODAS AS 30 ISSUES FORAM CADASTRADAS COM SUCESSO!")
    print("=" * 60)

if __name__ == "__main__":
    main()
