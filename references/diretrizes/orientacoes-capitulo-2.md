# Orientações para o Capítulo 2: Processos de Acordo

Documento de diretrizes e requisitos para a elaboração do **Capítulo 2** do Manual de Processos de Software, baseado na **Seção 6.1 da ABNT NBR ISO/IEC/IEEE 12207:2021** e no material da **Aula 2**.

---

## 2.1 Objetivo do Capítulo

Formalizar as decisões da equipe quanto à aquisição de serviços externos versus desenvolvimento interno (Make or Buy), e analisar o potencial do sistema desenvolvido para fornecimento a outros parceiros e clientes no mercado.

---

## 2.2 Atividade Pedagógica da Aula 2 (Passo a Passo)

Conforme a **Aula 2** (*Processos de Acordo*), a equipe deve cumprir 5 passos metodológicos:

- **Passo 1 — Relembrar o Sistema:** Contextualizar o escopo do produto da equipe.
- **Passo 2 — Listar as Principais Funcionalidades:** Mapear as capacidades centrais do software.
- **Passo 3 — Mapear os Elementos do Sistema:** Decompor a solução em módulos, bibliotecas, microsserviços, componentes ou serviços de infraestrutura.
- **Passo 4 — Perspectiva de Aquisição (Adquirir Pronto?):** Avaliar para cada elemento a viabilidade de aquisição externa (SaaS, biblioteca, API de terceiro) versus construir internamente.
- **Passo 5 — Perspectiva de Fornecimento:** Identificar elementos do sistema que possuem valor autônomo e poderiam ser comercializados/fornecidos para clientes externos (como API, SaaS ou licença).

---

## 2.3 Estrutura Mínima e Tabelas Exigidas

### 2.1 Processo de Aquisição (Seção 6.1.1 da ISO 12207)
A equipe deve apresentar a **Tabela de Análise de Aquisição**:

| Elemento do Sistema | Adquirir pronto? | Justificativa Técnica/Negócio | Possível Fornecedor / Tecnologia |
| :--- | :---: | :--- | :--- |
| *Ex: Autenticação e controle de acesso* | *Sim* | *Solução madura, segura e certificada; alto custo de fazer do zero* | *Auth0 / Supabase Auth* |
| *Ex: Reserva e seleção de assentos* | *Não* | *Regra central do cinema; diferencial competitivo do produto* | *Desenvolvimento Interno* |
| *Ex: Banco de Dados e Infraestrutura* | *Sim* | *Eficiência de escalabilidade e alta disponibilidade gerenciada* | *Neon PostgreSQL / Vercel* |

Além da tabela, descrever sucintamente as 5 atividades de aquisição da norma:
1. **Preparação para a aquisição:** Critérios de seleção e custo.
2. **Divulgação e seleção de fornecedores:** Comparação de opções.
3. **Formalização e manutenção do acordo:** Termos de serviço, SLAs e conformidade.
4. **Monitoramento do acordo:** Acompanhamento de custos, uptime e qualidade.
5. **Aceite do serviço/produto:** Testes de conformidade e integração.

---

### 2.2 Processo de Fornecimento (Seção 6.1.2 da ISO 12207)
A equipe deve apresentar a **Tabela de Perspectiva de Fornecimento**:

| Elemento com Potencial de Fornecimento | Possível Adquirente | Modelo de Acordo |
| :--- | :--- | :--- |
| *Ex: API de Mapa de Assentos em Tempo Real* | *Teatros, casas de shows e arenas esportivas* | *API RESTful sob assinatura (SaaS)* |
| *Ex: Módulo de Validação de Meia-Entrada Legal* | *Outras ticketeiras e eventos culturais* | *API por consulta (Pay-per-use)* |

> **💡 Dica da Professora:** O que é desenvolvido internamente como diferencial competitivo hoje pode se tornar um ativo de fornecimento comercial amanhã.
