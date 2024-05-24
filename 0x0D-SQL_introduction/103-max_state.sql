-- This script calculates the maximum temperature for each state
-- and lists them ordered by state name

SELECT state, MAX(temperature) AS max_temp
FROM temperature
GROUP BY state
ORDER BY state;
