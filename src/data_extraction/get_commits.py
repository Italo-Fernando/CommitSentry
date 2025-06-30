# src/data_extraction/get_commits.py
import pandas as pd
from pydriller import Repository
import json
import os
import sys
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from config import LUCENE_REPO_PATH, SZZ_OUTPUT_FILE, PROCESSED_DATA_DIR


def extract_commit_data():
    """Extrai dados dos commits """
    print("Iniciando extração de dados dos commits com pydriller...")
        

    commit_list = []
    author_experience = {}
    count = 0
    for commit in Repository(str(LUCENE_REPO_PATH)).traverse_commits():
        total_complexity = 0
        files_renamed = 0
        files_deleted = 0
        subsystems = set()
        count += 1
        for f in commit.modified_files:
            total_complexity += (f.complexity or 0)
            if f.change_type.name == 'RENAME':
                files_renamed += 1
            elif f.change_type.name == 'DELETE':
                files_deleted += 1
                
                
            if f.new_path:
                subsystems.add(str(Path(f.new_path).parent))
            elif f.old_path:
                subsystems.add(str(Path(f.old_path).parent))
            
        author_name = commit.author.name
        current_author_experience = author_experience.get(author_name, 0)
        author_experience[author_name] = current_author_experience + 1

        commit_list.append({
                'hash': commit.hash,
                'msg': commit.msg,
                'author': commit.author.name,
                'date': commit.author_date,
                'lines_added': commit.insertions,
                'lines_deleted': commit.deletions,
                'files_modified': len(commit.modified_files),
                'is_merge': commit.merge,
                'author_experience': current_author_experience,
                'commit_day' : commit.author_date.weekday(),
                'commit_hour' : commit.author_date.hour,
                'subsystems_modified': len(subsystems),
                'total_complexity': total_complexity,
                'ddm_unit_size' : commit.dmm_unit_size,
                'ddm_unit_count' : commit.dmm_unit_complexity,
                'ddm_unit_interfacing' : commit.dmm_unit_interfacing,
                
            })

        if count % 5000 == 0:
            print(f"Processados {count} commits...")

    df = pd.DataFrame(commit_list)
    output_path = PROCESSED_DATA_DIR / 'commits_labeled.parquet'
    df.to_parquet(output_path, index=False)
    print(f"Dados dos commits extraídos e salvos em {output_path}")
    return df

def identify_regular_expressions(dataframe):
    """Identifica padrões de commits relacionados a bugfixes e agrupa os demais."""
    import re
    from collections import defaultdict

    pattern = {
        'bugfix': r'\b(fix|bug|issue|error|fixed a bug|fixed)\b',
    }

    bugfix_commits = []
    repo_name = str(LUCENE_REPO_PATH).split(os.sep)[-1]

    for index, row in dataframe.iterrows():
        msg = row['msg'].lower()
        if re.search(pattern, msg):
            bugfix_commits.append({
                "fix_commit_hash": row['hash'],
                "repo_name": repo_name
            })

    # Salva apenas os commits de bugfix no JSON
    with open(SZZ_OUTPUT_FILE, 'w') as f:
        x = json.dump(bugfix_commits, f, indent=4)
    print(f"Bugfix commits saved to {SZZ_OUTPUT_FILE}")

    return x