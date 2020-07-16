-- Fetch all the details of the customer who born in between Jan 1st 1980 and Dec 31 1990


USE sql_store;
SELECT * FROM customers WHERE birth_date BETWEEN '1980-01-01' AND '1990-12-31';