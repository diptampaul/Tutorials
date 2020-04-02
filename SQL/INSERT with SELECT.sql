USE sql_store;

INSERT INTO customer_archieved
SELECT *
FROM customers
WHERE points < 2000;