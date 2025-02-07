# Data Contracts Framework

A comprehensive framework for implementing data contracts in a modern data architecture.

## 📚 Documentation

Documentation is available in both English and French:

### English
1. [Fundamentals of Data Contracts](docs/en/articles/01-fundamentals.md)
2. [Structure and Content](docs/en/articles/02-structure-and-content.md)
3. [Workflow and Versioning](docs/en/articles/03-workflow-and-versioning.md)
4. [Architecture Patterns](docs/en/articles/04-architecture-patterns.md)
5. [Implementation](docs/en/articles/05-implementation.md)
6. [Governance and Adoption](docs/en/articles/06-governance-and-adoption.md)

### Français
1. [Fondamentaux des Data Contracts](docs/fr/articles/01-fondamentaux.md)
2. [Structure et Contenu](docs/fr/articles/02-structure-et-contenu.md)
3. [Workflow et Versioning](docs/fr/articles/03-workflow-et-versioning.md)
4. [Patterns d'Architecture](docs/fr/articles/04-patterns-architecture.md)
5. [Mise en Œuvre Pratique](docs/fr/articles/05-mise-en-oeuvre.md)
6. [Gouvernance et Adoption](docs/fr/articles/06-gouvernance-et-adoption.md)

## 🏗️ Structure du Projet

```
data-contracts-framework/
├── contracts/                    # Définitions des data contracts
│   ├── customer-domain/         # Contracts liés au domaine client
│   ├── templates/              # Templates de contracts
│   └── shared/                 # Types et définitions partagés
├── sql/                        # Implémentations SQL
│   ├── bronze/                # Couche d'ingestion
│   ├── silver/                # Couche de transformation
│   ├── gold/                  # Couche business
│   └── monitoring/            # Vues de monitoring
├── governance/                 # Outils de gouvernance
│   ├── workflow.py            # Gestion des workflows
│   └── coe_config.yaml        # Configuration du CoE
├── scripts/                    # Scripts utilitaires
│   └── generate_sample_data.py # Générateur de données
├── validation/                 # Tests et validations
│   ├── contract_tests.py      # Tests des contracts
│   └── version_migration.py   # Gestion des migrations
└── docs/                      # Documentation
    └── articles/              # Articles détaillés
```

## 🚀 Quick Start / Démarrage Rapide

### Docker Demo / Démo Docker

The easiest way to try out the framework is to use the Docker demo / La façon la plus simple d'essayer le framework est d'utiliser la démo Docker :

```bash
# Build the image / Construction de l'image
docker build -t data-contracts-demo .

# Run the container / Lancement du conteneur
docker run -p 8501:8501 data-contracts-demo
```

Then open / Puis ouvrez : http://localhost:8501

The demo includes / La démo inclut :
- 100,000 generated customer events / 100 000 événements clients générés
- Medallion architecture implementation / Implémentation de l'architecture médaillon
  - Bronze layer: raw events / Couche bronze : événements bruts
  - Silver layer: normalized views (V1 & V2) / Couche silver : vues normalisées (V1 & V2)
  - Gold layer: business views / Couche gold : vues métier
- Interactive Streamlit dashboard / Tableau de bord Streamlit interactif
  - Data exploration / Exploration des données
  - Version comparison / Comparaison des versions
  - Metrics & visualizations / Métriques & visualisations

### Manual Installation / Installation Manuelle

1. Installation:
```bash
git clone https://github.com/pybonnefoy/data-contracts-framework.git
cd data-contracts-framework
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

2. Generate test data:
```bash
python scripts/generate_sample_data.py
```

3. Explore contract examples in `contracts/`

4. Read the documentation:
   - Start with [Fundamentals](docs/en/articles/01-fundamentals.md)
   - Check implementation examples in `contracts/` and `sql/`
   - Follow the tutorials in the documentation

## 👥 Governance / Gouvernance

### English
The framework includes a complete governance structure:

- Defined roles and responsibilities
- Validation workflows
- Tracking metrics
- Training program

See [Governance and Adoption](docs/en/articles/06-governance-and-adoption.md) for details.

### Français
Le framework inclut une structure de gouvernance complète :

- Rôles et responsabilités définis
- Workflows de validation
- Métriques de suivi
- Programme de formation

Consultez [Gouvernance et Adoption](docs/fr/articles/06-gouvernance-et-adoption.md) pour plus de détails.

## 🛠️ Testing / Tests

```bash
# Run tests / Exécuter les tests
python -m pytest validation/

# Check contract compatibility / Vérifier la compatibilité des contracts
python validation/version_migration.py check
```

## 📊 Monitoring

### English
The framework includes SQL views for monitoring:
- Contract usage
- Data quality
- Performance metrics
- Versioning alerts

### Français
Le framework inclut des vues SQL pour le monitoring :
- Utilisation des contracts
- Qualité des données
- Métriques de performance
- Alertes de versioning

## 👤 Author / Auteur

Pierre-Yves Bonnefoy - Olexya