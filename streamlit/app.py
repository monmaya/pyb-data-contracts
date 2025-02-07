import streamlit as st
import duckdb
import pandas as pd
import os

st.set_page_config(
    page_title="Data Contracts Demo",
    layout="wide"
)

@st.cache_resource
def get_connection():
    # Utilisation d'un chemin absolu dans le conteneur
    db_path = '/app/data/demo.db'
    return duckdb.connect(db_path)

def main():
    st.title("Data Contracts Framework Demo")
    
    # Sidebar pour la navigation
    page = st.sidebar.selectbox(
        "Select Layer",
        ["Bronze", "Silver", "Gold"]
    )
    
    con = get_connection()
    
    if page == "Bronze":
        st.header("Bronze Layer - Raw Data")
        
        # Affichage des données bronze
        df = con.execute("""
            SELECT * FROM bronze.customer_events 
            LIMIT 1000
        """).df()
        
        st.dataframe(df)
        
        # Métriques
        col1, col2, col3 = st.columns(3)
        with col1:
            count = con.execute("SELECT COUNT(*) FROM bronze.customer_events").fetchone()[0]
            st.metric("Total Events", f"{count:,}")
        with col2:
            customers = con.execute(
                "SELECT COUNT(DISTINCT customer_id) FROM bronze.customer_events"
            ).fetchone()[0]
            st.metric("Unique Customers", f"{customers:,}")
        with col3:
            event_types = con.execute(
                "SELECT COUNT(DISTINCT event_type) FROM bronze.customer_events"
            ).fetchone()[0]
            st.metric("Event Types", event_types)
            
    elif page == "Silver":
        st.header("Silver Layer - Normalized Views")
        
        version = st.selectbox("Select Version", ["V1", "V2"])
        
        if version == "V1":
            df = con.execute("""
                SELECT * FROM silver.customer_events_v1 
                LIMIT 1000
            """).df()
        else:
            df = con.execute("""
                SELECT * FROM silver.customer_events_v2 
                LIMIT 1000
            """).df()
            
        st.dataframe(df)
        
    else:  # Gold
        st.header("Gold Layer - Business Views")
        
        df = con.execute("""
            SELECT * FROM gold.customer_profile 
            LIMIT 1000
        """).df()
        
        st.dataframe(df)
        
        # Visualisations
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Status Distribution")
            status_df = con.execute("""
                SELECT current_status, COUNT(*) as count 
                FROM gold.customer_profile 
                GROUP BY current_status
            """).df()
            st.bar_chart(status_df.set_index('current_status'))
            
        with col2:
            st.subheader("Events per Customer")
            # Création d'un histogramme en utilisant des intervalles manuels
            events_dist = con.execute("""
                WITH stats AS (
                    SELECT 
                        MIN(event_count) as min_count,
                        MAX(event_count) as max_count
                    FROM gold.customer_profile
                ),
                ranges AS (
                    SELECT 
                        CASE 
                            WHEN event_count <= 5 THEN '1-5'
                            WHEN event_count <= 10 THEN '6-10'
                            WHEN event_count <= 20 THEN '11-20'
                            WHEN event_count <= 50 THEN '21-50'
                            ELSE '50+'
                        END as range
                    FROM gold.customer_profile
                )
                SELECT 
                    range,
                    COUNT(*) as count
                FROM ranges
                GROUP BY range
                ORDER BY 
                    CASE range
                        WHEN '1-5' THEN 1
                        WHEN '6-10' THEN 2
                        WHEN '11-20' THEN 3
                        WHEN '21-50' THEN 4
                        ELSE 5
                    END
            """).df()
            st.bar_chart(events_dist.set_index('range'))

if __name__ == "__main__":
    main() 