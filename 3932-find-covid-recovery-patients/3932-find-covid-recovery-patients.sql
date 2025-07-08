# Write your MySQL query statement below
WITH FirstPositive AS (
    SELECT 
        patient_id,
        MIN(test_date) AS first_positive
    FROM covid_tests
    WHERE result = 'Positive'
    GROUP BY patient_id
),
FirstNegative AS (
    SELECT 
        ct.patient_id,
        MIN(ct.test_date) AS first_negative
    FROM covid_tests ct
    JOIN FirstPositive fp 
        ON ct.patient_id = fp.patient_id 
       AND ct.result = 'Negative'
       AND ct.test_date > fp.first_positive
    GROUP BY ct.patient_id
),
Recovered AS (
    SELECT 
        fp.patient_id,
        DATEDIFF(fn.first_negative, fp.first_positive) AS recovery_time
    FROM FirstPositive fp
    JOIN FirstNegative fn 
        ON fp.patient_id = fn.patient_id
)
SELECT 
    r.patient_id,
    p.patient_name,
    p.age,
    r.recovery_time
FROM Recovered r
JOIN patients p 
    ON r.patient_id = p.patient_id
ORDER BY r.recovery_time ASC, p.patient_name ASC;