# Capítulo 4 – Processos de Gerenciamento Técnico

## 4.1 Plano de projeto: escopo, cronograma, recursos e entregas

O planejamento do projeto (ISO/IEC/IEEE 12207:2021 – Cláusula 6.3.1) organiza a execução e o cronograma do CineDoom:

### Escopo por Incremento e Releases

| Incremento | Escopo Funcional | Requisitos Vinculados | Status |
|---|---|---|---|
| **Inc. 1 (Fundação)** | Filmes, Salas e Assentos | RF-03, RF-04 | Concluído no planejamento |
| **Inc. 2 (Operação)** | Sessões e Mapa de Assentos | RF-05, RF-06 | Em andamento |
| **Inc. 3 (Transação)** | Venda atômica, Cancelamento e Auditoria | RF-07, RF-08, RF-12 | Prioridade MVP |
| **Inc. 4 (Clientes)** | Cadastro de Clientes e Interesses | RF-09, RF-10 | Backlog Release 1.1 |
| **Inc. 5 (Fechamento)** | Indicadores de Ocupação e Release Demo | RF-11 | Prioridade MVP |

### Cronograma de Execução (Foco na Entrega de 12/11/2026)
- **22/10 a 24/10:** Congelamento do escopo do MVP, modelagem do Prisma e configuração do CI no GitHub Actions.
- **25/10 a 31/10:** Implementação das rotas de filmes, salas, sessões e do mapa de assentos interativo.
- **01/11 a 04/11:** Implementação da trava transacional de venda, testes no Vitest e cancelamento.
- **05/11 a 08/11:** Integração total na Vercel com banco Neon, consolidação dos Capítulos 4 e 5 do Manual.
- **09/11 a 11/11:** Ensaios da apresentação oral com slides Beamer e congelamento da release `v1.0.0-mvp`.
- **12/11/2026:** Apresentação final perante a banca avaliadora.

## 4.2 Plano de gestão de riscos: identificação, probabilidade, impacto e respostas

A gestão de riscos (Cláusula 6.3.4) monitora incertezas que possam comprometer o cronograma ou a qualidade do sistema:

| ID | Risco Identificado | Categoria | Prob. | Impacto | Estratégia de Mitigação | Responsável |
|---|---|---|:---:|:---:|---|---|
| **R-01** | Indisponibilidade de banco na nuvem | Técnico | Baixa | Alto | Uso de provedor com SLA comprovado (Neon) e script local de fallback com SQLite | DevOps |
| **R-02** | Conflito de venda concorrente de assentos | Técnico | Média | Alto | Restrição única `@@unique([sessionId, seatId])` no banco e transações atômicas | Arquiteto |
| **R-03** | Estouro de prazo para a apresentação | Organizacional | Média | Alto | Corte formal de escopo (foco estrito no MVP de bilheteria e ocupação) | Gerente de Projeto |
| **R-04** | Falha de rede durante a demonstração | Operacional | Média | Alto | Gravação prévia de vídeo de contingência com o fluxo ponta a ponta | Analista de QA |
| **R-05** | Inconsistência entre código e manual | Metodológico | Média | Médio | Matriz de rastreabilidade contínua ligando RFs a commits e testes | Analista de Requisitos |

## 4.3 Plano de gestão de configuração: controle de versões, branches e releases

A gestão de configuração (Cláusula 6.3.5) assegura o controle formal dos artefatos:

### Itens de Configuração (CIs)
São itens de configuração controlados: código-fonte da aplicação, arquivos de migração do banco de dados, arquivos de teste, documentação Markdown do manual, código-fonte LaTeX dos relatórios e slides, e diagramas visuais.

### Estratégia de Branches
- `main`: Código estável em produção, espelhado automaticamente na Vercel.
- `develop`: Branch de integração de novas funcionalidades concluídas.
- `feat/RF-XX-...`: Branches de trabalho individuais criadas a partir de `develop`.

### Releases e Tags
Toda release demonstrável recebe tag semântica: `v1.0.0-mvp`. O changelog é gerado no GitHub mapeando cada requisito atendido aos seus respectivos Pull Requests.

## 4.4 Registro de decisões técnicas relevantes (ADRs)

A gestão de decisões (Cláusula 6.3.3) registra escolhas técnicas e suas justificativas:

| Código | Decisão Técnica | Justificativa | Status |
|---|---|---|---|
| **ADR-001** | Arquitetura Monólito Modular em Next.js 14 | Reduz sobrecarga operacional em comparação a microsserviços | Aprovada |
| **ADR-002** | Interface Reativa com Tailwind CSS e React Components | Facilidade no desenvolvimento de mapas interativos e reativos | Aprovada |
| **ADR-003** | Backend em TypeScript com Route Handlers | Unificação de linguagem entre cliente e servidor com tipagem estática | Aprovada |
| **ADR-004** | Banco Relacional PostgreSQL com Prisma ORM | Garantia de propriedades ACID fundamentais para venda e reserva | Aprovada |
| **ADR-005** | Hospedagem na Vercel com Neon Serverless | Zero custo operacional inicial e deploy automático via GitHub Actions | Aprovada |
| **ADR-006** | API RESTful e Polling de 2s no Mapa | Simplicidade de atualização serverless sem conexões WebSocket ociosas | Aprovada |
| **ADR-007** | Pré-população de SessionSeat para Trava SELECT FOR UPDATE | Elimina race conditions e garante anti-double-booking determinístico | Aprovada |
| **ADR-008** | Criptografia de CPF (HMAC-SHA256 + AES-256-GCM) | Proteção contra rainbow tables no espaço finito de CPFs (LGPD) | Aprovada |
| **ADR-009** | Anonimização In-Place para LGPD Art. 18 | Atende direito ao esquecimento sem quebra de integridade fiscal do CDC | Aprovada |
| **ADR-010** | Auditoria Append-Only via Trigger PostgreSQL | Imutabilidade em nível de banco de dados sem custos de S3 WORM | Aprovada |
| **ADR-011** | Log Drain Gerenciado (Axiom) para Retenção de 365 Dias | Cumpre prazo legal da LGPD fora do limite de 1h da Vercel | Aprovada |
| **ADR-012** | Portal do Cliente com Expiração Just-in-Time | Reserva online sem gateway financeiro e baixa presencial no balcão | Aprovada |

## 4.5 Métricas de acompanhamento do projeto

A medição e controle (Cláusula 6.3.2) subsidiam o acompanhamento do avanço do projeto:
- **Velocidade de Entrega:** Percentual de requisitos funcionais com status *Done*.
- **Cobertura de Testes de Regra Crítica:** 100% de cobertura nos métodos do serviço de venda e cancelamento de ingressos.
- **Densidade de Defeitos:** Número de bugs abertos versus resolvidos no GitHub Issues antes da release.

---
