use book_store;

create table books(book_id int identity(1,1) primary key,
author_firsname varchar(50), 
author_lastname varchar(50),
title varchar(100),
year_released INT,
genre varchar(100),
pages int,
available_copies int,
reviews int,
gender varchar(100));

exec sp_columns books;

insert into books(author_firsname, author_lastname, title, year_released, genre, pages, available_copies, reviews, gender)
values
('bryan', 'stevenson', 'Just Mercy',2014,'Memoir',368,80,4866,'male'),
('elizabeth', 'gilbert', 'CIty of girls',2020,'Fiction',496,164,2380,'female'),
('grant', 'cardone', 'be obsessed or be average', 2016, 'self help', 240,150,2735,'Male'),
('john', 'maxwell', 'intentional living', 2014, 'self help', 288, 320, 876,'female'),
('chimamanda', 'Adichie', 'Purpel Hibiscus', 2013, 'fiction',320 ,95, 5644, 'female'),
('calros', 'zafon', 'the shadow of the wind', 2005, 'thriller', 512, 55, 2790, 'male'),
('patricia', 'cornwell', 'bow fly', 2005, 'fiction', 224, 345, 2826, 'male');

select * from books;

select concat ('hello', 'world') as name;

select CONCAT (author_firsname, ' ',author_lastname) as author, CONCAT ('was written by ', title) from books;
select left('4456 liverpool street', 5);

select title, left(title, 5) from books;
select author_firsname, author_lastname, left (author_firsname, 6) as nickname from books;

select * from books;


select concat(left(title, 10), '.....') as 'short title' from books;


select concat(title, ' was written by ', author_firsname, ' in year ', right(year_released, 2)) from books;

select len(title) from books;

select upper(author_firsname) from books;

select concat(upper(author_lastname), ', ',author_firsname) from books;

select len('    pass')

select len(ltrim('    pass'))

select len(('pass    ')) --4

select len(rtrim('pass    ')) --4

select len(trim('     password    '));

select reverse(author_lastname) as reverse_names from books;

select replace('vinay purs', 'purs', 'pursnani');

select substring('vinay pursnani', 1,5);

-- insert character value with apostrophe
insert into books(author_firsname)
values('mc''mcbride');

