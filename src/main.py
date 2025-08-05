# src/main.py
from data_extraction.get_commits import extract_commit_data, identify_regular_expressions
from features.build_features import create_commit_table
from config import REQUIREMENTS_FILE_PATH,SZZ_INPUT_FILE, SZZ_BUGS_FILE, PARQUET_FILE
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

        else:
            print("Arquivo 'commits_labeled.parquet' já existe. Pulando a extração de dados dos commits.")
            commit_data = pd.read_parquet('data/processed/commits_labeled.parquet')
            print("Dados dos commits extraídos com sucesso.")
            """Criando o json de bugfixes"""
            if not pd.io.common.file_exists(SZZ_INPUT_FILE):
                print("Arquivo 'szz_output.json' não encontrado. Executando o SZZ para rotular os commits de bugfix.")
                identify_regular_expressions(commit_data)
                print("Expressões regulares identificadas com sucesso.")
            else:
                pass
            # Rodar o SZZ para rotular os commits de bugfix
            create_commit_table(PARQUET_FILE, 'data/processed/commits_labeled.csv', SZZ_BUGS_FILE)
            print("Tabela de commits criada com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro durante a execução do pipeline: {e}")
        return

if __name__ == "__main__":
    #main()
    create_commit_table(PARQUET_FILE, '../data/processed/dataset_labeled.parquet', SZZ_BUGS_FILE)
    #extract_commit_data()
    print("--- PIPELINE FINALIZADO ---")
