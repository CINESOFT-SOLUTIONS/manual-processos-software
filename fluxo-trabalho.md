# 🚀 Fluxo de Trabalho e Colaboração

Este guia rápido explica como qualquer membro da equipe deve trabalhar no repositório para elaborar prompts, validar saídas de IA e consolidar as partes do **Manual de Processos de Software**.

---

## 🏛️ Os Três Pilares (Fontes da Verdade e Diretrizes)

Antes de escrever qualquer prompt, lembre-se:

1. **Instruções e Slides da Docente (Profa. Dra. Juliana Pereira de Souza Zinader):**  
   Consulte as diretrizes consolidadas em [`docs/instrucoes-disciplina.md`](docs/instrucoes-disciplina.md).  
   ⚠️ **OBRIGATÓRIO:** Antes de iniciar qualquer parte, vá também ao **Google Classroom** da disciplina. Baixe e analise com atenção os **slides da aula correspondente** e todas as orientações publicadas pela professora. As exigências de aula definem o que deve ser cobrado no prompt.
2. **Constituição do Projeto ([`docs/constituicao/project-definition-workbook.md`](docs/constituicao/project-definition-workbook.md)):**  
   Manda nas regras de negócio, tecnologias e escopo do CineDoom. A IA nunca pode inventar algo fora do PDW.
3. **Norma ISO/IEC/IEEE 12207:2021 ([`docs/norma-iso/`](docs/norma-iso/)):**  
   Manda na estrutura formal dos processos, nomenclaturas, cláusulas e entregáveis exigidos.

---

## 🔄 Fluxo de Trabalho (Passo a Passo)

Para cada capítulo do trabalho (**Capítulos 1 a 5**), siga este ciclo:

```text
[0. Classroom & Slides] ──> [1. Prompt] ──> [2. Execução + Validação] ──> [3. Rascunho] ──> [4. Imagens] ──> [5. Manual Oficial]
```

### Passo 0: Consultar o Google Classroom e a Estrutura Mínima
- Acesse o Google Classroom da disciplina ministrada pela **Profa. Dra. Juliana Pereira de Souza Zinader**.
- Consulte sempre o documento [`docs/estrutura-minima-manual.md`](docs/estrutura-minima-manual.md) para garantir a cobertura de todas as seções e subseções do capítulo correspondente.
- Examine os **slides apresentados em sala** para extrair critérios específicos (tabelas, notações, diagramas mínimos e priorizações).

### Passo 1: Elaborar ou Ajustar o Prompt
- Acesse a pasta correspondente: `prompts/parte-XX/` (mapeada para o Capítulo correspondente).
- Caso seja um prompt novo, copie a estrutura de [`prompts/template-prompt.md`](prompts/template-prompt.md).
- Incorpore no prompt:
  1. O contexto do CineDoom e link para o PDW.
  2. As cláusulas da ISO 12207 aplicáveis.
  3. **Todas as diretrizes da professora em `docs/estrutura-minima-manual.md` e nos slides da aula.**
  4. A instrução final de validação obrigatória.

### Passo 2: Executar com a IA e Rodar o Auditor de Qualidade
- Envie o prompt para o modelo de IA.
- Ao obter a resposta, peça a auditoria crítica e rigorosa baseada no [`prompts/auditor-de-qualidade.md`](prompts/auditor-de-qualidade.md).
- **Salve o laudo de auditoria gerado** em:
  `docs/validacoes/parte-XX/analise-validacao-parte-XX.md`

### Passo 3: Rascunhar e Ajustar o Texto
- Salve o texto preliminar proposto pela IA em:
  `docs/rascunhos/parte-XX/rascunho-parte-XX.md`
- O grupo revisa em conjunto com base no laudo de auditoria, elimina prolixidades ("encher linguiça"), resolve eventuais alucinações da IA e alinha com a realidade do CineDoom.

### Passo 4: Guardar Diagramas e Evidências Visuais
- Se o capítulo exige diagramas (BPMN, PlantUML, C4, classes UML ou fluxos de processo):
  - Salve os arquivos fonte (`.puml`, `.bpmn`) e as exportações (`.png`, `.svg`, `.pdf`) em:
    `assets/` (organizados por capítulo).

### Passo 5: Incorporar ao Documento Oficial
- Com o texto revisado e aprovado pelo grupo, transfira o conteúdo definitivo para o manual consolidado:
  [`manual-processos-software.md`](manual-processos-software.md)
- Atualize o histórico de versões na contracapa do manual.

---

## 🗺️ Onde Salvar Cada Coisa (Guia Rápido)

| O que você tem na mão? | Onde deve salvar? | Exemplo de Arquivo |
|---|---|---|
| **Instrução / Prompt para a IA** | `prompts/parte-XX/` | `prompt-processos-acordo.md` |
| **Laudo de Auditoria da IA** | `docs/validacoes/parte-XX/` | `analise-validacao-parte-01.md` |
| **Texto Preliminar em Revisão** | `docs/rascunhos/parte-XX/` | `rascunho-parte-01.md` |
| **Diagramas / Modelos Visuais** | `assets/` | `assets/c4-container.png` |
| **Texto Final Aprovado** | Raiz (`manual-processos-software.md`) | Integrado na seção oficial do Capítulo |

---

## ⚠️ Regras Inegociáveis

1. **Classroom e Estrutura Mínima Primeiro:** Nunca monte um prompt apenas "pelo que acha que é". Verifique sempre [`docs/estrutura-minima-manual.md`](docs/estrutura-minima-manual.md) e as orientações da **Profa. Dra. Juliana Zinader**.
2. **Qualidade > Quantidade (Critério Transversal):** Os artefatos não precisam ser extensos — precisam ser consistentes, justificados e aplicados ao CineDoom. Nada de "encher linguiça" ou marketing.
3. **Coerência Intermódulos:** Todos os módulos devem conversar entre si e respeitar o contexto fundacional do Capítulo 1 e o PDW.
4. **Nunca jogue texto direto no manual:** Sempre passe pelo ciclo *Classroom ➔ Prompt ➔ Auditoria ➔ Rascunho ➔ Manual*.
5. **Conflito de Informação:** Se a norma sugerir algo genérico e o PDW definir algo específico para o CineDoom, **prevalece o PDW**.
6. **Commit Limpo:** Faça commits objetivos citando o capítulo trabalhado (ex: `docs(cap-03): adiciona processos organizacionais habilitadores`).
