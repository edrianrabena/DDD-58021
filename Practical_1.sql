CREATE DATABASE ABC_Computer;

CREATE TABLE Computer (
SerialNumber BIGINT NOT NULL,
Make TEXT (12) NOT NULL,
Model TEXT (12) NOT NULL,
ProcessorType TEXT (24),
ProcessorSpeed DOUBLE (3,2) NOT NULL,
MainMemory TEXT (15) NOT NULL,
DiskSize TEXT (15) NOT NULL,
PRIMARY KEY (SerialNumber),
CONSTRAINT Computer CHECK (Make IN ('Dell', 'HP','Other')));

SELECT * FROM Computer;

INSERT INTO Computer VALUES
(9871234, 'HP', 'Pavilion 500-210qe', 'Intel i5-4530', 3.00, '6.0 Gbytes', '1.0 Tbytes'),
(9871245, 'HP', 'Pavilion 500-210qe', 'Intel i5-4531', 3.00, '6.0 Gbytes', '1.0 Tbytes'),
(9871256, 'HP', 'Pavilion 500-210qe', 'Intel i5-4532', 3.00, '6.0 Gbytes', '1.0 Tbytes'),
(9871267, 'HP', 'Pavilion 500-210qe', 'Intel i5-4533', 3.00, '6.0 Gbytes', '1.0 Tbytes'),
(9871278, 'HP', 'Pavilion 500-210qe', 'Intel i5-4534', 3.00, '6.0 Gbytes', '1.0 Tbytes'),
(9871289, 'HP', 'Pavilion 500-210qe', 'Intel i5-4535', 3.00, '6.0 Gbytes', '1.0 Tbytes'),
(6541001, 'Dell', 'OptiPlex 9020', 'Intel i7-4770', 3.00, '8.0 Gbytes', '1.0 Tbytes'),
(6541002, 'Dell', 'OptiPlex 9021', 'Intel i7-4771', 3.00, '8.0 Gbytes', '1.0 Tbytes'),
(6541003, 'Dell', 'OptiPlex 9022', 'Intel i7-4772', 3.00, '8.0 Gbytes', '1.0 Tbytes'),
(6541004, 'Dell', 'OptiPlex 9023', 'Intel i7-4773', 3.00, '8.0 Gbytes', '1.0 Tbytes'),
(6541005, 'Dell', 'OptiPlex 9024', 'Intel i7-4774', 3.00, '8.0 Gbytes', '1.0 Tbytes'),
(6541006, 'Dell', 'OptiPlex 9025', 'Intel i7-4775', 3.00, '8.0 Gbytes', '1.0 Tbytes');

SELECT * FROM Computer WHERE Make = 'HP';
SELECT * FROM Computer WHERE Make = 'Dell';

ALTER TABLE Computer ADD COLUMN Graphics Text(40) NOT NULL AFTER DiskSize;

UPDATE Computer SET Graphics = 'Integrated Intel HD Graphics 4600';

ALTER TABLE Computer DROP ProcessorSpeed;