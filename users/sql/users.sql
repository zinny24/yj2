show databases;

create database users;

show databases;

use users;

create table users(
id int not null auto_increment,
name varchar(20),
email varchar(50) unique,
passwd varchar(100),
primary key(id)	
);

show tables;













