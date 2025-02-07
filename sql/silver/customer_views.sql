-- Vues spécifiques aux versions pour les consommateurs
CREATE VIEW v1_customer_view AS
SELECT  
    customer_id,
    v1_format.*
FROM customer_events
WHERE contract_version = '1.0'
AND processing_version = (
    SELECT max(processing_version)
    FROM customer_events
    WHERE contract_version = '1.0'
);

-- Vue de compatibilité v1 pour les données v2
CREATE VIEW v1_compatibility_view AS
SELECT  
    customer_id,
    v2_format.full_name as name,
    concat_ws(', ',  
        v2_format.address_components.street,
        v2_format.address_components.city
    ) as address,
    CASE v2_format.status
        WHEN 'ACTIVE' THEN 'A'
        WHEN 'INACTIVE' THEN 'I'
        WHEN 'PENDING' THEN 'P'
    END as status
FROM customer_events
WHERE contract_version = '2.0';

-- Vue unifiée pour la couche silver
CREATE VIEW silver.unified_customer_profile AS
SELECT  
    CASE contract_version
        WHEN '1.0' THEN extract_v1_address(raw_data)
        WHEN '2.0' THEN extract_v2_address(raw_data)
    END as normalized_address,
    -- Autres transformations spécifiques aux versions
FROM bronze.customer_profile; 