# Orientações para o Capítulo 5: Processos Técnicos

Neste capítulo, a equipe documentará as práticas de engenharia de software aplicadas na construção do sistema: requisitos, arquitetura e design, implementação e integração, verificação e validação, até a transição, operação e descontinuação. A atividade é fundamentada na Seção 6.4 da ABNT NBR ISO/IEC/IEEE 12207:2021.

# **5.1 Requisitos**

## 5.1.1 Documento de requisitos do sistema
Listem formalmente os requisitos funcionais (RFs) e não funcionais (RNFs) do sistema com identificadores únicos (ex.: RF-01, RNF-01). Detalhem as regras de negócio associadas e restrições técnicas.

## 5.1.2 Rastreabilidade de requisitos
Apresentem a matriz ou mecanismo de rastreabilidade garantindo que cada necessidade de negócio esteja vinculada a um requisito, a uma tarefa no quadro, ao código-fonte e ao caso de teste correspondente.

## 5.1.3 Critérios de aceitação
Definam os critérios objetivos que determinam quando cada requisito é considerado concluído e aceito pelos stakeholders (ex.: formato *Dado que... Quando... Então...* ou checklist de validação).

## 5.1.4 Registro de stakeholders e necessidades elicitadas
Identifiquem as partes interessadas do sistema e documentem as técnicas de elicitação empregadas (entrevistas, workshops, observação, prototipação) e as necessidades capturadas.

# **5.2 Arquitetura e Design**

## 5.2.1 Documento de arquitetura do sistema
Descrevam a visão geral da arquitetura do software, os principais componentes, módulos e interfaces externas. Vinculem com as decisões arquiteturais (ADRs) que fundamentaram a escolha.

## 5.2.2 Diagramas de design
Apresentem pelo menos **2 diagramas formais de design** (ex.: C4 Model Nível 1/2/3, diagramas de componentes UML, diagramas de sequência ou diagramas de entidade-relacionamento). Cada diagrama deve vir acompanhado de texto explicativo sobre o fluxo representado.

## 5.2.3 Justificativa das escolhas tecnológicas
Justifiquem o stack de tecnologias adotado para frontend, backend, persistência, bibliotecas e serviços de infraestrutura, destacando benefícios de desempenho, manutenibilidade e produtividade.

# **5.3 Implementação e Integração**

## 5.3.1 Padrões de codificação adotados
Apresentem as diretrizes de código seguidas pelo time: convenções de nomenclatura, estruturação de pastas, padrões de tipagem estrita (TypeScript), regras de linter (ESLint) e formatação (Prettier).

## 5.3.2 Plano de integração entre componentes
Descrevam a estratégia de integração contínua (CI): esteira automatizada de build, validação de tipos e execução de testes a cada Pull Request.

## 5.3.3 Registro de testes unitários e de integração
Documentem a suíte de testes automatizados da aplicação: ferramentas utilizadas (ex.: Vitest), escopo testado (funções críticas, regras de negócio) e evidências de execução da suíte de testes.

## 5.3.4 Rastreabilidade entre código e requisitos
Mostrem como commits, branches e Pull Requests referenciam explicitamente os identificadores de requisitos (ex.: `feat: RF-03 - seleção de assentos em tempo real`).

# **5.4 Verificação, Validação e Transição**

## 5.4.1 Plano de verificação e validação
Diferenciem claramente as ações de **verificação** (*"Estamos construindo o produto corretamente?"* — análise de código, testes unitários) das ações de **validação** (*"Estamos construindo o produto certo?"* — testes de aceitação e homologação com stakeholders).

| Critério de Comparação | Verificação | Validação |
| :--- | :--- | :--- |
| **Pergunta Central** | *"Estamos construindo o produto corretamente?"* | *"Estamos construindo o produto certo?"* |
| **Foco** | Conformidade com especificações e requisitos definidos | Adequação ao uso pretendido pelo stakeholder |
| **Quando Ocorre** | Em cada fase do ciclo de vida (contínua) | Ao final de fases ou do projeto |
| **Quem Realiza** | Equipe técnica interna | Stakeholders e usuários reais |
| **Exemplos** | Revisão de código, análise estática, testes unitários | Testes de aceitação, demonstrações, pilotos |

## 5.4.2 Critérios de aceitação por stakeholder
Definam as condições formais de aprovação das entregas para cada perfil de stakeholder do projeto.

## 5.4.3 Relatório de testes de aceitação
Apresentem o registro dos testes de homologação/aceitação realizados, com status de aprovação de cada cenário testado.

## 5.4.4 Plano de transição/implantação do sistema
Detalhem os procedimentos para transição do software para o ambiente de produção: automação de deploy, execução de migrações de banco de dados e validação pós-implantação (smoke test).

# **5.5 Operação, Manutenção e Descontinuação**

## 5.5.1 Procedimentos de operação e monitoramento
Descrevam a rotina de operação do sistema em produção: suporte a usuários, monitoramento de desempenho e coleta de logs de erros.

## 5.5.2 Plano de manutenção
Apresentem a estratégia para as modalidades de manutenção: corretiva (correção de defeitos), adaptativa (mudanças no ambiente), perfectiva (melhorias) e preventiva (refatoração e segurança).

## 5.5.3 Estratégia de descontinuação e migração de dados
Descrevam o plano para eventual encerramento responsável do ciclo de vida do produto: arquivamento de dados com conformidade à LGPD, desativação de infraestrutura e notificação de usuários.

# **Artefatos e Assets Visuais Obrigatórios e Recomendados**

Para cumprir as exigências formais da Seção 6.4 da ISO 12207 e as diretrizes do professor, a equipe deve incluir:
- **Diagramas Formais de Design (Mínimo de 2 Obrigatórios na Seção 5.2.2):**
  - `assets/diagrams/c4-containers.png` (ou bloco Mermaid): **Diagrama C4 Nível 2 (Contêineres)** representando a integração entre Frontend (Next.js/React), Backend Serverless, Banco de Dados (Neon PostgreSQL), APIs de terceiros e navegadores dos clientes/atendentes.
  - `assets/diagrams/diagrama-sequencia-reserva.png` (ou bloco Mermaid): **Diagrama de Sequência UML ou Atividades BPMN** ilustrando a regra de reserva atômica de assentos (*SELECT FOR UPDATE*), disparo de vouchers e cancelamento.
  - `assets/diagrams/diagrama-er-banco.png` (ou bloco Mermaid): **Modelo de Dados / DER (Diagrama Entidade-Relacionamento)** com tabelas, chaves primárias/estrangeiras e cardinalidades do banco de dados (Slide 19 da Aula 06).
- **Prints e Screenshots Reais do Projeto (salvos em `assets/prints/`):**
  - `print-testes-unitarios-vitest.png`: Screenshot do terminal executando `npm test` / `vitest` com a suíte de testes passando 100% em verde e exibindo as taxas de cobertura.
  - `print-pipeline-ci-cd.png`: Screenshot da esteira de CI/CD no GitHub Actions executando com sucesso (Lint + Typecheck + Testes + Build).
- **Tabelas e Procedimentos Obrigatórios:**
  - Tabela 1: *Catálogo de Requisitos Funcionais e Não Funcionais* (com IDs únicos RF-XX e RNF-XX).
  - Tabela 2: *Matriz de Rastreabilidade Ponta a Ponta* (Requisito $\leftrightarrow$ Caso de Uso $\leftrightarrow$ Código $\leftrightarrow$ Teste Unitário).
  - Tabela 3: *Quadro Comparativo de Verificação vs. Validação* (Slide 33 da Aula 06).
  - Tabela 4: *Critérios de Entrada e Saída de V&V (Entry / Exit Criteria)* (Slide 37 da Aula 06).
  - Tabela 5: *Registro de Testes de Aceitação* (Cenários, Critérios e Status de Homologação com Stakeholders).
  - Procedimento: *Procedimento de Rollback e Critérios de Implantação* (Slide 31 e 36 da Aula 06).

# **Critérios de avaliação**

Apresentem as seções 5.1 a 5.5 no Manual de Processos de Software. A avaliação considerará a rastreabilidade ponta a ponta dos requisitos, o rigor dos diagramas de arquitetura, a robustez dos testes de V&V e a completude das práticas do ciclo de vida técnico.
