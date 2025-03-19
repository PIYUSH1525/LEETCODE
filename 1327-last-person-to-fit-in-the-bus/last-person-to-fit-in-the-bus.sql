WITH cte AS (
    SELECT person_name, 
           turn, 
           SUM(weight) OVER (ORDER BY turn) AS cumulative_weight
    FROM Queue
)
SELECT person_name
FROM cte
WHERE cumulative_weight <= 1000
ORDER BY turn DESC
LIMIT 1;
