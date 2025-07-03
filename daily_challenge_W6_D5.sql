-- Task 1: Average Budget Growth Rate per Production Company

-- Calculate per-movie budget growth using LAG, then average per company

-- Average Budget Growth Rate per Company (fixed version)

-- WITH company_budgets AS (
--     SELECT 
--         pc.company_name,
--         m.budget,
--         LAG(m.budget) OVER (
--             PARTITION BY pc.company_name 
--             ORDER BY m.release_date
--         ) AS prev_budget
--     FROM movie AS m
--     JOIN movie_company AS mc 
--       ON m.movie_id = mc.movie_id
--     JOIN production_company AS pc 
--       ON mc.company_id = pc.company_id
-- ),
-- growth_rates AS (
--     SELECT 
--         company_name,
--         (budget - prev_budget) * 1.0 / prev_budget AS growth_rate
--     FROM company_budgets
--     WHERE prev_budget IS NOT NULL AND prev_budget <> 0
-- )
-- SELECT 
--     company_name,
--     AVG(growth_rate) AS avg_growth_rate
-- FROM growth_rates
-- GROUP BY company_name
-- ORDER BY avg_growth_rate DESC;



-- WITH avg_rating AS (
--     SELECT AVG(vote_average) AS avg_rating 
--     FROM movie
-- ),
-- above_avg_movies AS (
--     SELECT m.movie_id
--     FROM movie m
--     JOIN avg_rating ar ON TRUE
--     WHERE m.vote_average > ar.avg_rating
-- ),
-- actor_counts AS (
--     SELECT 
--         mc.person_id,
--         COUNT(*) AS high_rated_movie_count
--     FROM movie_cast mc
--     JOIN above_avg_movies aam ON mc.movie_id = aam.movie_id
--     GROUP BY mc.person_id
-- ),
-- top_actor AS (
--     SELECT 
--         person_id,
--         high_rated_movie_count,
--         RANK() OVER (ORDER BY high_rated_movie_count DESC) AS rnk
--     FROM actor_counts
-- )
-- SELECT 
--     p.person_name,
--     ta.high_rated_movie_count
-- FROM top_actor ta
-- JOIN person p ON ta.person_id = p.person_id
-- WHERE rnk = 1;


-- SELECT 
--     g.genre_name,
--     m.title,
--     m.release_date,
--     m.revenue,
--     ROUND(
--         AVG(m.revenue) OVER (
--             PARTITION BY g.genre_name
--             ORDER BY m.release_date
--             ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
--         ), 2
--     ) AS rolling_avg_revenue
-- FROM movie m
-- JOIN movie_genres mg ON m.movie_id = mg.movie_id
-- JOIN genre g ON mg.genre_id = g.genre_id
-- ORDER BY g.genre_name, m.release_date;


-- SELECT 
--     pc.company_name,
--     SUM(m.revenue) AS total_revenue
-- FROM movie m
-- JOIN movie_company mc ON m.movie_id = mc.movie_id
-- JOIN production_company pc ON mc.company_id = pc.company_id
-- GROUP BY pc.company_name
-- ORDER BY total_revenue DESC
-- LIMIT 1;


SELECT 
    g.genre_name,
    SUM(m.revenue) AS total_revenue
FROM movie m
JOIN movie_genres mg ON m.movie_id = mg.movie_id
JOIN genre g ON mg.genre_id = g.genre_id
GROUP BY g.genre_name
ORDER BY total_revenue DESC
LIMIT 1;








