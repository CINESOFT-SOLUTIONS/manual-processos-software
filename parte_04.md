# Parte 04 - Processos Técnicos

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