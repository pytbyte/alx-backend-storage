-- Creates a stored procedure ComputeAverageWeightedScoreForUsers that
-- computes and stores the average weighted score for all students.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    ALTER TABLE users ADD collective_score INT NOT NULL;
    ALTER TABLE users ADD all_weight INT NOT NULL;

    UPDATE users
        SET collective_score = (
            SELECT SUM(corrections.score * projects.weight)
            FROM corrections
            INNER JOIN projects ON corrections.project_id = projects.id
            WHERE corrections.user_id = users.id
        );

    UPDATE users
        SET all_weight = (
            SELECT SUM(projects.weight)
            FROM corrections
            INNER JOIN projects ON corrections.project_id = projects.id
            WHERE corrections.user_id = users.id
        );

    UPDATE users
        SET users.average_score = IF(users.all_weight = 0, 0, users.collective_score / users.all_weight);

    ALTER TABLE users DROP COLUMN collective_score;
    ALTER TABLE users DROP COLUMN all_weight;
END;
//

DELIMITER ;
