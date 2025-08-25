sudo apt update ; sudo apt upgrade -Y 
sudo apt install mysql-server
sudo systemctl status mysql 														(check functionality)
sudo mysql 
sudo mysql -u <username> -p <password> -h <website> 								(pro connecting way. user, password and place)
sudo mysqladmin -u root password "<newpassword>"									(set up a password for your mysql)

create database <namethedatabase>;
show databases; 
use <database>;
create table <nametable> (
1 column [int NOT NULL AUTOINCREMENT,												(it's possible to use INT NOT NULL AUTO INCREMENT)
2 column [FLOAT (X,Y),																(adding x and y is not mandatory)
3 column [varchar (<numberofcharacters>)],											(this is for  text, string)
);

show tables;
describe <table>

insert into <table> values (<1columnvalue>, <2columnvalue>, <3columnvalue>);
select * from <table>;																(The * will return all data from the table)
select <column> from <table>;
select * from <table> where <column> = '<condition>';								(show all the columns that have a specific data in one of'em)
select * from <table> where <column> = '<condition>' or <column> = '<confition>'	(there can be more than one condition)

delete from <table> where <column> = '<condition>';
update <table> set <column> = NULL where <column> = '<condition>';					(change a chosen value to null)
select * from <table> order by <column> asc;										(organize a table by ascendence on a specific column)
alter table <table> add <namecolumn> <namedatatype>									(add a new column to a table. All inner values shall be Null)

LOAD DATA LOCAL INFILE '<directory>'												(LOCAL should avoid probs with 'secure-file-priv')
INTO TABLE <table> 
FIELDS TERMINATED BY '<character>' 
LINES TERMINATED BY '\n' 

SHOW VARIABLES LIKE 'secure-file-priv';												(to show where files can be manipulated. Put the .csv files in this folder to make tables') 



SELECT * FROM empresa WHERE dependentes >= 2 AND id LIKE '111%'                     (LIKE is used with simple quotes after (no equal sign), having the character % as its best feature)

THE NOT OPERATOR
Can be placed before WHERE or LIKE, to make condition of exclusion.
