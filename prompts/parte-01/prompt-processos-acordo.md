# Prompt — Parte 1: Processos de Acordo

## 1. Identificação
- **Código:** `PR-P01_Processos_Acordo`
- **Parte do Trabalho:** Parte 1 – Processos de Acordo (Agreement Processes)
- **Norma / Cláusula de Referência:** ISO/IEC/IEEE 12207:2021 — Cláusulas 6.1.1 (Acquisition Process) e 6.1.2 (Supply Process)
- **Documento-base:** `docs/constituicao/project-definition-workbook.md` (Seções 4, 11 e 12)

---

## 2. Prompt Estruturado (Input)

```markdown
Atue como Especialista em Processos de Software conforme a norma ABNT NBR ISO/IEC/IEEE 12207:2021.
De forma clara, traga estes pontos solicitados com no máximo 1 seção por cada tópico solicitado.
Use o documento-base como contexto interno para entender a idealização do projeto, mas não o cite nem referencie no documento de processos entregue. Quando a informação necessária não estiver claramente definida no documento-base, registre um bloco de [PREMISSA] para que a decisão adotada seja validada posteriormente.
Após identificar o índice da ISO realize a leitura do material em `docs/norma-iso/abnt-iso-iec-12207-2021.md` para garantir que está de acordo com a norma.


Elabore a especificação dos Processos de Acordo para o CineDoom:

1. PROCESSO DE AQUISIÇÃO (ISO 12207 – 6.1.1):
   Produza a seção de forma verticalizada, seguindo as cinco atividades da cláusula (a→e), nesta ordem. Descreva as atividades UMA vez, no nível do processo; o detalhamento por item adquirido vai nas tabelas.

   a) Preparação para a aquisição: estratégia de aquisição e decisão desenvolver-vs-adquirir (build vs. buy), com justificativa técnica e econômica; requisitos do item e solicitação de fornecimento.
   b) Comunicar a aquisição e selecionar o fornecedor: avalie os fornecedores usando exatamente estes critérios: custo, segurança, disponibilidade, escalabilidade, compatibilidade, suporte, condições contratuais, portabilidade e dependência do fornecedor.
   c) Estabelecer e manter o acordo: contrato, critérios de aceitação, SLA, tratamento de mudanças, direitos de dados/propriedade intelectual e licenciamento.
   d) Monitorar o acordo: avaliação da execução, registro de desempenho, tratamento de incidentes e revisão periódica.
   e) Aceitar o produto ou serviço: defina critérios de aceitação e SLA do serviço adquirido antes do aceite; confirmação de conformidade, pagamento, aceite formal e encerramento.

   FRONTEIRA — itens de aquisição do CineDoom:
   - Infraestrutura cloud (AWS): computação, rede e armazenamento.
   - Banco de dados gerenciado (PostgreSQL gerenciado).
   - Serviços de monitoramento e logging.
   - Serviço de backup.
   - Serviço de e-mail transacional — condicional (somente se notificações entrarem no escopo).
   - Consultoria especializada — condicional.
   - Declare explicitamente a situação de APIs externas e de bibliotecas/dependências pagas, incluindo licenciamento; se não houver, registre como tal.
   - Não incluir gateway de pagamento (fora do escopo).

   IDENTIFICAÇÃO DE FORNECEDORES E PARCEIROS (obrigatório): tabela com colunas Item adquirido | Fornecedor/parceiro | Tipo (IaaS/PaaS/SaaS/consultoria) | Criticidade | Justificativa da contratação.

   MATRIZ DE SELEÇÃO: para os itens de maior criticidade, compare ao menos duas alternativas usando os critérios definidos em (b).

   Regras obrigatórias: não escreva "conforme o PDW", "seção X do PDW" ou equivalente — referencie no máximo a cláusula da ISO. Registre decisões não claramente definidas no documento-base como bloco: `> [PREMISSA] <decisão adotada> — <motivo/a validar>`.

2. PROCESSO DE FORNECIMENTO (ISO 12207 – 6.1.2):
   Descreva o Processo de Fornecimento com clareza, sem reproduzir a norma. Não há necessidade de manter obrigatoriamente os rótulos 7.1–7.7. Garanta, contudo, a cobertura dos seguintes elementos: propósito e justificativa, aplicação ao sistema (entradas, atividades, participantes, saídas), papéis e responsabilidades, artefatos, critérios de avaliação do processo, relacionamento com outros processos e decisões e justificativas.

   Mantenha o enfoque no recorte exigido pela disciplina: como o software é entregue ao cliente, contrato, critérios de aceite e suporte, além da identificação dos fornecedores e parceiros relevantes.

   Desenvolva o processo observando:

   - **Propósito e enquadramento:** descreva brevemente o propósito do processo e sua justificativa, no contexto do CineDoom.
   - **Modelo de fornecimento:** SaaS com assinatura mensal por estabelecimento, voltado a cinemas de pequeno e médio porte. Especifique a divisão de responsabilidades: CineSoft (implanta, opera a infraestrutura, monitora, mantém e presta suporte) e cliente (opera o sistema no dia a dia). Mencione "operação assistida" quando pertinente.
   - **Atividades (ISO 6.1.2):** cubra, no nível do processo, as atividades relevantes: (a) preparação do fornecimento, (c) estabelecimento e manutenção do acordo, (d) execução do acordo e (e) entrega e prestação de suporte. Para a atividade (b) "Responder a uma solicitação de fornecimento de produtos ou serviços", registre explicitamente que **não se aplica**, pois trata-se de um produto pronto (não sob encomenda).
   - **Contrato:** indique o que deve constar no contrato (escopo, preço, prazo, critérios de aceite, responsabilidades das partes, suporte, níveis de serviço, tratamento de mudanças, encerramento do serviço e tratamento dos dados do cliente).
   - **Preparação do fornecimento e catálogo de entregáveis por release:** detalhe o que compõe a entrega de cada release (aplicação, ambiente configurado, documentação, manual do usuário, manual técnico, relatório de testes, registro de versão e orientação inicial). Inclua, quando aplicável, versionamento, notas de versão, registro de alterações e aprovação antes da produção.
   - **Critérios de aceite e homologação:** defina critérios concretos (validação dos requisitos, homologação, ausência de defeitos críticos e aprovação formal do representante do cliente). Não confunda esses critérios com os "critérios de avaliação do processo".
   - **Suporte pós-entrega:** descreva manutenção corretiva, adaptativa, evolutiva e preventiva. Especifique canais de atendimento (sistema de chamados, ao menos) e os elementos de SLA (severidade, tempo de primeira resposta, tempo de solução, horário de atendimento e escalonamento). Caso qualquer valor de SLA não esteja definido no documento-base, registre `[PREMISSA]` com o motivo.
   - **Fornecedores e parceiros relevantes:** identifique, de forma objetiva, os fornecedores e parceiros que sustentam a entrega do SaaS (aqueles que mantêm o fornecimento em funcionamento). Remeta à seção 1 (Processo de Aquisição) sempre que possível, sem duplicar integralmente a tabela — foque apenas no que é crítico para o fornecimento.
   - **Relacionamento com outros processos:** estabeleça claramente as relações: entrada proveniente da Aquisição; saídas e interações com Operação, Manutenção, Suporte e Configuração/Releases. Mencione, ainda, o relacionamento com Encerramento do Produto e Portabilidade.
   - **Critérios de avaliação do processo:** indique, de forma breve, como verificar se o Processo de Fornecimento atingiu seus resultados esperados (ex.: aceite formal emitido, obrigações contratuais básicas cumpridas).
   - **Decisões e justificativas:** registre decisões adotadas e eventuais premissas em bloco `[PREMISSA]` (ex.: RTO 4h, RPO 24h, disponibilidade 95% — caso mantidos como premissas). Não inclua gateway de pagamento (fora do escopo da primeira versão). Declare, também, a situação de APIs externas e de bibliotecas/dependências pagas (incluindo licenciamento), caso aplicável.

   Regras obrigatórias: não escreva "conforme o PDW", "seção X do PDW" ou equivalente — referencie no máximo a cláusula da ISO. Não reproduza literalmente o texto da norma. Utilize o documento-base apenas como contexto interno.

[FORMATO DE SAÍDA]
Texto em Markdown formatado, com tabelas quando aplicável (critérios de seleção e matriz de entregáveis), salvo em `docs/rascunhos/parte-01/rascunho-parte-01.md`.

[VALIDAÇÃO OBRIGATÓRIA]
Ao finalizar a proposta, execute uma autoavaliação rigorosa utilizando o validador em `prompts/validador-iso12207.md`.
Gere o relatório completo e salve-o em `docs/validacoes/parte-01/analise-validacao-parte-01.md`:
1. Valide a conformidade com as cláusulas 6.1.1 (Aquisição) e 6.1.2 (Fornecimento) da ISO/IEC/IEEE 12207:2021.
2. Cheque a consistência da especificação com os modelos de comercialização e infraestrutura do documento-base (`docs/constituicao/project-definition-workbook.md`), usando-o como referência interna de verificação, sem citá-lo no documento entregue.
3. Anexe no relatório a tabela comparativa de conformidade do processo (Processo, Cláusula, Cobertura e Ajustes).
```
