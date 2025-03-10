# Write your MySQL query statement below
WITH cte AS (
    SELECT student_id, subject, score,
           RANK() OVER (PARTITION BY student_id, subject ORDER BY exam_date ASC) AS first_rank,
           RANK() OVER (PARTITION BY student_id, subject ORDER BY exam_date DESC) AS last_rank
    FROM Scores
)

SELECT student_id, subject,
       MAX(CASE WHEN first_rank = 1 THEN score END) AS first_score,
       MAX(CASE WHEN last_rank = 1 THEN score END) AS latest_score
FROM cte
GROUP BY student_id, subject
HAVING latest_score > first_score
ORDER BY student_id, subject;