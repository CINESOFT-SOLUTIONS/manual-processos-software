---
kind: agent_artifact
feature_id: F-CINEDOOM-PLATAFORMA-B2B-SAAS-C
agent: UI
generated_by:
  run_id: run_2026-10-23T03-58-17_eedeb0ce
  session_id: 2026-09-03T15-33-01-hdb88xzyiu
  model: anthropic:claude-sonnet-4-6
generated_at: 2026-10-23T04:37:47.696Z
regenerative: true
title: "[UI] CineDoom — plataforma B2B SaaS para cinemas independentes e redes de pequeno/méd"
---

# UI — CineDoom — plataforma B2B SaaS para cinemas independentes e redes de pequeno/méd

> Artefato derivado de `.specs/features/F-CINEDOOM-PLATAFORMA-B2B-SAAS-C/spec.md` e gerado pelo agente **UI**
> via AI-4SDLC Platform. **Regenerative work product** (não-canonical SDD).
> Não edite manualmente — re-gere via `sdlc resume`.

## Resumo

UI mockups HTML fallback para CineDoom MVP — plataforma B2B SaaS de bilheteria e back-office para cinemas independentes. Telas: Login, Mapa de Assentos (Atendente), Modal de Venda, Painel de Ocupação (Gerente) e Back-Office (filmes/salas/sessões).

> **Mode:** `html_fallback`

## Frames

- **FRAME-1** Login — PNG: `/20-design/ui-mockups/login.png`
- **FRAME-2** Mapa de Assentos - Atendente — PNG: `/20-design/ui-mockups/mapa-assentos.png`
- **FRAME-3** Modal Confirmacao Venda — PNG: `/20-design/ui-mockups/modal-venda.png`
- **FRAME-4** Painel de Ocupacao - Gerente — PNG: `/20-design/ui-mockups/painel-ocupacao.png`
- **FRAME-5** Back-Office Filmes — PNG: `/20-design/ui-mockups/backoffice-filmes.png`
- **FRAME-6** Back-Office Salas e Sessoes — PNG: `/20-design/ui-mockups/backoffice-sessoes.png`
- **FRAME-7** Cadastro de Usuario Atendente — PNG: `/20-design/ui-mockups/cadastro-usuario.png`

## Design tokens

**Colors:**
- `primary`: `#1A1A2E`
- `cta`: `#E94560`
- `neutralBg`: `#F5F5F5`
- `card`: `#FFFFFF`
- `textMain`: `#2D2D2D`
- `textSecondary`: `#6B7280`
- `seatAvailable`: `#22C55E`
- `seatSold`: `#EF4444`
- `seatSelected`: `#3B82F6`
- `seatBlocked`: `#9CA3AF`

**Typography:**
- `heading`: `Inter Bold 24px`
- `subheading`: `Inter SemiBold 18px`
- `body`: `Inter 14px`
- `caption`: `Inter 12px`

**Spacing scale:**
- `base`: `4px`
- `lg`: `24px`

**Radii:**
- `card`: `6px`
- `badge`: `4px`

## Fallback HTML preview

> Preview-only (não código de produção).

```html
<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"/><title>CineDoom Mockups</title><script src="https://cdn.tailwindcss.com"></script></head><body class="bg-gray-100 text-sm font-sans text-gray-800 p-6 space-y-12">

<!-- FRAME 1: LOGIN -->
<section>
  <h2 class="text-xs uppercase tracking-widest text-gray-400 mb-3">FRAME-1 · Login</h2>
  <div class="max-w-sm mx-auto bg-white rounded-md shadow-sm p-8 space-y-5">
    <div class="text-center">
      <div class="text-2xl font-bold" style="color:#1A1A2E">CineDoom</div>
      <p class="text-xs text-gray-500 mt-1">Plataforma B2B de Bilheteria</p>
    </div>
    <div class="space-y-3">
      <div>
        <label class="block text-xs font-medium mb-1">E-mail</label>
        <input class="w-full border rounded px-3 py-2 text-sm" placeholder="atendente@cinema.com" />
      </div>
      <div>
        <label class="block text-xs font-medium mb-1">Senha</label>
        <input type="password" class="w-full border rounded px-3 py-2 text-sm" placeholder="••••••••" />
      </div>
    </div>
    <button class="w-full py-2 rounded text-white text-sm font-semibold" style="background:#E94560">Entrar</button>
  </div>
</section>

<!-- FRAME 2: MAPA DE ASSENTOS -->
<section>
  <h2 class="text-xs uppercase tracking-widest text-gray-400 mb-3">FRAME-2 · Mapa de Assentos — Atendente</h2>
  <div class="bg-white rounded-md shadow-sm p-6 max-w-2xl mx-auto space-y-4">
    <div class="flex items-center justify-between">
      <div>
        <div class="font-semibold" style="color:#1A1A2E">Duna: Parte Dois — Sala 2</div>
        <div class="text-xs text-gray-500">Hoje 19:30 · 120 lugares</div>
      </div>
      <span class="text-xs px-2 py-0.5 rounded font-medium bg-blue-100 text-blue-700">Polling 2s ativo</span>
    </div>
    <!-- Legenda -->
    <div class="flex gap-4 text-xs">
      <span class="flex items-center gap-1"><span class="w-3 h-3 rounded-sm inline-block" style="background:#22C55E"></span>Disponível</span>
      <span class="flex items-center gap-1"><span class="w-3 h-3 rounded-sm inline-block" style="background:#EF4444"></span>Vendido</span>
      <span class="flex items-center gap-1"><span class="w-3 h-3 rounded-sm inline-block" style="background:#3B82F6"></span>Selecionado</span>
      <span class="flex items-center gap-1"><span class="w-3 h-3 rounded-sm inline-block" style="background:#9CA3AF"></span>Bloqueado</span>
    </div>
    <!-- Grid assentos (5x10 simplificado) -->
    <div class="grid gap-1" style="grid-template-columns:repeat(10,2rem)">
      <!-- Linha A: alguns vendidos -->
      <div class="w-8 h-8 rounded-sm" style="background:#EF4444"></div>
      <div class="w-8 h-8 rounded-sm" style="background:#EF4444"></div>
      <div class="w-8 h-8 rounded-sm" style="background:#22C55E"></div>
      <div class="w-8 h-8 rounded-sm" style="background:#22C55E"></div>
      <div class="w-8 h-8 rounded-sm" style="background:#3B82F6"></div>
      <div class="w-8 h-8 rounded-sm" style="background:#22C55E"></div>
      <div class="w-8 h-8 rounded-sm" style="background:#22C55E"></div>
      <div class="w-8 h-8 rounded-sm" style="background:#9CA3AF"></div>
      <div class="w-8 h-8 rounded-sm" style="background:#22C55E"></div>
      <div class="w-8 h-8 rounded-sm" style="background:#EF4444"></div>
      <!-- Linha B -->
      <div class="w-8 h-8 rounded-sm" style="background:#22C55E"></div>
      <div class="w-8 h-8 rounded-sm" style="background:#22C55E"></div>
      <div class="w-8 h-8 rounded-sm" style="background:#EF4444"></div>
      <div class="w-8 h-8 rounded-sm" style="background:#22C55E"></div>
      <div class="w-8 h-8 rounded-sm" style="background:#22C55E"></div>
      <div class="w-8 h-8 rounded-sm" style="background:#EF4444"></div>
      <div class="w-8 h-8 rounded-sm" style="background:#22C55E"></div>
      <div class="w-8 h-8 rounded-sm" style="background:#22C55E"></div>
      <div class="w-8 h-8 rounded-sm" style="background:#22C55E"></div>
      <div class="w-8 h-8 rounded-sm" style="background:#22C55E"></div>
    </div>
    <div class="text-center text-xs text-gray-400">[ TELA ]</div>
    <div class="flex justify-between items-center pt-2">
      <span class="text-xs text-gray-500">Assento selecionado: <strong>A5</strong></span>
      <button class="px-4 py-2 rounded text-white text-sm font-semibold" style="background:#E94560">Vender Ingresso</button>
    </div>
  </div>
</section>

<!-- FRAME 3: MODAL CONFIRMAÇÃO VENDA -->
<section>
  <h2 class="text-xs uppercase tracking-widest text-gray-400 mb-3">FRAME-3 · Modal Confirmação de Venda</h2>
  <div class="max-w-md mx-auto bg-white rounded-md shadow-sm p-6 space-y-4 border border-gray-200">
    <div class="font-semibold text-base" style="color:#1A1A2E">Confirmar Venda — Assento A5</div>
    <div class="space-y-3">
      <div>
        <label class="block text-xs font-medium mb-1">Nome do Comprador <span class="text-red-500">*</span></label>
        <input class="w-full border rounded px-3 py-2 text-sm" placeholder="Maria da Silva" />
      </div>
      <div>
        <label class="block text-xs font-medium mb-1">CPF <span class="text-red-500">*</span></label>
        <input class="w-full border rounded px-3 py-2 text-sm" placeholder="000.000.000-00" />
      </div>
      <div>
        <label class="block text-xs font-medium mb-1">E-mail <span class="text-red-500">*</span></label>
        <input class="w-full border rounded px-3 py-2 text-sm" placeholder="maria@email.com" />
      </div>
      <div class="flex items-start gap-2 text-xs text-gray-500 bg-gray-50 rounded p-3">
        <input type="checkbox" class="mt-0.5" />
        <span>Comprador consente com a coleta e uso dos dados conforme LGPD. <strong>Campo obrigatório.</strong></span>
      </div>
    </div>
    <div class="flex gap-3 justify-end">
      <button class="px-4 py-2 rounded border text-sm">Cancelar</button>
      <button class="px-4 py-2 rounded text-white text-sm font-semibold" style="background:#E94560">Confirmar Venda</button>
    </div>
  </div>
</section>

<!-- FRAME 4: PAINEL OCUPAÇÃO -->
<section>
  <h2 class="text-xs uppercase tracking-widest text-gray-400 mb-3">FRAME-4 · Painel de Ocupação — Gerente</h2>
  <div class="bg-white rounded-md shadow-sm p-6 max-w-3xl mx-auto space-y-4">
    <div class="flex items-center justify-between">
      <div class="font-semibold text-base" style="color:#1A1A2E">Ocupação do Dia — 15/01/2025</div>
      <span class="text-xs px-2 py-0.5 rounded font-medium" style="background:#1A1A2E;color:#fff">GERENTE</span>
    </div>
    <table class="w-full text-sm">
      <thead>
        <tr class="text-left text-xs text-gray-500 border-b">
          <th class="pb-2">Filme</th><th class="pb-2">Sala</th><th class="pb-2">Horário</th><th class="pb-2">Vendidos/Total</th><th class="pb-2">Ocupação</th>
        </tr>
      </thead>
      <tbody class="divide-y">
        <tr class="py-2">
          <td class="py-2">Duna: Parte Dois</td><td>Sala 2</td><td>19:30</td><td>87/120</td>
          <td><div class="w-32 bg-gray-200 rounded h-2"><div class="h-2 rounded" style="width:73%;background:#E94560"></div></div><span class="text-xs ml-1">73%</span></td>
        </tr>
        <tr>
          <td class="py-2">Kung Fu Panda 4</td><td>Sala 1</td><td>15:00</td><td>45/80</td>
          <td><div class="w-32 bg-gray-200 rounded h-2"><div class="h-2 rounded" style="width:56%;background:#E94560"></div></div><span class="text-xs ml-1">56%</span></td>
        </tr>
        <tr>
          <td class="py-2">Duna: Parte Dois</td><td>Sala 2</td><td>21:45</td><td>12/120</td>
          <td><div class="w-32 bg-gray-200 rounded h-2"><div class="h-2 rounded" style="width:10%;background:#22C55E"></div></div><span class="text-xs ml-1">10%</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<!-- FRAME 5: BACK-OFFICE FILMES -->
<section>
  <h2 class="text-xs uppercase tracking-widest text-gray-400 mb-3">FRAME-5 · Back-Office — Filmes</h2>
  <div class="bg-white rounded-md shadow-sm p-6 max-w-3xl mx-auto space-y-4">
    <div class="flex items-center justify-between">
      <div class="font-semibold text-base" style="color:#1A1A2E">Catálogo de Filmes</div>
      <button class="px-3 py-1.5 rounded text-white text-xs font-semibold" style="background:#E94560">+ Novo Filme</button>
    </div>
    <table class="w-full text-sm">
      <thead>
        <tr class="text-left text-xs text-gray-500 border-b">
          <th class="pb-2">Título</th><th class="pb-2">Gênero</th><th class="pb-2">Duração</th><th class="pb-2">Ações</th>
        </tr>
      </thead>
      <tbody class="divide-y">
        <tr><td class="py-2">Duna: Parte Dois</td><td>Ficção</td><td>166 min</td><td class="space-x-2"><a class="text-blue-600 text-xs" href="#">Editar</a></td></tr>
        <tr><td class="py-2">Kung Fu Panda 4</td><td>Animação</td><td>94 min</td><td class="space-x-2"><a class="text-blue-600 text-xs" href="#">Editar</a></td></tr>
      </tbody>
    </table>
  </div>
</section>

<!-- FRAME 6: BACK-OFFICE SESSÕES -->
<section>
  <h2 class="text-xs uppercase tracking-widest text-gray-400 mb-3">FRAME-6 · Back-Office — Salas e Sessões</h2>
  <div class="bg-white rounded-md shadow-sm p-6 max-w-3xl mx-auto space-y-4">
    <div class="flex items-center justify-between">
      <div class="font-semibold text-base" style="color:#1A1A2E">Sessões</div>
      <button class="px-3 py-1.5 rounded text-white text-xs font-semibold" style="background:#E94560">+ Nova Sessão</button>
    </div>
    <table class="w-full text-sm">
      <thead>
        <tr class="text-left text-xs text-gray-500 border-b">
          <th class="pb-2">Filme</th><th class="pb-2">Sala</th><th class="pb-2">Data/Hora</th><th class="pb-2">Ações</th>
        </tr>
      </thead>
      <tbody class="divide-y">
        <tr><td class="py-2">Duna: Parte Dois</td><td>Sala 2</td><td>15/01 19:30</td><td><a class="text-blue-600 text-xs" href="#">Editar</a></td></tr>
        <tr><td class="py-2">Kung Fu Panda 4</td><td>Sala 1</td><td>15/01 15:00</td><td><a class="text-blue-600 text-xs" href="#">Editar</a></td></tr>
      </tbody>
    </table>
  </div>
</section>

<!-- FRAME 7: CADASTRO ATENDENTE -->
<section>
  <h2 class="text-xs uppercase tracking-widest text-gray-400 mb-3">FRAME-7 · Cadastro de Usuário Atendente</h2>
  <div class="max-w-sm mx-auto bg-white rounded-md shadow-sm p-6 space-y-4">
    <div class="font-semibold text-base" style="color:#1A1A2E">Novo Atendente</div>
    <div class="space-y-3">
      <div>
        <label class="block text-xs font-medium mb-1">Nome Completo</label>
        <input class="w-full border rounded px-3 py-2 text-sm" placeholder="João Silva" />
      </div>
      <div>
        <label class="block text-xs font-medium mb-1">E-mail</label>
        <input class="w-full border rounded px-3 py-2 text-sm" placeholder="joao@cinema.com" />
      </div>
      <div>
        <label class="block text-xs font-medium mb-1">Perfil</label>
        <select class="w-full border rounded px-3 py-2 text-sm"><option>ATENDENTE</option></select>
        <p class="text-xs text-gray-400 mt-1">Apenas GERENTE pode criar usuários. Perfil fixo: ATENDENTE.</p>
      </div>
    </div>
    <button class="w-full py-2 rounded text-white text-sm font-semibold" style="background:#E94560">Criar Conta</button>
  </div>
</section>

</body></html>
```
