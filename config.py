from pathlib import Path

# Diretório raiz do projeto
ROOT_DIR = Path(__file__).parent

CONFIG_FILE_PATH = ROOT_DIR / 'config.yml'
REQUIREMENTS_FILE_PATH = ROOT_DIR / 'requirements.txt'
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
SZZ_INPUT_FILE = INTERIM_DATA_DIR / 'szz_output.json'


# Caminho para salvar modelos treinados
SAVED_MODELS_DIR = ROOT_DIR / 'models'

# Caminho para os diretorios dos submodulos
SUBMODULES_DIR = PYSZZ_MODULE_PATH / 'requirements.txt'
# Caminho para o ambiente virtual do submódulo
SUBMODULE_VENV_PATH = PYSZZ_MODULE_PATH / 'venv_submodule/bin/python'