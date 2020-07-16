USE sql_store;

-- SELECT first_name,last_name FROM customers WHERE STATE = 'VA' OR STATE = 'FL' OR STATE = 'CA'

SELECT first_name,last_name FROM customers WHERE STATE IN ('VA', 'FL', 'CA');