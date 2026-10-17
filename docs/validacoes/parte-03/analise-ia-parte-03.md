# Relatório de Validação de IA — Parte 3 (Processos de Gerenciamento Técnico)

> **Origem:** Análise da sugestão de IA versus a norma ISO/IEC/IEEE 12207:2021 (Cláusula 6.3).
> **Status:** Aplicado nas correções da Parte 3 do manual.

---

## 1. O que foi validado

A sugestão de IA para a Parte 3 previa os elementos Escopo, Cronograma, Recursos e Entregas (todos da atividade de planejamento) e o seguinte índice:
- 3.1 Planejamento do Projeto
- 3.2 Gestão de Riscos
- 3.3 Gestão de Configuração
- 3.4 Gestão de Decisões Técnicas (ADRs)
- 3.5 Medição e Avaliação/Controle do Projeto

---

## 2. Conformidade com a ISO/IEC/IEEE 12207 – 6.3

A ISO/IEC/IEEE 12207 define, no grupo 6.3 (*Technical management processes*), sete processos:

| Processo da norma | Cláusula | Na sugestão de IA | Avaliação Crítica |
|---|---|---|---|
| Project planning | 6.3.1 | 3.1 (parcialmente) | Cobertura parcial |
| Project assessment and control | 6.3.2 | fundido em 3.5 | Incorreto (deve ser separado) |
| Decision management | 6.3.3 | 3.4 (ADRs) | Válido, mas requer decisões além de ADR |
| Risk management | 6.3.4 | 3.2 | Válido |
| Configuration management | 6.3.5 | 3.3 | Válido |
| Information management | 6.3.6 | **ausente** | **Grave: processo omitido** |
| Measurement | 6.3.7 | fundido em 3.5 | Incorreto (deve ser separado) |

---

## 3. Constatações e Correções Aplicadas

1. **Lacuna — Information management (6.3.6) ausente:** O processo é obrigatório no grupo 6.3. Foi criada a seção 3.6 no manual.
2. **Separação de Medição e Controle:** A medição fornece métricas; a avaliação/controle decide intervenções. Foram desacoplados em 3.2 e 3.7.
3. **Escopo de Decisões Técnicas:** Decisões de produto/escopo envolvem GP e cliente, enquanto decisões arquiteturais usam ADRs técnicos.
4. **Alinhamento Numérico com a Norma:** Reordenamento 1:1 com as cláusulas 6.3.1 a 6.3.7 para facilitar auditoria acadêmica.
