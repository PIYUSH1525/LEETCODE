WITH Quality AS (
    SELECT
        query_name,
        ROUND(AVG(rating * 1.0 / position), 2) AS quality
    FROM Queries
    GROUP BY query_name
),
PoorQueryPercentage AS (
    SELECT
        query_name,
        ROUND(
            COUNT(CASE WHEN rating < 3 THEN 1 END) * 100.0 / COUNT(*),
            2
        ) AS poor_query_percentage
    FROM Queries
    GROUP BY query_name
)

SELECT
    q.query_name,
    q.quality,
    p.poor_query_percentage
FROM Quality q
JOIN PoorQueryPercentage p
ON q.query_name = p.query_name;

