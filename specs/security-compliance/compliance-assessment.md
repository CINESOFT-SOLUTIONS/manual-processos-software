---
kind: agent_artifact
feature_id: F-CINEDOOM-PLATAFORMA-B2B-SAAS-C
agent: Compliance
generated_by:
  run_id: run_2026-10-23T03-58-17_eedeb0ce
  session_id: 2026-09-03T15-33-01-hdb88xzyiu
  model: anthropic:claude-sonnet-4-6
generated_at: 2026-10-23T04:51:48.202Z
regenerative: true
title: "[Compliance] CineDoom — plataforma B2B SaaS para cinemas independentes e redes de pequeno/méd"
---

# Compliance — CineDoom — plataforma B2B SaaS para cinemas independentes e redes de pequeno/méd

> Artefato derivado de `.specs/features/F-CINEDOOM-PLATAFORMA-B2B-SAAS-C/spec.md` e gerado pelo agente **Compliance**
> via AI-4SDLC Platform. **Regenerative work product** (não-canonical SDD).
> Não edite manualmente — re-gere via `sdlc resume`.

## Resumo

Parecer de compliance para F-CINEDOOM-MVP: plataforma B2B SaaS de bilheteria para cinemas independentes no Brasil. Trata dados pessoais de compradores (nome, CPF, e-mail) coletados no ato da venda presencial por atendentes de cinemas tenants. Frameworks aplicáveis: LGPD-Base e SOC-2-Type-II. Dois blockers críticos identificados pelo Security Agent (CPF hash reversível e gestão de chave AES não especificada) devem ser resolvidos antes do go-live. Isolamento multi-tenant por row-level com tenant_id é arquitetura adequada, mas exige validação contínua por testes de isolamento cross-tenant. Retenção de logs via Axiom com 365 dias atende requisito de auditoria LGPD. Exclusão/anonimização de dados de compradores é executada exclusivamente pela equipe CineDoom via processo interno — ausência de self-service ao titular eleva risco regulatório e deve ser compensada por SLA documentado e canal de contato claro. DRAFT para revisão humana.

> ⚠️ **DRAFT para revisão humana — não substitui parecer jurídico**
>
> Este parecer é gerado por LLM como assistivo. NÃO substitui parecer jurídico.
> Antes de decisões regulatórias, encaminhe para advogado(a) ou DPO.

## Frameworks aplicáveis

- `LGPD-Base`
- `SOC-2-Type-II`

## Legal bases (LGPD)

| Purpose | Basis | LGPD | Rationale |
|---|---|---|---|
| Cadastro e identificação do comprador no ato da venda presencial de ingresso, coletando nome, CPF e e-mail para vinculação ao ingresso e assento reservado. | `contract` | Art. 7º, V LGPD | O tratamento dos dados do comprador (nome, CPF, e-mail) é necessário para a execução do contrato de compra do ingresso: identificar o titular do assento, prevenir fraude de double-booking e emitir comprovante da transação. Sem esses dados, o serviço contratado não pode ser prestado. |
| Registro de consentimento explícito do comprador para tratamento de dados pessoais no ato da venda, com timestamp e campo de aceite obrigatório conforme AC-6. | `consent` | Art. 7º, I LGPD | O PRD exige campo de consentimento LGPD registrado com timestamp antes da confirmação da venda (AC-6). O consentimento documentado reforça a base legal contratual e garante evidência auditável de que o titular foi informado sobre o tratamento de seus dados pessoais. |
| Manutenção de registro imutável de cancelamentos de ingressos (auditoria_cancelamentos) com id do ingresso, id do usuário executante, timestamp UTC, tenant_id e motivo, para fins de rastreabilidade fiscal e operacional. | `legal_obligation` | Art. 7º, II LGPD | A auditoria de cancelamentos constitui obrigação de rastreabilidade operacional e pode ser exigida por fiscalização tributária ou trabalhista. O registro imutável é mandatório pelo AC-3 do PRD. O tratamento de dados mínimos de identificação do cancelamento é amparado por obrigação legal. |
| Tratamento de dados de autenticação e logs de acesso de usuários internos (Atendentes e Gerentes dos cinemas tenants) para controle de acesso RBAC, rastreabilidade de ações e segurança da plataforma. | `legitimate_interests` | Art. 7º, IX LGPD | O tratamento de e-mail, nome e role dos usuários internos dos tenants é necessário para autenticação via NextAuth.js, controle de perfis ATENDENTE/GERENTE e rastreabilidade de ações auditáveis. O legítimo interesse da CineDoom e dos cinemas clientes em segurança e integridade operacional prevalece sobre o impacto mínimo nos dados dos funcionários. |
| Execução do contrato B2B entre a CineDoom e os cinemas tenants, incluindo provisionamento de tenant, gestão de contas de usuário e prestação do serviço SaaS de bilheteria. | `contract` | Art. 7º, V LGPD | O tratamento de dados dos representantes dos cinemas clientes (nome, e-mail corporativo, tenant_id) é necessário para a execução do contrato de prestação do serviço SaaS. O provisionamento manual pela equipe CineDoom e a gestão de tenants ativos são atividades diretamente vinculadas à relação contratual B2B. |
| Retenção de logs de aplicação por 365 dias no Axiom para fins de auditoria de segurança, investigação de incidentes e conformidade LGPD/SOC-2-Type-II. | `legitimate_interests` | Art. 7º, IX LGPD | A retenção de logs por 365 dias (decisão do stakeholder: Axiom como log drain) é necessária para auditorias de segurança, investigação de incidentes e evidências SOC-2-Type-II. O tratamento de metadados de log (sem PII de comprador exposta em texto claro) é proporcional ao interesse legítimo de segurança e conformidade regulatória. |

## Data subject rights

| Right | How supported | SLA |
|---|---|---|
| `access` | Titulares (compradores) solicitam acesso via canal de suporte CineDoom (e-mail/formulário publicado na política de privacidade). A equipe CineDoom consulta a tabela Buyer filtrando por email ou cpf_hash e retorna relatório com os dados armazenados (nome, e-mail, ingressos vinculados). Não há endpoint self-service no MVP — processo é manual e documentado em runbook interno. | ≤ 15 dias úteis |
| `rectification` | Titular solicita correção via canal de suporte CineDoom. A equipe CineDoom executa UPDATE na tabela Buyer (campos name, email) e re-cifra CPF se aplicável, registrando a alteração em log de auditoria com timestamp e operador responsável. Processo documentado em runbook interno com trilha de auditoria. | ≤ 15 dias úteis |
| `erasure` | Titular solicita exclusão/anonimização via canal de suporte CineDoom. Conforme decisão do stakeholder, somente a equipe CineDoom executa o processo: anonimização dos campos name, email e cpf_hash/cpf_encrypted na tabela Buyer, preservando registros de ingressos com referência anonimizada para integridade de auditoria fiscal. Processo documentado em runbook com aprovação de DPO. | ≤ 15 dias úteis |
| `portability` | Titular solicita portabilidade via canal de suporte CineDoom. A equipe executa exportação dos dados do comprador em formato JSON ou CSV estruturado (nome, e-mail, histórico de ingressos do tenant solicitado), entregue por canal seguro (link expirado ou e-mail cifrado). Escopo limitado ao tenant do cinema onde a compra foi realizada. | ≤ 15 dias úteis |
| `objection` | Titular pode se opor ao tratamento de seus dados para finalidades de legítimo interesse (logs, analytics) via canal de suporte CineDoom. A equipe avalia a oposição, documenta a decisão e, se procedente, executa anonimização ou supressão do tratamento contestado. Dados tratados sob base contratual (venda de ingresso) não são objeto de oposição válida enquanto o ingresso estiver ativo. | ≤ 15 dias úteis |
| `automated_decision` | O MVP CineDoom não realiza decisões automatizadas com efeitos jurídicos ou significativos sobre os titulares compradores. A trava ACID de assentos (SELECT FOR UPDATE) é decisão técnica de integridade transacional, não decisão sobre o titular. Direito não aplicável no escopo atual — monitorar se futuras features de recomendação ou precificação dinâmica ativarem este direito. | N/A — não aplicável no MVP |

## DPIA summary

A plataforma CineDoom MVP trata dados pessoais de compradores de ingressos (nome, CPF cifrado com AES-256-GCM + hash HMAC-SHA256 para busca, e-mail) coletados por atendentes de cinemas clientes (tenants B2B) no ato da venda presencial. O risco é classificado como MÉDIO-ALTO: os dados incluem CPF, que é dado pessoal sensível para fins de identificação civil no Brasil, e o espaço finito de CPFs válidos (~900M) torna hashes sem HMAC/salt reversíveis por rainbow table (blocker T-1 do Security Agent). A chave AES-256-GCM para cifragem do CPF não tem estratégia de gerenciamento especificada no MVP, representando blocker T-2 — vazamento simultâneo de dump de DB e .env exporia 100% da PII de compradores. Mitigações técnicas requeridas antes do go-live: (a) substituir SHA-256 por HMAC-SHA256 com chave server-side para hash de CPF; (b) armazenar chave AES exclusivamente em Vercel Env Secrets ou AWS KMS, nunca em .env comitado; (c) pre-commit hooks com detect-secrets/gitleaks. O isolamento multi-tenant por row-level com tenant_id em shared schema PostgreSQL Neon Serverless é adequado para o contexto B2B, desde que a suíte de 500 cenários de isolamento cross-tenant (NFR Security) seja executada continuamente no CI. A retenção de logs por 365 dias no Axiom atende o requisito de auditoria LGPD, mas logs devem ser configurados para excluir CPF e e-mail em texto claro. A ausência de self-service para direitos LGPD (acesso, retificação, exclusão exclusivamente via equipe CineDoom) é compensada por SLA documentado de 15 dias úteis e canal de contato publicado na política de privacidade.

## Incident response plan

DETECÇÃO: Alertas automáticos configurados no Axiom para anomalias de acesso cross-tenant (queries sem filtro tenant_id), volume anormal de exports de PII, falhas de autenticação em série e tentativas de acesso a rotas 403. SIEM/alerting deve cobrir T-1 (acesso a cpf_hash em volume), T-2 (acesso à chave AES) e T-3 (secret leak via logs de build Vercel). SLA de detecção: alerta em até 15 minutos para eventos críticos de segurança. CLASSIFICAÇÃO: Incidentes são triados em três níveis — Crítico (vazamento confirmado de PII de compradores, acesso cross-tenant verificado, comprometimento de chave AES), Alto (tentativa de acesso não autorizado, anomalia em auditoria_cancelamentos, secret detectado em log) e Médio (falha de isolamento sem acesso confirmado, degradação de disponibilidade). ESCALATION: Crítico → DPO + CTO + equipe de segurança em até 1h; Alto → DPO + engenharia em até 4h; Médio → engenharia em até 24h. Comunicação interna via canal dedicado (#incident-response) com thread de timeline. COMUNICAÇÃO A TITULARES E ANPD: Confirmado incidente com acesso indevido a dados de compradores — notificação à ANPD em até 72h conforme Art. 48 LGPD, com formulário de comunicação de incidente contendo: natureza dos dados afetados (nome, CPF, e-mail), número estimado de titulares impactados por tenant, data/hora da detecção, medidas imediatas adotadas e contato do DPO. Titulares afetados notificados individualmente por e-mail em até 5 dias úteis quando o risco for classificado como alto ou crítico. Cinemas tenants afetados notificados imediatamente após confirmação do escopo do incidente. POST-MORTEM: Conduzido em até 7 dias após contenção do incidente. Documento obrigatório: timeline completa, root cause analysis, controles falhos, ações corretivas com owner e prazo, atualização do risk register e comunicação aos tenants afetados. Lições aprendidas incorporadas no runbook de resposta a incidentes e revisadas no ciclo de auditoria SOC-2-Type-II.

## Risk register

| ID | Category | Likelihood | Impact | Mitigation | Residual |
|---|---|---|---|---|---|
| R-CMP-1 | `privacy` | high | high | Substituir SHA-256 por HMAC-SHA256 com chave server-side para hash de CPF, inviabilizando rainbow table sobre espaço finito de CPFs brasileiros | low |
| R-CMP-2 | `security` | high | high | Armazenar chave AES-256-GCM exclusivamente em Vercel Env Secrets ou AWS KMS com rotação anual e re-cifragem; nunca em .env comitado | medium |
| R-CMP-3 | `security` | high | high | Implementar pre-commit hooks com detect-secrets/gitleaks, .env* no .gitignore verificado por CI e secrets exclusivamente via Vercel Env Vars interface com rotação trimestral | low |
| R-CMP-4 | `regulatory` | medium | high | Ausência de self-service para direitos LGPD (acesso, retificação, exclusão via equipe CineDoom apenas): publicar canal de contato na política de privacidade com SLA 15 dias úteis e runbook interno documentado | medium |
| R-CMP-5 | `privacy` | medium | high | Vazamento cross-tenant por falha no middleware Prisma de injeção de tenant_id: suíte de 500 cenários de isolamento executada no CI com zero tolerância a falhas | low |
| R-CMP-6 | `regulatory` | low | high | Não conformidade com prazo de 72h ANPD (Art. 48 LGPD) por ausência de plano de resposta formalizado: documentar IRP com template de notificação ANPD e DPO designado antes do go-live | low |
| R-CMP-7 | `privacy` | medium | medium | Logs de aplicação no Axiom podem conter PII de compradores em texto claro se endpoints de venda logarem payloads completos: configurar mascaramento de CPF e e-mail no logger antes de envio ao Axiom | low |
| R-CMP-8 | `security` | medium | medium | Provisionamento manual de tenants pela equipe CineDoom sem processo de offboarding documentado pode deixar dados de tenants inativos acessíveis: implementar processo formal de desativação com anonimização de dados após encerramento de contrato | medium |
