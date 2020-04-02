USE sql_store;

SELECT 
first_name, 
last_name, 
address, 
points,
points * (20 + 5) AS 'final points'
FROM customers;