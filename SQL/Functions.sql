USE sql_hr;

-- CREATE FUNCTION full_name(first_name varchar(50), last_name varchar(50))
-- RETURNS varchar(100) deterministic
-- RETURN concat(first_name, ' ', last_name);


SELECT employee_id, full_name(first_name, last_name) AS name
FROM employees;