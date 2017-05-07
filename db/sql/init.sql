-- init database

drop database if exists test;

create database test;

use test;
create table user (
    id varchar(20) not null auto_increment,
    name varchar(20) not null, 
    primary key (`id`) 
) engine=innodb default charset=utf8;

insert into user (name) values('Harden');
insert into user (name) values('Kobe')
