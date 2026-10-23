# Ativos Visuais e Diagramas (assets)

Esta pasta centraliza os diagramas, modelos visuais de processo e esquemas arquiteturais utilizados no Manual de Processos de Software e na documentação técnica do sistema **CineDoom**.

As identidades visuais internas do tema de apresentação de slides da universidade residem de forma autocontida em `latex/presentation/lib/`.

---

## Estrutura de Diretórios

* **`diagrams/`:** Diagramas arquiteturais (C4 Model: Contexto, Contêineres e Componentes), fluxos de processo (BPMN), diagramas de sequência de transação atômica e modelos de entidade-relacionamento.

---

## Padrão de Arquivos e Resolução

* **Exportações Vetoriais:** Arquivos `.svg` e `.pdf` (recomendados para inclusão no LaTeX sem distorção).
* **Imagens Raster:** Arquivos `.png` em alta resolução (300 DPI) com canal alfa (fundo transparente).
* **Fontes Editáveis:** Textos-fonte em PlantUML (`.puml`) ou Mermaid (`.mmd`) podem ser armazenados diretamente junto aos diagramas ou incorporados nos documentos Markdown.
