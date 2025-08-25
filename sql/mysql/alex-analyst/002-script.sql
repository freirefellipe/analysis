show databases;

use Parks_and_Recreation;
show tables;
SELECT * FROM employee_salary;

use mysql;
show tables;
SELECT * FROM columns_priv;

use performance_schema;
show tables;
SELECT * FROM accounts;

-- in case I want to exclude the repeated values, I can simply write 'DISTINCT' after 'SELECT', like this:
SELECT DISTINCT occupation FROM employee_salary;

-- besides selecting columns, you can also create new columns, separating them by coma. Some of them are even preset functions, like the following ones:
SELECT occupation, sum(salary), count(salary), avg(salary) FROM employee_salary GROUP BY occupation;

SELECT * FROM analytics.empresa;

