-- Daily Challenge

-- CREATE TABLE employees (
--     employee_id INT PRIMARY KEY,
--     employee_name VARCHAR(50),
--     salary DECIMAL(10, 2),
--     hire_date VARCHAR(20),
--     department VARCHAR(50)
-- );

-- INSERT INTO employees (employee_id, employee_name, salary, hire_date, department) VALUES
-- (1, 'Amy West', 60000.00, '2021-01-15', 'HR'),
-- (2, 'Ivy Lee', 75000.50, '2020-05-22', 'Sales'),
-- (3, 'joe smith', 80000.75, '2019-08-10', 'Marketing'), 
-- (4, 'John White', 90000.00, '2020-11-05', 'Finance'),
-- (5, 'Jane Hill', 55000.25, '2022-02-28', 'IT'),
-- (6, 'Dave West', 72000.00, '2020-03-12', 'Marketing'),
-- (7, 'Fanny Lee', 85000.50, '2018-06-25', 'Sales'),
-- (8, 'Amy Smith', 95000.25, '2019-11-30', 'Finance'),
-- (9, 'Ivy Hill', 62000.75, '2021-07-18', 'IT'),
-- (10, 'Joe White', 78000.00, '2022-04-05', 'Marketing'),
-- (11, 'John Lee', 68000.50, '2018-12-10', 'HR'),
-- (12, 'Jane West', 89000.25, '2017-09-15', 'Sales'),
-- (13, 'Dave Smith', 60000.75, '2022-01-08', NULL),
-- (14, 'Fanny White', 72000.00, '2019-04-22', 'IT'),
-- (15, 'Amy Hill', 84000.50, '2020-08-17', 'Marketing'),
-- (16, 'Ivy West', 92000.25, '2021-02-03', 'Finance'),
-- (17, 'Joe Lee', 58000.75, '2018-05-28', 'IT'),
-- (18, 'John Smith', 77000.00, '2019-10-10', 'HR'),
-- (19, 'Jane Hill', 81000.50, '2022-03-15', 'Sales'),
-- (20, 'Dave White', 70000.25, '2017-12-20', 'Marketing');



-- 1) Identify and handle any missing value.

-- SELECT employee_id, employee_name
-- FROM employees
-- WHERE department IS NULL;


-- Replace NULL department with 'Unknown' in results
-- SELECT 
--     employee_id,
--     employee_name,
--     salary,
--     hire_date,
--     COALESCE(department, 'Unknown') AS department
-- FROM employees;


-- Permanently update missing department to 'Unknown'
-- UPDATE employees
-- SET department = 'Unknown'
-- WHERE department IS NULL;



-- 2) Remove duplicate rows

-- Check for duplicate rows (compare total count vs distinct count)
-- SELECT 
--     COUNT(*) AS total_rows,
--     COUNT(DISTINCT employee_id || employee_name || salary || hire_date || COALESCE(department, '')) AS distinct_rows
-- FROM employees;


-- SELECT COUNT (*) AS total_rows FROM employees;
-- SELECT COUNT(DISTINCT *) AS distinct_rows FROM employees;


-- WITH RankedEmployees AS (
--   SELECT *, ROW_NUMBER() OVER (
--       PARTITION BY employee_id, employee_name, salary, hire_date, department 
--       ORDER BY employee_id
--   ) AS rn
--   FROM employees
-- )
-- DELETE FROM employees
-- USING RankedEmployees r
-- WHERE employees.employee_id = r.employee_id
--   AND r.rn > 1;



-- 3) Correcting structural issues

-- UPDATE employees
-- SET employee_name = INITCAP(employee_name);

-- UPDATE employees
-- SET 
--     employee_name = TRIM(employee_name),
--     department = TRIM(department);

-- UPDATE employees
-- SET department = UPPER(department)
-- WHERE department IS NOT NULL;

-- SELECT employee_id, hire_date
-- FROM employees
-- WHERE hire_date::TEXT !~ '^\d{4}-\d{2}-\d{2}$';



-- 4) Correct data types

-- Convert hire_date text to date in the query result
-- SELECT 
--     employee_id,
--     employee_name,
--     salary,
--     CAST(hire_date AS DATE) AS hire_date,
--     department
-- FROM employees;


-- Alter the column to correct DATE type (permanent schema change)
-- ALTER TABLE employees 
-- ALTER COLUMN hire_date TYPE DATE 
-- USING TO_DATE(hire_date, 'YYYY-MM-DD');



-- 5) Handling Outliers

-- Find salary outliers above $100,000
-- SELECT * 
-- FROM employees
-- WHERE salary > 100000;


-- Validate salary range between 0 and 100000
-- SELECT employee_id, salary 
-- FROM employees
-- WHERE salary < 0 OR salary > 100000;


-- Remove outlier records (example: salary > 100000)
-- DELETE FROM employees
-- WHERE salary > 100000;



-- 6) Standarising and normailizing data

-- Query names in Title Case without altering the table
-- SELECT employee_id, INITCAP(employee_name) AS employee_name_title_case, department
-- FROM employees;

-- Update names to Title Case in the table
-- UPDATE employees
-- SET employee_name = INITCAP(employee_name);

-- SELECT 
--   (salary - MIN(salary) OVER ()) / (MAX(salary) OVER () - MIN(salary) OVER ()) 
--   AS salary_normalized
-- FROM employees;




