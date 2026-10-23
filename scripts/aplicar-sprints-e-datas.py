#!/usr/bin/env python3
"""
scripts/aplicar-sprints-e-datas.py
--------------------------------------------------------------------------------
Aplica a divisão de trabalho da equipe (assignees) e as datas de início e
término (Start date e Target date) nas 30 issues do Kanban CineDoom.

Padrão de Saída:
  - Estilo minimalista, sem emojis.
  - Badges ANSI invertidos [OK], [EXEC], [INFO], [WARN].
--------------------------------------------------------------------------------
"""

import subprocess
import json
import sys
import os

START_DATE_FIELD_ID = "IFD_kgDOAulZJw"
TARGET_DATE_FIELD_ID = "IFD_kgDOAulZKA"

APP_DATA = {
    1: {"assignee": "gabrlou", "start": "2026-10-23", "target": "2026-10-25"},
    2: {"assignee": "gabrlou", "start": "2026-10-25", "target": "2026-10-27"},
    3: {"assignee": "gabrlou", "start": "2026-10-28", "target": "2026-10-30"},
    4: {"assignee": "gabrlou", "start": "2026-10-29", "target": "2026-11-01"},
    5: {"assignee": "carloseduduu", "start": "2026-10-29", "target": "2026-10-31"},
    6: {"assignee": "carloseduduu", "start": "2026-11-01", "target": "2026-11-03"},
    7: {"assignee": "carloseduduu", "start": "2026-11-01", "target": "2026-11-04"},
    8: {"assignee": "carloseduduu", "start": "2026-11-03", "target": "2026-11-05"},
    9: {"assignee": "gabrlou", "start": "2026-11-01", "target": "2026-11-03"},
    10: {"assignee": "gabrlou", "start": "2026-11-03", "target": "2026-11-06"},
    11: {"assignee": "gabrlou", "start": "2026-11-05", "target": "2026-11-07"},
    12: {"assignee": "gabrlou", "start": "2026-11-06", "target": "2026-11-08"},
    13: {"assignee": "carloseduduu", "start": "2026-11-05", "target": "2026-11-07"},
    14: {"assignee": "carloseduduu", "start": "2026-11-06", "target": "2026-11-08"},
    15: {"assignee": "carloseduduu", "start": "2026-10-24", "target": "2026-10-26"},
    16: {"assignee": "carloseduduu", "start": "2026-10-26", "target": "2026-10-28"},
    17: {"assignee": "gabrlou", "start": "2026-10-26", "target": "2026-10-29"},
    18: {"assignee": "gabrlou", "start": "2026-11-07", "target": "2026-11-09"},
    19: {"assignee": "gabrlou", "start": "2026-11-08", "target": "2026-11-10"},
    20: {"assignee": "carloseduduu", "start": "2026-11-08", "target": "2026-11-10"},
}

DOCS_DATA = {
    1: {"assignee": "YuryNog", "start": "2026-10-23", "target": "2026-10-26"},
    2: {"assignee": "YuryNog", "start": "2026-10-26", "target": "2026-10-29"},
    3: {"assignee": "K4yquee", "start": "2026-10-24", "target": "2026-10-28"},
    4: {"assignee": "K4yquee", "start": "2026-10-28", "target": "2026-11-01"},
    5: {"assignee": "YuryNog", "start": "2026-10-29", "target": "2026-11-02"},
    6: {"assignee": "YuryNog", "start": "2026-11-02", "target": "2026-11-05"},
    7: {"assignee": "YuryNog", "start": "2026-11-05", "target": "2026-11-08"},
    8: {"assignee": "K4yquee", "start": "2026-11-01", "target": "2026-11-05"},
    9: {"assignee": "K4yquee", "start": "2026-11-05", "target": "2026-11-09"},
    10: {"assignee": "K4yquee", "start": "2026-11-08", "target": "2026-11-11"},
}

def badge(text, color="7"):
    return f"\033[{color}m {text} \033[0m"

def run_cmd(cmd, check=True):
    res = subprocess.run(cmd, capture_output=True, text=True)
    if check and res.returncode != 0:
        print(f"{badge('ERRO', '41;97')} Falha ao executar: {' '.join(cmd)}\n{res.stderr.strip()}", file=sys.stderr)
        sys.exit(1)
    return res

def obter_node_ids():
    query = """
    query {
      app: repository(owner: "CINESOFT-SOLUTIONS", name: "cinedoom-app") {
        issues(first: 50) {
          nodes {
            number
            id
            title
          }
        }
      }
      docs: repository(owner: "CINESOFT-SOLUTIONS", name: "manual-processos-software") {
        issues(first: 50) {
          nodes {
            number
            id
            title
          }
        }
      }
    }
    """
    res = run_cmd(["gh", "api", "graphql", "-f", f"query={query}"])
    data = json.loads(res.stdout)
    app_ids = {node["number"]: node["id"] for node in data["data"]["app"]["issues"]["nodes"]}
    docs_ids = {node["number"]: node["id"] for node in data["data"]["docs"]["issues"]["nodes"]}
    return app_ids, docs_ids

def atribuir_issue(repo, number, assignee):
    run_cmd(["gh", "issue", "edit", str(number), "--repo", repo, "--add-assignee", assignee])

def atualizar_datas(node_id, start_date, target_date):
    mutation = f"""
    mutation {{
      setStart: updateIssueFieldValue(input: {{
        issueId: "{node_id}",
        issueField: {{
          fieldId: "{START_DATE_FIELD_ID}",
          dateValue: "{start_date}"
        }}
      }}) {{ clientMutationId }}
      setTarget: updateIssueFieldValue(input: {{
        issueId: "{node_id}",
        issueField: {{
          fieldId: "{TARGET_DATE_FIELD_ID}",
          dateValue: "{target_date}"
        }}
      }}) {{ clientMutationId }}
    }}
    """
    run_cmd(["gh", "api", "graphql", "-f", f"query={mutation}"])

def main():
    print(f"\n{badge('EXEC', '44;97')} Iniciando aplicacao de assignees e datas do roadmap...")
    
    print(f"{badge('INFO', '7')} Obtendo Node IDs das issues nos dois repositorios...")
    app_ids, docs_ids = obter_node_ids()
    print(f"{badge('OK', '42;97')} {len(app_ids)} issues encontradas em cinedoom-app, {len(docs_ids)} em manual-processos-software.\n")
    
    # 1. Trilha A: cinedoom-app
    print(f"--- [TRILHA A] cinedoom-app ({len(APP_DATA)} issues) ---")
    for num, meta in sorted(APP_DATA.items()):
        node_id = app_ids.get(num)
        if not node_id:
            print(f"{badge('WARN', '43;97')} Issue #{num} de cinedoom-app nao encontrada no GitHub.")
            continue
        
        assignee = meta["assignee"]
        start = meta["start"]
        target = meta["target"]
        
        print(f"[{num:02d}/20] cinedoom-app #{num} -> @{assignee} ({start} a {target})...", end=" ")
        atribuir_issue("CINESOFT-SOLUTIONS/cinedoom-app", num, assignee)
        atualizar_datas(node_id, start, target)
        print(f"{badge('OK', '42;97')}")

    print()
    # 2. Trilha B: manual-processos-software
    print(f"--- [TRILHA B] manual-processos-software ({len(DOCS_DATA)} issues) ---")
    for num, meta in sorted(DOCS_DATA.items()):
        node_id = docs_ids.get(num)
        if not node_id:
            print(f"{badge('WARN', '43;97')} Issue #{num} de manual-processos-software nao encontrada.")
            continue
        
        assignee = meta["assignee"]
        start = meta["start"]
        target = meta["target"]
        
        print(f"[{num:02d}/10] manual-processos-software #{num} -> @{assignee} ({start} a {target})...", end=" ")
        atribuir_issue("CINESOFT-SOLUTIONS/manual-processos-software", num, assignee)
        atualizar_datas(node_id, start, target)
        print(f"{badge('OK', '42;97')}")

    print(f"\n{badge('CONCLUIDO', '42;97')} Todas as 30 issues foram atribuidas e cronogramadas no Roadmap!")

if __name__ == "__main__":
    main()
