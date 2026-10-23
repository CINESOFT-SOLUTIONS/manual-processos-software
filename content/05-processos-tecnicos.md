# Capítulo 5 – Processos Técnicos

## 5.1 Requisitos

### 5.1.1 Documento de requisitos do sistema
Os requisitos do CineDoom cobrem os três módulos integrados (Back-office do Gerente, Bilheteria do Atendente e Portal do Cliente), classificados formalmente em funcionais (RF-01 a RF-18) e não funcionais (RNF-01 a RNF-06), com priorização MoSCoW:
- **RF-01 a RF-06:** Gestão de acesso, acervo de filmes, salas/assentos, sessões e visualização do mapa com polling a 2s.
- **RF-07 a RF-11:** Venda direta no balcão com trava atômica (*SELECT FOR UPDATE*), cancelamento auditável append-only via trigger PostgreSQL, proteção de PII/LGPD (HMAC-SHA256 + AES-256-GCM), painel de ocupação e observabilidade Axiom com retenção legal de 365 dias.
- **RF-12 a RF-18 (Portal do Cliente e Reserva):** Consulta pública de grade de exibição, reserva de assentos com status `RESERVED`, cadastro e login seguro do espectador com consentimento LGPD, emissão de voucher por e-mail transacional (*NotificationService*), painel web "Minhas Reservas" com cancelamento voluntário pelo cliente, baixa presencial da reserva pelo atendente e expiração Just-in-Time para reservas não quitadas a 1 hora da sessão.
- **RNF-01 (Desempenho):** Tempo de resposta para consultas e reservas inferior a 2 segundos (p95 < 800ms).
- **RNF-02 (Confiabilidade Transacional):** Zero conflitos de venda ou reserva dupla sob concorrência paralela de 50 threads simultâneas.
- **RNF-03 (Segurança e LGPD):** Isolamento total cross-tenant e proteção criptográfica de dados de identificação do espectador.
- **RNF-04 (Usabilidade):** Interface responsiva para o Portal do Cliente e layout intuitivo de bilheteria física.

### 5.1.2 Rastreabilidade de requisitos
A integridade da engenharia de software é assegurada pela cadeia de rastreabilidade contínua:
$$\text{Necessidade do Negócio} \longrightarrow \text{RF/RNF} \longrightarrow \text{ADR} \longrightarrow \text{Issue GitHub} \longrightarrow \text{Código-Fonte} \longrightarrow \text{Teste Automatizado} \longrightarrow \text{Deploy Vercel}$$

### 5.1.3 Critérios de aceitação
Os critérios de aceitação foram formalizados para assegurar a consistência dos fluxos híbridos (digital $\to$ presencial):
1. **Reserva Online com Trava Atômica:** A solicitação de reserva no portal valida a antecedência (>60 min), bloqueia o assento com status `RESERVED` no PostgreSQL e despacha o voucher com código alfanumérico e e-mail transacional.
2. **Cancelamento Voluntário pelo Cliente:** O espectador autenticado cancela sua reserva pendente no portal com reversão imediata do assento para `AVAILABLE`.
3. **Baixa Presencial na Bilheteria:** O atendente pesquisa a reserva por código ou CPF, confirma o recebimento presencial e converte a reserva em `Ticket` vendido (`SOLD`).
4. **Expiração Just-in-Time:** Assentos reservados não confirmados até 60 minutos antes da sessão são liberados dinamicamente em tempo de execução nas queries do sistema.

### 5.1.4 Registro de stakeholders e necessidades elicitadas
Mapeamento formal dos interesses de proprietários de cinemas (redução de custos e controle de ocupação), gerentes (agilidade operacional), atendentes de guichê (eliminação de filas e atritos) e espectadores finais (planejamento antecipado com assento garantido).

## 5.2 Arquitetura e Design

### 5.2.1 Documento de arquitetura do sistema
Arquitetura Monólito Modular em Next.js 14 (App Router) estruturada em camadas lógicas:
1. **Camada de Apresentação:** React Server Components para o catálogo público e Client Components reativos para o mapa interativo de assentos (polling a 2s) e checkout de reserva.
2. **Camada de Aplicação / API:** Route Handlers tipados em TypeScript processando requisições REST com validação de schemas Zod.
3. **Camada de Domínio / Negócio:** Serviços encapsulados (`VendaTransactionHandler`, `ReservaTransactionHandler`, `CancelamentoService`, `NotificationService`, `CryptoService`).
4. **Camada de Acesso a Dados:** Prisma Client integrado ao Neon PostgreSQL com extensão de contexto para injeção global de filtro `WHERE tenant_id`.

### 5.2.2 Diagramas de design
- **Diagrama C4 Nível 2 (Contêineres):** Demonstra a integração entre o navegador do espectador (Portal do Cliente), o terminal do atendente (Bilheteria), a aplicação Next.js na Vercel, o serviço transacional de e-mails e o banco de dados Neon Serverless.
- **Diagrama de Atividades (BPMN):** Mapeia o ciclo de vida completo da reserva de assentos: Solicitação no Portal $\to$ Trava `RESERVED` $\to$ Despacho de Voucher $\to$ [Bifurcação: Cancelamento pelo Cliente / Expiração a 1h / Comparecimento Físico com Baixa no Balcão].

### 5.2.3 Justificativa das escolhas tecnológicas
A combinação de Next.js 14, Prisma ORM e Neon PostgreSQL viabiliza o desenvolvimento integral dos três módulos dentro do prazo de 21 dias por uma equipe de 4 desenvolvedores, assegurando conformidade ACID nativa e custo de infraestrutura zero no nível de entrada.

## 5.3 Implementação e Integração

### 5.3.1 Padrões de codificação adotados
Guia estrito de TypeScript (`strict: true`), ESLint configurado contra ciclos de importação (`import/no-cycle`) e Prettier para padronização de formatação em toda a base de código.

### 5.3.2 Plano de integração entre componentes
A integração entre o Portal do Cliente e o Módulo de Bilheteria opera sobre o mesmo schema relacional PostgreSQL. Conflitos de seleção entre um cliente web e um atendente físico são resolvidos deterministicamente pela trava `SELECT FOR UPDATE` na linha de `session_seats`, retornando `HTTP 409 Conflict` em caso de disputa.

### 5.3.3 Registro de testes unitários e de integração
Suíte automatizada com **Vitest** e **Playwright**:
- **Testes Unitários:** Validação de hashing HMAC-SHA256 e cifra AES-256-GCM no `CryptoService`, cálculo de expiração temporal e validação de schemas Zod.
- **Testes de Integração Concorrente:** Simulação de 50 requisições simultâneas disputando o mesmo assento entre reserva web e venda de balcão (`reserva-atomica.test.ts` e `venda-atomica-acid.test.ts`), confirmando zero inconsistências.
- **Testes de Expiração Just-in-Time:** Validação de liberação dinâmica de assento expirado após a barreira de 1 hora (`expiracao-reserva-jit.test.ts`).
- **Testes E2E:** Jornada completa do cliente (cadastro $\to$ escolha de assento $\to$ reserva $\to$ voucher) e atendimento presencial de baixa no balcão.

### 5.3.4 Rastreabilidade entre código e requisitos
Todas as rotas de API, use cases e suites de teste incluem anotações explícitas de rastreabilidade (ex.: `// Requisito: RF-13 | AC-9 | ADR-012`).

## 5.4 Verificação, Validação e Transição

### 5.4.1 Plano de verificação e validação
- **Verificação Contínua:** Pipeline automatizado no GitHub Actions disparado a cada Pull Request (verificação de tipagem TypeScript, linting, testes unitários e integração).
- **Validação com Dados de Caso Real:** Simulação de grade de exibição e carga de espectadores reais para validação perante a banca examinadora da UFG/INF.

### 5.4.2 Critérios de aceitação por stakeholder
- **Espectador:** Facilidade para escolher poltrona, agilidade no recebimento do e-mail com voucher e autonomia para cancelar reservas.
- **Atendente:** Agilidade na localização da reserva pelo código na bilheteria física.
- **Gerente:** Visualização clara das poltronas reservadas versus vendidas no painel de ocupação.

### 5.4.3 Relatório de testes de aceitação
Documentação formal dos testes executados com evidências de aprovação dos cenários de concorrência e conformidade regulatória.

### 5.4.4 Plano de transição/implantação do sistema
Deploy contínuo automatizado na Vercel para branches aprovadas, com migrações de banco executadas via `prisma migrate deploy` sobre branches dedicadas do banco Neon.

## 5.5 Operação, Manutenção e Descontinuação

### 5.5.1 Procedimentos de operação e monitoramento
Monitoramento contínuo de latência, taxa de erro HTTP e integridade transacional via Axiom Log Drain e painel analítico da Vercel.

### 5.5.2 Plano de manutenção (corretiva, preventiva, adaptativa)
Fluxo ágil de tratamento de incidentes operacionais via issues categorizadas por severidade no GitHub Projects da organização.

### 5.5.3 Estratégia de descontinuação e privacidade de dados
Procedimento de encerramento seguro de tenant com geração de dump completo em SQL e expurgo de dados pessoais conforme os princípios de finalidade, necessidade e segurança da LGPD (Art. 6º e Art. 18).
