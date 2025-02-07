-- Bronze layer: Raw customer events ingestion
CREATE TABLE IF NOT EXISTS bronze.raw_customer_events (
    event_id UUID,
    customer_id UUID,
    event_type STRING,
    event_timestamp TIMESTAMP,
    event_data STRING, -- JSON format
    source_system STRING,
    ingestion_timestamp TIMESTAMP,
    contract_version STRING,
    _metadata STRUCT<
        source_file: STRING,
        batch_id: STRING,
        validation_status: STRING
    >
)
PARTITIONED BY (dt STRING)
STORED AS PARQUET
LOCATION '/data/bronze/customer_events';

-- Quality validation view
CREATE VIEW bronze.validated_customer_events AS
SELECT 
    *,
    CASE 
        WHEN event_id IS NULL THEN 'Missing event ID'
        WHEN customer_id IS NULL THEN 'Missing customer ID'
        WHEN event_timestamp IS NULL THEN 'Missing timestamp'
        ELSE 'VALID'
    END as validation_status
FROM bronze.raw_customer_events; 