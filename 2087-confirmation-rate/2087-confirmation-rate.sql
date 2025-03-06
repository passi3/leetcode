# Write your MySQL query statement below
SELECT s.user_id,
    COALESCE(ROUND(SUM(c.action = 'confirmed') / COUNT(s.user_id),2), 0
) AS confirmation_rate
FROM Confirmations c RIGHT JOIN Signups s ON c.user_id = s.user_id
GROUP BY s.user_id;