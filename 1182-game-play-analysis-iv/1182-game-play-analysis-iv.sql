# Write your MySQL query statement below
WITH first_login AS (
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
)

SELECT ROUND(COUNT(DISTINCT a.player_id) / COUNT(DISTINCT f.player_id), 2) AS fraction
FROM first_login f LEFT JOIN Activity a ON f.player_id = a.player_id
AND a.event_date = DATE_ADD(f.first_login, INTERVAL 1 DAY);