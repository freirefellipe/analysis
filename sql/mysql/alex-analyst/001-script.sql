SHOW databases;
USE Parks_and_recreation;
SHOW tables;

SELECT * FROM employee_salary;
SELECT * FROM employee_demographics;
SELECT * FROM parks_departments;

#### When selecting columns, it's useful to write each one of them in a different line in order to make easier the visualization.

SELECT first_name,
last_name,
age,
(age + 10) * 10 + 10
FROM Parks_and_Recreation.employee_demographics;

#### Order operation in mysql is PEMDAS:
# Parenthesis
# Exponential
# Multiplication
# Division
# Addition
# Subtraction

SELECT DISTINCT first_name, last_name, age 
FROM Parks_and_Recreation.employee_demographics 
WHERE age > 20 
AND first_name;

SELECT gender FROM employee_demographics
GROUP BY gender;

SELECT occupation
FROM employee_salary
GROUP BY occupation
;
