# Write your MySQL query statement below
SELECT p.product_id AS product_id, p.product_name AS product_name
FROM Product p
WHERE p.product_id IN (
    SELECT DISTINCT s.product_id
    FROM Sales s
    WHERE s.sale_date BETWEEN '2019-01-01' AND '2019-03-31'
) AND p.product_id NOT IN (
    SELECT DISTINCT s.product_id
    FROM Sales s
    WHERE s.sale_date < '2019-01-01' OR s.sale_date > '2019-03-31'
)