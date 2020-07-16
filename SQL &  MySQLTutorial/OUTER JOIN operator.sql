USE sql_hr;

-- SELECT c.customer_id, c.first_name, o.order_id, s.shipper_id
-- FROM customers c
-- LEFT JOIN orders o
-- 	ON o.customer_id = c.customer_id
    
-- LEFT JOIN shippers s
-- 	ON o.shipper_id = s.shipper_id
-- ORDER BY c.customer_id ASC; 


-- SELF OUTER JOIN


SELECT e.employee_id, e.first_name, m.first_name
FROM employees e
LEFT JOIN employees m ON e.reports_to = m.employee_id