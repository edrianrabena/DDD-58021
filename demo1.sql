CREATE SCHEMA myscheme;

CREATE TABLE orderstable(OrderID INT NOT NULL, OrderNumber INT NOT NULL, PRIMARY KEY (OrderID));

INSERT INTO orderstable(OrderID, OrderNumber) VALUES ('1','77895'), ('2','44678'), ('3','22456');

SELECT * FROM testdatabase.PersonsTable;

SELECT * FROM testdatabase.SAMPLE

SELECT * FROM myownschema.student;

INSERT INTO customer
values('12', 'HEHE', '45');

DROP DATABASE testdatabase;

CREATE DATABASE testdatabase
