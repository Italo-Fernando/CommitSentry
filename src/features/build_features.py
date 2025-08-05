import json
import pandas as pd
from pathlib import Path
from typing import Set

def bugs_to_list(bugs_file: str) -> Set[str]:
    """
    Load a JSON file of bugs and return a set of inducing_commit_hash strings.
    Handles both single-string and list-of-strings cases.
    """
    with open(bugs_file, 'r', encoding='utf-8') as f:
        bugs_data = json.load(f)

    bug_hashes: Set[str] = set()
    for bug in bugs_data:
        ref = bug.get('inducing_commit_hash')
        if not ref:
            continue
        if isinstance(ref, list):
            for h in ref:
                if isinstance(h, str):
                    bug_hashes.add(h)
        elif isinstance(ref, str):
            bug_hashes.add(ref)
        else:
            continue
    return bug_hashes

def create_bug_feature(file_parquet: str, bugs_file: str) -> pd.DataFrame:
    """
    Read commits from a Parquet file, add a boolean 'is_bug' column,
    and return the enriched DataFrame.
    """
    bug_hashes = bugs_to_list(bugs_file)
    df = pd.read_parquet(file_parquet)
    df['is_bug'] = df['hash'].isin(bug_hashes)  
    return df

def save_dataframe(df: pd.DataFrame, output_path: str) -> None:
    """
    Save DataFrame to disk. Chooses format based on file extension.
    """
    ext = Path(output_path).suffix.lower()
    if ext == '.csv':
        df.to_csv(output_path, index=False)
    elif ext in ('.parquet', '.pq'):
        df.to_parquet(output_path, index=False)
    else:
        raise ValueError(f"Unsupported extension: {ext}")
    print(f"Saved DataFrame to {output_path}")

def create_commit_table(
    file_parquet: str,
    output_path: str,
    bugs_file: str
) -> None:
    df = create_bug_feature(file_parquet, bugs_file)
    save_dataframe(df, output_path)
