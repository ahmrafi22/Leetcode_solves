-- Write your PostgreSQL query statement below
SELECT email as Email
FROM Person
GROUP BY email
HAVING count(email) > 1;