import subprocess
import pandas as pd
from pydriller import Repository
import re
import json
import os
import sys
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from config import LUCENE_REPO_PATH, SZZ_INPUT_FILE, PROCESSED_DATA_DIR, CONFIG_FILE_PATH, SUBMODULES_DIR, PYSZZ_SCRIPT_PATH, SUBMODULE_VENV_PATH, SZZ_BUGS_FILE


def bugs_to_list(bugs_file):
    """ Converts a JSON file containing bugs to a list using 'inducing_commit_hash' as reference."""
    with open(bugs_file, 'r') as file:
        bugs_data = json.load(file)
    
    bugs_list = []
    for bug in bugs_data:
        inducing_commit_hash = bug.get('inducing_commit_hash')
        if inducing_commit_hash:
            bugs_list.append(inducing_commit_hash)
    
    return bugs_list

def create_bug_feature(file_parquet, bugs_file):
    """ Creates a feature indicating whether a commit is a bug fix or not."""
    bugs_list = bugs_to_list(bugs_file)
    
    df = pd.read_parquet(file_parquet)
    df['is_bug'] = df['hash'].apply(lambda x: 1 if x in bugs_list else 0)
    
    return df

def transform_parquet_to_csv(df, output_csv):
    """Salva o DataFrame em um arquivo CSV"""
    df.to_csv(output_csv, index=False)
    print(f"Arquivo convertido para CSV: {output_csv}")


def create_commit_table(file_parquet, output_csv, bugs_file):
    df = create_bug_feature(file_parquet, bugs_file)
    transform_parquet_to_csv(df, output_csv)
