# Configuração do Vercel Log Drain com Axiom (ADR-011 / TASK-15)

## 1. Objetivo e Conformidade Legal
A legislação brasileira de proteção de dados (LGPD) e o Código de Defesa do Consumidor (CDC Art. 27) exigem a guarda e auditabilidade de registros operacionais, autenticação e cancelamentos por **no mínimo 365 dias (1 ano)**.
Como o plano padrão da Vercel retém logs por apenas 1 hora, a arquitetura do CineDoom utiliza a exportação contínua de logs via **Vercel Log Drain** conectado ao serviço gerenciado **Axiom** (ADR-011).

---

## 2. Configuração do Dataset no Axiom

1. **Nome do Dataset:** `cinedoom-production-logs`
2. **Ambiente:** `production` / `preview`
3. **Política de Retenção:**
   - **Retenção configurada:** `365 dias` (12 meses).
   - **Estratégia de Expurgamento:** FIFO automático após 365 dias.
4. **Endpoint de Ingestão OpenTelemetry:**
   - URL: `https://api.axiom.co/v1/datasets/cinedoom-production-logs/ingest`
   - Formato de payload: JSON estruturado delimitado por nova linha (NDJSON).

---

## 3. Configuração do Vercel Log Drain

Para integrar a Vercel ao Axiom:

```bash
# Instalação da integração oficial Axiom via Vercel Marketplace ou CLI
vercel integration add axiom

# Alternativamente, configuração manual de Log Drain via Vercel CLI:
vercel log-drains add \
  --name cinedoom-axiom-drain \
  --url https://api.axiom.co/v1/datasets/cinedoom-production-logs/ingest \
  --type json \
  --headers "Authorization=Bearer ${AXIOM_TOKEN}"
```

### Variáveis de Ambiente Necessárias no Vercel Project
- `AXIOM_TOKEN`: Token de autenticação seguro gerado no painel do Axiom com permissão `ingest`.
- `AXIOM_DATASET`: `cinedoom-production-logs`

---

## 4. Estrutura Padronizada dos Logs JSON da Aplicação

Todos os logs emitidos pelo serviço `cinedoom-api` seguem compulsoriamente a especificação de observabilidade (`specs/planning/devops-spec.md`):

```json
{
  "timestamp": "2026-10-23T20:30:00.000Z",
  "level": "INFO",
  "service": "cinedoom-api",
  "env": "production",
  "message": "Ingresso vendido com sucesso",
  "module": "bilheteria",
  "tenant_id": "11111111-1111-4111-a111-111111111111",
  "user_id": "00000000-0000-4000-a000-000000000002",
  "request_id": "550e8400-e29b-41d4-a716-446655440000",
  "route": "/api/vendas",
  "method": "POST",
  "status_code": 201,
  "duration_ms": 142,
  "action": "ticket_sold",
  "details": {
    "session_id": "sess-uuid",
    "seat_id": "seat-uuid",
    "ticket_id": "tick-uuid"
  }
}
```

### Regras de Sanitização de PII (LGPD R-CMP-7):
1. **NUNCA** logar CPF, e-mail ou nome de compradores em texto claro.
2. Em cancelamentos, o motivo é transformado em hash determinístico `motivo_hash = SHA256(motivo)`.
3. Tentativas de violação cross-tenant disparam eventos com `level: "ERROR"` e `action: "cross_tenant_query_attempt"`.
