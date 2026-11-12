---
document_id: SPEC-CINEDOOM-UI-MOCKUPS-001
version: "2.0.0"
date: "2026-11-05"
status: "Aprovado e Consolidado"
standard: "ABNT NBR ISO/IEC/IEEE 12207:2021 (Cláusula 6.4.5 — Design de Interface)"
title: "Especificação de Interface (UI), Tokens de Design e Protótipos HTML — CineDoom"
---

# Especificação de Interface (UI), Tokens de Design e Protótipos HTML — CineDoom

> **Documento Técnico Oficial — CineSoft Solutions (UFG/INF — Processos de Software 2026/1)**
> Rastreabilidade direta com [`cinedoom-spec.md`](../cinedoom-spec.md) (`HU-01` a `HU-11`, `RF-01` a `RF-18`, `RNF-04`, `RNF-05`, `CA-01` a `CA-15`) e [`ux-design.md`](ux-design.md).

## Resumo Executivo

Especificação visual de interface de usuário (UI), tokens de design e protótipos HTML estruturais para o **CineDoom**, contemplando as telas de **Login**, **Mapa de Assentos da Bilheteria (Atendente)**, **Modal de Venda com Consentimento LGPD**, **Painel de Ocupação (Gerente)**, **Gestão de Back-Office (Filmes, Salas, Sessões e Usuários)** e **Portal do Cliente (Catálogo, Reserva de Poltronas, Voucher e Minhas Reservas)**.

---

## 1. Telas Especificadas (Frames)

- **FRAME-1:** Tela de Autenticação (Login) — `RF-01`, `RF-14`
- **FRAME-2:** Mapa de Assentos Interativo com Polling de 2s (Atendente) — `RF-05`, `CA-02`
- **FRAME-3:** Modal de Confirmação de Venda e Consentimento LGPD — `RF-06`, `RF-09`, `CA-01`, `CA-06`
- **FRAME-4:** Painel de Ocupação em Tempo Real (Gerente) — `RF-10`, `CA-07`
- **FRAME-5:** Gestão (Back-Office) — Catálogo de Filmes — `RF-02`, `CA-08`
- **FRAME-6:** Gestão (Back-Office) — Salas e Sessões — `RF-03`, `RF-04`, `CA-08`
- **FRAME-7:** Gestão (Back-Office) — Cadastro de Usuário Atendente — `RF-01`, `CA-05`
- **FRAME-8:** Portal do Cliente — Catálogo de Filmes e Grade de Sessões — `RF-12`
- **FRAME-9:** Portal do Cliente — Seleção de Poltronas, Reserva e Voucher (`CD-XXXX`) — `RF-13`, `RF-15`, `CA-09`, `CA-11`
- **FRAME-10:** Portal do Cliente — Área "Minhas Reservas" e Cancelamento Voluntário — `RF-16`, `CA-12`

---

## 2. Tokens de Design (Design Tokens)

**Cores Semânticas:**
- `primary`: `#1A1A2E` (Azul escuro institucional)
- `cta`: `#E94560` (Vermelho destaque / ação principal)
- `neutralBg`: `#F5F5F5` (Plano de fundo secundário)
- `card`: `#FFFFFF` (Superfície de cartões e modais)
- `textMain`: `#2D2D2D` (Texto primário de alto contraste)
- `textSecondary`: `#6B7280` (Texto auxiliar e metadados)
- `seatAvailable`: `#22C55E` (Assento disponível — `AVAILABLE`)
- `seatSold`: `#EF4444` (Assento vendido — `SOLD`)
- `seatReserved`: `#F59E0B` (Assento reservado online — `RESERVED`)
- `seatSelected`: `#3B82F6` (Assento selecionado na operação atual)
- `seatBlocked`: `#9CA3AF` (Assento bloqueado — `BLOCKED`)

**Tipografia:**
- `heading`: `Inter Bold 24px`
- `subheading`: `Inter SemiBold 18px`
- `body`: `Inter Regular 14px`
- `caption`: `Inter Regular 12px`

**Escala de Espaçamento e Bordas:**
- `base`: `4px`
- `lg`: `24px`
- `radiusCard`: `6px`
- `radiusBadge`: `4px`

---

## 3. Protótipo HTML de Referência Visual

> Estrutura HTML/Tailwind de referência para validação visual dos componentes especificados.

```html
<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"/><title>CineDoom — Protótipos de Interface</title><script src="https://cdn.tailwindcss.com"></script></head><body class="bg-gray-100 text-sm font-sans text-gray-800 p-6 space-y-12">

<!-- FRAME 1: LOGIN -->
<section>
  <h2 class="text-xs uppercase tracking-widest text-gray-400 mb-3">FRAME-1 · Login</h2>
  <div class="max-w-sm mx-auto bg-white rounded-md shadow-sm p-8 space-y-5">
    <div class="text-center">
      <div class="text-2xl font-bold" style="color:#1A1A2E">CineDoom</div>
      <p class="text-xs text-gray-500 mt-1">Plataforma SaaS de Bilheteria e Gestão</p>
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
      <span class="flex items-center gap-1"><span class="w-3 h-3 rounded-sm inline-block" style="background:#F59E0B"></span>Reservado</span>
      <span class="flex items-center gap-1"><span class="w-3 h-3 rounded-sm inline-block" style="background:#3B82F6"></span>Selecionado</span>
      <span class="flex items-center gap-1"><span class="w-3 h-3 rounded-sm inline-block" style="background:#9CA3AF"></span>Bloqueado</span>
    </div>
    <!-- Grid assentos (2x10 simplificado) -->
    <div class="grid gap-1" style="grid-template-columns:repeat(10,2rem)">
      <div class="w-8 h-8 rounded-sm" style="background:#EF4444"></div>
      <div class="w-8 h-8 rounded-sm" style="background:#EF4444"></div>
      <div class="w-8 h-8 rounded-sm" style="background:#22C55E"></div>
      <div class="w-8 h-8 rounded-sm" style="background:#F59E0B"></div>
      <div class="w-8 h-8 rounded-sm" style="background:#3B82F6"></div>
      <div class="w-8 h-8 rounded-sm" style="background:#22C55E"></div>
      <div class="w-8 h-8 rounded-sm" style="background:#22C55E"></div>
      <div class="w-8 h-8 rounded-sm" style="background:#9CA3AF"></div>
      <div class="w-8 h-8 rounded-sm" style="background:#22C55E"></div>
      <div class="w-8 h-8 rounded-sm" style="background:#EF4444"></div>
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
        <span>Comprador consente com a coleta e uso dos dados conforme LGPD. <strong>Campo obrigatório (CA-06).</strong></span>
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
      <div class="font-semibold text-base" style="color:#1A1A2E">Ocupação do Dia — 05/11/2026</div>
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
          <td><div class="w-32 bg-gray-200 rounded h-2"><div class="h-2 rounded" style="width:73%;background:#E94560"></div></div><span class="text-xs ml-1">72.5%</span></td>
        </tr>
        <tr>
          <td class="py-2">Ainda Estou Aqui</td><td>Sala 1</td><td>15:00</td><td>45/80</td>
          <td><div class="w-32 bg-gray-200 rounded h-2"><div class="h-2 rounded" style="width:56%;background:#E94560"></div></div><span class="text-xs ml-1">56.3%</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<!-- FRAME 5: GESTÃO FILMES -->
<section>
  <h2 class="text-xs uppercase tracking-widest text-gray-400 mb-3">FRAME-5 · Gestão — Catálogo de Filmes</h2>
  <div class="bg-white rounded-md shadow-sm p-6 max-w-3xl mx-auto space-y-4">
    <div class="flex items-center justify-between">
      <div class="font-semibold text-base" style="color:#1A1A2E">Catálogo de Filmes</div>
      <button class="px-3 py-1.5 rounded text-white text-xs font-semibold" style="background:#E94560">+ Novo Filme</button>
    </div>
    <table class="w-full text-sm">
      <thead>
        <tr class="text-left text-xs text-gray-500 border-b">
          <th class="pb-2">Título</th><th class="pb-2">Diretor</th><th class="pb-2">Duração</th><th class="pb-2">Ações</th>
        </tr>
      </thead>
      <tbody class="divide-y">
        <tr><td class="py-2">Duna: Parte Dois</td><td>Denis Villeneuve</td><td>166 min</td><td class="space-x-2"><a class="text-blue-600 text-xs" href="#">Editar</a></td></tr>
        <tr><td class="py-2">Ainda Estou Aqui</td><td>Walter Salles</td><td>135 min</td><td class="space-x-2"><a class="text-blue-600 text-xs" href="#">Editar</a></td></tr>
      </tbody>
    </table>
  </div>
</section>

<!-- FRAME 6: GESTÃO SESSÕES -->
<section>
  <h2 class="text-xs uppercase tracking-widest text-gray-400 mb-3">FRAME-6 · Gestão — Salas e Sessões</h2>
  <div class="bg-white rounded-md shadow-sm p-6 max-w-3xl mx-auto space-y-4">
    <div class="flex items-center justify-between">
      <div class="font-semibold text-base" style="color:#1A1A2E">Sessões Programadas</div>
      <button class="px-3 py-1.5 rounded text-white text-xs font-semibold" style="background:#E94560">+ Nova Sessão</button>
    </div>
    <table class="w-full text-sm">
      <thead>
        <tr class="text-left text-xs text-gray-500 border-b">
          <th class="pb-2">Filme</th><th class="pb-2">Sala</th><th class="pb-2">Data/Hora</th><th class="pb-2">Ações</th>
        </tr>
      </thead>
      <tbody class="divide-y">
        <tr><td class="py-2">Duna: Parte Dois</td><td>Sala 2</td><td>05/11 19:30</td><td><a class="text-blue-600 text-xs" href="#">Editar</a></td></tr>
        <tr><td class="py-2">Ainda Estou Aqui</td><td>Sala 1</td><td>05/11 15:00</td><td><a class="text-blue-600 text-xs" href="#">Editar</a></td></tr>
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
        <p class="text-xs text-gray-400 mt-1">Apenas GERENTE pode criar usuários (RN-01 / CA-05).</p>
      </div>
    </div>
    <button class="w-full py-2 rounded text-white text-sm font-semibold" style="background:#E94560">Criar Conta</button>
  </div>
</section>

</body></html>
```
