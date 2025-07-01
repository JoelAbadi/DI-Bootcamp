-- CREATE TABLE FirstTab (
--      id integer, 
--      name VARCHAR(10)
-- )

-- INSERT INTO FirstTab VALUES
-- (5,'Pawan'),
-- (6,'Sharlee'),
-- (7,'Krish'),
-- (NULL,'Avtaar')

-- SELECT * FROM FirstTab

-- CREATE TABLE SecondTab (id integer )

-- INSERT INTO SecondTab VALUES
-- (5),
-- (NULL)


-- SELECT * FROM SecondTab

-- Questions
-- Q1. What will be the OUTPUT of the following statement?

    -- SELECT COUNT(*) 
    -- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )

-- Explanation:
-- SELECT id FROM SecondTab WHERE id IS NULL returns NULL.

-- ft.id NOT IN (NULL) evaluates to UNKNOWN (i.e., NULL) for all rows.

-- WHERE clause with NULL excludes all rows.

-- No rows match.

-- Q2. What will be the OUTPUT of the following statement?

    -- SELECT COUNT(*) 
    -- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )

-- Explanation:
-- Subquery returns (5).

-- NOT IN (5) excludes only id = 5.

-- id = 6 and id = 7 match.

-- id = NULL is excluded.

-- 2 rows match.

-- Q3. What will be the OUTPUT of the following statement?

    -- SELECT COUNT(*) 
    -- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )

-- Explanation:
-- Subquery returns (5, NULL).

-- NOT IN with NULL results in UNKNOWN for all comparisons.

-- All rows filtered out due to NULL.

-- No rows match.

-- Q4. What will be the OUTPUT of the following statement?

--     SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )

-- Explanation:
-- Subquery returns (5).

-- NOT IN (5) excludes id = 5.

-- id = 6 and id = 7 match.

-- id = NULL is excluded.

-- 2 rows match.


