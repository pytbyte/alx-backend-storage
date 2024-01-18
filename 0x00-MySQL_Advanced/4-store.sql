-- Drop the trigger if it exists
DROP TRIGGER IF EXISTS decrease_quantity;

-- Change delimiter to handle semicolons within the trigger
DELIMITER //

-- Create the trigger
CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;
//

-- Reset the delimiter
DELIMITER ;
