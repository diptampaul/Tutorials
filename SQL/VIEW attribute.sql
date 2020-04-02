USE sql_hr;

-- CREATE VIEW employees_under_manager AS
-- SELECT e.employee_id, e.first_name, m.first_name AS manager
-- FROM employees e
-- INNER JOIN employees m ON e.reports_to = m.employee_id;

UPDATE employees_under_manager SET employee_id = 35000 WHERE first_name = 'Sayer';