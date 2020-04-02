USE sql_hr;

SELECT e.employee_id, e.first_name AS 'Employees First name', e.last_name, m.first_name, m.last_name
FROM employees e
JOIN employees m ON e.reports_to = m.employee_id