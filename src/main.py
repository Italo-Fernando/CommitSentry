# src/main.py
from data_extraction.get_commits import extract_commit_data, identify_regular_expressions

import pandas as pd

def main():
    """Executa o pipeline completo do projeto."""
    print("--- INICIANDO PIPELINE JIT DEFECT PREDICTION ---")
    
    # Extrai dados dos commits
    commit_data = extract_commit_data()
    

    # Identifica expressões regulares nos commits
    identified_commits = identify_regular_expressions(commit_data)
    print("Expressões regulares identificadas com sucesso.")

if __name__ == "__main__":
    main()
    print("--- PIPELINE FINALIZADO ---")
