USE sql_store;

SELECT *
FROM customers
-- WHERE last_name LIKE '%s%';
WHERE last_name REGEXP 'e[a-i]';

-- ^ starting characters
-- $ Ending      "
-- | Logical Or
-- [ABCD]
-- [a-z]