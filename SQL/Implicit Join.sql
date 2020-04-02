USE sql_store;

-- SELECT *
-- FROM orders o
-- JOIN customers c ON o.customer_id = c.customer_id

-- Implicit Format

SELECT *
FROM orders, customers
WHERE orders.customer_id = customers.customer_id;
