# Write your MySQL query statement below
WITH withr AS (
    SELECT e.employee_id, name, rating, rank() OVER (
        PARTITION BY employee_id ORDER BY review_date DESC
    ) AS r
    FROM employees e JOIN performance_reviews p ON e.employee_id = p.employee_id
)

SELECT r1.employee_id, r1.name, r1.rating - r3.rating AS improvement_score
FROM withr r1, withr r2, withr r3
WHERE r1.employee_id = r2.employee_id AND r1.employee_id = r3.employee_id
AND r1.rating > r2.rating AND r2.rating > r3.rating
AND r1.r = 1 AND r2.r = 2 AND r3.r = 3
ORDER BY improvement_score DESC, name ASC;