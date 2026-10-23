# Configuração do Pipeline de CI/CD, ESLint No-Cycle e Preview Vercel (ADR-005 / TASK-16)

## 1. Rastreabilidade e Governança

- **Issue:** #17 — `[CHORE(CI)] CI/CD Pipeline - GitHub Actions com typecheck, ESLint no-cycle e preview Vercel`
- **Task TechLead:** TASK-16
- **ADR Vinculada:** ADR-005 (Hospedagem na Vercel com Neon Serverless e GitHub Actions)
- **Normas de Referência:**
  - ABNT NBR ISO/IEC/IEEE 12207:2021 — Processo de Integração de Software (6.4.8) e Processo de Garantia da Qualidade (7.2.3).
  - SLSA (Supply-chain Levels for Software Artifacts) — Nível de integridade de compilação automatizada.

---

## 2. Arquitetura do Pipeline no GitHub Actions

O pipeline de Integração Contínua (CI) do CineDoom é implementado via GitHub Actions no arquivo `.github/workflows/ci.yml` do repositório `cinedoom-app`.

### 2.1 Gatilhos de Disparo
- **Push:** Ramos `main` e `develop`.
- **Pull Request:** Direcionados aos ramos `main` e `develop`.
- **Controle de Concorrência:** `concurrency` com `cancel-in-progress: true` para cancelar execuções obsoletas ao receber novos commits no mesmo PR.

### 2.2 Etapas Sequenciais do Job `validate`
1. **Checkout do Repositório:** `actions/checkout@v4` com profundidade de histórico completa.
2. **Setup do pnpm:** `pnpm/action-setup@v4` fixado na versão major 9.
3. **Setup do Node.js:** `actions/setup-node@v4` com Node.js 20 LTS e cache automático de store do pnpm.
4. **Instalação Determinística de Dependências:** `pnpm install --frozen-lockfile` garantindo integridade estrita do lockfile.
5. **Geração dos Clientes Prisma:** `pnpm prisma generate` compilando tipos do schema PostgreSQL antes dos linters e validadores.
6. **Validação Estática de Tipos (TypeScript):** `pnpm typecheck` (`tsc --noEmit`) assegurando zero erros de tipagem estrita.
7. **Linter e Análise Estática com No-Cycle:** `pnpm lint` executando ESLint com a regra `import/no-cycle` (maxDepth: 5), bloqueando dependências circulares na raiz.
8. **Execução de Testes Unitários:** `pnpm test` executando toda a suíte de testes Vitest com tempo médio inferior a 2 segundos.
9. **Compilação e Build de Produção:** `pnpm build` (`next build`) validando a compilação de todas as páginas estáticas, dinâmicas e rotas de API.

---

## 3. Prevenção de Dependências Circulares (ESLint `import/no-cycle`)

Dependências circulares provocam problemas severos em tempo de execução (módulos indefinidos, bugs sutis no NextAuth/Prisma e estouro de memória).
A regra é formalizada no arquivo `.eslintrc.json`:

```json
{
  "extends": ["next/core-web-vitals"],
  "plugins": ["import"],
  "rules": {
    "import/no-cycle": [
      "error",
      {
        "maxDepth": 5
      }
    ]
  }
}
```

Qualquer ciclo de importação gera código de saída não-zero e interrompe o pipeline no GitHub Actions.

---

## 4. Integração de Ambientes de Preview na Vercel e Neon DB Branching

Conforme estabelecido na **ADR-005**, cada Pull Request gera um ambiente de pré-visualização efêmero e isolado.

### 4.1 Vercel GitHub App Integration
- **Deploy Automático:** A Vercel intercepta a criação e atualização de Pull Requests através da GitHub App integrada à organização `CINESOFT-SOLUTIONS`.
- **Configuração do Repositório (`vercel.json`):**
  - `buildCommand`: `"pnpm prisma generate && pnpm build"`
  - `installCommand`: `"pnpm install"`
  - `framework`: `"nextjs"`
- **Domínio Efêmero:** Cada PR recebe uma URL exclusiva no formato `https://cinedoom-app-git-<branch>-cinesoft-solutions.vercel.app`.

### 4.2 Neon Database Branching (Isolamento de Dados por PR)
- O PostgreSQL do CineDoom é provisionado no **Neon Serverless**.
- A integração Vercel-Neon provisiona automaticamente um branch de banco de dados copy-on-write para cada deployment de Preview.
- O branch isolado contém o estado do banco do branch principal sem impactar os dados de produção.
- Ao aprovar e realizar o merge do PR, o branch do Neon é destruído automaticamente, mantendo custo zero e total isolamento.

---

## 5. Critérios de Aceite e Métricas de Eficiência

| Métrica / Critério | Alvo | Implementação |
|---|---|---|
| Duração total do pipeline no GitHub Actions | < 2 minutos (120s) | Cache de dependências pnpm + execução paralela de testes unitários em ~45s |
| Bloqueio obrigatório de merge em falha | 100% de cobertura | Branch protection configurado requerendo status check verde |
| Detecção de ciclos de importação | 0 tolerância | ESLint `import/no-cycle` ativado |
| Status visível no repositório | README com badge | Badge oficial do GitHub Actions apontando para `ci.yml` |
