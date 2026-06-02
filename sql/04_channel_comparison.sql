
SELECT
    Education,
    ROUND(AVG(NumWebPurchases), 2) AS avg_web_purchases,
    ROUND(AVG(NumCatalogPurchases), 2) AS avg_catalog_purchases,
    ROUND(AVG(NumStorePurchases), 2) AS avg_store_purchases,
    ROUND(AVG(NumWebPurchases) * 100.0 /
        NULLIF(AVG(NumWebPurchases) + AVG(NumCatalogPurchases) +
               AVG(NumStorePurchases), 0), 1) AS web_pct,
    ROUND(AVG(NumCatalogPurchases) * 100.0 /
        NULLIF(AVG(NumWebPurchases) + AVG(NumCatalogPurchases) +
               AVG(NumStorePurchases), 0), 1) AS catalog_pct,
    ROUND(AVG(NumStorePurchases) * 100.0 /
        NULLIF(AVG(NumWebPurchases) + AVG(NumCatalogPurchases) +
               AVG(NumStorePurchases), 0), 1) AS store_pct,
    COUNT(*) AS total_customers
FROM customers
GROUP BY Education
ORDER BY avg_web_purchases DESC;
