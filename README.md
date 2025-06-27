# CommitSentry

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3776AB?style=for-the-badge&logo=matplotlib&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-FA0F00?style=for-the-badge&logo=jupyter&logoColor=white)







---


## 📖 Sobre o Projeto

O CommitSentry é um projeto desenvolvido no contexto da disciplina de Reconhecimento de Padrões, com o objetivo de explorar técnicas de Machine Learning aplicadas à identificação de commits de risco. Esses commits representam alterações no código-fonte que apresentam alta probabilidade de introduzir defeitos no software.

O projeto visa responder questões como:

- Quais algoritmos oferecem maior acurácia na identificação de commits defeituosos? 
- Quais os atributos são os mais relevantes para o processo de predição?
- Quais técnicas oferecem melhor equilíbrio entre precisão e generalização?

---

## 🚀 Iniciando o projeto

Follow the steps below to run the project on your local machine.

1.  **Clone the repository:**
    ```bash
    git clone git clone --recurse-submodules https://github.com/Italo-Fernando/CommitSentry
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # Windows:
    .\venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
    ```
3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Go to raw folder then clone lucene repository:**
    ```bash
    cd data/raw
    ```
    ```
    git clone https://github.com/apache/lucene
    ```
5.  **Run** `main.py`.
---
