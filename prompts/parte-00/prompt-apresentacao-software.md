# Prompt — Parte 0: Apresentação do Software

## 1. Identificação
- **Código:** `PR-P00_Apresentacao_Software`
- **Parte do Trabalho:** Parte 0 – Apresentação do Software
- **Norma / Cláusula de Referência:** ISO/IEC/IEEE 12207:2021 — Insumo preliminar para Stakeholder Needs and Requirements Definition (6.4.2) e System Requirements Definition (6.4.3)
- **Documento-base:** `docs/guia-projeto/project-definition-workbook.md` (Seções 1 a 8)

---

## 2. Prompt Estruturado (Input)

```markdown
Atue como Analista de Negócios e Engenheiro de Requisitos de Software.

Estamos elaborando o Manual de Processos de Software para o sistema "CineDoom" (sistema de gestão de salas de cinema e emissão de ingressos).

[CONTEXTO E PREMISSAS]
- Consulte como fonte da verdade o Project Definition Workbook (docs/guia-projeto/project-definition-workbook.md).
- O CineDoom é voltado para exibidores de cinema comercial, com módulos de Filmes, Salas, Sessões, Ingressos, Clientes e Relatórios.

[TAREFA]
Elabore o texto da "Parte 0 – Apresentação do Software" para o Manual de Processos, contendo obrigatoriamente:
1. Identificação e Descrição (missão, proposta de valor e limites do sistema).
2. Público-Alvo e Contexto de Uso (perfis de operadores, gerentes e clientes).
3. Escopo e Funcionalidades (lista estruturada de requisitos funcionais principais).
4. Restrições e Premissas (restrições tecnológicas, regulatórias e operacionais).

[FORMATO DE SAÍDA]
Texto em Markdown técnico, pronto para compor o manual, com linguagem precisa, sem adjetivações vazias e alinhado às seções 1 a 8 do PDW.

[VALIDAÇÃO OBRIGATÓRIA]
Ao concluir o texto, utilize os critérios do validador em `prompts/validador-iso12207.md`.
Gere o relatório da análise e salve-o em `docs/validacoes/parte-00/analise-validacao-parte-00.md`:
1. Valide a conformidade com as diretrizes de insumo para requisitos da ISO/IEC/IEEE 12207:2021 (6.4.2 e 6.4.3).
2. Verifique se nenhuma premissa contradiz as seções 1 a 8 do PDW (`docs/guia-projeto/project-definition-workbook.md`).
3. Anexe no relatório a tabela de validação indicando a cobertura dos tópicos e ajustes.
```
