FROM python:3.9-slim

WORKDIR /app

# Installation des dépendances système
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Création du répertoire data
RUN mkdir -p /app/data

# Installation des dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie des fichiers du projet
COPY scripts/ scripts/
COPY sql/ sql/
COPY contracts/ contracts/
COPY validation/ validation/
COPY examples/ examples/

# Script de démarrage
COPY streamlit/ streamlit/
COPY docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh

# Exposition du port Streamlit
EXPOSE 8501
ENTRYPOINT ["./docker-entrypoint.sh"] 