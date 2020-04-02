USE sql_store;


-- Using of WHEN and THEN operator
SELECT order_id, order_date,
CASE status
WHEN 1 THEN 'shipped'
ELSE concat(order_id, ' will be shipped soon')
END AS order_status
FROM orders;


-- Using of IF and NULL IF operator

SELECT customer_id, state,
IF(first_name LIKE '%a%', 'vowel' , NULL) AS name
FROM customers;

SELECT order_id, order_date,
NULLIF( status , 2 ) AS order_status
FROM orders;

