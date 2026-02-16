-- Write your PostgreSQL query statement below
SELECT customer_id, COUNT(v.visit_id) AS count_no_trans
FROM Visits v
         LEFT JOIN transactions t on t.visit_id = v.visit_id
WHERE transaction_id IS NULL
GROUP BY customer_id