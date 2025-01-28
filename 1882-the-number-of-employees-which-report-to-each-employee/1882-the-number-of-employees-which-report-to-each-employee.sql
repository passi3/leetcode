# Write your MySQL query statement below
SELECT e.employee_id AS employee_id, e.name AS name, COUNT(r.reports_to) AS reports_count, ROUND(AVG(r.age), 0) AS average_age
FROM Employees e LEFT JOIN Employees r
ON e.employee_id = r.reports_to
WHERE r.employee_id IS NOT NULL
GROUP BY e.employee_id, e.name
ORDER BY e.employee_id;