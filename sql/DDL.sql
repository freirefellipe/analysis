USE analise;

CREATE TABLE employees(
employee_id INT(10),
name VARCHAR(999),
manager_id INT(10),
sector_id INT(10)
);

CREATE TABLE sectors(
sector_id INT (10),
name VARCHAR(999)
);

CREATE TABLE managers(
manager_id INT(10),
name VARCHAR(999),
area VARCHAR(999)
);


LOAD DATA LOCAL INFILE '/home/fellipe/Dropbox/code/analysis/public_data/company/employees.csv'
INTO TABLE employees
FIELDS TERMINATED BY ';'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/fellipe/Dropbox/code/analysis/public_data/company/managers.csv'
INTO TABLE managers
FIELDS TERMINATED BY ';'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/fellipe/Dropbox/code/analysis/public_data/company/sectors.csv'
INTO TABLE sectors
FIELDS TERMINATED BY ';'
IGNORE 1 ROWS;
