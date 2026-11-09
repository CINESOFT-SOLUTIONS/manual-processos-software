#!/usr/bin/env python3
# =============================================================================
# SYNC MANUAL MD TO LATEX
# Sincroniza os capítulos em Markdown (referência absoluta) para LaTeX
# =============================================================================

import os
import re
import subprocess
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MD_DIR = os.path.join(BASE_DIR, "manual", "capitulos")
TEX_DIR = os.path.join(BASE_DIR, "manual", "latex", "template", "capitulos")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

CHAPTERS = [
    {
        "num": "1",
        "file_md": "01-apresentacao-software.md",
        "file_tex": "01-apresentacao-software.tex",
        "title": "Apresentação do software",
    },
    {
        "num": "2",
        "file_md": "02-processos-acordo.md",
        "file_tex": "02-processos-acordo.tex",
        "title": "Processos de Acordo",
    },
    {
        "num": "3",
        "file_md": "03-processos-organizacionais.md",
        "file_tex": "03-processos-organizacionais.tex",
        "title": "Processos Organizacionais Habilitadores",
    },
    {
        "num": "4",
        "file_md": "04-gerenciamento-tecnico.md",
        "file_tex": "04-gerenciamento-tecnico.tex",
        "title": "Processos de Gerenciamento Técnico",
    },
    {
        "num": "5",
        "file_md": "05-processos-tecnicos.md",
        "file_tex": "05-processos-tecnicos.tex",
        "title": "Processos Técnicos",
    },
    {
        "num": "6",
        "file_md": "06-avaliacao-melhoria.md",
        "file_tex": "06-avaliacao-melhoria.tex",
        "title": "Avaliação e melhoria dos processos",
    },
]

MERMAID_FIGURES = {
    "c4": r"\figuracomfonte{capitulo-05/diagramas/c4-containers.pdf}{0.96\textwidth}{Diagrama C4 Nível 2: Contêineres da Plataforma CineDoom}{CineSoft Solutions (2026)}{fig:c4_containers}",
    "classdiagram": r"\figuracomfonte{capitulo-05/diagramas/diagrama-classes-dominio.pdf}{0.96\textwidth}{Diagrama de Classes do Domínio de Negócios CineDoom}{CineSoft Solutions (2026)}{fig:classes_dominio}",
    "sequencediagram": r"\figuracomfonte{capitulo-05/diagramas/diagrama-sequencia-reserva.pdf}{0.96\textwidth}{Diagrama de Sequência UML: Reserva Web e Emissão de Voucher}{CineSoft Solutions (2026)}{fig:sequencia_reserva}",
    "statediagram": r"\figuracomfonte{capitulo-05/diagramas/diagrama-estados-assento.pdf}{0.96\textwidth}{Diagrama de Máquina de Estados do Ciclo de Vida da Poltrona}{CineSoft Solutions (2026)}{fig:estados_assento}",
    "erdiagram": r"\figuracomfonte{capitulo-05/diagramas/diagrama-er-banco.pdf}{0.96\textwidth}{Diagrama Entidade-Relacionamento (DER) do Banco PostgreSQL}{CineSoft Solutions (2026)}{fig:der_banco}",
    "ciclo-de-vida": r"\figuracomfonte{capitulo-03/diagramas/diagrama-ciclo-de-vida.pdf}{0.95\textwidth}{Fluxo do Ciclo de Vida do Projeto CineDoom (Sprints Ágeis e Release)}{CineSoft Solutions (2026)}{fig:ciclo_vida}",
    "eap": r"\figuracomfonte{capitulo-04/diagramas/eap-projeto-3-niveis.pdf}{0.98\textwidth}{Estrutura Analítica do Projeto (EAP de 3 Níveis) do CineDoom}{CineSoft Solutions (2026)}{fig:eap_projeto}",
    "git": r"\figuracomfonte{capitulo-04/diagramas/fluxo-git-branches.pdf}{0.95\textwidth}{Fluxo de Ramificação e Promoção de Branches Git (GitFlow)}{CineSoft Solutions (2026)}{fig:fluxo_git}",
}

TABLE_INPUTS = [
    (r"\|[^\n]*Elemento do sistema[^\n]*\|[\s\S]*?(?=\n\n|\n#|$)", r"\n\n\\input{../../../assets/capitulo-02/tabelas/analise-make-or-buy.tex}\n\n"),
    (r"\|[^\n]*Elemento com potencial[^\n]*\|[\s\S]*?(?=\n\n|\n#|$)", r"\n\n\\input{../../../assets/capitulo-02/tabelas/perspectiva-fornecimento.tex}\n\n"),
    (r"\|[^\n]*Inventário de infraestrutura[^\n]*\|[\s\S]*?(?=\n\n|\n#|$)", r"\n\n\\input{../../../assets/capitulo-03/tabelas/inventario-ferramental.tex}\n\n"),
    (r"\|[^\n]*Macroatividade / Entregável[^\n]*\|[\s\S]*?(?=\n\n|\n#|$)", r"\n\n\\input{../../../assets/capitulo-03/tabelas/matriz-raci.tex}\n\n"),
    (r"\|[^\n]*Risco identificado[^\n]*\|[\s\S]*?(?=\n\n|\n#|$)", r"\n\n\\input{../../../assets/capitulo-04/tabelas/registro-riscos.tex}\n\n"),
    (r"\|[^\n]*Pugh Matrix[^\n]*\|[\s\S]*?(?=\n\n|\n#|$)", r"\n\n\\input{../../../assets/capitulo-04/tabelas/matriz-pugh-decisao.tex}\n\n"),
    (r"\|[^\n]*Catálogo Formal de Requisitos Funcionais[^\n]*\|[\s\S]*?(?=\n\n|\n#|$)", r"\n\n\\input{../../../assets/capitulo-05/tabelas/catalogo-requisitos.tex}\n\n"),
    (r"\|[^\n]*Matriz de Rastreabilidade Ponta a Ponta[^\n]*\|[\s\S]*?(?=\n\n|\n#|$)", r"\n\n\\input{../../../assets/capitulo-05/tabelas/matriz-rastreabilidade.tex}\n\n"),
    (r"\|[^\n]*Critérios de Aceitação Formais[^\n]*\|[\s\S]*?(?=\n\n|\n#|$)", r"\n\n\\input{../../../assets/capitulo-05/tabelas/criterios-aceitacao.tex}\n\n"),
    (r"\|[^\n]*Quadro Comparativo de Verificação vs\. Validação[^\n]*\|[\s\S]*?(?=\n\n|\n#|$)", r"\n\n\\input{../../../assets/capitulo-05/tabelas/verificacao-validacao.tex}\n\n"),
    (r"\|[^\n]*Pergunta de avaliação[^\n]*\|[\s\S]*?(?=\n\n|\n#|$)", r"\n\n\\input{../../../assets/capitulo-06/tabelas/diagnostico-processo.tex}\n\n"),
    (r"\|[^\n]*Campo do plano[^\n]*\|[\s\S]*?(?=\n\n|\n#|$)", r"\n\n\\input{../../../assets/capitulo-06/tabelas/plano-melhoria-pmp.tex}\n\n"),
]

def preprocess_markdown(text):
    # Substituir imagens markdown que apontam para caminhos relativos de prints por comandos oficiais
    # ex: ![Figura 1 – Portal...](../assets/prints/print-portal-cliente.png)
    def replace_md_image(match):
        caption = match.group(1)
        path = match.group(2)
        basename = os.path.basename(path)
        # Identificar capitulo pelo nome do arquivo
        if "portal" in basename or "bilheteria" in basename or "painel" in basename:
            cap = "capitulo-01"
            sub = "prints"
        elif "kanban" in basename or "metricas" in basename:
            cap = "capitulo-04"
            sub = "prints"
        elif "vitest" in basename:
            cap = "capitulo-05"
            sub = "prints"
        elif "evidencia" in basename:
            cap = "capitulo-06"
            sub = "prints"
        else:
            return ""
        return f"\n\n\\figuracomfonte{{{cap}/{sub}/{basename}}}{{0.92\\textwidth}}{{{caption}}}{{CineSoft Solutions (2026)}}{{fig:{basename.split('.')[0]}}}\n\n"

    text = re.sub(r"!\[(.*?)\]\((.*?)\)", replace_md_image, text)

    # Substituir blocos mermaid por comandos LaTeX de figura oficial
    def replace_mermaid(match):
        content = match.group(0).lower()
        for key, fig in MERMAID_FIGURES.items():
            if key in content:
                return f"\n\n{fig}\n\n"
        return ""

    text = re.sub(r"```mermaid[\s\S]*?```", replace_mermaid, text)

    # Injetar chamadas de tabelas centralizadas em assets
    for pat, rep in TABLE_INPUTS:
        text = re.sub(pat, rep, text, flags=re.IGNORECASE)

    # Sanitizar matemática simples no markdown antes do pandoc
    text = re.sub(r"\$([^$]+)\$", r"\1", text)
    text = text.replace(r"\le", "≤").replace(r"\ge", "≥").replace(r"\to", "→")
    text = text.replace(r"\times", "×")
    text = text.replace(r"\sum", "Σ")

    return text

def convert_chapter(ch):
    md_path = os.path.join(MD_DIR, ch["file_md"])
    tex_path = os.path.join(TEX_DIR, ch["file_tex"])

    if not os.path.exists(md_path):
        print(f"Aviso: {md_path} não encontrado.")
        return

    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    processed_md = preprocess_markdown(md_content)

    # Converter para LaTeX usando pandoc
    cmd = ["pandoc", "-f", "markdown", "-t", "latex", "--wrap=none"]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    tex_out, err = p.communicate(input=processed_md)

    if p.returncode != 0:
        print(f"Erro no pandoc para o capítulo {ch['num']}: {err}")
        return

    # Pós-processamento para adequar aos comandos editoriais e layout CineDoom
    lines = []
    lines.append(f"% =============================================================================")
    lines.append(f"% CAPÍTULO {ch['num']}: {ch['title'].upper()}")
    lines.append(f"% GERADO AUTOMATICAMENTE VIA scripts/sync-md-to-latex.py A PARTIR DO MD")
    lines.append(f"% =============================================================================\n")
    lines.append(f"\\aberturacapitulo{{Capítulo {ch['num']}}}{{{ch['title']}}}\n")

    in_header_1 = False
    for line in tex_out.splitlines():
        # Pular o primeiro título H1 que é a abertura
        if line.startswith(r"\section{Capítulo") or line.startswith(r"\section{") and not in_header_1:
            in_header_1 = True
            continue

        # Mapeamento semântico de seções (limpando \texorpdfstring e \label)
        if line.startswith(r"\section{"):
            # Extrair título puro
            t = re.sub(r"^\\section\{", "", line)
            t = re.sub(r"\\label\{[^}]+\}", "", t)
            t = re.sub(r"\\texorpdfstring\{([^}]+)\}\{[^}]*\}", r"\1", t)
            t = re.sub(r"\}\s*$", "", t).strip()
            t = re.sub(r"^\d+\.\d+\s*", "", t)
            lines.append(f"\n\\secao{{{t}}}")
            continue

        if line.startswith(r"\subsection{"):
            t = re.sub(r"^\\subsection\{", "", line)
            t = re.sub(r"\\label\{[^}]+\}", "", t)
            t = re.sub(r"\\texorpdfstring\{([^}]+)\}\{[^}]*\}", r"\1", t)
            t = re.sub(r"\}\s*$", "", t).strip()
            t = re.sub(r"^\d+\.\d+\.\d+\s*", "", t)
            lines.append(f"\n\\subsecao{{{t}}}")
            continue

        if line.startswith(r"\subsubsection{"):
            t = re.sub(r"^\\subsubsection\{", "", line)
            t = re.sub(r"\\label\{[^}]+\}", "", t)
            t = re.sub(r"\\texorpdfstring\{([^}]+)\}\{[^}]*\}", r"\1", t)
            t = re.sub(r"\}\s*$", "", t).strip()
            t = re.sub(r"^\d+\.\d+\.\d+\.\d+\s*", "", t)
            lines.append(f"\n\\subsubsecao{{{t}}}")
            continue

        if line.startswith(r"\paragraph{"):
            t = re.sub(r"^\\paragraph\{", "", line)
            t = re.sub(r"\\label\{[^}]+\}", "", t)
            t = re.sub(r"\\texorpdfstring\{([^}]+)\}\{[^}]*\}", r"\1", t)
            t = re.sub(r"\}\s*$", "", t).strip()
            lines.append(f"\n\\paragraph{{{t}}}")
            continue

        # Limpar labels automáticas desnecessárias do pandoc que possam causar colisão
        line = re.sub(r"\\label\{[^}]+\}", "", line)

        lines.append(line)

    final_tex = "\n".join(lines) + "\n"

    # Substituir blocos de longtable completos gerados pelo pandoc por tabularx limpo
    def clean_longtable(match):
        body = match.group(0)
        # remover comando inicial e final do longtable
        body = re.sub(r"^\\begin\{longtable\}\[\]\{[^}]*\}", "", body)
        body = re.sub(r"\\end\{longtable\}$", "", body)
        # remover linhas que contêm apenas chaves de fechamento ou sobras de definicao de colunas
        cleaned_lines = []
        for bl in body.splitlines():
            sbl = bl.strip()
            if sbl in ["}", "}}", "}@{}}", "@{}}"] or sbl.startswith(">") or "linewidth" in sbl or "tabcolsep" in sbl:
                continue
            cleaned_lines.append(bl)
        body = "\n".join(cleaned_lines)
        # remover \noalign{}
        body = body.replace(r"\noalign{}", "")
        # remover \begin{minipage} e \end{minipage} que o pandoc coloca nas celulas
        body = re.sub(r"\\begin\{minipage\}\[[^\]]*\]\{[^}]*\}", "", body)
        body = body.replace(r"\end{minipage}", "")
        # remover \endhead, \endfirsthead, etc.
        body = re.sub(r"\\endhead|\\endfirsthead|\\endfoot|\\endlastfoot", "", body)

        # Detectar número de colunas contando o número de '&' no corpo da tabela
        cols = 4
        for l in body.splitlines():
            # pegar linhas com dados válidos
            if "&" in l and not l.startswith(r"\toprule") and not l.startswith(r"\midrule") and not l.startswith(r"\bottomrule"):
                cols = max(cols, l.count("&") + 1)
        col_spec = " ".join(["X"] * cols)

        return f"\\begin{{center}}\\small\\begin{{tabularx}}{{\\textwidth}}{{{col_spec}}}\n{body}\n\\end{{tabularx}}\\end{{center}}"

    final_tex = re.sub(r"\\begin\{longtable\}\[\]\{[^}]*\}[\s\S]*?\\end\{longtable\}", clean_longtable, final_tex)
    # Remover chaves sobrantes de {\def\LTcaptype{none} ... }
    final_tex = re.sub(r"\{\\def\\LTcaptype\{none\}\s*%[^\n]*\n", "", final_tex)
    final_tex = re.sub(r"\\end\{tabularx\}\\end\{center\}\s*\}", r"\\end{tabularx}\\end{center}", final_tex)

    # Limpar qualquer delimitador de matemática do LaTeX mal formatado pelo pandoc
    final_tex = re.sub(r"\\\(", "", final_tex)
    final_tex = re.sub(r"\\\)", "", final_tex)
    final_tex = final_tex.replace(r"\text{h}", "h")
    final_tex = final_tex.replace(r"\text{min}", "min")

    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(final_tex)

    print(f"✓ Capítulo {ch['num']} sincronizado: {ch['file_md']} -> {ch['file_tex']} ({len(final_tex.splitlines())} linhas)")

def main():
    print("=== Sincronizando Markdown com LaTeX ===")
    for ch in CHAPTERS:
        convert_chapter(ch)
    print("=== Sincronização concluída com sucesso! ===")

if __name__ == "__main__":
    main()
