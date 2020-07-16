USE sql_store;

DROP TRIGGER IF EXISTS ins_name;

CREATE TRIGGER ins_name
BEFORE INSERT ON customers
FOR EACH ROW
SET NEW.first_name = UPPER(NEW.first_name);

CREATE TRIGGER up_name
BEFORE UPDATE ON customers
FOR EACH ROW
SET NEW.first_name = LOWER(NEW.first_name);