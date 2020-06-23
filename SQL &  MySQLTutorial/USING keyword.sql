USE sql_store;

SELECT c.customer_id, o.status, c.address
FROM orders o
JOIN customers c USING (customer_id);