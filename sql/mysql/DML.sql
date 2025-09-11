SHOW databases;

USE mysql;
USE bytebytego;
USE analytics;

SHOW tables;
SELECT * FROM columns_priv;
SELECT * FROM brasil_pib_pop;

USE performance_schema;
SHOW tables;
SELECT * FROM accounts;

USE Parks_and_Recreation;
SHOW tables;

SELECT * FROM employee_salary;
SELECT * FROM employee_demographics;
SELECT * FROM parks_departments;

-- When selecting columns, it's useful to write each one of them in a different line in order to make easier the visualization.
SELECT first_name,
last_name,
age,
(age + 10) * 10 + 10
FROM Parks_and_Recreation.employee_demographics
;

/*
Order operation in mysql is PEMDAS:
Parenthesis
Exponential
Multiplication
Division
Addition
Subtraction
*/

-- in case I want to exclude the repeated values, I can simply write 'DISTINCT' after 'SELECT', like this:
SELECT DISTINCT occupation FROM employee_salary;

-- besides selecting columns, you can also create new columns, separating them by coma. Some of them are even preset functions, like the following ones:
SELECT occupation, sum(salary), count(salary), avg(salary) FROM employee_salary GROUP BY occupation;

-- it's also possible (and recommended) that, when using SELECT, add the column as well as the originating database, in order to avoid errors.
SELECT * FROM analytics.empresa;

-- WHERE: using WHERE for logical inferences: (if there's two columns selected, the distinction will be taking into account the columns together)
SELECT DISTINCT first_name, last_name, age 
FROM Parks_and_Recreation.employee_demographics 
WHERE age > 20 
AND first_name
;
 
 -- the 'different' logal operator in MySQL is the  != or the <>. Other operators are AND, OR, NOT...
SELECT * 
FROM employee_demographics
WHERE birth_date > '1985-01-01'
OR NOT gender = 'male'
;

-- LIKE: the LIKE statement allows you to search for something with no need to write the whole - in case you don't know the etire name, for instance.
SELECT * 
FROM Parks_and_Recreation.employee_salary
WHERE first_name NOT LIKE 'A%'
;

-- GROUP BY: if there's no function along with the selected column to aggregate with, the column must be the same one chosen after the GROUP BY command.
SELECT gender
FROM employee_demographics
GROUP BY gender
;
SELECT gender, AVG(age), max(age), min(age), count(age) FROM employee_demographics GROUP BY gender;

-- ORDER BY: this works for organizing the order of the registries in the selected column, as ASC or DESC:
SELECT * FROM analytics.empresa ORDER BY 3 ASC; 
-- it's also possible to refer to the column by its respective number. Not recommended for, though; the counting may be wrong. Counting starts on 1, unlike python.

-- HAVING: some situations require using HAVING instead of WHERE, when in sinchrony with GROUP BY.
SELECT gender, avg(age) FROM employee_demographics GROUP BY gender HAVING avg(age) > 40; 

-- the avg() only works if you GROUP; and the HAVING only works when after the GROUP BY.
SELECT occupation, avg(salary) FROM employee_salary WHERE occupation LIKE '%Manager%' GROUP BY occupation HAVING avg(salary) > 75000;

-- LIMIT: if you put a single value, it shows only the first n registries you asked. If two values are placed, the first one tells where to start counting, and the second tells how many to count, starting by your registry of choice.
SELECT * FROM employee_salary LIMIT 5;
SELECT * FROM employee_demographics LIMIT 3, 3;

-- ALIASING (AS or   ): is used to change the name of a column. Too useful to change names given by functions like avg() for instance.
SELECT occupation, avg(salary) avg_salary FROM employee_salary GROUP BY occupation HAVING avg_salary > 75000;

SELECT * FROM analytics.empresa;
SELECT avg(dependentes) AS avg_mensile FROM analytics.empresa GROUP BY dependentes;

-- (INNER)JOIN: join two tables together. use the command (INNER) JOIN. Notice it'll only work if you tell the smallest table to INNER JOIN the bigger one. INNER JOIN <smaller table>
SELECT * FROM employee_salary
INNER JOIN employee_demographics ON employee_salary.employee_id = employee_demographics.employee_id;

-- LEFT JOIN: put employee salary on the left side, and the otehr table on the right one. Since the rght table is missing n2, it adds NULL for values.
SELECT * FROM employee_salary AS saly
LEFT JOIN employee_demographics AS demo
ON demo.employee_id = saly.employee_id
LIMIT 5;

-- RIGHT JOIN: 
SELECT * FROM employee_salary AS saly
RIGHT JOIN employee_demographics AS demo
ON demo.employee_id = saly.employee_id
LIMIT 5;

SELECT * FROM employee_demographics AS dem
RIGHT JOIN employee_salary AS sal ON sal.employee_id = dem.employee_id
LIMIT 5;

-- Edit > Preferences > SQL Editor > uncheck the box for 'safe update and delete.' to enable function.

UPDATE employee_salary 
SET first_name = 'Fellipe' 
WHERE empĺoyee_id = 1;