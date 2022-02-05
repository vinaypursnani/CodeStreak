use pets;

select * from customer2;


insert into customer2(username, firstname, lastname, email)
values('archenite', 'gamer', 'front','arch3nite@gmail.com');

create table voters(firstname VARCHAR(50), lastname VARCHAR(50), city VARCHAR(50) DEFAULT 'Indore');
select * from voters;

INSERT into voters (firstname, lastname)
VALUES ('vinay', 'pursnani');

insert into voters (firstname, lastname, city)
values('archenite', 'gamer', 'indore');

create table employees(id INT, firstname VARCHAR(20), lastname VARCHAR(30));

insert into employees(id, firstname, lastname)
values(1, 'peter', 'peter.parker@gmail.com'), (2, 'peter', 'peter.parker@gmail.com');
select * from employees;

create table employeesUnique(id int, firstname varchar(20), lastname varchar(50) unique);

insert into employeesUnique(id, firstname, lastname)
values(1, 'peter', 'parker'), (2, 'peter', 'parking');

create table students (student_id INT PRIMARY KEY, firstname varchar(20), lastname varchar(20));

insert into students(student_id, firstname, lastname)
values(1, 'jhon', 'snow'), (2, 'jhon', 'snow');

select  * from students;

/* IDENTITY (seed, increment)
*/
create table student2(student_id int identity(101, 1) primary key, firstname varchar(50), lastname varchar(50));

insert into student2(firstname, lastname)
values ('jhon', 'snow'), ('sharp', 'sully');

select * from student2;

create table penguin(
penguin_id INT IDENTITY(1,1) PRIMARY KEY,
name VARCHAR(50),
breed VARCHAR(50),
sex VARCHAR(3),
age int,
color varchar(50)
);

insert into penguin(name, breed, sex, age, color)
values ('mel', 'little penguin', 'f', 5, 'gray'), 
('cindy', 'fairy penguine', 'f', 5, 'gray'),
('frosty', 'african penguine', 'm', 5, 'gray'),
('sassy', 'northeastern rockhopper', 'f', 6, 'black'),
('fubby', 'little penguine', 'm',  7, 'golden brown');

select * from penguin;

select name from penguin;	

select age, breed from penguin;
select * from penguin where sex = 'f'; 

update penguin set name = 'melanie' where name = 'mel';
update penguin set breed = 'just penguin' where breed = 'little penguin';

select breed from penguin;

update penguin set breed = 'dexter', age = 5 where breed ='african penguine';

select * from penguin;

delete from penguin where name = 'fubby'

select * from penguin where color = 'gray'

delete from penguin where color = 'gray'

select * from penguin;

create table shoes(shoe_id INT IDENTITY(1,1) PRIMARY KEY,
shoe_size DECIMAL(3,1),
shoe_price DECIMAL(5,2),
shoe_type VARCHAR(50),
shoe_color VARCHAR(50),
)

INSERT INTO shoes(shoe_type, shoe_color, shoe_size, shoe_price)
VALUES ('sneakers', 'red', 10.5, 80),
('sneakers', 'green', 10, 155),
('converse', 'red', 11, 100),
('flipflop', 'white', 11, 34.99),
('flipflop', 'green', 12,35.99),
('boots', 'black', 8.5, 75);

select * from shoes;

create database book_store;

