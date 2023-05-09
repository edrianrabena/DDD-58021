#Creating demo2 database
CREATE DATABASE demo2;

#Creating Customer table
CREATE TABLE Customer (
CustomerID INT NOT NULL,
CustomerName TEXT (30) NOT NULL,
Municipality TEXT (20) NOT NULL,
City TEXT (20) NOT NULL,
PRIMARY KEY (CustomerID)
);

SELECT * FROM Customer;

#Populating the table
INSERT INTO Customer VALUES
(1, 'Gina de Leon', 'Apalit', 'Pampanga'),
(2, 'Amara Luna', 'Mexico', 'Pampanga'),
(3, 'Lucina Maulon', 'Angat', 'Bulacan'),
(4, 'Rafael Santos', 'Lumban', 'Laguna'),
(5, 'Maricel Moran', 'Calupit', 'Bulacan'),
(6, 'Antonio Moreno', 'Santa Maria', 'Bulacan'),
(7, 'Hanna Moos', 'Alaminos', 'Laguna'),
(8, 'Fred Gregorio', 'Lumban', 'Laguna'),
(9, 'Maria Andres', 'Porac', 'Pampanga'),
(10, 'Liza Ramos', 'Alaminos', 'Laguna');

#Command that shows all customer names from Bulacan
SELECT * FROM Customer WHERE City = 'Bulacan';

#Command that shows customers who are residing in Alaminos, Laguna
SELECT * FROM Customer WHERE Municipality = 'Alaminos' AND City = 'Laguna';

#Command that shows customers who are not residing in Pampanga
SELECT * FROM Customer WHERE NOT City = 'Pampanga'