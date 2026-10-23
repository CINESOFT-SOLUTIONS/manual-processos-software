---
kind: agent_artifact
feature_id: F-CINEDOOM-PLATAFORMA-B2B-SAAS-C
agent: Data Architect
generated_by:
  run_id: run_2026-10-23T03-58-17_eedeb0ce
  session_id: 2026-09-03T15-33-01-hdb88xzyiu
  model: anthropic:claude-sonnet-4-6
generated_at: 2026-10-23T04:44:56.868Z
regenerative: true
title: "[Data Architect] CineDoom — plataforma B2B SaaS para cinemas independentes e redes de pequeno/méd"
---

# Data Architect — CineDoom — plataforma B2B SaaS para cinemas independentes e redes de pequeno/méd

> Artefato derivado de `.specs/features/F-CINEDOOM-PLATAFORMA-B2B-SAAS-C/spec.md` e gerado pelo agente **Data Architect**
> via AI-4SDLC Platform. **Regenerative work product** (não-canonical SDD).
> Não edite manualmente — re-gere via `sdlc resume`.

## Resumo

Modelo de dados para plataforma B2B SaaS CineDoom: 11 entidades cobrindo multi-tenancy (Tenant), autenticação RBAC com perfil cliente (User), catálogo cinematográfico (Film), salas e assentos (Room/Seat), sessões com mapa de status (Session/SessionSeat para SELECT FOR UPDATE anti-double-booking e reserva temporária), reservas web com expiração Just-in-Time (Reservation), venda de ingressos (Ticket), compradores com PII/LGPD cifrada (Buyer) e auditoria imutável de cancelamentos (CancellationAudit) (Tenant), autenticação RBAC (User), catálogo cinematográfico (Film), salas e assentos (Room/Seat), sessões com mapa de status (Session/SessionSeat para SELECT FOR UPDATE anti-double-booking), venda de ingressos (Ticket), compradores com PII/LGPD cifrada (Buyer) e auditoria imutável de cancelamentos (CancellationAudit). Isolamento por tenant_id em shared schema PostgreSQL Neon Serverless.

## Entities

### E-1. Tenant

- **Primary key flavor:** `UUID-PK`

| Field | Type | Nullable | Indexed | PII |
|---|---|---|---|---|
| `id` | `uuid` |  |  |  |
| `name` | `string` |  |  |  |
| `slug` | `string` |  | ✓ |  |
| `active` | `boolean` |  |  |  |
| `created_at` | `timestamp` |  |  |  |

### E-2. User

- **Primary key flavor:** `UUID-PK`

| Field | Type | Nullable | Indexed | PII |
|---|---|---|---|---|
| `id` | `uuid` |  |  |  |
| `tenant_id` | `uuid` |  | ✓ |  |
| `email` | `string` |  | ✓ | ⚠ |
| `name` | `string` |  |  | ⚠ |
| `password_hash` | `string` |  |  |  |
| `role` | `string` |  | ✓ |  |
| `active` | `boolean` |  |  |  |
| `created_at` | `timestamp` |  |  |  |

### E-3. Film

- **Primary key flavor:** `UUID-PK`

| Field | Type | Nullable | Indexed | PII |
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

### E-4. Room

- **Primary key flavor:** `UUID-PK`

| Field | Type | Nullable | Indexed | PII |
|---|---|---|---|---|
| `id` | `uuid` |  |  |  |
| `tenant_id` | `uuid` |  | ✓ |  |
| `name` | `string` |  |  |  |
| `capacity` | `int` |  |  |  |
| `layout_metadata` | `jsonb` | ✓ |  |  |
| `created_at` | `timestamp` |  |  |  |
| `updated_at` | `timestamp` |  |  |  |

### E-5. Seat

- **Primary key flavor:** `UUID-PK`

| Field | Type | Nullable | Indexed | PII |
|---|---|---|---|---|
| `id` | `uuid` |  |  |  |
| `room_id` | `uuid` |  | ✓ |  |
| `tenant_id` | `uuid` |  | ✓ |  |
| `row_label` | `string` |  |  |  |
| `column_number` | `int` |  |  |  |
| `seat_code` | `string` |  |  |  |
| `status` | `string` |  |  |  |
| `created_at` | `timestamp` |  |  |  |

### E-6. Session

- **Primary key flavor:** `UUID-PK`

| Field | Type | Nullable | Indexed | PII |
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

### E-7. SessionSeat

- **Primary key flavor:** `UUID-PK`

| Field | Type | Nullable | Indexed | PII |
|---|---|---|---|---|
| `id` | `uuid` |  |  |  |
| `session_id` | `uuid` |  | ✓ |  |
| `seat_id` | `uuid` |  | ✓ |  |
| `tenant_id` | `uuid` |  | ✓ |  |
| `status` | `string` |  | ✓ |  |
| `updated_at` | `timestamp` |  |  |  |

### E-8. Buyer

- **Primary key flavor:** `UUID-PK`

| Field | Type | Nullable | Indexed | PII |
|---|---|---|---|---|
| `id` | `uuid` |  |  |  |
| `tenant_id` | `uuid` |  | ✓ |  |
| `name` | `string` |  |  | ⚠ |
| `email` | `string` |  | ✓ | ⚠ |
| `cpf_hash` | `string` |  | ✓ |  |
| `cpf_encrypted` | `text` |  |  | ⚠ |
| `lgpd_consent_at` | `timestamp` |  |  |  |
| `created_at` | `timestamp` |  |  |  |

### E-9. Ticket

- **Primary key flavor:** `UUID-PK`

| Field | Type | Nullable | Indexed | PII |
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

### E-10. CancellationAudit

- **Primary key flavor:** `UUID-PK`

| Field | Type | Nullable | Indexed | PII |
|---|---|---|---|---|
| `id` | `uuid` |  |  |  |
| `tenant_id` | `uuid` |  | ✓ |  |
| `ticket_id` | `uuid` |  | ✓ |  |
| `cancelled_by_user_id` | `uuid` |  | ✓ |  |
| `reason` | `text` |  |  |  |
| `cancelled_at` | `timestamp` |  |  |  |


### E-11. Reservation

- **Primary key flavor:** `UUID-PK`

| Field | Type | Nullable | Indexed | PII |
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

## Relationships

| ID | From | Kind | To | FK | onDelete |
|---|---|---|---|---|---|
| R-1 | Tenant | `oneToMany` | User | tenant_id | CASCADE |
| R-2 | Tenant | `oneToMany` | Film | tenant_id | CASCADE |
| R-3 | Tenant | `oneToMany` | Room | tenant_id | CASCADE |
| R-4 | Tenant | `oneToMany` | Session | tenant_id | CASCADE |
| R-5 | Room | `oneToMany` | Seat | room_id | CASCADE |
| R-6 | Film | `oneToMany` | Session | film_id | RESTRICT |
| R-7 | Room | `oneToMany` | Session | room_id | RESTRICT |
| R-8 | Session | `oneToMany` | SessionSeat | session_id | CASCADE |
| R-9 | Seat | `oneToMany` | SessionSeat | seat_id | RESTRICT |
| R-10 | Session | `oneToMany` | Ticket | session_id | RESTRICT |
| R-11 | Buyer | `oneToMany` | Ticket | buyer_id | RESTRICT |
| R-12 | User | `oneToMany` | Ticket | sold_by_user_id | RESTRICT |
| R-13 | Ticket | `oneToOne` | CancellationAudit | ticket_id | RESTRICT |
| R-14 | User | `oneToMany` | CancellationAudit | cancelled_by_user_id | RESTRICT |
| R-15 | Tenant | `oneToMany` | Reservation | tenant_id | RESTRICT |
| R-16 | Session | `oneToMany` | Reservation | session_id | RESTRICT |
| R-17 | User | `oneToMany` | Reservation | user_id | RESTRICT |
| R-18 | Buyer | `oneToMany` | Reservation | buyer_id | RESTRICT |
| R-19 | Reservation | `oneToMany` | SessionSeat | reservation_id | SET NULL |

## Indexes

| Entity | Fields | Kind | Unique |
|---|---|---|---|
| User | tenant_id, email | `btree` | ✓ |
| SessionSeat | session_id, status | `btree` |  |
| Buyer | tenant_id, cpf_hash | `btree` |  |
| Session | tenant_id, starts_at | `btree` |  |
| Ticket | session_id, seat_id | `btree` | ✓ |
| CancellationAudit | cancelled_at | `brin` |  |

## DDL (Postgres)

```sql
-- ============================================================
-- CineDoom SaaS — DDL PostgreSQL (Neon Serverless)
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
-- E-2: User (Atendente / Gerente)
-- ------------------------------------------------------------
CREATE TABLE users (
  id            UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id     UUID        NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
  email         VARCHAR(255) NOT NULL,
  name          VARCHAR(255) NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  role          VARCHAR(20)  NOT NULL CHECK (role IN ('ATENDENTE','GERENTE')),
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
CREATE INDEX idx_reservations_tenant_id        ON reservations(tenant_id);
CREATE INDEX idx_reservations_code             ON reservations(code);
CREATE INDEX idx_reservations_user_id          ON reservations(user_id);
CREATE INDEX idx_reservations_session_id       ON reservations(session_id);
CREATE INDEX idx_reservations_status_expires   ON reservations(status, expires_at);

-- ------------------------------------------------------------
-- E-7: SessionSeat  (pré-populada na criação da sessão;
--                    SELECT FOR UPDATE aqui garante anti-double-booking)
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
CREATE INDEX idx_session_seats_session_id        ON session_seats(session_id);
CREATE INDEX idx_session_seats_session_status    ON session_seats(session_id, status);
CREATE INDEX idx_session_seats_tenant_id         ON session_seats(tenant_id);

-- ------------------------------------------------------------
-- E-8: Buyer  (PII: nome, e-mail, CPF cifrado AES-256-GCM)
-- ------------------------------------------------------------
CREATE TABLE buyers (
  id               UUID         PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id        UUID         NOT NULL REFERENCES tenants(id) ON DELETE RESTRICT,
  name             VARCHAR(255) NOT NULL,          -- PII
  email            VARCHAR(255) NOT NULL,          -- PII
  cpf_hash         CHAR(64)     NOT NULL,          -- SHA-256 hex para lookup
  cpf_encrypted    TEXT         NOT NULL,          -- AES-256-GCM (PII)
  lgpd_consent_at  TIMESTAMPTZ  NOT NULL,
  created_at       TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_buyers_tenant_id ON buyers(tenant_id);
CREATE INDEX idx_buyers_cpf_hash  ON buyers(cpf_hash);
CREATE INDEX idx_buyers_tenant_cpf ON buyers(tenant_id, cpf_hash);

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
-- E-10: CancellationAudit  (imutável — sem UPDATE/DELETE)
-- ------------------------------------------------------------
CREATE TABLE cancellation_audits (
  id                   UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id            UUID        NOT NULL,
  ticket_id            UUID        NOT NULL REFERENCES tickets(id) ON DELETE RESTRICT,
  cancelled_by_user_id UUID        NOT NULL REFERENCES users(id)   ON DELETE RESTRICT,
  reason               TEXT        NOT NULL,
  cancelled_at         TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_cancellation_audits_tenant_id  ON cancellation_audits(tenant_id);
CREATE INDEX idx_cancellation_audits_ticket_id  ON cancellation_audits(ticket_id);
CREATE INDEX idx_cancellation_audits_user_id    ON cancellation_audits(cancelled_by_user_id);
```

## Retention policy

| Entity | Days | Rationale | LGPD basis |
|---|---|---|---|
| Tenant | indefinite | Registro do cliente B2B; mantido enquanto contrato ativo e por prazo indeterminado para histórico contratual CineDoom. | (n/a) |
| User | indefinite | Conta de usuário vinculada ao tenant; retida enquanto tenant ativo para rastreabilidade de ações RBAC. | Execução de contrato entre CineDoom e cinema tenant — Art. 7º, V LGPD. |
| Film | indefinite | Catálogo operacional do tenant; sem PII; retido enquanto tenant ativo. | (n/a) |
| Room | indefinite | Cadastro estrutural de salas; referenciado por sessões históricas; sem PII. | (n/a) |
| Seat | indefinite | Layout físico de assentos; referenciado por tickets históricos; sem PII. | (n/a) |
| Session | 1825 | Sessões cinematográficas compõem histórico operacional; retidas 5 anos para auditoria e disputas contratuais. | (n/a) |
| SessionSeat | 1825 | Status de assentos por sessão; retido junto com Session para reconstrução de estado histórico. | (n/a) |
| Buyer | 1825 | Dados de comprador (nome, e-mail, CPF) retidos 5 anos por obrigação legal (CDC Art. 26/27) e contratual. Exclusão/anonimização executada exclusivamente pela equipe CineDoom via processo interno sob solicitação LGPD Art. 18. | Obrigação legal (CDC) e execução de contrato de compra de ingresso — Art. 7º, II e V LGPD. Consentimento explícito coletado no campo lgpd_consent_at. |
| Ticket | 1825 | Registro de venda; base para disputas, estornos e auditoria fiscal; retido 5 anos alinhado ao prazo prescricional do CDC. | (n/a) |
| CancellationAudit | 2555 | Registro imutável de auditoria de cancelamentos; retido 7 anos seguindo prazo prescricional de ações civis (CC Art. 205) e melhores práticas de compliance. | (n/a) |
