-- init database

drop database if exists test;

create database test;

use test
create table user (
    `id` varchar(20) not null,
    `name` varchar(20) not null, 
    primary key (`id`) 
) engine=innodb default charset=utf8;
