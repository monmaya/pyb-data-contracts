-- Détection des versions approchant de leur fin de support
CREATE VIEW version_sunset_alerts AS
WITH version_usage AS (
    SELECT  
        contract_version,
        end_of_support_date,
        array_agg(DISTINCT consumer_system) as affected_systems,
        count(DISTINCT event_id) as daily_events
    FROM contract_registry r
    JOIN usage_metrics u USING (contract_version)
    WHERE u.event_date >= current_date - interval '7 days'
    GROUP BY 1, 2
)
SELECT  
    contract_version,
    end_of_support_date,
    affected_systems,
    daily_events,
    date_diff('day', current_date, end_of_support_date) as days_until_sunset,
    CASE  
        WHEN end_of_support_date < current_date + interval '30 days' THEN 'CRITICAL'
        WHEN end_of_support_date < current_date + interval '90 days' THEN 'WARNING'
        ELSE 'INFO'
    END as alert_level
FROM version_usage
WHERE end_of_support_date IS NOT NULL;

-- Monitoring de l'utilisation des versions
CREATE VIEW version_usage_metrics AS
SELECT  
    contract_version,
    date_trunc('hour', event_timestamp) as hour,
    count(*) as event_count,
    count(DISTINCT customer_id) as unique_customers,
    count(DISTINCT consumer_system) as unique_consumers,
    avg(processing_latency) as avg_latency
FROM customer_events
WHERE event_timestamp >= current_date - interval '7 days'
GROUP BY 1, 2; 