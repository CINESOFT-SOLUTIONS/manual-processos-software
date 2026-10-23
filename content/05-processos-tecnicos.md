# Capítulo 5 – Processos Técnicos

## 5.1 Requisitos

### 5.1.1 Documento de requisitos do sistema
Os requisitos são classificados formalmente em funcionais (RF-01 a RF-12) e não funcionais (RNF-01 a RNF-05), com identificador único, descrição concisa e priorização pelo método MoSCoW:
- **RNF-01 (Desempenho):** O mapa de assentos e as ações de bilheteria devem responder em menos de 2 segundos.
- **RNF-02 (Confiabilidade):** O sistema deve impedir que duas requisições comprem o mesmo assento na mesma sessão.
- **RNF-03 (Segurança):** Todas as comunicações devem trafegar via protocolo seguro HTTPS.
- **RNF-04 (Usabilidade):** Interface acessível com representação cromática clara de status de assento.

### 5.1.2 Rastreabilidade de requisitos
Cada requisito é rastreado por meio da cadeia:
$$\text{Necessidade do Negócio} \longrightarrow \text{RF} \longrightarrow \text{ADR} \longrightarrow \text{Commit/PR} \longrightarrow \text{Teste Automatizado} \longrightarrow \text{Release}$$

### 5.1.3 Critérios de aceitação
Os critérios de aceitação para o fluxo principal exigem: seleção livre de assento no mapa, confirmação da compra com transação gravada no banco, emissão do código identificador do ingresso e bloqueio imediato do assento para novos clientes.

### 5.1.4 Registro de stakeholders e necessidades elicitadas
Mapeamento formal dos interesses de proprietários de cinemas, gerentes operacionais e atendentes de bilheteria, com registro de prioridades na matriz de requisitos e critérios de aceite do projeto.

## 5.2 Arquitetura e Design

### 5.2.1 Documento de arquitetura do sistema
Arquitetura em camadas no modelo Monólito Modular:
1. **Camada de Apresentação:** Componentes React com renderização client-side reativa para o mapa de assentos.
2. **Camada de Controle e API:** Rotas Next.js Serverless processando payloads REST.
3. **Camada de Domínio / Serviços:** Regras de negócio encapsuladas para cálculo de assentos e integridade de transação.
4. **Camada de Acesso a Dados:** Prisma Client mapeando consultas no PostgreSQL Neon.

### 5.2.2 Diagramas de design
- **Diagrama de Contêineres (Modelo C4):** Ilustra a interação entre navegador do cliente, aplicação Next.js na Vercel e o banco Neon PostgreSQL.
- **Diagrama de Atividades (UML / BPMN):** Mapeia o fluxo da transação de venda de ingressos, desde a seleção da cadeira até a confirmação atômica ou reversão por conflito.

### 5.2.3 Justificativa das escolhas tecnológicas
O ecossistema Next.js com Prisma e Neon oferece a maior velocidade de entrega para uma equipe enxuta, permitindo tipagem ponta a ponta em TypeScript e validação de banco com ORM moderno.

## 5.3 Implementação e Integração

### 5.3.1 Padrões de codificação adotados
Adoção do guia padrão de TypeScript com ESLint e Prettier configurados para manter consistência semântica e estilística.

### 5.3.2 Plano de integração entre componentes
A integração entre o mapa de assentos e o backend de bilheteria ocorre via requisições assíncronas com tratamento explícito de estados de erro HTTP (ex.: 409 Conflict em caso de assento ocupado).

### 5.3.3 Registro de testes unitários e de integração
Suíte de testes desenvolvida no framework **Vitest**:
- Testes unitários para cálculos de capacidade de salas e ocupação percentual.
- Testes de integração simulando requisições paralelas para compra do mesmo assento na mesma sessão, comprovando que o banco rejeita a segunda compra.

### 5.3.4 Rastreabilidade entre código e requisitos
Os arquivos e funções de teste contêm em suas assinaturas a referência explícita ao requisito (ex.: `describe('RF-07: Registro de Venda de Ingresso')`).

## 5.4 Verificação, Validação e Transição

### 5.4.1 Plano de verificação e validação
- **Verificação:** Executada a cada PR pela esteira de CI do GitHub Actions (compilação de código, lint e testes automatizados).
- **Validação:** Homologação com dados realistas de cinema para garantir que o fluxo atende ao contexto operacional da bilheteria.

### 5.4.2 Critérios de aceitação por stakeholder
Critérios definidos para o Perfil Gerente (capacidade de agendar sessões) e Perfil Atendente (agilidade no fechamento de pedidos de ingressos).

### 5.4.3 Relatório de testes de aceitação
Registro documentado evidenciando o comportamento esperado e obtido em cada cenário de teste funcional.

### 5.4.4 Plano de transição/implantação do sistema
A transição para o ambiente de produção na Vercel ocorre automaticamente a cada merge aprovado na branch `main`. Procedimentos de migração executados via `npx prisma migrate deploy`.

## 5.5 Operação, Manutenção e Descontinuação

### 5.5.1 Procedimentos de operação e monitoramento
Monitoramento de logs de execução e latência via painel analítico da Vercel e console de métricas do banco Neon.

### 5.5.2 Plano de manutenção (corretiva, preventiva, adaptativa)
Fluxo documentado para abertura de issues de defeito, priorização de correção e publicação de hotfixes com testes de regressão.

### 5.5.3 Estratégia de descontinuação e migração de dados
Diretrizes para expurgo seguro de dados, geração de dumps relacionais para o cliente e encerramento de instâncias conforme exigido pela LGPD e pelos processos de encerramento da ISO 12207.
