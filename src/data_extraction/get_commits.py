# src/data_extraction/get_commits.py
import pandas as pd
from pydriller import Repository
import json
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from config import LUCENE_REPO_PATH, SZZ_OUTPUT_FILE, PROCESSED_DATA_DIR


def extract_commit_data():
    """Extrai dados dos commits e os combina com os rótulos do SZZ."""
    print("Iniciando extração de dados dos commits com pydriller...")
        

    commit_list = []
    count = 0
    for commit in Repository(str(LUCENE_REPO_PATH)).traverse_commits():
            count += 1
            commit_list.append({
                'hash': commit.hash,
                'msg': commit.msg,
                'author': commit.author.name,
                'date': commit.author_date,
                'lines_added': commit.insertions,
                'lines_deleted': commit.deletions,
                'files_modified': len(commit.modified_files),
            })

            if count % 100 == 0:
                print(f"Processados {count} commits...")

    df = pd.DataFrame(commit_list)
    output_path = PROCESSED_DATA_DIR / 'commits_labeled.parquet'
    df.to_parquet(output_path, index=False)
    print(f"Dados dos commits extraídos e salvos em {output_path}")
    return df

def identify_regular_expressions(dataframe): # vai ler a 'msg' do dataframe e , com expressões regulares, identificar os padrões de commits e retornar um json com os shas
    """Identifica padrões de commits usando expressões regulares."""
    import re
    from collections import defaultdict

    patterns = {
        'bugfix': r'\b(fix|bug|issue|error)\b',
        'feature': r'\b(feature|add|new)\b',
        'refactor': r'\b(refactor|cleanup|optimize)\b',
        'documentation': r'\b(doc|docs|readme)\b',
    }

    identified_commits = defaultdict(list)

    for index, row in dataframe.iterrows():
        msg = row['msg'].lower()
        for key, pattern in patterns.items():
            if re.search(pattern, msg):
                identified_commits[key].append(row['hash'])

    # Convert defaultdict to a regular dict for JSON serialization
    identified_commits = {key: value for key, value in identified_commits.items() if value}
    # Save the identified commits to a JSON file
    with open(SZZ_OUTPUT_FILE, 'w') as f:
        json.dump(identified_commits, f, indent=4)
    print(f"Identified commits saved to {SZZ_OUTPUT_FILE}")

    return dict(identified_commits)

def main():
    """Executa a extração de dados dos commits e identificação de expressões regulares."""
    print("--- INICIANDO EXTRAÇÃO DE DADOS DOS COMMITS ---")
    
    # Extrai dados dos commits
    commit_data = extract_commit_data()
    print("Dados dos commits extraídos com sucesso.")

if __name__ == "__main__":
    main()