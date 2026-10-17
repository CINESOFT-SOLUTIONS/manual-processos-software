# Prompt & Diretrizes — Parte 4: Processos Técnicos

## 1. Identificação
- **Código:** `PR-P04_Processos_Tecnicos`
- **Parte do Trabalho:** Parte 4 – Processos Técnicos (Technical Processes)
- **Norma / Cláusula de Referência:** ISO/IEC/IEEE 12207:2021 — Cláusula 6.4 (Business Analysis, Stakeholder Requirements, System Requirements, Architecture Definition, Design Definition, System Analysis)
- **Documento-base:** `docs/constituicao/project-definition-workbook.md` e diretrizes de aula

---

## 2. Diretrizes Teóricas e Instruções de Elaboração (Input)

## Processos de Análise do Negócio

### Atividades Principais

* Preparação da análise do negócio
* Definição do problema/oportunidade
* Caracterização da solução
* Avaliação de alternativas de solução
* Gestão do conceito de operação

### Saídas do Processo

* **Declaração do problema/oportunidade:**
* Descrição formal do problema ou oportunidade identificada no negócio.

* **Conceito de operação (ConOps):**
* Documento que descreve como o sistema será operado pelos usuários e stakeholders.

* **Requisitos de negócio:**
* Conjunto de necessidades e restrições derivadas da análise do negócio.

* **Avaliação de viabilidade:**
* Análise da viabilidade técnica, econômica e operacional da solução proposta.

* **Rastreabilidade para stakeholders:**
* Mapeamento dos requisitos às necessidades e expectativas dos stakeholders.

---

## Processo de Definição de Necessidades e Requisitos dos Stakeholders

### Atividades Principais

* Preparação do processo
* Identificação dos stakeholders
* Elicitação das necessidades
* Definição dos requisitos dos stakeholders
* Análise e validação dos requisitos
* Gestão dos requisitos dos stakeholders



### Saídas do Processo

* **Registro dos stakeholders:**
* Lista identificada e classificada de todos os stakeholders envolvidos.

* **Necessidades dos stakeholders:**
* Declaração das necessidades, expectativas e restrições capturadas.

* **Requisitos dos stakeholders:**
* Conjunto formal de requisitos derivados das necessidades identificadas.

* **Critérios de aceitação:**
* Condições mensuráveis que o sistema deve satisfazer para ser aceito.

* **Rastreabilidade:**
* Mapeamento entre necessidades, requisitos e stakeholders de origem.


> **Nota:** O Método MoSCoW é uma técnica de priorização usada em gestão de projetos, desenvolvimento de produtos e análise de negócios para definir o que é mais urgente ou necessário.
> 
> 
---

## Processo de Definição de Requisitos de Sistemas/Software

### Atividades Principais

* **Elicitação:**
* Identificação e captura das necessidades dos stakeholders através de entrevistas, workshops, análise de documentos, observação/etnografia, prototipação, brainstorming e casos de uso.

* **Análise:**
* Refinamento, priorização (ex.: MoSCoW) e resolução de conflitos/ambiguidades entre requisitos, com verificação de viabilidade técnica e de custo, além da classificação (funcionais, não funcionais, de interface, de restrição).

* **Especificação:**
* Documentação clara, completa, não ambígua e rastreável dos requisitos mensuráveis no formato SRS (*Software Requirements Specification*) ou equivalente.

* **Validação:**
* Confirmação de que os requisitos especificados refletem as necessidades reais através de revisões formais, prototipagem, checklists, revisão por pares e simulações, garantindo critérios SMART (Específico, Mensurável, Atingível, Relevante e Testável).

### Saídas do Processo

* **Necessidade do stakeholder:**
* Identificação e documentação formal da origem da necessidade.

* **Requisito do sistema:**
* Requisito detalhado e especificado no documento SRS com identificador (ID) único.

* **Componente de design:**
* Mapeamento da arquitetura e dos módulos de software que implementam o requisito.

* **Código-fonte:**
* Implementação técnica diretamente rastreável ao requisito correspondente.

* **Caso de teste:**
* Conjunto de testes configurados para a verificação e validação do requisito.

---
# Processo de Definição de Arquitetura

### Propósito

* Definir a estrutura de alto nível do sistema
* Identificar os componentes e suas responsabilidades
* Estabelecer interfaces entre os elementos arquiteturais
* Garantir que os requisitos sejam alocados à arquitetura
* Avaliar alternativas arquiteturais



### Atividades Principais

* Preparação do processo de arquitetura
* Definição dos elementos arquiteturais
* Alocação de requisitos aos elementos
* Definição de interfaces entre elementos
* Avaliação de alternativas de arquitetura
* Gestão da arquitetura do sistema



### Saídas do Processo

* **Documento de Arquitetura:**
* Descrição formal da estrutura, componentes e interfaces do sistema.

* **Alocação de Requisitos:**
* Mapeamento de cada requisito ao(s) elemento(s) arquitetural(is) responsável(is).

* **Especificação de Interfaces:**
* Definição formal das interfaces entre os componentes do sistema.

* **Avaliação Arquitetural:**
* Registro das alternativas consideradas e justificativa das decisões tomadas.

* **Rastreabilidade:**
* Vínculo entre requisitos dos stakeholders e elementos da arquitetura.

---

# Processo de Definição de Design

### Propósito

* Detalhar os elementos arquiteturais em componentes implementáveis
* Especificar algoritmos, estruturas de dados e lógica interna
* Definir interfaces detalhadas entre componentes
* Garantir que o design satisfaz todos os requisitos alocados
* Fornecer base suficiente para a implementação

### Atividades Principais

* Preparação do processo de design
* Transformação da arquitetura em design detalhado
* Especificação de interfaces de componentes
* Especificação de estruturas de dados e algoritmos
* Avaliação do design
* Gestão do design do software

### Saídas do Processo

* **Documento de Design Detalhado:**
* Especificação completa dos componentes, algoritmos e estruturas de dados.

* **Especificação de Interfaces:**
* Definição precisa das interfaces internas e externas dos componentes.

* **Modelo de Dados:**
* Estruturas de dados, entidades, relacionamentos e restrições do sistema.

* **Avaliação do Design:**
* Registro das decisões de design e justificativas técnicas adotadas.

* **Rastreabilidade:**
* Vínculo entre elementos de design e requisitos/elementos arquiteturais.


---

# Processo de Análise de Sistema

### Propósito

* Analisar o problema ou oportunidade no contexto do sistema
* Definir o conceito de solução do sistema
* Identificar restrições técnicas, operacionais e de negócio
* Avaliar alternativas de solução do sistema
* Estabelecer a viabilidade da solução proposta

### Atividades Principais

* Preparação do processo de análise
* Análise do problema/oportunidade no contexto do sistema
* Definição do conceito de solução
* Identificação de restrições e premissas
* Avaliação de alternativas de solução
* Gestão da análise do sistema

### Saídas do Processo

* **Conceito de Solução do Sistema:**
* Descrição da solução proposta e como ela atende às necessidades identificadas.

* **Restrições e Premissas:**
* Limitações técnicas, operacionais, regulatórias e de negócio consideradas.

* **Alternativas Avaliadas:**
* Registro das opções consideradas e critérios utilizados na seleção.

* **Avaliação de Viabilidade:**
* Análise técnica, económica e operacional da solução escolhida.

* **Rastreabilidade:**
* Vínculo entre o conceito de solução e as necessidades dos stakeholders.


> **Sugestão:** Fazer um diagrama de componentes ou somente escrever os componentes da arquitetura. Dar justificativas para as decisões tomadas.


# O que precisa constar na parte 4

# Parte 4 - Processos técnicos 
## 4.1 - Requisitos
- Identficar problemas ou oportunidades de negócio
- Validação requisitos: Validar se o que foi documentado foi o que realmente o que o steakholder realmente quer.

### 4.1.1 - Documento de requisitos do sistema
definir os requisitos funcionais, não funcionais, restrições

### 4.1.2 - Rastreabilidade de requisitos
Rastreabilidade para stakeholders: Mapear os requistios às necessidades e expectatvas dos stakeholders
dica: Tabela com steakholder e requisitos

### 4.1.3 - Critérios de aceitação
Cada requisito tem um critério de aceitação relacionado

### 4.1.4 - Registro de stakeholders e necessidades elicitadas
Simular todos os steakholders e as necessidades que eles solicitam
- Técnica MoSCoW
- Registro de stakeholders: Ex: cliente, paciente, secretária
- Necessidade de cada steakholder
- Critérios de aceitação para as necessidades

## 4.2 - Arquitetura e Design
### 4.2.1 - Documento de arquitetura do sistema & Decisões arquiteturais (ADRs)
#### Visão geral

Descrição formal da estrutura, componentes e interfaces do sistema
Escrever uma visão geral da arquitetura do sistema
Podem ser feito por esccrito: componentes tal tal tal
Pode ser feito um diagrama de componetes (opcional, porém melhor)

#### Componentes

Especificação completa dos componentes, algoritmos e estruturas de dados

#### Interfaces

Definição formal das interfaces entre os componentes do sistema
O que são interfaces: Um meio de comunicação entre dois componentes. Conceito de interface padronização de saídas e entradas entre os componentes(classes).

#### Decisões arquiteturais (ADRs)

Registro das alternativas consideradas e justificativa das decisões tomadas
Justificatvas dos componentes

### 4.2.2 - Diagramas de design (UML, C4, etc.)

Detalhar os elementos arquiteturais em componentes implementáveis
Especificar algoritmos, estruturas de dados e lógica interna
Pelo menos um diagrama de classe do projeto

### 4.2.3 - Justificativa das escolhas tecnológicas

Registro das decisões de design e justificativas técnicas adotadas
Escolheu uma tecnologia x, ex login: para fazer o login precisa de logar com uma conta GOV por exemplo, então é necessário a integração com o GOV, e seria assim justificado
Atenção: Os artefatos não precisam ser extensos — precisam ser consistentes, justificados e aplicados ao seu projeto real. Qualidade > quantidade.

---

## 3. Validação Obrigatória

Ao gerar qualquer entrega ou seção da Parte 4, execute uma autoavaliação rigorosa utilizando o auditor em `prompts/auditor-de-qualidade.md`.
Gere o laudo de auditoria e salve-o em `docs/validacoes/parte-04/analise-validacao-parte-04.md`:
1. Valide a conformidade com as cláusulas de Processos Técnicos (6.4) da ISO/IEC/IEEE 12207:2021 (6.4.1 a 6.4.5).
2. Garanta que a rastreabilidade (Stakeholder -> Requisito -> Arquitetura -> Design) esteja documentada e consistente com o PDW (`docs/constituicao/project-definition-workbook.md`).
3. Avalie os critérios transversais (qualidade > quantidade, linguagem técnica e coerência intermódulos).
4. Anexe no relatório a tabela comparativa de conformidade do processo (Processo, Cláusula, Cobertura e Ajustes).
