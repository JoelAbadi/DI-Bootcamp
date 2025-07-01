-- Exercise 2 : dvdrental database

--1
-- SELECT * FROM customer

--2
-- SELECT first_name ||' '|| last_name AS full_name FROM customer

--3
-- SELECT DISTINCT create_date FROM customer

--4
-- SELECT * FROM customer
-- ORDER BY first_name DESC

--5
-- SELECT film_id, title, description, release_year, rental_rate
-- FROM film
-- ORDER BY rental_rate ASC

--6
-- SELECT address, phone FROM address
-- WHERE district = 'Texas'

--7
-- SELECT * FROM film
-- WHERE film_id = 15 OR film_id = 150

--8
-- SELECT film_id, title, description, length, rental_rate FROM film
-- WHERE title = 'The Matrix'

--9
-- SELECT film_id, title, description, length, rental_rate FROM film
-- WHERE title LIKE ('Th%')

--10
-- SELECT * FROM film
-- ORDER BY rental_rate LIMIT(10)

--11
-- SELECT * FROM film
-- ORDER BY rental_rate
-- LIMIT(10)
-- OFFSET (10)

--12
-- SELECT
-- 	customer.customer_id,
--     customer.first_name,
--     customer.last_name,
--     payment.amount,
--     payment.payment_date
-- FROM customer
-- JOIN payment ON customer.customer_id = payment.customer_id
-- ORDER BY customer.customer_id ASC

--13
-- SELECT
-- film.film_id,
-- film.title
-- FROM film
-- LEFT JOIN inventory ON film.film_id = inventory.film_id
-- WHERE inventory.film_id IS NULL;


--14
-- SELECT
-- country.country_id,
-- country.country,
-- city.city
-- FROM country
-- JOIN city ON country.country_id = city.country_id
-- ORDER BY country.country, city.city

--15
-- SELECT
-- customer.customer_id,
-- customer.first_name || ' ' || customer.last_name AS name,
-- payment.amount,
-- payment.payment_date
-- FROM customer
-- JOIN payment ON customer.customer_id = payment.customer_id
-- ORDER BY payment.staff_id


 select * from customer