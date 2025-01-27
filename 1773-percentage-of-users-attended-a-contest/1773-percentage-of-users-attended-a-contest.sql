# Write your MySQL query statement below
SELECT contest_id, ROUND(100* COUNT(user_id) / (SELECT COUNT(*) FROM Users), 2) AS percentage
FROM Register
WHERE contest_id IS NOT NULL
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;