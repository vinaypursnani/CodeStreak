CREATE TABLE customer2( username VARCHAR(20) NOT NULL,
firstname VARCHAR(50) NOT NULL,
lastname VARCHAR(50) NOT NULL,
telephone INT,
email VARCHAR(50) NOT NULL,
age INT);

SELECT * FROM customer2;

INSERT INTO customer2(username, firstname, lastname, telephone, email, age)
VALUES ('vpursnani', 'vinay', 'pursnani', 70200, 'vinaypursnani@icloud.com', 21);