# ABNT NBR ISO/IEC/IEEE 12207:2021

> **VERSÃO PARCIAL DE PRÉ-VISUALIZAÇÃO** — este arquivo foi gerado por OCR a partir de um PDF de pré-visualização parcial.

NORMA ABNT NBR

BRASILEIRA ISO/IEC/IEEE

12207

Primeira edição

24.08.2021

Engenharia de sistemas e software - Processos

de ciclo de vida de software

Systems and software engineering - Software life cycle processes

ICS 35.080 ISBN 978-85-07-08635-2

ASSOCIAÇAO Número de referência

BRASILEIRA ABNT NBR SO/EC/EEE 12207:2021

DE NORMAS TÉCNICAS 190 páginas

ABNT

Todos os direitos reservados. A menos que especificado de outro modo, nenhuma parte desta publicação pode ser

reproduzida ou utilizada por qualquer meio, eletrônico ou mecânico, incluindo fotocópia e microfilme, sem permissão por

escrito da ABNT, único representante da ISO no território brasileiro.

Todos os direitos reservados. A menos que especificado de outro modo, nenhuma parte desta publicação pode ser

reproduzida ou utilizada por qualquer meio, eletrônico ou mecânico, incluindo fotocópia e microfilme, sem permissão por

escrito da ABNT.

ABNT

Av. Treze de Maio, 13 - 28° andar

20031-901 - Rio de Janeiro - RJ

Tel.: + 55 21 3974-2300

Fax: + 55 21 3974-2346

abnt@abnt.org.br

www.abnt.org.br


**Sumário**

| Entrada | Página |
|---|---|
| Prefácio Nacional | vii |
| Introdução | viii |
| 1 Escopo | 1 |
| 1.3 Campo de aplicação |  |
| Limitações.. 1.4 |  |
| AWN Referências normativas |  |
| Termos, definições, e termos abreviados | 3 |
| Conformidade | 14 |
| 4.1 Uso pretendido | 14 |
| Conformidade total .. 4.2 | 15 |
| Conformidade total com resultados.. 4.2.1 | 15 |
| Conformidade total com tarefas 4.2.2 | 15 |
| 4.3 Conformidade personalizada | 16 |
| 5 Conceitos-chaves e aplicação | 16 |
| Introdução.. 5.1 | 16 |
| Conceitos de sistema de software.. 5.2 | 16 |
| Sistemas de software.. 5.2.1 | 16 |
| Estrutura de sistema de software... 5.2.2 | 17 |
| Sistemas habilitadores 5.2.3 | 18 |
| Processos do ciclo de vida para o sistema de software. 5.2.4 | 20 |
| 5.3 Conceitos de organização e projeto | 20 |
| 5.3.1 Organizações | 20 |
| 5.3.2 Adoção em nível de projeto e organização | 21 |
| Conceitos do ciclo de vida. 5.4 | 21 |
| Fases do ciclo de vida de software. 5.4.1 | 21 |
| 5.4.2 Modelo de ciclo de vida para sistema de software | 22 |
| Conceitos do processo 5.5 | 23 |
| 5.5.1 Critérios para processos | 23 |
| 5.5.2 Descrição de processos | 23 |
| 5.5.3 Características gerais de processos | 24 |
| Adaptação.. 5.5.4 | 24 |
| Grupos de processo 5.6 | 24 |
| Introdução.. 5.6.1 | 24 |
| Processos de Acordo 5.6.2 | 26 |
| 5.6.3 Processos Organizacionais Habilitadores de Projeto | 26 |
| 5.6.4 Processos de Gerenciamento Técnico | 26 |
| 5.6.5 Processos Técnicos | 27 |
| Aplicação do processo 5.7 | 27 |
| Modelo de referência de processo.. 5.8 | 28 |
| 6 Processos do Ciclo de Vida de Software | 28 |
| 6.1 Processos de Acordo | 28 |
| Processo de Aquisição.. 6.1.1 | 29 |
| Processo de Fornecimento.. 6.1.2 | 32 |
| 6.2 Processos Organizacionais Habilitadores de Projeto | 35 |
| 6.2.1 Processo de Gerenciamento de Modelo de Ciclo de Vida | 35 |
| 6.2.2 Processo de Gerenciamento de Infraestrutura | 37 |
| Processo de Gerenciamento de Portfólio.. 6.2.3 | 39 |
| Processo de Gerenciamento de Recursos Humanos 6.2.4 | 41 |
| Processo de Gestão da Qualidade.... 6.2.5 | 42 |
| Processo de Gerenciamento do Conhecimento . 6.2.6 | 44 |
| Processos de Gerenciamento Técnico. 6.3 | ‚46 |
| 6.3.1 Processo de Planejamento de Projeto | 47 |
| 6.3.2 Processo de Avaliação e Controle de Projeto | 50 |
| Processo de Gerenciamento de Decisão. 6.3.3 | 53 |
| Processo de Gestão de Riscos. 6.3.4 | 55 |
| Processo de Gerenciamento de Configuração . 6.3.5 | 57 |
| Processo de Gerenciamento da Informação.. 6.3.6 | 62 |
| 6.3.7 Processo de Medição | 64 |
| 6.3.8 Processo de Garantia da Qualidade | 66 |
| 6.4 Processos Técnicos | 68 |
| Processo de Análise de Negócio ou Missão .. 6.4.1 | 70 |
| Processo de Definição de Necessidades e Requisitos dos Stakeho/ders .. 6.4.2 | 73 |
| Processo de definição de requisitos de Sistema/Software. 6.4.3 | 78 |
| Processo de Definição de Arquitetura.. 6.4.4 | 83 |
| 6.4.5 Processo de Definição de Design | 88 |
| 6.4.6 Processo de Análise de Sistema | 93 |
| 6.4.7 Processo de Implementação | 95 |
| 6.4.8 Processo de Integração | 99 |
| Processo de Verificação. 6.4.9 | 103 |
| Processo de Transição. 6.4.10 | 108 |
| 6.4.11 Processo de Validação | 113 |
| 6.4.12 Processo de Operação | 117 |
| 6.4.13 Processo de Manutenção | 121 |
| Processo de Desativação 6.4.14 | 127 |
| Anexo A (normativo) Processo de Adaptação | 130 |
| A. 1 Introdução | 130 |
| Processo de Adaptação.. A.2 | 130 |
| Propósito.. A.2.1 | 130 |
| A.2.2 Resultados esperados | 130 |
| Atividades e tarefas . A.2.3 | 130 |
| Anexo B (informativo) Exemplos de itens de informação de processo | 133 |
| Anexo C (informativo) Modelo de Referência de Processo (MRP) para Fins de Avaliação | 139 |
| Introdução.. C.1 | 139 |
| Conformidade com a ISO/IEC 33004 ... C.2 | 139 |
| Geral ... C.2.1 | 139 |
| Requisitos para os Modelos de Referência de Processo C.2.2 | 139 |
| C.2.3 Descrições de Processo | 140 |
| C.3 O Modelo de Referência de Processo | 140 |
| Anexo D (informativo) Integração e construtos de processo | 141 |
| D.1 Introdução | 141 |
| Construtos de processo e sua utilização D.2 | 141 |
| (informativo) Visões de processo | 144 |
| E. 1 Introdução | 144 |
| Conceito de visão de processo. E.2 | 144 |
| Ponto de vista de processo E.3 | 144 |
| E.4 Visão de processo de engenharia especializada | 145 |
| E.5 Visão do processo de Gerenciamento de Interface | 148 |
| Visão do processo para Garantia do Software (Segurança da Informação) .. E.6 | 151 |
| (informativo) Modelagem da arquitetura de sistemas de software | 156 |
| F.1 Introdução | 156 |
| F.2 Visões, modelos e tipos de modelos usados em arquitetura de sistemas de software.. 156 |  |
| Modelo funcional | 157 |
| Modelo estático | 157 |
| Modelo de dados | 157 |
| Modelo comportamental | 157 |
| Modelo temporal | 158 |
| Modelo estrutural | 158 |
| Modelo de rede | 158 |
| Outras considerações sobre modelos | 158 |
| Anexo G (informativo) Aplicação de processos de ciclo de vida de software a um sistema |  |
| de sistemas | 159 |
| Introdução | 159 |
| Características e tipos de SoS | 159 |
| Processos de Engenharia de Sistemas aplicados aos sistemas de sistemas | 160 |
| Geral | 160 |
| Processos de Acordo | 160 |
| Processos Organizacionais Habilitadores de Projeto | 161 |
| Processos de Gerenciamento Técnico. G.3.4 | 161 |
| G.3.5 Processos Técnicos | 162 |
| Anexo H (informativo) Aplicação da Abordagem Ágil | 164 |
| Anexo \| (informativo) Mapeamento de Processo da ISO/IEC/IEEE 12207:2008 | 167 |
| Bibliografia | 187 |



**Figuras**

| Entrada | Página |
|---|---|
| Figura 1 - Sistema de software e relacionamento entre seus elementos | 17 |
| Figura 2 - Exemplo de estrutura de sistema de software de interesse | 18 |
| Figura 3 - Sistema de interesse de software, seu ambiente de operação e sistemas |  |
| habilitadores | 19 |
| Figura 4 - Processos do ciclo de vida de software | 25 |
| Figura D.1 - ABNT NBR ISO/IEC/IEEE 12207:2021 e ISO/IEC/IEEE 15288:2015 - Construtos |  |
| de processo | 143 |



**Tabelas**

| Entrada | Página |
|---|---|
| Tabela B.1 - Amostras de itens de informação por processo | 133 |
| Tabela G.1 - Tipos de Sistemas de Sistemas | 160 |
| Tabela I.1 - Comparação de processos na ABNT NBR ISO/IEC/IEEE 12207:2021 e na versão |  |
| anterior | 167 |
| Tabela 1.2 - Comparação dos resultados esperados do processo na |  |
| ABNT NBR ISO/IEC/IEEE 12207:2021 e dos resultados esperados relativos ao |  |
| software na edição anterior | 170 |



## Prefácio Nacional

A Associação Brasileira de Normas Técnicas (ABNT) é o Foro Nacional de Normalização. As Normas Brasileiras, cujo conteúdo é de responsabilidade dos Comitês Brasileiros (ABNT/CB), dos Organismos de Normalização Setorial (ABNT/ONS) e das Comissões de Estudo Especiais (ABNT/CEE), são elaboradas por Comissões de Estudo (CE), formadas pelas partes interessadas no tema objeto da normalização.

Os Documentos Técnicos internacionais adotados são elaborados conforme as regras da ABNT Diretiva 3.

AABNT chama a atenção para que, apesar de ter sido solicitada manifestação sobre eventuais direitos de patentes durante a Consulta Nacional, estes podem ocorrer e devem ser comunicados à ABNT a qualquer momento (Lei n° 9.279, de 14 de maio de 1996).

Os Documentos Técnicos ABNT, assim como as Normas Internacionais (ISO e IEC), são voluntários e não incluem requisitos contratuais, legais ou estatutários. Os Documentos Técnicos ABNT não substituem Leis, Decretos ou Regulamentos, aos quais os usuários devem atender, tendo precedência sobre qualquer Documento Técnico ABNT.

Ressalta-se que os Documentos Técnicos ABNT podem ser objeto de citação em Regulamentos Técnicos. Nestes casos, os órgãos responsáveis pelos Regulamentos Técnicos podem determinar as datas para exigência dos requisitos de quaisquer Documentos Técnicos ABNT.

A ABNT NBR ISO/IEC/IEEE 12207 foi elaborada no Comitê Brasileiro de Computadores e Processamento de Dados (ABNT/CB-021), pela Comissão de Estudo de Engenharia de Software e Sistemas (CE-021:000.007). O Projeto circulou em Consulta Nacional conforme Edital n° 07, de 16.07.2021 a 16.08.2021.

AABNT NBR ISO/IEC/IEEE 12207 é uma adoção idêntica, em conteúdo técnico, estrutura e redação, à ISO/IEC/IEEE 12207:2017, que foi elaborada pelo Joint Technical Committee Information Technology (ISO/EC JTC 1), Subcommittee Software and systems engineering (SC 7).

O Escopo em inglês da ABNT NBR ISO/IEC/IEEE 12207 é o seguinte:

Scope

This document establishes a common framework for life cycle processes, with well-defined termonilogy, that can be referred by the software industry. It contains processes, activities, and tasks that are applicable during the acquisition, supply, development, operation, maintenance or disposal of software systems, products, and services. These life cycle processes are accomplished through the involvement of stakeholders, with the ultimate goal of achieving customer satisfaction.


## Introdução

A complexidade dos sistemas de software aumentou a um nível sem precedentes. Isto levou a novas oportunidades, mas também aumentou os desafios para as organizações que criam e utilizam sistemas. Estes desafios existem ao longo do ciclo de vida de um sistema e em todos os níveis de detalhes arquiteturais. Este documento fornece uma estrutura de processo comum para descrever o ciclo de vida de sistemas criados por seres humanos, adotando uma abordagem de Engenharia de Software. A Engenharia de Software é uma abordagem interdisciplinar e propicia a produção bem-sucedida de sistemas de software. Ela foca a definição das necessidades dos stakeholders e a funcionalidade requerida no início do ciclo de desenvolvimento, a documentação dos requisitos, a execução da síntese do design e a validação do sistema, considerando o problema completo. Ela integra todas as disciplinas e grupos de especialidade em um esforço de equipe, formando um processo de desenvolvimento estruturado que passa do conceito à produção, operação e manutenção. Ela considera tanto as necessidades de negócio quanto técnicas de todos os stakeholders, com o objetivo de fornecer um produto de qualidade que atenda às necessidades dos usuários e outros stakeholders aplicáveis. Este ciclo de vida abrange da concepção de ideias até a desativação de um sistema. Ela provê os processos para aquisição e fornecimento de sistemas. Ela ajuda a melhorar a comunicação e a cooperação entre as partes que criam, utilizam e gerenciam sistemas de software modernos para que possam trabalhar de forma integrada e coerente. Além disso, a estrutura proposta contribui para a avaliação e melhoria dos processos do ciclo de vida.

Os processos neste documento formam um conjunto abrangente a partir do qual uma organização pode construir modelos de ciclo de vida de software apropriados para seus produtos e serviços. Uma organização, dependendo da sua finalidade, pode selecionar e aplicar um subconjunto apropriado para alcançar este propósito.

Este documento pode ser usado de uma ou mais das seguintes formas:

Por uma organização - para ajudar a estabelecer um ambiente de processos desejados. Estes processos podem ser sustentados por uma infraestrutura de métodos, procedimentos, técnicas, ferramentas e pessoal treinado. A organização pode então empregar este ambiente para executar e gerenciar seus projetos e evoluir sistemas de software ao longo as fases do ciclo de vida. Dessa forma, este documento é usado para avaliar a conformidade de um ambiente declarado e estabelecido em relação ao que ele provê.

- b) Por um projeto - para ajudar a selecionar, estruturar e utilizar os elementos de um ambiente estabelecido para fornecer produtos e serviços. Dessa forma, este documento é usado na avaliação da conformidade do projeto em relação ao ambiente estabelecido e declarado.
- c) Por um adquirente e um fornecedor - para ajudar a desenvolver um acordo relativo a processos e atividades. Por meio desse acordo, os processos e atividades deste documento são selecionados, negociados, acordados e executados. Dessa forma, este documento é usado para orientar o desenvolvimento do acordo.
- d) Por avaliadores de processo - para servir como um modelo de referência de processo utilizado na execução de avaliações de processo, que podem ser usadas para apoiar a melhoria do processo organizacional.
NORMA BRASILEIRA ABNT NBR ISO/IEC/IEEE 12207:2021

Engenharia de sistemas e software - Processos de ciclo de vida de

software


# 1 Escopo


## 1.1 Visão Geral

Este documento estabelece uma estrutura comum para processos de ciclo de vida de software, com terminologia bem definida, que pode ser referenciada pela indústria de software. Ele contém processos, atividades e tarefas que são aplicáveis durante a aquisição, fornecimento, desenvolvimento, operação, manutenção ou desativação de sistemas, produtos e serviços de software. Estes processos de ciclo de vida são executados com sucesso por meio do envolvimento de stakeholders, com o objetivo final de alcançar a satisfação do cliente.

Este documento é aplicável à aquisição, fornecimento, desenvolvimento, operação, manutenção e desativação de sistemas de software, produtos e serviços, e a parte de software de qualquer sistema (executados tanto interna como externamente a uma organização). Software inclui a parte de software do firmware. Os aspectos de definição de sistema necessários para prover o contexto para produtos e serviços de software estão incluidos.

Este documento também fornece processos que podem ser empregados na definição, controle e melhoria dos processos de ciclo de vida de software dentro de uma organização ou projeto.

Os processos, atividades e tarefas deste documento também podem ser aplicados durante a aquisição de um sistema que contenha software, seja individualmente ou em conjunto com a ISO/IEC 15288:2015, Systems and software engineering - System life cycle processes.

No contexto deste documento e da ISO/IEC/IEEE 15288, há um continuum de sistemas desenvolvidos por humanos desde os que usam pouco ou nenhum software, até aqueles nos quais o software é o principal componente. É raro encontrar um sistema complexo sem software e todos os sistemas de software exigem que os componentes do sistema físico (hardware) funcionem, ou seja, como parte do sistema de software de interesse. Assim, a escolha de quando aplicar este documento para os processos de ciclo de vida de software, ou a ISO/IEC/IEEE 15288: 2015, Systems and software engineering-System life cycle processes, depende do sistema de interesse. Os processos em ambos os documentos têm os mesmos propósitos e resultados de processo, mas diferem em atividades e tarefas para executar a engenharia de software ou a engenharia de sistemas, respectivamente.


## 1.2 Propósito

O propósito deste documento é fornecer um conjunto definido de processos para facilitar a comunicação entre adquirentes, fornecedores e outros stakeholders no ciclo de vida de um sistema de software.

Este documento foi escrito para adquirentes, fornecedores, desenvolvedores, integradores, operadores, mantenedores, gestores, gerentes de garantia de qualidade e usuários de sistemas, produtos e serviços de software. Ele pode ser usado por uma única organização de forma autoimposta ou em uma situação que envolva várias organizações. As partes podem ser da mesma organização ou de diferentes organizações, podendo variar para a realização de um acordo informal a um acordo formal.

Os processos neste documento podem ser usados como base para estabelecer ambientes de negócios, por exemplo, métodos, procedimentos, técnicas, ferramentas e pessoal treinado. O Anexo A fornece orientação normativa para a adaptação destes processos de ciclo de vida de software.


## 1.3 Campo de aplicação

Este documento é aplicável a todo o ciclo de vida de sistemas, produtos e serviços de software, incluindo concepção, desenvolvimento, produção, utilização, suporte e desativação, e à sua aquisição e fornecimento, sejam estes processos executados interna ou externamente a uma organização. Os processos do ciclo de vida deste documento podem ser aplicados de forma concorrente, iterativa e recursiva a um sistema de software e de forma incremental aos seus elementos.

Há uma grande variedade de sistemas de software em termos de propósito, domínio de aplicação, complexidade, tamanho, novidade, adaptabilidade, quantidade, localizações, vida útil e evolução. Este documento descreve os processos que compõem o ciclo de vida de sistemas de software criados pelo homem. Portanto, aplica-se aos sistemas de software únicos, sistemas de software para ampla distribuição comercial ou pública e sistemas de software adaptáveis e customizados. Também se aplica a um sistema de software independente completo e aos sistemas de software que são incorporados e integrados a sistemas maiores, mais complexos e completos.

Este documento fornece um modelo de referência de processo caracterizado em termos de propósito e resultados de processo, que são consequência da execução bem-sucedida das tarefas da atividade. O Anexo B lista exemplos de artefatos e itens de informação que podem estar associados a vários processos. Este documento pode, portanto, ser usado como um modelo de referência para apoiar a avaliação de processo, conforme especificado na ISO/IEC 33002:2015. O Anexo C fornece informações sobre o uso dos processos de ciclo de vida do software como um modelo de referência de processo. O Anexo D descreve os construtos do processo para uso no modelo de referência de processo. O Anexo | fornece a correspondência entre este documento e a ISO/IEC/IEEE 12207:2009 no nível de nome e resultado de processo.


## 1.4 Limitações

Este documento não prescreve um modelo específico de ciclo de vida de software, metodologia de desenvolvimento, método, abordagem de modelagem ou técnica. Os usuários deste documento são responsáveis por selecionar um modelo de ciclo de vida para o projeto e por mapear os processos, atividades e tarefas deste documento naquele modelo. As partes também são responsáveis pela seleção e aplicação de metodologias, métodos, modelos e tecnicas apropriados para o projeto.

Este documento não estabelece um sistema de gestão ou requer o uso de qualquer norma de sistema de gestão. No entanto, destina-se a ser compatível com o sistema de gestão da qualidade especificado pela ABNT NBR ISO 9001, com o sistema de gestão de serviços especificado pela ABNT NBR ISO/IEC 20000-1 (IEEE Std 20000-1) e com o sistema de gestão de segurança da informação especificado pela ISO/IEC 27000.

Este documento não detalha itens de informação em termos de nome, formato, conteúdo explícito e mídia de registro. A ISO/IEC/IEEE 15289 aborda o conteúdo dos itens de informação de processo de ciclo de vida (documentação).


# 2 Referências normativas

Não há referências normativas neste documento.


# 3 Termos, definições, e termos abreviados


## 3.1 Termos e definições

Para os propósitos deste documento, aplicam-se os seguintes termos e definições.

A ISO e a IEC mantêm bancos de dados terminológicos para uso em padronização nos seguintes endereços:

- IEC Electropedia: disponível em http://www.electropedia.org

- Plataforma de navegação on-line da ISO: disponível em http://www.iso.org/obp

- IEEE Standards Dictionary Online: disponível em http://ieeexplore.ieee.org/xpls/dictionary.jsp

Definições para outros termos podem ser encontradas em ISO/IEC/IEEE 24765, System and software engineering - Vocabulary, disponivel em <www.computer.org/sevocab>.


### 3.1.1 adquirente

stakeholder que adquire ou obtém um produto ou serviço de um fornecedor

NOTA Outros termos comumente usados para um adquirente são comprador, cliente, proprietário, consumidor ou patrocinador interno/organizacional.


### 3.1.2 aquisição

processo de obtenção de um sistema, produto ou serviço


### 3.1.3 atividade

conjunto de tarefas coesas de um processo


### 3.1.4 desenvolvimento ágil

abordagem de desenvolvimento de software baseada em desenvolvimento iterativo, inspeção e adaptação frequentes e entregas incrementais, nas quais os requisitos e as soluções evoluem por meio da colaboração em equipes multifuncionais e por meio de feedback contínuo dos stakeholders

[FONTE: ISO/IEC/IEEE 26515: 2011]


### 3.1.5 acordo

reconhecimento mútuo de termos e condições sob os quais um relacionamento de trabalho é conduzido

EXEMPLO Contrato, memorando de acordo.


### 3.1.6 arquitetura

‹sistema> conceitos fundamentais ou propriedades de um sistema em seu ambiente incorporados em seus elementos, relacionamentos e nos princípios de seu design e evolução.

[FONTE: ISO/IEC/IEEE 42010:2011]


### 3.1.7 framework de arquitetura

convenções, princípios e práticas para a descrição de arquiteturas estabelecidas dentro de um domínio específico de aplicação e/ou comunidade de stakeholders

EXEMPLO 1 Arquitetura e Metodologias de Referência Corporativa Generalizada (GERAM - Generalised Enterprise Reference Architecture and Methodologies) [ISO 15704] é um framework de arquitetura.

EXEMPLO 2 Modelo de Referência de Processamento Distribuído Aberto (RM-ODP - Reference Model of Open Distributed Processing ) [ISO/IEC 10746] é um framework de arquitetura.

[FONTE: ISO/IEC/IEEE 42010:2011]


### 3.1.8 visão de arquitetura

produto de trabalho que expressa a arquitetura de um sistema a partir da perspectiva de interesses específicos do sistema.

[Fonte: ISO/IEC/IEEE 42010:2011]


### 3.1.9 ponto de vista de arquitetura

produto de trabalho que estabelece as convenções para a construção, interpretação e uso de visões de arquitetura para enquadrar interesses específicos do sistema

[FONTE: ISO/EC/IEEE 42010:2011]


### 3.1.10 auditoria

exame independente de um ou mais produtos de trabalho para avaliar a conformidade com especificações, normas, acordos contratuais ou outros critérios


### 3.1.11 baseline

versão formalmente aprovada de um item de configuração, independentemente da mídia, designada formalmente e fixada em um momento específico durante o ciclo de vida do item de configuração

[FONTE: IEEE Std 828-2012]


### 3.1.12 processo de negócio

conjunto parcialmente ordenado de atividades da empresa, que podem ser executadas para alcançar algum resultado final desejado no atendimento a um determinado objetivo de uma organização


### 3.1.13 conceito de operações

declaração verbal e/ou gráfica, em linhas gerais, das premissas ou intenções de uma organização em relação a uma operação ou série de operações

Nota 1 de entrada: O conceito de operações frequentemente é incorporado em planos estratégicos de longo prazo e planos operacionais anuais. Neste último caso, o conceito de operações no plano abrange uma série de operações conectadas a serem executadas simultaneamente ou em sequência. O conceito e projetado para fornecer uma visão geral das operações da organização. Ver também conceito operacional (3.1.28).

Nota 2 de entrada: Ele fornece a base para delimitar o espaço operacional, as capacidades do sistema, as interfaces e o ambiente operacional.

[FONTE: ANSI/AIAA G-043A-2012e]


### 3.1.14 interesse

‹sistema> interesse em um sistema relevante para um ou mais de seus stakeholders

Nota 1 de entrada : Um interesse significa qualquer influência sobre um sistema em seu ambiente, incluindo aquelas de desenvolvimento, tecnológicas, negócios, operacionais, organizacionais, politicas, econômicas, legais, regulatorias, ecologicas e sociais.

[FONTE: ISO/IEC/IEEE 42010:2011]


### 3.1.15 item de configuração

item ou agregação de hardware, software ou ambos, que é designado para gerenciamento de configuração e tratado como uma entidade única no Processo de Gerenciamento de Configuração

EXEMPLO Software, firmware, dado, hardware, pessoas, processos (por exemplo, processos para prover serviços aos usuários), procedimentos (por exemplo, instruções ao operador e manuais do usuário), instalações, serviços, materiais e outras entidades.


### 3.1.16 cliente

organização ou pessoa que recebe um produto ou serviço

EXEMPLO Consumidor, cliente, usuário, adquirente ou comprador

NOTA Um cliente pode ser interno ou externo à organização.


### 3.1.17 design, verbo

‹processo> para definir a arquitetura, elementos do sistema, interfaces e outras características de um sistema ou elemento do sistema

[FONTE: ISO/IEC/IEEE 24765:2010, o termo 'componentes' foi substituído por 'elemento do sistema']


### 3.1.18 design, substantivo

resultado do processo em 3.1.17

Nota 1 de entrada: Informações, incluindo a especificação de elementos do sistema e seus relacionamentos, que estejam suficientemente completas para apoiar uma implementação compatível com a arquitetura

Nota 2 de entrada: O design fornece o nível de implementação detalhado da estrutura física, comportamento, relacionamentos temporais e outros atributos dos elementos do sistema.


### 3.1.19 característica de design

atributos ou características distintivas de design que se referem a uma descrição mensurável de um produto ou serviço


### 3.1.20 sistema habilitador

sistema que apoia um sistema de interesse durante suas fases de ciclo de vida, mas não necessariamente contribui diretamente para sua função durante a operação

EXEMPLO Um sistema de gerenciamento de configuração utilizado para controlar elementos do software durante o seu desenvolvimento.

Nota 1 de entrada: Cada sistema habilitador tem um ciclo de vida próprio. Este documento é aplicável a cada sistema habilitador quando este, por si só, é tratado como um sistema de interesse.


### 3.1.21 ambiente

‹sistema> contexto que determina o cenário e as circunstâncias de todas as influências sobre um sistema

[FONTE: ISO/IEC/IEEE 42010:2011]


### 3.1.22 instalações

meios físicos ou equipamentos para permitir a execução de uma ação, por exemplo, prédios, instrumentos, ferramentas


### 3.1.23 incidente

evento, conjunto de eventos, condição ou situação, anômalo ou inesperado, que ocorre a qualquer momento durante o ciclo de vida de um projeto, produto, serviço ou sistema


### 3.1.24 item de informação

informação ou conjunto de informações identificável separadamente que é produzida, armazenada e entregue para uso humano

[FONTE: ISO/IEC/IEEE 15289:2015]


### 3.1.25 infraestrutura

ambiente de hardware e software para apoiar o design, desenvolvimento e alterações de sistemas e software de computadores


### 3.1.26 ciclo de vida

evolução de um sistema, produto, serviço, projeto ou outra entidade feita por humanos, desde a concepção até a desativação


### 3.1.27 modelo de ciclo de vida

framework de processos e atividades relacionados com o ciclo de vida, que pode ser organizado em etapas, atuando como uma referência comum para comunicação e entendimento


### 3.1.28 conceito operacional

declaração verbal e gráfica das premissas ou intenções de uma organização em relação a uma operação ou série de operações de um sistema ou um conjunto relacionado de sistemas

Nota 1 de entrada: O conceito operacional é projetado para fornecer uma visão geral das operações usando um ou mais sistemas específicos, ou conjunto de sistemas relacionados, no ambiente operacional da organização, do ponto de vista dos usuários e dos operadores. Ver também o conceito de operações (3.1.13).

[FONTE: ANSI/AIAA G-043A-2012e]


### 3.1.29 operador

indivíduo ou organização que executa as operações de um sistema

Nota 1 de entrada: O papel do operador e do usuário pode ser atribuído, simultânea ou sequencialmente, pelo mesmo indivíduo ou organização.

Nota 2 de entrada: Um operador combinado com conhecimento, habilidades e procedimentos pode ser considerado como um elemento do sistema.

Nota 3 de entrada: Um operador pode executar operações sobre um sistema, ou dentro de um sistema que é operado, dependendo de se as instruções de operação estão ou não dentro da fronteira do sistema.


### 3.1.30 organização

grupo de pessoas e instalações com uma estrutura de responsabilidades, autoridades e relacionamentos

EXEMPLO Companhia, corporação, firma, empresa, instituição, instituição de caridade, comerciante único, associação, partes ou combinação destes.

Nota 1 de entrada: Uma parte identificada de uma organização (mesmo que pequena com um único indivíduo) ou um grupo identificado de organizações pode ser considerada como uma organização se tiver responsabilidades, autoridades e relacionamentos. Um grupo de pessoas organizadas para algum propósito específico, como um clube, sindicato, corporação ou sociedade, é uma organização.


### 3.1.31 parte

organização que é parte de um acordo

Nota 1 de entrada: Neste documento, as partes de um acordo são chamadas de adquirente e fornecedor.


### 3.1.32 problema

dificuldade, incerteza ou evento percebido e indesejável, conjunto de eventos, condição ou situação que exija investigação e ação corretiva


### 3.1.33 processo

conjunto de atividades inter-relacionadas ou interativas que transformam entradas em saídas


### 3.1.34 resultado do processo

resultado observável do alcance com sucesso do propósito do processo


### 3.1.35 propósito do processo

objetivo de alto nível para a execução do processo e os possíveis resultados da implementação eficaz do processo

Nota 1 de entrada: O propósito da implementação do processo é fornecer benefícios aos stakeholders.


### 3.1.36 produto

resultado de um processo

Nota 1 de entrada: Existem quatro categorias genéricas de produtos acordadas: hardware (por exemplo, parte mecânica de um motor); software (por exemplo, programas de computador e possivelmente documentação e dados associados); serviços (por exemplo, transporte); e materiais processados (por exemplo, lubrificante). Hardware e materiais processados são geralmente produtos tangiveis, enquanto software ou serviços são geralmente intangíveis.


### 3.1.37 projeto

empreendimento com critérios de início e fim definidos para criar um produto ou serviço de acordo com recursos e requisitos especificados

Nota 1 de entrada: Um projeto pode ser visto como um processo único compreendendo atividades coordenadas e controladas e composto de atividades dos processos Técnicos e de Gerenciamento Técnico definidos neste documento.


### 3.1.38 ‹projeto> portfólio

coleção de projetos que apoiam a consecução dos objetivos estratégicos da organização


### 3.1.39 qualificação

processo de demonstrar se uma entidade é capaz de atender aos requisitos especificados


### 3.1.40 garantia da qualidade

parte da gestão da qualidade focada em prover confiança de que os requisitos de qualidade serão atendidos

[FONTE: ABNT NBR ISO 9000:2015]


### 3.1.41 característica de qualidade

característica inerente de um produto, processo ou sistema relacionada a um requisito

Nota 1 de entrada: As características críticas de qualidade geralmente incluem aquelas relacionadas à saúde, proteção, garantia de segurança, confiabilidade, disponibilidade e de suporte.


### 3.1.42 gestão da qualidade

atividades coordenadas para direcionar e controlar uma organização no que diz respeito à qualidade


### 3.1.43 liberação

versão específica de um item de configuração que é disponibilizada para um propósito específico

EXEMPLO Liberação de teste.


### 3.1.44 requisito

declaração que traduz ou expressa uma necessidade e suas restrições e condições associadas

[FONTE: ISO/IEC/IEEE 29148:2011, modificada, a NOTA foi removida.]


### 3.1.45 recurso

ativo que é utilizado ou consumido durante a execução de um processo

Nota 1 de entrada: Recursos incluem aqueles que são reutilizáveis, renováveis ou consumiveis.

EXEMPLO Diversas entidades como financiamento, pessoal, instalações, bens de capital, ferramentas e serviços públicos, como infraestrutura de energia, água, combustível e comunicação.


### 3.1.46 desativação

retirada de suporte ativo pela organização que opera ou faz manutenção, substituição parcial ou total por um novo sistema ou instalação de um sistema atualizado


### 3.1.47 risco

efeito da incerteza sobre o alcance dos objetivos

Nota 1 de entrada: Um efeito é um desvio em relação ao esperado - positivo ou negativo. Um efeito positivo também é conhecido como uma oportunidade.

Nota 2 de entrada: Os objetivos podem ter diferentes aspectos (como metas financeiras, de saúde, de proteção e ambientais) e podem aplicar-se em diferentes níveis (como estratégico, organizacional, de projeto, de produto e de processo).

Nota 3 de entrada: O risco é frequentemente caracterizado pela referência a eventos e consequências potenciais, ou uma combinação destes.

Nota 4 de entrada: O risco é frequentemente expresso em termos de uma combinação das consequências de um evento (incluindo mudanças nas circunstâncias) e a probabilidade de ocorrência associada.

Nota 5 de entrada: Incerteza é o estado, mesmo que parcial, da deficiência de informação relacionada com a compreensão ou conhecimento de um evento, sua consequência ou probabilidade.

[FONTE: ABNT ISO Guia 73:2009, definição 1.1]


### 3.1.48 proteção

expectativa de que um sistema, sob condições definidas, não conduza a um estado em que a vida humana, a saúde, a propriedade ou o ambiente estejam em perigo


### 3.1.49 segurança

proteção contra falha intencional ou forçada; um composto de quatro atributos - confidencialidade, integridade, disponibilidade e responsabilização - além de aspectos de um quinto atributo, usabilidade, incluindo os aspectos relacionados à garantia de todos estes

[FONTE: NATO AEP-67]


### 3.1.50 serviço

execução de atividades, trabalho ou obrigações

Nota 1 de entrada: Um serviço é autocontido, coerente, discreto e pode ser composto por outros serviços.

Nota 2 de entrada: Um serviço é geralmente um produto intangível.


### 3.1.51 elemento de software

elemento do sistema que é software


### 3.1.52 engenharia de software

aplicação de uma abordagem sistemática, disciplinada e quantificável para o desenvolvimento, operação e manutenção de software; isto é, a aplicação da engenharia ao software


### 3.1.53 item de software

código fonte, código objeto, código de controle, dado de controle ou uma coleção destes itens

Nota 1 de entrada: Um item de software pode ser visto como um elemento de sistema neste documento e na ISO/IEC/IEEE 15288: 2015. Itens de software são tipicamente itens de configuração.


### 3.1.54 produto de software

conjunto de programas de computador, procedimentos, podendo incluir documentação e dados associados

Nota 1 de entrada: Um produto de software é um sistema de software visto como a saída (produto) resultante de um processo.


### 3.1.55 sistema de software

sistema para o qual o software é de importância primordial para os stakeholders

Nota 1 de entrada: No caso mais geral, um sistema de software é composto por hardware, software, pessoas e procedimentos manuais.

Nota 2 de entrada: Em um sistema de software, o software é o principal agente para atender aos requisitos do sistema.


### 3.1.56 elemento do sistema de software

item de um conjunto de elementos que constituem um sistema de software

Nota 1 de entrada: Um elemento do sistema de software pode incluir uma ou mais unidades de software, elementos de software, unidades de hardware, elementos de hardware, serviços e outros elementos de sistema e sistemas.

Nota 2 de entrada: Um elemento do sistema de software pode ser visto como um elemento do sistema.


### 3.1.57 unidade de software

componente de software no nível atômico da arquitetura de software que pode ser sujeito a testes independentes

Nota 1 de entrada: Algumas unidades de software são partes de código compiláveis separadamente.

[FONTE: ISO 26262-1:2011, modificada, Nota 1 adicionada.]


### 3.1.58 fase

período dentro do ciclo de vida de uma entidade que se relaciona com o estado de sua descrição ou realização

Nota 1 de entrada: Conforme usados neste documento, as fases estão relacionadas aos principais marcos de realização e progresso da entidade ao longo de seu ciclo de vida.

Nota 2 de entrada: As fases geralmente se sobrepõem.


### 3.1.59 stakeholder

indivíduo ou organização que tenha direito, participação, demanda ou interesse em um sistema ou na existência de características deste sistema que atendam às suas necessidades e expectativas

EXEMPLO Usuários finais, organizações de usuários finais, responsáveis pelo suporte, desenvolvedores, produtores, instrutores, mantenedores, responsáveis pela descontinuação, adquirentes, organizações de fornecedores e órgãos reguladores.

Nota 1 de entrada: Alguns stakeholders podem ter interesses divergentes ou podem se opor ao sistema.


### 3.1.60 fornecedor

organização ou um indivíduo que celebra um acordo com o adquirente para o fornecimento de um produto ou serviço

Nota 1 de entrada: Outros termos comumente usados para fornecedor são: contratado, produtor, vendedor ou representante.

Nota 2 de entrada: O adquirente e o fornecedor às vezes fazem parte da mesma organização.


### 3.1.61 sistema

combinação de elementos organizados que interagem para atingir um ou mais propósitos declarados

Nota 1 de entrada: Um sistema é por vezes considerado como um produto ou como os serviços que fornece.

Nota 2 de entrada: Na prática, a interpretação do seu significado é frequentemente esclarecida pelo uso de um substantivo associativo, por exemplo, sistema de aeronave ou sistema de gerenciamento de banco de dados. Alternativamente, a palavra "sistema" é substituída simplesmente por um sinônimo dependente de contexto, por exemplo, aeronave ou banco de dados, embora isto possa potencialmente obscurecer a perspectiva dos princípios do sistema.

Nota 3 de entrada: Um sistema pode incluir equipamento, instalações, material, software, firmware, documentação técnica, serviços e pessoal requeridos para operação e suporte, na medida necessária para uso no seu ambiente pretendido.

Nota 4 de entrada: Para comparação ver: sistema habilitador, sistema de interesse, sistema de sistemas.


### 3.1.62 elemento de sistema

item de um conjunto de elementos que constituem um sistema

EXEMPLO Hardware, software, dados, pessoas, processos (por exemplo, processos para fornecer serviço aos usuários), procedimentos (por exemplo, instruções ao operador), instalações, materiais e entidades que ocorrem naturalmente ou qualquer combinação.

Nota 1 de entrada: Um elemento do sistema é uma parte discreta de um sistema que pode ser implementada para satisfazer requisitos especificados.


### 3.1.63 sistema de interesse

SOI (system-of-interest) sistema cujo ciclo de vida está sendo considerado


### 3.1.64 sistema de sistemas

SoS (system of systems) conjunto de sistemas que se integram ou interoperam para fornecer uma capacidade única que nenhum dos sistemas constituintes pode realizar isoladamente

Nota 1 de entrada: Cada sistema constituinte é um sistema por si só, tendo seu próprio gerenciamento, metas e recursos, mas é coordenado dentro do SoS para fornecer a capacidade exclusiva do SoS.


### 3.1.65 engenharia de sistemas

abordagem interdisciplinar que rege todo o esforço técnico e gerencial necessário para transformar um conjunto de necessidades, expectativas e restrições dos stakeholders em uma solução e oferecer suporte a esta solução durante sua vida


### 3.1.66 tarefa

ação requerida, recomendada ou permitida, com intenção de contribuir para o atingimento de um ou mais resultados de um processo


### 3.1.67 gerenciamento técnico

aplicação de recursos técnicos e administrativos para planejar, organizar e controlar funções de engenharia


### 3.1.68 trade-off

ações de tomada de decisão que selecionam entre vários requisitos e soluções alternativas com base no benefício efetivo para os stakeholders


### 3.1.69 rastreabilidade

grau de relacionamento que pode ser estabelecido entre duas ou mais entidades lógicas, especialmente entidades que têm um relacionamento predecessor-sucessor ou superior-subordinado entre si, como requisitos, elementos do sistema, verificações ou tarefas

EXEMPLO Características de software e casos de teste são normalmente rastreados para requisitos de software.


### 3.1.70 usuário

indivíduo ou grupo que interage com um sistema ou se beneficia de um sistema durante sua utilização

Nota 1 de entrada: O papel do usuário e do operador às vezes são exercidos, simultânea ou sequencialmente, pelo mesmo indivíduo ou organização.

[FONTE: ISO/IEC 25010:2011, modificada, Nota 1 de entrada adicionada.]


### 3.1.71 validação

confirmação, por meio do fornecimento de evidência objetiva, de que os requisitos para uma aplicação ou um uso pretendido específico tenham sido atendidos

Nota 1 de entrada: Um sistema é capaz de atingir seu uso, metas e objetivos pretendidos (isto é, satisfazer os requisitos dos stakeholders) no ambiente operacional pretendido. O sistema certo foi construído.

Nota 2 de entrada: Em um contexto de ciclo de vida, a validação envolve o conjunto de atividades para ganhar confiança de que um sistema é capaz de ser usado, atendendo às metas e aos objetivos pretendidos em um ambiente similar ao ambiente operacional.


### 3.1.72 verificação

confirmação, por meio do fornecimento de evidência objetiva, de que os requisitos especificados foram atendidos

do sistema com as características requeridas. Isto inclui, mas não está limitado a requisitos especificados, Nota 1 de entrada: A verificação é um conjunto de atividades que compara um sistema ou elemento

design, descrições e o próprio sistema. O sistema foi construído corretamente.

[FONTE: ABNT NBR ISO 9000:2015, modificada, Nota 1 de entrada adicionada]


## 3.2 Termos abreviados

CCB Conselho de Controle de Configuração (Configuration Control Board)

CM Gerenciamento de Configuração de Software (Configuration Management - usamos GCS)

COTS Produtos Comercialmente Disponíveis / Pacote de Software de Prateleira (Commercial-Off-The-Shelf)

FCA Auditoria Funcional de Configuração (Functional Configuration Audit)

FOSS Software Livre e de Código Aberto (Free and Open Source Software)

GUI Interface Gráfica do Usuário (Graphical User Interface)

NDI Itens que Não Serão Desenvolvidos (Non-Developmental Items)

OTS Software de prateleira não comercializado (Off-The-Shelf Software)

QA Garantia da Qualidade (Quality Assurance)

Auditoria Física de Configuração

PESTEL Politica, Econômica, Social, Tecnológica, Ambiental e Legal (Political, Economic, Social, Technological, Environmental, and Legal)

PMI Instituto de Gerenciamento de Projeto (Project Management Institute)

PMP Plano de Gerenciamento de Projeto (Project Management Plan)

PRM Modelo de Referência de Processo (Process Reference Model)

SCM Gerenciamento de Configuração de Software (Software Configuration Management)

SDP Plano de Desenvolvimento de Software (Software Development Plan)

SEMP Plano de Gerenciamento de Engenharia de Sistemas (Systems Engineering Management Plan)

SOI Sistema de Interesse (System-of-Interest)

SoS Sistema de Sistemas (System of Systems)

SWOT Forças, Fraquezas, Oportunidades, Ameaças (Strengths, Weaknesses, Opportunities, Threats)

WBS Estrutura Analítica de Projeto -EAP (Work Breakdown Structure)


# 4 Conformidade


## 4.1 Uso pretendido

Os requisitos neste documento estão contidos na Seção 6 e no Anexo A. Este documento fornece requisitos para uma variedade processos adequados para uso durante o ciclo de vida de um sistema ou produto de software. E reconhecido que projetos ou organizações específicos podem não precisar usar todos os processos fornecidos por este documento. Portanto, a implementação deste documento geralmente envolve a seleção e a declaração de um conjunto de processos adequados à organização ou projeto. Existem duas formas de reivindicar a conformidade com as disposições deste documento - conformidade total e conformidade personalizada.

Existem dois critérios para reivindicar a conformidade total. Atingir qualquer destes critérios é suficiente para conformidade, embora o criterio (ou criterios) escolhido(s) deva(m) ser deciarado(s) na reivindicação. Reivindicar conformidade total com as tarefas afirma que todos os requisitos

reivindicar "conformidade total com os resultados" afirma que todos os resultados requeridos das atividades e tarefas do conjunto declarado de processos são alcançados. Alternativamente,

do conjunto declarado de processos são alcançados. A conformidade total com resultados permite maior liberdade na implementação de processos e pode ser útil para implementar processos a serem usados no contexto de um modelo inovador de ciclo de vida.

NOTA 1 Opções para conformidade são fornecidas para a flexibilidade necessária na aplicação deste documento. Cada processo tem um conjunto de objetivos (expressos como resultados) e um conjunto de atividades e tarefas que representam uma maneira de alcançar os objetivos.

NOTA 2 Os usuários que implementam as atividades e tarefas do conjunto declarado de processos podem afirmar conformidade total com as tarefas dos processos selecionados. Alguns usuários, no entanto, podem ter variantes inovadoras de processos que atinjam os objetivos (ou seja, os resultados) do conjunto declarado de processos sem implementar todas as atividades e tarefas. Estes usuários podem afirmar conformidade total com os resultados do conjunto declarado de processos. Os dois critérios - conformidade com tarefa e conformidade com resultado - não são necessariamente equivalentes, pois a execução específica de atividades e tarefas pode requerer, em alguns casos, um nível mais alto de capacidade do que apenas o alcance de resultados.

NOTA 3 Quando este documento é usado para auxiliar o desenvolvimento de um acordo entre um adquirente e um fornecedor, seções deste documento podem ser selecionadas para incorporação ao acordo, com ou sem modificação. Neste caso, é mais apropriado que o adquirente e o fornecedor reivindiquem a conformidade com o acordo do que com este documento.

Uma organização (por exemplo, pública, associação industrial, corporação) que impõe este documento, como condição comercial, pode especificar e tornar público o conjunto mínimo de processos, resultados, atividades e tarefas exigidos, que constituem a conformidade dos fornecedores com as condições do negócio.

Os requisitos deste documento são assinalados pelo uso do verbo "deve" . As recomendações são assinaladas pelo uso da expressão "convém que". As permissões são assinaladas pelo uso do verbo "pode". No entanto, apesar do termo usado, os requisitos de conformidade são selecionados conforme descrito anteriormente.


## 4.2 Conformidade total


### 4.2.1 Conformidade total com resultados

Uma reivindicação de conformidade total declara o conjunto de processos com os quais a conformidade é requerida. A conformidade total com resultados é alcançada pela demonstração que todos os resultados do conjunto declarado de processos foram alcançados. Nesta situação, as disposições para atividades e tarefas do conjunto declarado de processos são orientações e não requisitos, independentemente da expressão ou forma verbal usada na disposição.

uma base para melhorias. Os usuários que pretendem avaliar e melhorar processos podem usar os resultados de processo escritos no presente documento como o "modelo de referência de processos" requerido pela ISO/IEC 33002.


### 4.2.2 Conformidade total com tarefas

Uma reivindicação de conformidade total declara o conjunto de processos para os quais a conformidade é reivindicada. A conformidade total com tarefas é alcançada pela demonstração que todos os requisitos

das atividades e tarefas do conjunto declarado de processos foram satisfeitos. Nesta situação, as disposições para os resultados do conjunto declarado de processos são orientações e não requisitos, independentemente da expressão ou forma verbal usada na disposição.

NOTA Uma reivindicação de conformidade total com tarefas pode ser apropriada em situações contratuais em que um adquirente ou um regulador requer um entendimento detalhado dos processos dos fornecedores.


## 4.3 Conformidade personalizada

Quando este documento é utilizado como base para estabelecer um conjunto de processos que não se qualificam para conformidade total, as seções deste documento são selecionadas ou modificadas de acordo com o processo de adaptação prescrito no Anexo A. O texto adaptado, para o qual a conformidade personalizada é reivindicada, é declarado. A conformidade personalizada é obtida pela demonstração de que foram alcançados os resultados, atividades e tarefas, conforme adaptados.


# 5 Conceitos-chaves e aplicação


## 5.1 Introdução

Esta seção é incluída para destacar e ajudar a explicar conceitos essenciais nos quais este documento se baseia.

NOTA Elaborações adicionais destes conceitos relativos à aplicação do gerenciamento do ciclo de vida podem ser encontradas nas ISO/IEC TS 24748-1, ISO/IEC TR 24748-2 e ISO/IEC TR 24748-3.


## 5.2 Conceitos de sistema de software


### 5.2.1 Sistemas de software

Os sistemas de software considerados neste documento são feitos, criados e utilizados por pessoas para fornecer produtos ou serviços em ambientes definidos para o benefício dos usuários e de outros stakeholders. Estes sistemas de software podem incluir os seguintes elementos de sistema: hardware, software, dados, pessoas, processos (por exemplo, processos para fornecer serviços aos usuarios), procedimentos (por exemplo, instruções do operador), instalações, serviços, materiais e entidades. Conforme vistos pelo usuário, eles são considerados produtos ou serviços.

Este documento se aplica a sistemas para os quais o software é de primordial importância para os stakeho/ders. Este documento é baseado nos princípios gerais da engenharia de sistemas e engenharia de software. É uma premissa fundamental deste documento que o software sempre exista no contexto de um sistema. Como o software não opera sem hardware, o processador no qual o software é executado pode ser considerado como parte do sistema. Como alternativa, o hardware ou serviços que hospedam o sistema de software e lidam com as comunicações com outros sistemas também podem ser vistos como sistemas habilitadores ou sistemas externos no ambiente operacional.

A percepção e a definição de um sistema de software específico, sua arquitetura e seus elementos dependem dos interesses e responsabilidades de um stakeholder. O sistema de interesse de um stakeholder pode ser visto como um elemento do sistema de interesse de outro stakeholder. Além disso, pode ser visto também como parte do ambiente de um sistema de interesse de outro stakeholder.

A seguir, são apresentados os principais pontos sobre as características de sistemas de interesse:

- a) limites definidos encapsulam necessidades significativas e soluções práticas;
- b) existem hierarquias ou outros relacionamentos entre os elementos do sistema;
- c) uma entidade em qualquer nível no sistema de interesse pode ser vista como um sistema;
- d) um sistema compreende um conjunto integrado e definido de elementos de sistema subordinados;
- e) pessoas podem ser vistas como usuários externos a um sistema e como elementos internos ao sistema (isto é, operadores); e
- f) um sistema pode ser visto isoladamente como uma entidade, isto é, um produto; ou como um conjunto de funções capazes de interagir com o ambiente ao seu redor, isto é, um conjunto de serviços.
Quaisquer que sejam os limites escolhidos para definir o sistema, os conceitos neste documento são genéricos e permitem correlacionar ou adaptar instâncias individuais dos ciclos de vida aos princípios de sistema de um profissional.


### 5.2.2 Estrutura de sistema de software

Os processos do ciclo de vida neste documento são descritos em relação a um sistema de software que é composto por um conjunto de elementos que interagem (incluindo elementos de software), cada um dos quais pode ser implementado para satisfazer os respectivos requisitos especificados (Figura 1). A responsabilidade pela implementação de qualquer elemento do sistema pode, portanto, ser delegada a outra parte por meio de um acordo.

Um sistema de software ...para alcançar um ou mais propósitos declarados e composto por um (dentro dos limites do conjunto de elementos sistema). de sistema interativos. incluindo elementos de Sistema de software... Software

Elemento de sistema Elemento de sistema Elemento de sistema de software A de software B de software C


**Figura 1 - Sistema de software e relacionamento entre seus elementos**

O relacionamento entre o sistema de software e o conjunto completo de seus elementos geralmente pode ser representado mostrando os relacionamentos entre os elementos - frequentemente descritos como uma hierarquia para o mais simples dos sistemas de interesse. A decomposição é uma abordagem para algumas atividades de software. Outras abordagens incluem a orientação a objetos, na qual os elementos do sistema são dispostos em um mesmo plano (não hierárquica), como em um diagrama de rede. Para sistemas de interesse de software mais complexos, pode ser necessário considerar um futuro elemento como um sistema (que por sua vez é composto por outros elementos) antes que um conjunto completo possa ser definido de forma confiável (Figura 2). Desta forma, os processos apropriados de ciclo de vida de sistema são aplicados recursivamente a um sistema de interesse para resolver sua estrutura, até que elementos compreensíveis e gerenciáveis do sistema de software possam ser implementados (criados, adaptados, adquiridos ou reutilizados).

Sistema de Software de Interesse

Sistema de Software Sistema Elemento do Sistema

Elemerto Elemento Sistema de Elemento Elemento Sistema de do Sistema do Sistema Software do Sistema Sotware Software

Elemento Elemento Elemento Sistema de Sistema Sistema Software Sotware Softvare Software

Elemento Elemento Elemento Elemento Elemento Elemento Elemento de Sistema Sotware de Sistema de Sistema Softvere Softvare de Sistema


**Figura 2 - Exemplo de estrutura de sistema de software de interesse**

Enquanto as Figuras 1 e 2 sugerem um relacionamento hierárquico, na realidade há um número crescente de sistemas que, em um ou mais aspectos, não são hierárquicos, como redes e outros sistemas distribuídos. O Anexo G discute o conceito de um sistema de sistemas (SoS).

NOTA A decomposição é uma atividade fundamental para muitas atividades de software. Nem todas as decomposições implicam a designação de novos elementos do sistema de software e a correspondente aplicação recursiva da atividade. A designação de um construto decomposto como um elemento é necessária apenas quando for apropriado aplicar diferentes requisitos, design ou atividades de implementação ao seu desenvolvimento. Um exemplo de situação que se aplica a decomposição é quando um elemento deve ser desenvolvido por outra organização. Outro exemplo é quando o gerenciamento determina que é adequado monitorar de forma independente o status do desenvolvimento ou customização do elemento.


### 5.2.3 Sistemas habilitadores

Ao longo do ciclo de vida de um sistema de interesse, são necessários serviços essenciais de sistemas que não fazem parte diretamente do seu ambiente operacional, por exemplo, sistema de modelagem, sistema de treinamento, sistema de manutenção. Cada um deles permite que Os denominados "sistemas habilitadores" facilitam a progressão do sistema de interesse ao longo uma parte, por exemplo, uma etapa do ciclo de vida do sistema de interesse seja conduzida.

do seu ciclo de vida.

O relacionamento entre os serviços entregues ao ambiente de operação pelo sistema de interesse e os serviços entregues pelos sistemas habilitadores ao sistema de interesse é mostrada na Figura 3. Como pode ser visto, os sistemas habilitadores contribuem indiretamente para os serviços fornecidos pelo sistema de interesse. As inter-relações entre o sistema de interesse e os sistemas habilitadores podem ser bidirecionais ou não. Além de interagir com os sistemas habilitadores, o sistema de interesse também pode interagir com outros sistemas no ambiente de operação, mostrados na Figura 3 como Sistemas A, B e C. Os requisitos para interfaces com sistemas habilitadores e outros sistemas no ambiente de operação estão incluídos nos requisitos do sistema de interesse.

Sistema B no ambiente operacional

Sistema de Sistema de software A software C no ambiente no ambiente operacional operacional

Interação com sistemas que formamo ambiente operacional Sistema Habilitador de Software

Sistem a de software de interes se Sistema Habilitador

Interação com sistemas habilitadores Sistema Habilitador de Software Z


**Figura 3 - Sistema de interesse de software, seu ambiente de operação e sistemas habilitadores**

Durante uma etapa do ciclo de vida do software, os sistemas habilitadores relevantes e o sistema de interesse são considerados em conjunto. Uma vez que são interdependentes, também podem ser vistos como um sistema. Quando um sistema habilitador adequado ainda não existe, o projeto responsável pelo sistema de interesse pode ser diretamente responsável pela criação e uso do sistema habilitador. A criação do sistema habilitador pode ser vista como um projeto separado e, posteriormente, como outro sistema de interesse.

Uma elaboração mais aprofundada destes conceitos pode ser encontrada na ISO/EC/EEE 24748 (todas as partes) sobre a aplicação dos processos do ciclo de vida.

NOTA Sistemas habilitadores no desenvolvimento de software incluem ambientes de desenvolvimento e teste de software para plataformas alvo.


### 5.2.4 Processos do ciclo de vida para o sistema de software

No sistema de software, os processos de requisitos, arquitetura e design no nível do sistema resultam em uma alocação dos requisitos de sistema a vários elementos. O sistema de software de interesse é implementado principalmente pela análise dos requisitos, da arquitetura e do design do sistema de software e pela determinação de quais funções serão implementadas no software ou por outros elementos, implementando-os e integrando-os como um sistema. Portanto, um produto ou serviço de software pode ser tratado como um elemento de um sistema de software.

Em alguns casos, a definição da arquitetura de um sistema de software pode indicar que é adequado considerá-lo como um conjunto de elementos subordinados distintos. Cada um dos elementos do software, por sua vez, pode ser tratado como um sistema de software distinto, conforme descrito anteriormente. Nestes casos, este documento pode ser aplicado recursivamente para adquirir

Este documento possui uma forte relação com a ISO/IEC/IEEE 15288:2015, Systems and Software Engineering--System Life Cycle Processes, e é mais aplicável a sistemas de software. Para contemplar situações nas quais são aplicadas a ISO/IEC/IEEE 15288:2015 e a ABNT NBR ISO/IEC/IEEE 12207:2021 (por exemplo, o desenvolvimento de um sistema que contém software ou o desenvolvimento de um sistema de software que contém hardware), suas estruturas de processos estão harmonizadas para serem idênticas. Os processos deste documento correspondem diretamente aos processos da ISO/IEC/IEEE 15288:2015, com especialização para produtos e serviços de software.

No caso em que os elementos de importância primordial do sistema não sejam software, uma organização pode decidir aplicar a ISO/EC/EEE 15288 para executar os processos, atividades e tarefas apropriados do ciclo de vida. Para cada elemento de software do sistema, a organização pode aplicar este documento para criar, adaptar, adquirir ou reutilizar os elementos de software.


## 5.3 Conceitos de organização e projeto


### 5.3.1 Organizações

Quando uma organização, como um todo ou uma parte, participa de um acordo, por vezes é chamada de "parte" para o acordo. As partes podem ser da mesma organização ou de organizações distintas. Uma organização pode ser tão pequena quanto um único indivíduo, se lhe forem atribuídas responsabilidades e autoridades.

Em termos informais, a organização responsável pela execução de um processo às vezes é referenciada pelo nome deste processo. Por exemplo, a organização que executa o Processo de Aquisição às vezes é chamada de adquirente*. Outros exemplos incluem fornecedor, implementador, mantenedor e operador.

Outros termos também são aplicados às organizações neste documento: 'usuário" pode ser a organização ou indivíduos que se envolvem diretamente ou se beneficiam com a utilização do produto ou serviço; "cliente" refere-se ao usuário e adquirente coletivamente; e "stakeholder' refere-se a um indivíduo ou organização com interesse no sistema.

Os processos e organizações estão relacionados apenas funcionalmente. Este documento não impõe ou implica uma estrutura para uma organização, nem define que determinados processos sejam executados por partes específicas da organização. É de responsabilidade da organização que implementa este documento definir uma estrutura adequada para si mesma e atribuir papéis apropriados para a execução dos processos.

Os processos neste documento formam um conjunto abrangente para atender a várias organizações. Uma organização, pequena ou grande, dependendo de seu objetivo de negócio ou de sua estratégia de aquisição, pode selecionar um conjunto apropriado de processos (atividades e tarefas associadas) para atender a este propósito. Uma organização pode executar um ou mais processos.

Este documento é destinado para ser aplicado internamente por uma organização ou externamente por duas ou mais organizações. Quando aplicado internamente, as duas partes envolvidas geralmente agem sob os termos de um acordo que pode variar em formalidade para circunstâncias diferentes. Quando aplicado externamente, as duas partes envolvidas geralmente agem sob os termos de um acordo. Este documento usa o termo "acordo" para ambas as situações.

Para o propósito deste documento, assume-se que qualquer projeto é conduzido no contexto de uma organização. Isto é importante, porque um projeto depende de vários resultados produzidos pelos processos de negócios da organização, por exemplo, funcionários para a equipe do projeto e instalações para abrigar o projeto. Para este propósito, este documento fornece um conjunto de processos "Organizacionais Habilitadores de Projetos". Não se pode assumir que estes processos sejam adequados para operar um negócio; em vez disso, os processos, considerados como uma coleção, destinam-se a declarar o conjunto mínimo de dependências que o projeto requer da organização.


### 5.3.2 Adoção em nível de projeto e organização

Os negócios modernos se esforçam para desenvolver um conjunto robusto de processos de ciclo de vida que são aplicados repetidamente aos projetos e serviços do negócio. Portanto, este documento pretende ser útil para adoção tanto no nível da organização quanto do projeto. Uma organização pode adotar o documento e complementá-lo com procedimentos, práticas, ferramentas e políticas apropriados. Por sua vez, um projeto geralmente está em conformidade com os processos da organização, em vez de estar em conformidade direta com este documento.

Em alguns casos, os projetos podem ser executados por uma organização que não possui um conjunto adequado de processos adotados em nível organizacional. Este projeto pode aplicar as disposições deste documento diretamente no projeto.


## 5.4 Conceitos do ciclo de vida


### 5.4.1 Fases do ciclo de vida de software

Os ciclos de vida variam de acordo com a natureza, propósito, uso e circunstâncias predominantes do sistema de software. O uso de fases simultaneamente e em diferentes ordens pode levar a formas de ciclo de vida com características distintas. Cada fase tem um propósito e uma contribuição distintos para o planejamento e execução de todo o ciclo de vida do sistema de software. De acordo com a ISO/IEC TS 24748-1, as fases típicas do ciclo de vida de sistema incluem concepção, desenvolvimento, produção, utilização, suporte e desativação. O uso destes termos para definir fases não é normativo. Um conjunto comum de fases para um sistema de software é concepção, exploração, desenvolvimento, manutenção e desativação, com transições entre fases para o sistema como um todo e para seus elementos.

As fases correspondem aos principais períodos do ciclo de vida de um sistema de software e estão relacionadas à situação do próprio sistema de software ou sua descrição. As fases descrevem os principais marcos de realização e progresso do sistema de software ao longo de seu ciclo de vida. Elas dão origem aos principais pontos de decisão do ciclo de vida. Estes pontos de decisão são usados pelas organizações para entender e gerenciar as incertezas e riscos inerentes associados aos custos, cronograma e funcionalidades ao criar ou utilizar um sistema de software. O uso de fases provê

às organizações uma estrutura na qual o gerenciamento da organização tem visibilidade e controle de alto nível dos processos técnicos e do projeto. As organizações definem e utilizam fases de maneira diferente para satisfazer as estratégias de negócio e de mitigação de riscos.

Os processos do ciclo de vida definidos neste documento não estão vinculados a nenhuma fase específica do ciclo de vida de software. Todos os processos do ciclo de vida envolvem atividades de planejamento, execução e avaliação que convém que sejam consideradas para uso em todas as fases.

Um aprofundamento destes conceitos pode ser encontrado na ISO/EC/EEE 24748 (todas as partes), sobre a aplicação do gerenciamento do ciclo de vida.


### 5.4.2 Modelo de ciclo de vida para sistema de software

Todo sistema de software tem um ciclo de vida. Um ciclo de vida pode ser descrito usando um modelo funcional abstrato que representa a conceituação de uma necessidade do sistema, sua realização, utilização, evolução e desativação.

Um sistema de software evolui no seu ciclo de vida como resultado de ações das atividades dos processos. Estas ações são executadas e gerenciadas por pessoas nas organizações. Os detalhes no modelo de ciclo de vida são expressos em termos destes processos, seus resultados, relacionamentos e sequência.

Este documento não prescreve nenhum modelo de ciclo de vida específico. Em vez disso, define um conjunto de processos, denominados processos do ciclo de vida, que podem ser usados na definição do ciclo de vida do sistema. Além disso, este documento não prescreve nenhuma sequência específica de processos dentro do modelo de ciclo de vida. A sequência dos processos é determinada pelos objetivos do projeto e pela seleção do modelo de ciclo de vida. Muitas vezes, a fase de desenvolvimento é subdividida de formas diferentes e mais detalhada.

Um conjunto, frequentemente mencionado de fases de desenvolvimento de software, é elicitação, requisitos, design, construção e teste - do modelo preditivo ou cascata". Se as fases forem consideradas sequenciais, será necessário que cada fase produza resultados corretos antes de prosseguir para a próxima fase. Na prática, isto é extremamente difícil de alcançar, a menos que os requisitos sejam bem conhecidos e as estimativas iniciais de custo sejam precisas. Ao executar um ciclo cascata, existe o risco de se ter muito retrabalho que não se enquadra adequadamente em nenhuma das fases planejadas e, portanto, provavelmente não se enquadra em nenhum orçamento.

NOTA 1 Winston Royce, comumente reconhecido como um dos primeiros analistas dos modelos de processo do ciclo de vida, descreveu a necessidade de fases de retrabalho em vez de cascata (um termo que ele não usou). Infelizmente, as etapas de retrabalho foram retiradas do modelo "cascata", como era popularmente entendido.

Para lidar com questões de requisitos parcialmente conhecidos e estimativas imprecisas, vários outros tipos de modelos foram propostos: incremental, espiral, iterativo e evolutivo (adaptativo). Estes modelos de ciclo de vida podem incorporar técnicas e métodos ágeis. Estes modelos geralmente podem envolver desempenho repetido dos processos e fases do ciclo de vida durante o ciclo de vida, por exemplo, para diferentes incrementos do produto de software, para tratamento mais preciso de exceções a funções comuns ou para requisitos que não foram totalmente definidos desde o início. Estes modelos podem ser aplicados em fases, como desenvolvimento e utilização ou implantação. O uso destes modelos pode afetar as estratégias de liberação de software e as estratégias de aquisição para serviços de software.

EXEMPLO Os elementos de software podem ser desenvolvidos de forma incremental e mantidos para liberação operacional do bloco em um momento oportuno no ciclo de negócios da organização.

O modelo de "desenvolvimento incremental" inclui planejamento inicial, análise de requisitos iniciais, definição de arquitetura inicial e validação inicial, mas aloca atividades de design, implementação, verificação (e às vezes entrega) para uma série de fases, cada uma das quais fornece uma parte da funcionalidade pretendida. A abordagem fornece alguma flexibilidade para responder a estimativas imprecisas de custo ou cronograma, movendo a funcionalidade para incrementos posteriores.

A variação "espiral no desenvolvimento incremental propõe ordenar o desenvolvimento da funcionalidade com base no risco, com os problemas mais arriscados considerados nos incrementos iniciais. Isto fornece alguma proteção contra surpresas de custo que ocorrem no final do ciclo de desenvolvimento.

O modelo de "desenvolvimento iterativo realiza o planejamento inicial e, em seguida, consiste em um processo ciclico de prototipagem, teste, análise e refino dos requisitos e da solução. Os modelos "¡terativos" executam repetidamente os processos do ciclo de vida para fornecer funções prioritárias do sistema mais cedo, com elementos refinados ou mais complexos do sistema em iterações posteriores.

O "modelo evolutivo" tem como objetivo lidar com o conhecimento incompleto dos requisitos. Ele fornece planejamento inicial e definição inicial da arquitetura, mas aloca análise de requisitos, design, construção, verificação, validação e entrega em uma série de fases. As funcionalidades entregues que não atendem às necessidades do usuário podem ser reformuladas nas fases subsequentes da evolução.

Os métodos ágeis podem realmente ser aplicados em uma variedade de modelos. Embora os métodos ágeis sejam comuns na execução de um modelo de ciclo de vida evolutivo, eles podem ser usados em outros modelos de ciclo de vida, em várias fases. O que os métodos têm em comum é a ênfase na inspeção e colaboração contínuas na produção rápida de software em funcionamento em um ambiente em que mudanças são esperadas, incluindo mudanças nos requisitos. O Anexo H fornece informações sobre a aplicação deste documento em um contexto ágil.

NOTA 2 A seleção do nome de um tipo de modelo não atende ao requisito de definir um modelo composto por fases, com finalidade e resultados definidos, alcançados por meio dos processos deste documento.

NOTA 3 As ISO/IEC TS 24748-1, ISO/IEC TR 24748-2, ISO/IEC TR 24748-3 e ISO/EC/IEEE 24748-4 fornecem detalhes adicionais sobre modelos e fases do ciclo de vida. Os modelos descritos nesta seção se aplicam não apenas aos sistemas de software, mas também a outros sistemas, conforme descrito na ISO/IEC/IEEE 15288: 2015.


## 5.5 Conceitos do processo


### 5.5.1 Critérios para processos

A determinação dos processos do ciclo de vida neste documento é baseada em três princípios básicos:

- 1) Cada processo do ciclo de vida tem fortes relações entre seus resultados, atividades e tarefas.
- 2) As dependências entre os processos são reduzidas ao mínimo possível.
- 3) Um processo é capaz de ser executado por uma única organização no ciclo de vida.

### 5.5.2 Descrição de processos

Cada processo deste documento é descrito em termos dos seguintes atributos:

- a) O titulo transmite o escopo do processo como um todo.
- b) O propósito descreve os objetivos de executar o processo.
- c) Os resultados expressam os resultados observáveis esperados do desempenho bem-sucedido do processo.
- d) As atividades são conjuntos de tarefas coesas de um processo.
- e) As tarefas são requisitos, recomendações ou ações admissíveis destinadas a apoiar a consecução dos resultados.
Os processos e grupos de processos neste documento têm objetivos e resultados idênticos aos da ISO/IEC/IEEE 15288:2015, System and software engineering - System life cycle processes, com uma exceção: o processo de Definição de Requisitos de Sistema/Software deste documento é renomeado do processo de Definição de Requisitos do Sistema da ISO/IEC/IEEE 15288:2015. Para enfatizar esta harmonização de sistemas e processos de sistemas de software, os propósitos e resultados do processo são apresentados nas caixas da Seção 6.

Atividades, tarefas e produtos de trabalho específicos de software são aplicados para alcançar os resultados dos processos neste documento. O Anexo E fornece visões adicionais de processo.

Detalhes adicionais sobre esta forma de descrição de processo podem ser encontrados no ISO/IEC TR 24774.


### 5.5.3 Características gerais de processos

Além dos atributos básicos descritos na subseção anterior, os processos podem ser caracterizados por outros atributos comuns a todos os processos. A ISO/IEC 33020:2015 identifica atributos comuns de processo que caracterizam seis níveis de realização em um framework de medição para a capacidade de processo. O Anexo C inclui a lista de atributos de processo que contribuem para a obtenção de níveis mais altos de capacidade de processo, conforme definido na ISO/IEC 33020:2015.


### 5.5.4 Adaptação

O Anexo A, que é normativo, define as atividades básicas necessárias para realizar a adaptação. Observar que a adaptação pode diminuir o valor percebido de uma solicitação de conformidade com este documento. Isto ocorre porque é difícil para outras organizações entender até que ponto a adaptação pode ter excluído as disposições desejáveis. Uma organização que reivindique uma solicitação de conformidade de uma única parte com este documento pode achar vantajoso solicitar conformidade total com uma lista menor de processos, em vez de conformidade adaptada com uma lista maior de processos.


## 5.6 Grupos de processo


### 5.6.1 Introdução

Este documento agrupa as atividades que podem ser executadas durante o ciclo de vida de um sistema de software em quatro grupos de processos. Cada um dos processos do ciclo de vida destes grupos é descrito em termos de sua finalidade e resultados desejados, com um conjunto de atividades e tarefas relacionadas que podem ser executadas para alcançar estes resultados. Os quatro grupos de processos e os processos incluídos em cada grupo estão representados na Figura 4 da seguinte

- a) processos de Acordo;
- b) processos Organizacionais Habilitadores de Projeto;
- c) processos de Gerenciamento Técnico; e
- d) processos Técnicos.
Os processos descritos neste documento não se destinam a impedir ou desencorajar o uso de processos adicionais que as organizações considerem úteis. A ordem das subseções em que os processos são definidos neste documento não determina a ordem em que os processos são executados durante o ciclo de vida do sistema ou em qualquer uma de suas fases. Uma descrição de cada grupo de processos é fornecida nas quatro subseções a seguir.

Processos do Ciclo de Vida de Software

Processos de Acordo Processos de Processos Técnicos Gerenciamento Técnico Processo de Planejamento Processo de Analise Processo de Aquisição (6.1.1) de Projeto (6.3.1) de Negócio (6.4.1)

Processo de Fornecimento (6.1.2) Processo de Avaliação e Controle Processo de Definição de de Projeto (6.3.2) Necessidades e Requisitos dos Stakeholders (6.4.2) Processos Processo de Gerenciamento de Processo de Definição de Decisão (6.3.3) Requisitos de Organizacionais Sistema/Software (6.4.3) Habilitadores de Projeto Processo de Gerenciamento Processo de Definição de Processo de Gerenciamento de de Risco (6.3.4) Arquitetura (6.4.4) Modelo de Ciclo de Vida (6.2.1)

Processo de Gerenciamento de Processo de Definição Processo de Gerenciamento Configuração (6.3.5) de Design (6.4.5) de Infraestrutura (6.2.2)

Processo de Gerenciamento da Processo de Análise Processo de Gerenciamento de Informação (6.3.6) de Sistema (6.4.6) Portfólio (6.2.3)

Processo de Medição Processo de Implementação Processo de Gerenciamento de (6.4.7) Recursos Humanos (6.2.4) (6.3.7)

Processo de Garantia da Qualidade Processo de Integração Processo de Gerenciamento (6.3.8) (6.4.8) da Qualidade (6.2.5) Processo de Verificação Processo de Gerenciamento (6.4.9) de Conhecimento (6.2.6)

Processo de Transição (6.4.10)

Processo de Validação (6.4.11)

Processo de Operação (6.4.12)

Processo de Manutenção (6.4.13)

Processo de Desativação (6.4.14)


**Figura 4 - Processos do ciclo de vida de software**


### 5.6.2 Processos de Acordo

As organizações são produtoras e usuárias de sistemas de software. Uma organização (atuando como adquirente) pode encarregar outra (atuando como fornecedor) de produtos ou serviços. Isto é alcançado usando acordos. Os acordos permitem que adquirentes e fornecedores percebam valor e apoiem estratégias de negócios para suas organizações.

Os Processos de Acordo são processos organizacionais que se aplicam fora do período de vida de um projeto, bem como pela vida útil do projeto. Geralmente, as organizações agem simultaneamente ou sucessivamente como adquirentes e fornecedores de sistemas de software. Os Processos de Acordo podem ser usados com menos formalidade quando o adquirente e o fornecedor estão na mesma organização. Da mesma forma, eles podem ser usados dentro da organização para concordar com as respectivas responsabilidades da organização, projeto e funções técnicas. A Figura 4 lista os processos contidos neste grupo de processos.


### 5.6.3 Processos Organizacionais Habilitadores de Projeto

Os Processos Organizacionais Habilitadores de Projeto se encarregam de fornecer os recursos para permitir que o projeto atenda às necessidades e expectativas dos stakeholders da organização. Os Processos Organizacionais Habilitadores de Projeto, tipicamente, estão relacionados ao nível estratégico com a gestão e melhoria dos negócios ou empreendimento da organização, com o fornecimento e a disponibilização de recursos e ativos e com a gestão de riscos em situações de incertezas e concorrência. Os Processos Organizacionais Habilitadores de Projeto se aplicam fora do ciclo de vida de um projeto, bem como durante a execução do projeto.

Os Processos Organizacionais Habilitadores de Projeto estabelecem o ambiente em que os projetos são conduzidos. A organização estabelece os processos e modelos de ciclo de vida a serem usados pelos projetos; estabelece, redireciona ou cancela projetos; fornece os recursos necessários, incluindo recursos humanos e financeiros; e define e monitora as medidas de qualidade para sistemas de software e outros entregáveis que são desenvolvidos pelos projetos para clientes internos e externos.

Os Processos Organizacionais Habilitadores de Projeto criam uma forte imagem de negócio para muitas organizações e implicam na motivação para os negócios e na lucratividade. No entanto, os Processos Organizacionais Habilitadores de Projeto são igualmente relevantes para organizações sem fins lucrativos, uma vez que também são adequados para os stakeholders porque são responsáveis por recursos e endereçam riscos para os seus empreendimentos. Este documento pode ser aplicado a organizações com ou sem fins lucrativos. A Figura 4 lista os processos contidos neste grupo de processos.


### 5.6.4 Processos de Gerenciamento Técnico

Os Processos de Gerenciamento Técnico se encarregam em gerenciar os recursos e ativos alocados pela gerência organizacional e utilizá-los para atender aos acordos feitos dentro da organização ou entre organizações. Os Processos de Gerenciamento Técnico estão relacionados ao esforço técnico nos projetos, em particular ao planejamento em termos de custo, prazos e compromissos, à verificação das as ações que contribuem para garantir que sejam cumpridos os planos e às metas de desempenho; à identificação e à seleção de ações corretivas para recuperar desvios no progresso e nos compromissos do projeto. Estes processos são usados para estabelecer e executar planos técnicos para o projeto, gerenciar informações para a equipe técnica, avaliar o progresso técnico em relação aos planos do sistema, produtos ou serviços de software, controlar tarefas técnicas até a conclusão e auxiliar na tomada de decisões.

NOTA 1 A gerenciamento técnico é "a aplicação de recursos técnicos e administrativos para planejar, organizar e controlar as funções de engenharia". (ISO/IEC/IEEE 24765: 2010)

Normalmente, vários projetos coexistem em qualquer organização. Os Processos de Gerenciamento Técnico podem ser utilizados em nível corporativo para atender às necessidades internas. A Figura 4 lista os processos contidos neste grupo de processos.

NOTA 2 Os Processos de Gerenciamento Técnico são aplicados durante a execução de cada processo técnico.


### 5.6.5 Processos Técnicos

Os Processos Técnicos se encarregam das ações técnicas por meio do ciclo de vida. Os Processos Técnicos transformam as necessidades dos stakeholders em produtos ou serviços. Usando este produto ou operando este serviço, os Processos Técnicos fornecem desempenho sustentável, quando e onde necessário, a fim de atender aos requisitos dos stakeholders e alcançar a satisfação do cliente. Os Processos Técnicos são usados para criar e usar um sistema de software, seja na forma de um protótipo ou de um produto operacional. Os Processos Técnicos são usados em qualquer nível hierárquico da estrutura do sistema de software e em qualquer estágio do ciclo de vida. A Figura 4 lista os processos contidos neste grupo de processos.


## 5.7 Aplicação do processo

Os processos do ciclo de vida definidos neste documento podem ser usados por qualquer organização ao adquirir, usar, criar ou fornecer um sistema de software. Eles podem ser aplicados em qualquer nível na hierarquia de um sistema e em qualquer estágio do ciclo de vida.

As funções que estes processos executam são definidas em termos de propósitos específicos, resultados e um conjunto de atividades e tarefas que constituem o processo.

Cada processo do ciclo de vida na Figura 4 pode ser chamado, conforme necessário, a qualquer momento durante todo o ciclo de vida. A ordem em que os processos são apresentados neste documento não implica nenhuma ordem prescritiva no seu uso. Entretanto, os relacionamentos sequenciais dos processos são estabelecidos pela definição de um modelo de ciclo de vida. O propósito detalhado e a hora em que estes são utilizados ao longo do ciclo de vida são influenciados por vários fatores, incluindo as considerações sociais, comerciais, organizacionais e técnicas. Estas considerações podem ser diferentes ao longo da vida de um sistema de software. Um ciclo de vida de software próprio é criado por meio da seleção e aplicação de processos que, normalmente, podem ser concorrentes, iterativos, recursivos ou dependentes do tempo.

O uso concorrente de processos pode existir em um projeto (por exemplo, quando ações de design e ações para construir um sistema de software são executadas simultaneamente) e entre projetos (por exemplo, quando os elementos do sistema são projetados ao mesmo tempo sob diferentes responsabilidades do projeto)

Quando o uso do mesmo processo ou do conjunto de processos é repetido no mesmo sistema, este uso é referenciado como iterativo. O uso iterativo de processos é importante para o aprimoramento progressivo das saídas do processo, por exemplo, a interação entre ações sucessivas de verificação e ações de integração pode incrementalmente aumentar a confiança na conformidade do produto. Iterações com falhas também são esperadas. Novas informações são criadas pelo uso de um processo ou conjunto de processos. Normalmente, estas informações assumem a forma de perguntas com relação aos requisitos, análise de riscos ou oportunidades. Convém que tais questões sejam resolvidas antes da conclusão das atividades de um processo ou conjunto de processos.

O uso recursivo de processos, isto é, o uso repetido do mesmo processo ou conjunto de processos usado em níveis sucessivos de elementos do sistema na estrutura de um sistema, é um aspecto

chave na utilização deste documento. As saídas dos processos em qualquer nível, sejam informações, artefatos ou serviços, são entradas para os processos utilizados no nível abaixo (por exemplo, durante o design top-down) ou no nivel acima (por exemplo, durante a realização do sistema de software). As saídas de uma aplicação são usadas como entrada para o nível mais baixo (ou superior) do sistema na estrutura do sistema para chegar a um conjunto de resultados mais detalhado ou maduro. Esta abordagem agrega valor a sistemas sucessivos na estrutura do sistema.

As mudanças usuais que influenciam o sistema de software (por exemplo, mudanças no ambiente operacional, novas oportunidades para a implementação de elemento do sistema, estrutura e responsabilidades alteradas nas organizações) requer uma análise crítica contínua da seleção e de quando o processo será utilizado. O uso do processo no ciclo de vida pode ser dinâmico, respondendo às muitas influências externas no sistema de software. A abordagem do ciclo de vida também permite incorporar mudanças no próximo estágio. Os estágios do ciclo de vida auxiliam no planejamento, execução e gerenciamento dos processos do ciclo de vida pelo fornecimento e reconhecimento da estrutura e propósito de alto nivel mediante a complexidade que são os ciclos de vida. O conjunto de processos em um estágio do ciclo de vida é aplicado com o objetivo comum de satisfazer os critérios de saída para este estágio ou os critérios de entrada das análises críticas formais de progresso dentro deste estágio.

A discussão nesta seção sobre o uso iterativo e recursivo dos processos do ciclo de vida do software não implica na definição de uma estrutura hierárquica, vertical ou horizontal específica para o projeto, organização, sistema de apoio ou sistema de interesse.

Quando justificado em razão dos riscos de qualidade do produto, descrições detalhadas das instâncias dos processos no contexto de um produto específico podem ser criadas. A instanciação dos processos envolve identificar critérios de sucesso específicos para uma instância do processo, relacionadas aos requisitos do produto, identificando as atividades e tarefas específicas necessárias para atender ao critério de sucesso, que são derivadas das atividades e tarefas identificadas neste documento. A criação de uma descrição detalhada das instâncias do processo endereça para uma melhor gestão de riscos de qualidade do produto por estabelecer uma correlação entre os processos e os requisitos específicos do produto.

Um detalhamento mais aprofundado destes conceitos pode ser encontrado na ISO/IEC/IEEE 24748 (todas as partes) sobre o uso dos processos do ciclo de vida.


## 5.8 Modelo de referência de processo

O Anexo C define um modelo de referência de processo (PRM) em um nível de abstração maior que o dos requisitos detalhados na Seção 6. O PRM é aplicável a uma organização que está avaliando seus processos para determinar a capacidade destes processos. O propósito e os resultados são uma declaração dos objetivos do desempenho de cada processo. Esta declaração de objetivos permite avaliar a eficácia dos processos de outras formas, não somente a simples avaliação da conformidade.

Neste documento, o termo modelo de referência de processo é usado com o mesmo significado da ISO/IEC 33001: 2015: "modelo que compreende definições de processos em um domínio de aplicação descrito em termos de propósito e resultados do processo, juntamente com uma arquitetura descrevendo as relações entre os processos".


# 6 Processos do Ciclo de Vida de Software


## 6.1 Processos de Acordo

Esta subseção especifica os requisitos para o estabelecimento de acordos com organizações externas e internas à organização.

Os Processos de Acordo são os seguintes:

- a) Processo de Aquisição - usado pelas organizações para adquirir produtos ou serviços; e
- b) Processo de Fornecimento - usados pelas organizações para fornecer produtos e serviços.
Estes processos definem as atividades necessárias para estabelecer um acordo entre duas organizações. Se o Processo de Aquisição for utilizado, ele fornecerá os meios para conduzir negócios com um fornecedor. Isto pode incluir produtos fornecidos para uso como um sistema de software operacional, serviços de suporte às atividades operacionais, elementos de software de um sistema ou elementos de um sistema de software fornecidos por um fornecedor. Se o Processo de Fornecimento for acionado, ele fornecerá os meios para um acordo no qual o resultado é o produto ou serviço que será entregue ao adquirente.

A segurança é uma preocupação crescente em engenharia de sistemas e de software. Ver a ISO/IEC 27036, Security techniques - Information security for supplier relationships, para obter requisitos e orientações para fornecedores e adquirentes de como proteger as informações quando do relacionamento com fornecedores. Aspectos específicos de segurança da informação no relacionamento dos fornecedores


### 6.1.1 Processo de Aquisição


#### 6.1.1.1 Propósito

O propósito do Processo de Aquisição é obter um produto e/ou serviço de acordo com os requisitos do adquirente.

NOTA Como parte deste processo, o acordo pode ser modificado, se tiver a concordância do adquirente e fornecedor, quando existir uma solicitação de mudança que afeta os termos do acordo.


#### 6.1.1.2 Resultados esperados

Como resultado da implementação bem-sucedida do Processo de Aquisição:

- a) Uma solicitação de fornecimento é preparada.
- b) Um ou mais fornecedores estão selecionados.
- c) Um acordo é estabelecido entre o adquirente e o fornecedor.
- d) Os produtos ou serviços em conformidade com o acordo são aceitos.
- e) Obrigações definidas para o adquirente no acordo são satisfeitas.

#### 6.1.1.3 Atividades e tarefas

O adquirente deve implementar as atividades a seguir, de acordo com as políticas e procedimentos organizacionais que se apliquem ao Processo de Aquisição.

NOTA 1 As atividades e o acordo resultante deste processo geralmente se aplicam aos fornecedores da cadeia de suprimentos, incluindo fornecedores subcontratados.

NOTA 2 A IEEE Std 1062-2015, IEEE Recomended Practice for Software Acquisition, contém atividades detalhadas para alternativas de aquisição de software, incluindo desenvolvimento personalizado (software

sob medida), pronto para uso (pacotes) e software como serviço. A IEEE Std 1062-2015 também fornece diretrizes de aquisição de software e listas de verificação de problemas relevantes que a organização pode utilizar no Processo de Aquisição quando existe preocupação com a garantia de segurança ou requisitos de segurança da informação.

- a) Preparação para a aquisição. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir uma estratégia para condução da aquisição
NOTA 1 Esta estratégia descreve ou faz referência ao modelo de ciclo de vida, mitigação de riscos e problemas, um cronograma de marcos e critérios de seleção se o fornecedor for externo à organização adquirente. Também inclui os principais fatores e características da aquisição, como responsabilidades e obrigações; modelos, métodos ou processos específicos; nível de criticidade; formalidade; e prioridade para questões comerciais relevantes.

O Processo de Gerenciamento de Decisão e o de Análise de Sistema são frequentemente usados para trade-off na definição da estratégia de aquisição. Os exemplos incluem: determinar uma decisão de fazer ou comprar, bem como a adequação de soluções específicas de COTS (Commercial-Off-The-Shelf) ou OTS (Off-The-Shelf Software) modificado e avaliação de fornecedores.

NOTA 3 Se a estratégia exigir a aquisição de software comercial pronto (pacote de software) específico ou software de código aberto, a aquisição pode se limitar a identificar o fornecedor, aceitar ou negociar as condições predefinidas no acordo de licença, uso ou manutenção, determinando direitos à propriedade intelectual e direitos de dados no sistema de software e também o preço.

NOTA 4 Um fator a considerar em acordos entre fornecedores é o direito sobre os dados e o acesso lateral a dados constituintes e à propriedade intelectual. Como exemplo, os fornecedores de um componente do sistema podem precisar colaborar com os fornecedores de outro componente e compartilhar o código-fonte. Os acordos podem permitir esta colaboração.

  - 2) Preparar uma solicitação para o fornecimento de um produto ou serviço que inclua os requisitos.
NOTA 1 Se um fornecedor é externo à organização, a solicitação inclui as práticas de negócios que espera-se que o fornecedor cumpra e os critérios para a seleção do fornecedor.

NOTA 2 Uma definição de requisitos é fornecida a um ou mais fornecedores. Os requisitos são requisitos dos stakeholders ou de sistema/software, dependendo do tipo de abordagem de aquisição, e utilizando-se o processo de definição de requisitos associado.

NOTA 3 O adquirente desenvolve os requisitos por si mesmo ou contrata um fornecedor para desenvolvê-los. Se o adquirente contratar um fornecedor para desenvolver os requisitos, o próprio adquirente necessita manter a autoridade para aprovar os requisitos desenvolvidos pelo fornecedor.

- b) Comunicar a aquisição e selecionar o fornecedor. Esta atividade consiste nas seguintes tarefas:
  - 1) Comunicar a solicitação de fornecimento de um produto ou serviço para os potenciais fornecedores; e
  - 2) Selecionar um ou mais fornecedores.
NOTA Para obter respostas competitivas, as propostas de fornecimento são avaliadas e comparadas com os critérios de seleção e classificadas. A justificativa para classificar cada proposta é declarada e os fornecedores, geralmente, são informados sobre o motivo pelo qual foram ou não selecionados.

- c) Estabelecer e manter um acordo. Esta atividade consiste nas seguintes tarefas:
O custo, o cronograma e a execução do projeto são monitorados por meio do Processo de Avaliação e Controle de Projeto. Quaisquer questões identificadas que requeiram modificações no acordo são direcionadas para esta atividade. Quaisquer propostas de alterações nos elementos ou informações do sistema são controladas por meio da atividade Gerenciar Mudanças do Processo de Gerenciamento de Configuração.

  - 1) Desenvolver um acordo com o fornecedor que inclua critérios de aceitação.
Este acordo varia em formalismo, de um acordo formal (contrato) a um acordo verbal. Conforme o nível de formalismo, o acordo estabelece requisitos, marcos de desenvolvimento e entrega, condições para verificação, validação e aceitação, procedimentos de tratamento de exceções, de gerenciamento de mudanças no acordo e os cronogramas de pagamento, para que as partes que compõem o acordo compreendam as bases da sua execução. Outras disposições para os acordos incluem direitos e restrições associados a dados técnicos e propriedade intelectual, preparação de testes de aceitação e detalhes do ambiente de teste, além do grau de envolvimento do fornecedor. O acordo identifica os requisitos de processo que precisam ser impostos aos participantes subcontratados, como requisitos de gerenciamento de configuração, comunicação de riscos e de medidas, e análise de medições.

Critérios de aceitação, como testes de aceitação, referem-se a como o produto ou serviço satisfará o uso pretendido no seu ambiente de operação. Testes de aceitação podem ser realizados usando o Processo de Validação. As exceções que surgirem durante a execução do acordo ou após o produto ou serviço ser entregue são resolvidas seguindo os procedimentos estabelecidos

  - 2) Identificar mudanças necessárias no acordo.
NOTA Ao solicitar uma alteração no acordo, o adquirente ou o fornecedor detalha suas especificações, fundamentação e histórico.

  - 3) Avaliar o impacto nas mudanças do acordo.
NOTA Qualquer mudança é analisada em relação ao seu impacto nos planos do projeto, no cronograma, nos custos, na capacidade técnica e na qualidade. Uma mudança pode ser tratada dentro do acordo existente, exigir uma alteração no acordo ou um novo acordo.

  - 4) Negociar o acordo com o fornecedor.
Os termos do acordo são negociados entre o adquirente e o fornecedor. A negociação ocorre para o acordo inicial e, conforme necessário, para as suas alterações. Os acordos alterados são baseados nas mudanças necessárias e nos impactos identificados. Os detalhes são discutidos e alterados durante a negociação, após a qual o adquirente e o fornecedor aceitam os termos do acordo e inicia-se a sua execução. Para um acordo escrito, a sua execução ocorre quando ele é assinado ou conforme especificado no próprio acordo.

  - 5) Atualizar o acordo com o fornecedor, conforme necessário.
NOTA 1 O resultado da alteração do acordo é incorporado aos planos do projeto e comunicado a todas as partes envolvidas.

NOTA 2 Os acordos podem especificar as condições sob as quais ele será rescindido por qualquer uma das partes, como por exemplo, mudanças inesperadas na estratégia ou nos recursos financeiros disponíveis, ou atraso na sua execução.

- d) Monitorar o acordo. Esta atividade consiste nas seguintes tarefas:
  - 1) Avaliar a execução do acordo.
Isto inclui a confirmação de que todas as partes estão cumprindo suas responsabilidades conforme o acordo. O Processo de Avaliação e Controle de Projeto é usado para avaliar o custo, o cronograma, a execução do projeto e o impacto de resultados indesejáveis na organização. Esta informação é combinada com outras avaliações da execução dos termos do acordo. Se a execução do acordo não resultar em um produto ou serviço aceitável, o adquirente ou fornecedor pode rescindir o acordo conforme estabelecido nos seus termos.

NOTA 2 Os testes de aceitação podem ser realizados por meio do Processo de Validação. As exceções que surgem durante a condução do acordo, ou com o produto ou serviço entregue, sao resolvidas conforme os procedimentos estabelecidos no acordo.

  - 2) Prover dados necessários para o fornecedor e resolver os problemas em tempo hábil.
- e) Aceitar o produto ou serviço. Esta atividade consiste nas seguintes tarefas:
  - 1) Confirmar se o produto ou serviço entregue está em conformidade com o acordo.
NOTA Se os requisitos acordados e os critérios de aceitação foram atendidos, o fornecedor cumpriu sua obrigação. As exceções não tratadas, por exemplo, discordâncias em relação a realização de testes de aceitação ou nível de adequação do produto ao uso pretendido, estão sujeitas as condições estipuladas no acordo relacionadas a disputas, arbitragem ou legislação e regulamentos aplicáveis.

  - 2) Realizar pagamento ou outra forma de remuneração acordada.
  - 3) Aceitar o produto ou serviço do fornecedor, ou de outra parte, conforme estipulado no acordo.
  - 4) Encerrar o acordo.
NOTA O projeto é encerrado pelo processo de Gerenciamento de Portfólio.


### 6.1.2 Processo de Fornecimento


#### 6.1.2.1 Propósito

O propósito do Processo de Fornecimento é fornecer a um adquirente um produto ou serviço que satisfaça os requisitos acordados.

NOTA Como parte deste processo, o acordo é modificado quando uma requisição de mudança que afeta os termos do acordo é acordada por ambos, adquirente e fornecedor.


#### 6.1.2.2 Resultados

Como resultado da implementação bem-sucedida do Processo de Fornecimento:

- a) Um adquirente de um produto ou serviço é identificado.
- b) Uma resposta à solicitação do adquirente é produzida.
- c) Um acordo é estabelecido entre o adquirente e o fornecedor.
- d) Um produto ou serviço é fornecido.
- e) As obrigações do fornecedor definidas no acordo são satisfeitas.
- f) A responsabilidade pelo produto ou serviço adquirido, conforme previsto no acordo, é transferida.

#### 6.1.2.3 Atividades e tarefas

O fornecedor deve implementar as seguintes atividades e tarefas de acordo com as políticas e procedimentos da organização aplicáveis relacionadas ao Processo de Fornecimento.

- a) Preparar para o fornecimento. Esta atividade consiste nas seguintes tarefas:
  - 1) Verificar e identificar um adquirente que tenha uma necessidade de um produto ou serviço.
NOTA Geralmente, Isto é gerado pelo Processo de Análise de Negócio. Para um produto ou serviço desenvolvido para um consumidor ou um agente, por exemplo, uma função de marketing da organização fornecedora pode fazer o papel de adquirente.

  - 2) Definir uma estratégia para fornecimento.
NOTA de riscos e problemas e um cronograma em etapas. Também inclui os principais fatores e características da aquisição, como responsabilidades e passivos; modelos, métodos ou processos específicos; nível de criticidade; formalidade; e prioridade de fatores comerciais relevantes.

- b) Responder a uma solicitação de fornecimento de produtos ou serviços. Esta atividade consiste nas seguintes tarefas:
  - 1) Avaliar uma solicitação de fornecimento de um produto ou serviço para determinar a viabilidade e como deverá ser a resposta.
  - 2) Preparar uma resposta que satisfaça à solicitação.
- c) Estabelecer e manter um acordo. Esta atividade consiste nas seguintes tarefas:
  - 1) Negociar um acordo com o adquirente que inclua critérios de aceitação.
NOTA Este acordo varia em formalidade, de um acordo escrito a um verbal. O Fornecedor confirma que os requisitos, os prazos de entrega e as condições de aceitação do acordo são possíveis de serem atendidas, que os procedimentos de gerenciamento de mudanças no acordo, o manuseio de exceções alterações e os cronogramas de pagamento são aceitáveis e que ambas as partes, que compõe o acordo, compreendam a base da sua execução sem incorrerem em riscos desnecessários. Os problemas são discutidos e resolvidos durante a negociação, após a qual o adquirente e o fornecedor aceitam os termos do acordo e é iniciada a sua execução. Para um acordo feito por escrito, a sua execução ocorre quando ele é assinado ou conforme especificado no acordo.

  - 2) Identificar a necessidade de mudanças no acordo.
NOTA Ao solicitar uma alteração no acordo, o adquirente ou o fornecedor detalha suas especificações, justificativa e histórico

  - 3) Avaliar o impacto nas mudanças do acordo
NOTA Qualquer mudança é analisada em relação ao seu impacto nos planos, cronograma, custo, capacidade técnica e qualidade do projeto. Uma mudança pode ser tratada dentro do acordo existente, pode exigir uma alteração no acordo ou pode exigir um novo acordo.

  - 4) Negociar o acordo com o adquirente, se necessário.
NOTA Os termos do acordo são negociados entre o adquirente e o fornecedor. Isto inclui mudanças devido a alterações no contexto do mercado. A negociação ocorre para o acordo inicial e, conforme necessário, para as suas alterações. Os acordos alterados são baseados nas mudanças necessárias e nos impactos identificados.

  - 5) Atualizar o acordo com o fornecedor, conforme necessário.
NOTA O resultado da alteração do acordo é incorporado aos planos do projeto e comunicado a todas as partes afetadas.

- d) Executar o acordo. Esta atividade consiste nas seguintes tarefas:
  - 1) Executar o acordo de acordo com os planos de projeto estabelecidos.
NOTA Às vezes, um fornecedor adota ou concorda em usar os processos do adquirente.

  - 2) Avaliar a execução do acordo.
NOTA Isto inclui a confirmação de que todas as partes estão cumprindo suas responsabilidades de acordo com o acordo. O processo de Avaliação e Controle do Projeto é usado para avaliar o custo projetado, o cronograma, o desempenho e o impacto de resultados indesejáveis na organização. Esta informação é combinada com outras avaliações da execução dos termos do acordo. Se a execução do acordo não resultar em um produto ou serviço aceitável, o adquirente ou fornecedor pode rescindir o acordo conforme estabelecido nos termos do acordo.

- e) Entregar e prestar suporte ao produto ou serviço. Esta atividade consiste nas seguintes tarefas:
  - 1) Entregar o produto ou serviço de acordo com os critérios do acordo.
Conforme declarado no acordo, os critérios de aceitação, como o teste de aceitação, estão relacionados a como o produto ou serviço atenderá ao uso pretendido em seu ambiente operacional. As exceções não tratadas, por exemplo, discordâncias em relação a realização de testes de aceitação ou o quão adequado está o produto para ser usado, estão sujeitas a disposições estipuladas no acordo como: disputas, arbitragem ou leis e regulamentos aplicáveis.

  - 2) Dar assistência ao adquirente pela prestação de suporte ao produto ou serviço entregue, de acordo com o acordo.
  - 3) Aceitar e reconhecer o pagamento ou outra consideração acordada.
  - 4) Transferir o produto ou serviço para o adquirente ou outra parte, conforme indicado no acordo.
  - 5) Encerrar o acordo.
NOTA 1 O projeto é encerrado pelo Processo de Gerenciamento de Portfólio.

NOTA 2 Os acordos podem especificar as condições sob as quais ele será rescindido por qualquer uma das partes, por exemplo, mudanças inesperadas na estratégia, fundos disponíveis ou atraso na sua execução.


## 6.2 Processos Organizacionais Habilitadores de Projeto

Os Processos Organizacionais Habilitadores de Projeto ajudam a garantir a capacidade da organização de adquirir e fornecer produtos ou serviços por meio do inicio, suporte e controle de projeto. Estes processos fornecem recursos e infraestrutura necessários para apoiar os projetos e ajudar a garantir a satisfação dos objetivos organizacionais e dos acordos firmados. Eles não pretendem ser um conjunto completo de processos de negócios que permitem o gerenciamento estratégico dos negócios da organização.

Os Processos Organizacionais Habilitadores de Projeto consistem nos seguintes:

- a) Processo de Gerenciamento de Modelo de Ciclo de Vida;
- b) Processo de Gerenciamento de Infraestrutura;
- c) Processo de Gerenciamento de Portfólio;
- d) Processo de Gerenciamento de Recursos Humanos;
- e) Processo de Gestão da Qualidade; e
- f) Processo de Gerenciamento de Conhecimento

### 6.2.1 Processo de Gerenciamento de Modelo de Ciclo de Vida


#### 6.2.1.1 Propósito

O propósito do Processo de Gerenciamento de Modelo de Ciclo de Vida é definir, manter e garantir disponibilidade das políticas, processos de ciclo de vida, modelos de ciclo de vida e procedimentos de uso pela organização com relação ao escopo deste documento.

Este processo proporciona politicas, processos e procedimento de ciclo de vida que são consistentes com os objetivos da organização, os quais são definidos, adaptados, melhorados e mantidos, a fim de sustentar as necessidades individuais do projeto dentro do contexto da organização, e os quais são capazes de serem aplicados usando-se ferramentas e métodos eficazes e comprovados.


#### 6.2.1.2 Resultados esperados

Como resultado esperado da implementação bem-sucedida do Processo de Gerenciamento do Modelo de Ciclo de Vida:

- a) As políticas e procedimentos para o gerenciamento e desenvolvimento dos modelos de ciclo de vida e processo são fornecidos.
- b) A responsabilidade, autoridade e responsabilização para os processos, modelos, procedimentos e políticas do ciclo de vida são definidas.
- c) Os processos e os modelos de ciclo de vida são avaliados.
- a) As melhorias nos processos, nos modelos e nos procedimentos prioritários são implementadas.

#### 6.2.1.3 Atividades e tarefas

A organização deve implementar as seguintes atividades de acordo com as políticas e procedimentos organizacionais aplicáveis com relação ao Processo de Gerenciamento de Modelo de Ciclo de Vida.

- a) Estabelecer o processo. Esta atividade consiste nas seguintes tarefas:
NOTA Os detalhes da implementação do ciclo de vida em um projeto dependem da complexidade do trabalho, dos métodos utilizados e das habilidades e treinamento dos envolvidos na execução deste trabalho. Um projeto adapta politicas, processos, modelos e procedimentos de acordo com seus requisitos e necessidades, sempre mantendo o alinhamento com os regulamentos e políticas organizacionais. O anexo A contém informações sobre adaptação.

  - 1) Estabelecer politicas e procedimentos para gerenciamento e implantação de processos que sejam consistentes com as estratégias organizacionais.
  - 2) Estabelecer os processos que implementam os requisitos deste documento e que sejam consistentes com as estratégias organizacionais.
  - 3) Definir papéis, responsabilidades, autoridades e responsabilizações para facilitar a implementação dos processos e o gerenciamento estratégico dos ciclos de vida.
  - 4) Definir os critérios de negócios que controlam o progresso ao longo do ciclo de vida.
NOTA Os critérios de tomada de decisão relativos à entrada e saída de cada estágio do ciclo de vida e marcos importantes são estabelecidos. Às vezes, eles são expressos em termos de atendimento ao negócio.

  - 5) Estabelecer os modelos de ciclo de vida padrão para a organização, compostos por estágios e definir o propósito e os resultados de cada estágio.
NOTA O modelo de ciclo de vida compreende um ou mais modelos de estágio, conforme necessário. Ele é montado como uma sequência de estágios que podem se sobrepor ou iterar, conforme apropriado para o escopo, magnitude, complexidade, necessidades e oportunidades para o sistema de interesse. Os estágios são ilustrados na ISO/IEC TS 24748-1 usando um exemplo comum de estágios de ciclo de vida. Exemplos específicos para sistemas e software são fornecidos nas ISO/IEC TR 24748-2 e ISO/IEC TR 24748-3. Os processos e atividades do ciclo de vida são selecionados, adaptados, conforme apropriado, e utilizados em um estágio para cumprir o propósito e os resultados deste estágio.

- b) Avaliar o processo. Esta atividade consiste nas seguintes tarefas:
NOTA A ISO/IEC 33002: 2015 fornece um conjunto mais detalhado de atividades e tarefas de avaliação de processos que podem ser alinhadas com as tarefas mostradas abaixo.

  - 1) Monitorar a execução do processo em toda a organização.
NOTA Isto inclui o monitoramento do desempenho, a análise de medidas de processo e a análise crítica de tendências com relação à conformidade com regulamentos, políticas organizacionais, critérios de negócios e feedback dos projetos sobre a eficácia e eficiência dos processos.

  - 2) Realizar análises criticas periódicas dos modelos de ciclo de vida utilizados pelos projetos.
NOTA Isto inclui a confirmação continua da adequação e eficácia dos modelos de ciclo de vida utilizados pelos projetos e a realização de melhorias, conforme apropriado. Isto inclui os estágios, processos e criterios de sucesso que controlam o progresso ao longo do ciclo de vida.

  - 3) Identificar oportunidades de melhoria a partir dos resultados da avaliação.
NOTA As melhorias podem afetar os estágios, processos e critérios de sucesso que controlam a progressão ao longo do ciclo de vida.

- c) Melhorar o processo. Esta atividade consiste nas seguintes tarefas:
  - 1) Priorizar e planejar as oportunidades de melhoria.
  - 2) Implementar oportunidades de melhoria e informar os stakeholders.
NOTA O Processo de Melhoria inclui melhorias em qualquer um dos processos da organização. As lições aprendidas são capturadas e disponibilizadas.


### 6.2.2 Processo de Gerenciamento de Infraestrutura


#### 6.2.2.1 Propósito

O propósito do Processo de Gerenciamento de Infraestrutura é fornecer a infraestrutura e serviços para os projetos de modo a apoiar os objetivos do projeto e da organização durante o ciclo de vida.

Este processo define, fornece e mantém as facilidades, ferramentas e comunicações e tecnologia da informação necessários para o negócio da organização em relação ao objetivo deste documento.


#### 6.2.2.2 Resultados esperados

Como resultado da implementação bem-sucedida do Processo de Gerenciamento de Infraestrutura:

- a) Os requisitos de infraestrutura são definidos.
- b) Os elementos de infraestrutura são identificados e especificados.
- c) Os elementos de infraestrutura são desenvolvidos ou adquiridos.
- d) Os elementos de infraestrutura são disponibilizados.

#### 6.2.2.3 Atividades e tarefas

A organização deve implementar as seguintes atividades e tarefas de acordo com as políticas e procedimentos da organização aplicáveis em relação ao Processo de Gerenciamento de Infraestrutura.

- a) Estabelecer a infraestrutura. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir os requisitos de infraestrutura do projeto.
NOTA 1 Exemplos de elementos de infraestrutura incluem instalações, ferramentas, hardware, software, serviços e padrões. Além dos recursos gerais de infraestrutura comuns a uma organização para apoiar seus processos de negócios, uma organização também pode prover projetos permitindo sistemas exclusivos ou compartilhados de apoio aos processos técnicos do projeto.

NOTA 2 As necessidades de recursos de infraestrutura do projeto são consideradas juntamente com outros projetos e recursos dentro da organização, bem como também com as políticas e planos estrategicos da organização. As restrições e cronogramas de negócios que influenciam e controlam o fornecimento de recursos e serviços de infraestrutura para o projeto também são avaliados. Os planos do projeto e as necessidades futuras dos negócios contribuem para o entendimento da infraestrutura de recursos necessária. Fatores físicos (por exemplo, instalações), necessidades de logística e fatores humanos (incluindo aspectos de saúde e segurança) também são considerados.

NOTA 3 A ISO/IEC 27036, Information security for supplier relationships, fornece orientações para tratar da segurança da infraestrutura terceirizada.

  - 2) Identificar, obter e fornecer recursos e serviços de infraestrutura necessários para implementar e apoiar projetos.
NOTA Um registro com o inventário de ativos geralmente é estabelecido para rastrear elementos de infraestrutura e oferecer suporte à reutilização de ativos de infraestrutura.

- b) Manter a infraestrutura. Esta atividade consiste nas seguintes tarefas:
  - 1) Avaliar até que ponto os recursos de infraestrutura entregues atendem às necessidades do projeto.
  - 2) Identificar e prover as melhorias ou alterações nos recursos de infraestrutura à medida que os requisitos do projeto mudem.

### 6.2.3 Processo de Gerenciamento de Portfólio


#### 6.2.3.1 Propósito

O propósito do Processo de Gerenciamento de Portfólio é iniciar e sustentar projetos adequados, suficientes e necessários a fim de satisfazer os objetivos estratégicos da organização.

Este processo proporciona o investimento de recursos físicos e financeiros adequados, e aprova as autoridades necessárias para o estabelecimento dos projetos selecionados. Realizar qualificação contínua de projetos, a fim de confirmar que eles justificam ou podem ser redirecionados a justificarem, investimento continuo.

Para sistemas de software, o Gerenciamento de Portfólio também se refere geralmente ao gerenciamento de uma linha de produtos (portfólio de ativos, produtos e sistemas habilitadores ou catálogo de serviços) para atender às necessidades e objetivos organizacionais ou dos clientes e apoiar mudanças na tecnologia. A gestão de ativos é atendida pelo gerenciamento de projetos.


#### 6.2.3.2 Resultados esperados

Como resultado da implementação bem-sucedida do Processo de Gerenciamento de Portfólio:

  - a) Oportunidades de associações empresariais, investimentos ou necessidades são qualificadas, selecionadas e prioridades são estabelecidas.
  - b) Projetos são identificados.
  - c) Recursos e orçamentos para cada projeto são alocados.
  - d) Responsabilidade, autoridade e responsabilização pelo gerenciamento de projeto são definidas.
  - e) Projetos que atendem ao acordo e os requisitos dos stakeholders são sustentados.
  - f) Projetos que não atendem ao acordo ou os requisitos dos stakeholders são redirecionados ou cancelados.
  - g) Projetos que não atendem aos acordos ou aos requisitos são redirecionados ou encerrados.
  - h) Projetos que tem o seu acordo atendido e que satisfazem os requisitos completos são encerrados.

#### 6.2.3.3 Atividades e tarefas

A organização deve implementar as seguintes atividades e tarefas de acordo com as políticas e procedimentos da organização aplicáveis com relação ao processo de Gerenciamento de Portfólio.

- a) Definir e autorizar projetos. Esta atividade consiste nas seguintes tarefas:
  - 1) Identificar novas ou alterações de capacidades ou missões potenciais.
NOTA A estratégia de negócios da organização, conceito de operações, análise de lacunas (gap analysis) ou análise de oportunidades é analisada criticamente para verificar lacunas, problemas ou oportunidades atuais. Uma nova capacidade ou necessidade da empresa geralmente é determinada no Processo de Análise de Negócio, definida e gerenciada posteriormente no Processo de Definição de Necessidades e Requisitos dos Stakeholders, e gerenciada ao longo deste processo.

-FL47 -

  - 2) Priorizar, selecionar e estabelecer novas oportunidades de negócios, empreendimentos ou empresas.
NOTA Estes, geralmente, são consistentes com a estratégia de negócios e planos de ação da organização. Os projetos em potencial são priorizados e os limites estabelecidos para determinar quais projetos serão executados. As características dos projetos identificados são frequentemente determinadas, incluindo o valor dos stakeholders, riscos e barreiras ao sucesso, dependências e inter-relacionamentos, restrições, necessidades de recursos e contenção mútua de recursos. Cada projeto potencial é então avaliado com relação à probabilidade de sucesso e seu custo-benefício. Os processos de Gerenciamento de Decisão e Análise de Sistema fornecem detalhes sobre como executar uma análise de alternativas.

  - 3) Definir projetos, responsabilidade, responsabilizações e autoridades.
  - 4) Identificar as metas, objetivos e resultados esperados de cada projeto.
  - 5) Identificar e alocar os recursos para o atendimento as metas e objetivos do projeto.
  - 6) Identificar as interfaces e dependências de vários projetos a serem gerenciadas ou suportadas por cada projeto.
NOTA 1 Isto inclui o uso ou reutilização de sistemas habilitadores usados por mais de um projeto e o uso ou reutilização de elementos comuns do sistema, incluindo elementos de software, em mais de um projeto.

NOTA 2 Compreender cada projeto no contexto da arquitetura corporativa ajuda a garantir que restrições e interfaces sejam identificadas.

  - 7) Especificar os requisitos para que o projeto seja reportado e analisar criticamente os marcos que governam a execução de cada projeto.
  - 8) Autorizar cada projeto a iniciar a execução dos planos do projeto.
NOTA Ver o Processo de Planejamento de Projeto para obter informações adicionais sobre o desenvolvimento de planos do projeto. Os planos do projeto são mais úteis quando desenvolvidos e aprovados no início do ciclo de vida do projeto.

- b) Avaliar o portfólio de projetos. Esta atividade consiste nas seguintes tarefas:
  - 1) Avaliar os projetos para confirmar continuamente a sua viabilidade.
NOTA A viabilidade inclui os seguintes critérios:

i. O projeto está progredindo no sentido de alcançar metas e objetivos estabelecidos.

iI. O projeto está em conformidade com as diretrizes do projeto.

O projeto está sendo conduzido de acordo com as políticas, processos e procedimentos aprovados do ciclo de vida do projeto.

iv. O projeto permanece viável, como indicado, por exemplo, pela necessidade contínua do serviço, implementação prática do produto e benefícios aceitáveis de investimento.

  - 2) Atuar para continuar ou redirecionar projetos que estão progredindo satisfatoriamente ou que podem progredir satisfatoriamente pelo redirecionamento apropriado.
- c) Encerrar projetos. Esta atividade consiste nas seguintes tarefas:
  - 1) Quando os acordos permitirem, agir para cancelar ou suspender projetos cujas desvantagens ou riscos para a organização superem os benefícios dos contínuos investimentos.
NOTA A captura das lições aprendidas de projetos cancelados ou com falha pode ser especialmente útil para melhoria organizacional ou para uso em outros projetos.

  - 2) Após a conclusão do acordo de produtos e serviços, agir para encerrar os projetos.
NOTA O encerramento é realizado de acordo com as políticas e procedimentos organizacionais e com o acordo.


### 6.2.4 Processo de Gerenciamento de Recursos Humanos


#### 6.2.4.1 Propósito

• propósito do Processo de Gerenciamento de Recursos Humanos é fornecer à organização recursos humanos necessários e manter suas habilidades consistentes com as necessidades do negócio.

O processo garante o fornecimento de uma equipe qualificada com experiência e capacidade para a realização de processos de ciclo de vida de modo a alcançar os objetivos da organização, do projeto e dos stakeholder.


#### 6.2.4.2 Resultados esperados

Como resultado da implementação bem-sucedida do Processo de Gerenciamento de Recursos Humanos:

  - a) As habilidades necessárias para projeto são identificadas.
  - b) Os recursos humanos necessários são fornecidos para os projetos.
  - c) As habilidades da equipe são desenvolvidas, mantidas ou aperfeiçoadas.
  - d) Os conflitos em demandas por recursos em múltiplos projetos são resolvidos.

#### 6.2.4.3 Atividades e tarefas

A organização deve implementar as seguintes atividades e tarefas de acordo com as politicas e procedimentos da organização aplicáveis com relação ao Processo de Gerenciamento de Recursos Humanos:

- a) Identificar habilidades. Esta atividade consiste nas seguintes tarefas:
  - 1) Identificar as habilidades necessárias com base nos projetos atuais e previstos.
  - 2) Identificar e registrar as habilidades das pessoas.
- b) Desenvolver habilidades. Esta atividade consiste nas seguintes tarefas:
  - 1) Estabelecer uma estratégia de desenvolvimento de habilidades.
NOTA Este plano inclui tipos e níveis de treinamento, categorias de pessoal, agendas, requisitos de recursos de pessoal e necessidades de treinamento.

  - 2) Obter ou desenvolver recursos para treinamento, educação ou mentoria.
NOTA Estes recursos incluem materiais de treinamento que são desenvolvidos pela organização ou por terceiros, cursos de treinamento que são disponibilizados por fornecedores externos, instrução baseada em computador.

  - 3) Prover o desenvolvimento de habilidades planejado.
  - 4) Manter registros do desenvolvimento de habilidades.
- c) Adquirir e prover habilidades. Esta atividade consiste nas seguintes tarefas:
NOTA Isto inclui o recrutamento e a retenção de pessoal com níveis de experiência e habilidades necessários para alocar adequadamente a equipe ao projeto; avaliação e revisão da equipe, por exemplo, sua proficiência, motivação, capacidade de trabalhar em equipe, bem como a necessidade de ser requalificado, redesignado ou realocado.

  - 1) Obter pessoal qualificado quando forem identificados déficits de habilidade.
NOTA Isto inclui o uso de recursos terceirizados.

  - 2) Manter e gerenciar o conjunto de pessoas qualificadas necessárias para alocação nos projetos em andamento.
  - 3) Fazer as alocações no projeto com base nas necessidades do projeto e no desenvolvimento das pessoas.
  - 4) Motivar o pessoal, por exemplo, por meio de mecanismos de desenvolvimento de carreira e recompensa.
  - 5) Controlar interfaces de gerenciamento de múltiplos projetos para resolver conflitos de pessoal.
NOTA Isto inclui conflitos de capacidade de infraestrutura e serviços de suporte organizacional, bem como os recursos de pessoal entre os projetos em andamento; ou de superalocação de pessoal do projeto.


### 6.2.5 Processo de Gestão da Qualidade


#### 6.2.5.1 Propósito

O propósito do Processo de Gestão da Qualidade é assegurar que os produtos, os serviços e as implementações do Processo de Gestão da Qualidade atendam aos objetivos de qualidade do projeto e da organização, e alcancem a satisfação do cliente.


#### 6.2.5.2 Resultados esperados

Como resultado da implementação bem-sucedida do Processo de Gestão da Qualidade:

- a) As políticas, os objetivos e os procedimentos organizacionais de gestão de qualidade são definidos e implementados.
- b) Os critérios e os métodos de avaliação da qualidade são estabelecidos.
- c) Os recursos e a informação são fornecidos para os projetos para apoiar a operação e o monitoramento das atividades de garantia da qualidade do projeto.
- d) Os resultados da avaliação da garantia da qualidade são obtidos e analisados.
- e) As políticas e os procedimentos de gestão da qualidade são melhorados com base nos resultados organizacionais e do projeto.

#### 6.2.5.3 Atividades e tarefas

A organização deve implementar as seguintes atividades e tarefas de acordo com as políticas e procedimentos da organização aplicáveis ao Processo de Gestão da Qualidade.

NOTA Ver a ABNT NBR ISO 9001:2015 para informações e requisitos para estabelecer um Sistema de Gestão da Qualidade.

- a) Planejar a gestão da qualidade. Esta atividade consiste nas seguintes tarefas:
  - 1) Estabelecer políticas, objetivos e procedimentos de gestão da qualidade.
NOTA 1 A ISO 9004 2009 contém diretrizes para melhorias de desempenho.

NOTA BRASILEIRA A ISO 9004:2009 foi substituída pela ISO 9004:2018, a qual foi adotada no Brasil como ABNT NBR ISO 9004:2019, Gestão da qualidade - Qualidade de uma organização - Orientação para alcançar o sucesso sustentado.

NOTA 2 As políticas, os objetivos e os procedimentos são baseados na estratégia de negócio para satisfação do cliente e levam em consideração a gestão de riscos.

  - 2) Definir responsabilidades e autoridade para implementação da gestão da qualidade.
NOTA Para manter a independência do gerenciamento da qualidade, seus recursos são frequentemente atribuídos para uma organização apartada do projeto.

  - 3) Definir critérios e métodos de avaliação da qualidade.
  - 4) Fornecer recursos e informações para gestão da qualidade.
- b) Avaliar a gestão da qualidade. Esta atividade consiste nas seguintes tarefas:
  - 1) Reunir e analisar os resultados da avaliação da garantia da qualidade, de acordo com os critérios definidos.
  - 2) Avaliar a satisfação do cliente.
NOTA A ABNT NBR ISO 10004:2013 contém diretrizes para monitorar e medir a satisfação do cliente. A qualidade do sistema de software também é demonstrada pela satisfação do usuário.

  - 3) Realizar análises críticas periódicas das atividades de Garantia da Qualidade do projeto, em conformidade com as políticas, objetivos e procedimentos da Gestão da Qualidade.
NOTA Critérios e métodos de avaliação da qualidade são estabelecidos. As avaliações da qualidade estão em conformidade com os procedimentos do projeto e com as características da qualidade do produto.

  - 4) Monitorar a situação das melhorias da qualidade em processos, produtos e serviços.
- c) Realizar ações corretivas e preventivas. Esta atividade consiste nas seguintes tarefas:
  - 1) Planejar ações corretivas quando os objetivos de gestão da qualidade não forem atingidos.
  - 2) Planejar ações preventivas quando houver um risco suficiente de que os objetivos de gestão da qualidade não sejam atingidos.
  - 3) Monitorar ações corretivas e preventivas até a finalização e informar os stakeholders relevantes.
NOTA 1 A implementação de ações corretivas e preventivas é realizada em outros processos relevantes, como Gerenciamento de Modelo de Ciclo de Vida ou Avaliação e Controle de Projeto.

NOTA 2 A ABNT NBR ISO 9001:2015, 0.3.3 e o Anexo A.4 descrevem ações preventivas para eliminar possíveis não conformidades como parte da mentalidade de risco.


### 6.2.6 Processo de Gerenciamento do Conhecimento


#### 6.2.6.1 Propósito

O propósito do Processo de Gerenciamento do Conhecimento é criar a capacidade e os ativos que permitam à organização explorar oportunidades para reaplicar o conhecimento existente.

Isto inclui conhecimento, perfis e ativos de conhecimento, incluindo elementos do sistema.

NOTA A reaplicação do conhecimento existente é conhecida como reuso do conhecimento. O reuso do conhecimento pode ser sobre os elementos de software ou a partir deles.


#### 6.2.6.2 Resultados esperados

Como resultado da implementação bem-sucedida do Processo de Gerenciamento do Conhecimento:

- a) Uma taxonomia para a aplicação de ativos de conhecimento é identificada.
- b) O conhecimento organizacional, as habilidades e os ativos de conhecimento são desenvolvidos ou adquiridos.
- c) O conhecimento organizacional, habilidades e ativos de conhecimento estão disponíveis.
- a) Os dados de uso do gerenciamento do conhecimento são coletados e analisados.

#### 6.2.6.3 Atividades e tarefas

A organização deve implementar as seguintes atividades e tarefas de acordo com as políticas e procedimentos da organização aplicáveis ao Processo de Gerenciamento do Conhecimento:

- a) Planejar o gerenciamento do conhecimento. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir a estratégia de gerenciamento do conhecimento.
NOTA 1 Esta estratégia de gerenciamento do conhecimento geralmente inclui:

i. Identificação de domínios e seu potencial para a reaplicação de conhecimentos.

її. Planos para obter e manter conhecimentos, habilidades e ativos de conhecimento ao longo do tempo.

Caracterização dos tipos de conhecimento, habilidades e ativos de conhecimento a serem coletados e mantidos.

iv. Critérios de aceitação, qualificação e retirada de conhecimentos, habilidades e ativos.

V. Procedimentos para controlar mudanças de conhecimento, habilidades e ativos.

vi. Planos, mecanismos e procedimentos para proteção, controle e acesso aos dados e informações classificados ou sensiveis.

vii. Mecanismos de armazenamento e recuperação.

NOTA 2 O gerenciamento do conhecimento inclui tanto o conhecimento compartilhado internamente como fora da organização com os stakeholders, adquirentes e parceiros de negócios designados, sujeitos a acordos de propriedade intelectual e de não divulgação.

  - 2) Identificar conhecimentos, habilidades e ativos a serem gerenciados.
  - 3) Identificar projetos que podem se beneficiar da aplicação do conhecimento, habilidades e ativos de conhecimento.
- b) Compartilhar conhecimentos e habilidades em toda a organização. Esta atividade consiste nas seguintes tarefas:
  - 1) Estabelecer e manter uma classificação para capturar e compartilhar conhecimento e habilidades em toda a organização.
NOTA Esta classificação pode incluir conhecimento especializado, comum e de domínio e habilidades, bem como lições aprendidas de outras tarefas.

  - 2) Capturar ou adquirir conhecimentos e habilidades.
  - 3) Compartilhar conhecimentos e habilidades em toda a organização.
- c) Compartilhar ativos de conhecimento em toda a organização. Esta atividade consiste nas seguintes tarefas:
  - 1) Estabelecer uma taxonomia para organizar ativos de conhecimento.
NOTA 1 A taxonomia inclui o seguinte:

Definição das fronteiras dos domínios e seus relacionamentos.

ii. Modelos de domínio que capturam características, capacidades, conceitos e funções essenciais, comuns e diferentes.

iii. Uma arquitetura para uma família de sistemas dentro do domínio, incluindo suas características comuns e diferentes.

NOTA 2 Ver a ISO/IEC 26550 para obter mais informações sobre modelos de linha de produtos. Ver a ISO/IEC/IEEE 42010:2011 para obter requisitos sobre estruturas de arquitetura, pontos de vista, tipos de modelos, visões e modelos.

  - 2) Desenvolver ou adquirir ativos de conhecimento.
Ativos de conhecimento incluem elementos do sistema ou suas representações (por exemplo, bibliotecas de códigos reutilizáveis, arquiteturas de referência), elementos de arquitetura ou design (por exemplo, padrões de arquitetura ou design), processos, critérios ou outras informações técnicas (por exemplo, materiais de treinamento) relacionadas ao domínio do conhecimento e lições aprendidas.

  - 3) Compartilhar ativos de conhecimento em toda a organização.
NOTA Recursos de pesquisa automatizada aprimoram o acesso aos ativos de conhecimento.

- d) Gerenciar conhecimentos, habilidades e ativos de conhecimento. Esta atividade consiste nas seguintes tarefas:
  - 1) Manter conhecimento, habilidades e ativos de conhecimento.
  - 2) Monitorar e registrar o reuso de conhecimentos, habilidades e ativos de conhecimento.
  - 3) Reavaliar periodicamente a evolução da tecnologia e as necessidades do mercado para os ativos de conhecimento.
NOTA Avaliar os benefícios de negócios que a organização obteve com o uso de práticas de gerenciamento de conhecimento.


## 6.3 Processos de Gerenciamento Técnico

Os Processos de Gerenciamento Técnico são utilizados para estabelecer, evoluir e executar os planos, avaliar o cumprimento e o progresso real em relação aos planos e controlar a execução até a sua conclusão. Os Processos de Gerenciamento Técnico podem ser acionados de forma individual a qualquer momento no ciclo de vida e em qualquer nível em uma hierarquia de projetos, como requerido pelos planos ou eventos não previstos. Os Processos de Gerenciamento Técnico são aplicados com um nível de rigor e formalidade que depende do risco e da complexidade do projeto.

O escopo de um Processo de Gerenciamento Técnico é o gerenciamento técnico de um projeto ou de seus produtos, incluindo o produto de software ou o sistema de interesse.

NOTA Este conjunto de Processos de Gerenciamento Técnico é realizado para que os processos técnicos específicos do sistema de software possam ser conduzidos de maneira efetiva. Eles não compreendem um sistema de gerenciamento ou o conjunto abrangente de processos para gerenciamento de projetos, pois este não é o escopo deste documento.

Os Processos de Gerenciamento Técnico consistem nos seguintes:

- a) processo de Planejamento de Projeto;
- b) processo de Avaliação e Controle de Projeto;
- c) processo de Gerenciamento de Decisão;
- d) processo de Gestão de Riscos;
- e) processo de Gerenciamento de Configuração;
- f) processo de Gerenciamento da Informação;
- g) processo de Medição; e
- h) processo de Garantia da Qualidade.
Os processos Planejamento de Projeto e Avaliação e Controle de Projeto são chave para todas as práticas de gerenciamento. Estes processos estabelecem a abordagem geral para gerenciar um projeto ou um processo. Os outros processos deste grupo fornecem um conjunto de tarefas que são focadas em atender a um objetivo específico de gerenciamento. Todos eles são evidentes na gestão de qualquer empreendimento, desde uma organização completa até um único processo de ciclo de vida e suas tarefas. Neste documento, o projeto foi escolhido como o contexto para descrever processos. Os mesmos processos também podem ser aplicados na execução de serviços.


### 6.3.1 Processo de Planejamento de Projeto


#### 6.3.1.1 Propósito

O propósito do Processo de Planejamento de Projeto é produzir e coordenar planos efetivos e viáveis.

Este processo determina o escopo das atividades técnicas e de gerenciamento de projeto, identifica os resultados do processo, as tarefas e os entregáveis, estabelece cronogramas para condução das tarefas, incluindo critérios de cumprimento e recursos requeridos para completar as tarefas. Este é um processo continuo que se estende ao longo de um projeto, com revisões regulares dos planos.

NOTA As estratégias definidas em cada um dos outros processos fornecem entradas e são integradas ao Processo de Planejamento de Projeto. O Processo de Avaliação e Controle de Projeto é usado para avaliar se os planos estão integrados, alinhados e são viáveis.


#### 6.3.1.2 Resultados esperados

Como resultado da implementação bem-sucedida do Processo de Planejamento de Projeto:

- a) Os objetivos e os planos são definidos.
- b) Os papéis, as responsabilidades, as responsabilizações e as autoridades são estabelecidos.
- c) Os recursos e os serviços necessários para alcançar os objetivos são formalmente solicitados e comprometidos.
- d) Os planos para a execução do projeto são ativados.

#### 6.3.1.3 Atividades e tarefas

O projeto deve implementar as seguintes atividades e tarefas de acordo com políticas e procedimentos organizacionais aplicáveis relacionados ao Processo de Planejamento de Projeto.

- a) Definir o projeto. Esta atividade consiste nas seguintes tarefas:
  - 1) Identificar objetivos e restrições do projeto.
NOTA 1 Objetivos e restrições incluem o desempenho e outros aspectos de qualidade, custo, tempo e satisfação do cliente e do usuário. Cada objetivo é identificado com um nível de detalhe que permite seleção, adaptação e implementação dos processos e atividades adequados.

NOTA 2 AISO/IEC 15026 Systems and software assurance, a ABNT NBR ISO/IEC 27001 Sistemas de Gestão da Segurança da Informação e a ISO/IEC 27036 Information Security for Supplier Relationships fornecem orientações adicionais sobre objetivos e restrições relacionados à garantia e à segurança.

  - 2) Definir o escopo do projeto conforme estabelecido no acordo.
NOTA Isto inclui as atividades relevantes requeridas para satisfazer os critérios de decisão de negócio e completar o projeto com sucesso. Um projeto pode ser responsável por uma ou mais fases do ciclo de vida completo do sistema de software. O Processo de Planejamento de Projeto inclui definir ações apropriadas para manter os planos do projeto, executar avaliações e controlar o projeto.

  - 3) Definir e manter um modelo de ciclo de vida composto por fases, usando os modelos de ciclo de vida definidos da organização.
A ISO/IEC TS 24748-1 fornece informações detalhadas em relação às fases do ciclo de vida e à definição de um modelo de ciclo de vida adequado. Ela define um conjunto geral de exemplos de fases de ciclo de vida de sistemas, incluindo Concepção, Desenvolvimento, Produção, Utilização, Suporte e Desativação. Ela também identifica um conjunto geral de exemplos de fases de ciclo de vida de software, incluindo determinação de necessidades, exploração e definição de conceitos, demonstração e avaliação, engenharia/desenvolvimento, produção/fabricação, implantação/comercialização, operação, manutenção e suporte e desativação.

  - 4) Estabelecer uma Estrutura Analítica de Projeto (EAP) baseada nos produtos entregáveis ou na a arquitetura evolutiva do sistema de software.
NOTA 1 Cada elemento da arquitetura do sistema de software e processos e atividades apropriados são descritos em um nível de detalhe consistente com os riscos identificados. Tarefas relacionadas na Estrutura Analítica de Projeto são agrupadas para execução. As tarefas do projeto identificam itens de trabalho sendo desenvolvidos ou produzidos. O Practice Standard for Work Breakdown Structures do Project Management Institute (PMI) contém detalhes adicionais sobre EAP.

NOTA 2 Para projetos com métodos ágeis ou iterativos, um elemento da EAP pode corresponder às funcionalidades principais, sob a perspectiva do usuário, a serem produzidas durante as iterações.

  - 5) Definir e manter o processo que será aplicado no projeto.
NOTA 1 Estes processos são baseados nos processos definidos da organização (ver processo de Gerenciamento do Modelo de Ciclo de Vida). O Anexo A contém informações sobre adaptações que podem ser usadas para atender a necessidades específicas do projeto. A definição dos processos inclui os critérios de entrada e de saída, entradas, restrições de sequência do processo (relacionamentos do tipo predecessor/sucessor), requisitos de concorrência do processo (quais processos e tarefas devem ser trabalhados simultaneamente com outras tarefas ou atividades da área de processo), atributos de Medidas de Efetividade/Medidas de Desempenho e parâmetros de escopo e custo (para estimativas de custo de importância crítica).

NOTA 2 A identificação de interfaces com outros projetos ou unidades organizacionais é tratada por meio do processo de Gerenciamento de Portfólio.

- b) Planejar o projeto e o gerenciamento técnico. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir e manter um cronograma de projeto baseado em objetivos gerenciais e técnicos e em estimativas de trabalho.
NOTA Isto inclui definição da duração, relacionamentos, dependências e sequência de atividades, marcos de realização, recursos utilizados e as análises críticas e reservas de cronograma para a gestão de riscos, necessários para alcançar a conclusão do projeto no prazo.

  - 2) Definir critérios de atingimento para os pontos de decisão das fases do ciclo de vida, datas de entrega e principais dependências de entradas ou saídas externas.
NOTA Os intervalos de tempo entre análises críticas internas são definidos de acordo com políticas organizacionais relativas a questões como criticidade do negócio ou do sistema, cronograma e riscos técnicos.

  - 3) Definir os custos e planejar um orçamento.
NOTA Os custos orçados são baseados no cronograma, nas estimativas de tamanho e na complexidade do software, nas estimativas do trabalho, nos custos de infraestrutura, nos itens a serem adquiridos, nas estimativas de serviços adquiridos e nos sistemas habilitadores, e nas reservas de orçamento para gestão de riscos.

  - 4) Estabelecer papéis, responsabilidades, responsabilização e autoridades.
NOTA Isto inclui definir a organização do projeto, as aquisições de equipe e o desenvolvimento de habilidades da equipe. As autoridades incluem, conforme apropriado, os papéis e indivíduos legalmente responsáveis, por exemplo, por autorização de design, autorização de segurança, e os responsáveis por certificações ou acreditações aplicáveis.

  - 5) Definir a infraestrutura e os serviços requeridos.
NOTA Isto inclui definir a capacidade necessária, sua disponibilidade e sua alocação às tarefas do projeto. Infraestrutura inclui instalações, serviços, ferramentas, comunicações e ativos de tecnologia da informação. Requisitos para sistemas e serviços habilitadores para cada fase do ciclo de vida também são especificados.

  - 6) Planejar a aquisição externa de materiais e sistemas e serviços habilitadores.
NOTA 1 Isto inclui, conforme necessário, planos para solicitação de proposta, seleção de fornecedores, aceitação, administração e fechamento de acordos. Os processos de acordo são usados para as aquisições planejadas.

NOTA 2 A ISO/IEC 27036 Information security for supplier relationships fornece orientação para aquisição de infraestrutura e serviços.

  - 7) Gerar e comunicar um plano para gerenciamento e execução técnico e do projeto, incluindo análises críticas.
NOTA 1 O planejamento técnico para o sistema de software frequentemente é materializado em um Plano de Gerenciamento de Engenharia de Sistemas (PGES), Plano de Gerenciamento de Engenharia de Software ou Plano de Desenvolvimento de Software (PDS). A ISO/IEC/IEEE 24748-5 fornece mais detalhes sobre planejamento técnico de gerenciamento de engenharia de software e inclui um esboço para um PDS. O planejamento do projeto frequentemente é materializado em um Plano de Gerenciamento de Projeto. A ISO/IEC/IEEE 16326 fornece mais detalhes sobre planejamento de projetos.

NOTA 2 As atividades e tarefas de estratégia para cada um dos outros processos fornecem entradas e são integradas no Processo de Planejamento de Projeto. O Processo de Avaliação e Controle de Projeto é usado para ajudar a garantir que os planos estão integrados, alinhados e são viáveis.

- c) Ativar o projeto. Esta atividade consiste nas seguintes tarefas:
  - 1) Obter aprovação para iniciar o projeto.
NOTA A aprovação para iniciar (autorização para prosseguir) é fornecida pelo processo de Gerenciamento de Portfólio.

  - 2) Submeter requisições e obter comprometimentos em relação aos recursos necessários para executar o projeto.
NOTA Isto inclui acesso a sistemas e serviços habilitadores.

  - 3) Implementar planos de projeto.

### 6.3.2 Processo de Avaliação e Controle de Projeto


#### 6.3.2.1 Propósito

O propósito do Processo de Avaliação e Controle de Projeto é avaliar se os planos estão alinhados e são viáveis; determinar o status do projeto, o desempenho técnico e do processo; e direcionar a execução para ajudar a garantir que o desempenho está de acordo com os planos e cronogramas, dentro dos orçamentos projetados, para satisfazer os objetivos técnicos.

Este processo avalia, periodicamente e em eventos importantes, o progresso e as realizações em relação aos requisitos, planos e objetivos gerais de negócio. São fornecidas informações para ações gerenciais quando variações significativas são detectadas. Este processo também inclui redirecionar as atividades e tarefas do projeto, conforme apropriado, para corrigir desvios e variações identificados por outros processos técnicos ou gerenciais. Redirecionamento pode incluir replanejamento, conforme apropriado.


#### 6.3.2.2 Resultados esperados

Como resultado da implementação bem-sucedida do Processo de Avaliação e Controle de Projeto:

- a) As medidas de desempenho ou resultados de avaliações são disponibilizados.
- b) A adequação de papéis, responsabilidades, responsabilizações e autoridades é avaliada.
- c) A adequação de recursos é avaliada.
- d) As análises críticas de progresso técnico são executadas.
- e) Os desvios no desempenho do projeto em relação aos planos são investigados e analisados.
- f) Os stakeholders afetados são informados sobre o status do projeto.
- g) A ação corretiva é definida e direcionada quando a realização do projeto não está atingindo as metas.
- h) O replanejamento do projeto é iniciado quando necessário.
A ação para evoluir (ou não) de um marco ou evento programado para o próximo é autorizada.

Os objetivos do projeto são alcançados.


#### 6.3.2.3 Atividades e tarefas

O projeto deve implementar as seguintes atividades e tarefas, de acordo com políticas e procedimentos aplicáveis da organização, relacionados ao Processo de Avaliação e Controle de Projeto.

- a) Planejar a avaliação e o controle do projeto. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir a estratégia de avaliação e controle do projeto.
NOTA A estratégia identifica as atividades esperadas de Avaliação e Controle de Projeto, incluindo os métodos e prazos de avaliação planejados e as análises críticas técnicas e gerenciais necessárias.

- b) Avaliar o projeto. Esta atividade consiste nas seguintes tarefas:
  - 1) Avaliar o alinhamento dos objetivos e planos do projeto em relação ao contexto do projeto.
  - 2) Avaliar os planos gerenciais e técnicos em relação aos objetivos para determinar a adequação e a viabilidade.
  - 3) Avaliar o status técnico e do projeto em relação aos planos apropriados para determinar variações de custo, cronograma e desempenho reais em relação aos projetados.
  - 4) Avaliar a adequação de papéis, responsabilidades, responsabilizações e autoridades.
NOTA Isto inclui a avaliação da adequação das competências do pessoal para desempenhar os papéis e completar as tarefas do projeto. São usadas medidas objetivas sempre que possível, como por exemplo, eficiência no uso dos recursos e realizações do projeto.

  - 5) Avaliar a adequação e a disponibilidade dos recursos.
NOTA Recursos incluem infraestrutura, pessoal, financiamento, tempo ou outros itens pertinentes. Esta tarefa inclui avaliar o reuso de processos e recursos de infraestrutura e confirmar que os compromissos intraorganizacionais estão satisfeitos.

  - 6) Avaliar o progresso utilizando a realização medida e a conclusão do marco.
NOTA Isto inclui coletar e avaliar dados de mão de obra, materiais, custos de serviços e desempenho técnico, assim como outros dados técnicos sobre os objetivos, como viabilidade. Estes dados são comparados em relação às medidas esperadas. Isto inclui conduzir avaliações de efetividade para determinar a adequação do sistema de software em evolução em relação aos requisitos. Também inclui a prontidão de sistemas habilitadores para entregar seus serviços quando necessário.

  - 7) Conduzir análises críticas gerenciais e técnicas, auditorias e inspeções requeridas.
NOTA Estas são formais ou informais e são conduzidas para determinar a prontidão para prosseguir para a próxima fase do ciclo de vida ou marco do projeto, para ajudar a garantir que os objetivos tecnicos e do projeto estão sendo alcançados ou para obter feedback dos stakeholders.

  - 8) Monitorar processos críticos e novas tecnologias.
NOTA Isto inclui identificar e avaliar a maturidade da tecnologia e a viabilidade de sua inserção. A maturidade da tecnologia é a prontidão de uma tecnologia para uso operacional e frequentemente é medida em uma escala de baixa (existe apenas como um conceito) a alta (comprovada em uso operacional).

  - 9) Analisar resultados de medição e fazer recomendações.
NOTA Os resultados de medição são analisados para identificar desvios, variações ou tendências indesejáveis de valores planejados, que incluem preocupações potenciais e para fazer recomendações apropriadas para correções ou ações preventivas. Isto inclui, quando apropriado, análises estatísticas de medidas que indicam tendências, como por exemplo, densidade de falhas para indicar a qualidade dos resultados, ou distribuição de parâmetros medidos que indicam repetibilidade de processos.

  - 10) Registrar e fornecer status e achados de tarefas de avaliação.
NOTA Isto geralmente é estabelecido no acordo, nas políticas e nos procedimentos.

  - 11) Monitorar a execução do processo no projeto.
Isto inclui a análise das medidas do processo e a análise crítica de tendências em relação aos objetivos do projeto. Quaisquer ações de melhoria identificadas podem ser tratadas no processo de Garantia da Qualidade, no Processo de Gestão da Qualidade ou no processo de Gerenciamento

- c) Controlar o projeto. Esta atividade consiste nas seguintes tarefas:
  - 1) Iniciar ações necessárias para tratar questões identificadas.
NOTA 1 Esta tarefa ocorre quando o projeto ou a realização técnica não está atingindo as metas planejadas. Isto inclui ações preventivas, corretivas e de resolução de problemas. Ações geralmente requerem replanejamento ou realocação de pessoal, ferramentas e ativos de infraestrutura, quando for detectada inadequação ou indisponibilidade, ou quando realizações técnicas ou do projeto ficarem aquém das metas ou planos. Elas frequentemente impactam o custo, cronograma, escopo ou definições técnicas. As ações às vezes requerem mudanças na implementação e execução dos processos do ciclo de vida.

NOTA 2 Ações são registradas e analisadas criticamente para confirmar sua adequação e prazo de execução.

  - 2) Iniciar o replanejamento necessário do projeto.
NOTA 1 O replanejamento do projeto é iniciado quando os objetivos ou restrições do projeto mudaram ou quando as premissas de planejamento se mostraram inválidas.

NOTA 2 Qualquer mudança que requer uma mudança no acordo entre o adquirente e o fornecedor dá início ao Processo de Aquisição e Fornecimento.

  - 3) Iniciar ações de mudança quando há uma mudança contratual no custo, tempo ou qualidade, devida ao impacto de uma requisição do adquirente ou do fornecedor.
NOTA Isto inclui considerações sobre termos e condições modificados para o fornecimento ou iniciação de nova seleção de fornecedor, que dá início ao Processo de Aquisição e Fornecimento.

  - 4) Autorizar o projeto a prosseguir em direção ao próximo marco ou evento, se justificado.
NOTA O processo de Avaliação e Controle do Projeto é usado para chegar a um acordo sobre a conclusão do marco.


### 6.3.3 Processo de Gerenciamento de Decisão


#### 6.3.3.1 Propósito

O propósito do Processo de Gerenciamento de Decisão é fornecer uma estrutura analítica para identificar, caracterizar e avaliar objetivamente um conjunto de alternativas para uma decisão, em qualquer ponto do ciclo de vida, e selecionar a mais benéfica.

Este processo é usado para resolver questões técnicas ou de projeto, e responder requisições para decisões encontradas durante o ciclo de vida do software, de forma a identificar alternativas que fornecem os melhores resultados para a situação. Os métodos mais frequentemente usados para Gerenciamento de Decisão são o estudo econômico e a análise de engenharia. Cada uma das alternativas é avaliada em relação aos critérios de decisão (por exemplo, impacto nos custos, impacto no cronograma, restrições de programação, implicações regulatórias, características de desempenho técnico, características críticas de qualidade e riscos). Os resultados dessas comparações são classificados, por meio de um modelo de seleção adequado, e são usados para decidir sobre uma solução ótima. Os dados principais do estudo (por exemplo, premissas e lógica de decisão) geralmente são mantidos para informar os tomadores de decisão e apoiar futuras tomadas de decisão.

NOTA Quando é necessário executar uma avaliação detalhada de um parâmetro para um dos critérios, o Processo de Análise de Sistema pode ser utilizado para executar a avaliação.


#### 6.3.3.2 Resultados esperados

Como resultado da implementação bem-sucedida do Processo de Gerenciamento de Decisão:

- a) As decisões que requerem análise de alternativas são identificadas.
- b) As alternativas são identificadas e avaliadas.
- c) Uma alternativa preferencial é selecionada.
- d) A resolução, a lógica de decisão e as premissas são identificadas.

#### 6.3.3.3 Atividades e tarefas

O projeto deve implementar as seguintes atividades e tarefas, de acordo com as políticas e os procedimentos organizacionais aplicáveis relacionados ao Processo de Gerenciamento de Decisão.

- a) Preparar para decisões. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir uma estratégia de gerenciamento de decisão.
NOTA Uma estratégia de gerenciamento de decisão inclui a identificação de papéis, responsabilidades, responsabilização e autoridades. A estratégia considera a necessidade de obter informações e retornar uma decisão em tempo hábil. Isto inclui a identificação de categorias de decisão e de um esquema de priorização. As decisões frequentemente surgem como resultado de uma avaliação de efetividade, custo-benefício técnico, um problema que precisa ser resolvido, uma ação necessária como resposta a um risco que excede os limites aceitáveis ou uma nova oportunidade ou aprovação para avanço do projeto para a próxima fase do ciclo de vida. As diretrizes organizacionais ou do projeto determinam o grau de rigor e formalismo a ser aplicado a análise de decisão.

  - 2) Identificar as circunstâncias e a necessidade de decisão.
NOTA Os problemas ou oportunidades e as alternativas que irão resolver seus resultados são registrados, categorizados e reportados.

  - 3) Envolver os stakeholders pertinentes na tomada de decisão de forma a aproveitar sua experiência e conhecimento.
NOTA É uma boa prática identificar a experiência necessária no assunto para a análise e a decisão.

- b) Analisar as informações da decisão. Esta atividade consiste nas seguintes tarefas:
  - 1) Selecionar e declarar a estratégia de gerenciamento de decisão para cada decisão.
NOTA O grau de rigor requerido para resolver estes problemas ou oportunidades é determinado, bem como análise de dados e sistemas necessários para avaliar as alternativas. Definir o prazo para chegar a uma decisao.

  - 2) Determinar resultados desejados e critérios de seleção mensuráveis.
NOTA O valor desejado para critérios quantificáveis e o(s) valor(es) limítrofe(s) além dos quais o atributo será considerado insatisfatório são determinados, bem como os fatores de ponderação para os critérios.

  - 3) Identificar o ambiente (trade space) e as alternativas.
NOTA Se existe um grande número de alternativas, elas são avaliadas qualitativamente de forma a reduzi-las a um número gerenciável para posterior análise de sistemas detalhada. Esta análise é frequentemente baseada em avaliações qualitativas de fatores como risco, custo, cronograma e impactos regulatórios.

  - 4) Avaliar cada alternativa em relação aos critérios.
NOTA O Processo de Análise de Sistema é usado, conforme necessário, para quantificar critérios especificos para cada alternativa a ser avaliada. Isto inclui novos parâmetros de design, diferentes características de arquitetura e a faixa de valores para características críticas de qualidade. O Processo de Análise de Sistema avalia a faixa de variação dos parâmetros de forma a obter uma análise de sensibilidade para cada uma das alternativas avaliadas. Estes resultados são usados para estabelecer a viabilidade das várias alternativas.

- c) Tomar e gerenciar decisões. Esta atividade consiste nas seguintes tarefas:
  - 1) Determinar a alternativa mais adequada para cada decisão.
NOTA As alternativas são avaliadas quantitativamente, usando os critérios de seleção. A alternativa selecionada geralmente fornece uma otimização de, ou a melhoria em, uma decisão identificada.

  - 2) Registrar a resolução, a lógica de decisão e as premissas.
  - 3) Registrar, rastrear, avaliar e reportar as decisões.
NOTA 1 Isto inclui registros de problemas e oportunidades e suas disposições, conforme estipulado em acordos ou procedimentos organizacionais, e de forma que permita auditar e aprender com a experiência.

NOTA 2 Isto permite que a organização confirme que os problemas foram efetivamente resolvidos, que tendências adversas foram revertidas e que se obteve vantagem das oportunidades.


### 6.3.4 Processo de Gestão de Riscos


#### 6.3.4.1 Propósito

O propósito do Processo de Gestão de Riscos é identificar, analisar, tratar e monitorar continuamente os riscos.

O Processo de Gestão de Riscos é um processo contínuo para tratar sistematicamente os riscos ao longo de todo o ciclo de vida do produto ou serviço de um sistema. Pode ser aplicado a riscos relacionados à aquisição, ao desenvolvimento, à manutenção ou à operação de um sistema.

Riscos são definidos no ABNT ISO Guia 73:2009 como O efeito da incerteza nos objetivos. Ele tem uma Nota 1 anexada: "Um efeito é um desvio em relação ao esperado - positivo e/ou negativo. Um risco positivo é normalmente conhecido como uma oportunidade e pode ser tratado pelo Processo de Gestão de Riscos.


#### 6.3.4.2 Resultados esperados

Como resultado da implementação bem-sucedida do processo Gestão de Riscos:

- a) Os riscos são identificados.
- b) Os riscos são analisados.
- c) As opções de tratamento dos riscos são identificadas, priorizadas e selecionadas.
- d) O tratamento adequado é implementado.
- e) Os riscos são avaliados em relação a mudanças de status e progresso do tratamento.

#### 6.3.4.3 Atividades e tarefas

O projeto deve implementar as seguintes atividades e tarefas de acordo com as políticas e os procedimentos organizacionais aplicáveis relacionados ao Processo de Gestão de Riscos.

NOTA A ISO/IEC/IEEE 16085 fornece um conjunto mais detalhado de atividades e tarefas de gestão de riscos. Este processo está alinhado com a ABNT NBR ISO 31000:2009 Gestão de Riscos - Princípios e Diretrizes e o ABNT ISO Guia 73:2009 Gestão de Riscos - Vocabulário. A ABNT NBR ISO 9001:2015 descreve o planejamento de riscos e oportunidades na seção 6.1.

- a) Planejar a gestão de riscos. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir a estratégia de gestão de riscos.
NOTA Isto inclui o Processo de Gestão de Riscos dos fornecedores da cadeia de suprimentos, e descreve como os riscos dos fornecedores serão elevados ao(s) próximo(s) nível (eis) para incorporação ao processo de riscos do projeto.

  - 2) Definir e registrar o contexto do Processo de Gestão de Riscos.
NOTA 1 Isto inclui uma descrição das perspectivas dos stakeholders, categorias de riscos e uma descrição (talvez por referência) dos objetivos técnicos e gerenciais, premissas e restrições. As categorias de riscos incluem as áreas técnicas relevantes do sistema de software e facilitam a identificação de riscos ao longo do ciclo de vida do produto. Conforme nota da ABNT NBR ISO 31000:2009, a meta desta etapa é gerar uma lista de riscos abrangente, baseada naqueles eventos que podem criar, melhorar, prevenir, degradar, acelerar ou atrasar o alcance dos objetivos.

NOTA 2 Oportunidades, que são um tipo de risco, fornecem benefícios potenciais ao sistema ou projeto de software. Cada uma das oportunidades almejadas possui riscos associados que prejudicam o objetivo esperado. Isto inclui os riscos associados a não buscar uma oportunidade, bem como os riscos de não obter os seus efeitos.

- b) Gerenciar o perfil de risco. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir e registrar os limites e condições de risco sob as quais um nível de risco pode ser aceito.
  - 2) Estabelecer e manter um perfil de risco.
NOTA O perfil de risco registra: o contexto de gestão de riscos; um registro do status de cada risco, incluindo a probabilidade de ocorrência, consequências e limites de risco; a prioridade baseada nos critérios de risco fornecidos pelos stakeholders; e as requisições de ações junto com o status do seu tratamento. O perfil de risco é atualizado quando há mudanças no status de cada risco. A prioridade no perfil de risco é usada para determinar os recursos para seu tratamento.

  - 3) Fornecer periodicamente o perfil de risco relevante aos stakeholders, com base nas suas necessidades.
- c) Analisar riscos. Esta atividade consiste nas seguintes tarefas:
  - 1) Identificar os riscos nas categorias descritas no contexto de gestão de riscos.
NOTA Os riscos normalmente são identificados por meio de várias análises, como proteção, confiabilidade, segurança e desempenho; tecnologia, arquitetura e avaliações de prontidão; e estudos de mercado. Estes riscos são frequentemente identificados no início do ciclo de vida, e prosseguem sendo identificados na utilização, suporte e desativação do sistema de software. Além disso, os riscos são frequentemente identificados por meio da análise de medições do sistema de software em evolução.

  - 2) Estimar a probabilidade de ocorrência e as consequências de cada risco identificado.
NOTA As consequências de um risco normalmente envolvem impactos técnicos, no cronograma, no custo ou na qualidade.

  - 3) Avaliar cada risco em relação aos seus limites.
  - 4) Para cada risco que sai dos seus limites, definir e registrar medidas e estratégias de tratamento recomendadas.
NOTA Estratégias de tratamento de risco incluem, mas não estão limitadas a eliminar o risco, reduzir sua probabilidade de ocorrência ou severidade da consequência, ou aceitar o risco. Os tratamentos também incluem assumir ou aumentar o risco para buscar uma oportunidade. As medidas fornecem informações sobre a efetividade das alternativas de tratamento.

- d) Tratar os riscos. Esta atividade consiste nas seguintes tarefas:
  - 1) Identificar as alternativas recomendadas para tratamento de risco.
  - 2) Implementar alternativas de tratamento de risco para aqueles que os stakeholders determinam que ações sejam tomadas para torná-lo aceitável.
  - 3) Quando os stakeholders aceitam um risco que sai dos seus limites, considerá-lo de alta prioridade e monitorá-lo continuamente para determinar se ações futuras de tratamento são necessárias ou se houve mudança de prioridade.
  - 4) Uma vez que o tratamento de um risco é selecionado, coordenar as ações de gestão.
NOTA O Processo de Avaliação e Controle de Projeto pode ser aplicado.

- e) Monitorar riscos. Esta atividade consiste nas seguintes tarefas:
  - 1) Monitorar continuamente os riscos e o contexto da gestão de riscos em relação a alterações e avaliar os riscos quando seu status tiver mudado.
  - 2) Implementar e monitorar medidas para avaliar a efetividade do tratamento de riscos.
  - 3) Monitorar continuamente o surgimento de novos riscos e fontes de risco ao longo do ciclo de vida.

### 6.3.5 Processo de Gerenciamento de Configuração


#### 6.3.5.1 Propósito

O propósito do Gerenciamento de Configuração é gerenciar e controlar elementos e configurações do sistema durante o ciclo de vida. O Gerenciamento de Configuração (GC) também gerencia a consistência entre um

O gerenciamento de configuração de software (GCS) aplica-se tanto ao sistema de software como às suas interfaces. O objetivo do gerenciamento da interface é estabelecer acordos com parceiros sobre a troca de dados na comunicação entre sistemas e serviços de software. O Anexo E (ver E.5) fornece um exemplo de uma Visão do Processo de Gerenciamento de Interfaces.

As configurações de software são alteradas por meio da liberação controlada de uma nova versão. O propósito de uma liberação é autorizar e efetuar a disponibilização de um recurso, função ou sistema de software para um propósito específico, com ou sem restrições, para um subconjunto de usuários.


#### 6.3.5.2 Resultados esperados

Como resultado da implementação bem-sucedida do Processo de Gerenciamento de Configuração:

- a) Os itens que requerem gerenciamento de configuração são identificados e gerenciados.
- b) As baselines de configuração são estabelecidas.
- c) As mudanças em itens sob gerenciamento de configuração são controladas.
- d) As informações sobre o status da configuração são disponibilizadas.
- e) As auditorias de configuração requeridas são realizadas.
- f) As liberações e entregas do sistema são controladas e aprovadas.

#### 6.3.5.3 Atividades e tarefas

O projeto deve implementar as seguintes atividades e tarefas de acordo com as políticas e os procedimentos organizacionais aplicáveis relacionados ao Processo de Gerenciamento de Configuração.

NOTA A ISO/IEC/IEEE 19770 fornece procedimentos e requisitos para um sistema de gestão de ativos de TI.

- a) Planejar o gerenciamento de configuração. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir uma estratégia de gerenciamento de configuração, incluindo abordagens para:
Governança de GC, incluindo papéis, responsabilidades e autoridades, obrigações e comitês de controle de configuração (controle de mudanças); e

Consideração do nível de risco e impacto na aprovação de baselines de configuração e solicitações de mudança rotineiras e emergenciais.

NOTA As mudanças rotineiras agendadas para aplicar patches de software usando procedimentos aprovados, ou check-in e check-out de elementos de software em desenvolvimento testados unitariamente, são normalmente executadas automaticamente ou analisadas criticamente e aprovadas diariamente. Por outro lado, mudanças significativas no design do sistema de software com grande impacto no custo e no cronograma do projeto podem envolver análises abrangentes, consultas a fornecedores, análises críticas pelos stakeho/ders e aprovações nos niveis mais altos da organização.

Coordenação de GC em todo o conjunto de organizações adquirentes, fornecedoras e da cadeia de suprimentos, durante a vida do sistema de software ou extensão do acordo ou projeto, conforme apropriado

IV. Controle de acesso, mudanças e desativação de itens de configuração.

v. As baselines necessárias que serão estabelecidas, incluindo critérios ou eventos para iniciar o controle de configuração e manter baselines em evolução.

vi. Controle de licenças de software, direitos referentes a dados e outros ativos com propriedade intelectual.

vii. Frequência, prioridades e conteúdo de versões e liberações de software.

viii. A estratégia de auditoria e as responsabilidades por validar continuamente a integridade e segurança das informações sobre definições de configuração.

ix. Gerenciamento de mudanças, incluindo a preparação dos stakeholders e especialmente dos usuários para mudanças nos sistemas e serviços de software em operação.

NOTA 1 Para sistemas de software complexos, são conduzidos estudos de trade-off, por exemplo, quando for selecionar uma ferramenta automatizada para apoiar as necessidades e escopo de GCS, conforme identificado na estratégia.

NOTA 2 Orientações adicionais sobre atividades de gerenciamento de configuração podem ser encontradas nas ISO 10007, IEEE Std 828 e SAE ANSI/EIA-649-B.

NOTA 3 O SWEBOK, Guide to the Software Engineering Body of Knowledge, descreve mais detalhes sobre GCS. Esta área de conhecimento trata GCS no contexto de um sistema, planejamento de projeto

e processo, plano e estruturação, seleção de ferramentas, controle de subcontratados, inspeções e outras auditorias, itens de configuração e seus relacionamentos, bibliotecas de software e atividades do Processo de Gerenciamento de Configuração.

NOTA 4 A estratégia de GCS normalmente é documentada em um plano, por exemplo, um plano de gerenciamento de configuração, ou algumas vezes em um PGES (Plano de gerenciamento de engenharia de software), PDS (Plano de desenvolvimento de software) ou PGP (Plano de gerenciamento do projeto). O planejamento da estratégia do GCS é coordenado no Processo de Planejamento de Projeto. Ao estabelecer as baselines e as auditorias, o planejamento de GCS é alinhado com o ciclo de vida do software. A frequência das atividades recorrentes de GCS é compatível com a iteração entre fases e processos técnicos. O planejamento de GCS normalmente inclui decidir quando analisar criticamente o gerenciamento de configuração, que condições requerem a sua atualização e quem é autorizado a alterar os planos de GCS e os itens mantidos sob controle de configuração.

  - 2) Definir os procedimentos de armazenamento, arquivamento e recuperação de itens de configuração, artefatos de GCS e registros.
NOTA As localizações e condições de armazenamento para itens de configuração do sistema de software, como código fonte e software executável, são estabelecidas de acordo com níveis de integridade, segurança e proteção estabelecidos.

- b) Executar a identificação de configuração. Esta atividade consiste nas seguintes tarefas:
  - 1) Selecionar os elementos do sistema de software a serem identificados de forma única como itens de configuração sujeitos a controle de configuração.
EXEMPLO Itens de configuração sujeitos a controle de configuração em sistemas de software normalmente incluem: especificações de requisitos de sistema/software, especificações de interface; elementos de produto e de sistema (por exemplo, objetos de software, hardware e serviços) enquanto estiverem em desenvolvimento, configurações de baselines ou versões de software estabelecidas para transição entre fases e conforme liberadas para uso operacional; cópias mestras ("gold") do código fonte ou do software executável para diferentes plataformas ou versões; configurações locais específicas em uso operacional; itens de informação, como acordos, modelos de arquitetura, descrições de serviços e procedimentos operacionais; e itens de sistemas habilitadores.

NOTA 1 A identificação única pode ser aplicada a componentes de software, versões, ou a cópias licenciadas individuais. Os identificadores estão de acordo com padrões relevantes e convenções do setor de produtos, de forma que os itens sob controle de configuração sejam rastreáveis de forma inequívoca ao seu fornecedor e às suas especificações ou descrições registradas. Os itens de informação são frequentemente identificados e gerenciados separadamente de outros itens de configuração.

NOTA 2 Os identificadores de configuração de soffware facilitam a rastreabilidade quando mais de um desenvolvedor esta trabalhando na mesma função do software, de modo que os varios branches de código podem ser remontados e testados com sucesso.

NOTA 3 A ISO/IEC 19770 (múltiplas partes) fornece um sistema de gestão de ativos de TI para rastrear licenças de software.

  - 2) Identificar os atributos dos itens de configuração.
NOTA 1 Os atributos referem-se ao status do item, ou características físicas ou lógicas úteis para gerenciar ou manter o sistema de software. Atributos apropriados podem ser diferentes para itens de configuração de hardware e de software.

NOTA 2 Os atributos e identificadores de configuração podem refletir uma decomposição do sistema de software de forma que os itens de configuração sejam rastreados até o nível em que as mudanças necessitem ser controladas.

EXEMPLO Softwares de fornecedores externos podem ser rastreados por seus acordos de licenciamento e manutenção, que podem envolver o rastreamento até a localização, número ou tamanho de sistemas onde são usados ou o número permitido de usuários concorrentes. As versões do software podem ser rastreadas até os requisitos implementados dos stakeho/ders.

- 3) Definir baselines ao longo do ciclo de vida.
NOTA 1 As baselines capturam a evolução dos status de configuração dos elementos do sistema de software em momentos planejados ou circunstâncias específicas. O conteúdo das baselines é desenvolvido ao longo dos processos técnicos, mas é formalizado em algum momento pelo Processo de Gerenciamento de Configuração. As baselines formam a base para mudanças subsequentes. Baselines selecionadas normalmente tornam-se formalizadas entre o adquirente e o fornecedor, dependendo das práticas da indústria e do envolvimento contratual do adquirente no Processo de Gerenciamento de Configuração. Geralmente, há três principais tipos de baselines em nível de sistema: baseline funcional, baseline alocada e baseline de produto. Estas variam conforme o domínio ou estratégia local.

NOTA 2 O desenvolvimento de sistemas de software frequentemente implica estabelecer múltiplas baselines de desenvolvimento para tratar as necessidades de configuração do software em evolução em pontos chave do ciclo de vida, para, por exemplo, permitir o controle simultâneo de versões do software durante liberações de design, protótipo, integração e testes. Isto pode envolver responsabilidades distribuídas pelo gerenciamento de configuração e limitações de acesso para arquivamentos, por exemplo, em bibliotecas de desenvolvimento ou de teste e na biblioteca mestra de suporte à configuração.

- 4) Obter acordo entre adquirente e fornecedor para estabelecer uma baseline.
NOTA O Processo de Avaliação e Controle de Projeto é usado para estabelecer um acordo. Quando o software está sendo desenvolvido para uso comercial ou interno, o adquirente ou patrocinador do projeto pode ter autoridade para aprovar uma baseline.

Executar o gerenciamento de mudança de configuração. Esta atividade consiste nas seguintes tarefas:

NOTA O gerenciamento de mudança de configuração estabelece procedimentos e métodos para gerenciar mudanças em uma baseline uma vez que ela é estabelecida. Às vezes isto é denominado controle de configuração. O termo 'gerenciamento de mudanças' também é usado para a gerenciar mudanças em procedimentos organizacionais e fluxos de negócio.

- 1) Identificar e registrar Solicitações de Mudança ou Solicitações de Variação.
NOTA Uma solicitação de variação normalmente significa um desvio, exceção ou concessão.

- 2) Coordenar, avaliar e descartar Solicitações de Mudança e Solicitações de Variação.
NOTA 1 A avaliação normalmente inclui análise da fundamentação e da necessidade versus o impacto no software e nos sistemas que interagem entre si, considerando riscos e oportunidades, qualidade, usuários, cronograma e custo. Uma decisão é tomada sobre implementar ou negar uma solicitação de mudança.

NOTA 2 formal do Comitê de Controle de Configuração (CCC). Solicitações de Mudança e Solicitações de Variação frequentemente estão sob controle

- 3) Acompanhar e gerenciar mudanças aprovadas para a baseline, Solicitações de Mudança e Solicitações de Variação.
NOTA 1 Esta tarefa envolve priorização, acompanhamento, agendamento e fechamento de mudanças. Na sequência, as mudanças são realizadas por meio dos Processos Técnicos. Estas mudanças são verificadas ou validadas pelos processos de Verificação e Validação, para ajudar a garantir que as mudanças aprovadas foram corretamente executadas.

NOTA 2 As mudanças e sua fundamentação normalmente são registradas quando aprovadas e concluídas.

- d) Executar controle de liberações. Esta atividade consiste nas seguintes tarefas:
  - 1) Identificar e registrar solicitações de liberação, identificando os elementos do sistema de software.
O modelo de ciclo de vida ajuda a determinar a frequência das liberações iterativas ou incrementais do software. O Processo de Integração é usado para selecionar e configurar um pacote de liberação, versão do software, atualização ou patch. Estas alterações são verificadas ou validadas por meio dos processos de Verificação ou Validação. Mudanças são feitas por meio dos processos

EXEMPLO Liberações para um teste do software, para qualificação do software ou sistema ou outros testes formais, ou para beta teste em ambiente de operação.

  - 2) Aprovar liberações e entregas do sistema de software.
NOTA 1 Liberações frequentemente envolvem priorização, acompanhamento, agendamento e conclusão de mudanças. A aprovação de uma liberação para uso em operação pode incluir aceitação das mudanças verificadas e validadas. Os critérios para aprovação de uma liberação frequentemente incluem planos de rollback ou de contingência para o caso de uma liberação malsucedida.

NOTA 2 Para sistemas de software, ferramentas automatizadas de controle de versão podem ajudar a garantir que somente as versões corretas do código-fonte são acessadas, atualizadas, testadas e documentadas para mudanças aprovadas por pessoal apropriado, e então liberadas.

  - 3) Acompanhar e gerenciar a distribuição de liberações do sistema de software para ambientes especificados ou entregas de software.
NOTA As cópias mestras ou cópias de mudanças incrementais para versões liberadas do software podem ser mantidas por toda a vida do sistema ou projeto em um ambiente controlado. Os fornecedores de soffware frequentemente rastreiam cópias licenciadas entregues ao adquirente para executar a manutenção acordada. A liberação do sistema de software é armazenada e distribuída conforme o acordo e as políticas das organizações envolvidas.

- e) Relatar o status da configuração. Esta atividade consiste nas seguintes tarefas:
  - 1) Desenvolver e manter as informações de status de GCS para os elementos do sistema de software, baselines e liberações.
NOTA 1 O relato do status da configuração fornece dados sobre a situação de produtos controlados, necessários para tomar decisões sobre elementos do sistema ao longo do ciclo de vida do produto. Por exemplo, o status do software pode incluir histórico, situação atual e evolução planejada ao longo das fases do ciclo de vida para as funções do software, e conclusão das atividades de verificação e validação para os elementos do software. As informações sobre o status da configuração permitem avançar e retroceder na rastreabilidade para outros status de configuração. Os registros de status da configuração são mantidos ao longo do projeto ou ciclo de vida do software, e então arquivados conforme acordos, legislação relevante ou práticas organizacionais.

O registro, a recuperação e a consolidação do status da configuração atual e de configurações anteriores são gerenciados para confirmar correção, oportunidade, integridade e segurança das informações. Auditorias são realizadas para verificar a conformidade de uma baseline com uma visão de arquitetura, documentos de controle de interfaces, acordos de licenciamento de software e outros

- 2) Capturar, armazenar e relatar dados do gerenciamento de configuração.
Executar avaliações de configuração. Esta atividade consiste nas seguintes tarefas:

- 1) Identificar a necessidade de auditorias de GCS e agendá-las.
- 2) Verificar se a configuração do produto atende aos requisitos de configuração comparando requisitos, restrições e exceções (variações) com os resultados de atividades de verificação formais, que podem envolver métodos de amostragem.
- 3) Monitorar a incorporação de mudanças de configuração aprovadas.
- 4) Avaliar se o sistema de software atende às capacidades funcionais e de desempenho identificadas para a baseline.
NOTA Esta tarefa pode ser denominada auditoria funcional de configuração (FCA - Functional Configuration Audit), a qual garante que a configuração do produto atende aos requisitos especificados.

- 5) Avaliar se os elementos do sistema de software em operação estão em conformidade com as informações de configuração aprovadas.
NOTA Esta tarefa pode ser denominada auditoria física de configuração (PCA - Physical Configuration Audit). Para itens de software, os critérios para PCA podem incluir se itens de configuração especificados estão instalados em sistemas designados conforme acordo ou licença de software.

- 6) Registrar os resultados das auditorias de GCS e itens de ação para desativação.

### 6.3.6 Processo de Gerenciamento da Informação


#### 6.3.6.1 Propósito

O propósito do processo de Gerenciamento da Informação é gerar, obter, confirmar, transformar, reter, recuperar, disseminar e descartar informações para stakeholders identificados.

O Gerenciamento da Informação planeja, executa e controla o fornecimento de informações inequívocas, completas, verificáveis, consistentes, modificáveis, rastreáveis e apresentáveis aos stakeholders identificados Isto inclui informações técnicas, de projeto, organizacionais, de acordos e de usuários. As informações são frequentemente derivadas de registros de dados da organização, sistemas, processos ou projetos.

NOTA Informações gerenciadas têm estas características de qualidade: inequívocas, completas, verificáveis consistentes, modificáveis, rastreáveis e apresentáveis.


#### 6.3.6.2 Resultados esperados

Como resultado da implementação bem-sucedida do processo de Gerenciamento da Informação:

- a) As informações a serem gerenciadas são identificadas.
- b) As representações das informações são definidas.
- c) As informações são obtidas, desenvolvidas, transformadas, armazenadas, validadas, apresentadas e descartadas.
- d) O status das informações é identificado.
- e) As informações estão disponíveis para stakeholders identificados.

#### 6.3.6.3 Atividades e tarefas

O projeto deve implementar as seguintes atividades e tarefas de acordo com as políticas e os procedimentos organizacionais aplicáveis relacionados ao processo de Gerenciamento da Informação.

NOTA A ISO/IEC/IEEE 15289 resume os requisitos para o conteúdo dos itens de informação (documentação) do processo de ciclo de vida e fornece orientações sobre a sua geração.

- a) Preparar o gerenciamento da informação. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir a estratégia para gerenciamento da informação.
NOTA Informações sobre o mesmo tópico podem ser geradas de maneiras, para públicos e em pontos do ciclo de vida diferentes.

  - 2) Definir os itens de informação que serão gerenciados.
NOTA Isto inclui as informações que serão gerenciadas durante o ciclo de vida do software e possivelmente mantidas por um período posterior. É realizado conforme políticas organizacionais, acordos ou regulamentações.

  - 3) Designar autoridades e responsabilidades pelo gerenciamento da informação.
NOTA Dar a devida atenção à regulamentação relacionada a informações e dados, segurança e privacidade, como por exemplo, propriedade, restrições nos acordos, direitos de acesso e propriedade dos dados, propriedade intelectual e patentes. As informações são identificadas de acordo com as restrições e limitações, quando existirem. Colaboradores com conhecimento de tais itens de informação são comunicados de suas obrigações e responsabilidades.

  - 4) Definir conteúdo, formatos e estrutura dos itens de informação.
NOTA As informações se originam e materializam de várias formas (por exemplo, audiovisual, textual, gráfica, numérica) e meios (por exemplo, eletrônica, impressa, magnética, ótica). São levadas em consideração as restrições organizacionais, por exemplo, infraestrutura, comunicações entre organizações e projetos desenvolvidos de forma distribuída. Padrões e convenções sobre itens de informação relevantes são usados em conformidade com políticas, acordos e restrições legais.

  - 5) Definir ações de manutenção da informação.
NOTA Manutenção da informação inclui revisão do status de informações armazenadas em relação a integridade, validade e disponibilidade. Isto também inclui quaisquer necessidades de replicação ou

transformação para um meio alternativo, conforme necessário, tanto para reter a infraestrutura à medida que a tecnologia evolui para que seja acessada ou migrada para uma tecnologia mais recente.

- b) Executar gerenciamento da informação. Esta atividade consiste nas seguintes tarefas:
  - 1) Obter, desenvolver ou transformar os itens de informação identificados.
NOTA Isto inclui coletar os dados, informações ou itens de informação de fontes apropriadas (por exemplo, resultantes de qualquer processo do ciclo de vida), e escrevê-los, ilustrá-los ou transformá-los em informações úteis para os stakeholders. Isto inclui revisão, validação e edição de informações de acordo com padrões de informação.

  - 2) Manter itens de informação e seus registros de armazenamento, e registrar o status das informações.
NOTA 1 Os itens de informação são mantidos de acordo com seus requisitos de integridade, segurança e privacidade. O status dos itens de informação é mantido (por exemplo, descrição de versão, data de publicação ou de validade, registros de distribuição, classificação de segurança). Informações legíveis são armazenadas e retidas de tal forma que estejam prontamente disponíveis.

NOTA 2 Os dados originais e ferramentas utilizados para transformar as informações, juntamente com a documentação resultante, são colocados sob controle de configuração de acordo com o Processo de Gerenciamento de Configuração. A ISO/IEC/IEEE 26531 fornece requisitos para sistemas de gerenciamento de conteúdo úteis para informações e documentação do ciclo de vida.

  - 3) Publicar, distribuir ou fornecer acesso às informações ou itens de informação a stakeholders identificados.
NOTA As informações são fornecidas a stakeholders identificados de forma apropriada, conforme requerido por cronogramas acordados ou circunstâncias definidas. Os itens de informação incluem a documentação utilizada para certificação, acreditação, licenciamento ou classificação em uma avaliação, conforme requerido.

  - 4) Arquivar informações selecionadas.
NOTA O arquivamento é realizado de acordo com os propósitos de auditoria, retenção do conhecimento e encerramento do projeto. O meio, localização e proteção das informações são selecionados conforme os períodos de armazenamento e recuperação especificados, e com as políticas da organização, acordos e legislação. São adotadas ações para reter os itens de informação necessários após a conclusão do projeto.

  - 5) Descartar informações indesejadas, inválidas ou não validadas.
NOTA Isto é feito conforme políticas da organização e requisitos de segurança e privacidade.


### 6.3.7 Processo de Medição


#### 6.3.7.1 Propósito

O propósito do Processo de Medição é coletar, analisar e relatar dados e informações objetivos para apoiar um gerenciamento eficaz e demonstrar a qualidade dos produtos, serviços e processos.

NOTA As medidas possuem as seguintes características de qualidade: verificáveis, significativas, implementáveis, oportunas e com custo adequado.


#### 6.3.7.2 Resultados esperados

Como resultado da implementação bem-sucedida do Processo de Medição:

- a) As necessidades de informação são identificadas.
- b) Um conjunto apropriado de medidas, baseado nas necessidades de informações, é identificado ou desenvolvido.
- c) Os dados requeridos são coletados, verificados e armazenados.
- d) Os dados são analisados e os resultados interpretados.
- e) Os itens de informação fornecem informações objetivas, que apoiam decisões.

#### 6.3.7.3 Atividades e tarefas

O projeto deve implementar as seguintes atividades e tarefas, de acordo com as políticas e os procedimentos organizacionais aplicáveis relativos ao Processo de Medição.

NOTA 1 A ABNT NBR ISO/IEC 15939 fornece um conjunto mais detalhado de atividades e tarefas de medição, que estão alinhadas com as atividades e tarefas contidas neste documento.

NOTA 2 A ABNT ISO 9001:2015 especifica os requisitos do Sistema de Gestão da Qualidade para medição e monitoramento.

- a) Preparar para medição. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir a estratégia de medição.
  - 2) Descrever as características da organização que são relevantes para a medição, como objetivos técnicos e de negócio.
  - 3) Identificar e priorizar as necessidades de informação.
NOTA As necessidades de informação são baseadas nos objetivos de negócio da organização, nos objetivos do projeto, nos riscos identificados e outros itens relativos a decisões de projeto. As medições podem estar relacionadas a projetos, processos, produtos ou decisões.

  - 4) Selecionar e especificar medidas que satisfazem as necessidades de informação.
NOTA As medidas são definidas de forma que sejam verificáveis e com custo adequado.

  - 5) Definir procedimentos de coleta, análise, acesso e relato.
  - 6) Definir critérios para avaliação dos itens de informação e do Processo de Medição.
  - 7) Identificar e planejar os sistemas ou serviços habilitadores necessários a serem utilizados.
- b) Executar a medição. Esta atividade consiste nas seguintes tarefas:
  - 1) Integrar procedimentos manuais ou automatizados para geração, coleta, análise e relato de dados nos processos relevantes.
NOTA Esta tarefa pode demandar mudanças em outros processos do ciclo de vida para realizar a integração dos procedimentos.

  - 2) Coletar, armazenar e verificar dados.
  - 3) Analisar dados e desenvolver itens de informação.
  - 4) Registrar resultados e informar os usuários das medições.
NOTA Os resultados de análise da medição são relatados aos stakeholders relevantes de uma forma oportuna e utilizável para apoiar tomadas de decisões e auxiliar em ações corretivas, gestão de riscos e melhorias. Os resultados são relatados a participantes de processos de decisão, de revisões técnicas e gerenciais, e dono do processo de melhoria de processos e dono dos produtos (product owner).


### 6.3.8 Processo de Garantia da Qualidade


#### 6.3.8.1 Propósito

O propósito do processo de Garantia da Qualidade é ajudar a garantir a aplicação eficaz do Processo de Gestão da Qualidade da organização para o projeto.

A Garantia da Qualidade foca em fornecer confiança de que os requisitos de qualidade serão satisfeitos. A análise proativa dos processos do ciclo de vida do projeto e seus resultados é realizada para garantir que o produto que está sendo produzido terá a qualidade desejada, e que as políticas e procedimentos da organização e do projeto são seguidos.


#### 6.3.8.2 Resultados esperados

Como resultado da implementação bem-sucedida do processo de Garantia da Qualidade:

- a) Os procedimentos de garantia da qualidade do projeto são definidos e implementados.
- b) Os critérios e métodos para avaliações de garantia da qualidade são definidos.
- c) As avaliações dos produtos, serviços e processos do projeto são executados de forma consistente com as políticas, os procedimentos e os requisitos de gestão da qualidade.
- d) Os resultados das avaliações são fornecidos aos stakeholders relevantes.
- e) Os incidentes são resolvidos.
- f) Os problemas priorizados são tratados.
NOTA Os resultados esperados a) a d) estão alinhados com os resultados esperados das atividades e tarefas do Processo de Gestão da Qualidade.


#### 6.3.8.3 Atividades e tarefas

O projeto deve implementar as seguintes atividades e tarefas de acordo com as políticas e os procedimentos organizacionais aplicáveis relativos ao processo de Garantia da Qualidade.

NOTA O IEEE Std 730-2014, Software Quality Assurance Processes, fornece detalhes adicionais.

- a) Preparar para a garantia da qualidade. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir uma estratégia de Garantia da Qualidade. A estratégia é consistente com as políticas e objetivos organizacionais de Gestão da Qualidade, e inclui:
i. Prioridades para aplicação dos recursos de Garantia da Qualidade aos processos e tarefas que têm impacto mais significativo na qualidade dos produtos e serviços entregues;

ii. Papéis, responsabilidades, responsabilizações e autoridades definidos;

iii. Critérios e métodos de avaliação para processos, produtos e serviços, incluindo critérios para aceitação de produtos ou serviços;

iv. Atividades apropriadas para cada fornecedor (incluindo subcontratados);

v. Atividades requeridas de verificação, validação, monitoramento, medição, análise crítica, inspeção, auditoria e teste específicas para os produtos ou serviços; e

vi. Atividades de resolução de problemas e melhorias de produtos e processos.

NOTA Em projetos de software, atividades e tarefas que têm impacto significativo na qualidade do produto incluem obtenção de acordo para requisitos novos e alterados, execução de análises críticas por pares e testes unitários, análise de relatórios de problemas e feedback dos usuários; validação da conclusão de ações corretivas atribuídas em análises críticas de marcos do projeto, e análise de causas raiz de defeitos.

  - 2) Estabelecer independência da garantia da qualidade em relação a outros processos do ciclo de vida.
NOTA Os recursos para garantia da qualidade frequentemente são alocados por organizações diferentes para independência em relação à gerência do projeto.

- b) Executar avaliações de produtos ou serviços. Esta atividade consiste nas seguintes tarefas:
  - 1) Avaliar produtos e serviços em relação à conformidade com critérios, acordos, normas e regulamentações estabelecidos.
NOTA Esta tarefa inclui verificar se os critérios para aceitação de produtos ou serviços estão refletidos nas atividades de verificação e validação. Requisitos de qualidade de sistemas/software derivados são normalmente associados a características de qualidade durante os processos de definição de requisitos. As ISO/IEC 25010 e ABNT NBR ISO/IEC 25030 fornecem informações adicionais sobre características de qualidade para sistemas/software.

  - 2) Monitorar se a verificação e a validação das saídas dos processos do ciclo de vida são executadas para determinar a conformidade com os requisitos especificados.
- c) Executar avaliações de processos. Esta atividade consiste nas seguintes tarefas:
  - 1) Avaliar a conformidade dos processos de ciclo de vida do projeto.
  - 2) Avaliar a conformidade de ferramentas e ambientes que apoiam ou automatizam o processo.
  - 3) Avaliar a conformidade de processos de fornecedores em relação aos requisitos do processo.
NOTA Considerar itens que os fornecedores são solicitados a fornecer/executar como: um ambiente de desenvolvimento de software colaborativo, medidas de processo ou um processo de riscos. Isto inclui inspeções da implementação de processos em toda a cadeia de fornecimento.

- d) Gerenciar registros e relatórios de GQ. Esta atividade consiste nas seguintes tarefas:
  - 1) Criar registros e relatórios relativos às atividades de garantia da qualidade.
NOTA Criar registros e relatórios de acordo com os requisitos organizacionais, regulatórios e do projeto, usando o Processo de Gerenciamento da Informação.

  - 2) Manter, armazenar e distribuir registros e relatórios.
  - 3) Identificar incidentes e problemas associados a avaliações de produto, serviço e processo.
NOTA Isto inclui a captura de lições aprendidas. As responsabilidades pela resolução são identificadas.

- e) Tratar incidentes e problemas. Esta atividade consiste nas seguintes tarefas:
NOTA 1 Na terminologia de gestão da qualidade, problemas frequentemente são descritos como "não conformidades quando, se não forem tratados, podem causar o fracasso do projeto no atendimento de seus requisitos.

NOTA 2 Para informações adicionais e exemplos de categorias de problemas e classificações de prioridade, ver a ISO/IEC TS 24748-1:2016, Annex C.

  - 1) Registrar, analisar e classificar incidentes.
  - 2) Identificar incidentes selecionados para associar com erros ou problemas conhecidos.
  - 3) Registrar, analisar e classificar problemas.
NOTA Resultados de análises incluem opções de potenciais tratamentos.

  - 4) Identificar causas raiz e tratamento de problemas onde for possível.
  - 5) Priorizar tratamento de problemas (resolução de problemas) e acompanhar ações corretivas.
A implementação é feita nos processos Técnicos, após a iniciação pelo Processo de Avaliação e Controle de Projeto. Procedimentos organizacionais para escalar problemas podem ajudar a focar recursos em resoluções de problemas ainda pendentes.

  - 6) Analisar tendências em incidentes e problemas.
  - 7) Identificar melhorias em processos e produtos que podem prevenir futuros incidentes e problemas.
NOTA O Processo de Gestão de Riscos é usado para tratar riscos e oportunidades. O processo de Gerenciamento de Modelo de Ciclo de Vida é usado para melhorar os processos da organização.

  - 8) Informar stakeholders identificados sobre o status de incidentes e problemas.
  - 9) Acompanhar incidentes e problemas até o seu fechamento.

## 6.4 Processos Técnicos

Os Processos Técnicos são usados para definir os requisitos de um sistema de software, para transformá-los em um produto eficaz, para permitir a reprodução consistente do produto, quando necessário, para usar o produto de software para fornecer os serviços requeridos, para sustentar a operação e para desativar o produto quando ele for retirado de serviço.

Os Processos Técnicos definem as atividades que permitem às funções da organização e do projeto otimizarem os benefícios e reduzirem os riscos decorrentes de decisões e ações técnicas. Estas atividades permitem que os sistemas e serviços de software possuam a pontualidade, disponibilidade, relação custo-benefício, funcionalidade, confiabilidade, capacidade de manutenção, produtividade,

usabilidade e outras qualidades requeridas pelas organizações adquirentes e fornecedoras. Permitem também que os produtos e serviços estejam em conformidade com as expectativas ou requisitos legais da sociedade, incluindo fatores de saúde, segurança, proteção e meio ambiente.

Os Processos Técnicos consistem nos seguintes:

- a) Processo de Análise de Negócio;
- b) Processo de Definição de Necessidades e Requisitos dos Stakeholders;
- c) Processo de Definição de Requisitos de Sistema/Software;
- d) Processo de Definição de Arquitetura;
- e) Processo de Definição de Design;
- f) Processo de Análise de Sistema;
- g) Processo de Implementação;
- h) Processo de Integração;
- 1) Processo de Verificação;
- j) Processo de Transição;
- k) Processo de Validação;
- 1) Processo de Operação;
- m) Processo de Manutenção; e
- n) Processo de Desativação.
NOTA 1 Para sistemas de software, estes processos podem ser aplicados recursivamente em níveis mais abrangentes ou mais detalhados para a concepção e implementação de sistemas de software.

NOTA 2 Para sistemas de software, estes processos são frequentemente executados simultaneamente, iterando entre si para estabelecer uma solução satisfatória em relação aos requisitos, às medidas críticas de desempenho e às características críticas da qualidade. Em qualquer nível de abstração, os requisitos e modelos são construídos de forma consistente por meio de iterações dos processos técnicos aplicáveis. Quando os requisitos e os modelos não puderem ser implementados diretamente, os processos técnicos são aplicados recursivamente em um nível mais detalhado, ou por meio de diferentes visualizações do sistema.

NOTA 3 O conceito de fases do ciclo de vida e a aplicação dos processos técnicos em qualquer fase são descritos em detalhes na ISO/IEC TS 24748-1. Ela tem um conjunto completo de exemplos de fases e de resultados para a execução de processos técnicos dentro de um ciclo de vida de software.

NOTA 4 O gerenciamento de interfaces é um conjunto de atividades que permeiam os processos de engenharia de software. Estas atividades transversais, nos processos Técnico e Gerenciamento Técnico, se aplicam e acompanham como uma visão específica dos processos de sistema e de software. Ver o Anexo E (E.5) para obter um exemplo de uma visão do processo de Gerenciamento de Interface.

NOTA 5 A ABNT NBR ISO/IEC 27002 Código de práticas para controles de segurança da informação e ISO/IEC 27034 segurança de aplicativos fornecem orientações para a aplicação de conceitos de segurança nos processos técnicos de sistemas e de software. Ver o Anexo E (E.6) para obter um exemplo do Visão do Processo de Garantia de Software.


### 6.4.1 Processo de Análise de Negócio ou Missão


#### 6.4.1.1 Propósito

O propósito do Processo de Análise de Negócio ou Missão é definir o problema ou oportunidade de negócio ou missão, caracterizar o espaço da solução e determinar a(s) classe(s) potencial(is) de solução que podem resolver um problema ou tirar proveito de uma oportunidade.

NOTA 1 A análise de negócio ou missão está relacionada com a organização que abrange os stakeholders relacionados às atividades do ciclo de vida do software. Este processo interage com a estratégia da organização, que geralmente está fora do escopo da ABNT NBR ISO/IEC 12207. Os resultados da análise estratégica da organização incluem Conceito de Operações da organização, objetivos e planos estratégicos, novos elementos de mercado ou missão, e problemas e oportunidades identificados. A estratégia da organização estabelece o contexto no qual a análise de negócio ou missão é realizada. O Conceito de Operações da organização está relacionado com a forma de operação da organização pretendida pela liderança. Este conceito descreve as premissas da organização e como ela pretende usar, adquirir ou fornecer o sistema a ser desenvolvido, os sistemas existentes e de possíveis sistemas futuros para apoiar a operação geral ou uma série de operações do negócio. No caso em que, a organização é sistema de interesse, a estratégia da organização faz parte da definição do sistema.

NOTA 2 Este processo tem aplicação durante toda a vida útil da solução do sistema de software e pode ser revisitado se houver mudanças no ambiente, nas necessidades ou outros fatores.

NOTA 3 Em alguns domínios, a Análise de Negócio ou Missão se refere ao conceito de identificação e analise de capacidades necessárias ou desejadas pela organização. Este processo se concentra nas capacidades necessárias e interage com o processo de Gerenciamento de Portfólio para identificar as oportunidades de negócio de acordo com a capacidade. Os problemas ou oportunidades identificados são frequentemente traduzidos em capacidades alvo. Conforme aplicável em um determinado domínio, o espaço do problema ou da oportunidade inclui a capacidade-alvo.


#### 6.4.1.2 Resultados esperados

Como resultado da implementação bem-sucedida do Processo de Análise de Negócio ou Missão

- a) O domínio do problema ou da oportunidade é definido.
- b) O domínio da solução é caracterizado.
- c) Os conceitos operacionais preliminares e outros conceitos nos estágios do ciclo de vida são definidos.
- d) As alternativas de solução candidatas são identificadas e analisadas.
- e) As alternativas de solução candidatas preferidas são selecionadas.
- f) Todos os sistemas e serviços habilitadores necessários para Análise de Negócio ou Missão estão disponiveis.
- g) A rastreabilidade de problemas, as oportunidades de negócios ou missão e as alternativas de classes de solução preferidas são estabelecidas.

#### 6.4.1.3 Atividades e tarefas

O projeto deve implementar as seguintes atividades e tarefas de acordo com as políticas e os procedimentos organizacionais relativos ao Processo de Análise de Negócio ou Missão.

- a) Preparar para Análise de Negócio ou Missão. Esta atividade consiste nas seguintes tarefas:
  - 1) Analisar criticamente os problemas e as oportunidades identificados na estratégia da organização com relação às metas ou objetivos organizacionais desejados.
NOTA Isto inclui problemas ou oportunidades com relação aos negócios ou missão, visão, Conceito de Operações e outras metas e objetivos estratégicos da organização, incluindo deficiências ou lacunas identificadas em capacidades, sistemas, produtos ou serviços existentes.

  - 2) Definir a estratégia de Análise de Negócio ou Missão.
NOTA ISto inclui a abordagem a ser usada para identificar e definir o espaço do problema, caracterizar o espaço da solução e selecionar uma classe de soluçao.

  - 3) Identificar e planejar os sistemas ou serviços habilitadores necessários para dar suporte à análise de negócio ou missão.
NOTA Isto inclui a identificação de requisitos e de interfaces para os sistemas e serviços habilitadores. Sistemas habilitadores para análise de negócio ou missão incluem os sistemas e repositórios de negócio da organização ou outras entidades acessíveis.

  - 4) Obter ou adquirir acesso aos sistemas ou serviços habilitadores a serem utilizados.
NOTA O Processo de Validação é usado para confirmar objetivamente que o sistema habilitador satisfaz o uso pretendido para suas funções habilitadoras.

- b) Definir o espaço do problema ou da oportunidade. Esta atividade consiste nas seguintes tarefas:
  - 1) Analisar reclamações, problemas e oportunidades dos clientes no contexto de fatores relevantes do espaço de negócio.
NOTA 1 Esta análise está focada no entendimento do escopo, embasamento ou fatores que direcionam os problemas ou oportunidades, em oposição à síntese, que é o foco da análise de sistemas e gerenciamento de decisões necessários para estudos de negócios. O foco aqui inclui alterações nos requisitos da missão, oportunidades de negócio, capacidades, melhoria de desempenho ou falta de sistemas existentes, melhoria de segurança e proteção, fatores como custo e eficácia, mudanças na regulamentação, insatisfação do usuário e fatores PESTEL. Fatores relevantes podem ser identificados por meio de análise externa, interna ou SWOT (Forças, Fraquezas, Oportunidades e Ameaças).

NOTA 2 As saídas das análises são consideradas como parte das decisões de Gerenciamento de Portfólio.

  - 2) Definir a missão, o negócio, ou o problema ou a oportunidade operacional.
NOTA Esta definição inclui o contexto e quaisquer parâmetros chave, sem considerar uma solução específica, pois a solução pode ser uma alteração na operação, uma alteração em um produto ou serviço existente, ou um novo sistema.

- c) Caracterizar o espaço da solução. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir conceitos operacionais preliminares e outros conceitos em fases do ciclo de vida.
NOTA 1 Isto envolve a identificação dos principais grupos de stakeholders, como clientes, usuários, administradores, regulamentadores e proprietários de sistemas, que são definidos no Processo de Definição de Necessidades e Requisitos dos Stakeholders.

NOTA 2 Os conceitos preliminares do ciclo de vida incluem conceitos preliminares de aquisição, de implantação, de operação, de suporte e de desativação. Os conceitos de operação incluem modos ou estados operacionais de alto nível, cenários operacionais, casos de uso potenciais, ou uso em uma estratégia de negócio proposta. Estes conceitos permitem análise de viabilidade e avaliação de alternativas. Estes conceitos são posteriormente refinados no Processo de Definição de Necessidades e Requisitos dos Stakeholders.

NOTA 3 O ambiente operacional pode ter vulnerabilidades conhecidas associadas a ameaças de segurança e riscos de proteção específicos. Estas vulnerabilidades precisam ser entendidas em conjunto com o produto em desenvolvimento. As interfaces humanas e do sistema são um elemento do contexto de garantia do sistema, e as vulnerabilidades relacionadas são examinadas no contexto das ameaças de missão crítica.

  - 2) Identificar as classes de solução alternativas candidatas que abrangem o espaço potencial da solução.
NOTA Estas classes podem variar de simples mudanças operacionais a vários desenvolvimentos ou modificações de sistemas de software. Este espaço de solução pode incluir a identificação de ativos, sistemas e produtos de software existentes adequados para reutilização, bem como alterações nos serviços que podem atender às necessidades de modificações operacionais ou funcionais. Isto inclui deduzir quais serviços potenciais esperados serão necessários. A caracterização do espaço da solução geralmente utiliza o Processo de Definição de Arquitetura para obter uma arquitetura do ponto de vista do usuário, resultando em visões da arquitetura (por exemplo, visões de capacidade, de programação e de operação), conforme proposto pela ISO/IEC/IEEE 42010.

- d) Avaliar classes de solução alternativas. Esta atividade consiste nas seguintes tarefas:
  - 1) Avaliar cada classe de solução alternativa.
NOTA 1 Cada classe de solução alternativa é avaliada de acordo com critérios definidos estabelecidos com base na estrategia da organização. A viabilidade da classe de solução e um dos principais critérios de decisão. O processo de Gerenciamento de Portfólio fornece alguns critérios a serem considerados.

O Processo de Análise de Sistema é usado para avaliar o valor de cada critério para cada classe de solução alternativa. São recomendadas avaliações de compromisso de viabilidade econômica. A inclusão do custo como critério ajudará nas decisões de viabilidade financeira. A avaliação de alternativas pode incluir modelagem, simulação, técnicas analíticas ou avaliação de especialistas para compreender os riscos, viabilidade e valor das classes candidatas de soluções alternativa.

  - 2) Selecionar a(s) classe(s) de solução alternativa preferida(s)
NOTA O Processo de Gerenciamento de Decisão é usado para avaliar alternativas e orientar a seleção. As alternativas selecionadas são validadas no contexto da estratégia da organização. Feedback sobre riscos, viabilidade, fatores de mercado e alternativas são fornecidos para atualização da estratégia da organização.

- e) Gerenciar a análise de negócio ou missão. Esta atividade consiste nas seguintes tarefas:
  - 1) Manter a rastreabilidade da análise de negócio ou missão.
NOTA Durante o ciclo de vida, a rastreabilidade bidirecional é mantida entre os problemas e oportunidades de negócio e as classes preferidas de solução alternativas com a estratégia da organização, necessidades e requisitos dos stakeholders e resultados de análise que suportam as decisões.

  - 2) Fornecer os principais artefatos e informações selecionados para baselines.
NOTA O Processo de Gerenciamento de Configuração é usado para estabelecer e manter itens de configuração e baselines. Este processo identifica candidatos para a baseline e o Processo de Gerenciamento da Informação controla os itens de informação.


### 6.4.2 Processo de Definição de Necessidades e Requisitos dos Stakeholders


#### 6.4.2.1 Propósito

O propósito do Processo de Definição de Necessidades e Requisitos dos Stakeholders é definir os requisitos de um sistema que possa fornecer a capacidade necessária aos usuários e outros stakeholders em um ambiente definido.

Este processo identifica os stakeholders, ou classes de stakeholders e suas necessidades ao longo do ciclo de vida. Analisa e transforma estas necessidades em um conjunto comum de requisitos dos stakeholders que expressam a interação pretendida do sistema com o ambiente de operação que são referência para a capacidade operacional resultante ser validada. Os requisitos dos stakeholders são definidos considerando o contexto do sistema de interesse com os sistemas interoperantes e habilitadores.

O SWEBOK, Guide to the Software Engineering Body of Knowledge, área de conhecimento de Requisitos de Software discute os fundamentos dos requisitos (por exemplo, definição, tipos, propriedades, características da qualidade) e outros tópicos, como stakeholders, elicitação, análise e gerenciamento de requisitos que fornecem orientações adicionais para sistemas de software.


#### 6.4.2.2 Resultados esperados

Como resultado da implementação bem-sucedida do Processo de Definição de Necessidades e Requisitos dos Stakeholders:

- a) Os stakeholders do sistema são identificados.
- b) As características necessárias, o contexto de uso das capacidades e conceitos nas fases do ciclo de vida, incluindo conceitos de operação são definidos.
- c) As restrições do sistema são identificadas.
- d) As necessidades dos stakeholders são definidas.
- e) As necessidades dos stakeholders são priorizadas e transformadas em requisitos claramente definidos.
As medidas criticas de desempenho são definidas.

- g) os quaramentos taquilos, sapatançado suas necessidades e expectativas estão refeidas
- h) Todos os sistemas ou serviços habilitadores necessários para as necessidades e requisitos dos stakeholders estão disponiveis.
- i) A rastreabilidade dos requisitos dos stakeholders para suas necessidades é estabelecida.

#### 6.4.2.3 Atividades e tarefas

O projeto deve implementar as seguintes atividades e tarefas de acordo com as políticas e os procedimentos organizacionais aplicáveis relacionados ao Processo de Definição de Necessidades e Requisitos dos Stakeholders.

- a) Preparar para a Definição das Necessidades e Requisitos dos Stakeho/ders. Esta atividade consiste nas seguintes tarefas:
  - 1) Identificar os stakeholders que têm interesse no sistema de software ao longo do seu ciclo de vida.
Isto inclui pessoas e categorias de stakeholders que são usuários, operadores, desenvolvedores, instrutores, equipes de produção, de suporte, de manutenção, de desativação, organizações adquirentes e fornecedoras, responsáveis por interfaces com entidades externas, órgãos reguladores e outros que têm um interesse legítimo no sistema. Nos casos em que a comunicação direta não é possível (por exemplo, para produtos e serviços de consumo), são selecionados representantes ou stakeholders designados por procuração.

  - 2) Estabelecer a estratégia de definição de necessidades e requisitos dos stakeholders.
NOTA Alguns stakeholders têm interesses que se opõem aos interesses do adquirente (por exemplo, concorrentes de mercado, hackers, terroristas) ou entre si. Quando há conflito de interesse entre os stakeholders, mas não em relação ao sistema de software, este processo visa obter consenso entre as categorias de stakeholders para estabelecer um conjunto de requisitos aceitos por todas as partes. As intenções ou desejos daqueles que se opõem aos adquirentes, ou detratores do sistema, são abordados pelo Processo de Gestão de Riscos, análises de ameaças do Processo de Análise de Sistema, ou requisitos de sistema/software para segurança, adaptabilidade ou resiliência. Neste caso, as necessidades dos stakeholders não são satisfeitas, mas tratadas de maneira a ajudar a garantia da segurança e da integridade do sistema, se forem identificadas ações dos detratores.

  - 3) Identificar e planejar os sistemas ou serviços habilitadores necessários para apoiar as necessidades dos stakeholders e a definição de requisitos.
NOTA Isto inclui a identificação de requisitos e interfaces para os sistemas habilitadores. Os sistemas habilitadores para definição das necessidades e requisitos dos stakeholders incluem ferramentas para facilitação e gerenciamento de requisitos.

  - 4) Obter ou adquirir acesso aos sistemas ou serviços habilitadores a serem utilizados.
NOTA O Processo de Validação é utilizado para confirmar objetivamente que o sistema habilitador alcança o uso pretendido para suas funções habilitadoras.

- b) Definir as necessidades dos stakeholders. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir o contexto de uso no âmbito da operação e nos aspectos preliminares do ciclo de vida.
NOTA O contexto de uso geralmente é capturado usando uma Descrição de Contexto de Uso (ver ISO/EC 25063). Os aspectos preliminares do ciclo de vida são desenvolvidos pelo Processo de Análise de Negócio

  - 2) Identificar as necessidades dos stakeholders.
NOTA 1 A identificação das necessidades dos stakeholders inclui a elicitação de necessidades diretamente com os stakeholders, identificação de suas necessidades implicitas com base no conhecimento do domínio e na compreensão do contexto, e de lacunas identificadas a partir de atividades anteriores. As necessidades geralmente incluem medidas de eficácia. A análise funcional

é frequentemente utilizada para auxiliar na elicitação de necessidades. Também as características de qualidade descritas no modelo de qualidade da ISO/IEC 25010, e a aplicação do modelo de qualidade na análise de requisitos da ABNT NBR ISO/IEC 25030 são úteis para extrair e identificar requisitos da qualidade dos requisitos não funcionais, que geralmente são necessidades implícitas dos stakeholders.

NOTA 2 No SWEBOK, Guide to the Software Engineering Body of Knowledge, a área de conhecimento Requisitos de Software discute algumas técnicas adicionais para elicitar e clarificar requisitos de software, como prototipagem, observação, histórias de usuários, mineração de dados e análise de produtos de concorrentes, para determinar funcionalidades requeridas.

As necessidades dos stakeholders descrevem as suas necessidades, vontades, desejos, expectativas e restrições. A compreensão das necessidades dos stakeholders, quanto aos requisitos mínimos de segurança e privacidade necessários para o ambiente de operação, minimiza o potencial de desvios nos planos, cronogramas e desempenho. Se houver a possibilidade de surgirem problemas significativos em relação aos usuários e outros stakeholders na utilização do sistema de software, recomendações para identificar e tratar questões relativas à interação homem-sistema podem ser

  - 3) Priorizar e classificar necessidades.
NOTA O Processo de Gerenciamento de Decisão geralmente é utilizado para dar suporte à priorização. O Processo de Análise de Sistema é utilizado para analisar a viabilidade das necessidades ou outros fatores.

  - 4) Definir as necessidades e as justificativas dos stakeholders.
NOTA As necessidades se concentram no objetivo e no comportamento do sistema e são descritas no contexto do ambiente e condições de operação. É útil rastrear as necessidades para suas fontes e justificativas dos stakeholders.

- c) Desenvolver o conceito de operação e outros conceitos do ciclo de vida. Esta atividade consiste nas seguintes tarefas:
Outros conceitos de ciclo de vida podem incluir conceitos de aquisição, de implantação, de suporte, de segurança e de desativação. Nesta atividade, os conceitos preliminares do ciclo de vida definidos no Processo de Análise de Negócio são desenvolvidos posteriormente no contexto de necessidades específicas dos stakeholders, à medida que cenários e interações associados são definidos. Ver a ISO/IEC/IEEE 29148: 2011, Seções 5 e 6 para obter mais informações sobre conceitos de operações, e o Anexo A da mesma Norma para obter um esboço comentado de um Conceito de Operação de Sistema.

  - 1) Definir um conjunto representativo de cenários para identificar as capacidades necessárias que correspondem aos conceitos operacionais e de ciclo de vida previstos.
NOTA 1 Os cenários são utilizados para analisar a operação do sistema em seu ambiente pretendido, a fim de identificar necessidades ou requisitos adicionais que talvez não tenham sido explicitamente identificados por nenhum dos stakeholders, por exemplo, obrigações legais, regulatórias e sociais. O contexto de utilização do sistema é identificado e analisado, incluindo as atividades que os usuários executam para atingir os objetivos do sistema, as características relevantes dos usuários (por exemplo, treinamento e conhecimento esperados, frequência de uso do sistema, responsabilidades, preocupações de acessibilidade), o ambiente físico (por exemplo, luz disponível, temperatura) e qualquer equipamento a ser usado (por exemplo, equipamento de proteção ou de comunicação). As influências sociais e organizacionais sobre os usuários que afetam o uso do sistema ou restringem seu design são analisadas quando aplicável. Cenários centrados em invasores, seus ambientes, ferramentas, técnicas e capacidades são considerações-chave para o desenvolvimento do conceito de operação. Os cenários são priorizados para refletir a importância ponderada das várias necessidades de operação.

NOTA 2 Estes cenários geralmente motivam atualizações nos conceitos de operação ou outros conceitos do ciclo de vida. Os cenários de abuso e de falha destacam a necessidade de requisitos funcionais adicionais (ou requisitos derivados mais específicos) para mitigar os riscos identificados nestes cenários.

  - 2) Identificar os fatores que afetam as interações entre os usuários e o sistema.
i. Antecipar capacidades físicas, mentais e de aprendizado dos usuários;

Local de trabalho, ambiente e instalações, incluindo outros equipamentos no contexto de uso;

Condições normais, incomuns e de emergência; e

iv. Recrutamento, treinamento e cultura de operadores e usuários.

NOTA 1 Os requisitos de usabilidade consideram as capacidades e as limitações de habilidades humanas. Onde possível, são utilizados padrões aplicáveis, por exemplo, ABNT NBR ISO 9241 e práticas profissionais aceitas.

NOTA 2 Se a usabilidade for importante, os requisitos de usabilidade são planejados, especificados e implementados por meio dos processos do ciclo de vida. Ver a ISO TS 18152 para informações sobre questões relativas à interação homem-sistema e a ISO/IEC 25060: 2010 para informações sobre usabilidade.

- d) Transformar necessidades dos stakeholders em requisitos dos stakeholders. Esta atividade consiste nas seguintes tarefas:
  - 1) Identificar as restrições em uma solução do sistema.
NOTA Estas restrições podem resultar de 1) instâncias ou áreas de solução definida pelos stakeho/ders; 2) decisões de implementação tomadas em altos nível na estrutura hierárquica do sistema;

  - 3) uso requerido de sistemas habilitadores, legados ou de interface, elementos do sistema, recursos e equipe definidos; ou 4) objetivos de viabilidade econômica definidos pelos stakeholders. Incluindo as restrições que são consequências inevitáveis de acordos existentes, decisões gerenciais e técnicas.
  - 2) Identificar os requisitos e funções dos stakeholders que se relacionam com características críticas de qualidade, como garantia, proteção, segurança, meio ambiente ou saúde.
NOTA 1 Ver a ISO/IEC/IEEE 15026 para informações adicionais sobre garantia de sistema e software.

NOTA 2 A identificação de riscos de proteção facilita a identificação de requisitos e funções de proteção. Os riscos de proteção incluem aqueles associados a métodos de operações e de suporte, saúde e proteção, ameaças à propriedade e influências ambientais. Usar os padrões aplicáveis e práticas profissionais aceitas. Por exemplo, a IEC 61508:2010, Functional safety of electrical/electronic/ programmable electronic safety-related systems, fornece requisitos detalhados.

NOTA 3 A identificação de riscos à segurança facilita a identificação de requisitos e funções adicionais de segurança. Se necessário, incluir áreas aplicáveis de segurança do sistema, como física, procedural, comunicações, computadores, programas, dados e emissões. Isto inclui acesso e danos a pessoas protegidas, propriedades e informações, comprometimento de informações sensíveis e negação do acesso aprovado a propriedades e informações. Isto também inclui as funções de segurança necessárias, como mitigação e contenção, padrões de referência aplicáveis e práticas profissionais aceitas, quando obrigatórias ou relevantes. Ver o Anexo E (E.6) para obter uma visão de garantia de software do ciclo de vida.

NOTA 4 Ver a ISO/IEC 25030 para mais informações sobre características de qualidade sob uma perspectiva de qualidade em uso.

  - 3) Definir os requisitos dos stakeholders, consistentes com os conceitos do ciclo de vida, cenários, interações, restrições e características críticas de qualidade.
NOTA 1 Ver a ISO/ IEC/IEEE 29148:2011, Seções 5 e 6, para mais informações sobre os requisitos dos stakeholders, e as seções 8 e 9 para uma descrição e um esboço comentado de uma especificação de requisitos dos stakeholders.

NOTA 2 Os requisitos dos stakeho/ders são analisados criticamente nos momentos-chave de decisão no ciclo de vida para ajudar a garantir que as mudanças nas necessidades sejam levadas em conta.

Os requisitos dos stakeholders são registrados de forma adequada ao gerenciamento de requisitos durante o ciclo de vida. Estes registros estabelecem a baseline dos requisitos dos stakeholders e retêm as mudanças de necessidade e sua origem ao longo do ciclo de vida do software. Estes registros são a base para a rastreabilidade das decisões tomadas pelo Processo de Análise de Negócio, bem como para necessidades dos stakeholders, requisitos do sistema e elementos subsequentes do sistema de software.

NOTA 4 Os requisitos dos stakeholders são a base dos critérios de validação para o sistema de software e seus elementos.

- e) Analisar requisitos dos stakeholders. Esta atividade consiste nas seguintes tarefas:
  - 1) Analisar o conjunto completo de requisitos dos stakeholders.
NOTA 1 Os requisitos dos stakeholders são analisados quanto a características de requisitos individuais, bem como características do conjunto de requisitos. As características potenciais da análise incluem: que os requisitos são necessários, independentes de implementação, não ambíguos, consistentes, completos, únicos, factíveis, rastreáveis, verificáveis, economicamente viáveis e dentro do escopo. A ISO/IEC/IEEE 29148 fornece informações adicionais sobre características de requisitos.

NOTA 2 O Processo de Análise de Sistema é usado para avaliar a exequibilidade e a viabilidade econômica. Os processos de Verificação e Validação são usados na análise crítica dos requisitos dos stakeholders.

  - 2) Definir medidas críticas de desempenho que permitem a avaliação do progresso técnico.
NOTA Isto inclui a definição de medidas técnicas, de qualidade e parâmetros críticos de desempenho associados a cada medida de eficácia identificados nos requisitos dos stakeholders. As medidas críticas de desempenho (por exemplo, medidas de eficácia e de adequação) são definidas, analisadas e avaliadas para ajudar a assegurar que os requisitos dos stakeholders sejam atendidos e ajudar a assegurar a identiticaçao do custo do projeto, o cronograma ou o risco de desempenho associado e utilizar medidas adequadas. A INCOSE TP-2003-020-01, Technical Measurement, fornece informações a qualquer não conformidade. AABNT NBR ISO/IEC 15939 fornece um processo para identificar, definir

sobre a seleção, definição e implementação de medidas críticas de desempenho. A série de normas ISO/IEC 25000 fornece medidas relevantes de qualidade.

  - 3) Dar feedback sobre os requisitos analisados aos stakeholders pertinentes para validar se suas necessidades e expectativas foram adequadamente capturadas e expressas.
  - 4) Resolver questões relativas aos requisitos dos stakeholders.
NOTA Isto inclui requisitos que violam as características para os requisitos individuais ou o conjunto de requisitos, conforme definido na ISO/IEC/IEEE 29148.

- f) Gerenciar a definição de necessidades e requisitos dos stakeholders. Esta atividade consiste nas seguintes tarefas:
  - 1) Obter acordo explícito com os stakeholders designados sobre os requisitos dos stakeholders.
NOTA Isto inclui confirmar que os requisitos dos stakeholders estão expressos corretamente, são compreensíveis para seus declarantes, e que a resolução de conflitos relativos aos requisitos não tenha corrompido ou comprometido intenções dos stakeholders.

  - 2) Manter a rastreabilidade das necessidades e requisitos dos stakeholders.
NOTA Durante o ciclo de vida, a rastreabilidade bidirecional é mantida entre as necessidades e requisitos dos stakeholders, estratégia organizacional, problemas e oportunidades de negócio e de missão. Os requisitos dos stakeholders são rastreados para os requisitos do sistema/software durante o processo de Definição de Requisitos de Sistema/Software. A rastreabilidade é por vezes mantida usando um repositório de dados apropriado.

  - 3) Fornecer artefatos-chave e itens de informação que foram selecionados para baselines.
NOTA O Processo de Gerenciamento de Configuração é usado para estabelecer e manter os itens de configuração e as baselines. Este processo identifica candidatos para baselines, e o processo de Gerenciamento da Informação controla os itens de informação. Para este processo, as necessidades e os requisitos dos stakeholders, e conceito operacional são itens de informação típicos que são colocados sob baseline.


### 6.4.3 Processo de definição de requisitos de Sistema/Software


#### 6.4.3.1 Propósito

O propósito do processo de Definição de Requisitos de Sistema/Software é transformar as capacidades desejadas pelo stakeholder, visão orientada ao usuário, em uma visão técnica de uma solução que atenda às necessidades operacionais do usuário.

Este processo cria um conjunto de requisitos de sistema mensuráveis que especificam, do ponto de vista do fornecedor, quais as características, atributos e requisitos funcionais e de desempenho do sistema, a fim de satisfazer os requisitos dos stakeholders. Se houver restrições em relação aos requisitos, não é conveniente que os mesmos sejam implementados.

NOTA 1 A partir de uma visão de alto nível do sistema de software, este processo pode ser usado para definir os requisitos gerais do sistema. Como o sistema de software é decomposto em elementos, cada elemento, por sua vez, é tratado como um sistema, função ou conjunto de funções e este processo pode ser usado para detalhar os requisitos. Análises e ferramentas de requisitos suportam a rastreabilidade de requisitos entre o sistema de software e seus elementos.

NOTA 2 O SWEBOK, Guide to the Software Engineering Body of Knowledge, a Área de Conhecimento Requisitos de Software discute a definição, análise, modelagem, especificação, validação, gerenciamento de requisitos de software e outros tópicos que fornecem orientação adicional para sistemas de software.

NOTA 3 A redação dos resultados do processo de Definição de Requisitos de Sistema/Software difere ligeiramente dos resultados do processo de Definição de Requisitos de Sistema da ISO/IEC/IEEE 15288:2015. O uso do termo Requisitos de sistema/software enfatiza a aplicabilidade deste documento a sistemas de software, tendo requisitos de software e requisitos de sistemas. Este processo pretende apoiar os usuários que definem requisitos de sistemas e de software hierarquicamente ou em diferentes estágios.


#### 6.4.3.2 Resultados esperados

Como resultado da implementação bem-sucedida do processo de Definição de Requisitos de Sistema/Software:

- a) A descrição do sistema ou elemento, incluindo as interfaces, funções e fronteiras para uma solução de sistema é definida.
- b) Os requisitos de sistema/software (funcionais, de desempenho, de processo, não funcionais e de interface) e restrições de design são definidos.
- c) As medidas críticas de desempenho são definidas.
- d) Os requisitos de sistema/software são analisados.
Quaisquer sistemas ou serviços habilitadores necessários para a definição de requisitos de sistema/software estão disponíveis.

- f) A rastreabilidade de requisitos de sistema/software para os requisitos dos stakeholders é desenvolvida.

#### 6.4.3.3 Atividades e tarefas

O projeto deve implementar as seguintes atividades e tarefas de acordo com as políticas e os procedimentos organizacionais aplicáveis relacionados ao processo de Definição de Requisitos de Sistema/Software.

- a) Preparar para a Definição de Requisitos de Sistema/Software. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir a fronteira funcional do sistema de software ou elemento em termos de propriedades e comportamentos fornecidos.
NOTA A definição de fronteira funcional é parcialmente baseada no contexto de uso e cenários operacionais definidos no contexto do processo de Definição de Requisitos e Necessidades dos Stakeho/ders. Isto inclui os estímulos (entradas) do sistema de software e suas respostas aos usuários e aos sistemas externos, e uma análise e a descrição das interações necessárias entre o sistema de software e seu ambiente operacional, em termos de propriedades e restrições de interface, como: fluxos de procedimentos, chamadas, formatos e fluxos de dados, desempenho (throughput) e no tempo correto. Isto estabelece o comportamento esperado do sistema de software, expresso em termos quantitativos, nas suas fronteiras. Para software, as fronteiras são comumente expressas em Application Program Interfaces (API) e interface gráfica do usuário (GUI - Graphical User Interface) ou arquivos ou serviços de interface, incluindo formatos de dados. O Anexo E (E.5) fornece uma visão do gerenciamento de interface dos processos do ciclo de vida.

  - 2) Definir a estratégia de definição de requisitos do sistema/software.
NOTA Isto inclui a abordagem a ser utilizada para identificar, definir e gerenciar os requisitos do sistema/software de acordo com o modelo de ciclo de vida selecionado, por exemplo, evolutivo, incremental ou iterativo. Muitos fatores podem influenciar a estratégia, por exemplo, complexidade do sistema de software e das informações e funções a serem gerenciadas; necessidade de acesso disponível e entendimento comum por vários membros da equipe; grau de envolvimento colaborativo do adquirente ou dos representantes dos usuários durante toda a fase de desenvolvimento; se o projeto envolve um novo desenvolvimento, uma modificação, reutilização ou integração dos sistemas existentes; e requisitos de documentação do processo, incluindo o período de retenção. O modelo de ciclo de vida irá influenciar quando e quantas vezes a Definição de Requisitos de Sistema/Software será realizada. O Anexo H descreve o desenvolvimento progressivo de requisitos em projetos que usam métodos ágeis.

  - 3) Identificar e planejar os sistemas ou serviços habilitadores necessários para apoiar a definição de requisitos de sistema/software.
NOTA Isto inclui a identificação de requisitos e interfaces para sistemas habilitadores. Sistemas habilitadores para definição de requisitos incluem ferramentas para facilitação e gerenciamento de requisitos. Ferramentas para gerenciamento de requisitos de software que são integradas com o desenvolvimento, teste e gerenciamento de configuração de software podem simplificar o rastreamento e agilizar a construção de software. Planos para sistemas habilitadores e descrição de técnicas de modelagem usados em apoio ao processo de Definição de Requisitos de Sistema/Software podem ser incorporados no Processo de Desenvolvimento de Software.

  - 4) Obter ou adquirir acesso aos sistemas ou serviços habilitadores a serem utilizados.
NOTA O processo de validação é utilizado para confirmar objetivamente que o sistema habilitador atinge o uso pretendido para suas funções habilitadoras.

- b) Definir requisitos de sistema/software. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir cada função a ser executada para o sistema de software ou elemento.
NOTA 1 As funções de software podem ser descritas em casos de uso, histórias de usuários ou cenários e envolvem a transformação de dados e informações para atender às necessidades do usuário (requisitos dos stakeholders). Em alguns casos, as funções são derivadas da análise de características críticas da qualidade, como desempenho, segurança ou disponibilidade (por exemplo, função de diagnóstico do sistema ou backup de dados para confiabilidade).

NOTA 2 As funções habilitadoras necessárias para apoiar o sistema de interesse no atendimento de sua funcionalidade também são identificadas e definidas simultaneamente com a função do sistema de interesse. Isto é necessário para ajudar a garantir que as funções habilitadoras no ambiente do sistema sejam identificadas e consideradas.

  - 2) Identificar os estados ou modos de operação requeridos do sistema de software.
NOTA 1 Os estados ou modos de operação podem ser modelados e representados em várias técnicas e perspectivas de modelagem para fornecer uma descrição suficientemente completa dos requisitos de sistema ou de elemento desejados.

NOTA 2 As condições para desempenho de funções geralmente envolvem interoperabilidade entre funções ou elementos. Alguns requisitos de software (por exemplo, tempo de resposta) podem ser alocados entre vários elementos do sistema de software, afetando o tratamento do requisito em um caso de teste ou teste de regressão.

  - 3) Definir restrições de implementação necessárias.
NOTA Para elementos de software, isto inclui as decisões de implementação que são alocadas da definição da arquitetura em níveis mais altos no sistema de software, introduzidas pelos requisitos dos stakeholders ou pelas limitações da solução. As restrições de implementação incluem as condições sob as quais o sistema deve ser capaz de executar a função, as condições sob as quais o sistema deve começar a executar esta função (entrada) e as condições sob as quais o sistema deve parar de executar esta função (saída).

  - 4) Identificar requisitos relacionados a riscos, criticidade do sistema de software ou características críticas da qualidade.
NOTA 1 Requisitos não funcionais e características críticas da qualidade em sistemas de software geralmente incluem aqueles relacionados a saúde, proteção, segurança e garantia do software,

confiabilidade, disponibilidade e capacidade de suporte (capacidade de manutenção) e restrições de tempo para taxa de transferência e desempenho. O Processo de Análise de Sistema pode ser usado para determinar valores apropriados para os requisitos de desempenho, considerando o custo previsto para alcançá-los e seu impacto na operação e uso do sistema.

NOTA 2 A análise e definição de considerações de proteção incluem os requisitos relacionados a métodos de operação e manutenção, influências ambientais e risco de lesões de pessoas. Isto também inclui a expressão de cada função relacionada à proteção e sua integridade associada, em termos da necessária redução de riscos e alocação a sistemas de proteção designados. São utilizadas normas aplicáveis em relação à proteção funcional, por exemplo, IEC 61508, e proteção ambiental, por exemplo, ABNT NBR ISO 14001. A análise inclui considerações de segurança, por exemplo, aquelas relacionadas a comprometimento e proteção de informações, dados e materiais sensíveis. Os riscos relacionados à segurança são definidos, incluindo fatores administrativos, de pessoal, físicos, de computador, de comunicação, de rede, de emissões e ambientais, usando, conforme apropriado, as normas de segurança aplicáveis. Ver a ISO/IEC/IEEE 15026-4 para orientações sobre garantia de sistema e software. A ISO/IEC 27036 fornece orientação para requisitos de segurança da informação na terceirização de produtos e serviços. A ISO 25030 fornece orientação para fatores e características externos da qualidade do sistema. O Anexo E (E.6) fornece uma visão de garantia de software sobre os processos do ciclo de vida.

NOTA 3 Para sistemas de software destinados à interação humana, são consideradas especificações de engenharia de fatores humanos (ergonomia). Para sistemas que possuem requisitos de usabilidade, as recomendações para obter o nível desejado de usabilidade podem ser encontradas na ISO 9241-220, Ergonomics of human-system interaction - Part 220: Processes for enabling, executing and assessing human-centred design within organizations.

- 5) Definir requisitos de sistema/software e atributos de requisitos, incluindo os seguintes:
Elementos de dados, estruturas e formatos de dados, e requisitos de banco de dados ou de retenção de dados;

iL. Interfaces e documentação do usuário (informações para usuários) e treinamento do usuário;

Interfaces com outros sistemas e serviços;

iv. Funções e características não funcionais, incluindo características críticas da qualidade e metas de custo;

v. Transição de processos e dados de operação de sistemas existentes manuais e automatizados, abordagem de migração, cronograma, instalação do software e aceitação do produto; e

vi. Atributos de requisitos, como: fundamentação; prioridade; rastreabilidade para elementos do sistema de software, casos de teste e itens de informação; métodos de verificação; inclusão em baselines aprovadas; e risco avaliado.

NOTA 1 A definição de requisitos envolve etapas iterativas e recursivas em paralelo com outros processos do ciclo de vida. Dependendo do modelo de ciclo de vida que está sendo utilizado, é útil comparar os recursos a serem aplicados para garantir a correção inicial dos requisitos versus os recursos necessários para evoluir os requisitos com base nos resultados de verificação e validação.

Os requisitos e atributos do sistema/software são registrados com um nível de detalhe e de uma forma adequada para o gerenciamento de requisitos ao longo do ciclo de vida. Ver a ISO/EC/EEE 29148, Seções 5 e 6, para mais informações sobre requisitos, e as seções 8 e 9 para obter uma descrição e um esboço comentado de uma Especificação de Requisitos de Sistema e uma Especificação de Requisitos de Software.

- c) Analisar requisitos de sistema/software. Esta atividade consiste nas seguintes tarefas:
  - 1) Analisar o conjunto completo de requisitos de sistema/software.
Os requisitos são analisados quanto a características de requisitos individuais, bem como características do conjunto de requisitos. As características potenciais da análise incluem: que os requisitos são necessários, independentes de implementação, não ambíguos, consistentes, completos, unicos, factiveis, rastreaveis, verificáveis, economicamente viáveis e dentro do escopo. O processo de verificação é usado para determinar se os requisitos atendem aos atributos e caracteristicas de bons requisitos. Em alguns casos, a viabilidade técnica e econômica de validar e verificar formulações alternativas de requisitos é avaliada. A ISO/IEC/IEEE 29148 fornece informações adicionais sobre características de requisitos.

NOTA 2 O Processo de Análise de Sistema pode ser usado para avaliar a viabilidade técnica e econômica, balanceamento e outras características dos requisitos. O Processo de Análise de Sistema é usado para determinar valores apropriados para os parâmetros de requisitos considerando o custo estimado, o cronograma e o desempenho técnico do sistema de software.

NOTA 3 Considerando que alguns requisitos podem ser atendidos de forma incremental, ou mesmo postergados ou dispensados, pode ser feita a sua priorização.

  - 2) Definir medidas críticas de desempenho que permitam avaliar as realizações técnicas.
NOTA Isto inclui definir medidas técnicas, da qualidade e parâmetros críticos de desempenho associados a cada medida de eficácia identificada nos requisitos dos elementos do sistema de software. As medidas críticas de desempenho (por exemplo, medidas de desempenho e medidas técnicas de desempenho) são analisadas e revisadas para ajudar a garantir que os requisitos do sistema/software sejam atendidos e para garantir a identificação do custo do projeto, cronograma ou risco de desempenho associado a qualquer não conformidade. A ABNT NBR ISO/EC 15939 fornece um processo para identificar, definir e usar as medidas apropriadas. A INCOSE TP-2003-020-01, Technical Measurement, fornece informações sobre a seleção, definição e implementação de medidas críticas de desempenho. A série de normas ISO/IEC 25000 fornece medidas relevantes da qualidade.

  - 3) Dar feedback sobre os requisitos analisados aos stakeholders pertinentes para revisão.
O feedback ajuda a validar que os requisitos especificados foram capturados e expressos adequadamente. A confirmação é de que são uma resposta necessária e suficiente aos requisitos dos stakeholders e uma entrada necessária e suficiente para outros processos, em particular arquitetura, design e verificação de software. O processo de validação é usado para determinar se os requisitos

  - 4) Identificar e resolver problemas, deficiências, conflitos e pontos fracos dentro do conjunto completo de requisitos.
NOTA Isto inclui requisitos que não são verificáveis, ambíguos, violam as características de requisitos individuais ou são inconsistentes com outros no conjunto de requisitos. A resolução de problemas com requisitos pode ser iterativa em certos modelos de ciclo de vida.

- d) Gerenciar requisitos de sistema/software. Esta atividade consiste nas seguintes tarefas:
NOTA A manutenção dos requisitos de sistema/software inclui definir, registrar e controlar a baseline, geralmente sob gerenciamento formal de configuração, juntamente com o gerenciamento de alterações resultantes da aplicação de outros processos do ciclo de vida, como arquitetura ou design.

  - 1) Obter um acordo explícito sobre os requisitos do sistema/software.
NOTA Isto inclui confirmar que os requisitos do sistema/software são expressos corretamente, compreensíveis para os criadores e implementadores e que a resolução de conflitos nos requisitos é consistente com as decisões dos stakeholders.

- 2) Manter a rastreabilidade dos requisitos do sistema/software.
NOTA Durante o ciclo de vida, a rastreabilidade bidirecional é mantida entre os requisitos de sistema/software e os requisitos dos stakeholders, entidades arquiteturais, definições de interface, resultados de análises, métodos ou técnicas de verificação e requisitos alocados, decompostos e derivados. A rastreabilidade permite verificar se os requisitos exequíveis dos stakeholders são atendidos por um ou mais requisitos de sistema ou de elementos do sistema, e estes requisitos atendem ou contribuem para atender a pelo menos um requisito dos stakeholders. A rastreabilidade geralmente é facilitada por um repositório de dados apropriado ou por uma infraestrutura integrada de desenvolvimento e teste.

- 3) Fornecer artefatos e itens de informação principais que foram selecionados para baselines.
NOTA O Processo de Gerenciamento de Configuração é usado para estabelecer e manter itens de configuração e baselines. Este processo identifica candidatos para a baseline e o Processo de Gerenciamento da Informação controla os itens de informação, como especificações de requisitos. Para este processo, os requisitos de sistema/software são artefatos típicos para as baselines.


### 6.4.4 Processo de Definição de Arquitetura


#### 6.4.4.1 Propósito

O propósito do Processo de Definição de Arquitetura é gerar alternativas de arquitetura do sistema, selecionar uma ou mais alternativas que abranjam os interesses dos stakeholders e os requisitos do sistema e expressar em um conjunto de visões consistentes.

A iteração do Processo de Definição de Arquitetura com o Processo de Análise de Negócio, processo de Definição de Requisitos de Sistema/Software, Processo de Definição de Design e Processo de Definição de Necessidades e Requisitos dos Stakeholders é frequentemente usada para que haja um entendimento negociado do problema a ser resolvido e para que uma solução satisfatória seja identificada. Os resultados do Processo de Definição de Arquitetura são amplamente utilizados ao longo dos processos do ciclo de vida. A Definição da Arquitetura pode ser aplicada em vários níveis de abstração, destacando os detalhes relevantes que são necessários para as decisões neste nível.

NOTA 1 A arquitetura do sistema trata de princípios, conceitos, propriedades e características fundamentais e sua incorporação no sistema de interesse. A definição de arquitetura tem mais usos do que meramente ser um direcionador ou parte do design. Ver a ISO/IEC/IEEE 42010: 2011 para obter mais informações sobre a descrição da arquitetura e os usos e a natureza da arquitetura.

NOTA 2 O Processo de Definição de Arquitetura apoia a identificação de stakeholders e suas preocupações. À medida que o processo se desdobra, são obtidos insights sobre a relação entre os requisitos especificados para o sistema de software e as propriedades e comportamentos emergentes do sistema que surgem das interações e relações entre os elementos do sistema. Uma arquitetura eficaz é tão independente quanto possível do design para permitir a máxima flexibilidade no espaço do design. Mesmo para um sistema de software de um único produto, o design provavelmente mudará com o tempo, enquanto a arquitetura permanecerá estável. Uma arquitetura eficaz também destaca e suporta trade-offs para o Processo de Definição de Design e possivelmente outros processos, como Gerenciamento de Portfólio, Planejamento de Projeto, Definição de Requisitos de Sistema/Software e Verificação.

NOTA 3 A Definição de Arquitetura pode ser aplicada a uma linha de produtos, e não a um único sistema de software. Uma arquitetura de linha de produto descreve as propriedades estruturais para a construção de um grupo de sistemas relacionados com componentes comuns e seus relacionamentos. Nas arquiteturas da linha de produtos, a arquitetura necessariamente se propaga por vários designs. A arquitetura serve para tornar a linha de produtos coesa e ajuda a garantir a compatibilidade e a interoperabilidade ao longo da linha de produtos. A ISO/IEC 26550:2013 descreve o estabelecimento de uma arquitetura de domínio para uma linha de produtos.

NOTA 4 As áreas de conhecimento Requisitos de Software, design de Software e Modelos e Métodos de Engenharia de Software do SWEBOK (Guide to the Software Engineering Body of Knowledge) discutem os principais aspectos da arquitetura de software em relação ao sistema, bem como à iteração com o design.


#### 6.4.4.2 Resultados esperados

Como resultado da implementação bem-sucedida do Processo de Definição de Arquitetura:

- a) As preocupações dos stakeholders identificadas são atendidas pela arquitetura.
- b) Os pontos de vista da arquitetura são desenvolvidos.
- c) O contexto, fronteiras e interfaces externas do sistema são definidos.
- d) As visões e os modelos de arquitetura do sistema são desenvolvidos.
- e) Os conceitos, propriedades, características, comportamentos, funções ou restrições que são significativos para as decisões de arquitetura do sistema são alocados para entidades arquiteturais.
- f) Os elementos do sistema e suas interfaces são identificados.
- g) As arquiteturas candidatas são avaliadas.
- h) Uma base arquitetural para os processos ao longo do ciclo de vida é obtida.
O alinhamento da arquitetura com os requisitos e as características do design é obtido.

Todos os sistemas ou serviços habilitadores necessários para a definição da arquitetura são disponibilizados.

- k) A rastreabilidade dos elementos de arquitetura para os requisitos dos stakeholders e do sistema/software é desenvolvida.

#### 6.4.4.3 Atividades e tarefas

O projeto deve implementar as seguintes atividades e tarefas de acordo com as políticas e com os procedimentos organizacionais aplicáveis relacionados ao Processo de Definição de Arquitetura.

- a) Preparar a definição da arquitetura. Esta atividade consiste nas seguintes tarefas:
  - 1) Analisar criticamente as informações pertinentes e identificar os principais direcionadores da arquitetura.
NOTA 1 Os principais direcionadores são identificados pela análise crítica: (a) estudos de mercado, projeções da indústria, planos de produtos da concorrência e descobertas científicas; (b) estratégias organizacionais, conceito de operações no nível organizacional, politicas e diretrizes organizacionais, restrições regulatórias e legais e requisitos dos stakeholders; (c) os conceitos da missão ou do negócios sobre a operação, sistema de interesse e conceito operacional do sistema relacionado, ambiente operacional, roadmap de tecnologia e requisitos de sistema/software; e (d) outros fatores que afetam a adequação do sistema de software ao longo de seu ciclo de vida. Esta análise dos principais direcionadores geralmente se baseia nos processos de Análise de Negócio, Definição de Requisitos dos Stakeholders e Definição de Requisitos do Sistema/Software.

NOTA 2 Os principais direcionadores da arquitetura podem incluir estilos e padrões de arquitetura, elementos, princípios como componentes reutilizáveis, viabilidade de implementação e integração;

disponibilidade de COTS (Commercial-Off-The-Shelf) e componentes de código aberto; fontes de dados para sistemas intensivos de dados; e implicações de desempenho. O efeito de escolher vários elementos de design pode ser facilitado se o sistema de software estiver com uma arquitetura adequada.

  - 2) Identificar preocupações de stakeholder.
Os stakeholders são identificados inicialmente no processo Necessidades e Requisitos dos Stakeholders. Os stakeholders adicionais são geralmente identificados durante o Processo de Definição de Arquitetura. As preocupações dos stakeholders relacionadas à arquitetura incluem aquelas relacionadas à integridade do sistema que pode ser corrompido intencionalmente ou não, por meio de um agente de ameaça ou que o sistema pode causar acidentes com prejuízo à segurança. As expectativas ou restrições dos stakeholders são frequentemente associadas às fases do ciclo de vida do sistema, como utilização (por exemplo, disponibilidade, segurança, eficácia, usabilidade, interoperabilidade com sistemas existentes, riscos ou disponibilidade de dados do sistema), suporte (por exemplo, a capacidade de suporte do sistema durante sua vida útil planejada, gerenciamento de obsolescência), evolução do sistema de software e seu ambiente (por exemplo, adaptabilidade, escalabilidade, capacidade de sobrevivência), produção (por exemplo, distribuição, testabilidade) e desativação (por exemplo, eliminação ou retenção de dados confidenciais).

NOTA 2 As preocupações que afetam a arquitetura do sistema de software incluem implicações de desempenho e fontes de dados para sistemas com uso intensivo de dados e restrições no uso de elementos de software terceirizados, existentes, recém-desenvolvidos, proprietários, disponíveis comercialmente ou de código aberto, incluindo licenciamento de software. Embora a arquitetura de software seja idealmente independente do design, a viabilidade de implementar a arquitetura em um sistema de software financeiramente acessível é uma restrição significativa para a maioria dos sistemas.

  - 3) Definir o roadmap, a abordagem e a estratégia de Definição da Arquitetura.
Isto inclui a identificação de oportunidades de comunicação com os stakeho/ders designados, a definição de atividades de análise crítica de arquitetura, critérios e abordagens de avaliação, abordagens e métodos de medição (consulte o Processo de Medição). O roadmap mostra como a arquitetura evolui para um estado final planejado e geralmente possui um horizonte maior do que o atual sistema de interesse. A abordagem é a forma pela qual o trabalho é realizado, por exemplo, como envolver os stakeholders, como avaliar os resultados ou onde executar o trabalho. A estratégia trata do plano de ação sistemático para implementar a abordagem consistente com o roadmap.

  - 4) Definir critérios de avaliação da arquitetura com base nas preocupações dos stakeholders e nos principais requisitos.
  - 5) Identificar e planejar os sistemas ou serviços habilitadores necessários para apoiar o Processo de Definição de Arquitetura.
NOTA Isto inclui a identificação de requisitos e interfaces para os sistemas habilitadores e serviços. Sistemas habilitadores para definição da arquitetura podem incluir ferramentas para colaboração e desenvolvimento de arquitetura e repositórios de reutilização de arquitetura para artefatos, como, padrões de arquitetura, modelos e arquiteturas de referência.

  - 6) Obter ou adquirir acesso aos sistemas ou serviços habilitadores a serem utilizados.
NOTA O Processo de Validação é usado para confirmar objetivamente que o sistema habilitador atinge o uso pretendido para suas funções de habilitação. O Processo de Gerenciamento de Infraestrutura apoia a reutilização de sistemas habilitadores.

- b) Desenvolver pontos de vista da arquitetura. Esta atividade consiste nas seguintes tarefas:
  - 1) Selecionar, adaptar ou desenvolver pontos de vista e tipos de modelos com base nas preocupações dos stakeholders.
  - 2) Estabelecer ou identificar possíveis frameworks de arquitetura a serem utilizados no desenvolvimento de modelos e visões.
Alguns frameworks de arquitetura identificam os stakeholders e suas preocupações, e pontos de vista relevantes que tratam estas preocupações, enquanto outros frameworks de arquitetura são mais gerais em suas orientações. Os pontos de vista especificam os tipos de modelos a serem utilizados e como os modelos resultantes podem ser usados para gerar visões de arquitetura. Ver a ISO/IEC/IEEE 42010 para obter mais informações sobre framework e práticas de descrição de arquitetura.

  - 3) Capturar a justificativa para a seleção de frameworks, pontos de vista e tipos de modelos.
  - 4) Selecionar ou desenvolver técnicas e ferramentas de suporte à modelagem.
Tanto o SWEBOK (Guide to the Software Engineering Body of Knowledge) quanto a ISO/IEC TR 24748-3 descrevem técnicas de modelagem que apoiam Definição de Arquitetura e a Definição de Design de elementos de software.

- c) Desenvolver modelos e visões de arquiteturas candidatas. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir o contexto e a fronteira do sistema de software em termos de interfaces e interações com entidades externas.
Esta tarefa é baseada principalmente nos resultados do Processo de Análise de Negócio e é executada simultaneamente com o Processo de Definição de Necessidades e Requisitos dos Stakeholders. Consiste em identificar as entidades externas ao sistema de software (ou seja, sistemas, produtos e serviços existentes e projetados que constituem o contexto do sistema) e definir as fronteiras do sistema de software (ou seja, interações com estas entidades externas por meio das interfaces que atravessam as fronteiras). As entidades externas incluem os sistemas habilitadores necessários. O Processo de Definição de Arquitetura define as interfaces na medida necessária para apoiar o entendimento e as decisões arquiteturais essenciais. Estas definições de interface são então refinadas pelo processo Definição de Design.

  - 2) Identificar as entidades arquiteturais e os relacionamentos entre as entidades que tratam das principais preocupações dos stakeholders e dos requisitos críticos do sistema de software.
A arquitetura não está necessariamente preocupada com todos os requisitos, mas apenas com os requisitos de sistema/software que direcionam a arquitetura. Por outro lado, o processo de Definição de Design trata e leva em consideração todos os requisitos. As vezes, por meio do Processo de Definição de Arquitetura, existem requisitos que são considerados inapropriados, inviáveis ou inadequados. Estes são problemas de requisitos que são resolvidos por meio da iteração do processo de Definição de Requisitos de Sistema/Software. Também é importante que a arquitetura atenda às principais preocupações dos stakeholders, pois nem todas elas estarão capturadas nos requisitos.

  - 3) Alocar conceitos, propriedades, características, comportamentos, funções ou restrições que são significativos para as decisões de arquitetura do sistema de software para as entidades arquiteturais.
NOTA Os itens alocados podem ser conceituais, lógicos ou físicos.

  - 4) Selecionar, adaptar ou desenvolver modelos das arquiteturas candidatas do sistema de software.
NOTA É comum usar modelos na definição de arquitetura. Os modelos usados são aqueles que melhor atendem às principais preocupações dos stakeholders. Ver a ISO/IEC/IEEE 42010 para mais

detalhes. Historicamente, tem sido comum o uso de modelos lógicos e físicos na definição da arquitetura. Informações sobre modelos lógicos e outros modelos são fornecidas no Anexo F.

  - 5) Compor visões dos modelos de acordo com os pontos de vista identificados para expressar como a arquitetura trata as preocupações dos stakeholders e atende aos requisitos dos stakeholders e do sistema/software.
  - 6) Harmonizar os modelos e visões da arquitetura entre si.
NOTA As regras de correspondência dos frameworks são uma maneira de estabelecer harmonia entre as visões. Ver ISO/EC/IEEE 42010.

- d) Relacionar a arquitetura ao design. Esta atividade consiste nas seguintes tarefas:
  - 1) Identificar os elementos do sistema de software que se relacionam com entidades arquiteturais e a natureza dessas relações.
NOTA Algumas vezes os elementos do sistema de software são inicialmente teóricos até que a Definição de Design tenha acontecido, uma vez que isto depende do design real a ser feito. Às vezes, uma arquitetura de referência" é criada usando estes elementos teóricos do sistema como uma forma de transmitir a intenção arquitetural e para verificar a viabilidade do design.

  - 2) Definir as interfaces e as interações entre os elementos do sistema de software e entidades externas.
NOTA Isto é definido no nível de detalhe necessário para transmitir a intenção arquitetural e pode ser posteriormente refinado no Processo de Definição de Design.

  - 3) Particionar, alinhar e alocar requisitos às entidades arquiteturais e aos elementos do sistema.
  - 4) Mapear os elementos do sistema de software e as entidades arquiteturais para características do design.
  - 5) Definir princípios para o design e a evolução do sistema de software.
EXEMPLO Os princípios podem incluir interoperabilidade, uso de padrões de design selecionados, facilidade de substituição e atualização de elementos do sistema ou níveis de segurança.

- e) Avaliar arquiteturas candidatas. Esta atividade consiste nas seguintes tarefas:
  - 1) Avaliar cada arquitetura candidata em relação aos requisitos e restrições.
  - 2) Avaliar cada arquitetura candidata em relação às preocupações dos stakeholders, utilizando critérios de avaliação.
NOTA O Processo de Análise de Sistema e o Processo de Gestão de Riscos podem ser usados para apoiar esta tarefa.

  - 3) Selecionar a(s) arquitetura(s) preferencial(s) e capturar as principais decisões e justificativas.
NOTA O Processo de Gerenciamento de Decisão pode ser usado para apoiar esta tarefa.

  - 4) Estabelecer a baseline de arquitetura da arquitetura selecionada.
NOTA A baseline de arquitetura é composta por modelos, visões e outras descrições relevantes da arquitetura.

- f) Gerenciar a arquitetura selecionada. Esta atividade consiste nas seguintes tarefas:
  - 1) Formalizar a abordagem de governança da arquitetura e especificar os papéis, as responsabilidades, as responsabilizações e as autoridades relacionados ao design, qualidade, segurança e proteção.
  - 2) Obter aceitação explícita da arquitetura pelos stakeholders.
NOTA O Processo de Validação é usado para confirmar que os modelos e as visões da arquitetura refletem os requisitos dos stakeholders, que as preocupações dos stakeholders são tratadas e para ajudar a garantir que as iterações futuras da arquitetura do sistema de software melhor atendem às preocupações dos stakeholders.

  - 3) Manter concordância e completude das entidades arquiteturais e suas características arquiteturais.
NOTA As entidades a serem verificadas não são apenas técnicas. Também são, por exemplo, entidades legais, econômicas, organizacionais e operacionais que normalmente fazem parte dos requisitos e preocupações dos stakeholders.

  - 4) Organizar, avaliar e controlar a evolução dos modelos e visões da arquitetura para ajudar a garantir que a intenção arquitetural seja atendida e a visão arquitetural e os principais conceitos sejam implementados corretamente.
  - 5) Manter a definição da arquitetura e a estratégia de avaliação.
NOTA Isto inclui atualizar a arquitetura com base na experiência de implementação, operacional ou tecnológica (por exemplo, obsolescência). Também inclui o gerenciamento de interfaces externas e internas que são definidas neste nível de decomposição do sistema de software.

  - 6) Manter a rastreabilidade da arquitetura.
NOTA Ao longo do ciclo de vida, a rastreabilidade é frequentemente mantida entre as entidades ou elementos arquiteturais (modelos, visões e pontos de vista), os requisitos (incluindo os alocados, os decompostos e os derivados) e as preocupações dos stakeholders, design do sistema de software, definições de interface, resultados de análise e métodos ou técnicas de verificação.

  - 7) Fornecer artefatos e itens de informação principais selecionados para baselines.
NOTA O Processo de Gerenciamento de Configuração é usado para estabelecer e manter itens de configuração e baselines. Este processo identifica candidatos para a baseline. O Processo de Gerenciamento da Informação controla os itens de informação, como descrições de arquitetura (modelos e visões de arquitetura, avaliações e rastreabilidade).


### 6.4.5 Processo de Definição de Design


#### 6.4.5.1 Propósito

O propósito do Processo de Definição de Design é fornecer dados e informações suficientemente detalhados com relação ao sistema e seus elementos de forma a permitir a implementação consistente com entidades

Para sistemas de software, as atividades de design normalmente realizam iterações com atividades de Definição de Requisitos de Sistema/Software e de Definição de Arquitetura. A definição do design é tipicamente aplicada de forma iterativa e incremental para desenvolver um design detalhado,

incluindo elementos de software, interfaces, bancos de dados e documentação do usuário. O design do software ocorre geralmente de forma concomitante com a implementação, integração, verificação e validação do software. O Anexo H aborda o design de software utilizando métodos ágeis. Durante o design e implementação, a aplicação do processo refina a alocação de requisitos em evolução entre os elementos do software.

O processo de Definição de Projeto é orientado por requisitos que foram verificados por meio da arquitetura e análises mais detalhadas de viabilidade. A arquitetura foca na adequação, viabilidade e conveniência, enquanto o design se concentra na compatibilidade com tecnologias e outros elementos de design e viabilidade de implementação e integração. Uma arquitetura eficaz é tão independente quanto possível do design para permitir a máxima flexibilidade dentro do design no espaço de negócio.

NOTA 2 Este processo fornece feedback para a arquitetura do sistema de software para consolidar ou confirmar a alocação, particionamento e alinhamento das entidades arquiteturais.


#### 6.4.5.2 Resultados esperados

Como resultado da implementação bem-sucedida do Processo de Definição de Design:

- a) As características de design de cada elemento do sistema são definidas.
- b) Os requisitos do sistema/software são alocados em elementos do sistema.
- c) Os habilitadores de design necessários para a definição de design são selecionados ou definidos.
- d) As interfaces entre elementos do sistema que compõem o sistema são definidas ou refinadas.
- e) As alternativas de design para elementos do sistema são avaliadas.
- f) Os artefatos de design são desenvolvidos.
- g) Todos os sistemas ou serviços habilitadores necessários para definição de design estão disponíveis.
A rastreabilidade das características de design para as entidades arquiteturais da arquitetura do sistema é estabelecida.

A definição de design considera as tecnologias aplicáveis e sua contribuição para a solução do sistema. O design fornece o nível de implementação da definição, como design, diagramas de estado, histórias e descrições detalhadas de design. Para elementos de software, este processo pode resultar em uma descrição detalhada do design que pode ser verificada em relação aos requisitos e à arquitetura do software. Mesmo que o design do software não seja totalmente especificado em uma descrição formal, ele é suficientemente detalhado para permitir a implementação de software (construção) e o planejamento


#### 6.4.5.3 Atividades e tarefas

O projeto deve implementar as seguintes atividades e tarefas de acordo com as políticas e com os procedimentos organizacionais aplicáveis relacionados ao Processo de Definição de Design.

NOTA O SWEBOK, Guide to the Software Engineering Body of Knowledge, fornece uma discussão detalhada sobre o design de software. Esta área de conhecimento aborda fundamentos, questões-chave, estratégias, métodos e notações de design.

- a) Preparar para a definição de design do sistema de software. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir a estratégia de definição de design, consistente com o modelo de ciclo de vida selecionado e artefatos de design previstos.
NOTA A estratégia de design de software pode incluir decomposição inicial ou incremental em elementos de sistema; criação de diversas visões de procedimentos automatizados, estruturas de dados e sistemas de controle; seleção de padrões de design, ou definição progressivamente mais detalhada de objetos e seus relacionamentos.

  - 2) Selecionar e priorizar princípios e características de design.
NOTA Os princípios de design incluem controlar ideias como abstração, modularização e encapsulamento, separação entre interface e implementação, concorrência e persistência de dados. As considerações de segurança incluem o princípio do menor privilégio, defesas em camadas, acesso restrito aos serviços do sistema e outras considerações para minimizar e defender a superfície de ataque do sistema. As características do design incluem, por exemplo, disponibilidade, tolerância a falhas e resiliência, escalabilidade, usabilidade, capacidade e desempenho, testabilidade, portabilidade e acessibilidade.

  - 3) Identificar e planejar os sistemas ou serviços de apoio necessários para suportar a definição de design.
NOTA Isto inclui a identificação de requisitos e interfaces para os sistemas de apoio. Os sistemas habilitadores para definição de design incluem seleção de plataformas de software e sistemas, linguagens de programação, notações de design e ferramentas para colaboração e desenvolvimento do design, repositórios de reutilização de design (para linhas de produtos, design patterns), e artefatos de design, e normas de design.

  - 4) Obter ou adquirir acesso aos sistemas ou serviços habilitadores a serem utilizados.
NOTA O Processo de Validação é utilizado para confirmar objetivamente que o sistema habilitador atende ao seu uso pretendido para suas funções habilitadoras.

- b) Estabelecer design relacionados a cada elemento do sistema de software. Esta atividade consiste nas seguintes tarefas:
  - 1) Transformar características arquiteturais e de design no design de elementos do sistema de software.
NOTA Características se aplicam a elementos físicos e lógicos do sistema, como estruturas de banco de dados, disponibilização de memória e armazenamento, processos e controles de software, interfaces externas como interfaces de usuário ou serviços. A ISO 9241-210 fornece diretrizes de design centradas em aspectos humanos/ergonômicos.

  - 2) Definir e preparar ou obter os habilitadores de design necessários.
Os habilitadores de design incluem modelos, equações, algoritmos, cálculos, expressões formais e valores de parâmetros, padrões e heurísticas, que estão associados a características de design usando representação adequada, como design, diagramas lógicos, fluxogramas, convenções de codificação, padrões lógicos, modelos de informação, regras de negócios, perfis de usuários, cenários, casos de uso ou histórias de usuário, e tabelas de métricas e seus valores, por exemplo, pontos de função ou pontos de história do usuário.

  - 3) Examinar alternativas de design e viabilidade de implementação.
NOTA 1 Para o sistema de software e elementos de software, normalmente são examinados reuso, adaptação, serviço terceirizado ou novo desenvolvimento.

Avaliar a viabilidade de implementar as características do design. Se for justificado por resultados de avaliação, examinar outras opções alternativas de design ou analise os trade-offs da arquitetura ou dos requisitos, quando as características de design forem impossíveis de implementar.

  - 4) Refinar ou definir as interfaces entre os elementos do sistema de software e as entidades externas.
As interfaces são identificadas e definidas no Processo de Definição de Arquitetura (ver 6.4.4) ao nível ou extensão necessários para o objetivo e compreensão da arquitetura. Estes são refinados no processo Definição de Design com base nas características de design, interfaces e interações de elementos de software com outros elementos que compõem o sistema de software e com entidades externas. Algumas vezes interfaces adicionais que não foram abordadas na definição de arquitetura são identificadas e definidas.

  - 5) Estabelecer os artefatos de design.
NOTA Esta tarefa formaliza as características de design dos elementos do sistema de software por meio de artefatos exclusivos, dependendo da tecnologia de implementação. Exemplos de artefatos incluem protótipos, modelos de dados, pseudocódigo, diagramas de entidade-relacionamento, casos de uso, matrizes de função e privilégios do usuário, especificações de interface, descrições de serviços e procedimentos. Artefatos de design são desenvolvidos, obtidos ou modificados para as alternativas selecionadas. Os dados são associados a limites de detalhamento aceitáveis para implementação (se forem relevantes neste processo ou iteração de tarefas).

- c) Avaliar alternativas para obter elementos do sistema de software. Esta atividade consiste nas seguintes tarefas:
  - 1) Determinar tecnologias necessárias para cada elemento que compõe o sistema de software.
NOTA Várias tecnologias são às vezes usadas para um determinado elemento do sistema de software, por exemplo, presença na internet, sistemas embarcados, adaptação de software de código aberto, papéis para operadores humanos.

  - 2) Identificar alternativas de candidatos para os elementos do sistema de software.
As alternativas incluem itens recém-projetados e construídos; adaptações de linhas de produtos, componentes, objetos ou serviços existentes; aquisição ou reutilização de itens não desenvolvidos (NDI - Non-Developed Items). Os NDI incluem produtos de prateleira (COTS - Commercial-Off-The-Shelf) ou produtos gratuitos de código aberto (FOSS - Free and Open Source Software), reutilização de um design anterior ou ativos existentes, incluindo itens fornecidos pelo adquirente.

  - 3) Avaliar cada alternativa candidata em relação a critérios desenvolvidos a partir de características de design esperadas e requisitos de elementos para determinar a adequação da aplicação pretendida.
NOTA Uma decisão de fazer ou comprar e uma abordagem de implementação e integração resultante geralmente envolvem trade-offs dos critérios de design, incluindo custo. As escolhas de design geralmente consideram permitir sistemas habilitadores requeridos para testar a alternativa (design e desenvolvimento orientados a testes) e sustentabilidade ao longo da vida útil do sistema, incluindo custos de manutenção. O Processo de Manutenção pode ser usado para determinar a adequação do design para manutenção e sustentabilidade a longo prazo.

  - 4) Escolher as alternativas preferidas entre as soluções de design candidatas para os elementos do sistema de software.
NOTA O Processo de Análise de Sistema pode ser utilizado em análises e avaliações para apoiar o Processo de Gerenciamento de Decisão na realização da seleção. As análises críticas de design são realizadas usando o Processo de Validação.

- d) Gerenciar o design. Esta atividade consiste nas seguintes tarefas:
  - 1) Capturar o design e a justificativa.
NOTA As informações comumente capturadas incluem os elementos do sistema de software e os requisitos associados e dados de design, por exemplo, para elementos de software, interfaces internas e externas, estruturas de dados, requisitos de implementação e teste, dados de agregação de unidades para integração e casos de teste. A justificativa normalmente inclui informações sobre as principais opções de implementação e habilitadores. O design resultante é controlado de acordo com a estratégia.

  - 2) Estabelecer a rastreabilidade entre os elementos de design detalhados, os requisitos do sistema/software e as entidades arquiteturais do sistema de software.
NOTA 1 Esta tarefa facilita o fornecimento de feedback para o Processo de Definição de Arquitetura para possíveis modificações, por exemplo, para modificar a alocação de elementos do sistema de software, a fim de obter as características arquiteturais esperadas; ou possivelmente modificar a caracteristica arquitetural esperada devido a fatores descobertos durante o processo de design, ou para conscientizar os stakeholders sobre os potenciais impactos.

NOTA 2 Ao longo do ciclo de vida, a rastreabilidade bidirecional é mantida entre o design e os métodos ou técnicas de verificação, e os requisitos de elementos do sistema de software. Alocações e propriedades de design são atribuídas a elementos de software, unidades de software e artefatos associados, em um nível de detalhe suficiente para permitir testes e implementação de software, incluindo construção.

  - 3) Determinar o status do sistema de software e do design de elementos.
NOTA 1 O Processo de Medição é utilizado para estabelecer medidas para a completude e qualidade do design à medida que ele avança. Os processos de Verificação e Validação são utilizados para verificar e validar o design e implementação detalhados.

NOTA 2 Isto inclui avaliação periódica das caracteristicas de design em caso de evolução do sistema de software e de sua arquitetura, bem como a previsão de potencial obsolescência de componentes e tecnologias, sua substituição por outros ao longo do tempo no ciclo de vida do sistema de software, e as consequências para a definição de design. O Processo de Gestão de Riscos é normalmente utilizado para avaliar riscos na estratégia de design, design inicial e design em evolução.

  - 4) Fornecer artefatos-chave e itens informativos que foram selecionados para baselines.
O Processo de Gerenciamento de Configuração é usado para estabelecer e manter itens de configuração e baselines para artefatos como modelos de design. Este processo identifica os candidatos para a baseline, e o processo de Gerenciamento da Informação controla os itens de informação, como descrições de design e especificações.


### 6.4.6 Processo de Análise de Sistema


#### 6.4.6.1 Propósito

O propósito do Processo de Análise de Sistema é fornecer uma base rigorosa de dados e informações para o entendimento técnico para auxiliar a tomada de decisão ao longo do ciclo de vida.

O Processo de Análise de Sistema é aplicável ao desenvolvimento de entradas necessárias para qualquer avaliação técnica. Ele provê confiança na utilidade e integridade dos requisitos do sistema, da arquitetura e do design. A análise de sistema abrange uma ampla gama de funções analíticas, níveis de complexidade e rigor. Inclui análise matemática, modelagem, simulação, experimentação e outras técnicas para analisar o desempenho técnico, o comportamento do sistema, a viabilidade, a viabilidade econômica, as caracteristicas críticas de qualidade, os riscos técnicos, os custos do ciclo de vida e também para executar análises de sensibilidade da potencial gama de valores para os parâmetros definidos ao longo de todas as fases do ciclo de vida. É utilizado para uma ampla gama de necessidades analíticas relativas a conceitos operacionais, determinação de valores de requisitos, resolução de conflitos de requisitos, avaliação de alternativas para arquiteturas ou elementos de sistema e avaliação de estratégias de engenharia (integração, verificação, validação e manutenção). A formalidade e o rigor da análise dependem da criticidade das necessidades de informação ou do produto de trabalho suportado, da quantidade de informações/dados disponíveis, do tamanho do projeto e do cronograma de entregas.

NOTA O Processo de Análise de Sistema pode ser utilizado em todo o sistema de software ou em qualquer elemento. Este processo é frequentemente utilizado em conjunto com o Processo de Gerenciamento de Decisão.


#### 6.4.6.2 Resultados esperados

Como resultado da implementação bem-sucedida do Processo de Análise de Sistema:

- a) As necessidades de análise de sistema são identificadas.
- b) As premissas e os resultados de análise de sistema são validados.
Os resultados da análise de sistema são fornecidos para tomada de decisões.

- d) Quaisquer sistemas ou serviços habilitadores necessários para análise de sistema são disponibilizados.
- e) A rastreabilidade dos resultados da análise de sistema é estabelecida.

#### 6.4.6.3 Atividades e tarefas

O projeto deve implementar as seguintes atividades e tarefas de acordo com as políticas e os procedimentos aplicáveis da organização relacionados ao Processo de Análise de Sistema.

- a) Definir a estratégia e preparar-se para a análise de sistema. Esta atividade consiste nas seguintes tarefas:
  - 1) Identificar o problema ou a questão que requer análise.
NOTA Isto inclui objetivos técnicos, funcionais e não funcionais da análise. Objetivos não funcionais incluem características críticas de qualidade, diversas propriedades, maturidade tecnológica

e riscos técnicos. A declaração do problema ou questão a ser respondida pela análise é essencial para estabelecer os objetivos da análise e as expectativas e utilidade dos resultados.

  - 2) Identificar os stakeholders da análise.
  - 3) Definir o escopo, os objetivos e o nível de exatidão da análise.
NOTA O nível necessário de exatidão (acurácia ou precisão) é um fator na determinação do nível apropriado de rigor.

  - 4) Selecionar os métodos para apoiar a análise.
NOTA Os métodos são escolhidos com base no tempo, custo, exatidão, direcionadores técnicos e criticidade da análise. Os métodos de análise têm uma ampla gama de níveis de rigor e incluem o julgamento de especialistas, cálculos de planilha, estimativas e cálculos paramétricos, dados históricos e análise de tendências, modelos de engenharia, simulação, visualização e prototipação. Devido as restrições de custo e cronograma, a maioria dos projetos normalmente realiza análises de sistema apenas para características críticas.

  - 5) Identificar e planejar os sistemas ou serviços habilitadores necessários para apoiar a análise.
NOTA Esta tarefa inclui a identificação de requisitos e interfaces para os sistemas habilitadores. Os sistemas habilitadores de análise de sistema incluem as ferramentas, modelos relevantes e potenciais repositórios de dados necessários para apoiar a análise. Os métodos escolhidos serão um fator importante na determinação de quais ferramentas são adequadas para apoiar a análise. Isto também inclui determinar a disponibilidade de recursos ou de modelos relevantes e dados reutilizáveis ou não reutilizáveis.

  - 6) Obter ou adquirir acesso aos sistemas ou serviços habilitadores a serem utilizados.
NOTA O Processo de Gerenciamento de Infraestrutura permite a prestação de serviços de análise de sistemas. O Processo de Validação é utilizado para confirmar objetivamente que o sistema habilitador atende ao seu uso pretendido para suas funções habilitadoras.

  - 7) Coletar os dados e as entradas necessários para a análise.
- b) Realizar análise de sistema. Esta atividade consiste nas seguintes tarefas:
  - 1) Identificar e validar contextos e premissas.
  - 2) Aplicar os métodos de análise selecionados para realizar a análise necessária.
  - 3) Analisar criticamente os resultados da análise em relação à qualidade e à validade.
NOTA Os resultados são coordenados com análises associadas que foram previamente concluídas.

  - 4) Estabelecer conclusões e recomendações.
NOTA Os especialistas apropriados e stakeholders são identificados e engajados nesta tarefa.

  - 5) Registrar os resultados da análise de sistema.
- c) Gerenciar a análise de sistema. Esta atividade consiste nas seguintes tarefas:
  - 1) Manter a rastreabilidade dos resultados da análise.
NOTA Ao longo do ciclo de vida, a rastreabilidade bidirecional é mantida entre os resultados da análise e qualquer item do sistema de software para o qual a análise esteja apoiando uma decisão

ou fornecendo uma justificativa (por exemplo, valores de requisitos de sistema/software, arquiteturas alternativas). Isto é muitas vezes facilitado por um repositório de dados apropriado.

  - 2) Fornecer artefatos-chave e itens informativos selecionados para baselines.
O Processo de Gerenciamento de Configuração é usado para estabelecer e manter itens de configuração e baselines. Este processo identifica os candidatos para a baseline e o processo de Gerenciamento da Informação controla os itens de informação. Para este processo, os resultados


### 6.4.7 Processo de Implementação


#### 6.4.7.1 Propósito

O propósito do Processo de Implementação é construir um elemento de sistema especificado.

Este processo transforma requisitos, arquitetura e design, incluindo interfaces, em ações que criam um elemento de sistema de acordo com as práticas da tecnologia de implementação selecionada, utilizando competências técnicas ou disciplinas adequadas. Este processo resulta em um elemento de sistema que satistaz os requisitos especificados (incluindo requisitos alocados e derivados), arquitetura e design.

Para sistemas de software, o propósito do Processo de Implementação é construir um elemento de sistema de software.

Os elementos do sistema de software podem incluir hardware, software e serviços. Para a implementação de software, este processo transforma designs, comportamentos, interfaces e restrições de implementação especificados em ações que criam um elemento de sistema de software implementado como produto ou serviço de software, também conhecido como item de software". A implementação de software resulta em um elemento de software que satisfaz os requisitos especificados por meio de verificação, e requisitos de stakeholders por meio de validação. A implementação de software inclui várias combinações de construção (codificação de novos elementos de software), aquisição de novos pacotes de software (por exemplo, de código fonte aberto, comercial ou da organização) ou reuso de elementos existentes (com ou sem modificação).

A implementação de software geralmente envolve o uso dos processos de Acordo para obter itens que não serão desenvolvidos (NDI), como hardware e sistemas operacionais (a plataforma) ou sistemas e serviços habilitadores. A implementação de software geralmente é executada simultaneamente com a integração de software. A implementação é normalmente executada em conjunto com todos os processos de Gerenciamento Técnico e muitos dos processos Técnicos, especialmente:

- a) O Processo de Verificação, que fornece evidências objetivas de que a implementação do software atende a seus requisitos especificados e identifica anomalias (erros, defeitos, falhas) em itens de informação relacionados à implementação, (por exemplo, requisitos de sistema/software, arquitetura, design ou outras descrições), processos, elementos de software, itens, unidades;
- b) O Processo de Validação, que confirma que a implementação atende aos requisitos para um uso específico pretendido de um produto de trabalho de software.

#### 6.4.7.2 Resultados esperados

Como resultado da implementação bem-sucedida do Processo de Implementação:

- a) As restrições de implementação que influenciam os requisitos, arquitetura ou design são identificadas.
- b) Um elemento do sistema é construído.
- c) Um elemento do sistema é empacotado ou armazenado.
- d) Quaisquer sistemas ou serviços habilitadores necessários para implementação são disponibilizados.
- e) A rastreabilidade é estabelecida.

#### 6.4.7.3 Atividades e tarefas

O projeto deve implementar as seguintes atividades e tarefas de acordo com as políticas e com os procedimentos organizacionais aplicáveis relacionados ao Processo de Implementação.

- a) Preparar para a implementação. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir uma estratégia de implementação, considerando o seguinte:
i. políticas e padrões de desenvolvimento, incluindo padrões que regem as práticas aplicáveis de proteção, de segurança, de privacidade e ambientais; padrões de programação ou codificação; politicas de testes unitários; e padrões específicos de linguagem para implementar caracteristicas de segurança;

її. para software reutilizado ou adaptado, métodos para determinar o nível, a fonte e a adequação dos elementos do sistema reutilizados e a segurança da cadeia de suprimentos;

procedimentos e métodos para desenvolvimento de software (construção) e desenvolvimento de testes unitários; e o uso de análises críticas por pares, testes unitários e walkthroughs durante a implementação;

iv. uso de Gerenciamento de Configuração durante a construção do software;

V. considerações de gerenciamento de mudanças para processos manuais;

vi. prioridades de implementação para apoiar a migração e transição de dados e software, juntamente com a desativação de sistemas legados;

vii. criação de procedimentos de testes manuais ou automatizados para verificar se uma unidade de software atende aos seus requisitos antes de sua criação (desenvolvimento orientado a testes); e

viii. ambientes abrangentes ou especializados de desenvolvimento e suporte de ciclo de vida para gerenciamento e desenvolvimento de requisitos, modelos e protótipos, elementos de sistema ou software entregáveis, e especificações e casos de testes.

NOTA A estratégia de implementação normalmente é registrada no SPD (Plano de Desenvolvimento de Software) ou SEMP (Plano de Gerenciamento de Engenharia de Sistemas) de um projeto, ou às vezes em um PMP (Plano de Gerenciamento de Projeto).

  - 2) Identificar restrições da estratégia e da tecnologia de implementação nos requisitos do sistema/software, características de arquitetura e de design, ou técnicas de implementação.
As restrições incluem limitações atuais ou previstas da tecnologia de implementação escolhida (por exemplo, para software, sistema operacional, sistema de gerenciamento de banco de dados, serviços web), materiais ou elementos do sistema a serem adaptados fornecidos pelo adquirente, e limitações resultantes do uso de sistemas habilitadores necessários à implementação.

NOTA 2 A estratégia de implementação de software normalmente identifica e aloca critérios de implementação, por exemplo, características de arquitetura e design de software, requisitos de sistema/software, incluindo garantia de software, considerações de usabilidade, gerenciamento de configuração, rastreabilidade ou outras condições a serem atendidas. Estes critérios podem esclarecer os níveis de agregação, especificações e restrições adequados.

  - 3) Identificar e planejar os ambientes de software necessários e distintos, incluindo sistemas ou serviços habilitadores necessários para desenvolvimento e testes.
A implementação de software geralmente utiliza ambientes diferentes do ambiente de operação (produção) com controles de configuração distintos. Um processo Implementação, sistemas habilitadores e serviços comuns incluem ambientes abrangentes ou especializados de desenvolvimento e suporte de ciclo de vida para gerenciamento e desenvolvimento de requisitos, modelos e protótipos, elementos entregáveis e ambientes de testes, especificações e casos de testes; simuladores para sistemas externos, sistemas de treinamento; e sistemas de gerenciamento de conteúdo para documentação do usuário.

  - 4) Obter ou adquirir acesso aos ambientes de software e outros sistemas habilitadores e serviços.
NOTA O Processo de Validação é utilizado para confirmar objetivamente que a integração do sistema habilitador atende ao uso de suas funções para a finalidade pretendida.

- b) Realizar a implementação. Esta atividade consiste nas seguintes tarefas:
No decorrer do Processo de Implementação, o Processo de Verificação é utilizado para confirmar objetivamente que os elementos do sistema estão em conformidade com os requisitos. O Processo de Validação é usado para confirmar objetivamente que o elemento é adequado para ser utilizado no ambiente operacional pretendido, de acordo com os requisitos dos stakeholders.

  - 1) Construir ou adaptar elementos de software de acordo com a estratégia, restrições e procedimentos de implementação definidos.
NOTA 1 Elementos de software são adquiridos, reutilizados a partir de ativos organizacionais, ou desenvolvidos (construídos). Elementos de software adquiridos podem variar desde uma simples compra de produtos de acordo com as regras de compra da organização ou do projeto, até uma aquisição complexa de um sistema de software que envolve os processos de Aquisição e Fornecimento. A adaptação inclui a configuração de elementos de software que são reutilizados ou modificados. A construção pode envolver codificação de software, reutilização adaptativa e integração de unidades existentes, refatoração, desenvolvimento de banco de dados e construção de procedimentos de testes manuais ou automatizados para cada unidade.

Para elementos de software desenvolvidos, no nível mais baixo de implementação, são construídas unidades de software executáveis (muitas vezes com estruturas de dados associadas, interfaces de programação de aplicativos (API), descrições de serviços, documentação do usuário, casos de testes ou outros elementos), controladas, disponibilizadas para pessoas autorizadas e armazenadas de acordo com os procedimentos de gerenciamento da configuração.

O SWEBOK, Guide to the Software Engineering Body of Knowledge provê uma discussão detalhada sobre a Construção de Software. Esta área de conhecimento aborda fundamentos, gerenciamento, medição, considerações práticas (por exemplo, design de construção, linguagens de programação, testes, reuso e integração), tecnologias de construção (por exemplo, orientação a objeto, tratamento de erro e exceção, modelos executáveis, software distribuído), ferramentas e ambientes.

- 2) Construir ou adaptar elementos de hardware para sistemas de software.
NOTA Os elementos de hardware são adquiridos ou fabricados utilizando técnicas relevantes aplicáveis para a tecnologia de implementação física e materiais selecionados. A conformidade dos elementos de hardware é verificada com relação aos requisitos especificados do sistema e características críticas da qualidade. No caso de repetidas implementações do elemento do sistema (por exemplo, produção em massa, substituição de elementos do sistema) os procedimentos de implementação e processos de fabricação são definidos e podem ser automatizados para alcançar uma produção consistente e repetivel. Alguns elementos comuns de hardware em sistemas de software incluem integrações de produtos de prateleira (COTS - Commercial-Off-The-Shelf) adquiridos, modificações especiais, por exemplo, para ambientes de teste ou operacionais e controles de hardware com software embarcado.

- 3) Construir ou adaptar elementos de serviço para sistemas de software.
de serviço incluem um conjunto de serviços a serem fornecidos. A ISO/IEC 20000 (IEEE Std 20000) aplica-se ao gerenciamento de serviços realizados para elementos do sistema, incluindo estratégia, design e transição. A conformidade dos elementos de serviço é verificada com relação aos requisitos do sistema e critérios de serviço. Por exemplo, a conformidade de elementos de recursos operacionais é verificada com relação aos requisitos do sistema e conceitos de operação. Os elementos de serviço podem incluir rede de comunicações, treinamento, empacotamento de software e distribuição de serviços, serviços de customização de software para necessidades específicas do cliente, monitoramento de operação e segurança, e atendimento ao usuário.

- 4) Avaliar a unidade de software e dados associados ou outras informações de acordo com a estratégia e critérios de implementação.
Os critérios de avaliação geralmente incluem atendimento aos requisitos unitários e critérios de teste, cobertura de teste unitário, requisitos de rastreabilidade, consistência com os requisitos do elemento de software ou design, consistência dos requisitos unitários internos e viabilidade para atividades adicionais do processo, por exemplo, integração, verificação, validação, operação

NOTA 2 Utilizar a atividade Gerenciar resultados de implementação para registrar a construção e solucionar anomalias.

- 5) Empacotar e armazenar o elemento do sistema de software.
NOTA O elemento do sistema de software é empacotado com o objetivo de manter as suas características. O empacotamento pode ser influenciado pela forma de uso como: transmissão, armazenamento e duração. Uma cópia mestre do software implementado (eletrônica ou em mídia física) é armazenada em um local controlado e disponibilizada para pessoas autorizadas (por exemplo, para uso nos processos de Integração e Transição). Quando o elemento é armazenado, as informações do produto e de configuração são capturadas pelos processos de Gerenciamento de Configuração e Gerenciamento de Informações.

- 6) Registrar evidências objetivas de que o elemento do sistema de software atende aos requisitos.
NOTA As evidências são fornecidas conforme os acordos de fornecimento, legislação e políticas da organização. As evidências incluem modificações de elementos feitas devido ao tratamento de mudanças ou não conformidades encontradas durante os processos de Verificação e Validação.

A evidência objetiva faz parte da baseline de configuração do elemento conforme foi implementado, estabelecida por meio do Processo de Gerenciamento de Configuração e inclui os resultados de testes unitários, análises, inspeções, eventos de walkthrough, demonstrações, revisões técnicas ou de produto, ou outras técnicas de verificação.

- c) Gerenciar os resultados da implementação. Esta atividade consiste nas seguintes tarefas:
  - 1) Registrar resultados da implementação e anomalias encontradas.
NOTA Isto inclui anomalias devido à estratégia de implementação, sistemas habilitadores de implementação ou definição incorreta do sistema de software. Os processos de Avaliação e Controle de Projeto e de Garantia da Qualidade são utilizados para analisar os dados e identificar a causa-raiz, permitir ações corretivas ou de melhoria e registrar lições aprendidas.

  - 2) Manter a rastreabilidade dos elementos do sistema de software implementados.
NOTA 1 Fontes de licenças de software e outros ativos do sistema na cadeia de suprimentos são registrados para apoiar a rastreabilidade ao longo do ciclo de vida durante operações e manutenção. Os processos de Gerenciamento de Informações e de Gerenciamento de Configuração são usados para manter os termos de licença, suporte e manutenção para um aplicativo de software e sua infraestrutura necessária (sistema host). A ISO/IEC 19770 fornece requisitos para um sistema de gestão de ativos

NOTA 2 A rastreabilidade bidirecional é mantida entre os elementos implementados e a arquitetura do sistema de software; design e requisitos relacionados, incluindo requisitos de interface e definições necessárias para a implementação; e planos, procedimentos e resultados de validação e verificação.

  - 3) Fornecer artefatos-chave e itens de informação selecionados para baselines.
O Processo de Gerenciamento de Configuração é usado para estabelecer e manter itens de configuração e baselines. Este processo identifica os candidatos para a baseline, e o processo de Gerenciamento da Informação controla os itens de informação. Para este processo, os elementos do sistema de software (por exemplo, código fonte), pacotes de software e resultados de testes unitários são artefatos típicos que são colocados em baselines.


### 6.4.8 Processo de Integração


#### 6.4.8.1 Propósito

O propósito do Processo de Integração é sintetizar um conjunto de elementos do sistema em um sistema construido (produto ou serviço) que satisfaça os requisitos do sistema/software, arquitetura e design.

Este processo consolida os elementos implementados do sistema. As interfaces são identificadas e ativadas para permitir a interoperabilidade dos elementos do sistema conforme pretendido. Este processo integra os sistemas habilitadores com o sistema de interesse para facilitar a interoperabilidade.

A integração do sistema de software combina iterativamente elementos implementados do sistema de software para formar configurações completas ou parciais do sistema, a fim de construir um produto ou serviço. A integração de software é normalmente executada com frequência diária ou continuamente durante as etapas de desenvolvimento e manutenção, utilizando ferramentas automatizadas. A integração contínua envolve inclusão ou substituição frequente de itens, e o seu arquivamento em bibliotecas de software sob controle de configuração.

As interfaces são definidas pelos processos de Definição de Arquitetura e Definição de Design. • Processo de Integração atua de forma coordenada com esses outros processos para verificar

se as definições de interface, como foram implementadas e integradas, são adequadas e se levam em conta as necessidades de integração.


#### 6.4.8.2 Resultados Esperados

Como resultado da implementação bem-sucedida do Processo de Integração:

- a) As restrições de integração que influenciam os requisitos do sistema, arquitetura ou design, incluindo interfaces são identificadas.
- b) Os pontos de verificação e a abordagem para o funcionamento correto da consolidação das interfaces e funções do sistema são definidos.
- c) Todos os sistemas ou serviços habilitadores necessários para a integração estão disponíveis.
- d) Um sistema composto por elementos implementados do sistema é integrado.
- e) As interfaces entre os elementos implementados, que compõem o sistema, são verificadas.
- f) As interfaces entre o sistema e o ambiente externo são verificadas.
- g) Os resultados da integração e anomalias são identificados.
- h) A rastreabilidade dos elementos do sistema integrado é estabelecida.

#### 6.4.8.3 Atividades e tarefas

O projeto deve implementar as seguintes atividades e tarefas de acordo com as políticas e os procedimentos organizacionais aplicáveis relacionados ao Processo de Integração.

- a) Preparar para a integração. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir a estratégia de integração.
NOTA 1 A integração constrói sequências progressivamente mais completas de configurações do elemento do sistema de software ou item de software. Ela depende da disponibilidade do elemento do sistema de software aplicável e é consistente com uma estratégia de isolamento e diagnóstico de falhas. Sucessivas aplicações dos processos de Integração, de Verificação e, quando apropriado, de Validação, são repetidas para elementos na estrutura do sistema até que o sistema de interesse tenha sido construído. Simuladores ou protótipos são tipicamente utilizados para elementos do sistema que ainda não foram implementados, por exemplo, recebendo dados de sistemas de interface. A integração dos elementos implementados do sistema de software baseia-se nas prioridades dos requisitos relacionados e na definição da arquitetura, tipicamente focando as interfaces, paralelamente à minimização do tempo de integração, do custo e dos riscos. A integração do sistema de software geralmente mantém o controle de versão dos itens de configuração selecionados, a serem integrados, por meio do Processo de Gerenciamento de Configuração.

NOTA 2 Para a integração do software, a estratégia de integração normalmente é consistente com uma estratégia de regressão, que é aplicada para reverificar elementos de software quando são alteradas unidades de software relacionadas, incluindo requisitos, design e documentação potencialmente associados.

NOTA 3 A definição de uma estratégia para integração de unidades e elementos de software normalmente acompanha a definição de estratégias para outros processos que ocorrem simultaneamente, como:

O Processo de Implementação para ajudar a garantir a coordenação oportuna das tarefas dos Processo de Implementação e de Integração e os sistemas

habilitadores, por exemplo, ambientes combinados de desenvolvimento e teste de software para apoiar a implementação e a integração automatizada e/ou contínua de unidades e elementos de software.

O Processo de Verificação para fornecer evidências objetivas de que o software integrado atende aos seus requisitos especificados e para identificar anomalias (erros, defeitos, falhas) em elementos, itens e unidades de software, processos, e itens de informação relacionados à integração (por exemplo, requisitos de sistema/software, arquitetura, design, teste ou outras descrições).

O Processo de Validação para confirmar que um produto de trabalho atende aos seus requisitos para um uso específico pretendido de uma função de software integrada.

iv. O processo de Garantia da Qualidade para apoiar o Processo de Integração, auditorias e inspeções de produtos de trabalho, e resolver problemas, não conformidades ou relatos e tratamento de incidentes.

NOTA 4 A estratégia de integração é normalmente registrada em um plano, por exemplo, um plano de integração, ou o SDP ou SEMP de um projeto.

- 2) Identificar e definir critérios de integração e pontos em que o funcionamento correto, a integridade das interfaces e as funções selecionadas do sistema de software são verificados.
A verificação detalhada das interfaces é executada usando o Processo de Verificação. A integração do software normalmente envolve a combinação dos elementos de software, resultando em um conjunto integrado, que é consistente com o design do software, e que satisfaz os requisitos funcionais e não funcionais do sistema/software em um ambiente equivalente ao de operação.

Para projetos envolvendo vários fornecedores ou equipes de desenvolvimento, a disponibilidade de elementos do sistema de software para integração costuma fazer parte do cronograma do projeto com marcos no Processo de Avaliação e Controle de Projeto. A integração prossegue à medida que o software é verificado em sua funcionalidade, desempenho e adequação para ambientes específicos da instalação ou da plataforma. Normalmente são definidos checkpoints para revisões e validações com stakeholders nos principais pontos de integração como, por exemplo, a conclusão de uma fase, elemento ou versão. A frequência destas análises críticas está relacionada

- 3) Identificar e planejar os sistemas ou serviços habilitadores necessários para apoiar a integração.
NOTA Isto inclui a identificação de requisitos e interfaces para os sistemas habilitadores. Os sistemas habilitadores para integração geralmente incluem instalações de integração, equipamentos especializados, sistemas de treinamento, sistemas de notificação de divergências, simuladores, dispositivos de medição e segurança ambiental. Para software, isto pode envolver suites de teste de regressão e sistemas de controle de configuração para o teste integrado de sistemas de software, sistemas de notificação de incidentes e problemas, simuladores representando sistemas externos ou elementos não desenvolvidos, e sistemas de gerenciamento de bibliotecas de software para operações de desenvolvimento. Alterações ou funções específicas necessárias para que os sistemas habilitadores apoiem as tarefas de integração precisam ser identificadas e definidas. Normalmente, os sistemas ou serviços habilitadores utilizados para integração durante as etapas de desenvolvimento também podem ajudar a apoiar a integração de elementos do sistema à medida que o sistema de software e os ambientes habilitadores evoluem para o status de operação. A abordagem DevOps apoia implementação integração, verificação, transição, validação, operação e processos de manutenção iterativos de sistemas de software.

  - 4) Obter ou adquirir acesso aos sistemas ou serviços de apoio a serem utilizados para apoiar a integração.
NOTA O Processo de Validação é utilizado para confirmar objetivamente que um sistema de apoio a integração alcança seu uso pretendido para suas funções de apoio.

  - 5) Identificar as restrições para que a integração seja incorporada nos requisitos do sistema/software, arquitetura ou design.
NOTA Isto inclui requisitos como acessibilidade, segurança da cadeia de suprimentos, proteção para integradores, interconexões requeridas para conjuntos de elementos implementados do sistema de software, para habilitadores e para restrições de interface.

- b) Realizar integração. Integrar sucessivamente as configurações do elemento do sistema de software até que o sistema completo esteja finalizado. Esta atividade consiste nas seguintes tarefas:
  - 1) Obter elementos implementados do sistema de software de acordo com os cronogramas acordados.
NOTA Os elementos implementados do sistema de software ou outros recursos fornecidos pelos desenvolvedores ou recebidos de fornecedores ou adquirentes geralmente são colocados sob controle de configuração. Os elementos são tratados de acordo com as considerações relevantes de saúde, proteção, segurança e privacidade.

  - 2) Integrar os elementos implementados.
NOTA 1 Esta tarefa é realizada para alcançar a configuração do elemento do sistema de software (completo ou parcial) conectando os elementos implementados conforme prescrito na estratégia de integração, utilizando os procedimentos definidos, as descrições de controle de interface e os sistemas habilitadores previstos.

NOTA 2 Em termos de software, integrar os elementos implementados pode envolver a vinculação de código objeto ou simplesmente reunir os elementos implementados que fazem parte da configuração do software em uma abordagem metódica componente a componente. Os elementos de software são tipicamente compilados em um build para que as unidades ramificadas sejam devidamente ligadas ou integradas no elemento montado. Elementos de firmware são produzidos, muitas vezes como protótipos, e instalados em elementos de hardware. Se as funções de software ainda não estiverem disponíveis para integração, a funcionalidade emulada (stubs ou scaffolding) pode ser usada para suportar temporariamente a integração de elementos de software ou representar a entrada de interfaces externas. As agregações bem-sucedidas resultam em um elemento de software integrado, armazenado e disponível para processamento posterior, ou seja, integração, verificação ou validação de elementos adicionais do sistema de software.

NOTA 3 Ao realizar a integração do software e sistema, identificar e definir pontos de controle se surgirem preocupações com a segurança e interoperabilidade. Por questões de segurança ou privacidade, os processos de integração e verificação frequentemente utilizam dados fictícios. A ISO/IEC/IEEE 15026 e a série ISO/IEC 27000 incluem informações sobre garantia, integridade e considerações de segurança que afetam a integração.

  - 3) Verificar se as interfaces ou funções integradas de software funcionam desde o início até uma finalização prevista dentro de uma faixa esperada de valores de dados.
NOTA Como parte da aceitação dos elementos implementados do sistema de software, os elementos selecionados são verificados para ajudar a garantir que atendam aos critérios de aceitação, conforme especificado na estratégia de integração e nos acordos aplicáveis. A verificação pode incluir

conformidade com a configuração acordada, compatibilidade de interfaces e presença de itens de informação obrigatórios. O Processo de Avaliação e Controle de Projeto pode ser usado de acordo com a estratégia de integração para planejar e realizar revisões técnicas dos elementos integrados do sistema de software, por exemplo, uma revisão de prontidão de teste para ajudar a garantir que o elemento ou o sistema integrado com seus dados associados e itens de informação estão prontos para testes de qualificação.

- c) Gerenciar resultados de integração. Esta atividade consiste nas seguintes tarefas:
  - 1) Registar resultados de integração e anomalias encontradas.
Isto inclui anomalias devido à estratégia de integração, à integração dos sistemas habilitadores, a execução da integração, à definição incorreta do sistema ou elemento. Quando existem inconsistências na interface entre o sistema, seu ambiente operacional especificado e sistemas que permitem a fase de utilização, os desvios levam a ações corretivas. A resolução da anomalia geralmente envolve os Processos Técnicos, muitas vezes repetitivos no Processo de Implementação. O processo de Garantia da Qualidade e o Processo de Avaliação e Controle de Projeto são usados para analisar os dados para identificar a causa-raiz, permitir ações corretivas ou de melhoria e registrar lições aprendidas.

  - 2) Manter a rastreabilidade dos elementos integrados do sistema de software.
NOTA A rastreabilidade bidirecional é mantida entre os elementos do sistema integrado e a arquitetura do sistema de software, design e requisitos de sistema ou elemento, como casos de uso, requisitos de interface e definições necessários para a integração. Os elementos do software integrado e seus componentes são identificados por versão. As versões dos elementos de software integrados são normalmente rastreaveis as unidades implementadas, aos procedimentos e casos de testes.

  - 3) Fornecer artefatos-chave e itens de informação selecionados para baselines.
NOTA O Processo de Gerenciamento de Configuração é usado para estabelecer e manter itens de configuração e baselines. O Processo de Integração identifica os candidatos para a baseline, e o processo de Gerenciamento da Informação controla os itens de informação. Para este processo, os casos de testes, testes de regressão e scripts de testes automatizados são artefatos típicos para colocar sob baseline. A estratégia de integração é um item de informação típico para colocar em baseline.


### 6.4.9 Processo de Verificação


#### 6.4.9.1 Propósito

O propósito do Processo de Verificação é prover evidências objetivas de que o sistema ou um elemento do sistema atende aos seus requisitos e características especificados.

O Processo de Verificação identifica as anomalias (erros, defeitos ou falhas) em qualquer item de informação (por exemplo, requisitos de sistema/software ou descrição da arquitetura), elementos implementados do sistema ou processos de ciclo de vida usando métodos, técnicas, normas ou regras apropriadas. Este processo fornece as informações necessárias para determinar a resolução de anomalias identificadas.

A verificação pode ser executada em todos os processos técnicos. O Processo de Verificação é tipicamente usado em pontos chave no ciclo de vida de um sistema de software para demonstrar que os requisitos (incluindo requisitos funcionais e não funcionais) foram atendidos, ou que os resultados do processo foram alcançados ou as atividades do processo foram executadas. Diferentes domínios e comunidades de engenharia ou de desenvolvimento podem identificar os marcos, estratégias de verificação e critérios de forma diferente.

Para sistemas de software, o Processo de Verificação é tipicamente instanciado para os seguintes propósitos:

- a) Para confirmar que um produto de trabalho ou serviço de software reflete adequadamente os requisitos especificados (muitas vezes chamado de verificação de software);
- b) Para confirmar que o produto de software integrado atende aos seus requisitos definidos (muitas vezes chamado de teste de qualificação de software); e
- c) Para confirmar que a implementação de cada requisito do sistema/software é testada em relação à conformidade e que o sistema de software está pronto para entrega (muitas vezes chamado de teste de qualificação do sistema).
NOTA 1 O Processo de Verificação determina que "o produto é construído corretamente". O Processo de Validação determina que o é construído o produto correto.

NOTA 2 A ISO/IEC/IEEE 29119 Software and systems engineering - Software testing (em várias partes) fornece processos e técnicas detalhadas para verificação realizada por meio de testes. A IEEE Std 1012-2012, IEEE Standard for System and Software Verification and Validation, fornece detalhes adicionais sobre estes processos para sistemas, software, hardware e interfaces que estão sendo desenvolvidos, mantidos ou reutilizados.

NOTA 3 O SWEBOK, Guide to the Software Engineering Body of Knowledge, fornece uma discussão detalhada sobre testes de software. Esta área de conhecimento aborda fundamentos, terminologia, questões, técnicas, aplicação, planejamento de processos, medidas, ferramentas, considerações práticas e referências. O guia também discute Verificação e Validação de Software em termos de processos de Gerenciamento de Qualidade de Software, e identifica métodos e técnicas que apoiam a Verificação e a Validação. O SWEBOK também aborda tópicos como construção de software para verificação e suporte a modelos e métodos de engenharia de software.


#### 6.4.9.2 Resultados esperados

Como resultado da implementação bem-sucedida do Processo de Verificação:

- a) As restrições de verificação que influenciam os requisitos, arquitetura ou design são identificadas.
- b) Quaisquer sistemas ou serviços habilitadores necessários para verificação estão disponíveis.
- c) O sistema ou elemento do sistema é verificado.
- d) Os dados que fornecem informações para ações corretivas são relatados.
- e) As evidências objetivas de que o sistema construído atende aos requisitos, arquitetura e design são fornecidas.
- f) Os resultados de verificação e anomalias são identificados.
- g) A rastreabilidade entre os elementos do sistema verificados é estabelecida.

#### 6.4.9.3 Atividades e tarefas

O projeto deve implementar as seguintes atividades e tarefas de acordo com as políticas e os procedimentos organizacionais aplicáveis relacionados ao Processo de Verificação.

- a) Preparar-se para verificação. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir a estratégia de verificação, que inclui o seguinte:
NOTA 1 Uma estratégia de verificação geralmente foca em minimizar custos, cronograma ou riscos, tornecendo uma abordagem equilibrada para confirmar que o sistema de software ou elemento foi "construído corretamente".

A estratégia de verificação e o cronograma são responsáveis pelas mudanças dinâmicas quando ocorrem resultados inesperados (eventos, incidentes ou problemas). De acordo com o andamento do projeto, as ações de verificação planejadas são redefinidas ou replanejadas quando ocorrem eventos inesperados ou evoluções do sistema.

NOTA 3 A estratégia de verificação pode ser documentada em um plano, por exemplo, um plano de verificação ou o PDS (Plano de Desenvolvimento de Software) ou PGES (Plano de Gerenciamento de Engenharia de Software) de um projeto.

i. Identificar o escopo de verificação, incluindo o artefato, elemento ou sistema de software, as propriedades a serem verificadas e os resultados esperados.

NOTA O escopo geral de verificação inclui o sistema de software de interesse ou elementos do sistema, incluindo interfaces. Para cada ação de verificação, o escopo identifica o artefato, elemento ou sistema de software a ser verificado (por exemplo, o sistema real ou um modelo, um protótipo, código, um procedimento, um plano ou outro documento) e os resultados esperados, como conformidade, ou desempenho, tolerância a falhas e recuperação apos interrupção do serviço. As propriedades a serem verificadas podem incluir requisitos, características de arquitetura e design, integração e acurácia da documentação. As características do design podem incluir implicações de segurança no design no contexto do ambiente operacional planejado e de atendimento às características críticas de qualidade,

Identificar as restrições que potencialmente limitam a viabilidade das ações de verificação.

NOTA As restrições incluem viabilidade técnica, custo, tempo, disponibilidade de habilitadores de verificação ou de pessoal qualificado, restrições contratuais e características, como criticidade da missão. Tais restrições muitas vezes levam em consideração a estratégia de verificação, por exemplo, se um esforço de verificação por uma organização independente é necessário ou justificado.

iii. Identificar as prioridades de verificação.

NOTA Nos sistemas de software, a verificação de cada cenário possível (cobertura de código 100 %) é tipicamente inviável. A estratégia de verificação normalmente inclui o trade-off do que será verificado (escopo) em relação às restrições ou limites, e deduzir quais ações de verificação realizar e quantas iterações de ações de verificação e retrabalho são necessárias para reduzir riscos. Uma abordagem de teste baseada em modelos pode permitir a geração e o gerenciamento de vários cenários. Os riscos de possíveis exclusões de ações de verificação são avaliados.

  - 2) Identificar as restrições da estratégia de verificação a ser incorporada nos requisitos, arquitetura ou design do sistema/software.
NOTA Isto inclui limitações práticas de precisão, incerteza e repetibilidade que são impostas pelos habilitadores de verificação, os métodos de medição associados, a necessidade de integração do sistema de software e a disponibilidade, acessibilidade e interconexão com habilitadores.

  - 3) Definir o propósito, as condições e os critérios de conformidade para cada ação de verificação.
  - 4) Selecionar técnicas ou métodos de verificação adequados e critérios associados para ações de verificação, como inspeção, análise, demonstração ou testes.
NOTA 1 A seleção de métodos ou técnicas de verificação é feita de acordo com o tipo de sistema, o propósito da verificação, os objetivos do projeto e os riscos aceitáveis. Métodos ou técnicas de verificação incluem inspeção (incluindo walkthroughs e análises criticas por pares), análise (incluindo modelagem e simulação e analogia/similaridade), demonstração e testes dinâmicos e estáticos.

NOTA 2 A abordagem, os métodos e as técnicas de verificação selecionados podem ser coordenados com os stakeholders relevantes para ajudar a garantir que a abordagem de verificação seja aceitável.

  - 5) Identificar e planejar os sistemas ou serviços habilitadores necessários para apoiar a verificação.
Os sistemas habilitadores de verificação incluem instalações de verificação, pessoal qualificado, equipamentos, simuladores, ferramentas de automação de testes e sistemas de gerenciamento de incidentes e problemas. A verificação do sistema de software é tipicamente realizada em ambientes controlados distintos que não interferem no software operacional ou no desenvolvimento contínuo. Se os sistemas habilitadores para verificação tiverem capacidade diferente do ambiente operacional planejado, o Processo de Medição pode ser usado para calibrar o desempenho dos sistemas habilitadores

  - 6) Obter ou adquirir acesso aos sistemas ou serviços habilitadores a serem usados para apoiar a verificação.
A aquisição dos sistemas habilitadores pode ser feita de diversas formas como aluguel, aquisição, desenvolvimento, reutilização de ativos organizacionais ou subcontratação. Normalmente, a aquisição do conjunto completo de habilitadores é uma mistura destas formas. O Processo de Validação é utilizado para confirmar objetivamente que o sistema de apoio à verificação alcança o seu uso pretendido para as suas funções habilitadoras.

- b) Executar a verificação. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir os procedimentos de verificação, cada um apoiando uma ou mais ações de verificação.
NOTA Os procedimentos de verificação, que podem ser realizados por scripts automatizados, incluem os requisitos a serem verificados, o tipo de elemento ou artefato do sistema de software a ser verificado (por exemplo, o sistema real ou um modelo, um protótipo, código, um procedimento, um plano ou outro item de informação), e os resultados esperados (critérios de sucesso), como conformidade ou desempenho de uma função ou capacidade em termos de tempo de resposta ou throughput. Os procedimentos identificam o propósito da verificação com critérios de sucesso (resultados esperados), técnica de verificação a ser aplicada, os sistemas habilitadores necessários (instalações, equipamentos) e condições ambientais para realizar cada procedimento de verificação (recursos, pessoal qualificado, configuração especializada dos procedimentos ou instruções de trabalho). Os procedimentos de verificação incluem como os resultados do procedimento de verificação serão registrados, analisados, armazenados e relatados.

  - 2) Executar os procedimentos de verificação.
A verificação ocorre, de acordo com a estratégia de verificação, no momento adequado do cronograma, no ambiente definido, com sistemas habilitadores e recursos definidos. O desempenho de uma ação de verificação consiste em capturar um resultado da execução do procedimento de verificação; comparar o resultado obtido e registrado com o resultado esperado; e obter um grau de corretude (ou sucesso/fracasso) do elemento submetido.

- c) Gerenciar os resultados da verificação. Esta atividade consiste nas seguintes tarefas:
  - 1) Analisar criticamente os resultados de verificação e anomalias encontradas e identificar ações de acompanhamento.
NOTA 1 Isto inclui anomalias devido à estratégia de verificação, sistemas habilitadores da verificação, execução da verificação ou definição incorreta do sistema. Os processos de Controle e Avaliação de Projeto e de Garantia de Qualidade são utilizados para analisar os dados para identificar a causa-raiz, possibilitar ações corretivas ou de melhoria e registrar lições aprendidas.

NOTA 2 A avaliação dos resultados de verificação e acompanhamento das ações corretivas pode variar muito dependendo do propósito da verificação. Para elementos de software, exemplos incluem uma modificação ou renúncia de requisitos, uma simples correção de defeito para um elemento de software que falhou, seguido de reverificação ou redirecionamento total do projeto por conta de uma falha em alcançar um marco, por exemplo, falha do sistema de software em testes de qualificação. Muitas vezes soluções simples ou recomendadas para anomalias descobertas durante a verificação são registradas junto com o resultado de verificação para facilitar a análise e possíveis ações corretivas.

  - 2) Registrar incidentes e problemas durante a verificação e acompanhar a sua resolução.
NOTA 1 A execução da resolução de problemas é tratada por meio dos processos de Garantia de Qualidade e de Controle e Avaliação de Projetos. Durante a verificação do software, as condições em que o problema ocorreu são documentadas para que, se possivel, o problema possa ser replicado e a causa raiz do defeito do software identificada. Alterações nos requisitos, arquitetura, design ou elementos do sistema são feitas utilizando outros processos Técnicos.

  - 3) Obter o acordo dos stakeholders de que o sistema ou o elemento de software atende aos requisitos especificados.
  - 4) Manter a rastreabilidade dos elementos do sistema de software verificado.
NOTA A rastreabilidade bidirecional é mantida entre os elementos do sistema verificado e o registro da atividade de verificação, a arquitetura do sistema, o design ou os requisitos de sistema/software.

  - 5) Fornecer artefatos-chave e itens de informação selecionados para baselines.
NOTA O Processo de Gerenciamento de Configuração é usado para estabelecer e manter itens de configuração e baselines. Este processo identifica os candidatos para a baseline, e o Processo de Gerenciamento da Informação controla os itens de informação. Para este processo, a estratégia de verificação e os procedimentos de verificação são itens de informação típicos.


### 6.4.10 Processo de Transição


#### 6.4.10.1 Propósito

O propósito do Processo de Transição é estabelecer capacidade para um sistema fornecer serviços especificados pelos requisitos dos stakeholders no ambiente operacional.

Este processo transfere o sistema de forma ordenada e planejada para o status operacional, de modo que o sistema esteja funcional, operável e compatível com outros sistemas em operação. Instala um sistema verificado, juntamente com sistemas habilitadores relevantes, por exemplo, sistema de planejamento, sistema de suporte, sistema de treinamento de operadores, sistema de treinamento do usuário, conforme definido nos acordos. Este processo é utilizado em cada nível na estrutura do sistema e em cada fase para preencher os critérios estabelecidos para a saída da fase. Isto inclui preparar sistemas habilitadores de armazenamento, manuseio e envio aplicaveis.

Para sistemas de software, o propósito do Processo de Transição é estabelecer capacidade para um sistema fornecer serviços em um ambiente diferente.

O Processo de Transição é frequentemente usado para implantações recorrentes de software em diferentes ambientes, por exemplo, de um ambiente de desenvolvimento para um ambiente de teste ou de manutenção, ou entre varios ambientes de teste, ou de um ambiente operacional para outro (por exemplo, troca de hospedagem (rehosting) ou de serviços em nuvem). As transições para site de backup ou de contingência são tipicamente planejadas e simuladas para continuidade dos negócios e recuperação de desastres. A transição para sistemas de software pode envolver a realocação física de hardware, a instalação e ativação ou desativação de infraestrutura física ou virtual ou sistemas habilitadores em diferentes locais, ou nenhuma alteração na infraestrutura física. A transição pode envolver alterações nas fontes ou estrutura de dados, atualizações ou evoluções do software em uso. A transição inclui atualizações (patches) programadas recorrentes ou de emergência e correções de segurança e outras preocupações. A transição pode envolver a transferência entre as organizações e também abrange a inclusão de um grande grupo de novos usuários a um sistema ou serviço de software existente. A transição para um novo sistema é realizada frequentemente de forma simultânea com a descontinuação e a desativação de um sistema existente, implicando a migração de dados do sistema antigo para o seu substituto.

NOTA A transição pode envolver transferência de conhecimento usando o processo de Gerenciamento de Conhecimento.


#### 6.4.10.2 Resultados esperados

Como resultado da implementação bem-sucedida do Processo de Transição:

- a) As restrições de transição que influenciam os requisitos do sistema/software, arquitetura ou design são identificadas.
- b) Quaisquer sistemas ou serviços habilitadores necessários para a transição são disponibilizados.
- c) O ambiente é preparado.
- d) O sistema, conforme instalado em sua localização operacional, é capaz de entregar suas funções especificadas.
- e) Os operadores, usuários e outros stakeholders necessários à utilização e suporte ao sistema são treinados.
- f) Os resultados de transição e anomalias são identificados.
- g) O sistema instalado é ativado e pronto para operação.
- h) A rastreabilidade entre os elementos transitados é estabelecida.

#### 6.4.10.3 Atividades e tarefas

O projeto deve implementar as seguintes atividades e tarefas, de acordo com as políticas e os procedimentos organizacionais aplicáveis em relação ao Processo de Transição.

- a) Preparar para a transição do sistema de software. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir uma estratégia para gerenciar releases de software e outras transições de sistema de software, incluindo as seguintes considerações:
i. estabelecer o tipo de transição e os critérios de sucesso da transição;

ii. determinar a frequência de transições recorrentes, como atualizações e evoluções para sistemas de software em desenvolvimento, teste e operação;

iii. minimizar riscos de segurança, interrupção e tempo de inatividade durante a transição;

iv. arquivar, destruir ou converter e validar dados de sistemas anteriores para o novo sistema, incluindo dados recebidos por meio de interfaces externas;

v. planejar contingência para resolução de problemas, backup e retorno à última versão em funcionamento do sistema;

vi. agendar transições consistentes com o processamento contínuo dos negócios, com transição faseada ou sincronizada de sistemas;

vii. gerenciar mudanças para os stakeholders, incluindo parceiros de interface, operadores humanos, administradores de sistema e usuários de serviços ou sistemas de software;

NOTA As atividades de gerenciamento de mudanças são frequentemente conduzidas para projetar mudanças nos processos de negócios associados ao novo sistema, planejar a transição nos processos de negócios e obter o comprometimento dos usuários com o uso produtivo do novo sistema.

vill. estabelecer estrategias associadas para validar o sistema ou elemento em transição;

ix. iniciar o suporte ao usuário e as atividades de manutenção com a transferência e atualização da documentação do design do sistema, documentação do usuário e procedimentos de teste; e

executar simultaneamente os processos de Transição, Operação e Desativação, quando um novo sistema é ativado e um sistema antigo é desativado.

NOTA A estratégia inclui papéis e responsabilidades, autoridade de aprovação, uso de revisões de prontidão e treinamento.

- 2) Identificar e definir as mudanças na instalação, ambiente, rede de comunicações ou ambiente-alvo necessárias para a instalação ou transição do sistema de software.
Para cada transição, identificar e definir quaisquer mudanças necessárias na infraestrutura ou nos sistemas habilitadores. Uma pesquisa no ambiente pode ser realizada para identificar

exemplo, mudanças para manter a segurança fisica e segurança das informações do sistema.

Identificar as necessidades de informações e providenciar a documentação do usuário e o treinamento de operadores, usuários e outros stakeholders necessários para a utilização e suporte do sistema.

NOTA A transição inclui migração ou ativação do acesso dos usuários ao sistema de software. Os papéis dos usuários são estabelecidos e as contas dos usuários e os controles de acesso são implementados.

- 4) Preparar informações detalhadas para a transição, como planos, cronogramas e procedimentos.
NOTA 1 A estratégia de transição é comumente registrada em um plano, por exemplo, um plano de transição ou no PDS (Plano de Desenvolvimento de Software) ou PGES (Plano de Gerenciamento de Engenharia de Software) de um projeto. Os agendamentos da transição ajudam a validar que os recursos e a infraestrutura disponibilizados sejam suficientes para suportar a transição, para que as atividades possam ser executadas dentro de um prazo razoável para minimizar interrupções. Os agendamentos podem incluir simulações para transições complexas, nas quais procedimentos são testados para verificar as durações e corrigir os resultados, como backup e restauração de banco de dados e do sistema e instalação de software.

NOTA 2 Durante um período especificado de troca ou operação simultânea, a transferência de serviços é gerenciada para que a conformidade continua com as necessidades persistentes dos stakeholders ou com um nível de serviço acordado seja alcançada. Se for necessário um período de operações paralelas para os sistemas antigo e novo, procedimentos especiais são identificados e desenvolvidos para receber e utilizar dados de parceiros de interface.

- 5) Identificar as restrições para a transição do sistema a serem incorporadas nos requisitos, na arquitetura ou no design do sistema de software.
- 6) Identificar e planejar os sistemas ou serviços habilitadores necessários para apoiar a transição.
NOTA 1 Isto inclui a identificação de requisitos e interfaces para os sistemas habilitadores A transição geralmente envolve o uso de infraestrutura altamente automatizada para fornecer, instalar e ativar ou desativar o software. Para a distribuição digital de software, mudanças temporárias ou contínuas na conectividade são frequentemente necessárias para a migração de software e dados e para a manutenção contínua. Os sistemas habilitadores podem incluir sistemas alternativos

- 7) Obter ou adquirir acesso aos sistemas ou serviços habilitadores a serem utilizados.
NOTA 1 O Processo de Validação é usado para confirmar objetivamente que o sistema habilitador alcança o uso pretendido nas suas funções habilitadoras.

- b) Executar a transição. Esta atividade consiste nas seguintes tarefas:
  - 1) Preparar o ambiente de operação ou virtual de acordo com os requisitos de instalação.
NOTA A preparação do ambiente é realizada de acordo com as regulamentações aplicáveis da área de saúde, segurança e proteção ambiental. Ambientes virtuais e novos recursos de comunicação são inicializados e verificados. O envio e o recebimento de elementos físicos do sistema e sistemas habilitadores são preparados.

  - 2) Entregar o sistema ou componente de software para instalação no local e prazo acordados.
NOTA 1 Normalmente, o software é entregue eletronicamente. Para mídia física, hardware e sistemas de software embarcados, às vezes é necessário considerar o armazenamento temporário antes da entrega ou instalação.

NOTA 2 Entregar os itens de informação acordados em formato eletrônico ou físico, como material de treinamento, pacotes de suporte logístico ou documentação de usuário.

  - 3) Instalar o produto em seu ambiente operacional físico ou virtual e fazer o interfaceamento com o seu ambiente.
NOTA A instalação do produto inclui a sua configuração com os dados operacionais necessários, mudanças no ambiente ou nos processos de negócios. Os bancos de dados são instanciados e a migração de dados é executada quando aplicável. Licenças e acordos de manutenção para elementos do sistema e outras propriedades intelectuais são transferidos conforme os acordos estabelecidos.

  - 4) Fornecer documentação e treinamento de usuário necessários para a utilização e suporte do produto para operadores, usuários e outros stakeholders.
  - 5) Realizar a ativação e check-out, incluindo o seguinte, conforme acordado:
NOTA 1 Esta tarefa executa as etapas necessárias para colocar o produto em um status operacional, incluindo inicialização, avaliação das condições ambientais e outras avaliações de prontidão, de acordo com os procedimentos operacionais, políticas organizacionais e regulamentações. Em situações em que o local exato ou ambiente de operação não estiver disponível ou quando o software for acessado de vários locais ou dispositivos móveis, um exemplo representativo é selecionado.

Algumas vezes, os testes de aceitação são definidos em um acordo para garantir uma instalação satisfatória. Esta tarefa está relacionada ao Processo de Validação cujo propósito é confirmar objetivamente que o sistema atende aos requisitos dos stakeholders no ambiente operacional. Os testes de aceitação, conforme especificado no acordo, podem definir os critérios que demonstram que o sistema de software possui a capacidade de fornecer as funções e serviços necessários, quando instalados e mantidos em seu ambiente operacional. Uma atenção especial é dada às principais funções

NOTA 3 Como parte do Processo de Gerenciamento de Configuração, uma auditoria física de configuração e uma atualização da documentação para estar compatível são geralmente executadas no momento da ativação do sistema. Medidas antifraudes podem ser confirmadas.

i. Demonstrar a instalação adequada do sistema de software.

NOTA Esta tarefa pode incluir verificações de integridade de dados e operações, por exemplo, que o código do software e as representações de dados sejam inicializados, executados e finalizados, conforme especificado.

ii. Demonstrar que o produto instalado ou transitado é capaz de fornecer as funções requeridas.

NOTA Esta é uma tarefa de prontidão operacional que examina a prontidão da capacidade funcional para um status operacional. Atenção específica é dada às interfaces de dados e às preocupações de segurança: funções de garantia da informação e interoperabilidade são exercitadas.

iii. Demonstrar que as funções fornecidas pelo sistema são suportadas pelos sistemas habilitadores.

NOTA Esta é uma tarefa de prontidão operacional que examina a prontidão dos sistemas habilitadores para um status operacional. Por exemplo, a ativação do monitoramento, relatórios de problemas, controle de acesso, backup e recuperação, e assistência ao usuário (suporte ao cliente) são demonstrados.

iv. Analisar criticamente o sistema de software para garantir a prontidão operacional.

NOTA Isto inclui os resultados de demonstrações funcionais, atividades de validação demonstrações de sustentação. Umarevisãode prontidão pode serconduzida. Deficiências, riscos e problemas que afetam o sucesso da transição são resolvidos, aceitos, tolerados ou encerrados.

v. Colocar o sistema de software em operação.

NOTA Isto inclui fornecer suporte aos usuários, administradores e operadores durante o início das operações do sistema.

- c) Gerenciar os resultados da transição. Esta atividade consiste nas seguintes tarefas:
  - 1) Registrar os resultados da transição e as anomalias encontradas.
Isto inclui anomalias devido à estratégia de transição, sistemas habilitadores, execução da transição ou definição incorreta do sistema de software ou do banco de dados. Onde existirem inconsistências entre o sistema, seu ambiente operacional e sistemas habilitadores, os desvios são resolvidos por meio de ações corretivas, incluindo alterações de requisitos. Os processos de Avaliação e Controle de Projeto e de Garantia de Qualidade são usados para analisar os dados para identificar a causa-raiz, permitir ações corretivas ou de melhoria e registrar as lições aprendidas.

  - 2) Registrar incidentes e problemas de transição e acompanhar a sua resolução
NOTA A execução da resolução de problemas é realizada por meio dos processos de Garantia de Qualidade e de Avaliação e Controle de Projeto. Durante a transição, as condições sob as quais o problema ocorreu são documentadas para que, se possível, o problema possa ser replicado e a causa-raiz do defeito possa ser identificada. Alterações nos requisitos, arquitetura, design ou elementos do sistema de software são feitas usando outros Processos Técnicos.

  - 3) Manter a rastreabilidade dos elementos do sistema de software em transição.
NOTA A rastreabilidade bidirecional é mantida entre o sistema e os elementos transitados e implantados e as versões aprovadas e controladas do sistema de software e dos sistemas habilitadores.

  - 4) Fornecer artefatos principais e itens de informação selecionados para baselines.
NOTA O Processo de Gerenciamento de Configuração é usado para estabelecer e manter itens de configuração e baselines, incluindo elementos do sistema de software transitados. Este processo

identifica candidatos para a baseline e o Processo de Gerenciamento da Informação controla os itens de informação. Para este processo, a estratégia de transição, o material de treinamento e os procedimentos de instalação, transição e migração de dados e a documentação do usuário são itens de informação típicos que são colocados em baseline.


### 6.4.11 Processo de Validação


#### 6.4.11.1 Propósito

O propósito do Processo de Validação é fornecer evidências objetivas de que o sistema, quando em uso, cumpre seus objetivos de negócio e de missão e os requisitos dos stakeholders, alcançando o uso pretendido no ambiente operacional alvo.

O objetivo de validar um sistema ou elemento do sistema é adquirir confiança em sua capacidade de atingir sua missão ou uso pretendido, sob condições operacionais específicas. A validação é ratificada pelos stakeholders. Este processo fornece as informações necessárias para que anomalias identificadas possam ser resolvidas pelo processo técnico apropriado em que a anomalia foi criada.

O Processo de Validação é normalmente utilizado em pontos chave do ciclo de vida de um produto, para demonstrar que os requisitos do produto para o uso operacional pretendido pelos stakeholders foram atendidos. A validação também é aplicável aos artefatos de engenharia de software (vistos como elementos do sistema de software). Diferentes domínios e comunidades de engenharia ou de desenvolvimento podem identificar marcos, estratégias e critérios de validação de maneira diferente. Para sistemas de software, modelos de ciclo de vida altamente iterativos geralmente apresentam envolvimento frequente do adquirente, representante do usuário ou outros stakeholders, para validar, ESTES

por exemplo, a prioridade dos requisitos para inclusão em uma iteração, a usabilidade da interface do software por meio de protótipos e a adequação do software para executar tarefas de negócios e cumprir os conceitos operacionais.

Para sistemas de software, o Processo de Validação tem os seguintes propósitos:

- a) Confirmar o cumprimento dos requisitos para um uso específico pretendido do produto de trabalho de software (geralmente chamado de validação de software); e
- b) Alcançar a confiança (especialmente com um adquirente ou cliente) de que o produto entregue atende aos requisitos dos stakeholders e está apto para uso (geralmente chamado teste de aceitação de software).
NOTA 1 O Processo de Validação garante que o "produto certo foi construído". O Processo de Verificação garante que o *produto foi construído corretamente.

NOTA 2 Os critérios de aceitação, conforme usados nos testes de aceitação, incluem critérios para determinar se o produto entregue está apto ou não para uso. Os critérios de aceitação podem ser especificados e acordados entre duas partes, isto é, um adquirente e um fornecedor, e incluídos nos requisitos dos stakeholders.

NOTA 3 O padrão IEEE Std 1012-2012, IEEE Standard for System and Software Verification and Validation, fornece requisitos detalhados. The SWEBOK, Guide to the Software Engineering Body of Knowledge, discute a verificação e validação de software em termos de processos de Gestão da Qualidade de Software e contém métodos e técnicas que apoiam verificação e validação. O SWEBOK também aborda tópicos como validação de requisitos e modelo.


#### 6.4.11.2 Resultados esperados

Como resultado da implementação bem-sucedida do Processo de Validação

- a) Os critérios de validação para os requisitos dos stakeholders são definidos.
- b) A disponibilidade dos serviços requeridos pelos stakeholders é confirmada.
- c) As restrições de validação que influenciam os requisitos, arquitetura ou design são identificadas.
- d) O sistema ou elemento do sistema é validado.
- e) Todos os sistemas ou serviços habilitadores necessários para validação são disponibilizados.
†) Os resultados e anomalias de validação são identificados.

- g) A evidência objetiva de que o sistema ou elemento do sistema desenvolvido satisfaz as necessidades dos stakeholders é fornecida.
- h) A rastreabilidade dos elementos do sistema validados é estabelecida.

#### 6.4.11.3 Atividades e Tarefas

O projeto deve implementar as seguintes atividades e tarefas de acordo com as políticas e os procedimentos organizacionais aplicáveis relacionados ao Processo de Validação.

- a) Preparar para Validação. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir a estratégia de validação, que inclui o seguinte:
NOTA 1 Uma estratégia de validação geralmente se concentra em minimizar custos, cronogramas ou riscos, construindo progressivamente confiança na qualidade e adequação do sistema de software para os stakeholders.

NOTA 2 A estratégia de validação reflete o modelo do ciclo de vida e geralmente envolve repetir a validação para ciclos de vida iterativos, incrementais ou evolutivos.

NOTA 3 A estratégia de validação pode ser documentada em um plano, por exemplo, um plano de aceitação ou no PDS ou PGES de um projeto.

i. Identificar o escopo da validação, incluindo as características do sistema, elemento ou artefato de software a ser validado e os resultados esperados da validação.

NOTA A validação do sistema de software geralmente é realizada tanto em ambientes controlados distintos que não interferem no software operacional ou no desenvolvimento continuo, quanto em ambientes operacionais, geralmente antes do uso operacional completo (por exemplo, teste beta ou teste de aceitação por um período especificado, com critérios acordados). O escopo inclui os requisitos dos stakeho/ders, incluindo visões do sistema relacionadas (por exemplo, cenários ou conceito de operação) a serem avaliadas. O escopo depende do que é apropriado para a fase do ciclo de vida do sistema: o sistema, um elemento do sistema ou um artefato de engenharia, como uma descrição ou documento de conceito, um cenário operacional, um modelo, um mock-up ou protótipo. O escopo também inclui a avaliação de que o produto ou serviço de software é utilizável no ambiente pretendido para as funções principais ou críticas. Características adicionais a serem validadas podem incluir a usabilidade da documentação, recursos de tolerância a falhas, resiliência e recuperação do software.

Identificar restrições que potencialmente limitam a viabilidade das ações de validação.

Restrições incluem limitações práticas na precisão, incerteza e repetibilidade impostas pelos habilitadores de validação, pelos métodos de medição associados e pela disponibilidade, acessibilidade e interconexão com os habilitadores. A estratégia de validação é limitada pelo andamento do projeto; particularmente, as ações de validação planejadas são redefinidas ou reagendadas quando ocorrem eventos inesperados ou evoluções do sistema. A validação pode ser estendida para incluir medidas contínuas de satisfação do usuário e reclamações de clientes.

iii. Identificar prioridades de validação.

NOTA 1 Para fazer uso efetivo do tempo e conhecimento dos stakeholders, a validação geralmente se concentra nas prioridades dos stakeholders, enquanto a verificação é usada para requisitos não funcionais. As ações de validação que poderiam ser excluídas são avaliadas em relação aos riscos da retirada.

NOTA 2 O fornecedor, o adquirente ou um agente do adquirente participa ou executa a validação. A responsabilidade geralmente é designada no acordo.

- 2) Identificar restrições do sistema a partir da estratégia de validação a serem incorporadas nos requisitos dos stakeholders.
- 3) Definir propósito, condições e critérios de conformidade para cada ação de validação.
- 4) Selecionar métodos ou técnicas de validação apropriados e critérios associados para cada 00012 analogia/similaridade, demonstração, simulação, análise crítica por pares e testes. As técnicas de validação de software geralmente incluem demonstrações, inspeção, análises críticas e inspeções de código, testes de usabilidade e uso experimental do software (por exemplo, betatestes, testes ação de validação. Os métodos ou técnicas de validação de sistema de software incluem inspeção, análise,
operacionais, de usuários ou de aceitação com os critérios acordados). A seleção de métodos ou técnicas de validação é feita de acordo com o tipo de sistema, o objetivo da validação, os objetivos do projeto, os requisitos legais e regulamentares e os riscos aceitáveis de uma ação de validação. Para sistemas de software com interação humana, o teste de usabilidade é comumente usado para validar que usuários representativos podem atingir objetivos especificados com eficácia, eficiência e satisfação em um contexto de uso específico. Detalhes adicionais para testes de usabilidade são encontrados no ISO/EC TR 25060:2010 Systems and software engineering - Systems and software product Quality Requirements and Evaluation (SQuaRE) - Common Industry Format (CIF) for usability: General framework for usability-related information.

NOTA 2 Quando apropriado, fases ou estados de validação são definidos (por exemplo, validação interna, validação no local, validação operacional) que aumentam progressivamente a confiança na conformidade do sistema de software em desenvolvimento e auxiliam no diagnóstico de quaisquer discrepâncias encontradas.

NOTA 3 Os critérios para aceitação dos stakeholders do desempenho do serviço geralmente são declarados como nível de serviço e registrados em um ANS (Acordos de Nível de Serviço). Os níveis de serviço geralmente medem capacidade, disponibilidade, confiabilidade e prontidão de resposta para os serviços, e resultam em requisitos de desempenho para os sistemas de suporte.

- 5) Identificar e planejar sistemas ou serviços habilitadores necessários para dar suporte à validação.
NOTA Os sistemas habilitadores podem incluir simuladores, laboratório de usabilidade ou de teste, pessoal qualificado, stakeholders e representantes de usuários, de acordo com métodos ou técnicas

de validação selecionados. Isto inclui a identificação de requisitos e interfaces para os sistemas habilitadores.

  - 6) Obter ou adquirir acesso aos sistemas ou serviços habilitadores para apoiar a validação.
NOTA O Processo de Gerenciamento de Infraestrutura ou Processo de Aquisição podem ser usados para obter acesso aos sistemas habilitadores, como aluguel, aquisição, desenvolvimento, reutilização ou subcontratação. Normalmente, o acesso ao conjunto completo de habilitadores é uma combinação destas formas. O Processo de Validação também é usado para confirmar objetivamente que o sistema habilitador de validação atinge o seu uso pretendido para as suas funções habilitadoras.

- b) Realizar validação. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir os procedimentos de validação, cada um apoiando uma ou um conjunto de ações de validação.
NOTA Os procedimentos de validação identificam os requisitos dos stakeho/ders a serem validados, o artefato do sistema de software associado (por exemplo, o sistema real, ou um modelo, uma maquete, um protótipo, um código, um conjunto de instruções ou outro item de informação), e os resultados esperados (critérios de sucesso), como o desempenho total e adequado de uma função. Os procedimentos identificam o propósito de validação com critérios de sucesso (resultados esperados), a técnica de validação a ser aplicada, os sistemas habilitadores necessários (instalações, equipamentos) e as condições de ambiente para executar cada procedimento de validação (recursos, pessoal qualificado, stakeholders participantes, instruções específicas para configuração e instalação). A estratégia de validação contempla informações sobre como os resultados de validação serão registrados, analisados, armazenados e relatados.

  - 2) Executar procedimentos de validação no ambiente definido.
NOTA A validação ocorre, de acordo com a estratégia de validação, no momento apropriado do cronograma, em um ambiente definido (como o ambiente operacional, um ambiente de teste similar ou outro ambiente representativo), com habilitadores e recursos definidos. A execução de uma ação de validação geralmente consiste na captura dos resultados de execução, comparando-se o resultado obtido com os critérios de sucesso, resultando em um grau de conformidade ou satisfação dos stakeholders com o sistema de software, elemento, serviço ou artefato de engenharia.

- c) Gerenciar resultados da validação. Esta atividade consiste nas seguintes tarefas:
  - 1) Analisar criticamente os resultados da validação e as anomalias encontradas e identificar as ações de acompanhamento.
NOTA 1 Confirmar se os serviços do sistema definidos pelos stakeho/ders estão disponíveis. As anomalias podem resultar da estratégia de validação, da validação de sistemas habilitadores, da execução da validação, da definição incorreta do sistema, ou do design, implementação e integração ineficiente ou ineficaz do sistema.

A avaliação dos resultados da validação e das ações de acompanhamento pode incluir a aceitação da anomalia como uma ocorrência de baixo risco. A ação corretiva pode variar bastante, dependendo do impacto do resultado da validação. Para elementos de software, os exemplos incluem uma correção simples de defeito para um elemento com falha de software, treinamento adicional para usuários, correções e esclarecimentos na documentação ou novo direcionamento do projeto com base no insucesso em atingir um marco importante, como, por exemplo, falhas nos testes de aceitação

  - 2) Registrar incidentes e problemas durante a validação e acompanhar a sua resolução.
NOTA O processo de Avaliação e Controle do Projeto e o processo de Garantia da Qualidade são usados para analisar os dados com o objetivo de identificar a causa raiz dos problemas, permitir ações

corretivas ou de melhoria e registrar as lições aprendidas. Durante a validação do software, a diferença entre as expectativas dos stakeholders e a execução do sistema é documentada para que, se possível, a causa raiz das discrepâncias possa ser identificada. A resolução de problemas normalmente envolve determinar a gravidade e o impacto do problema e se ou quando uma discrepância de software deve ser corrigida ou aceita por um tempo como um erro conhecido. Frequentemente, soluções simples ou recomendadas para anomalias descobertas durante a validação são registradas com o resultado da validação para facilitar a análise e a ação corretiva em potencial. As alterações reais nos requisitos dos stakeholders e do sistema/software, arquitetura, design ou elementos do sistema são realizadas pelos outros Processos Técnicos.

- 3) Obter o acordo dos stakeholders de que o sistema ou elemento de software atende às suas necessidades.
- 4) Manter a rastreabilidade dos elementos validados do sistema.
NOTA A rastreabilidade bidirecional é mantida entre os elementos validados do sistema e os requisitos dos stakeholders e o registro dos resultados da validação.

- 5) Fornecer os artefatos principais e itens de informação que foram selecionados para compor as baselines.
NOTA O Processo de Gerenciamento de Configuração é usado para estabelecer e manter itens de configuração e baselines. Este processo identifica candidatos para a baseline (como o sistema ou elemento de software validado) e o Processo de Gerenciamento da Informação controla os itens de informação. Para este processo, a estratégia de validação e os resultados da validação são itens de informação típicos que estão em baselines.


### 6.4.12 Processo de Operação


#### 6.4.12.1 Propósito

O propósito do Processo de Operação é utilizar o sistema para fornecer seus serviços.

Este processo estabelece requisitos e designa pessoal para operar o sistema, e monitora os serviços e o desempenho do sistema em operação. Para manter os serviços, identifica e analisa as anomalias operacionais em relação a acordos, requisitos dos stakeholders e restrições organizacionais.

O Processo de Operação normalmente visa a controlar ou reduzir o custo da operação, mantendo um nível de serviço aceitável ou melhorado.

Os sistemas de software podem ter infraestrutura dedicada, mas normalmente são operados em ambientes distribuídos, onde outros sistemas e serviços de software (por exemplo, a Internet) estão sendo utilizados. A segurança, a disponibilidade e o desempenho operacional do sistema de software de interesse são, portanto, motivo de preocupação em um sistema composto de sistemas. Ele pode incluir a integração com serviços preexistentes, simultâneos ou contínuos fornecidos por outros sistemas que fornecem serviços idênticos ou similares.

A ISO/IEC 20000-1:2011 (IEEE Std 20000-1) é um padrão de sistema de gerenciamento de serviços que especifica os requisitos para o projeto, transição, entrega e melhoria dos serviços operacionais, e apoia o Processo de Operação para atingir o seu propósito.

NOTA BRASILEIRA A ISO/IEC 20000-1:2011 foi substituída pela ISO/IEC 20000-1:2018, a qual foi adotada no Brasil como ABNT NBR ISO/IEC 20000-1:2020, Tecnologia da informação - Gestão de serviço - Parte 1: Requisitos do sistema de gestão de serviço.


#### 6.4.12.2 Resultados esperados

Como resultado da implementação bem-sucedida do Processo de Operação:

- a) As restrições de operação que influenciam os requisitos de sistema/software, arquitetura ou design são identificadas.
- b) Todos os sistemas e serviços habilitadores e materiais necessários para a operação estão disponíveis.
Os operadores qualificados e treinados estão disponíveis.

- d) Os serviços do sistema que atendem aos requisitos dos stakeholders são fornecidos.
- e) O desempenho do sistema durante a operação é monitorado.
O suporte ao cliente é fornecido.


#### 6.4.12.3 Atividades e Tarefas

O projeto deve implementar as seguintes atividades e tarefas de acordo com as políticas e procedimentos organizacionais aplicáveis relacionados ao Processo de Operação.

- a) Preparar para a operação. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir uma estratégia de operação, incluindo as seguintes considerações:
i. capacidade esperada ou acordada, disponibilidade, tempo de resposta e segurança dos serviços à medida que estes são introduzidos, operados e retirados;

estratégia relacionada aos recursos humanos, dependendo da necessidade de definir requisitos de treinamento e qualificação, treinar ou disponibilizar pessoal para controlar e monitorar as operações do sistema de software, administrar o acesso ao sistema e dar suporte às solicitações de serviço ao cliente e assistência ao usuário;

critérios e cronogramas de liberação do sistema de software para permitir modificações que apoiem os serviços existentes ou melhorados;

iv. abordagem para implementar os modos operacionais no Conceito Operacional, incluindo operações normais e preparativos, incluindo os testes, para tipos previstos de operações de contingência;

V. medidas para operação que fornecerão informações sobre os níveis de desempenho;

VI. estratégia de segurança operacional e ocupacional para operadores e outras pessoas que estejam usando ou em contato com o sistema de software durante a operação, levando em consideração as regulamentações de segurança; e

vii. estratégia de proteção ambiental e sustentabilidade para a operação do sistema de software.

NOTA A ISO/EC 16350 Information technology - Systems and software engineering - Application management, fornece orientações para aspectos operacionais.

  - 2) Identificar as restrições de operação do sistema a serem incorporadas em alterações nos requisitos do sistema/software, arquitetura, design, implementação ou transição.
  - 3) Identificar e planejar os sistemas ou serviços habilitadores necessários para dar suporte à operação.
NOTA Isto inclui a identificação de requisitos operacionais e interfaces com os sistemas habilitadores. Modos especiais do sistema operacional de software, por exemplo, um modo de treinamento, às vezes podem estar ativos paralelamente ou em substituição ao modo operacional completo. Os sistemas habilitadores incluem o monitoramento de alterações de ameaças (riscos) ao sistema de software.

  - 4) Obter ou adquirir acesso aos sistemas ou serviços habilitadores a serem utilizados.
NOTA O Processo de Validação e usado para confirmar objetivamente que o sistema habilitador à operação atinge o uso pretendido para as suas funções de habilitação.

  - 5) Identificar ou definir os requisitos de treinamento e qualificação dos recursos humanos para a operação do sistema de software.
NOTA O treinamento e a qualificação incluem o conhecimento do sistema de software em seu ambiente operacional e um programa definido de familiarização, com detecção adequada de falhas e instrução de isolamento. Os requisitos de conhecimento, habilidade e experiência do operador orientam os critérios de seleção de pessoal e, quando relevante, é fornecida autorização para operar o sistema. O escopo da qualificação depende do sistema de interesse e de seu ambiente. Por exemplo, em alguns ambientes, os requisitos regulatórios incluem a certificação de operadores, enquanto em outros não há esta necessidade.

  - 6) Designar pessoal treinado e qualificado para ser operador do sistema, dependendo da necessidade de intervenção humana e controle das operações.
NOTA Com a devida atenção à separação de tarefas, como controle administrativo do acesso ao sistema e investigação de problemas de segurança, muitos produtos de software modernos minimizam a necessidade de operadores diferentes dos usuários finais. Os operadores geralmente oferecem suporte aos sistemas habilitadores, como serviços em nuvem, softwares de sistema e banco de dados, monitoramento de segurança, armazenamento de dados e suporte técnico.

- b) Realizar a operação. Esta atividade consiste nas seguintes tarefas:
  - 1) Usar o sistema de software em seu ambiente operacional pretendido.
NOTA Quando acordado, a capacidade e a qualidade do serviço são mantidas interruptamente quando o sistema de software substitui um sistema ou elemento existente que está sendo descontinuado.

  - 2) Utilizar recursos materiais e outros, conforme necessário, para operar o sistema de software e manter os seus serviços.
NOTA Isto inclui fontes de energia para hardware, conectividade para software e operadores humanos ou automatizados.

  - 3) Monitorar a operação do sistema de software, incluindo as seguintes considerações:
gerenciar a aderência à estratégia de operação (por exemplo, procedimentos operacionais);

iL. registrar e relatar eventos significativos, como possíveis violações de confidencialidade e integridade de software e dados;

iii. operar o sistema de software de maneira segura e em conformidade com as diretrizes regulatórias, por exemplo, aquelas relacionadas à segurança do trabalho e proteção ambiental; e

iv. Registrar quando o desempenho do sistema ou serviço de software não está dentro dos parâmetros aceitáveis.

NOTA Isto inclui anomalias devido à estratégia da operação, sistemas habilitadores à operação, execução da operação ou definição incorreta do sistema de software. O sistema às vezes apresenta desempenho inaceitável quando os elementos do sistema implementados no hardware degradam ou excedem sua vida útil ou o ambiente operacional do sistema afeta a operação do software, por exemplo, carga de trabalho acima dos limites de capacidade, utilização por aplicativos concorrentes, hacks de segurança ou defeitos de software.

  - 4) Desenvolver, de forma consistente com a estratégia operacional, e, sempre que possível, automatizar os procedimentos operacionais para minimizar o risco de anomalias operacionais.
Isto inclui procedimentos para tratar solicitações de serviço e mudanças rotineiras (pré-aprovadas), solução de problemas e relatórios de incidentes, especialmente incidentes de segurança.

  - 5) Analisar as medições de forma consistente com a estratégia operacional para confirmar que: o desempenho do serviço está dentro dos parâmetros aceitáveis ou dos níveis ados para a dente
de serviço acordados para a carga de trabalho acordada;

її. a disponibilidade do sistema e serviço e os tempos de resposta são aceitáveis;

\#II. o custo da operação é consistente com objetivos e restrições; e

iv. as melhorias potenciais são identificadas e priorizadas.

NOTA O feedback e as sugestões do operador geralmente são informações úteis para melhorar o desempenho operacional do sistema de software. Os processos de Garantia da Qualidade e Medição podem ser aplicados.

  - 6) Executar operações de contingência, se necessário.
Isto inclui a operação do sistema de software em um modo degradado, a execução de operações de rollback e restauração, desligamento do sistema, implementação de procedimentos de solução de work-around para restaurar a operação ou outros modos em condições especiais. Se necessário, o operador executa os passos necessários para entrar em operação de contingência e, possivelmente, desligar o sistema. As operações de contingência são realizadas de acordo com procedimentos preestabelecidos para este evento. Frequentemente, estes procedimentos são acompanhados por um plano de continuidade.

- c) Gerenciar resultados de operação. Esta atividade consiste nas seguintes tarefas:
  - 1) Registrar os resultados da operação e as anomalias encontradas.
NOTA Os processos de Avaliação e Controle do Projeto e Garantia da Qualidade são usados para analisar os dados de incidentes e problemas para identificar a causa-raiz, permitir ações corretivas ou de melhoria e registrar as lições aprendidas.

  - 2) Registrar incidentes e problemas operacionais e acompanhar a sua resolução.
NOTA 1 A execução da resolução de incidentes e problemas é tratada pelos processos de Garantia da Qualidade e Avaliação e Controle do Projeto. Alterações nos requisitos, arquitetura, design ou elementos do sistema de software são feitas usando outros processos Técnicos.

NOTA 2 Se ocorrer um incidente durante a operação, o operador registra o incidente (ou é alertado com uma notificação automatizada) e executa as ações prescritas nos procedimentos operacionais validados para restabelecer as operações normais. Alguns procedimentos permitem o fornecimento de uma solução temporária até que a análise da causa raiz possa ser executada.

Durante a operação do software, as condições sob as quais o problema ocorreu são tipicamente documentadas, consistentes com a manutenção ou com o restabelecimento da disponibilidade operacional, para que, se possivel, o problema possa ser replicado em um ambiente de teste e a causa-raiz seja identificada. A resolução de problemas geralmente envolve determinar a gravidade e o impacto do problema. Dependendo dessa análise, pode-se determinar se ou quando o problema será corrigido ou aceito por um tempo.

  - 3) Manter a rastreabilidade dos serviços operacionais e itens de configuração.
NOTA A rastreabilidade bidirecional é mantida entre os serviços operacionais e as necessidades de negócios ou missão, conceito operacional, conceito de operações e requisitos dos stakeholders. Os itens de configuração operacionais são rastreáveis para as versões liberadas e validados por meio da auditoria de configuração física ou funcional.

  - 4) Fornecer artefatos principais e itens de informações que foram selecionados para compor as baselines.
NOTA Este processo identifica candidatos para a baseline e o Processo de Gerenciamento da Informação controla os itens de informação, como relatórios de desempenho do serviço operacional. Os artefatos principais (itens de informação) para Operação estão listados no Anexo B.

- d) Dar suporte ao cliente. Esta atividade consiste nas seguintes tarefas:
  - 1) Fornecer assistência e consultoria aos clientes e usuários para resolver reclamações, incidentes, problemas e solicitações de serviço.
NOTA 1 A assistência e a consultoria incluem o fornecimento ou a recomendação de fontes de treinamento, documentação, resolução de vulnerabilidades, atividades antifraude e outros serviços que apoiem o uso efetivo do sistema de software.

NOTA 2 O suporte ao cliente pode incluir comunicação com clientes de serviços, usuários e outros stakeholders para receber solicitações de serviço e alterações, resolver reclamações e fornecer informações sobre a resolução de incidentes e problemas.

  - 2) Registrar e monitorar solicitações e ações subsequentes de suporte.
  - 3) Determinar até que ponto o sistema ou os serviços de software fornecidos satisfazem as necessidades dos clientes e usuários.
Os resultados são analisados e ações necessárias são identificadas com o objetivo de restaurar ou alterar os sistemas ou serviços de software, a fim de proporcionar satisfação continua ao cliente e usabilidade do sistema de software. Sempre que possível, o benefício de tal ação é acordado com os stakeho/ders ou com seus representantes. Os dados de satisfação do cliente também servem como entrada para o Processo de Gestão da Qualidade.


### 6.4.13 Processo de Manutenção


#### 6.4.13.1 Propósito

O propósito do Processo de Manutenção é manter a capacidade do sistema de fornecer um serviço.

Este processo monitora a capacidade do sistema de entregar serviços, registra incidentes para análise, executa ações corretivas, adaptativas, de melhorias e preventivas e confirma a capacidade restabelecida.

Para sistemas de software, o Processo de Manutenção faz correções, alterações e melhorias nos sistemas e elementos de software implantados. A abordagem de manutenção de sistemas de software difere para sistemas disponibilizados gratuitamente, com ampla distribuição comercial ou operando em um pequeno número de ambientes controlados.

A necessidade de manutenção de um sistema de software, durante o seu ciclo de vida, pode ter múltiplas causas, além de defeitos latentes do sistema, como alterações nos sistemas de interface ou na infraestrutura, ameaças crescentes à segurança, obsolescência técnica dos elementos do sistema e sistemas habilitadores. Frequentemente, a extensão da capacidade, atualização de meia-vida ou evolução de sistemas legados se tornam um novo projeto de desenvolvimento de sistema de software que aplicará o conjunto de processos dentro de um ciclo de vida apropriado. Nestes casos, o processo de Gerenciamento de Portfólio é o ponto de partida para iniciar o trabalho. Em outros casos, a manutenção do sistema de software é executada como uma série continua de itens de trabalho priorizados, possivelmente com base no nível de esforço. A manutenção dos elementos do sistema de software pode incluir hardware, software e serviços, como serviços de comunicação ou web. A manutenção está fortemente ligada ao Processo de Gerenciamento de Configuração e à Gestão de Ativos de Software, e é realizada simultaneamente com os outros processos técnicos.

A ISO/IEC/IEEE 14764:2006 - Software Engineering - Software Life Cycle Processes - Maintenance e a ISO/IEC 16350 - Information technology - Systems and software engineering - Application management fornecem detalhes adicionais. O SWEBOK, Guide to the Software Engineering Body of Knowledge, área de conhecimento de Manutenção de Software, discute os fundamentos da manutenção de software, questões-chave, medição, técnicas, Processo de Manutenção, atividades de suporte e ferramentas. O guia também discute modelos, técnicas e medidas que apoiam a confiabilidade do software.


#### 6.4.13.2 Resultados esperados

Como resultado da implementação bem-sucedida do Processo de Manutenção:

- a) As restrições de manutenção que influenciam os requisitos, arquitetura ou design do sistema são identificadas.
- b) Todos os sistemas ou serviços habilitadores necessários para manutenção são disponibilizados.
- c) Os elementos de sistema substituídos, reparados ou revisados são disponibilizados.
- d) As necessidades de alterações para tratar manutenção corretiva, de melhoria ou adaptativa são relatadas.
- e) Os dados de falhas e de tempo de vida, incluindo custos associados, são determinados.

#### 6.4.13.3 Atividades e tarefas

O projeto deve implementar as seguintes atividades e tarefas, de acordo com as políticas e procedimentos da organizacionais aplicáveis relacionados ao Processo de Manutenção.

- a) Preparar para manutenção. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir uma estratégia de manutenção, incluindo as seguintes considerações:
L. Estabelecer prioridades, cronogramas tipicos e procedimentos para executar, verificar, distribuir e instalar alterações de manutenção de software em conformidade com os requisitos de disponibilidade operacional;

її. Estabelecer técnicas e métodos para ficar atento à necessidade de manutenção corretiva, adaptativa e de melhoria;

iii. Avaliações periódicas das características do design em caso de evolução do sistema de software e de sua arquitetura;

iv. Prever obsolescência potencial de componentes e tecnologias usando informações sobre mudanças técnicas em sistemas relacionados;

Estabelecer prioridades e recursos para obter acesso às versões corretas e às informações do produto necessárias para executar a manutenção (por exemplo, instalação programada ou faseada, patches de manutenção ou atualizações de software);

vi. Medidas de manutenção que fornecerão informações sobre os níveis de desempenho, eficácia e eficiência, incluindo acesso a falhas e histórico de falhas;

Direitos acordados sobre os dados e o seu impacto no sistema durante a atividade de resolução de problemas e de manutenção;

viii. Abordagem para garantir que elementos falsos ou não autorizados não sejam introduzidos no sistema;

O impacto de alterações de manutenção em outros elementos de sistemas de software versus o risco de deixar uma anomalia de software relatada sem tratamento; e

x. Os níveis pessoal e de habilidade requeridos para efetuar reparos ou substituições de sistemas ou softwares, correções, patches, atualizações e evoluções, considerando os requisitos legais e regulatórios relativos à saúde e proteção,

- 2) Para elementos que não são software, definir uma estratégia de logística ao longo do ciclo de vida, incluindo considerações de aquisição e de operação; o número e o tipo de elementos de reposição a serem armazenados, seus locais e condições de armazenamento, sua taxa de substituição prevista, e sua validade e frequência de renovação.
NOTA As implicações de suporte são consideradas desde cedo durante as fases de exploração ou desenvolvimento de conceitos. A logística ajuda a garantir que o material e os recursos necessários, na quantidade e qualidade corretas, estejam disponíveis no local e na hora certos, durante as fases de implantação e sustentação.

- 3) Identificar restrições relativas à manutenção a serem incorporadas aos requisitos, arquitetura ou design do sistema/software.
NOTA Isto geralmente resulta da necessidade de 1) reutilizar os sistemas habilitadores existentes para manutenção e verificação; 2) reutilizar os estoques existentes de elementos de sistema substituíveis e adequar limitações de reabastecimento; 3) realizar manutenção em locais ou ambientes específicos. Por exemplo, arquitetura e design de software que enfatizam encapsulamento, modularidade e escalabilidade podem ser mais simples de manter. Os requisitos para documentar o design e a construção do sistema podem reduzir o esforço necessário para fazer a engenharia reversa de sistemas e elementos quando é necessária uma manutenção. A arquitetura e o design do sistema refletem a necessidade de rollback, backup e recuperação de dados durante a resolução de um problema. Funções para tornar o sistema disponível para diagnóstico e manutenção remotos podem ser incorporadas à arquitetura e ao design.

  - 4) Identificar aspectos a serem considerados de modo que o sistema e as ações de manutenção e logística associadas resultem em uma solução economicamente viável, operável, sustentável e que se possa dar suporte.
NOTA Os processos de Análise de Sistema e Gerenciamento de Decisão são usados para executar as avaliações e decisões sobre estes aspectos.

  - 5) Identificar e planejar os sistemas ou serviços habilitadores necessários para apoiar a manutenção.
NOTA Isto inclui a identificação de requisitos e interfaces para os sistemas habilitadores. A seleção de sistemas habilitadores para manutenção geralmente reflete a necessidade de reutilizar a infraestrutura de gerenciamento de design, desenvolvimento e configuração existente ou equivalente, como durante a implementação inicial do sistema.

  - 6) Obter ou adquirir acesso aos sistemas ou serviços habilitadores.
NOTA O Processo de Validação é usado para confirmar objetivamente que o sistema habilitador de manutenção atende ao uso pretendido para as suas funções de habilitação.

- b) Executar manutenção. Esta atividade consiste nas seguintes tarefas:
  - 1) Analisar criticamente os requisitos e reclamações dos stakeholders, eventos, relatórios de incidentes e problemas, com o objetivo de identificar as necessidades de manutenção corretiva, adaptativa, de melhoria e preventiva.
NOTA Para sistemas de software com ciclos de vida iterativos, as mudanças de requisitos podem ser consideradas a fonte para atividades de manutenção adaptativa e de melhoria. Para manutenção de software, este processo faz correções, alterações e melhorias no software implantado, bem como aplicação de patches e atualizações para manter a segurança do sistema.

  - 2) Analisar o impacto das alterações de manutenção nos dados e suas estruturas, funções de software, documentação do usuário e interfaces relacionadas.
NOTA As revisões e análises geralmente incluem fatores como: a categoria da ação de manutenção; tamanho da modificação; custo envolvido; tempo para modificação; e impactos no desempenho, segurança ou proteção.

  - 3) Restaurar o sistema ao status operacional ao encontrar defeitos inesperados que causem uma falha no sistema de software.
A restauração do status operacional pleno ou reduzido geralmente pode ser realizada por meio de um roliback, solução de contorno ou identificação e correção da causa da falha. Se a restauração completa atrasar ou não for possível, o sistema deverá ser restaurado para um modo reduzido, consistente com o plano de contingência. Se possível, a falha é replicada usando outro ambiente semelhante ao ambiente operacional para identificação das causas-raiz da falha. O Processo de Gerenciamento de Configuração, especialmente as atividades de gerenciamento de versão, é executado para controlar alterações agendadas e emergenciais no sistema.

  - 4) Implementar os procedimentos para correção de falhas (defeitos) e erros, ou para substituição ou atualização de elementos do sistema.
NOTA 1 A correção de falhas e erros utiliza a resolução de problemas e pode ser tratada por meio dos processos de Garantia da Qualidade e de Avaliação e Controle de Projeto.

Normalmente, testes de regressão são executados para verificar se a mudança resultante da manutenção não introduziu outros problemas, isto é, a implementação completa e correta dos requisitos novos e modificados, sem afetar o desempenho dos requisitos originais não modificados. O Processo de Transição pode ser aplicado para a implantação das principais mudanças de manutenção; pequenas correções geralmente são tratadas como parte do Processo de Manutenção. As ações são registradas para facilitar a manutenção futura e a resolução de problemas e para análises logísticas de elementos degradáveis do sistema.

NOTA 3 Os procedimentos de recuperação de dados e do sistema e as informações de manutenção geralmente são disponibilizados na mídia que é utilizável no momento da execução da manutenção.

  - 5) Realizar manutenção preventiva, substituindo, corrigindo, aumentando ou atualizando elementos do sistema de software, para melhorar o seu desempenho, de forma que não atinja níveis de serviço inaceitáveis, como, por exemplo, a falta de capacidade devido a aumentos na demanda ou nos dados armazenados, ou para evitar condições operacionais inaceitáveis, como, por exemplo, uma execução com software de segurança desatualizado.
  - 6) Identificar quando é necessária uma manutenção adaptativa ou de melhoria.
Ações de manutenção adaptativas e de melhoria geralmente envolvem alterações nos requisitos de sistema/software, arquitetura e design. Um novo projeto pode ser iniciado para modificar o sistema de software existente.

- c) Executar apoio logistico. Esta atividade consiste nas seguintes tarefas:
NOTA As ações de logística permitem que o sistema de software mantenha a prontidão operacional. As ações incluem provisões para pessoal, abastecimento de suprimentos, equipamento de suporte, necessidades de dados técnicos (documentação do usuário) e acordos sobre direitos de dados, suporte a treinamento, comunicações, suporte a recursos/equipamentos de computação e instalações.

  - 1) Obter recursos para dar suporte ao sistema de software durante o seu ciclo de vida ou da vida do projeto (logística de aquisição).
As considerações sobre Logística de Aquisição são incluídas no acordo resultante dos processos de Acordo. Isto inclui a realização de análises para identificar alterações com custo-benefício favorável no design inicial do sistema para permitir o suporte e a facilidade de manutenção, além de planejamento para distribuir correções e atualizações de software durante a utilização/implantação. Estas decisões geralmente são limitadas pelos requisitos de disponibilidade e impactam o gerenciamento da cadeia de suprimentos.

  - 2) Monitorar a qualidade e a disponibilidade dos elementos de substituição e dos sistemas habilitadores, seus mecanismos de entrega e sua integridade contínua durante o armazenamento.
A logística operacional envolve o ajuste simultâneo dos sistemas de interesse e dos sistemas habilitadores ao longo da vida operacional para ajudar a garantir a entrega eficaz e eficiente das funções do software. Isto também inclui disponibilidade de recursos qualificados. Por exemplo, sistemas habilitadores confiáveis estão disponíveis com a capacidade de ler o software armazenado em formatos de mídia anteriores ou migrar arquivos de backup para a mídia e os sistemas habilitadores

  - 3) Implementar mecanismos para a distribuição do sistema ou elemento de software, incluindo empacotamento, manuseio, armazenamento e comunicação ou transporte necessários para os itens durante o ciclo de vida.
NOTA 1 A distribuição e a instalação do software geralmente são automatizadas. Os pacotes de software geralmente incluem termos de licença de software, direitos de dados e elementos para gestão

de ativos de software. O planejamento de logística para outros elementos do sistema é frequentemente necessário para apoiar os objetivos dos processos de Integração e de Transição.

NOTA 2 Considerar a necessidade de armazenar elementos sobressalentes ou cópias de backup do software no local ou em locais adicionais, para manter os recursos do sistema de software, conforme necessário (talvez em um nível reduzido para operações de contingência).

  - 4) Confirmar que as ações de logística para atender aos requisitos de capacidade de suporte ao sistema ou elemento de software, ou para alcançar a prontidão operacional, são planejadas e implementadas.
NOTA Estas ações de logística podem incluir equipe, suporte ao fornecimento, equipamento de suporte, necessidade de dados técnicos (documentação do usuário, instruções, listas), treinamento de suporte, comunicações, suporte para equipamentos/recursos computacionais e instalações.

- d) Gerenciar resultados de manutenção e logística. Esta atividade consiste nas seguintes tarefas:
  - 1) Registrar incidentes e problemas, incluindo suas resoluções, e resultados significativos de manutenção e logística.
NOTA Isto inclui anomalias devido à estratégia de manutenção, sistemas habilitadores de manutenção, execução da manutenção e logistica, ou definição incorreta do sistema. Os processos de Avaliação e Controle de Projeto e Garantia da Qualidade são usados para executar a identificação e resolução de problemas de manutenção, por exemplo, analisar os dados para identificar a causa-raiz, permitir ações corretivas ou de melhoria e registrar as lições aprendidas. Esta atividade pode incluir alterações nos procedimentos de logística ou distribuição de software. Alterações nos requisitos, na arquitetura ou no design do sistema de software são executadas em outros Processos Técnicos.

  - 2) Identificar e registrar tendências de incidentes, problemas e ações de manutenção e logistica.
NOTA 1 Os dados de tendência e os relatórios de resolução de problemas são usados para informar as equipes de operação e de manutenção, clientes e outros stakeholders e projetos que estão criando ou usando entidades similares do sistema.

NOTA 2 O relato de incidentes e problemas, incluindo as ações resultantes tomadas, é rastreado por meio da atividade de gerenciamento de processos e incidentes do processo de Garantia da Qualidade.

  - 3) Manter rastreabilidade dos elementos do sistema que estão sendo mantidos.
NOTA A rastreabilidade bidirecional é mantida entre as ações de manutenção registradas, os elementos do sistema de software e artefatos do ciclo de vida. São registradas alterações na gestão de ativos de software como, por exemplo, atribuição de licenças de software, a sistemas de substituição

  - 4) Fornecer os artefatos-chave e itens de informação que foram selecionados para as baselines.
NOTA O Processo de Gerenciamento de Configuração é usado para estabelecer e manter itens de configuração e baselines, e rastrear licenças e direitos de dados. Este processo identifica candidatos para a baseline e o Processo de Gerenciamento da Informação controla os itens de informações, como procedimentos de manutenção.

  - 5) Monitorar e medir a satisfação do cliente com o suporte ao sistema e à manutenção.
NOTA A ABNT NBR ISO 10004:2013 contém diretrizes para monitorar e medir a satisfação do cliente. Quando os dados de satisfação do cliente são coletados, estes são usados no Processo de Gestão da Qualidade.


### 6.4.14 Processo de Desativação


#### 6.4.14.1 Propósito

O propósito do Processo de Desativação é encerrar a existência de um elemento ou sistema para um uso pretendido especificado, tratar adequadamente elementos substituídos ou desativados e atender as necessidades críticas de desativação identificadas (por exemplo, por um acordo, por política organizacional, ou por aspectos ambientais, legais, de segurança e de proteção).

Este processo desativa, desmonta e remove o sistema ou qualquer um de seus elementos do uso específico. Ele trata quaisquer produtos que não são mais necessários, remetendo-os a uma condição final e devolvendo o ambiente à sua condição original ou aceitável. Estes produtos podem estar sendo processados durante qualquer estágio do ciclo de vida, por exemplo, resíduos de materiais durante uma fabricação. Este processo armazena, destrói ou recupera elementos do sistema e produtos residuais de maneira ambientalmente correta, de acordo com a legislação, acordos, restrições organizacionais e requisitos dos stakeholders. A desativação inclui evitar que elementos expirados, não reutilizáveis ou inadequados retornem à cadeia de suprimentos. Onde necessário, mantém registros para que a saúde dos operadores e usuários e a segurança do meio ambiente possam ser monitoradas. Quando parte do sistema continuar sendo usada de forma modificada, o Processo de Desativação ajuda a garantir o manuseio adequado da parte que está sendo desativada.

A desativação de sistemas de software abrange o término de serviços e a desativação de elementos de software, dados armazenados, mídia e firmware, itens de informação e elementos de hardware associados que não serão reutilizados ou transferidos para outro sistema. O Processo de Desativação destina-se a ser aplicável em qualquer fase do ciclo de vida de um sistema de software. Para software, o Processo de Desativação é aplicado, durante o ciclo de vida, ao código fonte ou cópias executáveis do software, dados pessoais identificáveis ou controlados usados no sistema de software, e itens de informação associados, retidos sob controle de configuração centralizado ou distribuídos para uso, por exemplo, desativação de protótipos nas fases iniciais do ciclo de vida e elementos descartáveis substituídos devido a modificações durante as fases de implantação, utilização e suporte. Quando o sistema de interesse está sendo modificado para atualizações tecnológicas ou de capacidade, apenas os elementos impactados são desativados e removidos.

NOTA O Processo de Análise de Negócio e o Processo de Gerenciamento de Decisão geralmente são aplicados para tratar o impacto da desativação e potenciais novas capacidades do sistema para os stakeholders.


#### 6.4.14.2 Resultados esperados

Como resultado da implementação bem-sucedida do Processo de Desativação:

- a) As restrições de desativação são fornecidas como entradas para requisitos, arquitetura, design e implementação.
- b) Todos os sistemas ou serviços habilitadores necessários para a desativação são disponibilizados.
- c) Os elementos do sistema ou produtos residuais são armazenados, recuperados, reciclados ou destruídos de acordo com os requisitos, como, por exemplo, requisitos de segurança e proteção.
- a) O ambiente é retornado ao seu estado original ou um estado previamente acordado.
- e) Os registros de ações e análises de desativação são disponibilizados.

#### 6.4.14.3 Atividades e tarefas

O projeto deve implementar as seguintes atividades e tarefas de acordo com as políticas e procedimentos da organização aplicáveis, relativos ao Processo de Desativação.

- a) Preparar para a desativação. Esta atividade consiste nas seguintes tarefas:
  - 1) Definir uma estratégia de desativação para o sistema de software, para incluir cada elemento do sistema, e identificar e atender às necessidades críticas de desativação, incluindo as seguintes considerações:
- Desativação das funções do sistema e entrega de serviços de forma permanente, por exemplo, destruição física de dispositivos de armazenamento de dados ou transição dos elementos do sistema de software para reutilização futura de forma modificada ou adaptada;

Identificação da propriedade e responsabilidade pela retenção ou destruição de dados e propriedade intelectual no sistema de software;

iii. Retenção do produto ou sua transformação para um estado social e fisicamente aceitável, evitando assim efeitos adversos subsequentes sobre os stakeholders, a sociedade e o meio ambiente;

iv. Preocupação com a saúde, proteção e privacidade aplicáveis às ações de desativação e às condições de longo prazo do material físico e informações resultantes;

V. Notificação aos stakeholders relevantes de atividades significativas de desativação, por exemplo, desativação ou substituição de um sistema, produtos ou serviços de software, cronograma de desativação ou alternativas de substituição; e

vi. Identificação de cronogramas, ações, responsabilidades e recursos para atividades de desativação.

  - 2) Identificar restrições e técnicas de implementação de desativação para os requisitos de sistema/software, caracteristicas de arquitetura e design.
NOTA Isto inclui acesso e disponibilidade de arquivos ou locais de armazenamento de longo prazo e recursos qualificados disponíveis para desativação do sistema e comunicação com os stakeho/ders e parceiros de intertace.

  - 3) Identificar e planejar os sistemas ou serviços habilitadores necessários para apoiar a desativação.
NOTA Isto inclui a identificação de requisitos e interfaces para os sistemas habilitadores.

  - 4) Obter ou adquirir acesso aos sistemas ou serviços habilitadores a serem utilizados.
NOTA O Processo de Validação é usado para confirmar objetivamente que o sistema habilitador para a desativação atende ao uso pretendido para as suas funções habilitadoras.

  - 5) Especificar, de acordo com as considerações ambientais e de segurança, as instalações e locais de armazenamento, os critérios de inspeção e os períodos de armazenamento, e se o sistema de software ou os dados devem ser armazenados.
  - 6) Definir métodos preventivos para impedir que elementos e materiais descartados que não podem ser reaproveitados, recuperados ou reutilizados entrem novamente na cadeia de suprimentos.
- b) Realizar a desativação. Esta atividade consiste nas seguintes tarefas:
  - 1) Desativar o sistema ou elemento de software para prepará-lo para remoção.
NOTA As interfaces com outros sistemas são consideradas de acordo com procedimentos ou instruções especiais, e restrições relevantes de saúde, segurança, proteção e privacidade.

  - 2) Remover o sistema de software, seus elementos, dados e material não reutilizável, do uso ou da produção, para desativação e ação apropriados.
A desativação inclui reutilização, reciclagem, recondicionamento, restauração ou destruição. A desativação e as ações subsequentes são conduzidas de acordo com padrões, diretrizes e leis relevantes de segurança, proteção, privacidade e meio ambiente. Os elementos do sistema de software que têm vida útil restante, em sua condição atual ou após a modificação, são transferidos para outros sistemas de interesse ou organizações. Onde apropriado, considerar recondicionar os elementos do sistema para prolongar a sua vida útil.

  - 3) Retirar a equipe impactada, responsável pela operação do sistema de software ou elemento do sistema, e registrar o conhecimento operacional relevante.
NOTA

de Conhecimento.

  - 4) Reutilizar, reciclar, recondicionar, restaurar, arquivar ou destruir os elementos designados do sistema de software.
NOTA Manusear os elementos do sistema e as suas partes que não se destinam à reutilização de maneira a garantir que eles não retornem à cadeia de suprimentos.

  - 5) Proceder à destruição dos elementos do sistema, conforme necessário, para reduzir a quantidade de tratamento de resíduos ou facilitar o manuseio dos resíduos.
NOTA Quando não for possível manter ou reciclar o elemento, é necessário impedir que ele retorne à cadeia de suprimentos, por exemplo, eliminação completa de todos os softwares de todas as mídias de armazenamento do sistema e remoção de chaves de licença, dados e interfaces. Esta atividade inclui a obtenção dos serviços de destruição para derreter, esmagar, incinerar, demolir ou erradicar o sistema ou seus elementos, conforme necessário.

- c) Finalizar a desativação. Esta atividade consiste nas seguintes tarefas:
  - 1) Confirmar se as condições prejudiciais à saúde, segurança, proteção e meio ambiente posteriores à desativação foram identificadas e tratadas.
  - 2) Retornar o ambiente ao seu estado original ou a um estado especificado em acordo.
  - 3) Arquivar as informações coletadas durante a vida útil do produto para permitir auditorias e análises críticas em caso de riscos de longo prazo para saúde, segurança e meio ambiente, além de permitir que futuros criadores e usuários de sistemas de software construam uma base de conhecimento a partir da experiência.

## Anexo A (normativo) — Processo de Adaptação


### A.1 Introdução

Este Anexo fornece requisitos para a adaptação deste documento.

não é permitida quando se reivindica a 'conformidade total'. Se for reivindicada a 'conformidade adaptada', NOTA 1 A adaptação não é um requisito para a conformidade com este documento. De fato, a adaptação

então uma adaptação é executada aplicando este processo.

NOTA 2 Na ISO/IEC/IEEE 24748 (todas as partes) podem ser encontradas orientações para a adaptação dos processos do ciclo de vida.


### A.2 Processo de Adaptação


#### A.2.1 Propósito

O propósito do Processo de Adaptação é adaptar os processos deste documento para satisfazer circunstâncias ou fatores particulares como:

- a) o contexto de uma organização que está utilizando este documento em um acordo;
- b) as influências que afetam um projeto que necessita atender a um acordo no qual este documento e referenciado;
- c) os que refletem as necessidades da organização para fornecer produtos ou serviços.

#### A.2.2 Resultados esperados

Como resultado da implementação bem-sucedida do Processo de Adaptação:

- a) As modificações ou os novos processos do ciclo de vida para atender aos propósitos e aos resultados de um modelo de ciclo de vida são definido.

#### A.2.3 Atividades e tarefas

Se este documento for adaptado, então a organização ou projeto deve implementar as seguintes tarefas de acordo com as políticas e procedimentos aplicáveis relativos ao Processo de Adaptação.

- a) Identificar e documentar as circunstâncias que influenciam a adaptação. Estas influências incluem, mas não se limitam a:
  - 1) estabilidade e variedade dos ambientes operacionais;
  - 2) riscos comerciais ou de desempenho que preocupam os stakeholders;
  - 3) inovações, tamanho e complexidade;
  - 4) data de início e duração da utilização;
  - 5) questões relacionadas à integridade, como: proteção, segurança, usabilidade e disponibilidade;
  - 6) oportunidades de tecnologias emergentes;
  - 7) perfis dos recursos organizacionais e do orçamento disponíveis;
  - 8) disponibilidade dos serviços dos sistemas habilitadores;
  - 9) papéis, responsabilidades, autoridades e responsabilizações no ciclo de vida do sistema como um todo; e
  - 10) a necessidade de conformidade com outras normas.
- b) No caso de propriedades críticas para o sistema, levar em conta as estruturas de ciclo de vida recomendadas ou mandatórias pelas normas relevantes para o nível de criticidade.
- c) Obter informações de todas as partes afetadas pelas decisões de adaptação. Isto inclui, mas pode não ser limitado a:
  - 1) stakeholders do sistema;
  - 2) partes interessadas em um acordo feito pela organização; e
  - 3) funções organizacionais que contribuem.
- d) Tomar decisões de adaptação de acordo com o Processo de Gerenciamento de Decisão para atingir os propósitos e resultados do modelo de ciclo de vida selecionado.
NOTA 1 Organizações estabelecem modelos de ciclo de vida padrão como parte do Processo de Gerenciamento de Modelo de Ciclo de Vida. Pode ser apropriado para uma organização adaptar os processos deste documento para atingir os propósitos e resultados das fases de um modelo de ciclo de vida a ser estabelecido.

NOTA 2 Os projetos selecionam um modelo de ciclo de vida, estabelecidos organizacionalmente para o projeto como parte do Processo de Planejamento de Projeto. Muitas vezes é apropriado adaptar processos adotados organizacionalmente para atingir os propósitos e resultados esperados das fases do modelo de ciclo de vida selecionado.

NOTA 3 Em casos em que os projetos estão aplicando diretamente este documento, muitas vezes é apropriado adaptar os processos deste documento para atingir os propósitos e resultados esperados das fases de um modelo de ciclo de vida adequado.

- e) Selecionar os processos de ciclo de vida que requerem adaptação e exclusão de resultados esperados, atividades ou tarefas.
NOTA 1 Independentemente da adaptação, organizações e projetos sempre podem implementar processos que alcançam resultados esperados adicionais e implementam atividades e tarefas adicionais, além daquelas requeridas para a conformidade com este documento.

NOTA 2 Uma organização ou projeto muitas vezes pode encontrar uma situação na qual existe a necessidade de modificar uma disposição deste documento. A modificação é evitada, porque pode ter consequências não previstas para outros processos, resultados esperados, atividades ou tarefas. Se necessário, a modificação é realizada excluindo-se a disposição (fazendo-se a reivindicação apropriada de conformidade adaptada) e, com uma consideração cuidadosa das consequências, implementando um processo que alcance os resultados esperados adicionais ou realize atividades e tarefas, alem daquelas previstas neste documento adaptado.


## Anexo B (informativo) — Exemplos de itens de informação de processo

A Tabela B. 1 fornece um conjunto possível de produtos de trabalho, incluindo artefatos, registros, itens de informação e armazenamento de dados associados a cada processo. Esta lista não é abrangente: para cada processo, uma organização pode decidir desenvolver uma politica, planos, procedimentos, relatórios e registros, para demonstrar os resultados esperados ou executar atividades e tarefas. Onde a documentação menos intensiva é considerada suficiente, os itens de informação podem ser combinados. Além disso, as politicas e procedimentos organizacionais podem ser aplicados ou adaptados para cada processo e projeto. Titulos de itens típicos são mostrados, incluindo exemplos comuns de títulos alternativos entre parênteses.

NOTA Ver a ISO/IEC/IEEE 15289 para orientações sobre conteúdo e gerenciamento de Itens de Informação.

Artefatos, registros, armazenamentos de registros e itens de informações geralmente são iniciados em um processo e revisados, aprimorados ou concluídos em outros processos. Por conveniência, eles são listados uma vez nesta tabela, no processo em que geralmente são iniciados. Quando os artefatos e as informações do sistema de software são transformados ou elaborados por outro processo, a rastreabilidade é mantida e um mapeamento da rastreabilidade pode ser produzido. Por exemplo, a rastreabilidade pode ser mantida entre os processos organizacionais e do projeto e entre requisitos, elementos de arquitetura e de design e casos de verificação.


**Tabela B.1 - Amostras de itens de informação por processo**

| Grupo de Processo | Processo | Títulos típicos do item | Tipo do Item |
|---|---|---|---|
| Processos de Acordo |  |  |  |
|  | Processo de Aquisição |  |  |
|  |  | Plano de Aquisição | Informação |
|  |  | Solicitação de Fornecimento (p.ex. Solicitação de Proposta, Edital | Informação |
|  |  | de Licitação) |  |
|  |  | Solicitação de Mudança de Acordo | Informação |
|  |  | Acordo (p. ex. Contrato) | Informação |
|  |  | Procedimento para Gerenciamento de Mudança de Acordo | Informação |
|  |  | Relatório de Aceitação de Entrega | Informação |
|  | Processo de Fornecimento |  |  |
|  |  | Resposta de Fornecimento (p.ex. Proposta) | Informação |
|  |  | Solicitação de Mudança de Acordo | Informação |
|  |  | Procedimento para Gerenciamento de Mudança de Acordo | Informação |
|  |  | Registros de Entrega de Fornecimento (para sistema, software, | Registro |
|  |  | produto ou serviço) |  |
| Processos Organizacionais Habilitadores de Projeto |  |  |  |
|  | Processo de Gerenciamento do Modelo de Ciclo de Vida |  |  |
|  |  | Políticas Organizacionais | Informação |
|  |  | Processos do Ciclo de Vida | Artefato |
|  |  | Descrição dos Processos do Ciclo de Vida | Informação |
|  |  | Modelo do Ciclo de Vida | Artefato |
|  |  | Procedimentos Organizacionais (Procedimento de Gerenciamento | Informação |
|  |  | de Processo) |  |
|  |  | Relatório de Avaliação de Processo | Informação |
|  |  | Plano de Melhoria de Processo | Informação |
|  |  | Relatório de Melhoria de Processo | Informação |
|  | Processo de Gerenciamento de Infraestrutura |  |  |
|  |  | Requisitos de Infraestrutura | Artefato |
|  |  | Elementos de Infraestrutura | Artefato |
|  |  | Descrição de Infraestrutura | Informação |
|  |  | Solicitação de Mudança de Infraestrutura | Informação |
|  | Processo de Gerenciamento de Portfólio |  |  |
|  |  | Portfólio de Projetos | armazenamento |
|  |  | Orçamento de Projeto | Artefato |
|  |  | Autorização de Projeto | Informação |
|  | Processo de Gerenciamento de Recursos Humanos |  |  |
|  |  | Relatório de Necessidades de Perfis | Informação |
|  |  | Ativos de Desenvolvimento de Perfis (Material de Treinamento) | Artefato |
|  |  | Registros de Desenvolvimento de Perfis (Inventário de Perfis, | Registro |
|  |  | Registros de Treinamento) |  |
|  |  | Pessoal Qualificado | Artefato |
|  |  | Registros de Designação de Equipe | Registro |
|  | Processo de Gestão da Qualidade |  |  |
|  |  | Plano de Gestão da Qualidade (Políticas, Objetivos) | Informação |
|  |  | Procedimentos de gestão da Qualidade | Informação |
|  |  | Resultados de Avaliação de Garantia da Qualidade | Registro |
|  |  | Relatório de Ações Corretivas e Preventivas (Relatório de | Informação |
|  |  | Gerenciamento de Problema) |  |
|  | Processo de Gerenciamento do Conhecimento |  |  |
|  |  | Plano de Gerenciamento do Conhecimento | Informação |
|  |  | Procedimentos de Gerenciamento do Conhecimento | Informação |
|  |  | Registros de Ativos de Conhecimento | Registro |
|  |  | Ativos de Conhecimento | Artefato |
| Processos de Gerenciamento Técnico |  |  |  |
|  | Processo de Planejamento de Projeto |  |  |
|  |  | Plano de Projeto (por exemplo, Plano de Gerenciamento do |  |
|  |  | Projeto Técnico, Plano de Gerenciamento de Engenharia de Sistemas ou Software, Plano de Desenvolvimento de Software, | Informação |
|  |  | Plano de Transição) |  |
|  |  | Estrutura Analítica de Projeto (EAP) | Artefato |
|  |  | Solicitação de Recurso | informação |
|  |  | Cronograma do Projeto | Artefato |
|  |  | Requisitos de Infraestrutura e Serviços de Projeto | Artefato |
|  | Processo de Avaliação e Controle do Projeto |  |  |
|  |  | Resultados de Análise de Medições e Recomendações | informação |
|  |  | Relatório de Avaliação de Projeto | informação |
|  |  | Atas de Reunião | informação |
|  |  | Autorização para prosseguir para o Próximo Marco | informação |
|  | Processo de Gerenciamento da Decisão |  |  |
|  |  | Solicitação de Decisão | informação |
|  |  | Registro de Decisão | registro |
|  | Processo de Gestão de Riscos |  |  |
|  |  | Plano de Gestão de Riscos | informação |
|  |  | Perfil de Riscos | registro |
|  |  | Solicitação de Ação de Riscos | informação |
|  | Processo de Gerenciamento de Configuração |  |  |
|  |  | Plano de Gerenciamento da Configuração | informação |
|  |  | Procedimentos de Gerenciamento da Configuração | informação |
|  |  | Registro de Gerenciamento da Configuração | registro |
|  |  | Configuração da baseline | artefato |
|  |  | Mudança na GC / Solicitação de Alteração | informação |
|  |  | Relatório de Status de Configuração | informação |
|  |  | Relatório de Avaliação da Configuração | informação |
|  |  | Relatório de Liberação de Sistema/Software | informação |
|  | Processo de Gerenciamento da Informação |  |  |
|  |  | Arquivo de Item de Informação | armazenamento |
|  |  | Procedimento de Gerenciamento da Informação | informação |
|  |  | Relatório de Gerenciamento da Informação | informação |
|  | Processo de Medição |  |  |
|  |  | Registro de Medição | registro |
|  |  | Procedimento de Medição | informação |
|  |  | Relatório de Necessidades de Informações de Medição | informação |
|  |  | Relatório de Medições | informação |
|  | Processo de Garantia da Qualidade |  |  |
|  |  | Procedimento de Garantia da Qualidade | intormação |
|  |  | Relatório de Avaliação de Garantia da Qualidade | informação |
|  |  | Registro de Garantia da Qualidade | registro |
|  |  | Registro de Incidente | registro |
|  |  | Registro de Problema | registro |
| Processos Técnicos |  |  |  |
|  | Processo de Análise do Negócio |  |  |
|  |  | Conceito Preliminar de Ciclo de Vida | artefato |
|  |  | Relatório de Avaliação de Alternativas de Solução | informação |
|  | Processo de Definição de Necessidades e Requisitos dos Stakeho/ders |  |  |
|  |  | Conceito Operacional | artefato |
|  |  | Avaliação de Necessidades dos Stakeholders | informação |
|  |  | Requisitos dos Stakeholders | artefato |
|  |  | Especificação de Requisitos dos Stakeholders | informação |
|  |  | Relatório de Requisitos dos Stakeholders | informação |
|  |  | Medições Criticas de Desempenho | artefato |
|  | Processo de Definição de Requisitos de Sistema/Software |  |  |
|  |  | Descrição de Sistema ou Elemento | informação |
|  |  | Requisitos de Sistema/Software | artefato |
|  |  | Especificação de Requisitos de Sistema/Software | informação |
|  |  | Solicitação de Mudança de Requisitos | informação |
|  | Processo de Definição de Arquitetura |  |  |
|  |  | Pontos de Vista da Arquitetura | artefato |
|  |  | Visões e Modelos de Arquitetura (Descrição da Arquitetura) | artefato |
|  |  | Definição de Interface (inicial) | artefato |
|  | Processo de Definição de Design |  |  |
|  |  | Artefato de Design | artefato |
|  |  | Relatório de Artefatos de Design (Descrição de Design) | informação |
|  |  | Especificação de Interface | informação |
|  | Processo de Análise de Sistema |  |  |
|  |  | Relatório de Análise de Sistemas | informação |
|  | Processo de Implementação |  |  |
|  |  | Elemento de Sistema e Software | artefato |
|  |  | Procedimentos de Implementação | informação |
|  |  | Registros de Implementação (resultado de testes unitários) | registro |
|  | Processo de Integração |  |  |
|  |  | Descrição da Interface de Controle | informação |
|  |  | Integração e Procedimentos de Teste | informação |
|  |  | Elementos de Sistema e Software Integrados (biblioteca de | artefato |
|  |  | software) |  |
|  |  | Registros de Integração | registro |
|  | Processo de Verificação |  |  |
|  |  | Sistema Verificado | artefato |
|  |  | Procedimento de Verificação | informação |
|  |  | Registros de Verificação | registro |
|  |  | Relatório de Verificação | informação |
|  | Processo de Transição |  |  |
|  |  | Site preparado para operação | artefato |
|  |  | Sistema/Software com transição realizada | artefato |
|  |  | Registros de Transição | registro |
|  | Processo de Validação |  |  |
|  |  | Sistema Validado | artefato |
|  |  | Procedimentos de Validação | informação |
|  |  | Registros de Validação | registro |
|  |  | Relatório de Validação | informação |
|  | Processo de Operação |  |  |
|  |  | Plano de Continuidade | informação |
|  |  | Procedimentos Operacionais (Documentação de Usuário) | informação |
|  |  | Registros de Operação | registro |
|  |  | Relatório de Problema | informação |
|  |  | Solicitação de Suporte ao Consumidor | informação |
|  |  | Registros de Suporte ao Consumidor | registro |
|  |  | Relatório de Operação | informação |
|  | Processo de Manutenção |  |  |
|  |  | Elemento de Reposição do Sistema | artefato |
|  |  | Procedimentos de Manutenção (Procedimentos de Logística) | informação |
|  |  | Registros de Manutenção (Logística) | registro |
|  |  | Solicitação de Manutenção | registro |
|  |  | Relatório de Manutenção (Logística) | informação |
|  | Processo de Desativação |  |  |
|  |  | Registro de Desativação | registro |
|  |  | Relatório de Arquivamento | informação |



## Anexo C (informativo) — Modelo de Referência de Processo (MRP) para Fins de Avaliação


### C.1 Introdução

Alguns usuários deste documento podem querer avaliar os processos implementados de acordo com a série ISO/IEC 33000 para avaliação de processo. Este Anexo fornece um Modelo de Referência de Processo (MRP) adequado para uso em conjunto com aquelas normas.

O MRP é composto pelos processos no corpo deste documento, incluindo o nome, a declaração do propósito e os resultados esperados de cada processo. A subseção C3 identifica os processos no modelo de referência de processo e as seções nas quais eles são definidos.


### C.2 Conformidade com a ISO/IEC 33004


#### C.2.1 Geral

A ISO/IEC 33004, 5.3 estabelece requisitos para modelos de referência de processo adequados para a avaliação por esta norma. As seções a seguir citam os requisitos da ISO/IEC 33004 para os modelos de referência de processo e descrevem como eles são atendidos por este documento. Em cada uma das subseções a seguir, o texto em itálico cita o requisito da ISO/IEC 33004 e o texto não itálico (na vertical) descreve a forma como o requisito é satisfeito neste documento.


#### C.2.2 Requisitos para os Modelos de Referência de Processo

Um Modelo de Referência de Processo deve conter: [ISO/IEC 33020, 5.3.1]

- a) Uma declaração do domínio do Modelo de Referência do Processo. Isto é fornecido na Seção 1.
- b) Uma descrição do relacionamento entre o Modelo de Referência do Processo e seu contexto de uso pretendido. Isto é fornecido na Seção 5.
- c) Descrições, atendendo aos requisitos da [ISO/IEC 33004, 5.4], dos processos dentro do escopo do Modelo de Referência de Processo. Isto é fornecido na Seção 6 na descrição de cada processo.
- d) Uma descrição do relacionamento entre o Modelo de Referência de Processo e o contexto pretendido de uso. Isto é fornecido em 5.6.
O Modelo de Referência de Processo deve documentar a comunidade de interesse do modelo e as ações tomadas para se chegar a um consenso dentro desta comunidade de interesse: [ISO/IEC 33020, 5.3.2]

- a) A comunidade relevante de interesse deve ser caracterizada ou especificada. A comunidade relevante de interesse são os usuários das ABNT ISO/IEC 15288 e ABNT NBR ISO/IEC 12207.
- b) A extensão de alcance do consenso deve ser documentada. Tanto a ABNT NBR ISO/IEC 15288 quanto a ABNT NBR ISO/IEC 12207 são normas que satisfazem os requisitos de consenso da ISO/IEC e IEEE (Não aplicável).
- c) Se nenhuma ação for tomada para chegar ao consenso, uma declaração deste efeito deve ser documentada (Não aplicável).
Os processos definidos dentro de um Modelo de Referência de Processo devem possuir descrições e identificação de processo específicas [ISO/IEC 33020, 5.3.3]. As descrições do processo são específicas. A identificação é fornecida por nomes específicos e pelo número de seção deste Anexo.


#### C.2.3 Descrições de Processo

Os elementos fundamentais de um Modelo de Referência de Processo são as descrições dos processos dentro do escopo do modelo.

As descrições de processo no Modelo de Referência de Processo incorporam uma declaração do propósito do processo que descreve, em nível alto, os objetivos gerais da execução do processo, juntamente com um conjunto de resultados esperados que demonstram que o propósito do processo foi alcançado com sucesso.

A descrição do processo deve satisfazer os seguintes requisitos:

- a) um processo deve ser descrito em termos de seu propósito e resultados esperados;
- b) o conjunto de resultados esperados deve ser necessário e suficiente para atender ao propósito do processo; e
- c) as descrições de processo não podem conter ou implicar em aspectos da característica de qualidade do processo além do nível básico de qualquer framework de medição de processo relevante em conformidade com a ISO/IEC 33003.
Os resultados esperados do processo descrevem um dos seguintes: [ISO/IEC 30004:2015, 5.4]

- a) produção de um artefato;
- b) uma mudança significativa no estado; e
- c) atendimento a restrições específicas, por exemplo, requisitos, metas etc.
Estes requisitos são atendidos pelas descrições do processo na Seção 6 deste documento. Alguns resultados esperados podem ser interpretados como contribuintes para níveis de capacidade acima do nível 1 (básico) em alguns frameworks relevantes de medição de processo. Entretanto, uma implementação adequada dos processos relevantes não requer o atingimento destes níveis mais altos de capacidade.


### C.3 O Modelo de Referência de Processo

O Modelo de Referência de Processo (MRP) é composto pela declaração do propósito e dos resultados esperados de cada um dos processos incluídos na Seção 6 deste documento. O MRP para o ciclo de vida do software é composto pelo conjunto de processos da Figura 4, mostrado anteriormente na Seção 5.6.1 deste documento.


## Anexo D (informativo) — Integração e construtos de processo


### D.1 Introdução

Um projeto de harmonização dentro da ISO/IEC JTC 1/SC 7 - uma revisão paralela coordenada das ISO/IEC/IEEE 15288 e ISO/IEC/IEEE 12207 e o desenvolvimento de orientações na ISO/IEC/IEEE 24748 (todas as partes), que fornece diretrizes para estes documentos - é o primeiro grande passo em direção a um conjunto integrado de padrões que descreve os ciclos de vida do sistema e do software. Os conceitos de melhoria contínua do processo e avaliação de capacidade estão agora bem estabelecidos e reconhecidos, e estão sendo padronizados na série ISO/IEC 33000 (substituindo a série ABNT NBR ISO/IEC 15504). Os Modelos de Referência de Processo da ISO/IEC/IEEE 15288:2015, Anexo C, e este documento destinam-se a ser usados em conjunto com a ISO/IEC 33020:2015, para avaliação da capacidade dos processos do ciclo de vida. A determinação da capacidade dos processos requer que as descrições do processo incluam uma declaração clara do propósito do processo e uma descrição dos resultados esperados. A implementação consistente dos processos é auxiliada pela definição de atividades, tarefas e notas de implementação. Assim, os processos do ciclo de vida em ambas as normas adotaram construtos comuns de processos, conforme definido em D.2, Construtos de processos e seu uso, e são consistentes com as diretrizes de definição de processo contidas na ISO/IEC/IEEE TR 24774.


### D.2 Construtos de processo e sua utilização

As descrições de processo neste documento seguem regras claramente definidas. Primeiramente, os processos foram agrupados de uma forma lógica. Estes grupos são ditados por:

- a) Relações lógicas entre os processos; e
- b) Responsabilidade pela execução do processo.
Este documento agrupa as atividades que podem ser realizadas durante o ciclo de vida do sistema em quatro Grupos de Processos. A descrição em alto nível destes grupos pode ser encontrada em 5.6. Cada processo do ciclo de vida nestes grupos é descrito em termos de seu propósito e resultados esperados e listas de atividades e tarefas que são necessárias para atingir aqueles resultados.

- c) Processos de Acordo - dois processos (6.1);
- d) Processos Organizacionais Habilitadores - seis processos (6.2);
- e) Processos de Gerenciamento Técnico - oito processos (6.3); e
- f) Processos Técnicos - 14 processos (6.4).
A aplicação consistente das regras de descrição do processo permite a numeração padronizada da seção. Neste documento, uma subseção numerada como 6.x indica um grupo de processos e 6.x.y

indica um processo dentro deste grupo. Subseções numeradas como 6.x.y. 1 descrevem o propósito de um processo, subseções numeradas como 6.x.y.2 descrevem os resultados esperados de um processo e subseções numeradas como 6.x.y.3 descrevem as atividades e tarefas de um processo.

e na ISO/IEC/IEEE 15288: 2015. Estes são Processo, Atividade, Tarefa e Nota. A Figura D.1 é uma representação dos construtos dos processos usados neste documento

Um processo requer um nome, propósito e pelo menos um resultado esperado. Cada processo possui pelo menos uma atividade. Um conjunto de processos, com suas declarações de propósito e resultados esperados, constitui um Modelo de Referência de Processo (MRP).

Uma atividade é um construto de tarefas relacionadas para produzir resultados esperados. As atividades fornecem um meio de organizar tarefas relacionadas dentro do processo, para melhorar a compreensão e a comunicação do processo. Se uma atividade for coesa o suficiente, ela pode ser convertida em um processo de nível inferior, elaborando um propósito e um conjunto de resultados esperados.

Uma tarefa é uma seção detalhada para implementação de um processo. Pode ser apresentada como um requisito ("deve"), uma recomendação ("convém que") ou uma permissão ("pode").

As notas são usadas para explicar a intenção ou a mecânica de um processo, atividade ou tarefa. As notas fornecem insights sobre possíveis implementações ou áreas de aplicabilidade, como listas, exemplos e outras considerações.

PROCESSO

Nome Propósito Resultados esperados

ATIVIDADE

Nome

TAREFA

O ...

NOTA


**Figura D.1 - ABNT NBR ISO/IEC/IEEE 12207:2021 e ISO/IEC/IEEE 15288:2015 - Construtos**

de processo


## Anexo E (informativo) — Visões de processo


### E.1 Introdução

Uma visão de processo permite que um conjunto de atividades que representam interesses específicos da engenharia seja reunido em um único local. Para tais interesses, uma visão de processo pode ser desenvolvida para organizar processos, atividades e tarefas selecionados da ISO/IEC/IEEE 15288 ou da ABNT NBR ISO/IEC/IEEE 12207 para fornecer um foco nas suas preocupações particulares de uma forma que se estenda por todo o ciclo de vida ou partes dele. Este Anexo fornece exemplos de pontos de vista do processo que podem ser usados para definir visões do processo nessas instâncias.


### E.2 Conceito de visão de processo

Pode haver casos em que é necessário um foco unificado para atividades e tarefas que são selecionadas a partir de processos discrepantes para dar visibilidade a um conceito ou tópico significativo que percorre os processos empregados ao longo do ciclo de vida. É útil aconselhar os usuários deste documento sobre como identificar e definir estas atividades para o seu uso, mesmo que não possam localizar um único processo que atenda às suas preocupações específicas.

Com este propósito, o conceito de visão de processo foi formulado. Como um processo, a descrição de uma visão de processo inclui uma declaração de propósito e resultados esperados. Ao contrário de um processo, a descrição de uma visão de processo não inclui atividades e tarefas. Em vez disso, a descrição inclui orientações explicando como os resultados esperados podem ser alcançados utilizando as atividades e tarefas dos vários processos das ISO/IEC/IEEE 15288 e ABNT NBR ISO/IEC/IEEE 12207. As visões de processo podem ser construídas usando o modelo de ponto de vista de processo encontrado em E.3.


### E.3 Ponto de vista de processo

Uma visão de processo está em conformidade com um ponto de vista de processo. O ponto de vista de processo fornecido aqui pode ser utilizado para criar visões de processo.

- a) O ponto de vista do processo é definido por:
  - 1) seus stakeholders: usuários deste documento; e
  - 2) as preocupações que ele apresenta: os processos necessários para refletir um interesse particular de engenharia.
- b) Convém que o conteúdo das visões de processo resultantes inclua:
  - 1) nome da visão de processo;
  - 2) propósito da visão de processo;
  - 3) resultados esperados da visão de processo; e
  - 4) identificação e descrição dos processos, atividades e tarefas que implementam a visão de processo e referências às fontes destes processos, atividades e tarefas em outras normas.
NOTA Os requisitos para documentação de pontos de vista são encontrados na ISO/IEC/IEEE 42010: 2011, 5.4. Esta descrição é consistente com estes requisitos.

NOTA BRASILEIRA A itemização na Seção E.3 foi alterada em relação ao documento original, substituindo os números 1) e 2) por letras a) e b), a fim de destacar claramente os itens e subitens.


### E.4 Visão de processo de engenharia especializada

Esta Seção fornece um exemplo de aplicação do ponto de vista do processo para gerar uma visão de processo para engenharia especializada, destinada a ilustrar como um projeto pode montar processos, atividades e tarefas deste documento para fornecer atenção focada no atendimento às características do produto que foram selecionadas como sendo de interesse especial.

Este exemplo trata o cluster de interesses, geralmente chamado de engenharia especializada, que inclui, mas não se limita a áreas como disponibilidade, manutenibilidade, confiabilidade, segurança, proteção, fatores humanos e usabilidade. Neste documento, estes requisitos de "ilidades" são referidos como "características críticas da qualidade". Estas características determinam até que ponto o produto atende aos requisitos especificados em uma área específica selecionada para foco. Ver E.6 para obter uma visão do processo relacionada (garantia de segurança da informação para sistemas de software).

NOTA 1 Esta é uma instância generalizada de uma visão de processo que abrange um amplo conjunto de características funcionais e não funcionais relacionadas à engenharia especializada. Ela fornece uma visão ampla dos processos. Se uma característica de qualidade específica crítica tiver alta prioridade em relação a outras características, uma visão de processo especifica pode ser criada para esta caracteristica, incluindo informações e requisitos mais detalhados.

NOTA 2 A ISO/IEC 25030, Systems and software engineering - Systems and software quality requirements and evaluation (SQuaRE) - Quality requirements framework, pode ser consultada na especificação de requisitos de qualidade do produto de software.

NOTA 3 O INCOSE Systems Engineering Handbook contém descrições e elaboração sobre muitas das áreas de engenharia especializadas e as características críticas de qualidade associadas.

Nome: Visão do Processo de Engenharia Especializada

Propósito: O propósito da Visão do Processo de Engenharia Especializada é fornecer evidências objetivas de que o sistema atinge níveis satisfatórios de certas características críticas de qualidade selecionadas para atenção especial.

Resultados esperados

- a) Características críticas da qualidade do produto são selecionadas para atenção especial.
- b) Requisitos para o atendimento das características críticas da qualidade são definidos.
- c) Medidas para os requisitos são selecionadas e relacionadas às características críticas de qualidade desejadas.
- d) Abordagens para atender às características críticas de qualidade desejadas são definidas e implementadas.
- e) A extensão do atendimento dos requisitos é monitorada continuamente.
- f) Um nível satisfatório das características críticas da qualidade é especificado e alcançado.
Os resultados permitem a possibilidade de que as características críticas da qualidade desejadas possam nao ser medidas diretamente, mas, em vez disso, podem ser discutidas e inferidas com base em outras características do produto ou processo que podem ser medidas. Medições podem ser utilizadas para mostrar conformidade com os padrões estabelecidos. O adquirente e o fornecedor chegam a um acordo sobre padrões específicos a serem utilizados para esta verificação de conformidade.

Processos, atividades e tarefas de engenharia especializada

Esta visão de processo pode ser implementada usando os seguintes processos, atividades e tarefas deste documento.

- a) O processo de Avaliação e Controle do Projeto (6.3.2) prevê o monitoramento da extensão do atendimento dos requisitos e características críticas da qualidade e a comunicação dos resultados aos stakeholders e aos gerentes. Atividades e tarefas relevantes incluem b) 6), 7),
  - 9) e 10).
- b) O Processo de Gerenciamento de Decisão (6.3.3) fornece avaliação de requisitos alternativos, características de arquitetura e características de design em relação aos critérios de decisão, incluindo as características críticas de qualidade. Os resultados dessas comparações são classificados, por meio de um modelo de seleção adequado, e depois são usados para decidir sobre uma solução ideal. Atividades e tarefas relevantes incluem b) todas as tarefas; e c) 1).
- c) O Processo de Gestão de Riscos (6.3.4), na íntegra, prevê a identificação, avaliação e tratamento de riscos do sistema, incluindo aqueles relacionados ao atendimento das características críticas da qualidade.
- d) O Processo de Gerenciamento da Informação (6.3.6), na integra, fornece a especificação, desenvolvimento e manutenção de itens de informação para documentar e comunicar a extensão do atendimento. Os itens de informação usados para fins de características críticas de qualidade são, por vezes, especializados por natureza. As fontes para a descrição destes itens de informação incluem associações, reguladores e padrões específicos da indústria.
- e) O Processo de Medição (6.3.7), em sua totalidade, define uma abordagem que relaciona medidas com as características críticas de qualidade requeridas.
- f) O Processo de Garantia da Qualidade (6.3.8) trata de anomalias identificadas (incidentes e problemas) relacionadas ao atendimento de características críticas da qualidade.
- g) O Processo de Análise de Negócio (6.4.1) fornece a definição do espaço do problema e a caracterização do espaço da solução, incluindo os fatores relevantes do espaço do negócio e os conceitos preliminares do ciclo de vida. Isto inclui o desenvolvimento de um entendimento do contexto e de quaisquer parâmetros-chave, como caracteristicas criticas de qualidade, por exemplo, ameaças à segurança, riscos à proteção, interfaces humanas, características operacionais e contexto de garantia do sistema. Atividades e tarefas relevantes incluem b) 1) e 2);
  - c) 1); e d) 1).
- h) O Processo de Definição de Necessidades e Requisitos dos Stakeholders (6.4.2) fornece a seleção e a definição de características, incluindo características críticas de qualidade e itens de informação associados. As atividades e a documentação são úteis para identificar, priorizar, definir e registrar requisitos para as características críticas de qualidade. Atividades e tarefas relevantes incluem a) 1) e 2); b) 2), 3) e 4); c) 1) e 2); d) todas as tarefas; e e) 2).
O Processo de Definição de Requisitos de Sistema/Software (6.4.2) fornece a especificação de parâmetros para as características críticas da qualidade e a seleção de medidas para rastrear o cumprimento destes requisitos em relação ao sistema específico a ser desenvolvido. Atividades e tarefas relevantes incluem a) 1); b) todas as tarefas; e c) 2).

O Processo de Definição de Arquitetura (6.4.4) fornece a identificação de preocupações dos stakeholders sob a perspectiva de arquitetura. Estas preocupações geralmente se traduzem em expectativas ou restrições ao longo das fases do ciclo de vida, relacionadas às características críticas de qualidade, como: utilização (por exemplo, disponibilidade, segurança, eficácia, usabilidade); suporte (por exemplo, reparabilidade, gerenciamento de obsolescência); evolução do sistema e do ambiente (por exemplo, adaptabilidade, escalabilidade, capacidade de sobrevivência); produção (por exemplo, produtividade, testabilidade); desativação (por exemplo, impacto ambiental, transportabilidade). Este processo aborda ainda os requisitos críticos de características de qualidade que orientam as decisões de arquitetura, incluindo a avaliação da arquitetura com relação às preocupações e características associadas. Atividades e tarefas relevantes incluem a) 2) e 4); b) 1); c) 2), 3), 4) e 5); d) 1); e e) 2).

O Processo de Definição do Design (6.4.5) fornece a determinação das características necessárias do design, o que inclui características criticas da qualidade, como critérios de segurança do design para as características especiais e avaliação de design alternativos em relação a estes critérios.

O Processo de Análise de Sistema (6.4.6) fornece o nível de análise necessário para entender o espaço do negócio com relação às características críticas da qualidade, pela realização de análises matemáticas, modelagem, simulação, experimentação e outras técnicas. Os resultados da análise são entradas para a negociação realizada por meio do Processo de Gerenciamento de Decisão em apoio a outros processos técnicos. Atividades e tarefas relevantes incluem

  - a) todas as tarefas; e b) todas as tarefas.
- m) O Processo de Implementação (6.4.7) fornece o registro das evidências de que os requisitos críticos de qualidade foram atendidos. Atividades e tarefas relevantes incluem b) 3).
- n) O Processo de Integração (6.4.8) fornece o planejamento da integração, incluindo as considerações para características críticas de qualidade e a garantia de que o atendimento das características é determinado e registrado. Atividades e tarefas relevantes incluem a) 1); b) 3); e c) 1).
- o) O Processo de Verificação (6.4.9) fornece o planejamento e a execução de uma estratégia para executar a verificação, incluindo as características críticas de qualidade. A estratégia de verificação Atividades e tarefas relevantes incluem a) 1) e 3); b) 1), 2); e c) 1) e 2). selecionada pode introduzir restrições de design que afetem o atendimento das características.
O Processo de Transição (6.4.10) fornece a instalação do sistema em seu ambiente operacional. Como algumas propriedades especiais envolvem um balanceamento do custo/benefício entre as restrições de design e as restrições operacionais. A instalação em geral é um ponto de atenção importante. Atividades e tarefas relevantes incluem a) 4); e b) 4), 6) e 7).

- q) O Processo de Validação (6.4.11) fornece evidências de que os serviços fornecidos pelo sistema atendem às necessidades dos stakeholders, incluindo as características críticas de qualidade. Atividades e tarefas relevantes incluem a) 1) e 3); b) 1) e 2); c) 1) e 2).
г) O Processo de Operação (6.4.12) provê o uso do sistema. Garantir que as características críticas de qualidade sejam atendidas adequadamente envolve o monitoramento da operação do sistema. Atividades e tarefas relevantes incluem b) 3) e 4); c) 1) e 2); e d) 1) e 2).

- s) O Processo de Manutenção (6.4.13) sustenta os recursos do sistema, particularmente sua disponibilidade contínua para prover suas funções, incluindo suas características críticas de qualidade. Isto inclui análise de falhas, tarefas de manutenção e tarefas de logística necessárias para garantir a operação contínua do sistema. Atividades e tarefas relevantes incluem b) todas as tarefas; c) todas as tarefas; e d) 1) e 2).
- t) O Processo de Desativação (6.4.14) encerra a existência de um sistema. A necessidade inerente de antecipar a desativação pode restringir o desenvolvimento. De fato, estas restrições podem ser características críticas de qualidade. Atividades e tarefas relevantes incluem a) 2); b) 1) e 2)

### E.5 Visão do processo de Gerenciamento de Interface

Esta seção fornece um exemplo de aplicação do ponto de vista do processo para produzir uma visão do processo para o gerenciamento da interface, com o objetivo de demonstrar como um projeto pode compor processos, atividades e tarefas deste documento para proporcionar uma atenção especial no atendimento das características do produto que foram selecionadas como sendo de especial interesse.

Este exemplo trata uma instância específica de uma visão de processo, chamada gerenciamento de interface, que inclui definição, design e gerenciamento de mudanças de interface. Neste documento, as tarefas que compreendem o gerenciamento de interface estão totalmente contidas nos processos existentes.

NOTA Para sistemas de software, as interfaces com outros sistemas são uma maneira típica de receber dados de entrada ou exportar dados de saída (relatórios). As interfaces com sistemas e serviços externos permitem que o sistema de software funcione em seu ambiente operacional e com os sistemas habilitadores. A GUI é uma interface especial para interação humana com o sistema de software.

Nome: Visão do Processo de Gerenciamento de Interface

Propósito: O propósito da Visão do Processo de Gerenciamento de Interface é facilitar a identificação, a definição, o design e gerenciamento de interfaces do sistema de software.

Resultados esperados

- a) As necessidades de negócio relacionadas às interfaces são identificadas;
- b) As necessidades dos stakeholders relacionadas às interfaces são identificadas;
- c) Os requisitos para as interfaces são definidos;
- d) As interfaces entre os elementos do sistema de software são identificadas e definidas;
- e) As interfaces entre o sistema de software e os sistemas externos são identificadas e definidas;
- f) A extensão da implementação dos requisitos da interface é monitorada continuamente.
Processos, atividades e tarefas do Gerenciamento de Interface

Esta visão do processo pode ser implementada usando os seguintes processos, atividades e taretas deste documento.

NOTA O INCOSE Systems Engineering Handbook contém descrições e elaboração sobre gerenciamento de interface.

- a) O processo de Avaliação e Controle do Projeto (6.3.2) fornece o monitoramento da extensão do atendimento dos requisitos, incluindo as interfaces e a comunicação dos resultados aos stakeholders e tomadores de decisão. Atividades e tarefas relevantes incluem b) 6), 7), 9) e 10).
O Processo de Gerenciamento de Decisão (6.3.3) fornece a avaliação de requisitos, caracteristicas de arquitetura e de design alternativos em relação aos critérios de decisão, incluindo as interfaces. Os resultados destas comparações são classificados, por meio de um modelo de seleção adequado e, em seguida, são usados para decidir sobre uma solução ideal. Atividades e tarefas relevantes incluem b) todas as tarefas; e c) 1).

- c) O Processo de Gestão de Riscos (6.3.4), na íntegra, prevê a identificação, avaliação e tratamento de riscos do sistema, incluindo aqueles relacionados às interfaces.
- d) O Processo de Gerenciamento de Configuração (6.3.5) fornece a identificação e o controle de interfaces. Inclui gerenciamento de especificações de interface e dos documentos de controle de interface. Os requisitos e alterações da interface interna e externa são documentados de acordo com a estratégia de GC do projeto, que geralmente é representada em um plano de GC. As atividades relevantes incluem b) 1) e d) 1).
- e) O Processo de Gerenciamento da Informação (6.3.6), na integra, fornece a especificação, o desenvolvimento e a manutenção de itens de informação para documentar as interfaces e o seu desempenho operacional.
т) O Processo de Medição (6.3.7), na íntegra, define uma abordagem que relaciona medidas às necessidades de informações de interface requeridas e, em seguida, gera e usa estas medidas para atender às necessidades de informações de interface identificadas.

- g) O processo de Garantia da Qualidade (6.3.8), na íntegra, aborda anomalias identificadas (incidentes e problemas) relacionadas ao atendimento dos requisitos da interface.
- h) O Processo de Análise de Negócio (6.4.1) fornece a definição do espaço do problema e a caracterização do espaço da solução, incluindo a descrição do ambiente e do contexto, bem como os conceitos operacionais preliminares, incluindo interfaces de sistema de software e interfaces de sistemas habilitadores. Muitas vezes, identifica sistemas externos que fazem interface com o sistema de interesse. Atividades e tarefas relevantes incluem b) 1) e 2); e c) 1).
- i) O Processo de Definição de Necessidades e Requisitos dos Stakeholders (6.4.2) fornece a identificaçao de stakeno/ders relacionados as interaces, a detiniçao de conceitos operacionais, as interações do sistema com usuários, às interfaces existentes a serem implantadas e ao ambiente pretendido (incluindo outros sistemas). Muitas vezes, identifica sistemas externos que fazem interface com o sistema de interesse. As atividades e tarefas relevantes incluem
  - a) 1), c) 1) e2) ed) 1) e3).
O processo de Definição de Requisitos de Sistema/Software (6.4.3) fornece a definição dos limites do sistema e dos requisitos de interface. Atividades e tarefas relevantes incluem a) 1); b) 3) e 4);

  - c) todas as tarefas e d) 1) e 3).
- k) O Processo de Definição de Arquitetura (6.4.4) fornece a identificação de interfaces da perspectiva da arquitetura, à medida que os modelos de arquitetura evoluem. Este processo descreve e define detalhadamente as interfaces na extensão necessária para a descrição da arquitetura.
O processo de Definição de Design (6.4.5) fornece o refinamento e a definição completa das interfaces e a criação dos itens de informação para especificar as características e protocolos da interface. Atividades e tarefas relevantes incluem b) 2), 5) e 6); c3) e d) 2).

- m) O Processo de Análise de Sistema (6.4.6) fornece o nível de análise necessário para equilibrar a arquitetura da interface, as restrições de design, os requisitos de desempenho da interface e as medições de desempenho operacional, por meio da realização de modelagem, simulação e outras técnicas. Os resultados da análise são inseridos no Processo de Gerenciamento de Decisão em suporte a outros processos técnicos. Atividades e tarefas relevantes incluem a) todas as tarefas; e b) todas as taretas.
- n) O Processo de Implementação (6.4.7) fornece o desenvolvimento das interfaces e registra a evidência de que os requisitos da interface para um elemento do sistema implementado foram atendidos. Atividades e tarefas relevantes incluem b) 1) e 3).
- o) O Processo de Integração (6.4.8) fornece o planejamento da integração, incluindo as considerações para interfaces entre elementos do sistema de software e com sistemas externos. Também inclui a integração de sistemas ou elementos e interfaces do sistema e a confirmação das interfaces no sistema de software integrado. Atividades e tarefas relevantes incluem a) 1), 2) e 5); b) todas as tarefas; e c) 1).
- p) O Processo de Verificação (6.4.9) fornece evidências de que os serviços fornecidos pelo sistema atendem aos requisitos do sistema, incluindo os requisitos de interface. O processo prevê o planejamento e a execução de uma estratégia para executar a verificação, incluindo os requisitos de interface. A estratégia de verificação selecionada pode introduzir restrições de interface que afetem a sua implementação. Atividades e tarefas relevantes incluem a) 1) e 3); b) 1), 2); e c) 1).
O Processo de Transição (6.4.10) fornece planejamento e migração do sistema ou elementos do sistema de software e conjuntos de dados para um ambiente diferente usando interfaces e estabelecendo o uso de interfaces no novo sistema. Isto inclui identificar as restrições e verificar o status da instalação, ativação e operação das interfaces. Atividades e tarefas relevantes incluem

г) O Processo de Validação (6.4.11) fornece evidências de que os serviços fornecidos pelo sistema de software atendem às necessidades dos stakeholders, incluindo os requisitos de interface. A estratégia de validação selecionada pode introduzir restrições de interface que afetem a sua implementação. A validação envolve a comunicação com representantes dos stakenolders dos sistemas e serviços de interface. Atividades e tarefas relevantes incluem a) 4); b) 1) e 2); c) 1) e 2).

O Processo de Operação (6.4.12) fornece o uso do sistema de software. Também pode haver restrições nas interfaces para operações. A confirmação de que os requisitos da interface são atendidos adequadamente envolve o monitoramento da operação do sistema, a identificação e a execução de ações corretivas, quando as interfaces não funcionam adequadamente, e o suporte ao contato com os parceiros da interface (clientes). Atividades e tarefas relevantes incluem a) 1) e 2), b) 1), 3) e 4); c) 1) e 2) e d todas as tarefas.

- t) O Processo de Manutenção (6.4.13) mantém as capacidades do sistema de software, incluindo suas interfaces e a sua disponibilidade contínua para fornecer suas funções. Isto inclui tarefas de análise e manutenção de problemas e tarefas de logística necessárias para garantir a operação contínua e em tempo. Atividades e tarefas relevantes incluem a) 2); b) todas as tarefas; ed) 1), 2) e 3).
- u) O Processo de Desativação (6.4.14) encerra a existência de um sistema ou interface. Envolve atividades para desativar e interromper interfaces. Atividades e tarefas relevantes incluem
  - a) 2) e 3); e b) 1), 2) e 6).

### E.6 Visão do processo para Garantia do Software (Segurança da Informação)

Esta Seção fornece um exemplo de aplicação do ponto de vista do processo para gerar uma visão do processo para garantia do software, com o objetivo de ilustrar como um projeto pode gerar processos, atividades e tarefas deste documento, para fornecer atenção focada na obtenção das características de garantia do software que foram selecionadas como sendo de interesse especial. As características de garantia do software, sua extensão de atendimento, e informações relacionadas podem suportar uma reivindicação de garantia do software, conforme descrito na ISO/IEC/IEEE 15026.

Este exemplo é focado na proteção contra invasão intencional ou falha forçada devido à arquitetura, ao design ou à implementação do software, especialmente a construção do código.

Nome: Visão do Processo de Garantia do Software

Propósito: O propósito da Visão do Processo de Garantia do Software é fornecer evidências objetivas de que o software alcança níveis satisfatórios de certeza de que a proteção suficiente seja alcançada contra invasão intencional ou falha forçada devido à arquitetura, ao design ou à construção do código.

NOTA Em termos apropriados para conformidade com a ISO/IEC/IEEE 15026, as reivindicações de garantia com relação às características de software selecionadas para atenção especial são alcançadas e são fornecidas informações mostrando o atendimento destas reivindicações.

Resultados esperados

- a) As características de garantia do produto de software são selecionadas para atenção especial.
- b) Os requisitos para o atendimento às características de garantia do software são definidos.
- c) As medidas para os requisitos são selecionadas e relacionadas às características desejadas de garantia do software.
- d) As abordagens para atendimento às características desejadas de garantia do software são definidas e implementadas.
- e) A extensão do cumprimento dos requisitos é monitorada continuamente.
- f) Um nível satisfatório das características críticas de garantia do software é especificado e alcançado.
Os resultados esperados permitem a possibilidade de que as características de garantia do software desejadas ou requeridas não sejam medidas diretamente, mas possam ser inferidas com base em outras características do produto ou processo possam ser medidas. As medições podem ser usadas para mostrar conformidade com os padrões estabelecidos. O adquirente e o fornecedor acordam os padrões específicos a serem usados para esta verificação de conformidade.

Processos, atividades e tarefas de Garantia do Software

Esta visão do processo pode ser implementada usando os seguintes processos, atividades e tarefas deste documento.

- a) Os processos de Acordo (6.1) fornecem o estabelecimento de expectativas e responsabilidades relacionadas à garantia do software, incluindo acordos legais e requisitos de licenciamento, proteção dos ativos das organizações acessíveis aos fornecedores, possibilidade de comprometimento durante a entrega, detecção de anomalias, detecção de falsificações no elemento de entrada da aplicação, expectativas de resolução de defeitos, gerenciamento de patches, acordos de nível de serviço e proteção contra ameaças na cadeia de fornecedores. As atividades e tarefas relevantes incluem no Processo de Aquisição: a) 1) e 2) e c) 1); e no Processo de Fornecimento,
  - c) 1), e 1ez).
- b) O processo de Gerenciamento de Modelo de Ciclo de Vida (6.2.1) fornece o estabelecimento e a manutenção de políticas e procedimentos de garantia do software, incluindo um ciclo de vida de desenvolvimento de segurança do software e o uso controlado de código terceirizado. Atividades e tarefas relevantes incluem a) 2 e 3), b) 1 e c) todas as tarefas.
O Processo de Gerenciamento de Infraestrutura (6.2.2), na integra, fornece ambientes operacionais e de desenvolvimento seguros, ferramentas de garantia do software, gerenciamento no momento oportuno de patches e bibliotecas de códigos que são mantidas e aprimoradas adequadamente com base nas lições aprendidas dos projetos, organização e indústria.

- d) O Processo de Gerenciamento de Recursos Humanos (6.2.4), na integra, fornece avaliação relevante de funcionários e fornecedores com acesso ao software ou ao ambiente de desenvolvimento do software, e define o treinamento específico relacionado à garantia do software com base nos papéis e responsabilidades ao longo do ciclo de vida.
- e) O processo de Gerenciamento de Conhecimento (6.2.6) fornece coleta e manutenção de conhecimento e informação ao projeto sobre mudanças no cenário de ameaças, evoluções nas práticas de garantia do software, mitigação de vulnerabilidades do software, lições aprendidas de incidentes e respostas a incidentes e evoluções nas ferramentas de teste de garantia do software. Atividades e tarefas relevantes incluem b) todas as tarefas e d) 3).
- f) O Processo de Gerenciamento de Decisão (6.3.3), na íntegra, avalia requisitos, características de arquitetura e características de design alternativos, com base nos critérios de decisão, incluindo as características de garantia do software. Os resultados destas comparações são classificados e registrados junto com o modelo de seleção e, em seguida, são usados para decidir sobre uma solução ideal. Os stakeholders podem tomar decisões com base na justificativa fornecida.
- g) O Processo de Gerenciamento de Riscos (6.3.4), na íntegra, fornece a avaliação do potencial de não ser capaz de atender à segurança necessária do aplicativo, resultando em um risco para os usuários, incluindo os parceiros da interface, ou resultando na não utilização do software como pretendido. A segurança do software é uma categoria de risco em cada análise de risco.
Processo de Gerenciamento de Configuração (6.3.5) fornece o estabelecimento e a manutenção da integridade de todas as saídas identificadas de um projeto ou processo, incluindo o monitoramento de ativos e a segurança dos sistemas de armazenamento designados, e os disponibiliza para as partes autorizadas. Isto inclui registros de alterações feitas no software e nas versões do software, além de controle e auditoria de todos os acessos aos itens de software que tratam de funções de segurança. Atividades e tarefas relevantes incluem a) 1), d) 1) e f) 2).

O Processo de Gerenciamento da Informação (6.3.6), na íntegra, fornece as informações sobre o atendimento à garantia do software aos stakeholders relevantes, incluindo autoridades de aprovação ou regulatórias. As informações quantificáveis sobre o software são coletadas para apoiar um conjunto de argumentos que justificam uma reivindicação sobre a garantia do software de um sistema. Devido à sensibilidade dos dados, um cuidado adicional é tomado para identificar os públicos apropriados para as várias medidas de garantia. O gerenciamento de informação inclui a proteção de itens de informação confidenciais sobre garantia do software.

O Processo de Medição (6.3.7), na íntegra, fornece uma plataforma comum para coletar informações sobre as reivindicações, estratégias e evidências de garantia do software, às vezes chamadas de um caso de garantia.

O Processo de Garantia de Qualidade (6.3.8) avalia os processos do projeto e do fornecedor quanto à conformidade com os requisitos e procedimentos de garantia do software. Ele trata anomalias identificadas (incidentes e problemas) relacionadas à obtenção das características de garantia do software. Atividades e tarefas relevantes incluem c) e e) todas as tarefas.

O Processo de Análise de Negócio (6.4.1) fornece a compreensão do ambiente operacional do sistema de software em desenvolvimento e leis, políticas, riscos e restrições relacionadas à garantia do software. Atividades e tarefas relevantes incluem b) 1) e c) 1).

- m) O Processo de Definição de Necessidades e Requisitos dos Stakeholders (6.4.2) fornece a seleção e a definição de riscos e ameaças a missões ou informações. Ele incorpora esse conhecimento na definição de requisitos relacionados à garantia do software (segurança da informação), incluindo confidencialidade, disponibilidade e integridade no contexto de como é pretendido que o software funcione; e considerando os cenários de uso indevido ou violado. Os stakeholders precisam concordar sobre quais aspectos da garantia do software são suficientes. Atividades e tarefas relevantes incluem a) 2); b) 1) e 2); e c) todas as tarefas.
O Processo de Definição de Requisitos de Sistema/Software (6.4.3) fornece a seleção e definição de requisitos relacionados à garantia do software (segurança da informação), incluindo confidencialidade, disponibilidade e integridade no contexto de como é pretendido que o software funcione; e requisitos da integridade do software em caso de uso indevido ou violação. Atividades e tarefas relevantes incluem b) 3) e 4); e c) 3).

- o) O Processo de Definição de Arquitetura (6.4.4) fornece a identificação de preocupações dos stakeholders do ponto de vista da arquitetura, por meio da modelagem de ameaças e da avaliação da vulnerabilidade da arquitetura e do design do produto a possíveis ataques, a fim de obter uma compreensão do cenário de ameaças e dos elementos relevantes da arquitetura. Atividades e tarefas relevantes incluem a) 2) e 4); b) 1); c) todas as tarefas, d) 5) e f) 10, 20 e 5).
- p) O Processo de Definição do Design (6.4.5) fornece a determinação das características necessárias do design, que incluem a redução da área de ataque, incluindo a localização dos componentes; design patterns de garantia do software; e prevenção de anti-patterns. Atividades e tarefas relevantes incluem a) 2) e 3); b) 2), 3) e 6); c) 2) e d) 1).
O Processo de Implementação (6.4.7) fornece o uso de práticas seguras de codificação para evitar erros comuns de codificação que levem a vulnerabilidades exploráveis do produto e uso de uma variedade de técnicas de teste, incluindo inspeção de autenticidade competente, fuzz testing, teste de análise estática e testes dinâmicos, para identificar e solucionar os pontos fracos e vulnerabilidades do software. Atividades e tarefas relevantes incluem a) 1); e b) 1), 2) 3) e 4).

г) O Processo de Integração (6.4.8) fornece o planejamento da integração, incluindo as considerações para as características de garantia do software e a garantia de que o atendimento das características é determinado e registrado. A implementação de padrões de interface, sempre que possível, promove a sustentabilidade do sistema e do elemento e a reusabilidade do elemento. Atividades e tarefas relevantes incluem a) 2) e 5); b) 3); e c) 1) e 2).

S) O Processo de Verificação (6.4.9) fornece o planejamento e a execução de uma estratégia para verificar se os requisitos de garantia do software, incluindo as características de garantia do software, foram atendidos. A estratégia de verificação selecionada pode introduzir testes para fragilidades de código no processo de desenvolvimento ou durante a manutenção. A análise de ameaças fornece entradas para a criação de planos e casos de teste. Os resultados incluem as informações requeridas para efetuar as ações paliativas e corrigem as não conformidades no software ou nos processos que atuam sobre ele e respondem pela incerteza nas atividades de verificação, como a confiabilidade da ferramenta de teste e o nível de incerteza nos resultados (ou seja, taxas de falsos positivos e falsos negativos). Considerações adicionais incluem a resiliência do software para funcionar. Atividades e tarefas relevantes incluem a) 1), 4), 5) e 6 b) todas as tarefas; c) 1) e 2).

O Processo de Transição (6.4.10) fornece a instalação do sistema ou elemento do sistema de software em um ambiente diferente. Como algumas propriedades de garantia do software envolvem trade-off entre restrições de design e restrições operacionais, a atenção à instalação e a documentação do usuário geralmente é importante. Atividades e tarefas relevantes incluem

- a) 2); b) 1) e 4), 5) e 6); e c) 1) e 2).
O Processo de Validação (6.4.11) fornece evidências de que os serviços providos pelo sistema de software atendem às necessidades dos stakeholders, incluindo as caracteristicas de garantia do software. Os métodos de validação incluem varreduras de vulnerabilidades, avaliação e validação de código usando uma variedade de ferramentas e técnicas, como análise estática de código, análise dinâmica de código, análise de código binário, ferramentas de cobertura de código, teste de estresse e uso de ferramentas para reunir evidências de alterações resultantes de atividades de manutenção remota. Considerações adicionais incluem a resiliência do software para funcionar em casos de uso e violação. As atividades e tarefas relevantes incluem:

- a) 1), 3 e 4), b todas as tarefas e c) 2) e 3).
O Processo de Operação (6.4.12) fornece o uso do sistema de software. Garantir que as características de garantia do software sejam atendidas adequadamente envolve o monitoramento da operação do sistema para entregar seus serviços no ambiente pretendido e o fornecimento do suporte aos clientes do produto de software. Os planos para este processo consideram o atendimento à segurança da aplicação durante toda a vida do sistema, restrições operacionais como controle de acesso e consistência das premissas feitas durante as fases anteriores em relação à segurança da aplicação no ambiente operacional. O processo inclui o estabelecimento de sistemas e procedimentos de relatório para investigação e tratamento de incidentes relacionados à segurança da aplicação. Atividades e tarefas relevantes incluem

- a) 1), b) todas as tarefas; c) 1), 2) e 3); e d) 1).
O Processo de Manutenção (6.4.13) mantém as capacidades do sistema de software, particularmente a sua disponibilidade contínua para fornecer as suas características de garantia do software. Isto inclui análise de falhas, tarefas de manutenção e de logística necessárias para garantir a operação contínua do sistema. O Processo de Manutenção provê a avaliação do efeito das alterações feitas no software durante a sua manutenção sobre a garantia do software, mantendo evidências apropriadas. Inclui um processo documentado para correção e reparação do software, detectando e removendo ou inativando o software não autorizado e malicioso,

e um processo para informar um adquirente ou parceiro de interface sobre mecanismos de notificação e reparo. A correção de vulnerabilidades é priorizada com base em uma variedade de fatores, incluindo risco. As práticas documentadas de desenvolvimento e manutenção são seguidas ao implementar o reparo do software. Atividades e tarefas relevantes incluem

  - a) 1); b) todas as tarefas; c) todas as tarefas; e d) 1) e 2).
- x) O Processo de Desativação (6.4.14) encerra a existência de um sistema ou interface. A necessidade inerente de antecipar a desativação pode restringir o desenvolvimento e o gerenciamento dos dados contidos no sistema de software. Na realidade, estas restrições podem ser características de garantia do software. Atividades e tarefas relevantes incluem a) 1), 2) e 5); b) todas as tarefas; ec) 1)е3).

## Anexo F (informativo) — Modelagem da arquitetura de sistemas de software


### F.1 Introdução

Neste documento, as atividades de arquitetura e design são descritas como processos separados. Diversas iterações dos processos de Definição de Arquitetura, de Definição de Design e de Implementação podem estar envolvidas quando se estiver evoluindo a arquitetura de um elemento de software, isto é, para determinar quando uma entidade ou função será realizada por meio de integração de software existente, reuso adaptativo ou software recém-construído. Nas comunidades de Engenharia de Sistemas e Software que tratam de sistemas complexos, a arquitetura pode ser seguida por diferentes designs para diferentes sistemas em diferentes linhas de produto. Neste caso, é importante executar estes dois processos de forma separada. Além disso, a arquitetura é muitas vezes feita por outras razões que não servir de base imediata para o design, como direcionar os investimentos em tecnologia, atingir consistência ou reduzir a complexidade em uma linha de produto ou portfólio de projetos de uma organização, ou para orientar decisões na relação adquirente-fornecedor.

A arquitetura de um sistema de software pode ser entendida como um conjunto de entidades arquiteturais estruturadas e seus relacionamentos, escolhidos para atender a características como interoperabilidade, escalabilidade, resiliência ambiental, encapsulamento, disponibilidade, viabilidade econômica, robustez, eficiência na execução ou eficácia na missão (adequação para uso). A arquitetura funções, fluxos de função, interfaces, itens de fluxo de recursos, elementos de dados ou informações, de sistema de software trata dos relacionamentos entre uma variedade de entidades como cenários, objetos, componentes físicos e ambientes, contéineres, nós, links, recursos de comunicação, bientes, conteneres de, inha

restrições, equações e modelos paramétricos.

Este Anexo descreve alguns dos modelos (tipos de modelos) que são usados para criar e avaliar a arquitetura de sistemas de software.

NOTA A ISO/IEC/IEEE 15288:2015, Anexo F descreve como os modelos e as visões são aplicados para a arquitetura de sistemas de forma geral, e tem informações adicionais relativas a visões e modelagem da arquitetura de produtos físicos, como modelos de massa e modelos de layout.


### F.2 Visões, modelos e tipos de modelos usados em arquitetura de sistemas

de software

O processo de Definição Arquitetural usa uma variedade de modelos para sistemas de software, incluindo os modelos de exemplo listados na seção a seguir. Tipos de modelos especificam linguagens, notações, convenções, técnicas de modelagem, métodos analíticos ou outras operações a serem usadas nos modelos de cada tipo. (Práticas tradicionais de engenharia de sistemas classificam alguns destes modelos como "modelos lógicos" e "modelos físicos", mas a distinção de taxonomia é desnecessária na aplicação deste documento). Uma variedade de visões é usada para representar como a arquitetura do sistema trata as preocupações dos stakeholders. As visões são compostas por modelos. Por exemplo, uma visão lógica de software pode representar processos de negócio

em suas funções; uma visão de processo pode representar os eventos e as transformações que ocorrem em diferentes estados do software e podem incluir preocupações relativas às concorrência e oportunidade; uma visão estrutural representa os diferentes componentes do sistema, os quais podem estar associados a elementos físicos ou virtuais; uma visão da informação representa os relacionamentos entre os elementos de dados contidos no e transformados pelo software.

Ver a ISO/IEC/IEEE 42010 para definições de termos de arquitetura e detalhes adicionais sobre conceitos e modelos arquiteturais.


#### F.2.1 Modelo funcional

Um modelo funcional de sistema é uma representação de um conjunto de funções que define as transformações das entradas em saídas, executadas pelo sistema para cumprir a sua missão ou propósito. Estas funções são determinadas pelo comportamento esperado do sistema quando usado conforme pretendido. Consequentemente, toda função do sistema está associada com a interação entre o sistema e o seu ambiente. Requisitos funcionais, de desempenho, não funcionais e restrições são geralmente analisados para determinar funções e fluxos de entrada-saída. Quando as funções são associadas aos elementos do sistema, o processo de definição do design precisara determinar se cada elemento do sistema/software foi suficientemente especificado para construí-lo ou comprá-lo. Se o elemento do sistema for aperfeiçoado posteriormente para alcançar esta suficiência, então as funções associadas ao elemento do sistema também são melhoradas posteriormente e devidamente associadas aos subelementos. Normalmente, existem múltiplas formas de decompor as funções que contribuem para a definição das múltiplas arquiteturas candidatas.


#### F.2.2 Modelo estático

Um modelo estático descreve a estrutura do sistema de software. Em programação orientada a objetos, isto é representado por meio de um conjunto de objetos (classes) e seus relacionamentos (herança, associação e dependência), retratados como nós e links.


#### F.2.3 Modelo de dados

Um modelo de dados (modelo semântico ou de informação) representa os elementos de dados e seus relacionamentos e propriedades (atributos) que o sistema de software vai tratar. Modelos lógicos de dados usam um esquema para refletir os relacionamentos estruturais entre as entidades de dados que podem ser implementadas em bancos de dados. Modelos de dados refletem diferentes tipos de dados (texto, gráficos, dados geográficos, imagens, objetos em geral) e seu uso em funções do sistema (frequência de modificação, volume de dados, uso em pesquisas) assim como os relacionamentos lógicos entre os elementos de dados. Modelos de dados são aplicados ao desenvolvimento de interfaces e serviços de software, análise de dados e apresentação de dados. Modelos físicos de dados refletem o esquema para o armazenamento e a recuperação de registros de dados.


#### F.2.4 Modelo comportamental

Um modelo comportamental (modelo dinâmico) é um arranjo de funções e interfaces (internas e externas) que define como o sistema ou os seus elementos agem sob determinadas condições para sustentar os cenários operacionais, incluindo a sequência de execução, sincronização e concorrência, as condições de mudança comportamental e de desempenho. Modelos comportamentais são aplicaveis a sistemas de controle de software. Um modelo comportamental pode ser descrito com um conjunto de cenários interrelacionados. Isto inclui identificar os elementos comportamentais (por exemplo, modelos/estados, transições, gatilhos e cenários operacionais) ao longo do ciclo de vida.


#### F.2.5 Modelo temporal

Um modelo temporal de um sistema é uma representação que expressa como o tempo é levado em consideração no comportamento do sistema ou seus elementos que apresentam níveis de frequência de execução das funções (por exemplo, nível estratégico, nível tático, nível de monitoramento da operação, nível de regulação) correspondentes aos níveis de decisão que capacitam humanos e lógica de programa a monitorar e controlar a operação do sistema. Isto inclui identificar elementos temporais (por exemplo, duração, frequência, tempo de resposta, gatilhos, timeout, condições de parada), a partir do conceito operacional e dos requisitos do sistema.


#### F.2.6 Modelo estrutural

Um modelo estrutural de sistema é a representação que mostra a disposição dos elementos em relação uns aos outros e, quando necessário, mostra as interfaces entre os elementos e as entidades externas. Este modelo permite consolidar ou identificar interfaces físicas entre os elementos em um nível da hierarquia do sistema e entre níveis dessa hierarquia, assim como aquelas entidades externas que dizem respeito ao sistema (em seu ambiente/contexto). Modelos estruturais podem ser decomposições hierárquicas ou orientados a objetos.


#### F.2.7 Modelo de rede

Um modelo de rede define um arranjo de nós e links para ajudar a compreender como os recursos (por exemplo, informações e pessoas) cruzam de um nó para outro. Um modelo de rede pode ser usado para determinar restrições, como throughput, latência e pontos de congestionamento. Um modelo de rede é às vezes modelado juntamente com uma pilha de protocolos, para compreender como as camadas de rede interagem verticalmente para cima e para baixo na pilha.


### F.3 Outras considerações sobre modelos

Preocupações dos stakeholders sobre o ciclo de vida, como manutenção, evolução, desativação, potenciais mudanças no ambiente, gerenciamento da obsolescência e outros requisitos não funcionais são tratadas pela definição de características arquiteturais, como modularidade, independência relativa, escalabilidade, capacidade de atualização, adaptação a diversos ambientes, nível de eficácia, confiabilidade, robustez e resiliência. Outros modelos necessários podem incluir algumas dessas características ou outras características críticas de qualidade. Por exemplo, um caso de um software de segurança, considerado um modelo, pode ajudar na dedução de potenciais mitigações arquiteturais para minimizar riscos operacionais (perda de objetivo devido à exploração de vulnerabilidades de segurança) relacionados às preocupações e funções críticas.

A determinação de quais modelos utilizar em uma definição de sistema pode ser baseada no exame das preocupações dos stakeholders. Os modelos e suas visões resultantes podem ser usados para expressar como a arquitetura e o design do sistema abordam as suas preocupações e para obter um melhor entendimento de suas necessidades, desejos e expectativas reais.

Além disto, modelos podem ser usados em outros processos de ciclo de vida, além da definição da arquitetura e do design. A Engenharia de Sistemas Baseada em Modelos (MBSE) é a aplicação formalizada da modelagem para apoiar as atividades de sistema relativas a requisitos, arquitetura, design, análise, verificação e validação ao longo do ciclo de vida.

NOTA Um modelo de verificação e validação define representações de informações de teste que podem apoiar a verificação da arquitetura. Modelos de verificação e validação podem gerar análises, dados, casos e outras informações de testes.


## Anexo G (informativo) — Aplicação de processos de ciclo de vida de software a um sistema

de sistemas


### G.1 Introdução

Um sistema de sistemas (SoS) é um sistema de interesse (SOI) cujos elementos são sistemas. Um SoS reúne um conjunto de sistemas para uma tarefa que nenhum deles consegue cumprir sozinho. Cada sistema constituinte mantém seu próprio gerenciamento, objetivos e recursos ao mesmo tempo em que atua de forma coordenada com o SoS e se adapta para atender aos objetivos deste. No contexto da terminologia discutida em 5.2.3 (como ilustrado na Figura 3), o conjunto da composição dos sistemas, incluindo o SOl original, sistemas habilitadores e sistemas que interagem, constituem um SoS. Onde houver preocupações que afetem o conjunto da composição, o sistema de sistemas se torna o SOI, que é considerado para satisfazer alguns objetivos de negócio que não podem ser satisfeitos individualmente pelos sistemas que o compõem, ou para entender um comportamento emergente da combinação.

Este Anexo trata da aplicação dos processos de ciclo de vida de sistema para SoS. Ele descreve as características gerais, os tipos comuns de SoS e as implicações ao longo do ciclo de vida.


### G.2 Características e tipos de SoS

Os SoS são caracterizados pela independência gerencial e operacional dos sistemas constituintes, os quais, em muitos casos são desenvolvidos e continuam a apoiar os usuários originalmente identificados simultaneamente com os usuários do SoS. Em outros contextos, cada sistema constituinte em si é um SOI; sua existência frequentemente antecede o SoS, enquanto suas características foram originalmente desenvolvidas para atender às necessidades dos seus usuários iniciais. Como constituinte do Sos, suas considerações são expandidas para abranger as necessidades mais amplas do SoS. Isto implica complexidade adicional, particularmente quando os sistemas continuam a evoluir independentemente do SoS. Os sistemas constituintes normalmente também mantém seus stakeholders e seus mecanismos de governança originais, o que limita as alternativas para tratar

Os SoS têm sido caracterizados em quatro tipos com base nos relacionamentos de governança entre os sistemas constituintes e o SoS (Tabela G.1). As relações de governança mais fortes se aplicam aos sistemas de sistemas direcionados, onde a organização do Sos tem autoridade sobre os sistemas constituintes apesar do fato de que os sistemas constituintes não foram originalmente desenvolvidos para suportar o SoS. Um pouco menos de controle é oferecido aos SoS reconhecidos, onde a autoridade alocada entre os sistemas constituintes e o sistema de sistemas tem um impacto na aplicação de alguns dos processos de engenharia de sistemas. Nos Sos colaborativos, que não possuem autoridades de sistema de sistemas, a aplicação de engenharia de sistemas depende da cooperação entre os sistemas constituintes. Sistemas de sistemas virtuais são amplamente auto-organizados e limitam a oportunidade para engenharia de sistemas do SoS.


**Tabela G.1 - Tipos de Sistemas de Sistemas**

| Tipo de SoS | Característica |
|---|---|
| Virtual | • Autoridade de gerenciamento descentralizada |
|  | • Não há propósito explícito acordado centralizadamente |
|  | • Comportamentos emergentes que dependem de mecanismos |
|  | relativamente invisíveis para continuidade |
| Colaborativo | • Sistemas constituintes interagem voluntariamente para atender |
|  | aos propósitos acordados |
|  | • Coletivamente, decidem como interoperar, impondo e mantendo |
|  | padrões |
| Reconhecido | • Objetivos reconhecidos, um gerente e recursos designados para |
|  | o Sos |
|  | • Sistemas constituintes mantêm sua propriedade, gerenciamento |
|  | e recursos independentes |
| Direcionado | SoS integrado, construído e gerenciado para atender aos propósitos • |
|  | específicos |
|  | Gerenciado e evoluído de forma centralizada |
|  | Sistemas constituintes mantêm a capacidade de operar de forma |
|  | independente |
|  | Modo de operação normal é subordinado a um propósito central • |


Uma característica chave do SoS é a emergência - os efeitos imprevistos no nível do SoS atribuídos à dinâmica complexa de interação dos sistemas constituintes. No entanto, no SoS, os sistemas constituintes são intencionalmente considerados na sua combinação, de forma a obter e analisar os resultados que não seria possível obter com os sistemas individuais. A complexidade dos sistemas constituintes e o fato deles talvez terem sido projetados sem a preocupação do seu papel no SoS, podem resultar em comportamentos novos e inesperados. Identificar e tratar antecipadamente resultados emergentes é um desafio particular na engenharia de SoS.

NOTA Alguns dos maiores softwares SoS, como a Internet, são SoS virtuais, nos quais os sistemas constituintes são projetados para seguir recomendações e protocolos de comunicação comuns. SoS virtuais podem exibir comportamentos emergentes benéficos, como redundância, reconfiguração dinâmica, colaboração e resiliência.


### G.3 Processos de Engenharia de Sistemas aplicados aos sistemas de sistemas


#### G.3.1 Geral

As características de SoS acima descritas têm implicações na aplicação de cada um dos quatro tipos de processos de ciclo de vida de sistemas.


#### G.3.2 Processos de Acordo

Processos de Acordo são cruciais para o SoS, porque eles estabelecem modos de controle de desenvolvimento e de operação entre as organizações responsáveis pelo SoS e os sistemas constituintes geralmente independentes. Sistemas constituintes, que são adquiridos e gerenciados

por organizações diferentes, mantém, às vezes, os objetivos originais que não se alinham com os do SoS. Exceto no caso de SoS direcionado, a organização do SoS não pode executar tarefas em uma organização de um sistema constituinte sem a sua cooperação. Em um SoS reconhecido ou em um SoS colaborativo, estas tarefas são equilibradas com as tarefas do sistema constituinte como um SOl por si só. Para SoS virtual, os processos de acordo podem ser informais ou considerados apenas para propósitos de análise.

Mesmo em acordos entre proprietários de sistemas constituintes, existe ainda um adquirente e um fornecedor. Um proprietário de um sistema pode tanto ser um adquirente como um fornecedor para outro sistema constituinte.


#### G.3.3 Processos Organizacionais Habilitadores de Projeto

Em um Sistema de Interesse típico, os Processos Organizacionais Habilitadores de Projeto estabelecem o ambiente no qual os projetos são conduzidos. A organização estabelece os processos e os modelos de ciclo de vida a serem usados nos projetos; estabelece, redireciona ou cancela projetos; provê os recursos requeridos, incluindo recursos humanos e financeiros; e estabelece e monitora as medidas de qualidade para sistemas e outros entregáveis que sejam desenvolvidos por projetos para clientes

Em um SoS, os proprietários dos sistemas constituintes geralmente detêm a responsabilidade por desenvolver seus sistemas, e cada um deles tem os seus próprios Processos Organizacionais Habilitadores de Projeto. Dependendo do tipo do SoS, ele também aplica estes Processos Organizacionais Habilitadores de Projeto para as considerações específicas do SoS: planejamento, análise, organização e integração das capacidades de uma combinação de sistemas existentes e novos sistemas em uma capacidade do SoS.

Consequentemente, nos SoS, estes Processos Organizacionais Habilitadores de Projeto são implementados em dois níveis. As organizações responsáveis pelos sistemas constituintes implementam estes processos para seus SOI independentes do SoS. A organização do SoS (ou em sistemas de sistemas colaborativos por acordo do SoS) implementa estes processos para as considerações que se aplicam ao SoS como um todo. Por exemplo, o Gerenciamento de Recursos Humanos é tratado pela organização de cada sistema constituinte para o desenvolvimento do seu sistema. A organização do SoS trata do Gerenciamento de Recursos Humanos somente para as atividades de desenvolvimento dos sistemas que se aplicam a todos os sistemas constituintes do SoS.

Um desafio específico no desenvolvimento de SoS é a falta de alinhamento entre os Processos Organizacionais Habilitadores de Projeto dos sistemas constituintes e os do SoS. Os processos dos sistemas constituintes são projetados para atender aos seus próprios resultados e às vezes não se alinham aos do SoS. Por exemplo, Gerenciamento de Portfólio pode ser uma responsabilidade do sistema constituinte nos casos onde a sua organização tenha controle total sobre o sistema constituinte e outros sistemas e projetos do seu portfólio, diferentemente do Gerenciamento de Portfólio da organização do SoS


#### G.3.4 Processos de Gerenciamento Técnico

Em um sistema de interesse típico, os processos de Gerenciamento Técnico tratam do gerenciamento dos recursos e dos ativos alocados pela gestão da organização, e em aplicá-los para atender aos acordos dos quais a organização ou organizações fazem parte. Eles estão relacionados com o gerenciamento de projetos, em particular planejamento em termos de custo, cronograma e realizações, com a verificação das ações para conformidade com planos e critérios de desempenho, e com

a identificação e seleção de ações corretivas para recuperar falhas no progresso e nas realizações. Eles são usados para estabelecer e executar os planos técnicos para o projeto, gerenciar informações da equipe técnica, avaliar o progresso técnico em relação aos planos para os produtos ou serviços do sistema, controlar as tarefas técnicas até a sua conclusão, e apoiar o processo de tomada de decisão (6.3).

Os processos de Gerenciamento Técnico são também implementados no nível do SoS e dos sistemas constituintes. Os processos de Gerenciamento Técnico são aplicados às considerações específicas da engenharia do SoS - planejamento, análise, organização e integração das capacidades de uma combinação de sistemas existentes e novos dentro da capacidade de um sistema de sistemas. Em paralelo, as organizações dos sistemas constituintes são responsáveis pela engenharia dos seus sistemas e pelos seus próprios processos de Gerenciamento Técnico.

A organização do SoS trata dos processos de Gerenciamento Técnico conforme eles se aplicam em todo o SoS, enquanto estes processos são também implementados de forma independente nas organizações dos sistemas constituintes. Para o gerenciamento de configuração, por exemplo, os sistemas constituintes gerenciam as suas próprias configurações enquanto o Sos trata do gerenciamento de configuração, conforme se aplica à combinação de sistemas no SoS. Os riscos são gerenciados pelos sistemas constituintes com base na avaliação de risco, conforme se aplica aos seus resultados, enquanto a gestão de riscos do SoS olha para os riscos do SoS.

Planejamento e Avaliação e Controle (6.3) são chave para todas as práticas de gerenciamento; um desafio-chave na engenharia de SoS é a falta de controle da organização do SoS sobre os processos dos sistemas constituintes (particularmente para Sos reconhecidos e Sos colaborativos). Direcionados pelos seus próprios requisitos organizacionais, cada sistema constituinte pode estar em um cronograma de desenvolvimento ou atualização que difere dos cronogramas de outros sistemas constituintes. A organização do SoS planeja um ciclo de vida integrado que reconheça as mudanças independentes nos sistemas constituintes, em complemento às mudanças iniciadas pelo SoS em um ciclo de vida que trate do SoS como um SOI. Isto frequentemente envolve a definição de versões intermediárias estáveis que marcam a evolução do SoS com capacidades incrementais adicionadas aos sistemas constituintes.


#### G.3.5 Processos Técnicos

Processos Técnicos dizem respeito às ações técnicas ao longo o ciclo de vida. Eles transformam as necessidades dos stakeholders primeiro em um produto e, então, por meio da aplicação daquele produto, fornecem um serviço sustentável, quando e onde necessário de forma a alcançar a satisfação do cliente. Os processos Técnicos são aplicados de forma a criar e usar um sistema, seja na forma de um modelo ou de um produto final, e se aplicam a qualquer nível em uma hierarquia de estrutura de sistema (6.4).

Assim como em outros processos quando aplicados ao SoS, os processos Técnicos são implementados tanto para o SoS quanto para os sistemas constituintes; em alguns casos, a implementação do SoS ocorre por meio da condução dos processos do sistema constituinte em lugar do SoS como um todo.

Análise de Negócio para um SoS analisa todo o ambiente de negócios do SoS. Na medida em que o sistema constituinte foi desenvolvido para operar naquele espaço, a Análise de Negócio para o sistema de sistemas e para os sistemas constituintes será amplamente compartilhada. O objetivo é determinar os melhores meios para fornecer a capacidade desejada.

A Definição de Necessidades e Requisitos foca o SoS de alto nível, mas também considera como as diferentes necessidades dos stakeholders para os sistemas individuais podem levar a restrições

A Definição de Requisitos de Sistema/Software para o SoS tende a ser definida no nível necessário para satisfazer as necessidades e os objetivos da missão dos stakeholders, a serem traduzidos em requisitos para os sistemas constituintes, com o SoS servindo como "stakeholder" para novos requisitos para os sistemas constituintes.

A arquitetura para o SoS é um framework para organizar e integrar as capacidades de uma combinação de sistemas novos e existentes em uma capacidade do SoS, deixando as arquiteturas dos sistemas constituintes para as suas organizações. Como os sistemas constituintes em um SoS geralmente são anteriores ao SoS, a Definição de Arquitetura do SoS geralmente começa com a arquitetura de fato do SoS. As alternativas de arquitetura são então examinadas para enquadrar as preocupações dos stakeho/ders e atender aos requisitos de nível superior do SoS, para reconhecer o efeito de novos requisitos para os sistemas constituintes e acomodar as restrições da arquitetura do sistema constituinte.

O processo de Definição do Design fornece dados e informações detalhadas suficientes para permitir a implementação do SoS. Isto envolve a colaboração com as organizações dos sistemas constituintes que conduzirão as suas próprias operações de design para identificar a abordagem para atender aos requisitos do SoS à medida que se aplicam ao seu sistema. Estas são de responsabilidade das organizações dos sistemas constituintes. A implementação é feita pelos sistemas constituintes com a organização do SoS com a função de monitoramento.

Integração, Verificação, Transição e Validação são feitas pelos sistemas constituintes para as mudanças que eles implementam visando atender aos requisitos gerados pelo SoS. Estes processos também se aplicam ao SoS quando os sistemas constituintes atualizados são integrados ao SoS e o desempenho é verificado e validado. A natureza independente e assincrona dos sistemas constituintes em um SoS representa desafios à implementação eficaz destes processos, conforme implementados em um SOl tradicional. Em alguns casos, as avaliações no nível do SoS só podem ser realizadas no ambiente de operação. Neste caso, convém que medidas de precaução sejam consideradas para evitar o comportamento adverso do SoS.

Finalmente, os processos de Operações, Manutenção e Desativação tendem a ser implementados pelos sistemas constituintes, dada a sua independência gerencial e operacional. As interações no nível de SoS podem facilitar a interoperabilidade e reduzir o esforço duplicado para estes processos.


## Anexo H (informativo) — Aplicação da Abordagem Ágil

Este documento foi elaborado com a intenção de ser aplicado em organizações e projetos de software usando abordagens e métodos ágeis, bem como naquelas que usam outras abordagens formais de engenharia. O desenvolvimento ágil é uma das abordagens mais usadas para o desenvolvimento de software (incluindo manutenção de software), porque acredita-se que seja mais econômico e entregue produtos utilizáveis mais rapidamente. Em grandes esforços de desenvolvimento de software, bem como em projetos menores, muitos métodos Ágeis podem ser usados com vários modelos de ciclo de vida, e diferentes métodos podem ser usados em diferentes pontos do ciclo de vida. Este Anexo pontua interpretações dos requisitos do processo neste documento que são apropriadas para as técnicas ágeis normalmente usadas.

Conforme discutido em 5.4.2, os modelos de ciclo de vida usados em projetos ágeis são muitas vezes altamente incrementais e evolutivos. No entanto, as organizações que usam métodos ágeis aplicam os processos do ciclo de vida identificados neste documento, incluindo processos organizacionais, técnicos e de gerenciamento técnico (e podem operar sob os processos de acordo). Conforme declarado em 5.4.1, este documento não prescreve qualquer sequência especifica de processos dentro do modelo de ciclo de vida. A sequência dos processos é determinada pelos objetivos do projeto e pela seleção do modelo de ciclo de vida. Um projeto ágil, uma vez que transforma ou combina atividades enquanto cria ou aprimora um software em operação, pode considerar mais apropriado requerer conformidade total com os resultados esperados (4.2.1) em vez de conformidade total com atividades e tarefas (4.2.2).

O desenvolvimento ágil é bem-sucedido, em parte, devido à natureza do software, que acomoda flexibilidade no design enquanto o software está sendo construído. Na prática ágil, design de software, implementação (construção) e integração continua são frequentemente executados de forma simultânea. Esta prática é contrastada com uma abordagem top-down formal de rastreabilidade, na qual a construção não pode começar até que o design seja aprovado, para que o software construído seja rastreado para um design detalhado previamente aprovado. Assim, os projetos ágeis aproveitam ao máximo a abordagem deste documento, na qual os processos ocorrem simultaneamente, em contraste com os projetos em fases sequenciais (cascata ideal).

Em projetos ageis, os conceitos de exploração, desenvolvimento, construção, teste, transição e desativação de software existente podem ser executados simultaneamente em iterações sucessivas. Projetos ágeis geralmente executam replanejamento simultaneamente com as atividades mencionadas acima. Nestas abordagens, usar o final de uma fase como um ponto de verificação ou controle de gerenciamento não é muito útil. Outras abordagens ágeis executam replanejamento em pontos entre determinadas iterações (por exemplo, sprints ou cadências predefinidas em time-boxes), para que cada uma destas iterações possa ser tratada como uma fase.

Projetos ágeis podem ter ciclos estreitamente ligados de desenvolvimento e de liberação de software (por exemplo, com liberações diárias, semanais ou mensais agendadas) ou podem separar a conclusão das iterações de desenvolvimento do gerenciamento de liberações de software agendadas, para a conveniência do cliente ou de acordo com a estratégia organizacional.

Além de aplicar um modelo de ciclo de vida altamente iterativo e evolutivo, as organizações ágeis possuem práticas específicas para os processos de Planejamento de Projeto e de Avaliação

e Controle de Projeto. Em vez de estabelecer os principais pontos de controle na transição entre fases ou processos, os projetos ágeis geralmente mantêm pontos de verificação menos formais ou análises críticas retrospectivas ao final de um ciclo de time-box determinado para estabelecer melhorias para o próximo ciclo. Cada iteração inclui atividades de design, desenvolvimento e teste (podendo ser desenvolvimento orientado a teste). Após uma sprint de uma a quatro semanas ou mais, novos elementos de software em funcionamento são aceitos como "done* - completamente desenvolvidos, verificados (testados) e validados. As lições aprendidas e as melhorias do processo são identificadas, e o trabalho começa em outra sprint. O aprendizado contínuo, a gestão de riscos e a melhoria de processos podem ser facilitados pelas reuniões de planejamento que iniciam cada iteração e por reuniões de retrospectivas realizadas no final de cada iteração.

Os métodos ágeis enfatizam o processo de Definição de Necessidades e Requisitos de Stakeholders, facilitando a mudança por meio de um alto grau de envolvimento contínuo dos stakeholders. Em projetos ágeis, os principais stakeholders, como o adquirente ou o representante do usuário, não são apenas aprovadores de informações, medições e relatórios de avaliação. O envolvimento contínuo dos stakeholders é consistente com este documento, que identifica o envolvimento dos stakeholders em todos os processos técnicos, bem como no processo de Adaptação (Anexo A). Eles estão intimamente envolvidos no gerenciamento de requisitos (6.4.3.3.d) a cada iteração, trazendo novos requisitos e mudanças nas prioridades, e participando quando os requisitos priorizados são selecionados a partir de um backlog de histórias ou funções não desenvolvidas e posteriormente refinadas para o desenvolvimento. A abordagem iterativa incentiva a flexibilidade de adicionar, repriorizar ou adiar os requisitos que são reconhecidos como estando dentro do escopo geral do projeto. Além disso, o envolvimento dos stakeholders na aprovação do software testado em cada iteração significa que a validação é contínua ao longo do projeto.

Com a definição incremental de requisitos em evolução, o conceito de escopo do projeto difere em um projeto ágil em relação aos projetos em que o escopo é definido por uma baseline predeterminada de requisitos especificados. Quando um projeto ágil requer um produto definido, seu escopo é inicialmente vinculado aos requisitos de alto nível ou fundamentais. Espera-se que níveis mais detalhados de definição do produto surjam à medida que se adquire conhecimento adicional ao longo da construção. O trabalho ágil sem produtos predefinidos (por exemplo, nível de esforço de manutenção) pode controlar o escopo por meio de time-boxes ou equipes com recursos limitados. Esta abordagem é particularmente apropriada para os esforços de manutenção de software, onde a extensão ou o conteúdo do trabalho corretivo ou adaptativo não é totalmente especificado no início.

A especificação de baselines também difere em grau e momento para os projetos de desenvolvimento ágil em comparação com os esforços de desenvolvimento mais tradicionais. A baseline de requisitos pode incluir inicialmente histórias de usuário de alto nível ("épicos) e medições-chave de desempenho, incluindo padrões de usabilidade. Projetos ágeis tiram o máximo de proveito da tarefa "Definir baselines durante o ciclo de vida" (6.3.5.3.b) 4). Durante o desenvolvimento, novas baselines são definidas e construídas pelo menos diariamente sob controle de configuração. Um elemento de software geralmente é rastreável a um requisito funcional de alto nível, no caso de uso que implemente e no caso de teste usado para verificar a sua funcionalidade e desempenho. Em vez de ser rastreável a um documento de design previamente aprovado sob baseline, um novo elemento de software pode simplesmente ser rastreado para um elemento ou objeto de design que foi, de fato, criado durante a construção do software e somente depois colocado sob controle de configuração.

A preparação de especificações, artefatos de design e itens de informação ou documentação durante projetos ágeis geralmente é limitada, enquanto os desenvolvedores de software aplicam seu tempo e habilidades para transformar um cenário ou narrativa de uma função (*história de usuário) em um elemento de software funcional e testável. Em vez de preparar pacotes de revisão elaborados para briefing em revisões de marcos principais pouco frequentes, a equipe se reúne frequentemente

com os stakeholders para apresentar evidências informais de conclusão de um conjunto de funções e estabelecer o conteúdo da próxima iteração. Os itens de informações documentados concentram-se no que será necessário para a transição, operação e manutenção, como documentação do operador e do usuário final e baselines das versões do software testadas e liberadas, com planos e casos de teste. Os projetos reusam procedimentos organizacionais para gerenciamento de configuração e liberação, verificação e gerenciamento de incidentes e problemas. Sempre que possível, a rastreabilidade bidirecional é ativada e aplicada por sistemas e procedimentos automatizados integrados para gerenciamento de requisitos, arquitetura e design, gerenciamento de configuração, medição e gerenciamento de informações.

A natureza incremental e iterativa do desenvolvimento ágil pode facilitar processos e práticas técnicos e gerenciais eficientes para reduzir o custo associado à mudança. Em comparação, os projetos gerenciados em cascata até o final buscam reduzir o custo total de retrabalho, minimizando o número de alterações, limitando o número de pontos de controle e colocando especificações detalhadas sob baseline, as quais são revisadas e rastreadas ao longo do projeto.

Projetos ágeis para sistemas complexos tentam gerenciar custos priorizando a realização das capacidades mais importantes o quanto antes. Se uma organização gerencia o desenvolvimento e a manutenção de todo o seu portfólio de sistemas de software como um sistema único, gerenciado pela taxa de gastos e não pelo total de gastos, a organização pode, em princípio, gerenciar este portfólio de sistemas como um desenvolvimento ágil continuo, análogo ao gerenciamento de um esforço de manutenção "Kanban" altamente iterativo.


## Anexo I (informativo) — Mapeamento de Processo da ISO/IEC/IEEE 12207:2008

Este documento adota um modelo de processo idêntico ao da ISO/IEC/IEEE 15288:2015. Para permitir a rastreabilidade e facilitar a transição para usuários da edição anterior (2008) da ISO/IEC/IEEE 12207, a Tabela I.1 apresenta uma referência cruzada de processos que mostra os principais alinhamentos entre as duas versões. A Tabela l.1, não implica que as definições de processo sejam idênticas entre as edições de 2008 e 2021 deste documento. Em alguns casos, os processos na versão anterior agora são abordados por meio de atividades e tarefas ou descritos em notas. Outros mapeamentos mais detalhados para alinhar o propósito do processo, resultados esperados, atividades ou tarefas das duas versões são possíveis. Um destes mapeamentos é mostrado na Tabela I.2.


**Tabela 1.1 - Comparação de processos na ABNT NBR ISO/IEC/IEEE 12207:2021 e na versão anterior**

| Subseção (2021) | Título (2021) | Subseção (2008) | Título (2008) |
|---|---|---|---|
| 6 | Processos do Ciclo de Vida de Software | 6 | Processos de Ciclo de Vida de Sistema |
|  |  | 7 | Processos Específicos de Software |
| 6.1 | Processos de Acordo | 6.1 | Processo contratual |
| 6.1.1 | Processo de Aquisição | 6.1.1 | Processo de aquisição |
| 6.1.2 | Processo de Fornecimento | 6.1.2 | Processo de Fornecimento |
| 6.2 | Processos Organizacionais | 6.2 | Processos Organizacionais Capacitadores de |
|  | Habilitadores de Projeto |  | Projetos |
| 6.2.1 | Processo de Gerenciamento de Modelo | 6.2.1 | Processo de Gestão de Modelo de Ciclo de Vida |
|  | de Ciclo de Vida |  |  |
| 6.2.2 | Processo de Gerenciamento de | 6.2.2 | Processo de Gestão de Infraestrutura |
|  | Infraestrutura |  |  |
| 6.2.3 | Processo de Gerenciamento de Portfólio | 6.2.3 | Processo de Gestão de Portfólio de Projetos |
| 6.2.4 | Processo de Gerenciamento de | 6.2.4 | Processo de Gestão de Recursos Humanos |
|  | Recursos Humanos |  |  |
| 6.2.5 | Processo de Gestão da Qualidade | 6.2.5 | Processo de Gestão da Qualidade |
| 6.2.6 | Processo de Gerenciamento do Conhecimento | 6.2.4.2.e | Conhecimento, informação e habilidades |
|  |  |  | individuais são coletados, compartilhados, |
|  |  |  | reutilizados e aperfeiçoados por toda a |
|  |  |  | organização |
|  |  | 6.2.4.3.4 | Gestão de Conhecimento (atividade) |
|  |  | 7.3 | Processos de Reuso de Software |
|  |  | 7.3.1 | Processo de Engenharia de Domínio |
|  |  | 7.3.2 | Processo de Gestão de Reuso de Ativos |
|  |  | 7.3.3 | Processo de Gestão do Programa de Reuso |
| 6.3 | Processos de Gerenciamento Técnico | 6.3 | Processos do Projeto |
|  |  | 7.2 | Processos de Apoio ao Software |
| 6.3.1 | Processo de Planejamento de Projeto | 6.3.1 | Processo de Planejamento de Projeto |
| 6.3.2 | Processo de Avaliação e Controle de | 6.3.2 | Avaliação do Projeto e Processo de Controle |
|  | Projeto | 7.2.6 | Processo de Revisão de Software |
| 6.3.3 | Processo de Gerenciamento de Decisão | 6.3.3 | Processo de Tomada de Decisão |
| 6.3.4 | Processo de Gestão de Riscos | 6.3.4 | Processo de Gestão de Risco |
| 6.3.5 | Processo de Gerenciamento de | 6.3.5 | Processo de Gestão de Configuração |
|  | Configuração | 7.2.2 | Processo de Gestão de Configuração de |
|  |  |  | Software |
| 6.3.6 | Processo de Gerenciamento da | 6.3.6 | Processo de Gestão da Informação |
|  | Informação | 7.2.1 | Processo de Gestão de Documentação de |
|  |  |  | Software |
| 6.3.7 | Processo de Medição | 6.3.7 | Processo de Medição |
| 6.3.8 | Processo de Garantia da Qualidade | 7.2.3 | Processo de Garantia de Qualidade de Software |
|  |  | 7.2.7 | Processo de Auditoria de Software |
|  |  | 7.2.8 | Processo de Resolução de Problemas de |
|  |  |  | Software |
| 6.4 | Processos Técnicos | 6.4 | Processos Técnicos |
| 6.4.1 | Processo de Análise de Negócio |  | NA [mas relacionado a alguns resultados de |
|  |  |  | 6.4.1 Processo de Definição dos Requisitos dos |
|  |  |  | Stakeholders] |
| 6.4.2 | Processo de Definição de Necessidades | 6.4.1 | Processo de Definição dos Requisitos dos |
|  | e Requisitos dos Stakeholders |  | Stakeholders |
| 6.4.3 | Processo de Definição de Requisitos de | 6.4.2 | Processo de Análise dos Requisitos do Sistema |
|  | Sistema/Software |  |  |
|  |  | 7.1.2 | Processo de Análise de Requisitos de Software |
| 6.4.4 | Processo de Definição de Arquitetura | 6.4.3 | Processo de Design de Arquitetura do Sistema |
|  |  | 7.1.3 | Processo de Projeto de Arquitetura de Software |
| 6.4.5 | Processo de Definição de Design | 6.4.3 | Processo de Design de Arquitetura do Sistema |
| 6.4.6 | Processo de Análise de Sistema |  | NA [mas as atividades de análise são |
|  |  |  | encontradas em muitos processos, |
|  |  |  | especialmente no Processo de Tomada de Decisão] |
| 6.4.7 | Processo de Implementação | 6.4.4 | Processo de Implementação |
|  |  | 7.1 | Processos de Implementação de Software |
|  |  | 7.1.1 | Processo de Implementação de Software |
|  |  | 7.1.5 | Processo de Construção de Software |
| 6.4.8 | Processo de Integração | 6.4.5 | Processo de Integração do Sistema |
|  |  | 7.1.6 | Processo de Integração de Software |
| 6.4.9 | Processo de Verificação | 6.4.6 | Processo de Teste de Qualificação do Sistema |
|  |  | 7.1.7 | Processo de Testes de Qualificação de Software |
|  |  | 7.2.4 | Processo de Verificação de Software |
| 6.4.10 | Processo de Transição | 6.2.4 | Processo de Gestão de Recursos Humanos |
|  |  | 6.4.7 | Processo de Instalação de Software |
| 6.4.11 | Processo de Validação | 6.4.8 | Processo de Suporte na Aceitação de Software |
|  |  | 7.2.5 | Processo de Validação de Software |
| 6.4.12 | Processo de Operação | 6.4.9 | Processo de Operação de Software |
| 6.4.13 | Processo de Manutenção | 6.4.10 | Processo de Manutenção de Software |
| 6.4.14 | Processo de Desativação | 6.4.11 | Processo de Desativação de Software |
| Anexo A | Processo de Adaptação | Anexo A Processo de Adaptação |  |


A Tabela 1.2 fornece um mapeamento dos resultados esperados dos processos neste documento com os resultados esperados dos processos selecionados de implementação, reuso e suporte específicos de software na ISO/IEC/IEEE 12207:2008. A Tabela 1.2 não implica que os resultados do processo sejam idênticos entre as edições de 2008 e 2021 deste documento. Nem todos os resultados esperados de processos deste documento são explicitamente identificados na edição anterior.


**Tabela 1.2 - Comparação dos resultados esperados do processo**

| Subseção (2021) | Resultado esperado (2021) | Subseção (2008) | Resultado esperado (2008) |
|---|---|---|---|
| 6.2.6 | Processo de Gerenciamento do | 7.3.1 | Processo de Engenharia de Dominio |
|  | Conhecimento |  |  |
|  |  |  | Os formulários para representação dos |
|  |  | 7.3.1.2.a, | modelos e arquiteturas de domínio são |
|  |  |  | selecionados |
|  |  |  | As fronteiras do domínio e seus |
|  |  | 7.3.1.2.b, | relacionamentos com outros domínios |
|  |  |  | são estabelecidos |
|  | É identificada uma taxonomia para a |  | É desenvolvido um modelo de domínio |
| 6.2.6.2.a | aplicação de ativos de conhecimento |  | que captura as caracteristicas, |
|  |  | 7.3.1.2.c, | capacidades, conceitos e funções |
|  |  |  | essenciais (comuns e específicos) deste |
|  |  |  | domínio |
|  |  |  | Uma arquitetura de domínio é |
|  |  |  | desenvolvida, descrevendo a família de sistemas que compõem o domínio, |
|  |  | 7.3.1.2.d |  |
|  |  |  | incluindo suas características comuns e |
|  |  |  | variabilidades |
|  |  | 7.3.1.2.e, | Os ativos pertencentes ao domínio são |
|  | São desenvolvidos ou adquiridos |  | especificados |
| 6.2.6.2.b | conhecimento organizacional, |  | Os ativos pertencentes ao domínio são |
|  | habilidades e ativos de conhecimento | 7.3.1.2.f | adquiridos, desenvolvidos e mantidos |
|  |  |  | durante seus ciclos de vida |
| 6.2.6.2.c | O conhecimento organizacional, |  | Os modelos e arquiteturas de domínio |
|  | habilidades e ativos de conhecimento | 7.3.1.2.g | são mantidos durante seus ciclos de |
|  | estão disponíveis |  | vida |
|  |  | 7.3.2 | Processo de Gestão de Reuso de |
|  |  |  | Ativos |
|  |  | 7.3.2.2.a, | Uma estratégia de gestão de ativos é |
| 6.2.6.2.a | É identificada uma taxonomia para a |  | documentada |
|  | aplicação de ativos de conhecimento | 7.3.2.2.b | Um esquema de classificação de ativos é |
|  |  |  | estabelecido |
| 6.2.6.2.b | São desenvolvidos ou adquiridos | 7.3.2.2.ćł | Critérios para aceitação, certificação e |
|  | conhecimento organizacional, habilidades e ativos de conhecimento |  | desativação de ativos são definidos |
|  |  | 7.3.2.2.d, | Um mecanismo de armazenamento e |
|  |  |  | recuperação de ativos é operado |
|  | O conhecimento organizacional, | 7.3.2.2.f, | As alterações dos ativos são controladas |
| 6.2.6.2.c | habilidades e ativos de conhecimento |  | Os usuários dos ativos são notificados |
|  | estão disponíveis |  | de problemas detectados, modificações |
|  |  | 7.3.2.2.g | realizadas, novas versões criadas e |
|  |  |  | exclusão de ativos do mecanismo de |
|  |  |  | armazenamento e recuperação |
|  | São coletados e analisados os |  |  |
| 6.2.6.2.d | dados de uso do gerenciamento do | 7.3.2.2.e | A utilização dos ativos é registrada |
|  | conhecimento |  |  |
|  |  | 7.3.3 | Processo de Gestão do Programa de |
|  |  |  | Reuso |
|  |  |  | A estratégia de reuso da organização, |
|  | É identificada uma taxonomia para a | 7.3.3.2.a, | incluindo seu propósito, escopo, |
| 6.2.6.2.a | aplicação de ativos de conhecimento |  | objetivos e metas é definida |
|  |  | 7.3.3.2.b | Os domínios para oportunidades de |
|  |  |  | reuso potenciais são identificados |
|  |  | 7.3.3.2.c, | A capacidade de reuso sistemático da |
|  |  |  | organização é avaliada |
| 6.2.6.2.b | São desenvolvidos ou adquiridos | 7.3.3.2.d, | O potencial de reuso de cada domínio é |
|  | conhecimento organizacional, |  | avaliado |
|  | habilidades e ativos de conhecimento |  | Propostas de reuso são avaliadas para |
|  |  | 7.3.3.2.e | assegurar que o produto do reuso seja adequado para a aplicação proposta |
|  | O conhecimento organizacional, |  | A estratégia de reuso é implementada na |
| 6.2.6.2.c | habilidades e ativos de conhecimento | 7.3.3.2.f | organização |
|  | estão disponíveis |  |  |
|  |  |  | Mecanismos de feedback, comunicação |
|  | São coletados e analisados os | 7.3.3.2.g, | e notificação que operam entre as partes |
| 6.2.6.2.d | dados de uso do gerenciamento do |  | afetadas são estabelecidos |
|  | conhecimento | 7.3.3.2h | O programa de reuso é monitorado e |
|  |  |  | avaliado |
| 6.3.1 | Processo de Planejamento de | 7.2.6 | Processo de Revisão de Software |
|  | Projeto |  |  |
| 6.3.1.2.a | Objetivos e planos são definidos | 7.2.6.2.a | Revisões gerenciais e técnicas são |
|  |  |  | realizadas com base nas necessidades |
|  |  |  | do projeto |
| 6.3.1.2.b | Papéis, responsabilidades, | 7.2.6.2.a | Revisões gerenciais e técnicas são realizadas com base nas necessidades |
|  | responsabilizações e autoridades são |  |  |
|  | definidos |  | do projeto |
|  | Recursos e serviços necessários |  | Revisões gerenciais e técnicas são |
| 6.3.1.2.c | para alcançar os objetivos são formalmente solicitados e | 72.6.2a | realizadas com base nas necessidades |
|  | comprometidos |  | do projeto |
| 6.3.1.2.d | Planos para a execução do projeto |  | Revisões gerenciais e técnicas são |
|  | são ativados | 7.2.6.2.a | realizadas com base nas necessidades do projeto |
| 6.3.2 | Processo de Avaliação e Controle | 7.2.6 | Processo de Revisão de Software |
|  | de Projeto |  |  |
|  | Medidas de desempenho ou | 7.2.6.2.c, | Os resultados de revisão são divulgados |
| 6.3.2.2.a | resultados de avaliações são |  | para todas as partes envolvidas |
|  | disponibilizados | 7.2.6.2.e | Riscos e problemas são identificados e |
|  |  |  | registrados |
|  |  |  | Revisões gerenciais e técnicas são |
|  | A adequação de papéis, | 7.2.6.2.a | realizadas com base nas necessidades |
| 6.3.2.2.b | responsabilidades, |  | do projeto |
|  | responsabilizações e autoridades é |  | O estado e os produtos de uma atividade |
|  | avaliada | 7.2.6.2.b | de um processo são avaliados por meio |
|  |  |  | das atividades de revisão |
|  |  |  | Revisões gerenciais e técnicas são |
|  |  | 7.2.6.2.a | realizadas com base nas necessidades |
| 6.3.2.2.c | A adequação de recursos é avaliada |  | do projeto |
|  |  |  | O estado e os produtos de uma atividade |
|  |  | 7.2.6.2.b | de um processo são avaliados por meio |
|  |  |  | das atividades de revisão |
| 6.3.2.2.d | Análises críticas de progresso técnico |  | Revisões gerenciais e técnicas são |
|  | são executadas | 7.2.6.2.a | realizadas com base nas necessidades |
|  |  |  | do projeto |
| 6.3.2.2.e | Desvios no desempenho do |  | O estado e os produtos de uma atividade |
|  | projeto em relação aos planos são | 7.2.6.2.b | de um processo são avaliados por meio |
|  | investigados e analisados |  | das atividades de revisão |
| 6.3.2.2.f | Os stakeholders afetados são | 7.2.6.2.c | Os resultados de revisão são divulgados |
|  | informados sobre o status do projeto |  | para todas as partes envolvidas |
| 6.3.2.2.g | Ação corretiva é definida e |  | Os itens que requerem alguma |
|  | direcionada, quando a realização do projeto não está atingindo as metas | 7.2.6.2.d | ação, resultantes das revisões, são |
|  |  |  | acompanhados ate seu encerramento |
| 6.3.4 | Processo de Gerenciamento de | 7.2.6 | Processo de Revisão de Software |
|  | Riscos |  |  |
| 6.3.4.2.a | Os riscos são identificados | 7.2.6.2.e | Riscos e problemas são identificados e |
|  |  |  | registrados |
| 6.3.5 | Processo de Gerenciamento de | 7.2.2 | Processo de Gestão de Configuração |
|  | Configuração |  | de Software |
| ABNT NBR ISO/IEC/EEE 12207:2021 e |  |  |  |
|  |  | 7.2.2.2.a, | É desenvolvida uma estratégia de gestão |
|  | Os itens que requerem |  | de configuração de software |
| 6.3.5.2.a | gerenciamento de configuração são |  | Itens gerados pelo processo ou projeto |
|  | identificados e gerenciados | 7.2.2.2.b | são identificados, definidos e colocados |
|  |  |  | sob uma baseline |
| 6.3.5.2.b | Baselines de configuração são |  | Itens gerados pelo processo ou projeto |
|  | estabelecidas | 7.222b | são identificados, definidos e colocados |
|  |  |  | sob uma baseline |
|  |  | 7.2.2.2.c, | Modificações e liberações dos itens são |
|  | Mudanças em itens sob |  | controladas |
| 6.3.5.2.c | gerenciamento de configuração são |  | Modificações e liberações são |
|  | controladas | 7.2.2.2.d | disponibilizadas para as partes |
|  |  |  | envolvidas |
| 6.3.5.2.d | Informações sobre o status da | 7.2.2.2.e | A situação dos itens e as modificações |
|  | configuração são disponibilizadas |  | são registradas e relatadas |
| 6.3.5.2.e | Auditorias de configuração requeridas | 7.2.2.2.f | A completeza e a consistência dos itens |
|  | são realizadas |  | são asseguradas |
|  |  | 7.2.2.2.c, | Modificações e liberações dos itens são |
|  |  |  | controladas |
| 6.3.5.2.f | Liberações e entregas do sistema são |  | Modificações e liberações são |
|  | controladas e aprovadas | 7.2.2.2.d | disponibilizadas para as partes |
|  |  |  | envolvidas |
|  |  | 7222g | O armazenamento, manuseio e entrega |
|  |  |  | dos itens são controlados |
| 6.3.6 | Processo de Gerenciamento da | 7.2.1 | Processo de Gestão de Documentação |
|  | Informação |  | de Software |
|  |  |  | É desenvolvida uma estratégia |
|  |  | 7.2.1.2.aąłą | identificando a documentação a ser |
| 6.3.6.2.a | As informações a serem gerenciadas |  | produzida durante o ciclo de vida do |
|  | são identificadas |  | produto ou serviço de software |
|  |  | 7.2.1.2.c | É identificada a documentação a ser |
|  |  |  | produzida pelo processo ou projeto |
|  |  |  | São identificadas as normas a serem |
|  |  | 7.2.1.2.łșŘšę | aplicadas para o desenvolvimento da |
| 6.3.6.2.b | As representações das informações |  | documentação de software |
|  | são definidas |  | São especificados, revisados e |
|  |  | 7.2.1.2.d | aprovados o conteúdo e o objetivo de |
|  |  |  | toda a documentação |
|  |  |  | São especificados, revisados e |
|  |  | 7.2.1.2.d, | aprovados o conteúdo e o objetivo de |
|  | As informações são obtidas, |  | toda a documentação |
| 6.3.6.2.c | desenvolvidas, transformadas, |  | A documentação é desenvolvida e |
|  | armazenadas, validadas, | 7.2.1.2.e, | disponibilizada de acordo com as normas |
|  | apresentadas e descartadas |  | identificadas |
|  |  | 7.2.1.2.f | A documentação é mantida de acordo |
|  |  |  | com os critérios definidos |
| 6.3.6.2.d | O status das informações é | 7.2.1.2.f | A documentação é mantida de acordo |
|  | identificado |  | com os critérios definidos |
| 6.3.6.2.e | As informações estão disponíveis |  | A documentação é desenvolvida e |
|  | para os stakeholders identificados | 7.2.1.2.e | disponibilizada de acordo com as normas |
|  |  |  | identificadas |
| 6.3.8 | Processo de Garantia da Qualidade | 7.2.3 | Processo de Garantia de Qualidade de |
|  |  |  | Software |
|  |  | 7.2.3.2.a, | É desenvolvida uma estratégia para |
|  | Procedimentos de garantia da |  | realizar a garantia de qualidade |
| 6.3.8.2.a | qualidade do projeto são definidos e |  | É verificada a conformidade de produtos, |
|  | implementados | 7.2.3.2.d | processos e atividades aos padrões, |
|  |  |  | procedimentos e requisitos aplicáveis |
| 6.3.8.2.b | Critérios e métodos para avaliações |  | É desenvolvida uma estratégia para |
|  | de garantia da qualidade são | 7.2.3.2.a | realizar garantia de qualidade |
|  | definidos |  |  |
|  | São executadas avaliações dos |  |  |
| 6.3.8.2.c | produtos, serviços e processos do |  | É verificada a conformidade de produtos, |
|  | projeto, consistentes com políticas, | 7.2.3.2.d | processos e atividades aos padrões, |
|  | procedimentos e requisitos de gestão |  | procedimentos e requisitos aplicáveis |
|  | da qualidade |  |  |
| 6.3.8.2.d | Resultados das avaliações são |  | É produzida e mantida a evidência da |
|  | fornecidos aos stakeholders | 7.2.3.2łšę | garantia de qualidade de software |
|  | relevantes |  |  |
| 6.3.8.2.f | Problemas priorizados são tratados |  | Problemas e/ou não conformidade em |
|  |  | 7.2.3.2.c | relação aos requisitos são identificados e |
|  |  |  | registrados |
|  |  | 7.2.6 | Processo de Revisão de Software |
| 6.3.8.2.a | Procedimentos de garantia da qualidade do projeto são definidos e |  | Revisões gerenciais e técnicas são |
|  |  | 7.2.6.2a | realizadas com base nas necessidades |
|  | implementados |  | do projeto |
| 6.3.8.2.b | Critérios e métodos para avaliações de garantia da qualidade sã |  | Revisões gerenciais e técnicas são |
|  | definidos | 7.2.6.2a | realizadas com base nas necessidades |
|  |  |  | do projeto |
|  | São executadas avaliações dos | 7.2.6.2.ałą | Revisões gerenciais e técnicas são |
|  | produtos, serviços e processos do |  | realizadas com base nas necessidades |
| 6.3.8.2.c | projeto, consistentes com políticas, |  | do projeto |
|  | procedimentos e requisitos de gestão |  | O estado e os produtos de uma atividade |
|  | da qualidade | 7.2.6.2.łšęź | de um processo são avaliados por meio |
|  |  |  | das atividades de revisão |
| 6.3.8.2.d | Resultados das avaliações são |  | Os resultados de revisão são divulgados |
|  | fornecidos aos stakeholders | 7.2.6.2.c | para todas as partes envolvidas |
|  | relevantes |  |  |
|  |  |  | Os itens que requerem alguma |
|  |  | 7.2.6.2.d, | ação, resultantes das revisões, são |
| 6.3.8.2.f | Problemas priorizados são tratados |  | acompanhados até seu encerramento |
|  |  | 7.2.6.2.e | Riscos e problemas são identificados e |
|  |  |  | registrados |
|  |  | 7.2.7 | Processo de Auditoria de Software |
|  | Procedimentos de garantia da |  | É desenvolvida e implementada uma |
| 6.3.8.2.a | qualidade do projeto são definidos e | 7.2.7.2.a | estratégia de auditoria |
|  | implementados |  |  |
|  | Critérios e métodos para avaliações |  | É desenvolvida e implementada uma |
| 6.3.8.2.b | de garantia da qualidade são | 7.2.7.2.a | estratégia de auditoria |
|  | definidos |  |  |
|  |  |  | A conformidade de produtos de trabalho |
|  | São executadas avaliações dos |  | e/ou dos serviços ou processos de |
|  | produtos, serviços e processos do | 7.2.7.2.b, | software com os requisitos, planos e |
| 6.3.8.2.c | projeto, consistentes com políticas, |  | acordo é determinada de acordo com a |
|  | procedimentos e requisitos de gestão |  | estratégia de auditoria |
|  | da qualidade | 7.2.7.2.c | As auditorias são realizadas por uma |
|  |  |  | parte independente apropriada |
|  | Resultados das avaliações são |  | Problemas detectados durante |
| 6.3.8.2.d | fornecidos aos stakeholders | 7.2.7.2.d | uma auditoria são identificados e |
|  | relevantes |  | comunicados para os responsáveis pela |
|  |  |  | ação corretiva e resolução |
|  |  | 7.2.8 | Processo de Resolução de Problema |
|  |  |  | de Software |
| 6.3.8.2.a | Procedimentos de garantia da |  | É desenvolvida uma estratégia de gestão |
|  | qualidade do projeto são definidos e | 7.2.8.2.a | de problemas |
|  | implementados |  |  |
| 6.3.8.2.b | Critérios e métodos para avaliações |  | É desenvolvida uma estratégia de gestão |
|  | de garantia da qualidade são | 7.2.8.2.a | de problemas |
|  | definidos |  |  |
| 6.3.8.2.d | Resultados das avaliações são | 7.2.8.2.f | O estado de cada um dos problemas |
|  | fornecidos aos stakeholders |  | relatados é conhecido |
|  | relevantes |  |  |
| 6.3.8.2.e | Incidentes são resolvidos |  |  |
|  |  | 7.2.8.2.b, | Os problemas são documentados, identificados e classificados |
|  |  | 7.2.8.2.c, | Problemas são analisados e avaliados |
| 6.3.8.2.f | Problemas priorizados são tratados |  | para identificar solução(ões) aceitável(is) |
|  |  | 7.2.8.2.d, | É implementada a resolução de |
|  |  |  | problemas |
|  |  | 7.2.8.2.e | Problemas são rastreados até o seu |
|  |  |  | fechamento |
| 6.4.3 | Processo de Definição de | 7.1.2 | Processo de Análise de Requisitos de |
|  | Requisitos de Sistema/Software |  | Software |
|  | A descrição do sistema ou elemento, |  | São definidos os requisitos alocados |
| 6.4.3.2.a | incluindo as interfaces, funções | 7.1.2.2.a | aos itens de software do sistema e suas |
|  | e fronteiras para uma solução de |  | interfaces |
|  | sistema, é definida |  |  |
|  |  |  | São definidos os requisitos alocados |
|  |  | 7.1.2.2.a, | aos itens de software do sistema e suas |
|  |  |  | interfaces |
|  | Requisitos de sistema/software |  | Prioridades são estabelecidas para |
|  | (funcionais, de desempenho, de | 7.1.2.2.e, | a implementação dos requisitos de |
| 6.4.3.2.b | processo, não funcionais e de |  | software |
|  | interface) e restrições de design são |  | Os requisitos de software são aprovados |
|  | definidos | 7.1.2.2.1, | e alterados conforme necessário |
|  |  |  | Os requisitos de software são |
|  |  | 7.1.2.2.h | comparados com as linhas básicas e |
|  |  |  | comunicados a todas as partes afetadas |
| 6.4.3.2.c | Medidas críticas de desempenho são | 7.1.2.2.c | O impacto dos requisitos de software no |
|  | definidas |  | ambiente operacional é entendido |
|  |  |  | Os requisitos de software são |
|  |  | 7.1.2.2.b, | analisados para verificar sua correção e |
|  |  |  | testabilidade |
| 6.4.3.2.d | Os requisitos de sistema/software são | 7.1.2.2.c, | O impacto dos requisitos de software no |
|  | analisados |  | ambiente operacional é entendido |
|  |  |  | Alterações nos requisitos de software |
|  |  | 7.1.2.2.g | são avaliadas para aferir impactos de |
|  |  |  | custo e cronograma e impacto técnico |
|  | Quaisquer sistemas ou serviços |  |  |
| 6.4.3.2.ęłą | habilitadores necessários para a definição de requisitos de sistema/ |  |  |
|  | software estão disponíveis |  |  |
| 6.4.3.2.f | A rastreabilidade de requisitos de |  | Consistência e rastreabilidade são |
|  | sistema/software para os requisitos | 7.1.2.2.d | estabelecidas entre os requisitos de |
|  | dos stakeholders é desenvolvida |  | software e os requisitos de sistema |
| 6.4.4 | Processo de Definição de | 7.1.3 | Processo de Projeto de Arquitetura de |
|  | Arquitetura |  | Software |
|  |  |  | Um projeto de arquitetura de software |
|  |  |  | é desenvolvido e comparado com a |
|  |  | 7.1.3.2.a, | linha básica para descrever os itens |
| 6.4.4.2.a | As preocupações dos stakeholders |  | de software que implementarão os |
|  | identificadas são atendidas pela |  | requisitos de software |
|  | arquitetura |  |  |
|  |  | 7.1.3.2.c | Consistência e rastreabilidade são |
|  |  |  | estabelecidas entre os requisitos de |
|  |  |  | software e o projeto de software |
|  |  |  | Um projeto de arquitetura de software |
| 6.4.4.2.b | Os pontos de vista da arquitetura são |  | é desenvolvido e comparado com a |
|  | desenvolvidos | 7.1.3.2.a | baseline para descrever os itens de |
|  |  |  | software que implementarão os requisitos |
|  |  |  | de software |
| 6.4.4.2.c | Contexto, fronteiras e interfaces | 7.1.3.2.b | São definidas interfaces internas e |
|  | externas do sistema são definidos |  | externas para cada item de software |
|  |  |  | Um projeto de arquitetura de software |
| 6.4.4.2.d | As visões e modelos de arquitetura |  | é desenvolvido e comparado com a |
|  | do sistema são desenvolvidos | 7.1.3.2.a | baseline para descrever os itens de |
|  |  |  | software que implementarão os requisitos |
|  |  |  | de software |
|  | Conceitos, propriedades, |  | Um projeto de arquitetura de software |
|  | características, comportamentos, |  | é desenvolvido e comparado com a |
| 6.4.4.2.€ | funções ou restrições que são | 7.1.3.2.a | baseline para descrever os itens de |
|  | significativos para as decisões de |  | software que implementarão os requisitos |
|  | arquitetura do sistema são alocados |  | de software |
|  | para entidades arquiteturais |  |  |
|  |  |  | Um projeto de arquitetura de software |
|  |  |  | é desenvolvido e comparado com a |
|  | Os elementos do sistema e suas | 7.1.3.2.a, | baseline para descrever os itens de |
| 6.4.4.2.f | interfaces são identificados |  | software que implementarão os requisitos |
|  |  |  | de software |
|  |  | 7.1.3.2.b | São definidas interfaces internas e |
|  |  |  | externas para cada item de software |
|  |  |  | Um projeto de arquitetura de software |
| 644.2g | As arquiteturas candidatas são |  | é desenvolvido e comparado com a |
|  | avaliadas | 7.1.3.2.a | baseline para descrever os itens de |
|  |  |  | software que implementarão os requisitos |
|  |  |  | de software |
|  |  |  | Um projeto de arquitetura de software |
| 6.4.4.2.h | Uma base arquitetural para os |  | é desenvolvido e comparado com a |
|  | processos ao longo do ciclo de vida | 7.1.3.2.a | baseline para descrever os itens de |
|  | é obtida |  | software que implementarão os requisitos |
|  |  |  | de software |
|  |  |  | Um projeto de arquitetura de software |
|  |  | 7.1.3.2.a, | é desenvolvido e comparado com a baseline para descrever os itens de |
|  | O alinhamento da arquitetura com |  | software que implementarão os requisitos |
| 6.4.4.2.i | os requisitos e as características do |  | de software |
|  | design é obtido |  | Consistência e rastreabilidade são |
|  |  | 7.1.3.2.c | estabelecidas entre os requisitos de |
|  |  |  | software e o projeto de software |
|  | Todos os sistemas ou serviços |  |  |
| 6.4.4.2.j | habilitadores necessários para a definição da arquitetura são |  |  |
|  | disponibilizados |  |  |
|  | A rastreabilidade dos elementos de |  | Consistência e rastreabilidade são |
| 6.4.4.2.k | arquitetura para os requisitos dos stakeholders e do sistema/software é | 7.1.3.2.c | estabelecidas entre os requisitos de |
|  | desenvolvida |  | software e o projeto de software |
|  |  | 7.3.1 | Processo de Engenharia de Domínio |
| 6.4.4.2.c | Contexto, fronteiras e interfaces |  | As fronteiras do domínio e seus |
|  | externas do sistema são definidos | 7.3.1.2.b | relacionamentos com outros domínios |
|  |  |  | são estabelecidos |
|  |  |  | Os formulários para representação dos |
|  |  | 7.3.1.2.a, | modelos e arquiteturas de domínio são |
|  |  |  | selecionados |
| 6.4.4.2.d | As visões e modelos de arquitetura do sistema são desenvolvidos |  | É desenvolvido um modelo de domínio |
|  |  | 7.3.1.2.c | que captura as características, capacidades, conceitos e funções |
|  |  |  | essenciais (comuns e específicos) deste |
|  |  |  | domínio |
|  |  |  | Uma arquitetura de domínio é |
| 6.4.4.2. h | Uma base arquitetural para os processos ao longo do ciclo de vida |  | desenvolvida, descrevendo a família de sistemas que compõe o domínio, |
|  |  | 7.3.1.2.d |  |
|  | é obtida |  | incluindo suas características comuns e |
|  |  |  | variabilidades |
| 6.4.5 | Processo de Definição de Design | 7.1.4 | Processo de Projeto de Software |
|  |  |  | É desenvolvido um projeto detalhado |
| 6.4.5.2.a | As características de design de cada | 7.1.4.2.a | de cada componente de software, |
|  | elemento do sistema são definidas |  | descrevendo as unidades de software a |
|  |  |  | serem construídas |
|  |  |  | É desenvolvido um projeto detalhado |
|  |  | 7.1.4.2.a, | de cada componente de software, |
| 6.4.5.2.b | Os requisitos do sistema/software são |  | descrevendo as unidades de software a serem construídas |
|  | alocados em elementos do sistema |  | Consistência e rastreabilidade são |
|  |  | 7.1.4.2.c | estabelecidas entre o projeto detalhado e |
|  |  |  | os requisitos e projeto de arquitetura |
|  |  |  | ABNT NBR ISO/IEC/IEEE 12207:202 |
|  | Os habilitadores de design |  | É desenvolvido um projeto detalhado |
| 6.4.5.2.c | necessários para a definição de | 7.1.4.2.a | de cada componente de software descrevendo as unidades de software a |
|  | design são selecionados ou definidos |  | serem construídas |
|  | Interfaces entre os elementos do |  | São definidas interfaces externas para |
| 6.4.5.2.d | sistema que compõem o sistema são | 7.1.4.2.b | cada item de software |
|  | definidas ou refinadas |  |  |
|  | São avaliadas alternativas de design |  | É desenvolvido um projeto detalhado |
| 6.4.5.2.e |  | 7.1.4.2.a | de cada componente de software, |
|  | para elementos do sistema |  | descrevendo as unidades de software a |
|  |  |  | serem construídas |
|  |  |  | É desenvolvido um projeto detalhado |
| 6.4.5.2.f | Artefatos de design são | 7.1.4.2.a | de cada componente de software, descrevendo as unidades de software a |
|  | desenvolvidos |  |  |
|  |  |  | serem construídas |
|  | Todos os sistemas ou serviços |  |  |
| 6.4.5.2.g | habilitadores necessários para definição de design estão disponíveis |  |  |
|  | A rastreabilidade das características |  | Consistência e rastreabilidade são |
| 6.4.5.2.h | de design para as entidades | 7.1.4.2.c | estabelecidas entre o projeto detalhado e |
|  | arquiteturais da arquitetura do |  | os requisitos e projeto de arquitetura |
|  | sistema é estabelecida |  |  |
| 6.4.7 | Processo de Implementação | 7.1.1 | Processo de Implementação de |
|  |  |  | Software |
|  |  | 7.1.1.2.a, | É definida uma estratégia de |
|  | São identificadas restrições de |  | implementação |
| 6.4.7.2.a | implementação que influenciam os |  | São identificadas restrições de tecnologia |
|  | requisitos, arquitetura ou design | 7.1.1.2.łšęš | de implementação no projeto |
| 6.4.7.2.b | Um elemento do sistema é construído | 7.1.1.2.c | É realizado um item de software |
| 6.4.7.2.c | Um elemento do sistema é |  | Um item de software é acondicionado e |
|  | empacotado ou armazenado | 7.1.1.2.d | armazenado de acordo com um acordo |
|  |  |  | de fornecimento |
| 6.4.7.2.d | Quaisquer sistemas ou serviços |  |  |
|  | habilitadores necessários para implementação estão disponíveis |  |  |
|  |  | 7.1.5 | Processo de Construção de Software |
|  |  |  | São definidos critérios de verificação |
|  | São identificadas restrições de | 7.1.5.2.a, | para todas as unidades de software com |
| 6.4.7.2.a | implementação que influenciam os |  | base em seus requisitos |
|  | requisitos, arquitetura ou design |  | É conseguida a verificação das unidades |
|  |  | 7.1.5.2.d | de software com base em seus requisitos |
|  |  |  | e no projeto |
|  |  | 7.1.5.2.b, | São produzidas as unidades de software |
|  | Um elemento do sistema é |  | definidas pelo projeto |
| 6.4.7.2.b | construído |  | É conseguida a verificação das unidades |
|  |  | 7.1.5.2.d | de software com base em seus requisitos |
|  |  |  | e no projeto |
| 6.4.7.2.e |  |  | Consistência e rastreabilidade são |
|  | A rastreabilidade é estabelecida | 7.1.5.2.c | estabelecidas entre as unidades de |
|  |  |  | software e requisitos e projeto |
| 6.4.8 | Processo de Integração | 7.1.6 | Processo de Integração de Software |
|  | São identificadas restrições de |  | É desenvolvida uma estratégia de |
| 6.4.8.2.a | integração que intluenciam os | 7.1.6.2.a | integração para unidades de software |
|  | requisitos do sistema, arquitetura ou |  | consistentes com o projeto de software e |
|  | design, incluindo interfaces |  | os requisitos de software priorizados |
|  |  |  | É desenvolvida uma estratégia de |
|  | São definidos os pontos de | 7.1.6.2.a, | integração para unidades de software |
|  | verificação e a abordagem para |  | consistentes com o projeto de software e |
| 6.4.8.2.b | o funcionamento correto da |  | os requisitos de software priorizados |
|  | consolidação das interfaces e funções |  | Os itens de software são verificados |
|  | do sistema | 7.1.6.2.c | usando os critérios definidos |
|  | Todos os sistemas ou serviços |  |  |
| 6.4.8.2.c | habilitadores necessários para a integração estão disponíveis |  |  |
|  | Um sistema composto por elementos |  | São produzidos os itens de software |
| 6.4.8.2.d | implementados do sistema é | 7.1.6.2.d | definidos pela estratégia de integração |
|  | integrado |  |  |
|  | As interfaces entre os elementos |  | Os itens de software são verificados |
| 6.4.8.2.e | implementados, que compõem o | 7.1.6.2.c | usando os critérios definidos |
|  | sistema, são verificadas |  |  |
| 6.4.8.2.f | As interfaces entre o sistema e o | 7.1.6.2.c | Os itens de software são verificados |
|  | ambiente externo são verificadas |  | usando os critérios definidos |
|  |  | 7.1.6.2.c, | Os itens de software são verificados |
| 6.4.8.2.g | São identificados resultados da |  | usando os critérios definidos |
|  | integração e anomalias | 7.1.6.2.e | Os resultados dos testes de integração |
|  |  |  | são documentados |
| 6.4.8.2.h | A rastreabilidade dos elementos do |  | Consistência e rastreabilidade são |
|  | sistema integrado é estabelecida | 7.1.6.2.f | estabelecidas entre o projeto de software |
|  |  |  | e os itens de software |
| 6.4.9 | Processo de Verificação | 7.1.5 | Processo de Construção de Software |
| 6.4.9.2.a | As restrições de verificação que |  | São definidos critérios de verificação |
|  | influenciam os requisitos, arquitetura | 7.1.5.2.a | para todas as unidades de software com |
|  | ou design são identificadas |  | base em seus requisitos |
|  |  | 7.1.6 | Processo de Integração de Software |
|  |  |  | São desenvolvidos critérios para itens de |
|  |  | 7.1.6.2.b, | software que asseguram conformidade |
|  |  |  | com os requisitos de software alocados |
|  | As restrições de verificação que |  | aos itens |
| 6,4.9.2.a | influenciam os requisitos, arquitetura |  | É desenvolvida e aplicada uma estratégia |
|  | ou design são identificadas |  | de regressão para reverificar itens de |
|  |  | 7.1.6.2 g | software quando uma alteração ocorre |
|  |  |  | nas unidades de software (incluindo |
|  |  |  | requisitos, projeto e código associados) |
| 6.4.9.2.c | O sistema ou elemento do sistema é verificado | 7.1.6.2.c | Os itens de software são verificados |
|  |  |  | usando os critérios definidos |
|  |  | 7.1.7 | Processo de Testes de Qualificação de |
|  |  |  | Software |
|  |  |  | São desenvolvidos critérios para o |
|  |  | 7.1.7.2.a, | software integrado que demonstrem |
|  | As restrições de verificação que |  | conformidade aos requisitos de software |
| 6.4.9.2.a | influenciam os requisitos, arquitetura |  | É desenvolvida e aplicada uma |
|  | ou design são identificadas | 7.1.7.2.d | estratégia de regressão para retestar o |
|  |  |  | software integrado quando uma alteração |
|  |  |  | é feita nos itens de software |
|  |  | 7.1.7.2.b, | O software integrado é verificado usando os critérios definidos |
| 6.4.9.2.c | O sistema ou elemento do sistema é |  | É desenvolvida e aplicada uma |
|  | verificado | 7.1.7.2.d | estratégia de regressão para retestar o |
|  |  |  | software integrado quando uma alteração é feita nos itens de software |
|  | Evidências objetivas de que o sistema |  |  |
| 6.4.9.2.e | construído atende aos requisitos, | 7.1.7.2.c | Resultados de teste são documentados |
|  | arquitetura e design são fornecidas |  |  |
| 6.4.9.2.f | Resultados de verificação e | 7.1.7.2.c | Resultados de teste são documentados |
|  | anomalias são identificados |  |  |
| 64.9.2g | A rastreabilidade entre os elementos |  | São desenvolvidos critérios para o |
|  | verificados do sistema é estabelecida | 7.1.7.2.a | software integrado que demonstrem |
|  |  |  | conformidade aos requisitos de software |
|  |  | 7.2.3 | Processo de Garantia de Qualidade de |
|  |  |  | Software |
| 6.4.9.2.c | O sistema ou elemento do sistema é |  | É verificada a conformidade de produtos, |
|  | verificado | 7.2.3.2.d | processos e atividades aos padrões, |
|  |  |  | procedimentos e requisitos aplicáveis |
|  |  | 7.2.4 | Processo de Verificação de Software |
|  |  | 7.2.4.2.a, | É desenvolvida e implementada uma |
|  | As restrições de verificação que |  | estratégia de verificação |
| 6.4.9.2.a | influenciam os requisitos, arquitetura |  | São identificados critérios para |
|  | ou design são identificadas | 7.2.4.2.b | verificação de todos os produtos de |
|  |  |  | trabalho de software |
| 6.4.9.2.b | Quaisquer sistemas ou serviços |  | É desenvolvida e implementada uma |
|  | habilitadores necessários para | 7.2.4.2.a | estratégia de verificação |
|  | verificação estão disponíveis |  |  |
| 6.4.9.2.c | O sistema ou elemento do sistema é | 7.2.4.2.c | São executadas as atividades de |
|  | verificado |  | verificação necessárias |
| 6.4.9.2.d | Os dados que fornecem informações | 7.2.4.2.d | Defeitos são identificados e registrados |
|  | para ações corretivas são relatados |  |  |
| 6.4.9.2.€ | Evidências objetivas de que o sistema |  | Resultados das atividades de verificação |
|  | construído atende aos requisitos, | 7.2.4.2.e | são disponibilizados para o cliente e |
|  | arquitetura e design são fornecidas |  | outras partes envolvidas |
| 6.4.9.2.f | Resultados de verificação e | 7.2.4.2.d | Defeitos são identificados e registrados |
|  | anomalias são identificados |  |  |
|  |  |  | São identificados critérios para verificação de todos os produtos de |
|  | A rastreabilidade entre os elementos | 7.2.4.2.b, |  |
| 64.9.2g | verificados do sistema é estabelecida |  | trabalho de software |
|  |  | 7.2.4.2.c | São executadas as atividades de verificação necessárias |
| 6.4.10 | Processo de Transição | 6.2.4 | Processo de Gestão de Recursos |
|  |  |  | Humanos |
| 6.4.10.2.d | Os operadores, usuários e outros stakeholders necessários à utilização |  | As habilidades da equipe são |
|  |  | 6.2.4.2.c | desenvolvidas, mantidas ou |
|  | e suporte ao sistema são treinados |  | aperfeiçoadas |
|  |  | 6.4.7 | Processo de Instalação de Software |
|  |  | 6.4.7.2.a, | Uma estratégia de instalação de software |
|  | As restrições de transição que |  | e desenvolvida |
| 6.4.10.2.a | influenciam os requisitos do sistema/ software, arquitetura ou design são |  | Critérios de instalação de software que |
|  | identificadas | 6.4.7.2.b | demonstram conformidade com os requisitos de instalação de software são |
|  |  |  | desenvolvidos |
| 6.4.10.2.b | Quaisquer sistemas ou serviços |  | A disponibilidade do produto de software |
|  | habilitadores necessários para a | 6.4.7.2.d | para uso em seu ambiente pretendido é |
|  | transição estão disponíveis |  | garantida |
| 6.4.10.2.c | O ambiente é preparado |  | A disponibilidade do produto de software |
|  |  | 6.4.7.2.d | para uso em seu ambiente pretendido é |
|  |  |  | garantida |
|  | O sistema, conforme instalado |  | A disponibilidade do produto de software |
| 6.4.10.2.d | em sua localização operacional, é | 6.4.7.2.d | para uso em seu ambiente pretendido é |
|  | capaz de entregar suas funções |  | garantida |
|  | especificadas |  |  |
| 6.4.10.2.e | Os operadores, usuários e outros stakeholders necessários à utilização |  | A disponibilidade do produto de software |
|  |  | 6.4.7.2.d | para uso em seu ambiente pretendido é |
|  | e suporte ao sistema são treinados |  | garantida |
| ABNT NBR ISO/IEC/EEE 12207:2021 e |  |  |  |
| 6.4.10.2.f | Resultados e anomalias de transição | 6.4.7.2.d | A disponibilidade do produto de software |
|  | são identificados |  | para uso em seu ambiente pretendido é |
|  |  |  | garantida |
|  |  | 6.4.7.2.c, | O produto de software é instalado no |
|  | O sistema instalado está ativado e |  | ambiente alvo |
| 6.4.10.2.g | pronto para operação |  | A disponibilidade do produto de software |
|  |  | 6.4.7.2.d | para uso em seu ambiente pretendido é |
|  |  |  | garantida |
|  |  |  | Critérios de instalação de software que |
| 6.4.10.2.h | A rastreabilidade dos elementos em | 6.4.7.2.b | demonstram conformidade com os |
|  | transição é estabelecida |  | requisitos de instalação de software são |
|  |  |  | desenvolvidos |
|  |  | 6.4.8 | Processo de Suporte na Aceitação de |
|  |  |  | Software |
|  | O sistema, conforme instalado | 6.4.8.2.a, | O produto é finalizado e entregue ao |
| 6.4.10.2.d | em sua localização operacional, é |  | adquirente |
|  | capaz de entregar suas funções | 6.4.8.2.b | Os testes de aceitação e as revisões |
|  | especificadas |  | recebem suporte |
| 6.4.10.2.e | Os operadores, usuários e outros stakeholders necessários à utilização |  | O produto entra em operação no |
|  | e suporte ao sistema são treinados | 6.4.8.2.c | ambiente do cliente |
|  | Resultados e anomalias de transição |  | Os problemas detectados durante |
| 6.4.10.2.f | são identificados | 6.4.8.2.d | a aceitação são identificados e |
|  |  |  | comunicados aos responsáveis pela |
|  |  |  | resolução |
| 6.4.10.2.g | O sistema instalado é ativado e | 6.4.8.2.c | O produto entra em operação no |
|  | pronto para operação |  | ambiente do cliente |
| 6.4.11 | Processo de Validação | 6.4.8 | Processo de Suporte na Aceitação de |
|  |  |  | Software |
|  |  | 6.4.8.2.a, | O produto é finalizado e entregue ao |
|  | A disponibilidade dos serviços |  | adquirente |
| 6.4.11.2.b | requeridos pelos stakeholders é | 6.4.8.2.b, | Os testes de aceitação e as revisões recebem suporte |
|  | confirmada |  |  |
|  |  | 6.4.8.2.c | O produto entra em operação no |
|  |  |  | ambiente do cliente |
| 6.4.11.2.d | O sistema ou elemento do sistema é | 6.4.8.2.b | Os testes de aceitação e as revisões |
|  | validado |  | recebem suporte |
|  | Resultados e anomalias de validação |  | Os problemas detectados durante |
| 6.4.11.2.f | são identificados | 6.4.8.2.d | a aceitação são identificados e |
|  |  |  | comunicados aos responsáveis pela |
|  |  |  | resolução |
|  |  | 6.4.9 | Processo de Operação de Software |
| 6.4.11.2.d | O sistema ou elemento do sistema é |  | O software é testado e é tomada uma |
|  | validado | 6.4.9.2.c | decisão para que opere em seu ambiente |
|  |  |  | pretendido |
|  |  | 7.2.5 | Processo de Validação de Software |
|  |  | 7.2.5.2.a, | É desenvolvida e implementada uma |
| 6.4.11.2.a | Os critérios de validação para os requisitos dos stakeholders são |  | estratégia de validação |
|  | definidos | 7.2.5.2.b | São identificados critérios para validação |
|  |  |  | de todos os produtos de trabalho |
|  | A disponibilidade dos serviços |  | São executadas as atividades de |
| 6.4.11.2.łąź | requeridos pelos stakeholders é | 7.2.5.2.c | validação requeridas |
|  | confirmada |  |  |
|  | Restrições de validação que | 7.2.5.2.a, | É desenvolvida e implementada uma |
| 6.4.11.2.c | influenciam os requisitos, arquitetura |  | estratégia de validação |
|  | ou design são identificadas | 7.2.5.2.b | São identificados critérios para validação |
|  |  |  | de todos os produtos de trabalho |
| 6.4.11.2.d | O sistema ou elemento do sistema é | 7.2.5.2.c | São executadas as atividades de |
|  | validado |  | validação requeridas |
|  | Todos os sistemas ou serviços |  | É desenvolvida e implementada uma |
| 6.4.11.2.e | habilitadores necessários para | 7.2.5.2.a | estratégia de validação |
|  | validação são disponibilizados |  |  |
| 6.4.11.2.f | Resultados e anomalias de validação | 7.2.5.2.d | São identificados e documentados os |
|  | são identificados |  | problemas |
|  |  |  | É fornecida evidência de que os produtos |
|  | Evidência objetiva de que o sistema | 7.2.5.2.e, | de software como foram desenvolvidos |
| 6.4.11.2.g | ou elemento do sistema desenvolvido |  | são adequados para seu uso pretendido |
|  | satisfaz as necessidades dos |  | Os resultados das atividades de |
|  | stakeholders é fornecida | 7.2.5.2.f | validação são disponibilizados para o |
|  |  |  | cliente e outras partes envolvidas |
| 6.4.11.2.h | A rastreabilidade dos elementos | 7.2.5.2.6 | São identificados critérios para validação |
|  | validados do sistema é estabelecida |  | de todos os produtos de trabalho |
| 6.4.12 | Processo de Operação | 6.4.8 | Processo de Suporte na Aceitação de |
|  |  |  | Software |
| 6.4.12.2.d | Os serviços do sistema que atendem |  | O produto entra em operação no |
|  | aos requisitos dos stakeholders são | 6.4.8.2.c | ambiente do cliente |
|  | fornecidos |  |  |
|  |  | 6.4.9 | Processo de Operação de Software |
|  | As restrições de operação que |  |  |
| 6.4.12.2.a | influenciam os requisitos de sistema/ | 6.4.9.2.a | A estratégia de operação é definida |
|  | software, arquitetura ou design são |  |  |
|  | identificadas |  |  |
| 6.4.12.2.b | Todos os sistemas e serviços |  | As condições para a operação correta |
|  | habilitadores e materiais necessários para a operação estão disponíveis | 6.4.9.2.b | do software no ambiente pretendido são |
|  |  |  | identificadas e avaliadas |
| 6.4.12.2.e | O desempenho do sistema durante a | 6.4.9.2.b | As condições para a operação correta |
|  | operação é monitorado |  | do software no ambiente pretendido são |
|  |  |  | identificadas e avaliadas |
| 6.4.12.2.d | Os serviços do sistema que atendem | 6.4.9.2.d | O software é operado no ambiente |
|  | aos requisitos dos stakeholders são |  | pretendido |
|  | fornecidos |  |  |
| 6.4.12.2.f | O suporte ao cliente é fornecido |  | Assistência e consultoria são fornecidas |
|  |  | 6.4.9.2.e | para os clientes do produto de software, |
|  |  |  | de acordo com o acordo |
| 6.4.13 | Processo de Manutenção | 6.4.10 | Processo de Manutenção de Software |
|  |  |  | Uma estratégia de manutenção é |
|  | As restrições de manutenção | 6.4.10.2.a, | desenvolvida para administrar a |
|  | que influenciam os requisitos, a |  | modificação e migração de produtos de |
| 6.4.13.2.a | arquitetura ou o design do sistema |  | acordo com a estratégia de liberação |
|  | são identificadas | 6.4.10.2.b | O impacto de mudanças feitas em um sistema existente em organizações, |
|  |  |  | operações ou interfaces é identificado |
|  |  |  | Os produtos modificados são |
|  | Todos os sistemas ou serviços | 6.4.10.2.d, | desenvolvidos com testes associados |
| 6.4.13.2.łął | habilitadores necessários para |  | que demonstrem que os requisitos não |
|  | manutenção são disponibilizados |  | foram comprometidos |
|  |  | 6.4.10.2.e | As atualizações do produto são feitas no ambiente do cliente |
|  |  |  | A documentação do software sistema |
|  |  | 6.4.10.c, | afetado é atualizada conforme |
|  |  |  | necessário |
|  |  |  | Os produtos modificados são |
|  | Elementos de sistema substituídos, | 6.4.10.d, | desenvolvidos com testes associados |
| 6.4.13.2.ćł | reparados ou revisados são |  | que demonstrem que os requisitos não |
|  | disponibilizados |  | foram comprometidos |
|  |  | 6.4.10.e, | As atualizações do produto são feitas no |
|  |  |  | ambiente do cliente |
|  |  | 6.4.10.f | A modificação do software de sistema é |
|  |  |  | comunicada a todas as partes afetadas |
| 6.4.13.2.d | As necessidades de alterações para |  | O impacto de mudanças feitas em um sistema existente em organizações, |
|  | tratar manutenção corretiva, de melhoria ou adaptativa são relatadas | 6.4.10.2.b |  |
|  |  |  | operações ou interfaces é identificado |
| 6.4.13.2.e | Dados de falhas e de tempo de vida, |  | O impacto de mudanças feitas em um |
|  | incluindo custos associados, são | 6.4.10.2.b | sistema existente em organizações, |
|  | determinados |  | operações ou interfaces é identificado |
|  |  | 7.3.1 | Processo de Engenharia de Domínio |
|  | Elementos de sistema substituídos, |  | Os ativos pertencentes ao domínio são |
| 6.4.13.2.c | reparados ou revisados são | 7.3.1.2.f | adquiridos, desenvolvidos e mantidos |
|  | disponibilizados |  | durante os seus ciclos de vida |
| 6.4.14 | Processo de Desativação | 6.4.11 | Processo de Desativação de Software |
|  | As restrições de desativação são | 6.4.11.2.a, | Define-se uma estratégia de desativação |
|  | fornecidas como entradas para |  | de software |
| 6.4.14.2.a | requisitos, arquitetura, design e |  | As restrições de desativação são |
|  | implementação | 6.4.11.2.b | fornecidas como dados de entrada para |
|  |  |  | os requisitos |
|  | Todos os sistemas ou serviços | 6.4.11.2.a, | Define-se uma estratégia de desativação de software |
| 6.4.14.2.b | habilitadores necessários para a |  |  |
|  | desativação são disponibilizados | 6.4.11.2.c | Os elementos de software do sistema |
|  |  |  | são destruídos ou armazenados |
|  | Os elementos do sistema ou |  |  |
|  | produtos residuais são armazenados, |  | Os elementos de software do sistema |
| 6.4.14.2.c | recuperados, reciclados ou destruídos | 6.4.11.2.c |  |
|  | de acordo com os requisitos, por |  | são destruídos ou armazenados |
|  | exemplo, requisitos de segurança e |  |  |
|  | proteção |  |  |
|  | O ambiente é retornado ao estado |  | O ambiente é deixado no estado |
| 6.4.14.2.d | original ou a um estado previamente | 6.4.11.2.d | combinado |
|  | acordado |  |  |
|  |  |  | Registros que permitam a retenção de |
| 6.4.14.2.e | Registros de ações e análises de | 6.4.11.2.e | conhecimento das ações de desativação |
|  | desativação são disponibilizados |  | e análise de impactos a longo termo são |
|  |  |  | disponibilizados |



## Bibliografia

[1] ANSI/AIAA G-043A-2012e, ANSI/AIAA Guide to the Preparation of Operational Concept Documents

IEC 61508:2010 (all parts), Functional safety of electrical/electronic/programmable electronic safety-related systems

[3] IEEE Std 1012™-2012, IEEE Standard for System and Software Verification and Validation

[4] IEEE Std 1062™-2015, IEEE Recomended Practice for Software Acquisition

[5] IEEE Std 730™-2014, IEEE Standard for Software Quality Assurance Processes

[6] IEEE Std 828™-2012, IEEE Standard for Configuration Management in Systems and Software Engineering

INCOSE TP-2003-020-01, Technical Measurement

INCOSE.2015. Systems Engineering Handbook: A Guide for System Life Cycle Processes and Activities, version 4.0. Hoboken, NJ, USA: John Wiley and Sons, Inc., ISBN: 978-1-118-99940-0

[9] ABNT NBR ISO 10004:2013, Gestão da qualidade - Satisfação do cliente - Diretrizes para monitoração e medição

[10] ABNT NBR ISO 10007:2005, Sistemas de gestão da qualidade - Diretrizes para gestão de contiguração

[11] ABNT NBR ISO 14001:2015, Sistemas de gestão ambiental - Requisitos com orientações para uSo

[12] ISO 15704:2000, Industrial automation systems - Requirements for enterprise-reference architectures and methodologies

[13] ABNT NBR ISO 31000:2009, Gestão de Riscos - Diretrizes

[14] ABNT NBR ISO 9000:2015, Sistemas de gestão da qualidade - Fundamentos e vocabulário

[15] ABNT NBR ISO 9001:2015, Sistemas de gestão da qualidade - Requisitos

[16] ABNT NBR ISO 9004:2010, Gestão para o sucesso sustentado de uma organização - Uma abordagem da gestão da qualidade

[17] ABNT NBR ISO 9241-210:2011, Ergonomia da interação humano-sistema - Parte 210: Projeto centrado no ser humano para sistemas interativos

[18] ABNT ISO Guia 73:2009, Gestão de riscos - Vocabulário

[19] ISO 9241-220:2019, Ergonomics of human-system interaction - Part 220: Processes for enabling, executing and assessing human-centred design within organizations

[20] ISO TS 18152:2010, Ergonomics of human-system interaction - Specification for the process assessment of human-system issues

ABNT NBR ISO/EC/IEEE 12207:2021

[21] ISO/IEC 10746-3:2009, Information technology - Open distributed processing - Reference model: Architecture

[22] ISO/IEC 15026-3:2011, System and software engineering - Systems and software assurance - Part 3: System integrity levels

[23] ISO/EC 15026-4:2012, Systems and software engineering - Systems and software assurance - Part 4: Assurance in the life cycle

[24] ABNT NBR ISO/IEC 15939:2009, Engenharia de sistemas e de software - Processo de medição

[25] ISO/EC 16085:2006, System and Software Engineering - Life Cycle Management - Risk Management

[26] ISO/IEC 16350:2015, Information technology - Systems and software engineering - Application management

[27] ISO/IEC 19770-1:2012, Information technology - Software asset management- Part 1: Processes and tiered assessment of conformance

[28] ABNT NBR ISO/IEC 20000-1:2011, Tecnologia da informação - Gestão de serviços

[29] ISO/IEC 25010:2011, Systems and software engineering - Systems and software Quality Requirements and Evaluation (SQuaRE) - System and software quality models

[30] ABNT NBR ISO/IEC 25030:2008, Engenharia de software - Requisitos e avaliação da qualidade de produto de software (SQuaRE) - Requisitos de qualidade

[31] ISO/IEC 25063:2014, Systems and software engineering - Systems and software product Quality Requirements and Evaluation (SQuaRE) - Common Industry Format (CIF) for usability: Context of use description

[32] ISO/IEC 26550:2013, Software and systems engineering - Reference model for product line engineering and management

[33] ISO/IEC 27000:2016, Information technology - Security techniques - Information security management systems - Overview and vocabulary

[34] ISO/IEC 27036 (all parts), Information technology - Security techniques - Information security for supplier relationships

[35] ISO/IEC 33001:2015, Information technology - Process assessment - Concepts and terminology

[36] ISO/IEC 33002:2015, Information technology - Process assessment- Requirement for performing process assessment

[37] ISO/IEC 33004:2015, Information technology - Process assessment - Requirement for process reference, process assessment, and maturity models

[38] ISO/IEC 33020:2015, Information technology - Process assessment - Process measurement framework for assessment of process capability

[39] ISO/IEC TR 19759:2015, Guide to the Software Engineering Body of Knowledge (SWEBOK) V3, IEEE Computer Society, 2014

[40] ISO/IEC TR 24748-2:2011, Systems and software engineering - Life cycle management - Part 2: Guide to the application of ISO/IEC 15288 (System life cycle processes)

[41] ISO/EC TR 24748-3:2011, Systems and software engineering - Life cycle management - Part 3: Guide to the application of ISO/IEC 12207 (Software life cycle processes)

[42] ABNT ISO/IEC TR 24774:20101, Engenharia de software e de sistemas - Gerenciamento de cicio de vida - Orientações para descrição de processos

[43] ISO/IEC TR 25060:2010, Systems and software engineering - Systems and software product Quality Requirements and Evaluation (SQuaRE) - Common Industry Format (CIF) for usability: General framework for usability-related information

[44] ISO/IEC TS 24748-1:2016, Systems and software engineering - Life cycle management - Part 1: Guide for life cycle management

[45] ISO/IEC/IEEE 14764:2006, Software Engineering - Software Life Cycle Processes - Maintenance

[46] ISO/IEC/IEEE 15288:2015, Systems and software engineering - System life cycle processes

[47] ISO/EC/IEEE 15289:2015, Systems and software engineering - Content of life-cycle information products (documentation)

[48] ABNT NBR ISO/IEC/IEEE 16326:2012, Engenharia de sistemas e de software - Processos de ciclo de vida - Gerenciamento de projeto

[49] ISO/IEC/IEEE 24748-4:2016, Systems engineering - Life cycle management - Part 4: Application and management of the systems engineering process

[50] ISO/|EC/IEEE 24748-5, Systems and software engineering - Life cycle management - Part 5: Software development planning

[51] ISO/IEC/IEEE 24765, Systems and software engineering - Vocabulary www.computer.org/sevocab

[52] ISO/IEC/IEEE 26515:2011, Systems and software engineering: Developing user documentation in an agile environment

[53] ISO/IEC/IEEE 26531:2015, Systems and software engineering - Content management for product life-cycle, user, and service management documentation

[54] ISO/IEC/IEEE 29119 (all parts), Systems and software engineering - Software testing

[55] SO/EC/EEE 29148:2011, Systems and software engineering - Life cycle processes - Requirements engineering

A versão eletrônica desta Norma pode ser baixada gratuitamente do website do ISO/IEC Information Technology Task Force (ITTF).

[56] ISO/|EC/IEEE 42010:2011, Systems and software engineering - Architecture description

[57] NATO AEP-67, Engineering for System Assurance in NATO Programs

[58] PMI Practice Standard for Work Breakdown Structures-Second Edition

[59] SAE ANSI/EIA 649B, Configuration Management Standard
