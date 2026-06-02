
WITH daily_totals AS (
    SELECT
        customer_id,
        event_date,
        SUM(event_count) AS daily_events
    FROM engagement_log
    GROUP BY customer_id, event_date
)
SELECT
    customer_id,
    event_date,
    daily_events,
    SUM(daily_events) OVER (
        PARTITION BY customer_id
        ORDER BY event_date
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS rolling_7day_engagement,
    RANK() OVER (
        PARTITION BY customer_id
        ORDER BY daily_events DESC
    ) AS daily_rank
FROM daily_totals
ORDER BY customer_id, event_date
LIMIT 50;
