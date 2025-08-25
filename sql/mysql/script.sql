CREATE TABLE employees(
employee_id INT(10),
name VARCHAR(999),
manager_id INT(10),
sector_id INT(10)
);

CREATE TABLE sectors(
sector_id INT(10),
name VARCHAR(999)
);

CREATE TABLE managers(
manager_id INT(10),
name VARCHAR(999),
area VARCHAR(999)
);


LOAD DATA INFILE '/var/lib/mysql-files/bytebytego/employees.csv'
INTO TABLE employees
FIELDS TERMINATED BY ';'
IGNORE 1 ROWS;

LOAD DATA INFILE '/var/lib/mysql-files/bytebytego/managers.csv'
INTO TABLE managers
FIELDS TERMINATED BY ';'
IGNORE 1 ROWS;

LOAD DATA INFILE '/var/lib/mysql-files/bytebytego/sectors.csv'
INTO TABLE sectors
FIELDS TERMINATED BY ';'
IGNORE 1 ROWS;
