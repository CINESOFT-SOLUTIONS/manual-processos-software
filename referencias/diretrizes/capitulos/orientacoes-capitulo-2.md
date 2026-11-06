# Orientações para o Capítulo 2: Processos de Acordo

Neste capítulo, a equipe formalizará as decisões sobre o que construir internamente versus o que adquirir pronto de terceiros, além de analisar o potencial do sistema desenvolvido como ativo de fornecimento. A atividade é fundamentada na Seção 6.1 da ABNT NBR ISO/IEC/IEEE 12207:2021.

# **2.1 Processo de aquisição**

Descrevam o processo de aquisição da equipe: o que o projeto precisaria contratar ou adquirir de terceiros (ex.: APIs, bancos de dados em nuvem, serviços de autenticação, bibliotecas ou plataformas de hospedagem).

Preencham a tabela de análise de aquisição para cada elemento mapeado no sistema:

| Elemento do sistema | Adquirir pronto? | Justificativa | Possível fornecedor |
| :--- | :---: | :--- | :--- |
| [Módulo / Serviço / Biblioteca] | [Sim / Não / Parcial] | [Por que adquirir ou fazer do zero?] | [Provedor / API / Tecnologia] |

Classifiquem como:
- **Sim:** Solução madura, commodity ou de alto custo para desenvolver internamente.
- **Não:** Regra de negócio central da aplicação, núcleo de valor e diferencial competitivo.
- **Parcial:** A estrutura visual ou engine externa é aproveitada, mas as regras de negócio são desenvolvidas pela equipe.

Expliquem brevemente como a equipe conduz as cinco atividades de aquisição da norma: preparação, divulgação/seleção, estabelecimento do acordo, monitoramento e aceite do serviço.

# **2.2 Processo de fornecimento**

Descrevam o processo de fornecimento: como o software desenvolvido seria entregue, mantido ou licenciado a clientes, parceiros e outros sistemas.

Identifiquem quais elementos desenvolvidos internamente possuem valor autônomo e poderiam ser comercializados ou integrados externamente:

| Elemento com potencial | Possível adquirente | Modelo de acordo |
| :--- | :--- | :--- |
| [Módulo / API / Recurso interno] | [Quem se beneficiaria desse recurso?] | [API pública / Licença / SaaS] |

Expliquem os termos do acordo com o cliente: critérios de aceite, conformidade com requisitos, suporte e modelo de disponibilização da solução.

# **2.3 Identificação dos fornecedores e parceiros relevantes**

Listem os fornecedores e parceiros críticos para a operação contínua do software. Indiquem as dependências externas que podem impactar a disponibilidade, o custo ou a segurança da solução.

# **Artefatos e Assets Visuais Obrigatórios e Recomendados**

Para cumprir as diretrizes da aula e da ISO 12207, a equipe deve incluir os seguintes artefatos:
- **Tabelas Estruturadas Obrigatórias:**
  - Tabela 1: *Análise de Aquisição Make or Buy* (com colunas: Elemento, Adquirir pronto?, Justificativa, Possível fornecedor).
  - Tabela 2: *Perspectiva de Fornecimento* (com colunas: Elemento com potencial, Possível adquirente, Modelo de acordo).
- **Prints / Evidências Recomendadas** (salvos em `assets/prints/`):
  - Screenshot dos consoles de provedores terceiros configurados no projeto (ex.: dashboard do banco de dados na Neon/Supabase, console de deploy na Vercel ou painel de API de e-mails transacionais como Resend).

# **Critérios de avaliação**

Apresentem as seções 2.1 a 2.3 no Manual de Processos de Software. A avaliação considerará a solidez da justificativa técnica de cada item (Make or Buy), a coerência da análise de fornecimento e o alinhamento com os preceitos da ISO/IEC/IEEE 12207:2021.
