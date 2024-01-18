-- ComputeAverageScoreForUser computes and store the average score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id_ INT
)
BEGIN
    DECLARE marks INT;
    DECLARE projects INT;
    DECLARE mean FLOAT;

    -- Compute total score and total projects for the user
    SELECT SUM(score), COUNT(project_id)
    INTO marks, projects
    FROM corrections
    WHERE user_id = user_id_;

    -- Compute the average score
    IF projects > 0 THEN
        SET mean = marks / projects;
    ELSE
        SET mean = 0;
    END IF;

    -- Update the mean in the users table
    UPDATE users
    SET mean = mean
    WHERE id = user_id_;
END;
//

DELIMITER ;
