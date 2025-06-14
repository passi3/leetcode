# Write your MySQL query statement below
WITH Combined AS (
  SELECT 
    pp.user_id,
    pp.product_id,
    pi.category
  FROM ProductPurchases pp
  JOIN ProductInfo pi ON pp.product_id = pi.product_id
)

SELECT 
  p1.product_id AS product1_id,
  p2.product_id AS product2_id,
  p1.category AS product1_category,
  p2.category AS product2_category,
  COUNT(DISTINCT p1.user_id) AS customer_count
FROM Combined p1
JOIN Combined p2 
  ON p1.user_id = p2.user_id AND p1.product_id < p2.product_id
GROUP BY 
  p1.product_id, p2.product_id, p1.category, p2.category
HAVING customer_count >= 3
ORDER BY customer_count DESC, product1_id ASC, product2_id ASC;