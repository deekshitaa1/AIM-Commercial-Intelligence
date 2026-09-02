CREATE TABLE IF NOT EXISTS prospects (
    prospect_id BIGINT PRIMARY KEY,
    industry VARCHAR(100),
    region VARCHAR(50),
    company_size VARCHAR(30),
    annual_revenue NUMERIC(18,2),
    employees INTEGER,
    years_in_business INTEGER,
    existing_relationship INTEGER,
    website_visits INTEGER,
    email_opens INTEGER,
    email_clicks INTEGER,
    sales_contacts INTEGER,
    previous_applications INTEGER,
    campaign VARCHAR(100),
    channel VARCHAR(100),
    days_since_last_interaction INTEGER,
    engagement_score NUMERIC(10,2),
    converted INTEGER,
    expected_revenue NUMERIC(18,2),
    acquisition_cost NUMERIC(18,2),
    expected_net_value NUMERIC(18,2),
    duplicate_application_flag INTEGER,
    velocity_flag INTEGER,
    gaming_risk_score INTEGER,
    high_value_target INTEGER,
    created_at DATE,
    engagement_rate NUMERIC(10,4),
    sales_intensity NUMERIC(10,4),
    revenue_per_employee NUMERIC(18,2),
    is_recent_interaction INTEGER,
    is_high_engagement INTEGER
);

CREATE INDEX IF NOT EXISTS idx_prospects_channel
ON prospects(channel);

CREATE INDEX IF NOT EXISTS idx_prospects_campaign
ON prospects(campaign);

CREATE INDEX IF NOT EXISTS idx_prospects_region
ON prospects(region);

CREATE INDEX IF NOT EXISTS idx_prospects_converted
ON prospects(converted);

CREATE INDEX IF NOT EXISTS idx_prospects_gaming
ON prospects(gaming_risk_score);
