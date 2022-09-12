create database Project1;
use Project1;

select @@SERVERNAME;

create table tblEmployee(
	empNo int primary key,
	fName varchar(25),
	mName varchar(25),
	lName varchar(25),
	designation varchar(25),
	joinDate date,
	salary int,
	address_ varchar(300),
	city varchar(25)
);

select * from tblEmployee;

insert into tblEmployee values (1,'Jaya','Ranjita','Kumari','Product Manager','2019-07-01','35000','2640/3 2nd Floor, Gurudwara Road','Delhi');
insert into tblEmployee values (2,'Irfan','Arif','Khan','Chief Architect','2016-02-11','45000','603, Anna Salai','Chennai');
insert into tblEmployee values (3,'Sikandar','','Inayat','Software Architect','2018-11-21','40000','82/84, Masjid Bunder Road, Near Satkar Hotel, Mandvi','Mumbai');
insert into tblEmployee values (4,'Gotam','','Nagendra','Software Architect','2020-04-03','30000','204 Veena Industril Estate, L.b.s Marg, Vikhroli','Mumbai'); 