---
document_id: SPEC-CINEDOOM-DATA-MODEL-001
version: "2.0.0"
date: "2026-11-05"
status: "Aprovado e Consolidado"
standard: "ABNT NBR ISO/IEC/IEEE 12207:2021 (Cláusula 6.4.5 — Definição de Design)"
title: "Especificação do Modelo de Dados e Esquema Relacional — CineDoom"
---

# Especificação do Modelo de Dados e Esquema Relacional — CineDoom

> **Documento Técnico Oficial — CineSoft Solutions (UFG/INF — Processos de Software 2026/1)**
> Rastreabilidade direta com [`cinedoom-spec.md`](../cinedoom-spec.md) (`RF-01` a `RF-18`, `RNF-01` a `RNF-06`, `RN-01` a `RN-12`, `CA-01` a `CA-14`, `RES-01` a `RES-06`) e [`ADR-002` a `ADR-014`](../adr/).

## Resumo Executivo

Modelo de dados relacional para a plataforma B2B SaaS **CineDoom**: 11 entidades cobrindo isolamento multi-tenant (`Tenant`), autenticação e controle de acesso RBAC para Atendente, Gerente e Espectador (`User`), catálogo cinematográfico (`Film`), salas e layout físico de poltronas (`Room` e `Seat`), sessões de exibição com mapa de status pré-populado (`Session` e `SessionSeat` para trava pessimista `SELECT FOR UPDATE` anti-double-booking e reserva temporária), reservas online com expiração *Just-in-Time* (`Reservation`), venda de ingressos (`Ticket`), compradores com dados pessoais protegidos conforme a LGPD (`Buyer`) e trilha de auditoria imutável de cancelamentos (`CancellationAudit`). O isolamento lógico é garantido por `tenant_id` em esquema compartilhado (*shared schema*) no PostgreSQL 16 gerenciado no Supabase (`RES-02`, `RN-12`, `CA-04`).

---

## 1. Entidades do Modelo de Dados

### E-1. Tenant (Cinema Cliente B2B)

- **Padrão de Chave Primária:** `UUID-PK`
- **Requisitos Relacionados:** `RNF-03`, `RN-12`, `CA-04`, `RES-02`, `RES-03`

| Campo | Tipo | Nulo | Indexado | PII |
|---|---|---|---|---|
| `id` | `uuid` |  |  |  |
| `name` | `string` |  |  |  |
| `slug` | `string` |  | ✓ |  |
| `active` | `boolean` |  |  |  |
| `created_at` | `timestamp` |  |  |  |

### E-2. User (Usuário Autenticado: Atendente, Gerente ou Cliente)

- **Padrão de Chave Primária:** `UUID-PK`
- **Requisitos Relacionados:** `RF-01`, `RF-14`, `RNF-03`, `RN-01`, `CA-05`, `CA-10`

| Campo | Tipo | Nulo | Indexado | PII |
|---|---|---|---|---|
| `id` | `uuid` |  |  |  |
| `tenant_id` | `uuid` |  | ✓ |  |
| `email` | `string` |  | ✓ | ⚠ |
| `name` | `string` |  |  | ⚠ |
| `password_hash` | `string` |  |  |  |
| `role` | `string` |  | ✓ |  |
| `active` | `boolean` |  |  |  |
| `created_at` | `timestamp` |  |  |  |

### E-3. Film (Filme do Catálogo)

- **Padrão de Chave Primária:** `UUID-PK`
- **Requisitos Relacionados:** `RF-02`, `RF-12`, `RN-02`, `CA-08`

| Campo | Tipo | Nulo | Indexado | PII |
|---|---|---|---|---|
| `id` | `uuid` |  |  |  |
| `tenant_id` | `uuid` |  | ✓ |  |
| `title` | `string` |  |  |  |
| `director` | `string` | ✓ |  |  |
| `duration_minutes` | `int` |  |  |  |
| `rating` | `string` | ✓ |  |  |
| `synopsis` | `text` | ✓ |  |  |
| `poster_url` | `string` | ✓ |  |  |
| `created_at` | `timestamp` |  |  |  |
| `updated_at` | `timestamp` |  |  |  |

> **Nota de Arquitetura (`poster_url`):** Armazena exclusivamente a URL HTTPS do cartaz (`VARCHAR(500)`). Rejeita dados binários (BLOBs) para preservar o isolamento ACID e a performance do banco. No MVP, aponta para assets locais (`/public/posters/`) servidos via Edge Network da Vercel; em escala de produção, integra com *Direct-to-Storage* (*Pre-signed URLs* em AWS S3 / Cloudflare R2 / Vercel Blob) ou URLs da CDN oficial da API do TMDB.

### E-4. Room (Sala de Exibição)

- **Padrão de Chave Primária:** `UUID-PK`
- **Requisitos Relacionados:** `RF-03`, `RN-02`, `CA-08`

| Campo | Tipo | Nulo | Indexado | PII |
|---|---|---|---|---|
| `id` | `uuid` |  |  |  |
| `tenant_id` | `uuid` |  | ✓ |  |
| `name` | `string` |  |  |  |
| `capacity` | `int` |  |  |  |
| `layout_metadata` | `jsonb` | ✓ |  |  |
| `created_at` | `timestamp` |  |  |  |
| `updated_at` | `timestamp` |  |  |  |

### E-5. Seat (Poltrona Física da Sala)

- **Padrão de Chave Primária:** `UUID-PK`
- **Requisitos Relacionados:** `RF-03`, `RF-04`, `CA-08`

| Campo | Tipo | Nulo | Indexado | PII |
|---|---|---|---|---|
| `id` | `uuid` |  |  |  |
| `room_id` | `uuid` |  | ✓ |  |
| `tenant_id` | `uuid` |  | ✓ |  |
| `row_label` | `string` |  |  |  |
| `column_number` | `int` |  |  |  |
| `seat_code` | `string` |  |  |  |
| `status` | `string` |  |  |  |
| `created_at` | `timestamp` |  |  |  |

### E-6. Session (Sessão de Exibição)

- **Padrão de Chave Primária:** `UUID-PK`
- **Requisitos Relacionados:** `RF-04`, `RF-10`, `RF-12`, `RN-03`, `RN-04`, `CA-07`, `CA-08`

| Campo | Tipo | Nulo | Indexado | PII |
|---|---|---|---|---|
| `id` | `uuid` |  |  |  |
| `tenant_id` | `uuid` |  | ✓ |  |
| `film_id` | `uuid` |  | ✓ |  |
| `room_id` | `uuid` |  | ✓ |  |
| `starts_at` | `timestamp` |  | ✓ |  |
| `price` | `numeric` |  |  |  |
| `status` | `string` |  | ✓ |  |
| `created_at` | `timestamp` |  |  |  |
| `updated_at` | `timestamp` |  |  |  |

### E-7. SessionSeat (Estado do Assento na Sessão)

- **Padrão de Chave Primária:** `UUID-PK`
- **Requisitos Relacionados:** `RF-04`, `RF-05`, `RF-06`, `RF-13`, `RF-18`, `RN-04`, `RN-05`, `RN-08`, `RN-11`, `CA-01`, `CA-02`, `CA-09`, `CA-14`

| Campo | Tipo | Nulo | Indexado | PII |
|---|---|---|---|---|
| `id` | `uuid` |  |  |  |
| `session_id` | `uuid` |  | ✓ |  |
| `seat_id` | `uuid` |  | ✓ |  |
| `tenant_id` | `uuid` |  | ✓ |  |
| `status` | `string` |  | ✓ |  |
| `reservation_id` | `uuid` | ✓ |  |  |
| `reservation_expires_at` | `timestamp` | ✓ |  |  |
| `updated_at` | `timestamp` |  |  |  |

### E-8. Buyer (Comprador / Titular de Dados LGPD)

- **Padrão de Chave Primária:** `UUID-PK`
- **Requisitos Relacionados:** `RF-09`, `RNF-03`, `RN-07`, `CA-06`

| Campo | Tipo | Nulo | Indexado | PII |
|---|---|---|---|---|
| `id` | `uuid` |  |  |  |
| `tenant_id` | `uuid` |  | ✓ |  |
| `name` | `string` |  |  | ⚠ |
| `email` | `string` |  | ✓ | ⚠ |
| `cpf_hash` | `string` |  | ✓ |  |
| `cpf_encrypted` | `text` |  |  | ⚠ |
| `lgpd_consent_at` | `timestamp` |  |  |  |
| `created_at` | `timestamp` |  |  |  |

### E-9. Ticket (Ingresso Emitido)

- **Padrão de Chave Primária:** `UUID-PK`
- **Requisitos Relacionados:** `RF-06`, `RF-07`, `RF-17`, `RN-05`, `RN-10`, `CA-01`, `CA-13`

| Campo | Tipo | Nulo | Indexado | PII |
|---|---|---|---|---|
| `id` | `uuid` |  |  |  |
| `tenant_id` | `uuid` |  | ✓ |  |
| `session_id` | `uuid` |  | ✓ |  |
| `seat_id` | `uuid` |  | ✓ |  |
| `buyer_id` | `uuid` |  | ✓ |  |
| `sold_by_user_id` | `uuid` |  | ✓ |  |
| `status` | `string` |  | ✓ |  |
| `price` | `numeric` |  |  |  |
| `sold_at` | `timestamp` |  |  |  |
| `created_at` | `timestamp` |  |  |  |

### E-10. CancellationAudit (Auditoria Imutável de Cancelamento)

- **Padrão de Chave Primária:** `UUID-PK`
- **Requisitos Relacionados:** `RF-08`, `RN-06`, `CA-03`

| Campo | Tipo | Nulo | Indexado | PII |
|---|---|---|---|---|
| `id` | `uuid` |  |  |  |
| `tenant_id` | `uuid` |  | ✓ |  |
| `ticket_id` | `uuid` |  | ✓ |  |
| `cancelled_by_user_id` | `uuid` |  | ✓ |  |
| `reason` | `text` |  |  |  |
| `cancelled_at` | `timestamp` |  |  |  |

### E-11. Reservation (Reserva Online com Expiração Just-in-Time)

- **Padrão de Chave Primária:** `UUID-PK`
- **Requisitos Relacionados:** `RF-13`, `RF-15`, `RF-16`, `RF-17`, `RF-18`, `RN-08`, `RN-09`, `RN-10`, `RN-11`, `CA-09` a `CA-14`

| Campo | Tipo | Nulo | Indexado | PII |
|---|---|---|---|---|
| `id` | `uuid` |  |  |  |
| `code` | `string` |  | ✓ |  |
| `tenant_id` | `uuid` |  | ✓ |  |
| `session_id` | `uuid` |  | ✓ |  |
| `user_id` | `uuid` | ✓ | ✓ |  |
| `buyer_id` | `uuid` | ✓ | ✓ |  |
| `buyer_name` | `string` |  |  | ⚠ |
| `buyer_email` | `string` |  | ✓ | ⚠ |
| `buyer_cpf_hash` | `string` |  | ✓ |  |
| `buyer_cpf_encrypted` | `text` |  |  | ⚠ |
| `status` | `string` |  | ✓ |  |
| `total_price` | `numeric` |  |  |  |
| `expires_at` | `timestamp` |  | ✓ |  |
| `email_sent_at` | `timestamp` | ✓ |  |  |
| `confirmed_at` | `timestamp` | ✓ |  |  |
| `cancelled_at` | `timestamp` | ✓ |  |  |
| `created_at` | `timestamp` |  |  |  |
| `updated_at` | `timestamp` |  |  |  |

---

## 2. Relacionamentos e Integridade Referencial

| ID | Entidade Origem | Cardinalidade | Entidade Destino | Chave Estrangeira (FK) | Política `onDelete` |
|---|---|---|---|---|---|
| R-1 | Tenant | `1:N` (`oneToMany`) | User | `tenant_id` | `CASCADE` |
| R-2 | Tenant | `1:N` (`oneToMany`) | Film | `tenant_id` | `CASCADE` |
| R-3 | Tenant | `1:N` (`oneToMany`) | Room | `tenant_id` | `CASCADE` |
| R-4 | Tenant | `1:N` (`oneToMany`) | Session | `tenant_id` | `CASCADE` |
| R-5 | Room | `1:N` (`oneToMany`) | Seat | `room_id` | `CASCADE` |
| R-6 | Film | `1:N` (`oneToMany`) | Session | `film_id` | `RESTRICT` |
| R-7 | Room | `1:N` (`oneToMany`) | Session | `room_id` | `RESTRICT` |
| R-8 | Session | `1:N` (`oneToMany`) | SessionSeat | `session_id` | `CASCADE` |
| R-9 | Seat | `1:N` (`oneToMany`) | SessionSeat | `seat_id` | `RESTRICT` |
| R-10 | Session | `1:N` (`oneToMany`) | Ticket | `session_id` | `RESTRICT` |
| R-11 | Buyer | `1:N` (`oneToMany`) | Ticket | `buyer_id` | `RESTRICT` |
| R-12 | User | `1:N` (`oneToMany`) | Ticket | `sold_by_user_id` | `RESTRICT` |
| R-13 | Ticket | `1:1` (`oneToOne`) | CancellationAudit | `ticket_id` | `RESTRICT` |
| R-14 | User | `1:N` (`oneToMany`) | CancellationAudit | `cancelled_by_user_id` | `RESTRICT` |
| R-15 | Tenant | `1:N` (`oneToMany`) | Reservation | `tenant_id` | `RESTRICT` |
| R-16 | Session | `1:N` (`oneToMany`) | Reservation | `session_id` | `RESTRICT` |
| R-17 | User | `1:N` (`oneToMany`) | Reservation | `user_id` | `RESTRICT` |
| R-18 | Buyer | `1:N` (`oneToMany`) | Reservation | `buyer_id` | `RESTRICT` |
| R-19 | Reservation | `1:N` (`oneToMany`) | SessionSeat | `reservation_id` | `SET NULL` |

---

## 3. Índices de Desempenho

| Entidade | Campos Indexados | Tipo de Índice | Único |
|---|---|---|---|
| User | `tenant_id, email` | `btree` | ✓ |
| SessionSeat | `session_id, status` | `btree` |  |
| Buyer | `tenant_id, cpf_hash` | `btree` |  |
| Session | `tenant_id, starts_at` | `btree` |  |
| Ticket | `session_id, seat_id` | `btree` | ✓ |
| Reservation | `status, expires_at` | `btree` |  |
| CancellationAudit | `cancelled_at` | `brin` |  |

---

## 4. Esquema DDL (Supabase PostgreSQL 16)

```sql
-- ============================================================
-- CineDoom SaaS — DDL PostgreSQL (Supabase)
-- ============================================================

CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- ------------------------------------------------------------
-- E-1: Tenant
-- ------------------------------------------------------------
CREATE TABLE tenants (
  id          UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  name        VARCHAR(255) NOT NULL,
  slug        VARCHAR(100) NOT NULL UNIQUE,
  active      BOOLEAN      NOT NULL DEFAULT true,
  created_at  TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);

-- ------------------------------------------------------------
-- E-2: User (Atendente / Gerente / Cliente)
-- ------------------------------------------------------------
CREATE TABLE users (
  id            UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id     UUID        NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
  email         VARCHAR(255) NOT NULL,
  name          VARCHAR(255) NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  role          VARCHAR(20)  NOT NULL CHECK (role IN ('ATENDENTE','GERENTE','CLIENTE')),
  active        BOOLEAN      NOT NULL DEFAULT true,
  created_at    TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
  UNIQUE (tenant_id, email)
);
CREATE INDEX idx_users_tenant_id ON users(tenant_id);
CREATE INDEX idx_users_role      ON users(role);

-- ------------------------------------------------------------
-- E-3: Film
-- ------------------------------------------------------------
CREATE TABLE films (
  id               UUID         PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id        UUID         NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
  title            VARCHAR(255) NOT NULL,
  director         VARCHAR(255),
  duration_minutes INT          NOT NULL,
  rating           VARCHAR(10),
  synopsis         TEXT,
  poster_url       VARCHAR(500),
  created_at       TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
  updated_at       TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_films_tenant_id ON films(tenant_id);

-- ------------------------------------------------------------
-- E-4: Room
-- ------------------------------------------------------------
CREATE TABLE rooms (
  id              UUID         PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id       UUID         NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
  name            VARCHAR(100) NOT NULL,
  capacity        INT          NOT NULL,
  layout_metadata JSONB,
  created_at      TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
  updated_at      TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_rooms_tenant_id ON rooms(tenant_id);

-- ------------------------------------------------------------
-- E-5: Seat
-- ------------------------------------------------------------
CREATE TABLE seats (
  id            UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  room_id       UUID        NOT NULL REFERENCES rooms(id) ON DELETE CASCADE,
  tenant_id     UUID        NOT NULL,
  row_label     VARCHAR(10)  NOT NULL,
  column_number INT          NOT NULL,
  seat_code     VARCHAR(20)  NOT NULL,
  status        VARCHAR(20)  NOT NULL DEFAULT 'AVAILABLE'
                             CHECK (status IN ('AVAILABLE','BLOCKED')),
  created_at    TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
  UNIQUE (room_id, row_label, column_number)
);
CREATE INDEX idx_seats_room_id   ON seats(room_id);
CREATE INDEX idx_seats_tenant_id ON seats(tenant_id);

-- ------------------------------------------------------------
-- E-6: Session
-- ------------------------------------------------------------
CREATE TABLE sessions (
  id         UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id  UUID        NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
  film_id    UUID        NOT NULL REFERENCES films(id)   ON DELETE RESTRICT,
  room_id    UUID        NOT NULL REFERENCES rooms(id)   ON DELETE RESTRICT,
  starts_at  TIMESTAMPTZ NOT NULL,
  price      NUMERIC(10,2) NOT NULL,
  status     VARCHAR(20)  NOT NULL DEFAULT 'SCHEDULED'
             CHECK (status IN ('SCHEDULED','OPEN','CLOSED','CANCELLED')),
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_sessions_tenant_id ON sessions(tenant_id);
CREATE INDEX idx_sessions_starts_at ON sessions(starts_at);
CREATE INDEX idx_sessions_status    ON sessions(status);
CREATE INDEX idx_sessions_film_id   ON sessions(film_id);
CREATE INDEX idx_sessions_room_id   ON sessions(room_id);

-- ------------------------------------------------------------
-- E-8: Buyer (PII: nome, e-mail, CPF cifrado AES-256-GCM + HMAC-SHA256)
-- ------------------------------------------------------------
CREATE TABLE buyers (
  id               UUID         PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id        UUID         NOT NULL REFERENCES tenants(id) ON DELETE RESTRICT,
  name             VARCHAR(255) NOT NULL,          -- PII
  email            VARCHAR(255) NOT NULL,          -- PII
  cpf_hash         CHAR(64)     NOT NULL,          -- HMAC-SHA256 hex para lookup indexado
  cpf_encrypted    TEXT         NOT NULL,          -- AES-256-GCM (PII)
  lgpd_consent_at  TIMESTAMPTZ  NOT NULL,
  created_at       TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_buyers_tenant_id  ON buyers(tenant_id);
CREATE INDEX idx_buyers_cpf_hash   ON buyers(cpf_hash);
CREATE INDEX idx_buyers_tenant_cpf ON buyers(tenant_id, cpf_hash);

-- ------------------------------------------------------------
-- E-11: Reservation (Reserva pública online com expiração Just-in-Time)
-- ------------------------------------------------------------
CREATE TABLE reservations (
  id                  UUID          PRIMARY KEY DEFAULT gen_random_uuid(),
  code                VARCHAR(10)   NOT NULL UNIQUE,
  tenant_id           UUID          NOT NULL REFERENCES tenants(id) ON DELETE RESTRICT,
  session_id          UUID          NOT NULL REFERENCES sessions(id) ON DELETE RESTRICT,
  user_id             UUID          REFERENCES users(id) ON DELETE RESTRICT,
  buyer_id            UUID          REFERENCES buyers(id) ON DELETE RESTRICT,
  buyer_name          VARCHAR(255)  NOT NULL,
  buyer_email         VARCHAR(255)  NOT NULL,
  buyer_cpf_hash      CHAR(64)      NOT NULL,
  buyer_cpf_encrypted TEXT          NOT NULL,
  status              VARCHAR(20)   NOT NULL DEFAULT 'PENDING'
                      CHECK (status IN ('PENDING','CONFIRMED','CANCELLED','EXPIRED')),
  total_price         NUMERIC(10,2) NOT NULL,
  expires_at          TIMESTAMPTZ   NOT NULL,
  email_sent_at       TIMESTAMPTZ,
  confirmed_at        TIMESTAMPTZ,
  cancelled_at        TIMESTAMPTZ,
  created_at          TIMESTAMPTZ   NOT NULL DEFAULT NOW(),
  updated_at          TIMESTAMPTZ   NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_reservations_tenant_id      ON reservations(tenant_id);
CREATE INDEX idx_reservations_code           ON reservations(code);
CREATE INDEX idx_reservations_user_id        ON reservations(user_id);
CREATE INDEX idx_reservations_session_id     ON reservations(session_id);
CREATE INDEX idx_reservations_status_expires ON reservations(status, expires_at);

-- ------------------------------------------------------------
-- E-7: SessionSeat (pré-populada na criação da sessão;
--                   SELECT FOR UPDATE garante anti-double-booking)
-- ------------------------------------------------------------
CREATE TABLE session_seats (
  id                     UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  session_id             UUID        NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,
  seat_id                UUID        NOT NULL REFERENCES seats(id)    ON DELETE RESTRICT,
  tenant_id              UUID        NOT NULL,
  status                 VARCHAR(20) NOT NULL DEFAULT 'AVAILABLE'
                         CHECK (status IN ('AVAILABLE','RESERVED','SOLD','BLOCKED')),
  reservation_id         UUID        REFERENCES reservations(id) ON DELETE SET NULL,
  reservation_expires_at TIMESTAMPTZ,
  updated_at             TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  UNIQUE (session_id, seat_id)
);
CREATE INDEX idx_session_seats_session_id     ON session_seats(session_id);
CREATE INDEX idx_session_seats_session_status ON session_seats(session_id, status);
CREATE INDEX idx_session_seats_tenant_id      ON session_seats(tenant_id);

-- ------------------------------------------------------------
-- E-9: Ticket
-- ------------------------------------------------------------
CREATE TABLE tickets (
  id               UUID         PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id        UUID         NOT NULL REFERENCES tenants(id) ON DELETE RESTRICT,
  session_id       UUID         NOT NULL REFERENCES sessions(id) ON DELETE RESTRICT,
  seat_id          UUID         NOT NULL REFERENCES seats(id)    ON DELETE RESTRICT,
  buyer_id         UUID         NOT NULL REFERENCES buyers(id)   ON DELETE RESTRICT,
  sold_by_user_id  UUID         NOT NULL REFERENCES users(id)    ON DELETE RESTRICT,
  status           VARCHAR(20)  NOT NULL DEFAULT 'SOLD'
                   CHECK (status IN ('SOLD','CANCELLED')),
  price            NUMERIC(10,2) NOT NULL,
  sold_at          TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
  created_at       TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
  UNIQUE (session_id, seat_id)   -- garante unicidade no DB além do SELECT FOR UPDATE
);
CREATE INDEX idx_tickets_tenant_id       ON tickets(tenant_id);
CREATE INDEX idx_tickets_session_id      ON tickets(session_id);
CREATE INDEX idx_tickets_buyer_id        ON tickets(buyer_id);
CREATE INDEX idx_tickets_status          ON tickets(status);
CREATE INDEX idx_tickets_sold_by_user_id ON tickets(sold_by_user_id);

-- ------------------------------------------------------------
-- E-10: CancellationAudit (imutável — sem UPDATE/DELETE via trigger)
-- ------------------------------------------------------------
CREATE TABLE cancellation_audits (
  id                   UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id            UUID        NOT NULL,
  ticket_id            UUID        NOT NULL REFERENCES tickets(id) ON DELETE RESTRICT,
  cancelled_by_user_id UUID        NOT NULL REFERENCES users(id)   ON DELETE RESTRICT,
  reason               TEXT        NOT NULL,
  cancelled_at         TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_cancellation_audits_tenant_id ON cancellation_audits(tenant_id);
CREATE INDEX idx_cancellation_audits_ticket_id ON cancellation_audits(ticket_id);
CREATE INDEX idx_cancellation_audits_user_id   ON cancellation_audits(cancelled_by_user_id);
```

---

## 5. Política de Retenção de Dados e Bases Legais LGPD

| Entidade | Prazo de Retenção (Dias) | Justificativa Operacional e Legal | Base Legal (LGPD — Lei nº 13.709/2018) |
|---|---|---|---|
| `Tenant` | Indeterminado | Registro do cinema cliente B2B; mantido enquanto o contrato estiver ativo e para histórico societário/contratual. | Não aplicável (pessoa jurídica). |
| `User` | Indeterminado | Conta de operador ou cliente vinculada ao tenant; retida enquanto ativa para rastreabilidade de ações RBAC e reservas. | Execução de contrato e legítimo interesse — Art. 7º, V e IX da LGPD. |
| `Film` | Indeterminado | Catálogo operacional do tenant; não contém dados pessoais (PII). | Não aplicável (sem PII). |
| `Room` | Indeterminado | Cadastro estrutural de salas físicas; referenciado por sessões históricas; sem PII. | Não aplicável (sem PII). |
| `Seat` | Indeterminado | Layout físico de poltronas; referenciado por ingressos históricos; sem PII. | Não aplicável (sem PII). |
| `Session` | 1.825 (5 anos) | Sessões cinematográficas compõem histórico operacional; retidas por 5 anos para auditoria e eventuais disputas contratuais. | Não aplicável (sem PII). |
| `SessionSeat` | 1.825 (5 anos) | Estado de poltronas por sessão; retido junto com `Session` para reconstrução de histórico de ocupação. | Não aplicável (sem PII). |
| `Buyer` | 1.825 (5 anos) | Dados de comprador (nome, e-mail, CPF cifrado) retidos por 5 anos por obrigação legal (CDC Art. 26/27) ou até solicitação de anonimização *in-place* (Art. 18 LGPD via `/api/titulares/anonimizar`). | Execução de contrato, obrigação legal e consentimento explícito registrado em `lgpd_consent_at` — Art. 7º, I, II e V da LGPD (`CA-06`). |
| `Reservation` | 1.825 (5 anos) | Registro de reservas online; dados pessoais do titular sujeitos à mesma política de anonimização *in-place* da tabela `Buyer`. | Execução de contrato preliminar de reserva e consentimento — Art. 7º, I e V da LGPD (`CA-09`, `CA-10`). |
| `Ticket` | 1.825 (5 anos) | Registro fiscal e operacional de venda; retido por 5 anos alinhado ao prazo prescricional do Código de Defesa do Consumidor (CDC). | Obrigação legal e execução de contrato — Art. 7º, II e V da LGPD. |
| `CancellationAudit` | 2.555 (7 anos) | Registro imutável de auditoria de cancelamentos (`CA-03`); retido por 7 anos seguindo prazo prescricional e práticas de compliance. | Cumprimento de obrigação legal/regulatória — Art. 7º, II da LGPD. |
