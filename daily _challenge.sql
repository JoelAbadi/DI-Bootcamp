-- Database: hollywood

-- DROP DATABASE IF EXISTS hollywood;

-- CREATE DATABASE hollywood
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_United States.1252'
--     LC_CTYPE = 'English_United States.1252'
--     LOCALE_PROVIDER = 'libc'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- CREATE TABLE actors(
--  actor_id SERIAL PRIMARY KEY,
--  first_name VARCHAR (50) NOT NULL,
--  last_name VARCHAR (100) NOT NULL,
--  age DATE NOT NULL,
--  number_oscars SMALLINT NOT NULL
-- )

-- SELECT * FROM actors

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES
-- ('Matt','Damon','08/10/1970', 5)

-- SELECT * FROM actors


-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES
-- ('Gal','Gadot','30/04/1985', 2),
-- ('Miley','Cyrus','18/12/1995', 2)

-- SELECT * FROM  actors

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES
-- ('Angelina','Jolie','06/09/1973', 5),
-- ('Meryl','Streep','03/11/1962', 12)

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES
-- ('Michael','Jordan','06/09/1973', 6),
-- ('Lebron','James','06/10/1982', 12),
-- ('Megan','Fox','03/11/1961', 1)

-- SELECT * FROM actors

-- SELECT first_name, last_name FROM actors WHERE first_name = 'Matt'  AND 
-- last_name = 'Damon' ;

-- SELECT * FROM actors WHERE age > '1960-01-01' ORDER BY first_name ASC

-- SELECT * FROM actors LIMIT 4;

-- SELECT * FROM actors
-- ORDER BY last_name DESC
-- LIMIT 4;

-- SELECT first_name FROM actors WHERE first_name LIKE 'e%'

-- SELECT * FROM actors WHERE number_oscars > 5;

-- Daily Challenge
-- 1) 
-- SELECT COUNT(*) FROM actors;
-- 2)
-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES
-- ('Larry','Bird','06/09/1963',NULL )









