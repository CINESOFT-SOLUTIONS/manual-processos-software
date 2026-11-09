# Capítulo 2 – Processos de Acordo

## 2.1 Descrição do processo de aquisição

O processo de aquisição (ABNT NBR ISO/IEC/IEEE 12207:2021 – Cláusula 6.1.1) estabelece a governança da **CineSoft Solutions** para decidir entre desenvolver internamente (*Make*) ou contratar/adquirir de terceiros (*Buy*) os componentes, bibliotecas, APIs e serviços de infraestrutura que sustentam o produto **CineDoom** ao longo de suas três Macroentregas.

### Fronteira e Justificativa de Aquisição

A estratégia de engenharia da CineSoft Solutions concentra o esforço de desenvolvimento interno estritamente nos ativos que constituem o **núcleo de valor e diferencial competitivo** do CineDoom: o motor transacional de bilheteria e reservas com bloqueio pessimista ACID (*SELECT FOR UPDATE*), a máquina de estados de assentos com expiração *Just-in-Time*, o isolamento lógico multi-tenant e a camada de conformidade e anonimização da LGPD.

Em contrapartida, serviços de infraestrutura em nuvem, bancos de dados gerenciados, entrega de e-mails transacionais, retenção externa de logs, processamento financeiro PCI-DSS e mensageria fiscal SEFAZ são adquiridos de provedores especializados para reduzir o *time-to-market*, otimizar o Custo Total de Propriedade (TCO) e garantir Acordos de Nível de Serviço (SLA $\ge 99,9\%$).

### Tabela de Análise de Aquisição (*Make or Buy*)

A tabela a seguir consolida a decisão formal para cada elemento arquitetural do sistema, classificando a aquisição em **Sim** (solução madura/commodity adquirida pronta), **Não** (regra de negócio central desenvolvida internamente) ou **Parcial** (engine ou biblioteca externa combinada com regras de domínio proprietárias da CineSoft):

| Elemento do sistema | Adquirir pronto? | Justificativa | Possível fornecedor |
| :--- | :---: | :--- | :--- |
| **Motor de Bilheteria e Reserva Atômica ACID** | **Não** | Regra de negócio central e diferencial competitivo; exige controle estrito sobre locks de linha (`SELECT FOR UPDATE`), ordenação anti-deadlock e expiração *Just-in-Time*. | Desenvolvimento interno (CineSoft Solutions) |
| **Isolamento Multi-Tenant e Governança de Dados** | **Não** | Núcleo arquitetural do modelo SaaS B2B; requer injeção determinística de `tenant_id` em todas as queries e proteção contra vazamento *cross-tenant*. | Desenvolvimento interno sobre Prisma Client Extensions |
| **Módulo de Criptografia e Anonimização LGPD** | **Não** | Requisito legal crítico (Art. 18 e Art. 46 da LGPD) acoplado ao domínio fiscal de ingressos; combina `HMAC-SHA256` e `AES-256-GCM` nativos. | Desenvolvimento interno (`Node.js crypto`) |
| **Autenticação, Sessão JWT e Controle RBAC** | **Parcial** | A gestão de tokens criptográficos e cookies HTTP-only utiliza biblioteca consolidada, mas a política RBAC (`GERENTE`, `ATENDENTE`, `CLIENTE`), escopo por tenant e revogação são próprios. | `NextAuth.js` + Middleware proprietário CineSoft |
| **Interface Gráfica e Mapa Interativo de Salas** | **Parcial** | Primitivas estilísticas e ícones são acelerados por bibliotecas de mercado, porém a matriz bidimensional reativa de poltronas e o fluxo de guichê são proprietários. | `Tailwind CSS`, `Lucide Icons` + Componentes CineSoft |
| **ORM e Validação de Schemas de Entrada** | **Sim** | Bibliotecas de padrão industrial com alta segurança de tipos e prevenção nativa de *SQL Injection*, cujo desenvolvimento próprio seria antieconômico. | `Prisma ORM` e `Zod` (Open Source / MIT) |
| **Banco de Dados Relacional Gerenciado (DBaaS)** | **Sim** | Commodity de infraestrutura crítica; contratar DBaaS garante backups automatizados *Point-in-Time (PITR)*, connection pooling (`Supavisor`/`PgBouncer`) e alta disponibilidade. | **Supabase Pro / Neon PostgreSQL** |
| **Plataforma de Hospedagem Serverless e CDN** | **Sim** | Elimina custos de administração de servidores Linux, provendo deploy atômico, proteção DDoS, SSL automático e distribuição global na borda (*Edge Network*). | **Vercel Pro** (Cloud PaaS) |
| **Serviço de Disparo de E-mails Transacionais** | **Sim** | Manter servidores SMTP próprios acarreta alto risco de bloqueio em listas de spam; API especializada assegura entregabilidade (DKIM/SPF) para os vouchers de reserva. | **Resend** (SaaS de E-mail Transacional) |
| **Observabilidade e Retenção Legal de Logs** | **Sim** | A retenção imutável de telemetria por 365 dias (Marco Civil e LGPD) exige armazenamento colunar externo de baixo custo e busca rápida. | **Axiom Cloud** (Log Drain SaaS) |
| **Gateway de Pagamento Online (Macroentrega 2)** | **Sim** | Processar cartões e PIX exige certificação internacional PCI-DSS Nível 1 e antifraude dedicado, inviáveis para internalização em uma software house B2B. | **Stripe / Pagar.me** |
| **Motor de Mensageria Fiscal NFC-e (Macroentrega 3)** | **Sim** | A comunicação direta com webservices estaduais da SEFAZ sofre constantes mudanças normativas e tributárias; API terceirizada abstrai contingência e assinatura A1. | **Focus NFe / PlugNotas** |

### As Cinco Atividades do Processo de Aquisição (ISO 12207)

A CineSoft Solutions executa a contratação e governança de fornecedores externos por meio das cinco atividades normativas:

1. **Preparação da Aquisição:** O Arquiteto de Software especifica os requisitos técnicos, operacionais, de segurança (conformidade LGPD, criptografia em trânsito TLS 1.3 e em repouso AES-256) e de capacidade para o componente a ser adquirido.
2. **Divulgação e Seleção de Fornecedores:** Levantamento de pelo menos duas alternativas de mercado para cada categoria (ex.: Supabase vs. Neon; Resend vs. AWS SES; Vercel vs. AWS Amplify), avaliadas segundo custo escalonado, SLA ($\ge 99,9\%$), latência na região das Américas e maturidade do SDK TypeScript.
3. **Estabelecimento do Acordo:** Formalização da assinatura comercial (Termos de Serviço Corporativos e *Data Processing Addendum — DPA* para proteção de dados pessoais), configuração de cotas de faturamento e provisionamento de chaves de API em cofre seguro.
4. **Monitoramento do Acordo:** Acompanhamento contínuo pelo líder de DevOps por meio de páginas de status dos provedores, alertas de latência p95/p99, consumo de conexões do pooler e auditoria mensal de faturas frente ao volume de ingressos emitidos.
5. **Aceitação do Serviço/Produto Adquirido:** Execução de testes de integração automatizados na pipeline de CI/CD e validação de homologação (*smoke tests*) antes da liberação do componente para o tráfego de produção.

---

## 2.2 Descrição do processo de fornecimento

O processo de fornecimento (ABNT NBR ISO/IEC/IEEE 12207:2021 – Cláusula 6.1.2) regulamenta como a **CineSoft Solutions** comercializa, implanta, licencia, mantém e suporta a plataforma **CineDoom** junto aos cinemas clientes e parceiros de negócio.

### Perspectiva de Fornecimento e Ativos Comercializáveis

Além da oferta integral da plataforma, a arquitetura modular da CineSoft Solutions permite o fornecimento autônomo de subsistemas de alto valor agregado para diferentes perfis de adquirentes:

| Elemento com potencial | Possível adquirente | Modelo de acordo |
| :--- | :--- | :--- |
| **Plataforma Integrada CineDoom (Bilheteria + Back-office + Portal Web)** | Cinemas de rua, circuitos independentes, centros culturais e redes exibidoras de pequeno e médio porte | **Assinatura SaaS B2B** (mensalidade base por complexo + faixa variável por sala ativa, incluindo hospedagem e suporte) |
| **Engine de Mapa Bidimensional e Trava Atômica de Assentos (API)** | Produtoras de teatro, casas de espetáculos, auditórios universitários e plataformas regionais de eventos | **Licenciamento de API Transacional** (cobrança *pay-as-you-go* por assento reservado/emitido via REST) |
| **Módulo de Governança, Criptografia de CPF e Anonimização LGPD** | Software houses parceiras de varejo e entretenimento que necessitam adequar sistemas legados ao Art. 18 da LGPD | **Licenciamento de Biblioteca / SDK Corporativo** (taxa anual de licença + consultoria de integração) |
| **Portal White-Label de Reserva Antecipada com Expiração JIT** | Redes de cinemas que já possuem ERP fiscal próprio de balcão, mas carecem de canal digital moderno para espectadores | **Fornecimento de Módulo SaaS Integrado** (mensalidade fixa com customização de identidade visual *white-label*) |

### Termos do Acordo, Entregáveis e Evolução por Macroentregas

O fornecimento comercial aos cinemas adquirentes contempla os seguintes entregáveis contratuais e evolução funcional:

- **Provisionamento de Tenant Isolado:** Criação da organização no banco de dados de produção com isolamento lógico garantido por `tenant_id`, configuração de domínio/acesso e credenciais iniciais de gerência.
- **Carga de Dados e Parametrização Inicial:** Mapeamento das salas físicas do cinema (fileiras, colunas e categorias Clássica, IMAX ou VIP) e importação da grade inicial de filmes.
- **Documentação Operacional e Capacitação:** Entrega do Manual de Operação de Guichê e sessão de treinamento remoto ou presencial para atendentes e gerentes.
- **Roadmap Contratual em 3 Macroentregas:**
  - *Macroentrega 1 (`Release 1.0` — Implantação Imediata):* Operação completa de back-office, bilheteria física atômica e portal web de reservas com pagamento presencial no balcão.
  - *Macroentrega 2 (`Release 2.0` — Expansão Digital):* Habilitação de checkout online (PIX e cartão) e disparo de e-mails transacionais com domínio dedicado do exibidor.
  - *Macroentrega 3 (`Release 3.0` — Automação Fiscal e Varejo):* Integração com SEFAZ para emissão automática de NFC-e, módulo de bomboniere e painel self-service de faturamento.

### Critérios de Aceite Formal pelo Cliente Adquirente

A entrega de cada implantação ou macroentrega é considerada formalmente aceita mediante:
1. Aprovação integral da bateria de testes automatizados (770 cenários unitários, de integração e isolamento *cross-tenant*) e homologação assistida (*UAT*).
2. Inexistência de defeitos abertos de severidade **Crítica** (bloqueio de venda ou corrupção de dados) ou **Alta**.
3. Comprovação prática de zero ocorrência de venda dupla (*double-booking*) sob disputa simultânea entre portal web e balcão físico.
4. Assinatura digital do **Termo de Aceite de Implantação (TAI)** pelo representante legal do cinema contratante.

### Acordo de Nível de Serviço (SLA) e Suporte Pós-Entrega

A CineSoft Solutions assegura disponibilidade mensal mínima de **99,9%** da plataforma e provê suporte contínuo estruturado em quatro modalidades de manutenção:

| Severidade / Modalidade | Descrição do Cenário | Tempo de 1ª Resposta | Meta de Resolução / Contorno |
| :--- | :--- | :---: | :---: |
| **Crítica (P1 — Corretiva Urgente)** | Indisponibilidade total da bilheteria ou falha na emissão de ingressos em horário de sessão. | Até **15 minutos** | Até **2 horas** (rollback imediato em < 5 min) |
| **Alta (P2 — Corretiva Prioritária)** | Degradação no painel gerencial, falha no envio de voucher por e-mail ou lentidão acima do SLA. | Até **1 hora** | Até **8 horas** |
| **Normal (P3 — Adaptativa / Preventiva)** | Ajustes de compatibilidade de navegador, dúvidas operacionais ou otimização preventiva de índices. | Até **4 horas úteis** | Até **24 horas úteis** |
| **Evolutiva (P4 — Perfectiva)** | Solicitação de novos relatórios, filtros ou melhorias de usabilidade no Portal do Cliente. | Até **2 dias úteis** | Planejada na próxima *Sprint / Release* |

---

## 2.3 Identificação dos fornecedores e parceiros relevantes

A operação contínua e comercial da plataforma CineDoom apoia-se em provedores de tecnologia de primeira linha. A tabela abaixo detalha cada fornecedor crítico, seu papel arquitetural, a estrutura de contratação escalonada entre a validação inicial (Macroentrega 1) e a operação comercial plena (Macroentregas 2 e 3), bem como os impactos em disponibilidade, custo e segurança:

| Fornecedor / Parceiro | Categoria e Serviço Prestado | Plano e Estrutura de Custo Comercial | Impacto Operacional, Disponibilidade e Mitigação de Riscos |
| :--- | :--- | :--- | :--- |
| **Vercel Inc.** | **PaaS & Edge CDN:** Hospedagem da aplicação Next.js 14, execução de funções serverless e distribuição global de ativos estáticos. | **Vercel Pro** (`US$ 20/mês` por membro de engenharia; 1 TB de banda e execução concorrente expandida). *Piloto inicial em Hobby Tier.* | **Disponibilidade e Performance:** SLA de 99,99% na borda. Impacta diretamente o acesso ao portal e à bilheteria. Mitigação: build determinístico e rollback instantâneo de release em 1 clique. |
| **Supabase Inc. / Neon Tech** | **DBaaS PostgreSQL:** Persistência relacional ACID, gerenciamento de conexões via *Supavisor* (porta `6543`) e triggers de auditoria. | **Plano Pro Comercial** (`US$ 25 a US$ 69/mês`; compute dedicado, 8 GB+ de disco SSD, backups diários e *Point-in-Time Recovery — PITR*). | **Segurança e Integridade:** Crítico para evitar perda de vendas e garantir locks `SELECT FOR UPDATE`. Mitigação: replicação automática, conexões TLS obrigatórias e scripts de migração versionados no Prisma. |
| **Resend Technologies** | **Comunicação Transacional (SaaS):** API REST para entrega de vouchers de reserva e confirmações de ingresso com autenticação DKIM/SPF. | **Resend Pro** (`US$ 20/mês` para 50.000 e-mails/mês, domínios corporativos verificados `@cinedoom.com.br` e sem limite diário). | **Experiência do Cliente:** Impacta o recebimento do comprovante por e-mail (`CA-11`). Mitigação: desacoplamento via interface `EmailProvider` e exibição imediata do voucher na tela e na área *"Minhas Reservas"*. |
| **Axiom Inc.** | **Observabilidade e Log Drain:** Ingestão contínua de logs estruturados JSON e retenção de longo prazo para auditoria. | **Axiom Cloud Plan** (`US$ 25/mês` com ingestão de até 1 TB/mês e retenção estendida de 365 dias). | **Conformidade Legal (LGPD):** Essencial para rastreabilidade forense e retenção de 1 ano sem onerar o banco transacional. Mitigação: mascaramento prévio de PII antes do envio do log. |
| **GitHub Inc.** | **Engenharia e CI/CD:** Repositórios Git privados, gestão de backlog (GitHub Projects) e esteira automatizada (GitHub Actions). | **GitHub Team** (`US$ 4/usuário/mês`; 3.000 minutos de Actions, branches protegidas e *Codeowners*). | **Qualidade e Governança:** Sustenta a integração contínua e o bloqueio de código defeituoso. Baixo impacto em tempo de execução de produção. |
| **Stripe Inc. / Pagar.me** *(Macroentrega 2)* | **Gateway Financeiro PCI-DSS:** Processamento de pagamentos online via PIX dinâmico e cartões de crédito no Portal do Cliente. | **Taxa Variável Transacional** (`3,99% + R$ 0,39` por cartão aprovado; `0,99%` no PIX, sem mensalidade fixa). | **Segurança Financeira:** Elimina o tráfego de dados sensíveis de cartão nos servidores da CineSoft. Mitigação: webhooks idempotentes e fallback de pagamento presencial no balcão. |
| **Focus NFe / PlugNotas** *(Macroentrega 3)* | **Mensageria Fiscal (SaaS):** Emissão, assinatura digital e transmissão de NFC-e junto às SEFAZ estaduais. | **Plano Empresarial** (`R$ 149/mês` por CNPJ emissor para até 2.000 notas fiscais, com fila de contingência offline). | **Conformidade Tributária:** Desacopla a CineSoft das variações técnicas de cada estado brasileiro, garantindo emissão assíncrona sem travar a fila física da bilheteria. |

---
