-- Creates a trigger to reset valid_email only onchange
DROP TRIGGER IF EXISTS valid_email_reseter;
DELIMITER //

CREATE TRIGGER valid_email_reseter
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;
//

DELIMITER ;
