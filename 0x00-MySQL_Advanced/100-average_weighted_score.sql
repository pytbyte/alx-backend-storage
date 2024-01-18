-- Create a stored procedure ComputeAverageWeightedScoreForUser
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN myuser_id INT
)
BEGIN
    DECLARE score_weight FLOAT;
    DECLARE total_weight FLOAT;
    
    -- Initialize variables
    SET score_weight = 0;
    SET total_weight = 0;

    -- Calculate the total weighted score
    SELECT SUM(corrections.score * projects.weight) INTO score_weight
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = myuser_id;

    -- Calculate the total weight
    SELECT SUM(weight) INTO total_weight
    FROM projects;

    -- Update the average_score for the user
    UPDATE users
    SET average_score = IFNULL(score_weight / total_weight, 0)
    WHERE id = myuser_id;

END;
//

DELIMITER ;
