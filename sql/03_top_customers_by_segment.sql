
WITH customer_spend AS (
    SELECT
        ID,
        Education,
        Marital_Status,
        Income,
        MntWines + MntFruits + MntMeatProducts +
        MntFishProducts + MntSweetProducts + MntGoldProds AS total_spend
    FROM customers
),
ranked AS (
    SELECT
        ID,
        Education,
        Marital_Status,
        Income,
        total_spend,
        RANK() OVER (
            PARTITION BY Education
            ORDER BY total_spend DESC
        ) AS rank_in_segment
    FROM customer_spend
)
SELECT *
FROM ranked
WHERE rank_in_segment <= 5
ORDER BY Education, rank_in_segment;
