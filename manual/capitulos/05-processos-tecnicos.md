# Capítulo 5 – Processos Técnicos

## 5.1 Requisitos

### 5.1.1 Documento de requisitos do sistema
A especificação oficial do CineDoom ([`specs/cinedoom-spec.md`](../../specs/cinedoom-spec.md)) organiza os artefatos de requisitos em catálogos separados com identificadores únicos padronizados em português, cobrindo os três módulos integrados (Back-office do Gerente, Bilheteria do Atendente e Portal do Cliente) com priorização MoSCoW:
- **Stakeholders (`STK-01` a `STK-05`) e Necessidades Elicitadas (`NEC-01` a `NEC-08`):** Mapeamento de patrocinadores, gerentes, atendentes, espectadores e conformidade regulatória.
- **Histórias de Usuário (`HU-01` a `HU-11`, equiv. `US-1` a `US-11`):** Narrativas ágeis centradas nos atores do sistema.
- **Requisitos Funcionais (`RF-01` a `RF-18`):**
  - **RF-01 a RF-05:** Autenticação RBAC e gestão de operadores (`GERENTE`, `ATENDENTE`, `CLIENTE`), catálogo de filmes, salas/assentos, agendamento de sessões com pré-população de poltronas e mapa interativo com polling a 2s.
  - **RF-06 a RF-11:** Venda direta no balcão com trava atômica (*SELECT FOR UPDATE*), emissão de comprovante, cancelamento auditável *append-only* via trigger PostgreSQL, proteção de PII/LGPD (`HMAC-SHA256` + `AES-256-GCM`), painel de ocupação em tempo real e observabilidade Axiom com retenção legal de 365 dias.
  - **RF-12 a RF-18 (Portal do Cliente e Reserva):** Consulta pública de grade de exibição, reserva de assentos com status `RESERVED`, cadastro e login seguro do espectador com consentimento LGPD, emissão de voucher por e-mail transacional (*NotificationService*), painel web "Minhas Reservas" com cancelamento voluntário pelo cliente, baixa presencial da reserva pelo atendente e expiração *Just-in-Time* para reservas não quitadas a 1 hora da sessão.
- **Requisitos Não Funcionais (`RNF-01` a `RNF-06`, norma ISO/IEC 25010):**
  - **RNF-01 (Eficiência de Desempenho):** Latência p95 < 800 ms e p99 < 1.500 ms para venda/reserva; atualização do mapa em até 2 segundos.
  - **RNF-02 (Confiabilidade e Atomicidade ACID):** Zero vendas ou reservas duplas (*double-booking*) sob concorrência paralela de 50 requisições simultâneas.
  - **RNF-03 (Segurança e Conformidade LGPD):** Isolamento total cross-tenant validado por 500 cenários automatizados e proteção criptográfica de CPF (`HMAC-SHA256` + `AES-256-GCM`).
  - **RNF-04 (Usabilidade e Acessibilidade):** Interface responsiva aderente à WCAG 2.1 Nível AA para o Portal do Cliente e terminais touchscreen de bilheteria.
  - **RNF-05 (Compatibilidade de Navegadores):** Suporte integral a Chromium (Chrome/Edge) e Firefox em resolução mínima de `1024x768` sem dependências nativas.
  - **RNF-06 (Manutenibilidade e Modularidade):** Clean Architecture orientada a funcionalidades com zero dependências circulares verificadas por `ESLint import/no-cycle`.
- **Regras de Negócio (`RN-01` a `RN-12`) e Restrições (`RES-01` a `RES-06`):** Controles determinísticos de RBAC, conflito de salas, trava pessimista, antecedência mínima de 60 minutos, expiração *Just-in-Time* e isolamento por `tenant_id`.

### 5.1.2 Rastreabilidade de requisitos
A integridade da engenharia de software é assegurada pela cadeia de rastreabilidade bidirecional contínua:
$$\text{Stakeholder (STK)} \longrightarrow \text{Necessidade (NEC)} \longrightarrow \text{História (HU)} \longrightarrow \text{RF / RNF / RN} \longrightarrow \text{Critério de Aceite (CA)} \longrightarrow \text{Caso de Teste (CT)} \longrightarrow \text{Código e Deploy}$$

### 5.1.3 Critérios de Aceite (`CA-01` a `CA-14`)
Os 14 critérios de aceite (`CA-01` a `CA-14`, equivalentes às anotações de código `AC-1` a `AC-14`) foram especificados no formato comportamental (*Dado que / Quando / Então*) e validados por 26 casos de teste (`CT-01` a `CT-26`, equiv. `TC-1` a `TC-26`):
1. **Núcleo de Bilheteria, Gestão e Segurança (`CA-01` a `CA-08`):** Trava ACID anti-double-booking (`CA-01`), atualização do mapa em até 2s (`CA-02`), auditoria imutável de cancelamento antes da liberação do assento (`CA-03`), isolamento multi-tenant estrito em 500 cenários (`CA-04`), controle RBAC com bloqueio `HTTP 403` (`CA-05`), proteção LGPD com `HMAC-SHA256` e `AES-256-GCM` (`CA-06`), painel de ocupação gerencial (`CA-07`) e validação descritiva por campo no back-office (`CA-08`).
2. **Fluxos Híbridos do Portal do Cliente (`CA-09` a `CA-14`):** Reserva online com trava atômica e antecedência mínima de 60 min (`CA-09`), autenticação de espectador com proteção LGPD (`CA-10`), despacho de voucher por e-mail transacional (`CA-11`), cancelamento voluntário pelo cliente (`CA-12`), baixa presencial no balcão convertendo reserva em ingresso vendido (`CA-13`) e expiração *Just-in-Time* automática a 1 hora da sessão (`CA-14`).

### 5.1.4 Registro de stakeholders e necessidades elicitadas
Mapeamento formal dos interesses de proprietários e patrocinadores (`STK-01`, `NEC-01`), gerentes de cinema (`STK-02`, `NEC-02`), atendentes de bilheteria (`STK-03`, `NEC-03`), espectadores finais (`STK-04`, `NEC-05` a `NEC-08`) e encarregados de conformidade LGPD (`STK-05`, `NEC-04`).

## 5.2 Arquitetura e Design

### 5.2.1 Documento de arquitetura do sistema
Arquitetura Monólito Modular em Next.js 14 (App Router) organizada em Clean Architecture com fatias verticais de funcionalidades (`src/features/*`) e camadas lógicas estritas (Controller-Service-Repository):
1. **Camada de Apresentação:** React Server Components para o catálogo público e Client Components reativos para o mapa interativo de assentos (polling a 2s), painéis gerenciais e checkout de reserva.
2. **Camada de Aplicação / Controllers:** Route Handlers tipados em TypeScript (`src/app/api/**/route.ts`) atuando como Controllers finos para transporte HTTP e validação de schemas Zod.
3. **Camada de Serviços de Aplicação:** Orquestração de regras de negócio e casos de uso (`FilmService`, `SessionService`, `CounterService`, `ReservationService`, `NotificationService`, `CryptoService`).
4. **Camada de Domínio e Repositórios:** Interfaces de domínio e implementações de repositório (`PrismaFilmRepository`, `PrismaSessionRepository`, `PrismaCounterRepository`, `PrismaReservationRepository`) garantindo inversão de dependência e desacoplamento do ORM.
5. **Camada de Acesso a Dados e Tenancy:** Prisma Client integrado ao Neon PostgreSQL com extensão de contexto para injeção global de filtro `WHERE tenant_id`.

### 5.2.2 Diagramas de design
O design formal do sistema é documentado por meio do conjunto de modelos arquiteturais e diagramas UML/C4:
- **Diagrama C4 Nível 2 (Contêineres):** Demonstra a integração entre o navegador do espectador (Portal do Cliente), o terminal do atendente (Bilheteria), a aplicação Next.js na Vercel, o serviço transacional de e-mails e o banco de dados Neon Serverless.
- **Diagrama de Classes UML (Modelo de Domínio):** Estrutura as classes de domínio (`User`, `Tenant`, `Movie`, `Room`, `Seat`, `Session`, `SessionSeat`, `Reservation`, `Ticket`), evidenciando atributos tipados, métodos operacionais e cardinalidades de associação.
- **Diagrama de Sequência UML (Reserva Atômica e Baixa Presencial):** Ilustra a troca temporal de mensagens entre cliente, servidor Next.js e banco relacional com transação ACID (`SELECT FOR UPDATE`), disparo de voucher e confirmação no balcão.
- **Diagrama de Casos de Uso UML:** Mapeia os atores do sistema (*Espectador*, *Atendente*, *Gerente*) e suas respectivas interações com as funcionalidades do sistema.
- **Diagrama de Estados UML (Ciclo de Vida do Assento):** Mapeia a máquina de estados do assento na sessão: `AVAILABLE` $\to$ `RESERVED` (com expiração JIT) $\to$ `SOLD` (baixa presencial) ou reversão para `AVAILABLE` em caso de cancelamento.
- **Diagrama Entidade-Relacionamento (DER / Modelo de Dados):** Especificação visual do esquema relacional de tabelas, chaves primárias/estrangeiras e índices do banco PostgreSQL.

### 5.2.3 Justificativa das escolhas tecnológicas
A combinação de Next.js 14, Prisma ORM e Neon PostgreSQL viabiliza o desenvolvimento integral dos três módulos dentro do prazo de 21 dias por uma equipe de 4 desenvolvedores, assegurando conformidade ACID nativa e custo de infraestrutura zero no nível de entrada.

### 5.2.4 Estratégia de gestão de mídias e desacoplamento de storage
A persistência de imagens de filmes adota o padrão de desacoplamento de storage: o PostgreSQL registra apenas a URL no campo `poster_url` (`VARCHAR(500)`), eliminando o armazenamento de binários pesados (BLOBs) no banco relacional. No MVP, as imagens são distribuídas pela CDN Edge da Vercel (`/public/posters/`) ou links de CDNs públicas de cinema. Para escala corporativa (cenário não-mockado), a arquitetura define o padrão *Direct-to-Storage* com *Pre-signed URLs* (AWS S3/Cloudflare R2/Vercel Blob), evitando o limite de payload de 4.5 MB das funções serverless, ou integração com a API pública do The Movie Database (TMDB).

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
