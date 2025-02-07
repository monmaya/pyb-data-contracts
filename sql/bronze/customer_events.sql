-- Structure permettant le multiversioning des données
CREATE TABLE customer_events (
    event_id UUID,
    event_timestamp TIMESTAMP,
    customer_id STRING,
    -- Données spécifiques aux versions
    v1_format STRUCT<
        name: STRING,
        address: STRING,  -- Format combiné
        status: STRING    -- Codes courts (A, I, P)
    >,
    v2_format STRUCT<
        full_name: STRING,
        address_components: STRUCT<
            street: STRING,
            city: STRING,
            country: STRING
        >,
        status: STRING    -- Formats détaillés (ACTIVE, INACTIVE, PENDING)
    >,
    v3_format STRUCT<
        full_name: STRING,
        address_components: STRUCT<
            street: STRING,
            city: STRING,
            country: STRING,
            geo: STRUCT<lat: DOUBLE, lon: DOUBLE>
        >,
        status: STRING,
        preferences: ARRAY<STRING>
    >,
    -- Métadonnées de versioning
    contract_version STRING,
    processing_version STRING
)
PARTITIONED BY (contract_version); 