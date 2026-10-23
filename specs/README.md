# Especificações Técnicas e Governança (specs)

Este diretório reúne as especificações formais de engenharia, governança técnica e decisões arquiteturais da plataforma **CineDoom**.

Os artefatos aqui consolidados foram produzidos pela esteira de agentes canônicos de ciclo de vida de software, revisados através dos Gates HITL (*Human-in-the-Loop*) e validados para guiar tanto os **Capítulos 4 e 5 do Manual de Processos** quanto o desenvolvimento no repositório `cinedoom-app`.

---

## Estrutura de Especificações

### 1. Decisões Arquiteturais (ADRs)
* **[`adrs/README.md`](adrs/README.md):** Catálogo formal de 11 decisões técnicas registradas (ISO 12207 – Cláusula 6.3.3):
  * Monólito modular em Next.js 14, Tailwind CSS, PostgreSQL Neon com Prisma ORM.
  * Pré-população de `SessionSeat` para trava pessimista `SELECT FOR UPDATE` (anti-double booking).
  * Criptografia em duas camadas para CPF: HMAC-SHA256 (busca) e AES-256-GCM (armazenamento).
  * Soft-anonymization *in-place* para LGPD Art. 18 sem quebra de integridade referencial com o CDC.
  * Trigger append-only no PostgreSQL para auditoria imutável de cancelamentos.
  * Log Drain Vercel com Axiom para retenção legal de 365 dias.

### 2. Arquitetura e Design de Interface
* **[`architecture/solution-architecture.md`](architecture/solution-architecture.md):** Arquitetura macro, diagramas C4 (Contexto e Contêineres) e padrões de integração.
* **[`architecture/software-architecture.md`](architecture/software-architecture.md):** Arquitetura de software, Route Handlers, serviços de domínio e camadas lógicas.
* **[`architecture/ux-design.md`](architecture/ux-design.md):** Jornadas do usuário (Atendente de bilheteria e Gerente operacional) e fluxos de navegação.
* **[`architecture/ui-mockups.md`](architecture/ui-mockups.md):** Especificação de componentes, estados cromáticos do mapa de assentos e layout do balcão.

### 3. Modelo de Dados e Persistência
* **[`data-model/data-model.md`](data-model/data-model.md):** Schema relacional Prisma, 9 entidades de domínio (`Movie`, `Room`, `Seat`, `Session`, `SessionSeat`, `Ticket`, `Buyer`, `CancellationAudit`, `User`), índices e chaves estrangeiras.

### 4. Segurança e Privacidade (LGPD)
* **[`security-compliance/threat-model.md`](security-compliance/threat-model.md):** Modelagem de Ameaças baseada na metodologia STRIDE, superfícies de ataque e controles de mitigação.
* **[`security-compliance/compliance-assessment.md`](security-compliance/compliance-assessment.md):** Relatório de Impacto à Proteção de Dados Pessoais (DPIA - Art. 38 LGPD), política de DPO (Art. 41) e direitos dos titulares (Art. 18).

### 5. Qualidade e Estratégia de Testes
* **[`quality/test-strategy.md`](quality/test-strategy.md):** Pirâmide de testes, matriz de rastreabilidade bidirecional cobrindo os critérios de aceite (AC-1 a AC-8) e especificação do teste de carga concorrente (50 threads simultâneas com zero double-booking).

### 6. Planejamento Operacional e DevOps
* **[`planning/sprints-e-backlog.md`](planning/sprints-e-backlog.md):** Plano Mestre de Sprints, Backlog e Roadmap oficial do Kanban CineDoom com 30 issues distribuidas, datas de inicio/termino e matriz da equipe.
* **[`planning/tech-lead-plan.md`](planning/tech-lead-plan.md):** Detalhamento de 20 tarefas técnicas de desenvolvimento (`TASK-1` a `TASK-20`), caminho crítico e estimativa total de 102 horas.
* **[`planning/devops-spec.md`](planning/devops-spec.md):** Configuração de CI/CD (GitHub Actions), provisionamento na Vercel, banco Neon e observabilidade via Axiom.

### 7. Requisitos de Produto
* **[`cinedoom-spec.md`](cinedoom-spec.md):** Especificação funcional formal com Histórias de Usuário (`US-1` a `US-6`) e Critérios de Aceite (`AC-1` a `AC-8`).
* **[`cinedoom-spec.json`](cinedoom-spec.json):** Metadados estruturados consumíveis por automações e ferramentas de análise.
