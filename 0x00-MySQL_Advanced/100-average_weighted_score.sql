-- stored procedure ComputeAverageWeightedScoreForUser
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight FLOAT;
    
    -- variables
    SET total_weighted_score = 0;
    SET total_weight = 0;

    --weighted score
    SELECT SUM(corrections.score * projects.weight) INTO total_weighted_score
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;

    -- total weight
    SELECT SUM(weight) INTO total_weight
    FROM projects;

    -- Update the average_score 
    UPDATE users
    SET average_score = IFNULL(total_weighted_score / total_weight, 0)
    WHERE id = user_id;

END;
//

DELIMITER ;
