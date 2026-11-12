# Especificações Técnicas e Governança (specs)

Este diretório reúne as especificações formais de engenharia, governança técnica e decisões arquiteturais da plataforma **CineDoom**.

Os artefatos aqui consolidados foram produzidos pela esteira de engenharia de software da **CineSoft Solutions**, revisados e validados para guiar tanto os **Capítulos 4 e 5 do Manual de Processos** quanto o desenvolvimento no repositório `cinedoom-app`.

---

## Estrutura de Especificações

### 1. Decisões Arquiteturais (ADRs)
* **[`adrs/README.md`](adrs/README.md):** Catálogo formal de 12 decisões técnicas registradas (ISO 12207 – Cláusula 6.3.3) em arquivos Markdown individuais com metadados YAML:
  * Monólito modular em Next.js 14, Tailwind CSS, PostgreSQL 16 no Supabase com Prisma ORM.
  * Pré-população de `SessionSeat` para trava pessimista `SELECT FOR UPDATE` (anti-double booking).
  * Criptografia em duas camadas para CPF: HMAC-SHA256 (busca) e AES-256-GCM (armazenamento).
  * Soft-anonymization *in-place* para LGPD Art. 18 sem quebra de integridade referencial com o CDC.
  * Trigger append-only no PostgreSQL para auditoria imutável de cancelamentos.
  * Log Drain Vercel com Axiom para retenção legal de 365 dias.
  * Portal do Cliente com reserva de assentos, expiração Just-in-Time, notificação transacional e cancelamento web.

### 2. Arquitetura e Design de Interface
* **[`architecture/solution-architecture.md`](architecture/solution-architecture.md):** Arquitetura macro, diagramas C4 (Contexto e Contêineres) e padrões de integração para os três módulos (Gerente, Atendente e Cliente).
* **[`architecture/software-architecture.md`](architecture/software-architecture.md):** Arquitetura de software, Route Handlers, serviços de domínio e camadas lógicas.
* **[`architecture/ux-design.md`](architecture/ux-design.md):** Jornadas do usuário (Atendente de bilheteria, Gerente operacional e Espectador final) e fluxos de navegação em diagramas Mermaid.
* **[`architecture/ui-mockups.md`](architecture/ui-mockups.md):** Especificação de componentes, estados cromáticos do mapa de assentos (incluindo status reservado) e layouts de tela.

### 3. Modelo de Dados e Persistência
* **[`data-model/data-model.md`](data-model/data-model.md):** Schema relacional Prisma com 11 entidades de domínio (`Tenant`, `User`, `Film`, `Room`, `Seat`, `Session`, `SessionSeat`, `Buyer`, `Reservation`, `Ticket`, `CancellationAudit`), índices, constraints e chaves estrangeiras.

### 4. Segurança e Privacidade (LGPD)
* **[`security-compliance/threat-model.md`](security-compliance/threat-model.md):** Modelagem de Ameaças baseada na metodologia STRIDE cobrindo bilheteria e portal público (T-1 a T-17), superfícies de ataque e controles de mitigação.
* **[`security-compliance/compliance-assessment.md`](security-compliance/compliance-assessment.md):** Relatório de Impacto à Proteção de Dados Pessoais (DPIA - Art. 38 LGPD), política de DPO (Art. 41), bases legais (Art. 7º) e direitos dos titulares (Art. 18).

### 5. Qualidade e Estratégia de Testes
* **[`quality/test-strategy.md`](quality/test-strategy.md):** Pirâmide de testes, matriz de cobertura dos Critérios de Aceite (`CA-01` a `CA-14`), catálogo dos 26 Casos de Teste (`CT-01` a `CT-26`) no formato *Dado que / Quando / Então* e especificação dos testes de concorrência ACID.

### 6. Planejamento Operacional e DevOps
* **[`planning/sprints-e-backlog.md`](planning/sprints-e-backlog.md):** Plano Mestre de Sprints, Backlog e Roadmap oficial do Kanban CineDoom com 33 issues distribuídas (23 em `cinedoom-app` e 10 em `manual-processos-software`), datas de início/término e matriz RACI.
* **[`planning/tech-lead-plan.md`](planning/tech-lead-plan.md):** Detalhamento de 23 tarefas técnicas de desenvolvimento (`TASK-1` a `TASK-23`), caminho crítico e estimativa total de 116 horas.
* **[`planning/devops-spec.md`](planning/devops-spec.md):** Configuração de CI/CD (GitHub Actions), provisionamento na Vercel, banco Supabase PostgreSQL e observabilidade via Axiom.

### 7. Engenharia de Requisitos, Regras de Negócio e Rastreabilidade
* **[`cinedoom-spec.md`](cinedoom-spec.md):** Especificação formal completa (SRS) padronizada em português conforme a Seção 6.4 da ISO/IEC/IEEE 12207:2021, separada em:
  * **Stakeholders (`STK-01` a `STK-05`)** e **Necessidades Elicitadas (`NEC-01` a `NEC-08`)**;
  * **Histórias de Usuário (`HU-01` a `HU-11`)**;
  * **Requisitos Funcionais (`RF-01` a `RF-18`)** e **Requisitos Não Funcionais (`RNF-01` a `RNF-06`)**;
  * **Regras de Negócio (`RN-01` a `RN-12`)**;
  * **Critérios de Aceite (`CA-01` a `CA-14`)** e **Restrições (`RES-01` a `RES-06`)**;
  * **Matriz de Rastreabilidade Ponta a Ponta**.
