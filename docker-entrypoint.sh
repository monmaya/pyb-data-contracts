#!/bin/bash
set -e

# Création du répertoire data
mkdir -p data

# Génération des données
echo "Generating fake data..."
python scripts/generate_fake_data.py

# Démarrage du serveur Flask pour le Contract Registry
echo "Starting Flask server..."
python examples/contract_registry.py &

# Démarrage de Streamlit
echo "Starting Streamlit..."
streamlit run streamlit/app.py --server.port 8501 --server.address 0.0.0.0 