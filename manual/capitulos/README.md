# Capítulos Canônicos Modulares (manual/capitulos)

Este diretório armazena a **Fonte Canônica da Verdade (Single Source of Truth - SSOT)** de todo o conteúdo textual do Manual de Processos de Software.

O conteúdo é particionado em arquivos modulares numerados, correspondentes a cada capítulo exigido pela norma **ABNT NBR ISO/IEC/IEEE 12207:2021** e pela estrutura mínima da disciplina.

---

## Diretrizes de Contribuição para a Equipe

1. **Edição Exclusiva em `manual/capitulos/`:**
   * Nunca edite o arquivo consolidado `manual-processos-software.md` manualmente. Ele é um artefato derivado e sobregravado automaticamente pelo script de montagem.
2. **Branches Atômicas:**
   * Crie branches específicas por capítulo para evitar conflitos de merge entre os integrantes da equipe.
3. **Recompilação do Documento Unificado:**
   * Após editar qualquer capítulo, reconstrua o documento consolidado executando:
     ```bash
     ./scripts/montar-manual.sh
     ```
   * Ou compile a versão diagramada em LaTeX:
     ```bash
     ./scripts/compilar.sh
     ```
