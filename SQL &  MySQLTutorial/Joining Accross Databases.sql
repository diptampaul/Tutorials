USE sql_inventory;

SELECT oi.product_id, name, quantity
FROM sql_store.order_items oi
JOIN products p ON oi.product_id = p.product_id;