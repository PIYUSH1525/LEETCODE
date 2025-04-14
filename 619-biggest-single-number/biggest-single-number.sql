WITH NumberCounts AS (
    SELECT
        num,
        COUNT(*) AS count
    FROM MyNumbers
    GROUP BY num
),
SingleNumbers AS (
    SELECT
        num
    FROM NumberCounts
    WHERE count = 1
)

SELECT
    MAX(num) AS num
FROM SingleNumbers;

