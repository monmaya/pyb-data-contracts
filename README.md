# Data Contracts Framework

Un framework complet pour implémenter des data contracts dans une architecture moderne de données.

## 📚 Documentation

Une série complète d'articles détaillant l'approche :

1. [Fondamentaux des Data Contracts](docs/articles/01-fondamentaux.md)
2. [Structure et Contenu](docs/articles/02-structure-et-contenu.md)
3. [Workflow et Versioning](docs/articles/03-workflow-et-versioning.md)
4. [Patterns d'Architecture](docs/articles/04-patterns-architecture.md)
5. [Mise en Œuvre Pratique](docs/articles/05-mise-en-oeuvre.md)
6. [Gouvernance et Adoption](docs/articles/06-gouvernance-et-adoption.md)

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

## 🚀 Démarrage Rapide

1. Installation :
```bash
git clone https://github.com/pybonnefoy/data-contracts-framework.git
cd data-contracts-framework
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sous Windows
pip install -r requirements.txt
```

2. Générez des données de test :
```bash
python scripts/generate_sample_data.py
```

3. Explorez les exemples de contracts dans `contracts/`

## 👥 Gouvernance

Le framework inclut une structure de gouvernance complète :

- Rôles et responsabilités définis
- Workflows de validation
- Métriques de suivi
- Programme de formation

Consultez [Gouvernance et Adoption](docs/articles/06-gouvernance-et-adoption.md) pour plus de détails.

## 🛠️ Tests et Validation

```bash
# Exécuter les tests
python -m pytest validation/

# Vérifier la compatibilité des contracts
python validation/version_migration.py check
```

## 📊 Monitoring

Le framework inclut des vues SQL pour le monitoring :
- Utilisation des contracts
- Qualité des données
- Métriques de performance
- Alertes de versioning

## 👤 Auteur

Pierre-Yves Bonnefoy

## 📝 License

MIT License - voir le fichier [LICENSE](LICENSE) pour plus de détails. 