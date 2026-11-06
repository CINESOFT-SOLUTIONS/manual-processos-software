# Catálogo de Architecture Decision Records (ADRs) — CineDoom

Este diretório contém o registro formal e versionado de todas as decisões arquiteturais tomadas para o sistema **CineDoom**, em conformidade com o processo de **Gerenciamento Técnico de Decisões** (ABNT NBR ISO/IEC/IEEE 12207:2021 — Cláusula 6.3.3).

Cada ADR é mantida como um documento Markdown individual versionado com metadados em **YAML frontmatter**, garantindo rastreabilidade, auditoria de qualidade e governança Docs-as-Code.

---

## Estrutura Padrão de cada ADR

Cada registro de decisão arquitetural neste diretório segue o template formal:
- **YAML Frontmatter:** Identificador (`id`), título (`title`), status (`status`), data (`date`) e tomadores de decisão (`deciders`).
- **Contexto:** Cenário operacional, forças atuantes e problema técnico a ser resolvido.
- **Decisão:** Escolha tecnológica ou de design adotada, especificando bibliotecas, padrões e limites.
- **Consequências:** Trade-offs, impactos positivos, restrições e mitigações associadas.
