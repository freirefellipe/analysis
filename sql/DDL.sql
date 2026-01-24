USE analise;

CREATE TABLE customers(
customer_id VARCHAR(255),
first_name VARCHAR(255)
);

CREATE TABLE employees(
employee_id VARCHAR(255),
name VARCHAR(255),
manager_id INT(10),
sector_id INT(10)
);

CREATE TABLE sectors(
sector_id VARCHAR (255),
name VARCHAR(255)
);

CREATE TABLE managers(
manager_id VARCHAR(255),
name VARCHAR(255),
area VARCHAR(255)
);

CREATE TABLE products(
order_id VARCHAR(255),
amount INT(10),
customer VARCHAR(255)
);


LOAD DATA LOCAL INFILE '/home/fellipe/Dropbox/code/analysis/public_data/company/customers.csv'
INTO TABLE customers
FIELDS TERMINATED BY ';'
IGNORE 1 ROWS;

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

LOAD DATA LOCAL INFILE '/home/fellipe/Dropbox/code/analysis/public_data/company/products.csv'
INTO TABLE products
FIELDS TERMINATED BY ';'
IGNORE 1 ROWS;
