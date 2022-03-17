Use a2censo;

CREATE TABLE IF NOT EXISTS campaign (
idcampaign INT NOT NULL AUTO_INCREMENT,
name VARCHAR(200) NOT NULL,
amount DECIMAL(2) NOT NULL,
requestedAmount DECIMAL(2) NOT NULL,
adminRate DECIMAL(2) NULL,
PRIMARY KEY (idcampaign));

SHOW TABLES IN Campaign;

INSERT INTO campaign ( name, amount, requestedAmount) VALUES
('RobinFood 2.0', 200000000, 250000000);

INSERT INTO campaign ( name, amount, requestedAmount) VALUES ('T4
Tea For U', 1000000000, 1200000000);

INSERT INTO campaign ( name, amount, requestedAmount) VALUES
('Smoking Burgers', 200000000, 200000000);

INSERT INTO campaign ( name, amount, requestedAmount) VALUES
('Domino´s Pizza', 450000000, 500000000);

ALTER TABLE campaign
DROP amount,
DROP requestedAmount;

ALTER TABLE campaign
ADD amount DECIMAL(10) NOT NULL,
ADD requestedAmount DECIMAL(10) NOT NULL;



SELECT * FROM campaign
ORDER BY requestedAmount DESC;


