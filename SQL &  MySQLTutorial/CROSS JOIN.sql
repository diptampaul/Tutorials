USE sql_store;

SELECT c.first_name AS Customer_name, p.name AS Product_name
FROM customers c
CROSS JOIN products p;