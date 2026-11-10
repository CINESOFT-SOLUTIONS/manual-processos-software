# Prints recomendados — Capítulo 1 (Apresentação do Software)

Esta pasta concentra os registros visuais do sistema em operação. Os três artefatos abaixo são **recomendados** pela diretriz do Capítulo 1 e estão catalogados no Mapa de Artefatos e Evidências (ART-004, ART-005 e ART-006).

| ID | Arquivo | Conteúdo esperado | Status |
|---|---|---|---|
| ART-004 | `print-portal-cliente.png` | Catálogo de filmes em cartaz e mapa interativo de seleção de assentos do Portal do Cliente | Placeholder criado — substituir pelo print real |
| ART-005 | `print-bilheteria-atendente.png` | Tela do guichê físico de venda de ingressos e/ou baixa de reservas pelo atendente | Placeholder criado — substituir pelo print real |
| ART-006 | `print-painel-gerencial.png` | Tela de administração com sessões agendadas ou indicadores de ocupação das salas | Placeholder criado — substituir pelo print real |

> **Situação atual:** os três arquivos PNG existem apenas como placeholders provisórios, já referenciados no corpo do Capítulo 1. Para concluir a evidência, basta substituir cada arquivo pelo screenshot real, mantendo exatamente o mesmo nome e caminho.

## Roteiro de captura

1. Executar o seed e subir a aplicação:
   ```bash
   pnpm prisma db seed
   pnpm dev
   ```
2. Capturar o Portal do Cliente:
   - `/portal` — catálogo de filmes em cartaz;
   - `/portal/sessoes/<id-da-sessao>` — mapa interativo de assentos.
   - Se necessário, montar as duas telas em um único arquivo `print-portal-cliente.png`.
3. Capturar a Bilheteria:
   - `/bilheteria` — venda direta de ingressos;
   - `/bilheteria/baixa-reserva` — localização e confirmação de reserva web.
4. Capturar o Painel Gerencial:
   - `/backoffice` — visão geral dos módulos administrativos; ou
   - `/backoffice/sessoes` — programação e sessões agendadas.
5. Salvar em PNG de alta resolução (preferencialmente 300 DPI) e manter os nomes de arquivo exatamente como indicado na tabela.

## Observações

- As três figuras já estão inseridas no corpo do Capítulo 1; os arquivos atuais são placeholders e devem ser substituídos pelos screenshots reais.
- Os logotipos oficiais já estão disponíveis em `assets/logos/`.
- Em ambiente sem banco de dados configurado, o Portal do Cliente pode exibir dados de demonstração; para os prints de bilheteria e back-office, é necessário executar o seed.
