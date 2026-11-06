---
document_id: SPEC-CINEDOOM-COMPLIANCE-LGPD-001
version: "2.0.0"
date: "2026-11-05"
status: "Aprovado e Consolidado"
standard: "Lei Geral de Proteção de Dados Pessoais (Lei nº 13.709/2018 — LGPD) & SOC 2 Type II"
title: "Avaliação de Conformidade e Relatório de Impacto à Proteção de Dados Pessoais (DPIA/RIPD) — CineDoom"
---

# Avaliação de Conformidade e Relatório de Impacto à Proteção de Dados Pessoais (DPIA/RIPD) — CineDoom

> **Documento Técnico de Governança e Privacidade — CineSoft Solutions (UFG/INF — Processos de Software 2026/1)**
> Rastreabilidade direta com [`cinedoom-spec.md`](../cinedoom-spec.md) (`RF-08`, `RF-09`, `RF-11`, `RF-14`, `RNF-03`, `RN-06`, `RN-07`, `CA-03`, `CA-04`, `CA-06`, `CA-10`) e [`ADR-008`](../adr/ADR-008-protecao-cpf-hmac-sha256-aes256gcm.md) / [`ADR-009`](../adr/ADR-009-governanca-lgpd-anonimizacao-dpia-dpo.md).

## 1. Resumo Executivo

Este documento consolida a Avaliação de Conformidade Regulatória e o Relatório de Impacto à Proteção de Dados Pessoais (**DPIA / RIPD**, conforme Art. 38 da Lei nº 13.709/2018 — LGPD) para a plataforma B2B SaaS **CineDoom**.

A plataforma realiza o tratamento de dados pessoais de espectadores compradores (nome completo, CPF e endereço de e-mail) coletados tanto na bilheteria presencial quanto no Portal do Cliente. Todos os controles técnicos e organizacionais exigidos pela LGPD e pelo framework **SOC 2 Type II** foram implementados e verificados:
1. **Proteção Criptográfica de CPF (`ADR-008`, `RF-09`, `CA-06`):** O CPF nunca é armazenado em texto plano; utiliza-se **`HMAC-SHA256`** com chave secreta de servidor para indexação de busca (`cpf_hash`) e **`AES-256-GCM`** com IV aleatório de 96 bits e tag de autenticação de 128 bits para armazenamento cifrado (`cpf_encrypted`).
2. **Anonimização *In-Place* para Direitos do Titular (`ADR-009`, Art. 18 LGPD):** Implementada na rota administrativa `POST /api/titulares/anonimizar`, que sobrescreve os dados pessoais do titular mantendo a integridade referencial contábil dos ingressos emitidos.
3. **Isolamento Multi-tenant Estrito (`ADR-003`, `CA-04`):** Validado continuamente no pipeline de CI por meio de uma bateria automatizada de **500 cenários de segurança cross-tenant** (`CT-04`, `CT-18`).
4. **Retenção de Logs e Auditoria Imutável (`ADR-006`, `ADR-010`, `CA-03`):** Tabela de cancelamentos protegida por trigger PostgreSQL *append-only* e drenagem de logs para o **Axiom** com retenção de **365 dias** e mascaramento estrito de PII.

---

## 2. Frameworks Regulatórios e Normativos Aplicáveis

- **LGPD (Lei nº 13.709/2018):** Lei Geral de Proteção de Dados Pessoais (Brasil) — Artigos 6º, 7º, 18, 37, 38, 41, 46 e 48.
- **Marco Civil da Internet (Lei nº 12.965/2014) e CDC (Lei nº 8.078/1990):** Guarda de registros de transação e prazos prescricionais de relações de consumo.
- **SOC 2 Type II (AICPA Trust Services Criteria):** Critérios de Segurança (*Security*), Disponibilidade (*Availability*), Integridade de Processamento (*Processing Integrity*) e Confidencialidade (*Confidentiality*).
- **ABNT NBR ISO/IEC/IEEE 12207:2021:** Processos de Garantia da Qualidade (Cláusula 7.2.3) e Validação (Cláusula 6.4.11).

---

## 3. Bases Legais para o Tratamento de Dados (LGPD Art. 7º)

| Finalidade do Tratamento | Base Legal (Código) | Dispositivo LGPD | Justificativa e Rastreabilidade |
|---|---|---|---|
| Identificação do comprador no ato da venda presencial de ingresso (nome, CPF e e-mail) para vinculação ao assento e emissão de comprovante. | Execução de Contrato (`contract`) | Art. 7º, V da LGPD | O tratamento dos dados do comprador é indispensável para a execução do contrato de compra e venda do ingresso, prevenção a fraudes e identificação do titular na entrada da sala (`RF-06`, `RF-09`). |
| Registro de consentimento explícito do comprador para tratamento de dados pessoais no ato da venda ou reserva, com carimbo de tempo UTC (`lgpd_consent_at`). | Consentimento do Titular (`consent`) | Art. 7º, I da LGPD | Exigido por `RN-07` e `CA-06` (`AC-6`). O registro do timestamp UTC fornece evidência auditável de que o titular foi informado de forma clara sobre a finalidade da coleta antes da confirmação da transação. |
| Manutenção de registro imutável de cancelamentos de ingressos (`cancellation_audits`) contendo ID do ingresso, ID do operador, timestamp UTC, `tenant_id` e motivo. | Obrigação Legal ou Regulatória (`legal_obligation`) | Art. 7º, II da LGPD | A trilha de auditoria imutável (`RF-08`, `RN-06`, `CA-03`) é exigida para conformidade fiscal, contábil e prevenção a estornos fraudulentos em caixas presenciais. |
| Cadastro, autenticação e gestão de reservas no Portal do Cliente com emissão de voucher e e-mail transacional contendo código alfanumérico. | Execução de Contrato / Consentimento (`contract` / `consent`) | Art. 7º, I e V da LGPD | Necessário para a execução do procedimento preliminar de reserva de poltrona (`RF-13`, `RF-14`, `RF-15`, `CA-09`, `CA-10`, `CA-11`) solicitado pelo próprio espectador. |
| Controle de acesso baseado em papéis (RBAC) e rastreabilidade operacional de usuários internos dos cinemas (`ATENDENTE` e `GERENTE`). | Legítimo Interesse (`legitimate_interests`) | Art. 7º, IX da LGPD | O tratamento de nome, e-mail corporativo e perfil de acesso dos colaboradores do cinema tenant (`RF-01`, `CA-05`) é estritamente necessário para a segurança da informação e controle de acesso à plataforma. |
| Execução do contrato B2B SaaS entre a CineSoft Solutions e os cinemas locatários (provisionamento de tenant e suporte operacional). | Execução de Contrato (`contract`) | Art. 7º, V da LGPD | Necessário para a prestação do serviço de software sob demanda contratado pela pessoa jurídica exibidora (`RES-03`). |
| Retenção de logs estruturados de aplicação por 365 dias no Axiom para investigação de incidentes, segurança e conformidade. | Legítimo Interesse / Obrigação Legal (`legitimate_interests`) | Art. 7º, II e IX da LGPD | Garante rastreabilidade forense e evidências de auditoria (`RF-11`, `RNF-03`), sem exposição de CPF ou e-mail em texto claro nos registros de log. |

---

## 4. Atendimento aos Direitos dos Titulares (LGPD Art. 18)

| Direito do Titular (Art. 18) | Mecanismo Técnico e Operacional de Atendimento | Prazo / SLA |
|---|---|---|
| **Confirmação e Acesso aos Dados** (Incisos I e II) | O titular solicita o relatório pelo canal oficial do Encarregado (DPO) publicado na política de privacidade. A operação localiza o registro na tabela `Buyer` pelo índice determinístico `cpf_hash` (`HMAC-SHA256`) restrito ao `tenant_id` correspondente e exporta os dados vinculados. | $\le$ 15 dias corridos (conforme Art. 19, § 2º da LGPD) |
| **Correção de Dados Incompletos ou Inexatos** (Inciso III) | Mediante solicitação validada do titular, o operador autorizado atualiza os campos cadastrais (`name`, `email`) e, se necessário, regenera o par `cpf_hash` / `cpf_encrypted` via `CryptoService`, registrando a operação em log de auditoria. | $\le$ 15 dias corridos |
| **Anonimização, Bloqueio ou Eliminação** (Incisos IV e VI) | Executado de forma atômica pelo endpoint administrativo **`POST /api/titulares/anonimizar`** (`ADR-009`), que aplica *soft-anonymization in-place* na tabela `Buyer` (`name = 'TITULAR ANONIMIZADO'`, `email = 'anonimizado+<uuid>@lgpd.cinedoom.local'`, expurgo do CPF cifrado), preservando o UUID primário para não corromper o histórico fiscal de `Ticket` e `CancellationAudit`. | $\le$ 15 dias corridos (execução técnica imediata em < 1s) |
| **Portabilidade dos Dados** (Inciso V) | Exportação estruturada em formato JSON/CSV contendo os dados cadastrais do titular e o histórico de ingressos e reservas adquiridos no respectivo cinema tenant, entregue por canal seguro. | $\le$ 15 dias corridos |
| **Informação sobre Compartilhamento e Revogação de Consentimento** (Incisos VII, VIII e IX) | O titular pode revogar o consentimento ou opor-se a tratamentos não essenciais a qualquer momento, acionando o fluxo de anonimização *in-place* assim que encerradas as obrigações legais/fiscais de guarda do bilhete ativo. | $\le$ 15 dias corridos |
| **Revisão de Decisões Automatizadas** (Art. 20) | O sistema CineDoom não realiza perfilamento (*profiling*), pontuação de crédito ou precificação dinâmica automatizada baseada em características pessoais. A trava `SELECT FOR UPDATE` e a expiração *Just-in-Time* de 60 minutos são regras determinísticas de integridade de estoque físico. | Não aplicável (ausência de decisão automatizada de perfil) |

---

## 5. Resumo do Relatório de Impacto à Proteção de Dados Pessoais (DPIA / RIPD — Art. 38)

1. **Descrição do Tratamento e Ciclo de Vida:** Os dados pessoais dos espectadores (`name`, `email`, `cpf`) são coletados no momento da compra presencial (`RF-06`) ou reserva online (`RF-13`, `RF-14`). Antes de qualquer comando de escrita no banco de dados PostgreSQL, o módulo `CryptoService` normaliza o CPF, gera o resumo criptográfico `cpf_hash` via **`HMAC-SHA256`** (para pesquisas exatas sem revelação) e cifra o documento com **`AES-256-GCM`** (`cpf_encrypted`), descartando o valor em texto plano da memória.
2. **Avaliação de Necessidade e Proporcionalidade (Princípio da Minimização — Art. 6º, III):** São coletados apenas os três atributos estritamente necessários para identificar o portador do ingresso na portaria ou balcão, enviar o voucher eletrônico (`RF-15`) e cumprir obrigações fiscais/consumeristas. Dados financeiros de cartões de crédito não são coletados na plataforma (`RES-04`).
3. **Análise e Mitigação de Riscos aos Titulares:** O risco potencial de exposição de CPF foi reduzido de *Alto* para *Baixo (Residual)* por meio da combinação de: (a) `HMAC-SHA256` contra tabelas arco-íris (`ADR-008`); (b) cifragem autenticada `AES-256-GCM` com chaves gerenciadas em cofre seguro (*Vercel Secrets*); (c) isolamento multi-tenant via *Prisma Client Extension* validado por 500 testes automatizados (`CA-04`); e (d) mascaramento automático de PII nos logs enviados ao Axiom (`RF-11`).
4. **Governança e Encarregado pelo Tratamento de Dados (DPO — Art. 41):** Na relação B2B SaaS, o cinema exibidor atua como **Controlador** (*Controller*) dos dados de seus espectadores e a CineSoft Solutions atua como **Operadora Tecnológica** (*Processor*), conforme Acordo de Processamento de Dados (DPA) padronizado no [`ADR-009`](../adr/ADR-009-governanca-lgpd-anonimizacao-dpia-dpo.md).

---

## 6. Plano de Resposta a Incidentes de Segurança e Privacidade (Art. 48 LGPD)

1. **Detecção e Alerta (SLA $\le$ 15 minutos):** Alertas automatizados configurados no Axiom Log Drain monitoram tentativas de violação de isolamento cross-tenant (`cross_tenant_query_attempt`), picos anômalos de consultas à tabela `Buyer` e falhas repetidas de autenticação (`401/403`).
2. **Classificação de Severidade:**
   - **Nível Crítico (P0):** Suspeita ou confirmação de acesso não autorizado a dados pessoais decifrados, comprometimento de chaves criptográficas ou vazamento entre tenants.
   - **Nível Alto (P1):** Tentativa bloqueada de intrusão, anomalia na tabela `cancellation_audits` ou indisponibilidade do serviço de criptografia.
   - **Nível Médio (P2):** Degradação de performance ou falha pontual de entrega de e-mail transacional.
3. **Contenção e Escalonamento:** Incidentes Críticos (P0) acionam imediatamente o Encarregado de Dados (DPO), o Líder Técnico (TechLead) e o Engenheiro de Segurança em até **1 hora**, executando rotação imediata de `NEXTAUTH_SECRET`, `CPF_ENCRYPTION_KEY` e `CINEDOOM_CPF_HMAC_KEY`.
4. **Notificação à ANPD e aos Titulares (Art. 48 da LGPD):** Em caso de incidente de segurança que possa acarretar risco ou dano relevante aos titulares, a CineSoft Solutions notificará formalmente os cinemas Controladores imediatamente e submeterá a comunicação à **Autoridade Nacional de Proteção de Dados (ANPD)** e aos titulares afetados em até **72 horas** (3 dias úteis), informando a natureza dos dados afetados, as medidas técnicas de proteção utilizadas (cifragem `AES-256-GCM` e `HMAC-SHA256`) e as ações de mitigação adotadas.
5. **Análise Pós-Incidente (*Post-Mortem*):** Conduzida em até 7 dias corridos após a contenção, documentando a causa-raiz (RCA), linha do tempo, atualização da matriz de ameaças e adição de novos testes regressivos no pipeline de CI.

---

## 7. Matriz de Riscos de Conformidade e Privacidade

| ID | Categoria | Probabilidade Inicial | Impacto | Medida de Mitigação Implementada | Risco Residual |
|---|---|---|---|---|---|
| **R-CMP-1** | Privacidade | Alta | Alto | Implementação de `HMAC-SHA256` com chave secreta de servidor (`CINEDOOM_CPF_HMAC_KEY`) para indexação de CPF, eliminando vulnerabilidade a *rainbow tables* (`ADR-008`, `CA-06`). | **Baixo** |
| **R-CMP-2** | Segurança | Alta | Alto | Armazenamento de `CPF_ENCRYPTION_KEY` (`AES-256-GCM`) exclusivamente em *Vercel Environment Secrets* cifrados, com runbook de rotação periódica e re-cifragem em lote (`ADR-008`). | **Baixo** |
| **R-CMP-3** | Segurança | Média | Alto | Bloqueio de arquivos `.env*` no controle de versão, validação de segredos em CI e separação estrita de bancos de dados de *preview* com dados sintéticos. | **Baixo** |
| **R-CMP-4** | Regulatório | Média | Alto | Implementação do endpoint administrativo de anonimização *in-place* (`POST /api/titulares/anonimizar`, `ADR-009`), runbook operacional e SLA formal de até 15 dias para atendimento ao Art. 18 da LGPD. | **Baixo** |
| **R-CMP-5** | Privacidade | Média | Alto | Isolamento multi-tenant via *Prisma Client Extension* (`ADR-003`) auditado a cada commit pela suíte de 500 cenários de segurança cross-tenant (`CA-04`, `CT-04`, `CT-18`) com tolerância zero a falhas. | **Baixo** |
| **R-CMP-6** | Regulatório | Baixa | Alto | Formalização do Plano de Resposta a Incidentes com SLA de 72 horas para notificação à ANPD (Art. 48 LGPD) e definição contratual de Controlador/Operador (`ADR-009`). | **Baixo** |
| **R-CMP-7** | Privacidade | Média | Médio | Sanitização automática de payloads no logger estruturado para garantir que CPF e e-mail nunca sejam enviados em texto claro ao Axiom Log Drain (`RF-11`, `CT-15`). | **Baixo** |
| **R-CMP-8** | Segurança | Baixa | Médio | Procedimento formal de desativação e *offboarding* de tenants encerrados, com geração de backup contratual e expurgo seguro de dados pessoais após o término do prazo legal de retenção. | **Baixo** |
