USE sql_store;


-- You have to fetch all the columns from customers table where the mobile number of the customer ends with 9

SELECT *
FROM customers
WHERE phone LIKE '%9';