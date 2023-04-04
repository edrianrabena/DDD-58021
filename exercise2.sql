INSERT INTO EMP_1 (
EMP_NUM, EMP_Lname, EMP_FNAME, EMP_INITIAL, EMP_HIREDATE, JOB_CODE)
VALUES
('101', 'Nevas', 'John', 'G', '1994-11-08', 502),
('102', 'Senior', 'David', 'H', '1987-07-12', 501),
('103', 'Arbos', 'June', 'E', '1996-12-01', 500),
('104', 'Ramoras', 'Anne', 'K', '1998-11-15', 501),
('105', 'Joson', 'Alice', 'P', '1993-02-01', 502),
('106', 'Smith', 'William', 'D', '1990-06-23', 500),
('107', 'Alonso', 'Mara', 'F', '1991-10-10', 500),
('108', 'Washington', 'Raf', 'S', '1989-08-22', 501),
('109', 'Field', 'Larry', 'W', '1999-07-18', 501);

UPDATE exercise1.EMP_1 SET JOB_CODE = '501' WHERE EMP_NUM = '106';

DELETE FROM EMP_1 WHERE EMP_NUM = '106';

SELECT * FROM EMP_1;