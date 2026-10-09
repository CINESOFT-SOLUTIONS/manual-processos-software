# Parte 3 – Processos de Gerenciamento Técnico (pré-avaliação)

Este arquivo contém a Parte 3 gerada separadamente para pré-avaliação, antes da incorporação ao Manual de Processos de Software. Ele tem dois blocos:

- **Bloco A – Validação da sugestão de IA**: análise da tabela sugerida contra a ISO/IEC/IEEE 12207 (6.3) e correções aplicadas. Não entra no manual.
- **Bloco B – Texto proposto da Parte 3**: texto pronto para incorporação ao manual após aprovação do grupo.

---

# Bloco A – Validação da sugestão de IA

## A.1 O que foi validado

A sugestão de IA para a Parte 3 previa os elementos Escopo, Cronograma, Recursos e Entregas (todos da atividade de planejamento) e o seguinte índice: 3.1 Planejamento do Projeto, 3.2 Gestão de Riscos, 3.3 Gestão de Configuração, 3.4 Gestão de Decisões Técnicas (ADRs), 3.5 Medição e Avaliação/Controle do Projeto.

## A.2 Conformidade com a ISO/IEC/IEEE 12207 – 6.3

A ISO/IEC/IEEE 12207 define, no grupo 6.3 (Technical management processes), sete processos:

| Processo da norma | Clause | Na sugestão de IA |
|---|---|---|
| Project planning | 6.3.1 | 3.1 (parcialmente) |
| Project assessment and control | 6.3.2 | fundido em 3.5 |
| Decision management | 6.3.3 | 3.4 (ADRs) |
| Risk management | 6.3.4 | 3.2 |
| Configuration management | 6.3.5 | 3.3 |
| Information management | 6.3.6 | **ausente** |
| Measurement | 6.3.7 | fundido em 3.5 |

## A.3 Constatações e correções aplicadas

1. **Lacuna: Information management (6.3.6) estava ausente.** O processo é parte obrigatória do grupo 6.3 e já é anticipado pelo próprio manual (as seções 1.1, 2.5 e 2.6 referenciam "gestão da informação" como conteúdo futuro) e pelo PDW (seção 24 define documentos controlados e regras). Foi criada a seção 3.6.
2. **Medição e Avaliação/Controle estavam fundidas em um único item.** A norma trata 6.3.2 (avaliação e controle do projeto) e 6.3.7 (medição) como processos distintos, com resultados de entrada e saída diferentes: a medição fornece dados; a avaliação e o controle decide e age. Foram separados em 3.2 (6.3.2) e 3.7 (6.3.7).
3. **ADRs são mecanismo adequado, mas não esgotam 6.3.3.** Decision management cobre a definição e o registro de decisões em geral; no CineDoom, decisões técnicas/arquiteturais usam ADR (PDW 26), enquanto decisões de escopo seguem GP + representante do cliente (PDW 43) e são registradas no registro de mudanças (PDW 22). A seção 3.4 explicita essa divisão.
4. **Os quatro elementos da tabela (escopo, cronograma, recursos, entregas) são corretos e insuficientes.** Eles cobrem apenas parte dos resultados de 6.3.1. O planejamento também precisa tratar comprometimento das partes interessadas e necessidades de informação, tratados em 3.1.5 e 3.6.
5. **Numeração reordenada conforme a norma.** O índice 3.1–3.5 da sugestão foi reordenado para 1:1 com as cláusulas 6.3.1 a 6.3.7, facilitando auditoria de aderência.
6. **Terminologia.** O manual (Considerações Finais) usou "gerência técnica"; a seção de cabeçalho da Parte 3 usa "Gerenciamento Técnico". Recomenda-se adotar "Gerenciamento Técnico" em todo o manual (padrão ABNT) e corrigir a menção nas Considerações Finais ao consolidar esta parte.

## A.4 Conteúdo aproveitado das bases existentes

| Seção da Parte 3 | Origem |
|---|---|
| Escopo e exclusões | Manual 0.3–0.4; PDW 5, 7, 46.1 |
| Incrementos e critério de conclusão | Manual 2.1; PDW 14.1–14.3 |
| Cronograma (estrutura) | PDW 15.1 (datas em aberto) |
| Recursos | Manual 2.2, 2.4; PDW 15.2–15.3, 16, 17 |
| Entregas e aceite | Manual 1.2; PDW 13.2, 38 |
| Riscos | PDW 23.1–23.4 |
| Configuração e mudanças | PDW 21, 22, 37 |
| Decisões (ADR) | PDW 26, 43 |
| Informação | PDW 24 |
| Medição | PDW 19.3–19.4, 36 |

---

# Bloco B – Texto proposto da Parte 3

# Parte 3 – Processos de Gerenciamento Técnico

Os processos de gerenciamento técnico (ISO/IEC/IEEE 12207 – 6.3) planejam o projeto, avaliam e controlam seu andamento, gerenciam decisões, riscos, configuração, informação e medição. Esta parte cobre exclusivamente o grupo 6.3; os processos técnicos (6.4) — requisitos, arquitetura, implementação, verificação, validação, implantação, operação e manutenção — serão tratados nas partes seguintes do manual.

A responsabilidade pela execução destes processos é do Gerente de Projeto, com as atribuições definidas na matriz RACI (seção 2.4). Os papéis podem ser exercidos de forma acumulada, conforme registrado naquela seção.

| Processo deste manual | ISO/IEC/IEEE 12207 |
|---|---|
| 3.1 Planejamento do Projeto | 6.3.1 |
| 3.2 Avaliação e Controle do Projeto | 6.3.2 |
| 3.3 Gestão de Decisões Técnicas | 6.3.3 |
| 3.4 Gestão de Riscos | 6.3.4 |
| 3.5 Gestão de Configuração | 6.3.5 |
| 3.6 Gestão da Informação | 6.3.6 |
| 3.7 Medição | 6.3.7 |

## 3.1. Planejamento do Projeto

O planejamento (ISO/IEC/IEEE 12207 – 6.3.1) estabelece o contexto do projeto, suas estimativas, cronograma, organização, recursos, riscos iniciais e necessidades de informação. O produto do processo é o **Plano de Projeto**, documento controlado (seção 3.6) mantido pelo Gerente de Projeto e revisado ao final de cada incremento.

### 3.1.1. Escopo do projeto

O escopo do projeto é desenvolver, verificar, validar, implantar e colocar em operação a primeira versão do CineDoom, com o alcance funcional definido na seção 0.3 e as exclusões definidas na seção 0.4. Toda inclusão de funcionalidade fora do escopo inicial depende de análise de mudança formal (seção 3.5.3 e PDW, seções 5.1 e 46.1).

O escopo é decomposto por incremento, conforme o modelo de ciclo de vida incremental (seção 2.1 e PDW, seção 14.2):

| Incremento | Escopo funcional | Requisitos |
|---|---|---|
| 1 | Autenticação, usuários, filmes e salas | RF-01, RF-02, RF-03, RF-04 |
| 2 | Sessões, assentos e disponibilidade | RF-05, RF-06 |
| 3 | Venda, cancelamento e auditoria | RF-07, RF-08, RF-12 |
| 4 | Clientes e registros de interesse | RF-09, RF-10 |
| 5 | Relatórios, refinamentos e preparação para produção | RF-11 |

### 3.1.2. Cronograma

O cronograma do projeto planeja **como** cada incremento será entregue: define o percurso do incremento pelas etapas do modelo de ciclo de vida (requisito, design, implementação, teste e release — seção 2.1), a ordem entre os incrementos e o ponto de encerramento de cada um. Até que o grupo decida as datas (PDW, seção 15.1; decisão em aberto 4 das Considerações Finais), o cronograma é definido pela sua **lógica** — sequência de etapas e dependências — e não pelo calendário; as datas de início, término e duração serão registradas nesta seção quando decididas, observando as restrições de prazo, capacidade da equipe, orçamento controlado e escopo inicial limitado (PDW, seção 15.3).

#### Etapas de cada incremento

Todo incremento percorre as cinco etapas do modelo incremental (seção 2.1), produzindo funcionalidade executável ao término:

| Etapa | Resultado esperado |
|---|---|
| Requisito | Requisitos do incremento detalhados e com critérios de aceite (seção 0.3) |
| Design | Decisões de arquitetura e design do incremento, com ADRs quando aplicável (seção 3.3) |
| Implementação | Código implementado, revisado e integrado (seção 2.2) |
| Teste | Testes executados, defeitos registrados e críticos corrigidos (seção 3.1.4) |
| Release | Versão do incremento liberada e identificada por tag (seção 3.5.2) |

#### Marcos de revisão (M1–M5)

O marco de revisão **não é uma data**: é o **evento de encerramento** do incremento correspondente, definido por critérios de entrada e saída:

- **Entrada (quando pode ser avaliado):** as cinco etapas do incremento foram executadas.
- **Saída (quando é considerado atingido):** os critérios de conclusão foram verificados (seção 3.1.4 e PDW, seção 14.3), a auditoria de conformidade foi realizada (seção 2.5) e a revisão de lições aprendidas foi concluída (seção 2.6).

Atingido o marco, o incremento é considerado concluído e o incremento seguinte pode iniciar, respeitando as dependências abaixo. A aprovação da conclusão é do Gerente de Projeto, com participação do Analista de Qualidade (RACI, seção 2.4).

#### Sequência e dependências entre incrementos

| Marco | Incremento | Conteúdo | Dependência técnica | Data |
|---|---|---|---|---|
| M1 | 1 | Autenticação, usuários, filmes e salas | Nenhuma | Em aberto (PDW 15.1) |
| M2 | 2 | Sessões, assentos e disponibilidade | Depende de filmes e salas (M1) | Em aberto (PDW 15.1) |
| M3 | 3 | Venda, cancelamento e auditoria | Depende de sessões e assentos (M2) | Em aberto (PDW 15.1) |
| M4 | 4 | Clientes e interesses | Depende de filmes (M1) | Em aberto (PDW 15.1) |
| M5 | 5 | Relatórios, refinamentos e produção | Depende de M1 a M4 | Em aberto (PDW 15.1) |

### 3.1.3. Recursos

| Categoria | Composição | Referência |
|---|---|---|
| Humanos | Papéis do Gerente de Projeto, Analista de Requisitos, Arquiteto, Desenvolvedores Frontend e Backend, Engenheiro de Testes, DevOps, Analista de Qualidade e Suporte, com atribuições conforme a matriz RACI | Seção 2.4; PDW 16 e 17 |
| Infraestrutura | Ambientes de desenvolvimento, testes, homologação e produção | [Seção 2.2](#22-gestão-da-infraestrutura) |
| Ferramentas | Git/GitHub, GitHub Projects, Visual Studio Code, ferramenta de modelagem UML, GitHub Actions | Seção 2.2 |
| Serviços contratados | Computação e banco de dados na AWS, monitoramento, backup e gateway de pagamento (Stripe), conforme justificativas de aquisição | Seção 1.1 |
| Restrições | Prazo do semestre, equipe enxuta com sobreposição de papéis, orçamento controlado | Seção 2.4; PDW 15.3 |

Horas de equipe, orçamento e licenças não estão dimensionados (PDW, seção 15.2) e permanecem em aberto; o planejamento atual é conduzido por incremento e por capacidade da equipe, e não por carga horária nominal.

### 3.1.4. Entregas e critérios de conclusão de incremento

Cada incremento entrega, obrigatoriamente:

- Funcionalidade executável e liberada (release identificada por tag de versão, seção 3.5.2).
- Requisitos e artefatos de arquitetura atualizados e rastreados, mencionada na seção 0.3.
- Relatório de testes do incremento, com registro de defeitos.
- Documentação técnica atualizada.
- Registro de configuração atualizado (seção 3.5).
- Registro de lições aprendidas (seção 2.6).

Um incremento só é considerado concluído quando os critérios estiverem atendidos: requisitos do incremento implementados, verificação concluída, testes executados, defeitos críticos corrigidos, documentação atualizada e revisão de qualidade realizada. A aprovação interna da conclusão é do Gerente de Projeto, com o Analista de Qualidade e o Engenheiro de Testes como responsáveis pelas verificações (RACI, seção 2.4).

O aceite do produto pelo cliente, com os entregáveis contratuais (ambiente configurado, relatório de testes, manuais, registro de versão e orientação inicial), ocorre ao final do incremento 5, conforme a seção 1.2; não há aceite formal do cliente por incremento intermediário.

### 3.1.5. Comprometimento e comunicação

O Gerente de Projeto mantém a comunicação com os stakeholders internos (diretoria e equipe) e com o representante do cliente para decisões de escopo (PDW, seção 43). Reuniões de acompanhamento ocorrem a cada revisão de incremento e sempre que houver desvio relevante de escopo, prazo, custo ou risco.

## 3.2. Avaliação e Controle do Projeto

A avaliação e o controle (ISO/IEC/IEEE 12207 – 6.3.2) tornam o andamento do projeto transparente, permitem avaliar o desempenho em relação ao plano e gerenciar ações corretivas e preventivas.

### 3.2.1. Pontos de controle e relatórios

| Ponto de controle | Conteúdo avaliado | Responsável |
|---|---|---|
| Fim de cada etapa do incremento (requisito, design, implementação, teste) | Situação da etapa, requisitos e defeitos em aberto | Papel líder da etapa (RACI, seção 2.4) |
| Fim de cada incremento (M1–M5) | Conclusão conforme critérios de 3.1.4, métricas de 3.7, riscos de 3.4, ações corretivas | Gerente de Projeto e Analista de Qualidade |
| Sempre que houver desvio relevante | Impacto em escopo, prazo, recursos e riscos | Gerente de Projeto |

O relatório de status por incremento compõe a informação de gestão da seção 3.6 e é a base para o replanejamento. O acompanhamento usa as métricas de 3.7; valores fora da meta geram não conformidade registrada e ação corretiva (seção 2.5).

### 3.2.2. Ações corretivas, preventivas e replanejamento

Desvios identificados originam ações corretivas ou preventivas registradas, com responsável e prazo, acompanhadas até o encerramento. Mudanças de escopo, prazo ou arquitetura que alterem o plano aprovado só são incorporadas após o processo de mudança da seção 3.5.3. O replanejamento é aprovado pelo Gerente de Projeto; decisões que afetem escopo ou contrato exigem o representante do cliente (PDW, seção 43).

## 3.3. Gestão de Decisões Técnicas

A gestão de decisões (ISO/IEC/IEEE 12207 – 6.3.3) garante que alternativas sejam identificadas, avaliadas e registradas antes da implementação. No CineDoom, adotam-se dois registros, conforme a natureza da decisão:

- **ADRs (Architecture Decision Records)** – decisões técnicas e arquiteturais; autoridade: Arquiteto e equipe técnica.
- **Registro de mudanças** – decisões de escopo, contrato e iterações do plano; autoridade: Gerente de Projeto e representante do cliente.

### 3.3.1. Política de registro de ADRs

Toda decisão técnica relevante é registrada por ADR contendo, no mínimo: contexto, problema, alternativas avaliadas, decisão, consequências, data e responsável.

São registradas como ADR as decisões que afetam arquitetura, stack tecnológica, modelo de dados, segurança, estratégia de implantação ou integração com serviços externos. Os ADRs são documentos controlados (seção 3.6), versionados no repositório Git junto ao código e aos diagramas (itens de configuração, seção 3.x.1). ADRs incorporados só são revogados por novo ADR que explicitamente os substitua.

### 3.3.2. ADRs previstos

| ADR | Decisão | Status |
|---|---|---|
| ADR-001 | Arquitetura de monólito modular | Decidida (PDW 10.1; registro formal pendente) |
| ADR-002 | Frontend em React | Decidida (PDW 10.3; registro formal pendente) |
| ADR-003 | Backend em Node.js | Decidida (PDW 10.4; registro formal pendente) |
| ADR-004 | Banco de dados PostgreSQL | Decidida (PDW 10.5; registro formal pendente) |
| ADR-005 | Infraestrutura na AWS | Decidida (PDW 11.1; registro formal pendente) |
| ADR-006 | API REST versionada | Decidida (PDW 10.6–10.7; registro formal pendente) |
| ADR-007 | Estratégia de autenticação e controle de sessão | A decidir no incremento 1 |

## 3.4. Gestão de Riscos

A gestão de riscos (ISO/IEC/IEEE 12207 – 6.3.4) identifica, analisa, planeja respostas e acompanha riscos ao longo do projeto, com revisão ao final de cada incremento.

### 3.4.1. Abordagem e critérios

Riscos são classificados por probabilidade (Baixa, Média, Alta) e impacto (Baixo, Médio, Alto). A combinação define a criticidade, que orienta a prioridade de tratamento: riscos de criticidade alta exigem plano de mitigação e, quando aplicável, plano de contingência; riscos de criticidade média exigem monitoramento e plano de mitigação; riscos de criticidade baixa são monitorados.

### 3.4.2. Registro de riscos

Cada risco é registrado com os campos do PDW (seção 23.4): identificador, descrição, causa, consequência, probabilidade, impacto, exposição, responsável, mitigação, plano de contingência, status e categoria (técnico, organizacional ou de negócio, conforme PDW 23.1–23.3).

Registro inicial de riscos (proposta sujeita a aprovação do grupo):

| ID | Risco | Categoria | Prob. | Impacto | Mitigação | Responsável | Status |
|---|---|---|---|---|---|---|---|
| R-01 | Indisponibilidade do provedor de nuvem (AWS) | Técnico | Baixa | Alto | SLA contratado, monitoramento (seção 2.2), backup e plano de recuperação | DevOps | Em análise |
| R-02 | Erro de integração com o gateway de pagamento (Stripe) | Técnico | Média | Alto | Integração incremental no incremento 3, testes de integração, homologação no ambiente do fornecedor | Arquiteto | Em análise |
| R-03 | Vulnerabilidade de segurança com exposição de dados de clientes | Técnico | Média | Alto | HTTPS, hash de senhas, controle de acesso por perfil, revisão de segurança preventiva | Arquiteto | Em análise |
| R-04 | Perda ou corrupção de dados | Técnico | Baixa | Alto | Backup diário, RTO de até 4 h e RPO de até 24 h (sujeitos a aprovação), testes de restauração | DevOps | Em análise |
| R-05 | Desempenho abaixo das metas (2 s; 100 usuários simultâneos) | Técnico | Média | Médio | Testes de desempenho por incremento, revisão de consultas e indexes | Arquiteto | Em análise |
| R-06 | Rotatividade ou indisponibilidade de membros da equipe | Organizacional | Média | Alto | Sobreposição de papéis registrada (seção 2.4), documentação e ADRs (seção 3.3), onboarding (seção 2.6) | Gerente de Projeto | Em análise |
| R-07 | Atrasos por indefinição de cronograma e decisões em aberto | Organizacional | Alta | Médio | Fechamento das decisões em aberto do PDW (seção 47) como prioridade de governança | Gerente de Projeto | Em análise |
| R-08 | Mudança de escopo sem controle | Organizacional | Média | Médio | Regra de expansão do PDW (seção 5.1) e processo de mudança (seção 3.5.3) | Gerente de Projeto | Em análise |
| R-09 | Baixa adesão do mercado-alvo ao produto | Negócio | Média | Alto | Validação com clientes na homologação, indicadores de portfólio (seção 2.3) | Diretoria | Em análise |
| R-10 | Custo operacional de nuvem maior que o previsto | Negócio | Média | Médio | Monitoramento de consumo, dimensionamento inicial modesto, revisão por incremento | DevOps | Em análise |
| R-11 | Dependência de fornecedor (AWS, Stripe) | Negócio | Baixa | Médio | Critérios de portabilidade e avaliação de dependência na seleção (seção 1.1) | Gerente de Projeto | Em análise |

## 3.5. Gestão de Configuração

A gestão de configuração (ISO/IEC/IEEE 12207 – 6.3.5) identifica e controla os itens de configuração, as mudanças e a integridade das linhas de base ao longo do projeto.

### 3.3.1. Itens de configuração e linhas de base

São itens de configuração: código-fonte, requisitos, arquitetura e diagramas, ADRs, casos de teste e relatórios de teste, scripts de infraestrutura, documentação técnica e do usuário, configurações relevantes e releases.

> [!WARNING]
> Linhas de base (proposta, sujeita a aprovação):

| Linha de base | Conteúdo | Momento |
|---|---|---|
| Requisitos | RF e RNF do incremento, com critérios de aceite | Ao conclusão da etapa de requisito de cada incremento |
| Arquitetura | Diagramas e ADRs vigentes | Ao conclusão da etapa de design de cada incremento |
| Release | Tag de versão com código, testes e documentação do incremento | Na liberação de cada incremento (M1–M5) |

### 3.3.2. Controle de versão

O controle de versão usa Git com repositório remoto no GitHub (seção 2.2), com as seguintes regras:

- Branch `main` contém o código liberado; `develop` concentra o trabalho do incremento em andamento; branches de funcionalidade são criadas a partir de `develop` com identificação do requisito (ex.: `feature/RF-07-venda`).
- Integrações ocorrem por pull request, com revisão de código obrigatória antes da mesclagem.
- Cada incremento concluído é marcado por tag de versão conforme versionamento semântico: incrementos 1 a 4 correspondem a versões internas `0.x.y`; a primeira versão liberada ao cliente, ao final do incremento 5, é `1.0.0`.
- Toda release possui notas de versão e registro de alterações.

### 3.5.3. Controle de mudanças e auditorias de configuração

Mudanças em itens de configuração seguem o processo definido: registrar solicitação, classificar, avaliar impacto, estimar esforço, avaliar riscos, aprovar ou rejeitar, planejar, implementar, testar, atualizar documentação e encerrar. Nenhum item de configuração é alterado sem solicitação registrada.

Auditorias de configuração são executadas ao final de cada incremento, junto à auditoria de conformidade (seção 2.5), e verificam: identificação, versão e status de todos os itens de configuração; correspondência entre tags de release e linhas de base; e integridade dos ADRs em relação ao código implantado.

## 3.6. Gestão da Informação

A gestão da informação (ISO/IEC/IEEE 12207 – 6.3.6) planeja a coleta, o armazenamento, o controle e a distribuição da informação do projeto, garantindo que cada parte interessada receba a informação necessária, na versão correta.

### 3.6.1. Documentos controlados

São documentos controlados (PDW, seção 24.1): este manual, requisitos, arquitetura e diagramas, ADRs, plano de projeto, plano de testes, casos de teste, relatórios (status, teste, aceite), registros de risco, registros de mudança, registro de configuração, registros de qualidade e lições aprendidas.

Cada documento controlado possui identificação, responsável, versão, data, status e histórico de alterações (PDW, seção 24.2).

### 3.6.2. Armazenamento, controle e distribuição

| Informação | Armazenamento | Acesso |
|---|---|---|
| Código, documentação técnica, ADRs, diagramas, casos de teste | Repositório Git (GitHub) | Equipe técnica |
| Plano de projeto, status, registros de risco e mudança | Repositório Git ou GitHub Projects | Equipe e diretoria |
| Registros de qualidade e auditorias | Ferramenta de gestão da qualidade da equipe | QA, GP, diretoria |
| Chamados e atendimento ao cliente | Sistema de gestão de chamados | Suporte, cliente |

A informação distribuída fora da equipe (relatórios de status ao cliente, notas de versão) é gerada sempre a partir da versão controlada do documento. A preservação e o compartilhamento do conhecimento derivado desses documentos são tratados pela gestão do conhecimento (seção 2.6).

## 3.7. Medição

A medição (ISO/IEC/IEEE 12207 – 6.3.7) fornece os dados que sustentam a avaliação do projeto (seção 3.2), a gestão da qualidade (seção 2.5) e a melhoria dos processos. O plano de medição define, para cada métrica, nome, objetivo, fórmula, fonte, responsável, frequência, meta e ação quando fora da meta (PDW, seção 36.4).

### 3.7.1. Métricas do projeto

| Métrica | Fórmula (proposta) | Fonte | Responsável | Frequência | Meta |
|---|---|---|---|---|---|
| Progresso do cronograma | Marcos concluídos ÷ marcos previstos × 100 | Plano de projeto | GP | Por incremento | Conforme cronograma (em aberto, PDW 15.1) |
| Cumprimento das etapas do incremento | Etapas concluídas no prazo ÷ etapas previstas × 100 | Plano de projeto | GP | Por incremento | A definir |
| Retrabalho | Esforço de correção ÷ esforço total × 100 | Registros de tarefas | GP | Por incremento | A definir |

### 3.7.2. Métricas de produto

| Métrica | Fórmula (proposta) | Fonte | Responsável | Frequência | Meta |
|---|---|---|---|---|---|
| Requisitos com rastreabilidade | RF com cadeia completa ÷ total de RF × 100 | Matriz de rastreabilidade | AR | Por incremento | 100% (PDW 19.4) |
| Cobertura de testes (componentes críticos) | Casos de teste executados ÷ casos previstos no plano × 100 | Plano e relatório de testes | Engenheiro de Testes | Por incremento | ≥ 80% (PDW 19.4) |
| Defeitos críticos no aceite | Contagem de defeitos de severidade crítica | Registro de defeitos | QA | No aceite | Zero (PDW 19.4) |
| Requisitos críticos validados | RF críticos validados ÷ total de RF críticos × 100 | Evidências de validação | QA | No aceite | 100% (PDW 19.4) |
| Defeitos por severidade | Contagem por severidade | Registro de defeitos | Engenheiro de Testes | Por incremento | Monitorar |
| Defeitos reabertos | Reabertos ÷ resolvidos × 100 | Registro de defeitos | Engenheiro de Testes | Por incremento | A definir |
| Tempo de correção | Média (resolução − abertura) em dias | Registro de defeitos | Engenheiro de Testes | Por incremento | A definir |
| Disponibilidade em produção | Tempo disponível ÷ tempo medido × 100 | Monitoramento (CloudWatch) | DevOps | Mensal | 95% (seção 0.4; janela de medição em aberto, PDW 9.2) |

### 3.7.3. Uso dos resultados

Resultados fora da meta geram não conformidade registrada e ação corretiva ou preventiva (seção 2.5 e 3.2.2). Os indicadores de produto e processo compõem o relatório de status por incremento (seção 3.2.1), alimentam a reunião de lições aprendidas (seção 2.6) e subsidiam a reavaliação de viabilidade do produto (seção 2.3). Métricas sem meta definida têm seus valores propostos pelo Analista de Qualidade e aprovados pelo Gerente de Projeto até o encerramento do incremento 1.

---

**Notas para consolidação no manual**

1. Ao incorporar a Parte 3, atualizar o índice de aderência: substituir a linha "Partes 3+ (planejadas)" pelas sete linhas de 3.1 a 3.7 (6.3.1 a 6.3.7).
2. Acrescentar a Parte 3 ao sumário e registrar a versão no Histórico de Versões.
3. Corrigir nas Considerações Finais "gerência técnica" para "gerenciamento técnico".
4. Decisões em aberto desta parte: datas e duração dos incrementos (PDW 15.1); horas de equipe, orçamento e licenças (PDW 15.2); metas de retrabalho, cumprimento de etapas, defeitos reabertos e tempo de correção (PDW 47 – qualidade); janela de medição de disponibilidade (PDW 9.2); aprovação das linhas de base (PDW 37.2) e do registro inicial de riscos; confirmação do escopo do Stripe (contradição PDW 5.2 versus 7.4 e 49), que afeta o risco R-02.
