# Write your MySQL query statement below
SELECT ROUND(100* SUM(order_case) / COUNT(*), 2) AS immediate_percentage
FROM (
    SELECT customer_id, order_date, customer_pref_delivery_date, (CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) AS order_case
    FROM Delivery
    WHERE (customer_id, order_date) IN (
        SELECT customer_id, MIN(order_date)
        FROM Delivery
        GROUP BY customer_id
    )
) a;