-- Silver layer: Unified customer view with schema evolution handling
CREATE VIEW silver.unified_customer_view AS

WITH latest_profile AS (
    SELECT 
        customer_id,
        contract_version,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id 
            ORDER BY event_timestamp DESC
        ) as rn,
        -- Version-specific transformations
        CASE contract_version
            WHEN '1.0' THEN parse_v1_profile(profile_data)
            WHEN '2.0' THEN parse_v2_profile(profile_data)
            WHEN '3.0' THEN parse_v3_profile(profile_data)
        END as normalized_profile
    FROM bronze.raw_customer_events
    WHERE event_type = 'profile_update'
)

SELECT 
    customer_id,
    normalized_profile.email,
    normalized_profile.email_status,
    normalized_profile.address,
    normalized_profile.preferences,
    -- Quality metrics
    CASE 
        WHEN normalized_profile.email_status = 'verified' THEN 1
        ELSE 0
    END as is_email_verified,
    -- Metadata
    contract_version,
    CURRENT_TIMESTAMP() as processed_timestamp
FROM latest_profile
WHERE rn = 1;

-- Quality monitoring view
CREATE VIEW silver.customer_quality_metrics AS
SELECT
    DATE_TRUNC('hour', processed_timestamp) as metric_hour,
    COUNT(*) as total_profiles,
    SUM(is_email_verified) as verified_emails,
    AVG(is_email_verified) as email_verification_rate
FROM silver.unified_customer_view
GROUP BY 1; 