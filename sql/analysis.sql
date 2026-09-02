-- ============================================================
-- AIM COMMERCIAL MARKETING INTELLIGENCE
-- BUSINESS ANALYSIS QUERIES
-- ============================================================

-- Overall acquisition performance
SELECT
    COUNT(*) AS prospects,
    SUM(converted) AS conversions,
    ROUND(100.0 * SUM(converted) / COUNT(*), 2) AS conversion_rate_pct,
    ROUND(SUM(expected_revenue), 2) AS total_revenue,
    ROUND(SUM(acquisition_cost), 2) AS total_acquisition_cost,
    ROUND(SUM(expected_net_value), 2) AS total_net_value
FROM prospects;


-- Channel performance
SELECT
    channel,
    COUNT(*) AS prospects,
    SUM(converted) AS conversions,
    ROUND(100.0 * SUM(converted) / COUNT(*), 2) AS conversion_rate_pct,
    ROUND(AVG(expected_net_value), 2) AS avg_net_value,
    ROUND(SUM(expected_net_value), 2) AS total_net_value
FROM prospects
GROUP BY channel
ORDER BY total_net_value DESC;


-- Campaign performance
SELECT
    campaign,
    COUNT(*) AS prospects,
    SUM(converted) AS conversions,
    ROUND(100.0 * SUM(converted) / COUNT(*), 2) AS conversion_rate_pct,
    ROUND(SUM(expected_net_value), 2) AS total_net_value
FROM prospects
GROUP BY campaign
ORDER BY total_net_value DESC;


-- Industry performance
SELECT
    industry,
    COUNT(*) AS prospects,
    SUM(converted) AS conversions,
    ROUND(100.0 * SUM(converted) / COUNT(*), 2) AS conversion_rate_pct,
    ROUND(AVG(expected_net_value), 2) AS avg_net_value
FROM prospects
GROUP BY industry
ORDER BY conversion_rate_pct DESC;


-- Region performance
SELECT
    region,
    COUNT(*) AS prospects,
    SUM(converted) AS conversions,
    ROUND(100.0 * SUM(converted) / COUNT(*), 2) AS conversion_rate_pct,
    ROUND(SUM(expected_net_value), 2) AS total_net_value
FROM prospects
GROUP BY region
ORDER BY total_net_value DESC;


-- Customer segment / company size
SELECT
    company_size,
    COUNT(*) AS prospects,
    SUM(converted) AS conversions,
    ROUND(100.0 * SUM(converted) / COUNT(*), 2) AS conversion_rate_pct,
    ROUND(AVG(annual_revenue), 2) AS avg_revenue,
    ROUND(AVG(expected_net_value), 2) AS avg_net_value
FROM prospects
GROUP BY company_size
ORDER BY avg_net_value DESC;


-- Gaming / anomaly exposure
SELECT
    gaming_risk_score,
    COUNT(*) AS records,
    SUM(duplicate_application_flag) AS duplicate_flags,
    SUM(velocity_flag) AS velocity_flags
FROM prospects
GROUP BY gaming_risk_score
ORDER BY gaming_risk_score DESC;


-- High-value target pool
SELECT
    COUNT(*) AS high_value_targets,
    SUM(converted) AS conversions,
    ROUND(AVG(annual_revenue), 2) AS avg_revenue,
    ROUND(AVG(expected_net_value), 2) AS avg_net_value
FROM prospects
WHERE high_value_target = 1;


-- Best campaign/channel combinations
SELECT
    campaign,
    channel,
    COUNT(*) AS prospects,
    SUM(converted) AS conversions,
    ROUND(100.0 * SUM(converted) / COUNT(*), 2) AS conversion_rate_pct,
    ROUND(SUM(expected_net_value), 2) AS total_net_value
FROM prospects
GROUP BY campaign, channel
HAVING COUNT(*) >= 100
ORDER BY total_net_value DESC;
