# Write your MySQL query statement below
SELECT *, 
    (CASE WHEN dna_sequence LIKE 'ATG%' THEN 1 ELSE 0 END) AS has_start,
    (CASE WHEN dna_sequence REGEXP 'TAA$|TAG$|TGA$' THEN 1 ELSE 0 END) AS has_stop,
    (CASE WHEN dna_sequence LIKE '%ATAT%' THEN 1 ELSE 0 END) AS has_atat,
    (CASE WHEN dna_sequence LIKE '%GGG%' THEN 1 ELSE 0 END) AS has_ggg
FROM Samples
ORDER BY sample_id ASC;