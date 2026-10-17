# Prompt — Parte 0: Apresentação do Software

## 1. Identificação
- **Código:** `PR-P00_Apresentacao_Software`
- **Parte do Trabalho:** Parte 0 – Apresentação do Software (Módulo Fundação)
- **Papel no Manual:** Base de todo o documento — todos os módulos subsequentes (Partes 1 a 4) fazem referência direta a esta seção.
- **Norma / Cláusula de Referência:** ABNT NBR ISO/IEC/IEEE 12207:2021 — Insumo preliminar e contextual para definição de necessidades de stakeholders (6.4.2) e requisitos de sistema (6.4.3).
- **Documento-base da Verdade:** `docs/constituicao/project-definition-workbook.md` (Seções 1, 2, 3, 5, 6, 7, 8, 9 e 10).
- **Diretrizes Pedagógicas:** `docs/instrucoes-disciplina.md` (Diretrizes da Profa. Dra. Juliana Zinader).

---

## 2. Prompt Estruturado (Input para IA)

```markdown
Você é o Engenheiro de Requisitos e Arquiteto de Software Líder da CineSoft Solutions.
Estamos elaborando o documento oficial "Manual de Processos de Software" para a disciplina de Processos de Engenharia de Software da UFG (Profa. Dra. Juliana Pereira de Souza Zinader).

Sua tarefa é gerar o conteúdo completo, técnico e detalhado da:
"PARTE 0: Apresentação do Software — Sistema CineDoom"

Esta seção é a base fundacional de todo o manual. Todos os módulos posteriores (processos de acordo, organizacionais, gerenciamento técnico e processos técnicos da ISO 12207) dependerão estritamente do contexto estabelecido aqui.

---

### [CONTEXTO E FONTES DA VERDADE]
1. Organização Fictícia: CineSoft Solutions — software-house de pequeno/médio porte focada no mercado de entretenimento (PDW Seção 2).
2. Produto: CineDoom — plataforma web de gerenciamento operacional para cinemas de pequeno e médio porte (PDW Seção 1).
3. Fonte Oficial das Decisões: Você DEVE respeitar estritamente o Project Definition Workbook (`docs/constituicao/project-definition-workbook.md`). Não invente funcionalidades, tecnologias ou integrações divergentes do PDW.
4. Regra de Ouro Docente (Critério Transversal): 
   ⭐ QUALIDADE > QUANTIDADE. O artefato não deve ser extenso nem prolixo — deve ser consistente, justificado e estritamente aplicado ao CineDoom. Use linguagem técnica, clara e objetiva, sem marketing, clichês ou "encher linguiça".

---

### [ESTRUTURA OBRIGATÓRIA DA RESPOSTA]

Estruture a resposta com os 4 tópicos mínimos exigidos pela docente:

#### 0.1 Nome e Descrição do Software
- Nome oficial e caracterização precisa da solução (evite generalismos como "um sistema de cinema"; seja específico: plataforma web de gestão operacional e bilheteria física para exibidores independentes).
- Qual problema central resolve? (Controles manuais em planilhas/cadernos, falta de rastreabilidade de assentos, concorrência desordenada em horários de pico, ausência de consolidação de faturamento por sessão).
- Proposta de valor e vínculo com a organização responsável (CineSoft Solutions).

#### 0.2 Público-Alvo e Contexto de Uso
- Quem vai usar? Detalhe os perfis reais de usuários identificados no PDW (Operador de Caixa / Bilheteiro, Gerente de Operações do Cinema, Administrador de TI / Suporte e o Cliente Final espectador no guichê).
- Em que situação de uso o sistema é acionado? (Rotina matinal de abertura de sessão, horários de pico de filas antes das sessões noturnas de fim de semana, fechamento diário de caixa e auditoria de faturamento).
- Ambiente de operação esperado: Ambientes físicos e computacionais (navegadores web modernos em computadores dos guichês e escritório da gerência, operando em rede local estável com sincronização em nuvem).

#### 0.3 Escopo e Principais Funcionalidades
- O que está DENTRO do escopo (Funcionalidades Centrais):
  1. Catálogo e Programação de Filmes (título, classificação indicativa, duração, distribuidora).
  2. Gestão de Salas e Assentos (layout de poltronas, assentos PCD/mobilidade reduzida, status em tempo real: livre, selecionado, ocupado, bloqueado).
  3. Grade e Programação de Sessões (alocação de salas, regras anti-sobreposição de horários, intervalo técnico de limpeza).
  4. Emissão e Cancelamento de Ingressos (atendimento no guichê, código único do bilhete, meia-entrada legal, comprovante físico/digital).
  5. Cadastro e Histórico de Clientes (dados essenciais de identificação, fidelidade e comprovação de benefícios).
  6. Relatórios Operacionais e Gerenciais (taxa de ocupação por sala, faturamento por sessão e relatório de fechamento de caixa).
- O que fica FORA do escopo inicial (Fronteira Explícita do Sistema - PDW Seção 5):
  - Pagamentos online via internet / e-commerce próprio (nesta fase a venda é exclusiva no balcão físico).
  - Aplicativo mobile nativo para o consumidor final.
  - Módulo de bomboniere/concessão (venda de pipoca e alimentos é gerenciada separadamente).

#### 0.4 Restrições e Premissas
- Restrições Tecnológicas e Arquiteturais: Sistema desenvolvido como aplicação Web monolítica modular (React no frontend, Node.js no backend, banco de dados relacional PostgreSQL conforme PDW Seções 10 e 11), sem exigência de instalação local pesada.
- Restrições Regulatórias e Legais:
  - Conformidade com a Lei da Meia-Entrada (Lei Federal nº 12.933/2013 - cota obrigatória de 40% por sessão).
  - Acessibilidade e inclusão (Norma ABNT NBR 9050 para reserva de assentos acessíveis para pessoas com deficiência e mobilidade reduzida).
  - Proteção de Dados (LGPD - Lei nº 13.709/2018: minimização de coleta de dados pessoais no balcão).
- Premissas do Projeto:
  - Disponibilidade de infraestrutura de rede estável nas instalações do cinema.
  - Conexão concorrente de guichês sem sobreposição de reserva de um mesmo assento (bloqueio atômico de assento).
  - Equipe operacional capacitada nos fluxos de atendimento do PDV.

---

### [VALIDAÇÃO OBRIGATÓRIA DA SAÍDA]
Ao gerar o texto:
1. Submeta a resposta ao `prompts/auditor-de-qualidade.md`.
2. Gere o laudo crítico de auditoria e salve-o em:
   `docs/validacoes/parte-00/analise-validacao-parte-00.md`
3. Salve o rascunho textual consolidado em:
   `docs/rascunhos/parte-00/rascunho-parte-00.md`
4. Confirme que todos os critérios transversais (qualidade > quantidade, linguagem técnica e coerência intermódulos) receberam avaliação positiva.
```

---

## 3. Fluxo de Trabalho Integrado
1. **Passo 1 (Prompt):** Executar este prompt com o modelo de IA.
2. **Passo 2 (Auditoria):** Rodar o [`prompts/auditor-de-qualidade.md`](../auditor-de-qualidade.md) sobre o texto gerado.
3. **Passo 3 (Laudo):** Armazenar a avaliação em [`docs/validacoes/parte-00/analise-validacao-parte-00.md`](../../docs/validacoes/parte-00/analise-validacao-parte-00.md).
4. **Passo 4 (Rascunho):** Ajustar o texto conforme as recomendações do laudo e salvar em [`docs/rascunhos/parte-00/rascunho-parte-00.md`](../../docs/rascunhos/parte-00/rascunho-parte-00.md).
5. **Passo 5 (Manual Oficial):** Incorporar a versão aprovada na Seção "Parte 0" de [`manual-processos-software.md`](../../manual-processos-software.md).
