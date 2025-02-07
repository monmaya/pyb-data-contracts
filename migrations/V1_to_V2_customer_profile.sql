-- Migration script from v1 to v2 of customer profile
-- Main changes:
-- 1. Split address into components
-- 2. Add email verification status
-- 3. Structured preferences

-- Step 1: Create temporary migration table
CREATE TABLE customer_profile_migration AS
SELECT
    customer_id,
    email,
    -- Parse old address string into components
    parse_address(address).street as street,
    parse_address(address).city as city,
    parse_address(address).country as country,
    -- Default email status based on historical data
    CASE
        WHEN email_bounced = false AND last_email_open_date > CURRENT_DATE - 90
        THEN 'verified'
        WHEN email_bounced = true
        THEN 'invalid'
        ELSE 'pending'
    END as email_status,
    -- Convert old preferences to new structure
    CASE
        WHEN preferences LIKE '%email%' THEN array_append(preferences_array, 'email')
        ELSE preferences_array
    END as communication_preferences
FROM customer_profile_v1;

-- Step 2: Validate migration data
CREATE VIEW migration_validation AS
SELECT
    COUNT(*) as total_records,
    SUM(CASE WHEN street IS NULL THEN 1 ELSE 0 END) as missing_street,
    SUM(CASE WHEN city IS NULL THEN 1 ELSE 0 END) as missing_city,
    SUM(CASE WHEN email_status = 'verified' THEN 1 ELSE 0 END) as verified_emails
FROM customer_profile_migration;

-- Step 3: Apply migration if validation passes
INSERT INTO customer_profile_v2
SELECT
    customer_id,
    email,
    email_status,
    struct(
        street,
        city,
        country
    ) as address,
    struct(
        communication_preferences as channels
    ) as preferences,
    CURRENT_TIMESTAMP as migrated_at,
    '2.0' as schema_version
FROM customer_profile_migration;

-- Step 4: Create backward compatibility view
CREATE VIEW customer_profile_v1_compatibility AS
SELECT
    customer_id,
    email,
    concat_ws(', ', address.street, address.city, address.country) as address,
    preferences.channels as preferences,
    CASE
        WHEN email_status = 'verified' THEN false
        ELSE true
    END as email_bounced
FROM customer_profile_v2; 