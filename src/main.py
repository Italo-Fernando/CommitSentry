# src/main.py
from data_extraction.get_commits import extract_commit_data, identify_regular_expressions,ssz_label
from config import REQUIREMENTS_FILE_PATH,SZZ_INPUT_FILE
import subprocess


import pandas as pd

def main():
    try:
        # Verifica se o arquivo commits_labeled.parquet existe
        if not pd.io.common.file_exists('data/processed/commits_labeled.parquet'):
            print("Arquivo 'commits_labeled.parquet' não encontrado. Extraindo dados dos commits")
            """Executa o pipeline completo do projeto."""
            print("--- INICIANDO PIPELINE JIT DEFECT PREDICTION ---")
            
            # Extrai dados dos commits
            commit_data = extract_commit_data()
            

            # Identifica expressões regulares nos commits
            identify_regular_expressions(commit_data)
            print("Expressões regulares identificadas com sucesso.")

            #Rodar o SZZ para rotular os commits de bugfix
            szz_result = ssz_label()
        else:
            print("Arquivo 'commits_labeled.parquet' já existe. Pulando a extração de dados dos commits.")
            commit_data = pd.read_parquet('data/processed/commits_labeled.parquet')
            print("Dados dos commits extraídos com sucesso.")
            """Criando o json de bugfixes"""
            identify_regular_expressions(commit_data)
            print("Expressões regulares identificadas com sucesso.")
            # Rodar o SZZ para rotular os commits de bugfix
            szz_result = ssz_label(SZZ_INPUT_FILE)
    except Exception as e:
        print(f"Ocorreu um erro durante a execução do pipeline: {e}")
        return

if __name__ == "__main__":
    main()
    print("--- PIPELINE FINALIZADO ---")
