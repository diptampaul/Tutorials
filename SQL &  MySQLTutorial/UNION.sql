USE sql_store;

SELECT 
	order_id,
    customer_id,
    'ACTIVE' AS status
FROM orders
WHERE order_date >= '2019-01-01'
UNION
SELECT 
	order_id,
    customer_id,
    'ARCHIEVED' AS status
FROM orders
WHERE order_date < '2019-01-01';



-- EXERCISE 5 : Query the name of the customer along with address and points and level-type. Level type can be bronze, silver and gold. 

SELECT first_name AS name, address, points, 'BRONZE' AS level_type
FROM customers
WHERE points < 1500
UNION
SELECT first_name AS name, address, points, 'SILVER' AS level_type
FROM customers
WHERE points BETWEEN 1500 AND 3000
UNION
SELECT first_name AS name, address, points, 'GOLD' AS level_type
FROM customers
WHERE points > 3000
ORDER BY name;



