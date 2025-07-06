-- Exercise 1

-- CREATE TABLE df_employee AS
-- SELECT 
--     s.employee_id || '_' || CAST(s.date AS TEXT) AS id,
--     DATE(s.date) AS month_year,
--     s.employee_id,
--     e.employee_name,
--     e."GEN(M_F)" AS gender,
--     e.age,
--     s.salary,
--     f.function_group,
--     c.company_name,
--     c.company_city,
--     c.company_state,
--     c.company_type,
--     c.const_site_category
-- FROM salaries s
-- LEFT JOIN employees e ON s.employee_id = e.employee_code_emp
-- LEFT JOIN functions f ON s.func_code = f.function_code
-- LEFT JOIN companies c ON s.comp_name = c.company_name;

-- Exercise 2

-- 2.1) Trim text columns

-- UPDATE df_employee
-- SET 
--     id = TRIM(id),
--     employee_id = TRIM(employee_id),
--     employee_name = TRIM(employee_name),
--     gender = TRIM(gender),
--     function_group = TRIM(function_group),
--     company_name = TRIM(company_name),
--     company_city = TRIM(company_city),
--     company_state = TRIM(company_state),
--     company_type = TRIM(company_type),
--     const_site_category = TRIM(const_site_category);



-- 2.2) Check for NULL values

-- SELECT * FROM df_employee
-- WHERE id IS NULL
--    OR month_year IS NULL
--    OR employee_id IS NULL
--    OR employee_name IS NULL
--    OR gender IS NULL
--    OR age IS NULL
--    OR salary IS NULL
--    OR function_group IS NULL
--    OR company_name IS NULL
--    OR company_city IS NULL
--    OR company_state IS NULL
--    OR company_type IS NULL
--    OR const_site_category IS NULL;



-- 2.3) Delete rows with missing salary

-- DELETE FROM df_employee
-- WHERE salary IS NULL OR TRIM(salary::TEXT) = '';



-- Exercise 3

-- Current employee count

-- SELECT company_name,
--        COUNT(DISTINCT employee_id) AS current_employee_count
-- FROM df_employee
-- WHERE month_year = (SELECT MAX(month_year) FROM df_employee)
-- GROUP BY company_name
-- ORDER BY current_employee_count DESC;



-- Exercise 4

-- 4.1) total number of employees each city

-- SELECT company_city,
--        COUNT(DISTINCT employee_id) AS num_employees,
--        ROUND(COUNT(DISTINCT employee_id) * 100.0 / 
--            (SELECT COUNT(DISTINCT employee_id) 
--             FROM df_employee 
--             WHERE month_year = (SELECT MAX(month_year) FROM df_employee)), 2) AS percent_of_total
-- FROM df_employee
-- WHERE month_year = (SELECT MAX(month_year) FROM df_employee)
-- GROUP BY company_city
-- ORDER BY num_employees DESC;



-- 4.2) total number of employees each month

-- SELECT month_year,
--        COUNT(DISTINCT employee_id) AS total_employees
-- FROM df_employee
-- GROUP BY month_year
-- ORDER BY month_year;


-- 4.3) average number of employees each month

-- SELECT ROUND(AVG(month_count), 2) AS avg_employees_per_month
-- FROM (
--     SELECT month_year, COUNT(DISTINCT employee_id) AS month_count
--     FROM df_employee
--     GROUP BY month_year
-- ) sub;



-- Exercsie 5

-- 5.1) minimum and maximum number of employees throughout all the months

-- WITH month_counts AS (
--     SELECT month_year, COUNT(DISTINCT employee_id) AS cnt
--     FROM df_employee
--     GROUP BY month_year
-- )
-- SELECT * FROM month_counts
-- WHERE cnt = (SELECT MIN(cnt) FROM month_counts)
--    OR cnt = (SELECT MAX(cnt) FROM month_counts);



-- 5.2) monthly average number of employees by function group

-- WITH monthly_func_counts AS (
--     SELECT function_group, month_year, COUNT(DISTINCT employee_id) AS cnt
--     FROM df_employee
--     GROUP BY function_group, month_year
-- )
-- SELECT function_group,
--        ROUND(AVG(cnt), 2) AS avg_employees_per_month
-- FROM monthly_func_counts
-- GROUP BY function_group
-- ORDER BY avg_employees_per_month DESC;


-- 5.3) annual average salary

-- SELECT EXTRACT(YEAR FROM month_year) AS year,
--        ROUND(AVG(salary), 2) AS average_salary
-- FROM df_employee
-- GROUP BY year
-- ORDER BY year;
