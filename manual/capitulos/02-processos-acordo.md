# Capítulo 2 – Processos de Acordo

Este capítulo estabelece como a **CineSoft Solutions** gerencia suas relações comerciais e técnicas, fundamentando-se nas boas práticas da norma ABNT NBR ISO/IEC/IEEE 12207:2021 para os processos de **Aquisição** e **Fornecimento**. 

A abordagem adotada busca equilibrar rigor de engenharia e pragmatismo operacional: define claramente o que construir internamente versus o que contratar de terceiros (*Make or Buy*), estrutura a jornada de entrega e suporte da plataforma **CineDoom** para os cinemas clientes, e mapeia os parceiros de infraestrutura que viabilizam o sistema.

---

## 2.1 Processo de Aquisição: Decisões e Gestão de Provedores

No papel de adquirente, a CineSoft Solutions adota uma diretriz clara: **o esforço interno de desenvolvimento é concentrado no coração das regras de negócio do cinema e nos diferenciais competitivos do CineDoom**. Todo serviço em que o mercado já oferece soluções maduras, seguras e com economia de escala é contratado como serviço ou biblioteca, reduzindo tempo de desenvolvimento e custo operacional.

### O que construímos e o que contratamos (*Make or Buy*)

- **Desenvolvimento Interno (*Make*):** O motor de bilheteria e reservas atômicas com bloqueio pessimista (`SELECT FOR UPDATE`), a máquina de estados de assentos com liberação automática de ingressos expirados, o isolamento lógico multi-tenant entre diferentes redes de cinema e os mecanismos de anonimização exigidos pela LGPD. Esses itens compõem a propriedade intelectual e o diferencial de confiabilidade da CineSoft.
- **Soluções Prontas de Terceiros (*Buy*):** Infraestrutura de banco de dados gerenciado (PostgreSQL no Supabase), hospedagem serverless com distribuição global (Vercel), mensageria de e-mails transacionais (Resend), retenção de logs para auditoria (Axiom), processamento de pagamentos digitais (Stripe/Pagar.me na Macroentrega 2) e mensageria fiscal de notas (Focus NFe na Macroentrega 3).

As tabelas a seguir detalham a justificativa técnica e econômica de cada decisão:

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
| **Banco de Dados Relacional Gerenciado (DBaaS)** | **Sim** | Elimina custos de DBA, provendo restauração pontual automatizada (PITR), *connection pooling* para serverless e alta disponibilidade ($\ge 99,9\%$). | **Supabase Pro (PostgreSQL)** |
| **Plataforma de Hospedagem Serverless e CDN** | **Sim** | Elimina a manutenção de servidores dedicados, entregando deploys atômicos com reversão para a versão anterior, proteção DDoS e distribuição global na borda. | **Vercel Pro** (Cloud PaaS) |
| **Serviço de Disparo de E-mails Transacionais** | **Sim** | Evita que vouchers caiam em caixas de spam; a API especializada assegura entrega em milissegundos com autenticação SPF, DKIM e DMARC. | **Resend** (SaaS de E-mail Transacional) |
| **Observabilidade e Retenção Legal de Logs** | **Sim** | Cumpre a retenção legal de logs por 1 ano (Marco Civil e LGPD) sem sobrecarregar o armazenamento do banco relacional, com busca indexada rápida. | **Axiom Cloud** (Log Drain SaaS) |
| **Gateway de Pagamento Online (Macroentrega 2)** | **Sim** | Transfere a complexidade regulatória da certificação PCI-DSS Nível 1 e antifraude, automatizando a liquidação de PIX dinâmico e cartões. | **Stripe / Pagar.me** |
| **Motor de Mensageria Fiscal NFC-e (Macroentrega 3)** | **Sim** | Abstrai as constantes mudanças tributárias estaduais da SEFAZ, contingência offline e assinatura digital com certificado A1, evitando passivos fiscais. | **Focus NFe / PlugNotas** |

*Fonte: CineSoft Solutions (2026).*

### O Ciclo Prático de Aquisição de Provedores

Para selecionar e manter esses provedores em operação contínua, a CineSoft Solutions estrutura a contratação em cinco etapas práticas:

1. **Definição de Requisitos e Critérios:** O Arquiteto e os líderes técnicos mapeiam as restrições de cada necessidade — limites de latência (priorizando servidores na América do Sul), compatibilidade com Node.js/Next.js, conformidade com a LGPD e facilidade de integração local.
2. **Avaliação Técnica e Financeira:** São realizados testes práticos de integração (provas de conceito) entre alternativas de mercado (por exemplo, comparando Supabase versus PostgreSQL autogerenciado, ou Resend versus AWS SES), analisando a previsibilidade de custos à medida que o volume de bilheteria cresce.
3. **Contratação e Formalização:** Assinatura digital dos planos corporativos, formalização de Aditivos de Proteção de Dados (*Data Processing Agreements* – DPA) para garantir sigilo sob a LGPD e armazenamento seguro de chaves de API em gerenciadores de segredos com rotação periódica.
4. **Monitoramento e Acompanhamento de SLA:** A equipe monitora a disponibilidade real dos provedores via telemetria contínua, páginas de status e relatórios mensais de consumo, garantindo que o tempo de resposta e a taxa de erros permaneçam dentro dos padrões acordados.
5. **Homologação e Aceite Técnico:** Antes de qualquer serviço entrar em produção com clientes reais, o fluxo é validado em ambiente de testes (*sandbox*) na esteira de integração contínua (CI/CD), com procedimento de reversão (*rollback*) documentado caso ocorram falhas.

---

## 2.2 Processo de Fornecimento: Comercialização, Entrega e Operação

Como fornecedora de software, a CineSoft Solutions atende cinemas independentes, cinemas de rua e pequenas redes de exibição que buscam modernizar sua bilheteria física e expandir suas vendas online de forma integrada e sem riscos de sobreposição de assentos.

### Modelos de Negócio e Ativos Disponíveis

O principal produto fornecido é a plataforma **CineDoom** em modelo SaaS (*Software as a Service*), cobrada por assinatura mensal mais taxa por sala ativa. No entanto, sua arquitetura modular também permite licenciar componentes específicos para parceiros ou exibidores com sistemas legados:

**Tabela 4 – Perspectiva de Fornecimento e Ativos Comercializáveis**

| Ativo potencial                 | Possíveis adquirentes                                                                          | Modelo de fornecimento e preço estimado                                                                          |
| ------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Plataforma CineDoom (completa)  | Cinemas independentes, cinemas de rua e pequenas redes de exibição.                            | SaaS B2B: R$ 790/mês de assinatura-base, acrescidos de R$ 120/mês por sala ativa e R$ 1.500 de implantação (faixa efetiva de R$ 910 a R$ 1.270/mês para complexos de uma a quatro salas). |
| Engine de Trava Atômica (API)   | Plataformas de venda de ingressos, teatros e sistemas de reservas de eventos.                  | Licenciamento de API: R$ 0,08 por assento confirmado, com cobrança mínima de R$ 200/mês.                         |
| Módulo de Governança LGPD (SDK) | Empresas de desenvolvimento de software e plataformas de entretenimento.                       | Licenciamento de SDK: R$ 8.900/ano ou R$ 16.000 por licença perpétua, incluindo 10 horas de consultoria técnica. |
| Portal White-Label de Reservas  | Exibidores que utilizam sistemas administrativos próprios e desejam oferecer reservas on-line. | SaaS White-Label: R$ 490/mês por exibidor, com domínio próprio, SSL e taxa de implantação de R$ 800.             |

*Fonte: CineSoft Solutions (2026). Valores comerciais estimados para fins de planejamento.*

### Jornada do Cliente: Da Contratação ao Pós-Venda

A relação entre a CineSoft Solutions e o cinema contratante segue um ciclo transparente e estruturado em cinco etapas:

1. **Alinhamento e Diagnóstico Inicial:** A CineSoft compreende o perfil do cinema — quantidade de salas físicas, categorias de poltronas, volume médio de sessões semanais e necessidade de equipamentos físicos de guichê.
2. **Proposta e Escopo de Implantação:** Apresentação da proposta comercial contendo valores claros, cronograma de parametrização e requisitos mínimos de rede e navegadores para os computadores da bilheteria.
3. **Formalização Contratual:** Assinatura do Contrato de Licenciamento SaaS e do Termo de Tratamento de Dados (LGPD), definindo os níveis de serviço garantidos (SLA de 99,5%), a propriedade exclusiva dos dados pelo cinema e as regras de confidencialidade.
4. **Implantação e Treinamento:** Provisionamento do ambiente isolado do cinema (`tenant_id`), cadastro de salas e filmes, simulação de vendas com a equipe de atendentes e treinamento operacional dos gerentes de bilheteria.
5. **Entrada em Operação e Suporte Contínuo:** Liberação assistida do primeiro dia de operação em guichê (*go-live* assistido), assinatura do Termo de Aceite após comprovação prática de ausência de erros ou vendas duplicadas, e início do suporte técnico diário.

### Entregáveis da Implantação e Evolução Funcional

Cada cinema contratante recebe:
- **Tenant Exclusivo e Isolado:** Criação do identificador da organização (`tenant_id`) no banco de dados com isolamento lógico garantido em todas as consultas.
- **Configuração de Salas e Catálogo:** Montagem do mapa visual de poltronas de cada sala física (comun, VIP, acessibilidade) e treinamento prático para cadastro de sessões e preços.
- **Manual do Operador e Capacitação:** Guia rápido de utilização do ponto de venda no balcão e no portal web.
- **Evolução Contínua em Três Fases (Macroentregas):**
  - *Fase 1 (Atual):* Bilheteria presencial completa, controle de sessões, catálogo de filmes e portal web de reserva antecipada com pagamento no balcão.
  - *Fase 2 (Próxima):* Venda online direta com pagamento imediato via PIX dinâmico e cartão, com emissão de vouchers digitais no e-mail do cliente.
  - *Fase 3 (Futura):* Emissão integrada de notas fiscais (NFC-e na SEFAZ), controle de vendas de bomboniere/pipoca e relatórios consolidados de faturamento.

### Critérios de Aceite Formal

O cinema cliente formaliza a aceitação do sistema quando os seguintes requisitos são atendidos:
1. Aprovação de todos os testes da suíte automatizada do sistema (26 arquivos e 770 testes) e execução bem-sucedida dos testes práticos de balcão.
2. Inexistência de qualquer defeito impeditivo ou crítico em aberto.
3. Comprovação prática de que a trava atômica impede rigorosamente a venda simultânea da mesma poltrona entre a web e o guichê.
4. Assinatura do Termo de Aceite de Implantação (TAI) pelo responsável do cinema.

### Níveis de Serviço (SLA) e Atendimento

Para manter a bilheteria funcionando sem interrupções nas horas de pico (finais de semana e estreias), a CineSoft estabelece tempos máximos de resposta e resolução:

**Tabela 5 – Acordo de Nível de Serviço (SLA) e Suporte Pós-Entrega**

| Severidade / Modalidade | Descrição do Cenário | Tempo de 1ª Resposta | Meta de Resolução / Contorno |
| :--- | :--- | :---: | :---: |
| **Crítica (P1 — Corretiva Urgente)** | Indisponibilidade total da bilheteria ou falha na emissão de ingressos em horário de sessão. | Até **15 minutos** | Até **2 horas** (reversão documentada para a versão anterior) |
| **Alta (P2 — Corretiva Prioritária)** | Degradação no painel gerencial, falha no envio de voucher por e-mail ou lentidão acima do SLA. | Até **1 hora** | Até **8 horas** |
| **Normal (P3 — Adaptativa / Preventiva)** | Ajustes de compatibilidade de navegador, dúvidas operacionais ou otimização preventiva de índices. | Até **4 horas úteis** | Até **24 horas úteis** |
| **Evolutiva (P4 — Perfectiva)** | Solicitação de novos relatórios, filtros ou melhorias de usabilidade no Portal do Cliente. | Até **2 dias úteis** | Planejada na próxima *Sprint / Release* |

*Fonte: CineSoft Solutions (2026).*

---

## 2.3 Fornecedores e Parceiros de Tecnologia

Para manter a plataforma CineDoom estável, rápida e segura com custos proporcionais à escala dos cinemas, a CineSoft selecionou parceiros especializados para cada camada do sistema:

**Tabela 6 – Identificação dos Fornecedores e Parceiros Relevantes**

| Fornecedor | Categoria e serviço | Plano e custo comercial | Impacto e mitigação de riscos |
| :--- | :--- | :--- | :--- |
| **Vercel Inc.** | **PaaS & CDN Edge:** Next.js 14 e serverless | **US$ 20/mês** por dev (Vercel Pro; piloto Hobby grátis) | SLA 99,99% na borda. Mitigação: build determinístico e rollback instantâneo. |
| **Supabase** | **DBaaS PostgreSQL:** Persistência ACID e pooling | **US$ 25 a US$ 69/mês** (Plano Pro compute dedicado) | Crítico para locks `SELECT FOR UPDATE`. Mitigação: réplicas e migrações Prisma. |
| **Resend** | **E-mail transacional:** API de vouchers (DKIM/SPF) | **US$ 20/mês** (franquia de 50.000 e-mails/mês) | Impacta envio de voucher (`CA-11`). Mitigação: exibição imediata em tela. |
| **Axiom Inc.** | **Log drain:** Observabilidade e auditoria LGPD | **US$ 25/mês** (1 TB/mês; retenção de 365 dias) | Rastreabilidade legal (Marco Civil/LGPD). Mitigação: mascaramento de PII. |
| **GitHub Inc.** | **CI/CD & Git:** Repositórios e GitHub Actions | **US$ 4/usuário/mês** (Plano Team e branch rules) | Sustenta testes automatizados. Mitigação: bloqueio de merge sem testes. |
| **Stripe / Pagar.me** *(M2)* | **Gateway financeiro:** Checkout PIX e cartão | **0,99% PIX / 3,99% + R$ 0,39 Cartão** (sem mensalidade) | Certificação PCI-DSS. Mitigação: webhooks idempotentes e balcão físico. |
| **Focus NFe** *(M3)* | **Mensageria fiscal:** Emissão de NFC-e SEFAZ | **R$ 149/mês** (até 2.000 notas fiscais/mês) | Conformidade tributária. Mitigação: fila assíncrona com contingência offline. |

*Fonte: CineSoft Solutions (2026).*
