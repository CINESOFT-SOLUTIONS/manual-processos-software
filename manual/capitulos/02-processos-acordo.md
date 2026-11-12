# Capítulo 2 – Processos de Acordo

## 2.1 Descrição do processo de aquisição

O processo de aquisição (ABNT NBR ISO/IEC/IEEE 12207:2021 – Cláusula 6.1.1) estabelece a governança da **CineSoft Solutions** no papel de organização adquirente, definindo o que desenvolver internamente e o que contratar de terceiros para sustentar o produto **CineDoom**.

### Fronteira e Justificativa de Aquisição

A estratégia de engenharia da CineSoft Solutions concentra o desenvolvimento interno nos componentes que formam o **núcleo de valor e diferencial competitivo** da plataforma: o motor de bilheteria e reservas com trava atômica (`SELECT FOR UPDATE`), a máquina de estados de assentos com expiração *Just-in-Time*, o isolamento multi-tenant e o módulo de proteção de dados (LGPD).

Em contrapartida, serviços de infraestrutura em nuvem, bancos de dados gerenciados, disparo de e-mails transacionais, retenção de logs, processamento de pagamentos e mensageria fiscal são adquiridos de provedores especializados para reduzir o tempo de desenvolvimento, diminuir custos operacionais e garantir alta disponibilidade (SLA $\ge 99,9\%$).

### Tabela de Análise de Aquisição (*Make or Buy*)

A governança de aquisição da CineSoft Solutions consolida a decisão formal para cada elemento arquitetural do sistema, classificando a abordagem em **Sim** (solução madura/commodity adquirida pronta), **Não** (regra de negócio central desenvolvida internamente) ou **Parcial** (engine ou biblioteca externa combinada com regras de domínio proprietárias):

**Tabela 2 – Análise de Aquisição: Componentes de Software e Domínio (Make or Buy)**

| Elemento do sistema | Adquirir pronto? | Justificativa | Possível fornecedor |
| :--- | :---: | :--- | :--- |
| **Motor de Bilheteria e Reserva Atômica ACID** | **Não** | Diferencial competitivo central. Exige controle estrito sobre locks pessimistas (`SELECT FOR UPDATE`) para impedir venda dupla entre web e guichê físico. | Desenvolvimento interno (CineSoft Solutions) |
| **Isolamento Multi-Tenant e Governança de Dados** | **Não** | Núcleo do modelo SaaS B2B. A injeção automática de `tenant_id` via Prisma Client Extensions garante isolamento seguro na mesma base relacional com baixo custo. | Desenvolvimento interno sobre Prisma Extensions |
| **Módulo de Criptografia e Anonimização LGPD** | **Não** | Requisito legal (LGPD Art. 18 e 46). Exige anonimização irreversível sob demanda sem corromper o histórico fiscal de ingressos vendidos pelo cinema. | Desenvolvimento interno (`Node.js crypto`) |
| **Autenticação, Sessão JWT e Controle RBAC** | **Parcial** | Adota biblioteca madura (`NextAuth.js`) para gerenciar sessões e cookies seguros, desenvolvendo internamente a matriz de perfis (`RBAC`) e o vínculo por cinema. | `NextAuth.js` + Middleware proprietário CineSoft |
| **Interface Gráfica e Mapa Interativo de Salas** | **Parcial** | Aproveita bibliotecas de mercado (`Tailwind`, `Lucide`) para primitivas visuais, desenvolvendo sob medida a matriz reativa de poltronas e o fluxo do guichê. | `Tailwind CSS`, `Lucide Icons` + Componentes CineSoft |
| **ORM e Validação de Schemas de Entrada** | **Sim** | Padrão de mercado que provê tipagem estrita (*type-safety*) e proteção nativa contra *SQL Injection*, sendo antieconômico construir do zero. | `Prisma ORM` e `Zod` (Open Source / MIT) |

*Fonte: CineSoft Solutions (2026).*

**Tabela 3 – Análise de Aquisição: Infraestrutura Cloud e Serviços Gerenciados (Make or Buy)**

| Elemento do sistema | Adquirir pronto? | Justificativa | Possível fornecedor |
| :--- | :---: | :--- | :--- |
| **Banco de Dados Relacional Gerenciado (DBaaS)** | **Sim** | Elimina custos de DBA, provendo restauração pontual automatizada (PITR), *connection pooling* para serverless e alta disponibilidade ($\ge 99,9\%$). | **Supabase Pro / Neon PostgreSQL** |
| **Plataforma de Hospedagem Serverless e CDN** | **Sim** | Elimina a manutenção de servidores dedicados, entregando deploys atômicos com *rollback* instantâneo, proteção DDoS e distribuição global na borda. | **Vercel Pro** (Cloud PaaS) |
| **Serviço de Disparo de E-mails Transacionais** | **Sim** | Evita que vouchers caiam em caixas de spam; a API especializada assegura entrega em milissegundos com autenticação SPF, DKIM e DMARC. | **Resend** (SaaS de E-mail Transacional) |
| **Observabilidade e Retenção Legal de Logs** | **Sim** | Cumpre a retenção legal de logs por 1 ano (Marco Civil e LGPD) sem sobrecarregar o armazenamento do banco relacional, com busca indexada rápida. | **Axiom Cloud** (Log Drain SaaS) |
| **Gateway de Pagamento Online (Macroentrega 2)** | **Sim** | Transfere a complexidade regulatória da certificação PCI-DSS Nível 1 e antifraude, automatizando a liquidação de PIX dinâmico e cartões. | **Stripe / Pagar.me** |
| **Motor de Mensageria Fiscal NFC-e (Macroentrega 3)** | **Sim** | Abstrai as constantes mudanças tributárias estaduais da SEFAZ, contingência offline e assinatura digital com certificado A1, evitando passivos fiscais. | **Focus NFe / PlugNotas** |

*Fonte: CineSoft Solutions (2026).*

### As Cinco Atividades do Processo de Aquisição (ISO/IEC/IEEE 12207:2017)

A CineSoft Solutions conduz a contratação e a governança de serviços e componentes especializados por meio das cinco atividades normativas da norma:

1. **Preparação para a Aquisição:**
   - *Descrição:* O Arquiteto de Software e a equipe técnica especificam as necessidades do sistema, volumetria estimada de transações e requisitos de segurança (TLS 1.3, criptografia de dados e conformidade com a LGPD).
   - *Saídas:* Especificação Técnica de Aquisição e Matriz de Critérios de Seleção.
2. **Divulgação e Seleção de Fornecedores:**
   - *Descrição:* A equipe levanta e compara soluções consolidadas para cada categoria (ex.: Neon vs. Supabase; Resend vs. AWS SES; Vercel vs. AWS Amplify), pontuando maturidade do SDK, latência na América do Sul e custo escalonado.
   - *Saídas:* Parecer Comparativo de Fornecedores e Registro de Seleção.
3. **Estabelecimento e Manutenção do Acordo:**
   - *Descrição:* Formalização contratual via Termos de Serviço Corporativos e Aditivo de Tratamento de Dados (*DPA* para a LGPD), assegurando SLA $\ge 99,9\%$, limites de requisição (*rate-limiting*) e portabilidade de dados.
   - *Saídas:* Contrato de Serviço de Nuvem (DPA) e Registro de Credenciais em Cofre Seguro.
4. **Monitoramento do Acordo:**
   - *Descrição:* Integrado ao Controle de Projeto (Capítulo 4), acompanha-se a disponibilidade dos serviços via telemetria (latência p95/p99 e conexões do pooler), páginas públicas de status e conciliação mensal de consumo.
   - *Saídas:* Relatório Mensal de SLA/Consumo e Registro de Incidentes do Provedor.
5. **Aceitação do Produto ou Serviço:**
   - *Descrição:* O serviço é validado em ambiente de homologação (*sandbox*) e integrado à esteira de CI/CD, exigindo aprovação em testes de estabilidade antes da liberação em produção acompanhada de plano de contingência (*rollback plan*).
   - *Saídas:* Relatório de Testes em Sandbox e Termo de Liberação em Produção (*Go-Live*).

---

## 2.2 Descrição do processo de fornecimento

O processo de fornecimento (ABNT NBR ISO/IEC/IEEE 12207:2021 – Cláusula 6.1.2) regulamenta como a **CineSoft Solutions** comercializa, implanta, licencia, mantém e suporta a plataforma **CineDoom** junto aos cinemas clientes e parceiros de negócio.

### Perspectiva de Fornecimento e Ativos Comercializáveis

Além da oferta integral da plataforma, a arquitetura modular da CineSoft Solutions permite o fornecimento autônomo de subsistemas de alto valor agregado para diferentes perfis de adquirentes:

**Tabela 4 – Perspectiva de Fornecimento e Ativos Comercializáveis**

| Elemento com potencial | Possível adquirente | Modelo de acordo |
| :--- | :--- | :--- |
| **Plataforma Integrada CineDoom (Bilheteria + Back-office + Portal Web)** | Cinemas de rua, circuitos independentes, centros culturais e redes exibidoras de pequeno e médio porte | **Assinatura SaaS B2B:**<br>• **Mensalidade base:** **R$ 790,00 / mês** (complexo com até 2 salas ativas, hospedagem em nuvem e suporte técnico).<br>• **Sala adicional:** **R$ 120,00 / mês** por sala ativa.<br>• **Setup e Implantação:** **R$ 1.500,00** (taxa única de parametrização, carga de dados e treinamento operacional). |
| **Engine de Mapa Bidimensional e Trava Atômica de Assentos (API)** | Produtoras de teatro, casas de espetáculos, auditórios universitários e plataformas regionais de eventos | **Licenciamento de API Transacional (Pay-as-you-go):**<br>• **Tarifa por transação:** **R$ 0,08** por assento emitido (**R$ 0,05** acima de 10.000 assentos/mês).<br>• **Franquia mínima:** **R$ 200,00 / mês** (inclui franquia de 2.500 assentos e SLA de 99,9%). |
| **Módulo de Governança, Criptografia de CPF e Anonimização LGPD** | Software houses parceiras de varejo e entretenimento que necessitam adequar sistemas legados ao Art. 18 da LGPD | **Licenciamento de SDK Corporativo / Biblioteca:**<br>• **Assinatura Anual:** **R$ 8.900,00 / ano** (atualizações regulatórias e suporte normativo).<br>• **Licença Perpétua:** **R$ 16.000,00** (código compilado + 10 horas de consultoria técnica de integração). |
| **Portal White-Label de Reserva Antecipada com Expiração JIT** | Redes de cinemas que já possuem ERP fiscal próprio de balcão, mas carecem de canal digital moderno para espectadores | **Fornecimento de Módulo SaaS White-Label:**<br>• **Mensalidade:** **R$ 490,00 / mês** por cinema exibidor (domínio dedicado e certificado SSL inclusos).<br>• **Setup visual:** **R$ 800,00** (taxa única de adaptação da identidade visual da marca). |

*Fonte: CineSoft Solutions (2026).*

### As Cinco Atividades do Processo de Fornecimento (ISO/IEC/IEEE 12207:2017)

A CineSoft Solutions conduz o ciclo comercial e operacional de atendimento ao cliente por meio das cinco atividades normativas:

1. **Preparação do Fornecimento:**
   - *Descrição:* A equipe de negócios e arquitetura mapeia os perfis de exibidores adquirentes, definindo a estratégia de monetização SaaS, matriz de precificação por sala e modelos de licenciamento de APIs desacopladas.
   - *Saídas:* Matriz de Planos Comerciais e Catálogo de Ativos Licenciáveis.
2. **Resposta à Solicitação:**
   - *Descrição:* Ao receber solicitações de cotação ou RFPs de exibidores, a CineSoft avalia a viabilidade técnica e arquitetural da rede (quantidade de salas e integração fiscal), gerando proposta com cronograma e escopo de setup.
   - *Saídas:* Proposta Técnica de Implantação e Proposta Comercial de Fornecimento.
3. **Estabelecimento e Manutenção do Acordo:**
   - *Descrição:* Formalização do Contrato de Licenciamento SaaS e Acordo de Tratamento de Dados (DPA/LGPD), estipulando SLA de 99,9%, isolamento multi-tenant (`tenant_id`), roadmap em 3 Macroentregas e condições de rescisão com portabilidade.
   - *Saídas:* Contrato de Prestação de Serviço (SaaS) e Aditivo de Privacidade e DPA.
4. **Execução do Acordo:**
   - *Descrição:* Provisionamento do tenant isolado, carga inicial de salas/filmes, treinamento operacional de atendentes e evolução orientada à esteira de CI/CD com controle de versão e validação nos 711 testes automatizados.
   - *Saídas:* Ambiente de Produção Provisionado e Relatório de Validação de CI/CD.
5. **Entrega e Suporte:**
   - *Descrição:* Condução da homologação assistida (*UAT*), assinatura do Termo de Aceite de Implantação (TAI) após comprovação de zero *double-booking* e ativação do suporte técnico contínuo estruturado nos 4 níveis de SLA.
   - *Saídas:* Termo de Aceite de Implantação (TAI) e Relatório Mensal de Cumprimento de SLA.

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
1. Aprovação integral da bateria de testes automatizados (711 testes unitários, de integração e isolamento *cross-tenant*) e homologação assistida (*UAT*).
2. Inexistência de defeitos abertos de severidade **Crítica** (bloqueio de venda ou corrupção de dados) ou **Alta**.
3. Comprovação prática de zero ocorrência de venda dupla (*double-booking*) sob disputa simultânea entre portal web e balcão físico.
4. Assinatura digital do **Termo de Aceite de Implantação (TAI)** pelo representante legal do cinema contratante.

### Acordo de Nível de Serviço (SLA) e Suporte Pós-Entrega

A CineSoft Solutions assegura disponibilidade mensal mínima de **99,9%** da plataforma e provê suporte contínuo estruturado em quatro modalidades de manutenção:

**Tabela 5 – Acordo de Nível de Serviço (SLA) e Suporte Pós-Entrega**

| Severidade / Modalidade | Descrição do Cenário | Tempo de 1ª Resposta | Meta de Resolução / Contorno |
| :--- | :--- | :---: | :---: |
| **Crítica (P1 — Corretiva Urgente)** | Indisponibilidade total da bilheteria ou falha na emissão de ingressos em horário de sessão. | Até **15 minutos** | Até **2 horas** (rollback imediato em < 5 min) |
| **Alta (P2 — Corretiva Prioritária)** | Degradação no painel gerencial, falha no envio de voucher por e-mail ou lentidão acima do SLA. | Até **1 hora** | Até **8 horas** |
| **Normal (P3 — Adaptativa / Preventiva)** | Ajustes de compatibilidade de navegador, dúvidas operacionais ou otimização preventiva de índices. | Até **4 horas úteis** | Até **24 horas úteis** |
| **Evolutiva (P4 — Perfectiva)** | Solicitação de novos relatórios, filtros ou melhorias de usabilidade no Portal do Cliente. | Até **2 dias úteis** | Planejada na próxima *Sprint / Release* |

*Fonte: CineSoft Solutions (2026).*

---

## 2.3 Identificação dos fornecedores e parceiros relevantes

A operação contínua e comercial da plataforma CineDoom apoia-se em provedores de tecnologia de primeira linha. A tabela abaixo detalha cada fornecedor crítico, seu papel arquitetural, a estrutura de contratação escalonada entre a validação inicial (Macroentrega 1) e a operação comercial plena (Macroentregas 2 e 3), bem como os impactos em disponibilidade, custo e segurança:

**Tabela 6 – Identificação dos Fornecedores e Parceiros Relevantes**

| Fornecedor / Parceiro | Categoria e Serviço Prestado | Plano e Estrutura de Custo Comercial | Impacto Operacional, Disponibilidade e Mitigação de Riscos |
| :--- | :--- | :--- | :--- |
| **Vercel Inc.** | **PaaS & Edge CDN:** Hospedagem da aplicação Next.js 14, execução de funções serverless e distribuição global de ativos estáticos. | **Vercel Pro:**<br>**US$ 20,00 / mês** por desenvolvedor (1 TB de banda e execução concorrente expandida; piloto inicial gratuito em *Hobby Tier*). | **Disponibilidade e Performance:** SLA de 99,99% na borda. Impacta diretamente o acesso ao portal e à bilheteria. Mitigação: build determinístico e rollback instantâneo de release em 1 clique. |
| **Supabase Inc. / Neon Tech** | **DBaaS PostgreSQL:** Persistência relacional ACID, gerenciamento de conexões via *Supavisor* (porta `6543`) e triggers de auditoria. | **Plano Pro Comercial:**<br>**US$ 25,00 a US$ 69,00 / mês** (compute dedicado, 8 GB+ de disco SSD, backups diários e *Point-in-Time Recovery — PITR*). | **Segurança e Integridade:** Crítico para evitar perda de vendas e garantir locks `SELECT FOR UPDATE`. Mitigação: replicação automática, conexões TLS obrigatórias e scripts de migração versionados no Prisma. |
| **Resend Technologies** | **Comunicação Transacional (SaaS):** API REST para entrega de vouchers de reserva e confirmações de ingresso com autenticação DKIM/SPF. | **Resend Pro:**<br>**US$ 20,00 / mês** (franquia de 50.000 e-mails/mês, domínios corporativos verificados `@cinedoom.com.br` e sem limite diário). | **Experiência do Cliente:** Impacta o recebimento do comprovante por e-mail (`CA-11`). Mitigação: desacoplamento via interface `EmailProvider` e exibição imediata do voucher na tela e na área *"Minhas Reservas"*. |
| **Axiom Inc.** | **Observabilidade e Log Drain:** Ingestão contínua de logs estruturados JSON e retenção de longo prazo para auditoria. | **Axiom Cloud Plan:**<br>**US$ 25,00 / mês** (ingestão de até 1 TB/mês e retenção estendida de 365 dias para auditoria legal). | **Conformidade Legal (LGPD):** Essencial para rastreabilidade forense e retenção de 1 ano sem onerar o banco transacional. Mitigação: mascaramento prévio de PII antes do envio do log. |
| **GitHub Inc.** | **Engenharia e CI/CD:** Repositórios Git privados, gestão de backlog (GitHub Projects) e esteira automatizada (GitHub Actions). | **GitHub Team:**<br>**US$ 4,00 / usuário / mês** (3.000 minutos de Actions, branches protegidas e *Codeowners*). | **Qualidade e Governança:** Sustenta a integração contínua e o bloqueio de código defeituoso. Baixo impacto em tempo de execução de produção. |
| **Stripe Inc. / Pagar.me** *(Macroentrega 2)* | **Gateway Financeiro PCI-DSS:** Processamento de pagamentos online via PIX dinâmico e cartões de crédito no Portal do Cliente. | **Taxa Transacional (Pay-go):**<br>**0,99% (PIX) / 3,99% + R$ 0,39 (Cartão)** por transação aprovada (sem mensalidade fixa). | **Segurança Financeira:** Elimina o tráfego de dados sensíveis de cartão nos servidores da CineSoft. Mitigação: webhooks idempotentes e fallback de pagamento presencial no balcão. |
| **Focus NFe / PlugNotas** *(Macroentrega 3)* | **Mensageria Fiscal (SaaS):** Emissão, assinatura digital e transmissão de NFC-e junto às SEFAZ estaduais. | **Plano Empresarial:**<br>**R$ 149,00 / mês** por CNPJ emissor (para até 2.000 notas fiscais/mês, com fila de contingência offline). | **Conformidade Tributária:** Desacopla a CineSoft das variações técnicas de cada estado brasileiro, garantindo emissão assíncrona sem travar a fila física da bilheteria. |

*Fonte: CineSoft Solutions (2026).*

---
