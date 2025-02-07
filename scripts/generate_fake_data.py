from faker import Faker
import pandas as pd
import duckdb
import datetime

fake = Faker()

def generate_customer_events(n_rows=100000):
    data = []
    for _ in range(n_rows):
        event = {
            'event_id': fake.uuid4(),
            'customer_id': fake.uuid4(),
            'event_timestamp': fake.date_time_between(
                start_date='-1y',
                end_date='now'
            ),
            'event_type': fake.random_element(['signup', 'update', 'purchase']),
            'v1_format': {
                'name': fake.name(),
                'address': fake.address(),
                'status': fake.random_element(['A', 'I', 'P'])
            },
            'v2_format': {
                'full_name': fake.name(),
                'address_components': {
                    'street': fake.street_address(),
                    'city': fake.city(),
                    'country': fake.country()
                },
                'status': fake.random_element(['ACTIVE', 'INACTIVE', 'PENDING'])
            }
        }
        data.append(event)
    return pd.DataFrame(data)

def init_database():
    # Utilisation d'un chemin absolu dans le conteneur
    con = duckdb.connect('/app/data/demo.db')
    
    # Création des schémas
    con.execute("CREATE SCHEMA IF NOT EXISTS bronze")
    con.execute("CREATE SCHEMA IF NOT EXISTS silver")
    con.execute("CREATE SCHEMA IF NOT EXISTS gold")
    
    # Génération et chargement des données
    df = generate_customer_events()
    
    # Création de la table bronze
    con.execute("""
    CREATE OR REPLACE TABLE bronze.customer_events AS 
    SELECT * FROM df
    """)
    
    # Création des vues silver
    con.execute("""
    CREATE OR REPLACE VIEW silver.customer_events_v1 AS
    SELECT 
        event_id,
        customer_id,
        event_timestamp,
        event_type,
        v1_format.name,
        v1_format.address,
        v1_format.status
    FROM bronze.customer_events
    """)
    
    con.execute("""
    CREATE OR REPLACE VIEW silver.customer_events_v2 AS
    SELECT 
        event_id,
        customer_id,
        event_timestamp,
        event_type,
        v2_format.full_name,
        v2_format.address_components.street,
        v2_format.address_components.city,
        v2_format.address_components.country,
        v2_format.status
    FROM bronze.customer_events
    """)
    
    # Création des vues gold
    con.execute("""
    CREATE OR REPLACE VIEW gold.customer_profile AS
    SELECT 
        customer_id,
        MAX(v2_format.full_name) as full_name,
        MAX(v2_format.status) as current_status,
        COUNT(*) as event_count,
        MIN(event_timestamp) as first_seen,
        MAX(event_timestamp) as last_seen
    FROM bronze.customer_events
    GROUP BY customer_id
    """)
    
    con.close()

if __name__ == "__main__":
    init_database() 