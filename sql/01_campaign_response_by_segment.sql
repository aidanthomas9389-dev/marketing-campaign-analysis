
SELECT
    Education,
    Marital_Status,
    COUNT(*) AS total_customers,
    SUM(AcceptedCmp1 + AcceptedCmp2 + AcceptedCmp3 +
        AcceptedCmp4 + AcceptedCmp5 + Response) AS total_acceptances,
    ROUND(
        CAST(SUM(AcceptedCmp1 + AcceptedCmp2 + AcceptedCmp3 +
             AcceptedCmp4 + AcceptedCmp5 + Response) AS REAL)
        / (COUNT(*) * 6), 3
    ) AS response_rate
FROM customers
GROUP BY Education, Marital_Status
HAVING COUNT(*) > 50
ORDER BY response_rate DESC;
