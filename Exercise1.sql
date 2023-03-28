#Creating a database

CREATE DATABASE Exercise1;

#Question 1

CREATE TABLE EMP_1 (
EMP_NUM CHAR(3),
EMP_Lname VARCHAR(15),
EMP_FNAME VARCHAR(15),
EMP_INITIAL CHAR(1),
EMP_HIREDATE DATE,
JOB_CODE CHAR(3)
);

#Question 2

INSERT INTO EMP_1 (
EMP_NUM, EMP_Lname, EMP_FNAME, EMP_INITIAL, EMP_HIREDATE, JOB_CODE)
VALUES
('001', 'Kaedehara', 'Kazuha', 'K', '2022-07-13', '016'),
('002', 'Kamisato', 'Ayaka', 'A', '2023-03-21', '035');

#Creating an employee with a JOB_CODE of 502

INSERT INTO EMP_1 (
EMP_NUM, EMP_Lname, EMP_FNAME, EMP_INITIAL, EMP_HIREDATE, JOB_CODE)
VALUES (
'003', 'Apocalypse', 'Theresa', 'T', '2018-07-08', '502');

#Question 3

SELECT * FROM EMP_1 WHERE JOB_CODE = '502';

#Checking

SELECT * FROM EMP_1;