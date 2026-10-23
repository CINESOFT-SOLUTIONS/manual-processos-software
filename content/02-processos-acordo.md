# Capítulo 2 – Processos de Acordo

## 2.1 Descrição do processo de aquisição

O processo de aquisição (ISO/IEC/IEEE 12207:2021 – Cláusula 6.1.1) define as diretrizes para seleção, contratação e acompanhamento de produtos e serviços externos necessários à entrega do CineDoom.

### Fronteira e Justificativa de Aquisição
A CineSoft desenvolve internamente o núcleo de valor do negócio (lógica de bilheteria, regras de ocupação e frontend). Serviços de infraestrutura, plataforma e bibliotecas especializadas são contratados externamente para reduzir o tempo de colocação no mercado (*time-to-market*), evitar custos de imobilização em servidores físicos e garantir alta disponibilidade.

### Etapas do Processo de Aquisição
1. **Identificação da Necessidade:** Justificativa técnica e análise de viabilidade econômica (comprar vs. construir).
2. **Seleção de Alternativas:** Levantamento de provedores de mercado aderentes à stack tecnológica.
3. **Avaliação por Critérios:** Custo, disponibilidade (SLA ≥ 99.9%), conformidade com a LGPD, documentação e facilidade de integração.
4. **Aprovação e Contratação:** Homologação pelo Arquiteto de Software e Gerente de Projeto.
5. **Monitoramento Contínuo:** Avaliação de métricas de uptime, tempo de resposta e conformidade contratual.

## 2.2 Descrição do processo de fornecimento

O processo de fornecimento (ISO/IEC/IEEE 12207:2021 – Cláusula 6.1.2) formaliza como a CineSoft entrega a solução CineDoom ao cliente adquirente.

### Modelo de Fornecimento
O software é fornecido no modelo **SaaS**, mediante contrato de assinatura periódica, englobando licenciamento de uso, infraestrutura em nuvem, atualizações corretivas e suporte técnico.

### Entregáveis Contratuais
- **Ambiente Operacional Hospedado:** Instância em nuvem implantada e validada em produção.
- **Carga de Dados Inicial:** Banco de dados populado com as salas, capacidade e grade inicial de filmes do cliente.
- **Documentação de Uso:** Manual do Usuário e Guia de Procedimentos Operacionais de Bilheteria.
- **Capacitação:** Sessão de treinamento para atendentes e gerentes.

### Critérios de Aceite Formal
1. Execução bem-sucedida da bateria de testes de aceitação em ambiente de homologação.
2. Inexistência de defeitos com severidade Crítica ou Alta.
3. Demonstração de estabilidade na venda simultânea de ingressos sem ocorrência de venda dupla.
4. Assinatura do Termo de Aceite Formal pelo representante legal do cliente.

### Suporte Pós-Entrega
A CineSoft disponibiliza manutenção:
- **Corretiva:** Tratamento de falhas com SLA conforme severidade (Crítica: até 4h; Normal: até 24h).
- **Adaptativa:** Atualização de bibliotecas e adequações a novos navegadores.
- **Evolutiva:** Novas funcionalidades geridas via fila de backlog e aprovadas via processo formal de mudança.
- **Preventiva:** Revisões periódicas de integridade do banco e métricas de desempenho.

## 2.3 Identificação dos fornecedores e parceiros relevantes

| Fornecedor / Parceiro | Categoria | Serviço Prestado | Justificativa Técnica / Critério |
|---|---|---|---|
| **Vercel Inc.** | Plataforma como Serviço (PaaS) | Hospedagem do frontend, rotas serverless, CDN e deploy contínuo | Deploy atômico por commit, HTTPS nativo e alta performance de borda. |
| **Neon Technologies** | Banco de Dados como Serviço (DBaaS) | PostgreSQL Serverless gerenciado | Autoscaling, compatibilidade total com o Prisma ORM, backups e tier inicial gratuito. |
| **GitHub Inc.** | Ferramentas de Engenharia | Controle de versão, GitHub Actions (CI/CD) e GitHub Issues | Padronização de governança, rastreabilidade de código e automação de testes. |
| **Axiom Inc.** | Observabilidade como Serviço (SaaS) | Log Drain e retenção contínua de telemetria | Retenção legal de 365 dias para logs de auditoria e segurança exigida pela LGPD. |
| **Resend Technologies** | Comunicação Transacional (SaaS) | Despacho de e-mails transacionais com vouchers | Envio confiável de confirmações de reserva com código e prazo presencial. |
| **Stripe Inc.** *(Previsto para release futura)* | Gateway de Pagamento | Processamento de transações com cartões e certificação PCI-DSS | Delegação de responsabilidade e segurança no tráfego de dados bancários. |

---
