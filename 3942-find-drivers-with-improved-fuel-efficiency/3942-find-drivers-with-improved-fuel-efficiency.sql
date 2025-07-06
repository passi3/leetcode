# Write your MySQL query statement below
WITH r1 AS
(WITH r AS
(SELECT d.driver_id, 
    d.driver_name,
    CASE WHEN MONTH(t.trip_date) BETWEEN 1 AND 6 THEN 'f' ELSE 's' END AS Half,
    AVG(t.distance_km/t.fuel_consumed) AS avg
FROM drivers d
RIGHT JOIN trips t
ON t.driver_id = d.driver_id
GROUP BY d.driver_id, Half)
SELECT driver_id,
    driver_name,
    ROUND(SUM(CASE WHEN Half='f' THEN avg ELSE 0 END), 2) AS first_half_avg,
    ROUND(SUM(CASE WHEN Half='s' THEN avg ELSE 0 END), 2) AS second_half_avg,
    ROUND(SUM(CASE WHEN Half='s' THEN avg ELSE 0 END) - SUM(CASE WHEN Half='f' THEN avg ELSE 0 END), 2) AS efficiency_improvement
FROM r
WHERE driver_id IN 
(SELECT driver_id
FROM r
GROUP BY driver_id
HAVING COUNT(Half) = 2)
GROUP BY driver_id
ORDER BY efficiency_improvement DESC, driver_name)
SELECT * FROM r1
WHERE efficiency_improvement >= 0;