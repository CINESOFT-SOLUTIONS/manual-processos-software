# Catálogo de Architecture Decision Records (ADRs) — CineDoom

Este diretório contém o registro formal e versionado de todas as decisões arquiteturais tomadas para o **CineDoom MVP**, em conformidade com o processo de **Gerenciamento Técnico de Decisões** (ABNT NBR ISO/IEC/IEEE 12207:2021 — Cláusula 6.3.3).

Cada ADR é mantida como um documento Markdown individual versionado com metadados em **YAML frontmatter**, facilitando a rastreabilidade, auditoria de qualidade e governança Docs-as-Code.

---

## Índice Geral de ADRs

| Código | Título da Decisão | Status | Data | Racional Principal | Arquivo |
| :---: | :--- | :---: | :---: | :--- | :---: |
| **ADR-001** | Arquitetura Monólito Modular em Next.js 14 | Aprovada | 2026-10-22 | Necessidade de desenvolver uma aplicação robusta com prazo restrito de 3 semanas... | [`ADR-001-arquitetura-monolito-modular.md`](ADR-001-arquitetura-monolito-modular.md) |
| **ADR-002** | Interface Reativa com Tailwind CSS e React Server/Client Components | Aprovada | 2026-10-22 | O mapa de assentos da sala precisa ser interativo, de resposta imediata (<2s) e ... | [`ADR-002-interface-reativa-tailwind-components.md`](ADR-002-interface-reativa-tailwind-components.md) |
| **ADR-003** | Backend em TypeScript com Route Handlers | Aprovada | 2026-10-22 | Garantir tipagem estática e segurança de tipos entre o banco de dados, as valida... | [`ADR-003-backend-typescript-route-handlers.md`](ADR-003-backend-typescript-route-handlers.md) |
| **ADR-004** | Banco de Dados Relacional PostgreSQL com Prisma ORM | Aprovada | 2026-10-22 | Venda e reserva de ingressos de cinema exigem estrita consistência transacional ... | [`ADR-004-banco-postgresql-prisma-orm.md`](ADR-004-banco-postgresql-prisma-orm.md) |
| **ADR-005** | Hospedagem na Vercel com Neon Serverless e GitHub Actions | Aprovada | 2026-10-22 | Necessidade de ambiente de staging e produção com deploy contínuo automatizado e... | [`ADR-005-hospedagem-vercel-neon-github-actions.md`](ADR-005-hospedagem-vercel-neon-github-actions.md) |
| **ADR-006** | Comunicação via API RESTful e Polling de 2s no Mapa de Assentos | Aprovada | 2026-10-22 | Atualização contínua do mapa de assentos no balcão e no portal com múltiplos usu... | [`ADR-006-comunicacao-restful-polling-mapa.md`](ADR-006-comunicacao-restful-polling-mapa.md) |
| **ADR-007** | Pré-população de SessionSeat para Trava Pessimista SELECT FOR UPDATE | Aprovada | 2026-10-23 | Concorrência entre múltiplos atendentes e clientes tentando selecionar e comprar... | [`ADR-007-pre-populacao-sessionseat-select-for-update.md`](ADR-007-pre-populacao-sessionseat-select-for-update.md) |
| **ADR-008** | Criptografia de CPF: HMAC-SHA256 para Busca e AES-256-GCM para Armazenamento | Aprovada | 2026-10-23 | O CPF é dado pessoal sensível segundo a LGPD. O espaço finito de CPFs válidos (~... | [`ADR-008-criptografia-cpf-hmac-sha256-aes-256-gcm.md`](ADR-008-criptografia-cpf-hmac-sha256-aes-256-gcm.md) |
| **ADR-009** | Anonimização In-Place para LGPD Art. 18 sem Quebra de FK do CDC | Aprovada | 2026-10-23 | O titular tem direito ao esquecimento (Art. 18 da LGPD), mas o Código de Defesa ... | [`ADR-009-anonimizacao-in-place-lgpd-art-18.md`](ADR-009-anonimizacao-in-place-lgpd-art-18.md) |
| **ADR-010** | Auditoria de Cancelamentos Append-Only via Trigger PostgreSQL | Aprovada | 2026-10-23 | A auditoria de cancelamento de ingressos deve ser estritamente imutável para com... | [`ADR-010-auditoria-cancelamentos-append-only-trigger.md`](ADR-010-auditoria-cancelamentos-append-only-trigger.md) |
| **ADR-011** | Log Drain Gerenciado (Axiom) para Retenção de 365 Dias (LGPD) | Aprovada | 2026-10-23 | A retenção legal de logs de auditoria e segurança exigida pela LGPD é de no míni... | [`ADR-011-log-drain-gerenciado-axiom-retencao-365-dias.md`](ADR-011-log-drain-gerenciado-axiom-retencao-365-dias.md) |
| **ADR-012** | Portal do Cliente, Autenticação de Espectador, Expiração Just-in-Time e Notificação Transacional | Aprovada | 2026-10-23 | Necessidade de incorporar o Portal do Cliente para reserva pública de assentos c... | [`ADR-012-portal-cliente-reserva-expiracao-jit.md`](ADR-012-portal-cliente-reserva-expiracao-jit.md) |

---

## Estrutura Padrão de cada ADR

Cada registro de decisão arquitetural neste diretório segue o template formal:
- **YAML Frontmatter:** Identificador (`id`), título (`title`), status (`status`), data (`date`) e tomadores de decisão (`deciders`).
- **Contexto:** Cenário operacional, forças atuantes e problema técnico a ser resolvido.
- **Decisão:** Escolha tecnológica ou de design adotada, especificando bibliotecas, padrões e limites.
- **Consequências:** Trade-offs, impactos positivos, restrições e mitigações associadas.
