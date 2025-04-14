WITH ProductCount AS (
    SELECT COUNT(*) AS total_products FROM Product
),
CustomerProductCount AS (
    SELECT customer_id, COUNT(DISTINCT product_key) AS product_count
    FROM Customer
    GROUP BY customer_id
)
SELECT c.customer_id
FROM CustomerProductCount c
JOIN ProductCount p
ON c.product_count = p.total_products;