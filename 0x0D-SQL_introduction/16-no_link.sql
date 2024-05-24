-- This script lists all records from the table second_table without rows without a neme value,
-- displaying the score and name in descending order of score

SELECT score, name
FROM second_table
where name IS NOT NULL
ORDER BY score DESC;
