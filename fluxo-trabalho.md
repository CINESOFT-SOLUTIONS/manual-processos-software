# 🚀 Fluxo de Trabalho e Colaboração

Este guia rápido explica como qualquer membro da equipe deve trabalhar no repositório para elaborar prompts, validar saídas de IA e consolidar as partes do **Manual de Processos de Software**.

---

## 🏛️ Os Dois Pilares (Fontes da Verdade)

Antes de escrever qualquer prompt, lembre-se:
1. **Constituição do Projeto ([`docs/constituicao/project-definition-workbook.md`](docs/constituicao/project-definition-workbook.md)):** Manda nas regras de negócio, tecnologias e escopo do CineDoom. A IA nunca pode inventar algo fora do PDW.
2. **Norma ISO/IEC/IEEE 12207:2021 ([`docs/norma-iso/`](docs/norma-iso/)):** Manda na estrutura dos processos, nomenclaturas, cláusulas e entregáveis exigidos.

---

## 🔄 Fluxo de Trabalho (Passo a Passo)

Para cada parte do trabalho (`parte-00` a `parte-04`), siga este ciclo:

```text
[1. Prompt] ──> [2. Execução + Validação] ──> [3. Rascunho] ──> [4. Imagens] ──> [5. Manual Oficial]
```

### Passo 1: Elaborar ou Ajustar o Prompt
- Acesse a pasta correspondente: `prompts/parte-XX/`.
- Caso seja um prompt novo, copie a estrutura de [`prompts/template-prompt.md`](prompts/template-prompt.md).
- Certifique-se de que o prompt contenha o contexto do CineDoom, as cláusulas da norma e a instrução final de validação.

### Passo 2: Executar com a IA e Rodar o Validador
- Envie o prompt para o modelo de IA.
- Ao obter a resposta, peça a autoavaliação baseada no [`prompts/validador-iso12207.md`](prompts/validador-iso12207.md).
- **Salve o relatório de auditoria gerado** em:
  `docs/validacoes/parte-XX/analise-validacao-parte-XX.md`

### Passo 3: Rascunhar e Ajustar o Texto
- Salve o texto preliminar proposto pela IA em:
  `docs/rascunhos/parte-XX/rascunho-parte-XX.md`
- O grupo revisa, corta alucinações e ajusta a redação.

### Passo 4: Guardar Diagramas e Evidências Visuais
- Se a parte exigir diagramas (BPMN, PlantUML, classes UML ou telas):
  - Salve os arquivos fonte (`.puml`, `.bpmn`) e as exportações (`.png`, `.svg`, `.pdf`) em:
    `assets/parte-XX/`

### Passo 5: Incorporar ao Documento Oficial
- Com o texto revisado e aprovado pelo grupo, transfira o conteúdo definitivo para o manual consolidado:
  [`manual-processos-software.md`](manual-processos-software.md)
- Atualize o histórico de versões no topo do manual.

---

## 🗺️ Onde Salvar Cada Coisa (Guia Rápido)

| O que você tem na mão? | Onde deve salvar? | Exemplo de Arquivo |
|---|---|---|
| **Instrução / Prompt para a IA** | `prompts/parte-XX/` | `prompt-processos-acordo.md` |
| **Relatório de Conformidade da IA** | `docs/validacoes/parte-XX/` | `analise-validacao-parte-01.md` |
| **Texto Preliminar em Revisão** | `docs/rascunhos/parte-XX/` | `rascunho-parte-01.md` |
| **Diagramas / Modelos Visuais** | `assets/parte-XX/` | `fluxo-aquisicao.png` |
| **Texto Final Aprovado** | Raiz (`manual-processos-software.md`) | Integrado na seção oficial |

---

## ⚠️ Regras Inegociáveis

1. **Nunca jogue texto direto no manual:** Sempre passe pelo ciclo *Prompt ➔ Validação ➔ Rascunho ➔ Manual*.
2. **Conflito de Informação:** Se a norma sugerir algo genérico e o PDW definir algo específico para o CineDoom, **prevalece o PDW**.
3. **Commit Limpo:** Faça commits objetivos citando a parte trabalhada (ex: `docs(parte-02): adiciona rascunho dos processos habilitadores`).
