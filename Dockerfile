# Dockerfile
FROM python:3.10-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Instalar dependências do sistema, se necessário (ex: git)
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copiar o arquivo de dependências e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o código fonte e configurações para o diretório de trabalho
COPY . .

# Inicializar o submódulo dentro do container
RUN git submodule update --init --recursive

# Comando padrão para executar quando o container iniciar
CMD ["python", "src/main.py"]