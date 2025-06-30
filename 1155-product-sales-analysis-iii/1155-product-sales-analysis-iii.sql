# Write your MySQL query statement below
WITH first_sale_year AS (
    SELECT product_id, MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
)

SELECT s.product_id, s.year AS first_year, s.quantity, s.price
FROM Sales s
JOIN first_sale_year fsy
  ON s.product_id = fsy.product_id AND s.year = fsy.first_year;