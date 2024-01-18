-- divides (and returns) the first by the second number or 0
DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER //

CREATE FUNCTION SafeDiv(
    p_a INT,
    p_b INT
)
RETURNS FLOAT DETERMINISTIC
BEGIN
    DECLARE result FLOAT;

    -- results
    IF p_b = 0 THEN
        SET result = 0;
    ELSE
        SET result = p_a / p_b;
    END IF;

    RETURN result;
END;
//

DELIMITER ;
