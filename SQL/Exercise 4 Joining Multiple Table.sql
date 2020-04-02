USE sql_invoicing;

-- Queries the name of the clients with address, payment amount, and payment methods from the sql_invoicing database

SELECT c.name, c.address, p.amount, pm.name AS payment_methods
FROM clients c
JOIN payments p 
	ON c.client_id = p.client_id
    
JOIN payment_methods pm
	ON p.payment_method = pm.payment_method_id