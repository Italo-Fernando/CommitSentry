from pathlib import Path

# Diretório raiz do projeto
ROOT_DIR = Path(__file__).parent

CONFIG_FILE_PATH = ROOT_DIR / 'config.yml'

# Caminhos para as pastas de dados
DATA_DIR = ROOT_DIR / 'data'
RAW_DATA_DIR = DATA_DIR / 'raw'
PROCESSED_DATA_DIR = DATA_DIR / 'processed'
INTERIM_DATA_DIR = DATA_DIR / 'interim'

# Caminho para o repositório do Lucene
LUCENE_REPO_PATH = RAW_DATA_DIR / 'lucene'

# Caminhos para o PySZZ
PYSZZ_MODULE_PATH = ROOT_DIR / 'src' / 'external' / 'pyszz_v2'
PYSZZ_SCRIPT_PATH = PYSZZ_MODULE_PATH / 'main.py'
SZZ_OUTPUT_FILE = INTERIM_DATA_DIR / 'szz_output.json'

# Caminho para salvar modelos treinados
SAVED_MODELS_DIR = ROOT_DIR / 'models'