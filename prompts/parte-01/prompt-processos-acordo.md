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
   - Modelo de fornecimento (SaaS para redes exibidoras de cinema).
   - Preparação do fornecimento e catálogo de entregáveis por release.
   - Critérios de aceite e homologação pelo cliente.
   - Suporte pós-entrega, operação assistida e canais de SLA.

[FORMATO DE SAÍDA]
Texto em Markdown formatado, com tabelas quando aplicável (critérios de seleção e matriz de entregáveis), salvo em `docs/rascunhos/parte-01/rascunho-parte-01.md`.

[VALIDAÇÃO OBRIGATÓRIA]
Ao finalizar a proposta, execute uma autoavaliação rigorosa utilizando o validador em `prompts/validador-iso12207.md`.
Gere o relatório completo e salve-o em `docs/validacoes/parte-01/analise-validacao-parte-01.md`:
1. Valide a conformidade com as cláusulas 6.1.1 (Aquisição) e 6.1.2 (Fornecimento) da ISO/IEC/IEEE 12207:2021.
2. Cheque a consistência da especificação com os modelos de comercialização e infraestrutura do documento-base (`docs/constituicao/project-definition-workbook.md`), usando-o como referência interna de verificação, sem citá-lo no documento entregue.
3. Anexe no relatório a tabela comparativa de conformidade do processo (Processo, Cláusula, Cobertura e Ajustes).
```
