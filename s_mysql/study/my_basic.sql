use test;

create table tbl_member(
    email varchar(255) primary key,
    password varchar(255) not null,
    name varchar(255)
);

select * from tbl_member;
commit;

create table tbl_product(
    id bigint auto_increment primary key,
    name varchar(255) not null,
    price int default 0,
    created_date datetime
);

select * from tbl_product;

truncate table tbl_product;

insert into tbl_product(name, price, created_date)
values('한라봉', '5000', '2024-01-17T18:20:00');

insert into tbl_product(name, price, created_date)
values('자두', '500', '2024-01-17T18:20:00');

insert into tbl_product(name, price, created_date)
values('귤', '2500', '2024-01-17T18:20:00');

insert into tbl_product(name, price, created_date)
values('사과', '0', '2024-01-17T18:20:00');

insert into tbl_product(name, price, created_date)
values('배', '3000', '2024-01-17T18:20:00');

insert into tbl_product(name, price, created_date)
values('딸기', '2000', '2024-01-17T18:20:00');

insert into tbl_product(name, price, created_date)
values('수박', '20000', '2024-01-17T18:20:00');

insert into tbl_product(name, price, created_date)
values('용과', '30000', '2024-01-17T18:20:00');

insert into tbl_product(name, price, created_date)
values('스타후르츠', '3500', '2024-01-17T18:20:00');

insert into tbl_product(name, price, created_date)
values('두리안', '10000', '2024-01-17T18:20:00');