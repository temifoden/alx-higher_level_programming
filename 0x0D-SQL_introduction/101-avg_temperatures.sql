-- This script calculates the average temperature (fahrenheit) by city
-- and orders the result by the average temperature in descending order

SELECT city, AVG(temperature) AS avg_temp
FROM temperature
GROUP BY city
ORDER BY avg_temp DESC;
