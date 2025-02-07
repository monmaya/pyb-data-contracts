-- Gold layer: Business-ready customer 360 view
CREATE VIEW gold.customer_360 AS

WITH customer_profile AS (
    SELECT *
    FROM silver.unified_customer_view
),

customer_activity AS (
    SELECT 
        customer_id,
        COUNT(DISTINCT CASE 
            WHEN event_type = 'login' 
            AND event_timestamp >= CURRENT_DATE - 30
            THEN DATE(event_timestamp)
        END) as login_days_last_30d,
        MAX(event_timestamp) as last_activity
    FROM silver.unified_customer_events
    GROUP BY 1
),

consent_status AS (
    SELECT 
        customer_id,
        MAX(CASE 
            WHEN preference_type = 'email' THEN consent_given
            ELSE FALSE
        END) as has_email_consent,
        MAX(CASE 
            WHEN preference_type = 'sms' THEN consent_given
            ELSE FALSE
        END) as has_sms_consent
    FROM silver.customer_consents
    WHERE is_active = true
    GROUP BY 1
)

SELECT 
    p.*,
    a.login_days_last_30d,
    a.last_activity,
    c.has_email_consent,
    c.has_sms_consent,
    -- Derived business metrics
    CASE 
        WHEN a.login_days_last_30d >= 20 THEN 'highly_active'
        WHEN a.login_days_last_30d >= 10 THEN 'active'
        WHEN a.login_days_last_30d >= 1 THEN 'occasional'
        ELSE 'inactive'
    END as engagement_level,
    -- GDPR compliance status
    CASE 
        WHEN p.email_status = 'verified' 
        AND c.has_email_consent = true THEN 'compliant'
        ELSE 'non_compliant'
    END as compliance_status
FROM customer_profile p
LEFT JOIN customer_activity a USING (customer_id)
LEFT JOIN consent_status c USING (customer_id); 