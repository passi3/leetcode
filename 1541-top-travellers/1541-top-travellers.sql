# Write your MySQL query statement below
SELECT u.name AS name, COALESCE(SUM(r.distance), 0) AS travelled_distance
FROM Users u LEFT JOIN Rides r
ON u.id = r.user_id
GROUP BY r.user_id
ORDER BY travelled_distance DESC, name ASC;