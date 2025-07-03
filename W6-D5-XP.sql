-- Exercise 1: Movie Rankings and Analysis

-- SELECT 
--   g.genre_name AS genre,
--   m.title AS movie_title,
--   RANK() OVER (PARTITION BY g.genre_name ORDER BY m.popularity DESC) AS popularity_rank
-- FROM movie m
-- JOIN movie_genres mg ON m.movie_id = mg.movie_id
-- JOIN genre g ON mg.genre_id = g.genre_id;

-- SELECT 
--   title,
--   popularity,
--   NTILE(4) OVER (ORDER BY popularity DESC) AS quartile
-- FROM movie;

-- SELECT
--   g.genre_name AS genre,
--   m.title AS movie_title,
--   m.release_date
-- FROM movie m
-- JOIN movie_genres mg ON m.movie_id = mg.movie_id
-- JOIN genre g ON mg.genre_id = g.genre_id
-- WHERE (mg.genre_id, m.release_date) IN (
--   SELECT 
--     mg2.genre_id,
--     MIN(m2.release_date)
--   FROM movie m2
--   JOIN movie_genres mg2 ON m2.movie_id = mg2.movie_id
--   GROUP BY mg2.genre_id
-- );


-- SELECT 
--   pc.company_name,
--   m.title AS movie_title,
--   m.release_date
-- FROM movie m
-- JOIN movie_company mc ON m.movie_id = mc.movie_id
-- JOIN production_company pc ON mc.company_id = pc.company_id
-- WHERE (mc.company_id, m.release_date) IN (
--   SELECT 
--     mc2.company_id,
--     MIN(m2.release_date)
--   FROM movie m2
--   JOIN movie_company mc2 ON m2.movie_id = mc2.movie_id
--   GROUP BY mc2.company_id
-- );




-- Exercise 2: Cast and Crew Performance Analysis

-- SELECT 
--     person_name,
--     movie_count,
--     DENSE_RANK() OVER (ORDER BY movie_count DESC) AS rank
-- FROM (
--     SELECT 
--         p.person_name,
--         COUNT(DISTINCT mc.movie_id) AS movie_count
--     FROM 
--         movie_cast mc
--     JOIN 
--         person p ON mc.person_id = p.person_id
--     GROUP BY 
--         p.person_name
-- ) AS actor_counts
-- LIMIT 10;



-- SELECT * FROM movie LIMIT 5;

-- WITH director_avg_rating AS (
--     SELECT 
--         p.person_name,
--         AVG(m.vote_average) AS avg_rating
--     FROM 
--         movie_crew mc
--     JOIN 
--         person p ON mc.person_id = p.person_id
--     JOIN 
--         movie m ON mc.movie_id = m.movie_id
--     WHERE 
--         mc.job = 'Director'
--         AND m.vote_average IS NOT NULL
--     GROUP BY 
--         p.person_name
-- )

-- SELECT 
--     person_name,
--     avg_rating,
--     RANK() OVER (ORDER BY avg_rating DESC) AS rank
-- FROM 
--     director_avg_rating
-- LIMIT 10;


-- WITH genre_avg_revenue AS (
--     SELECT 
--         g.genre_name,
--         AVG(m.revenue) AS avg_revenue
--     FROM 
--         movie m
--     JOIN 
--         movie_genres mg ON m.movie_id = mg.movie_id
--     JOIN 
--         genre g ON mg.genre_id = g.genre_id
--     WHERE 
--         m.revenue IS NOT NULL
--     GROUP BY 
--         g.genre_name
-- )

-- SELECT 
--     genre_name,
--     avg_revenue,
--     RANK() OVER (ORDER BY avg_revenue DESC) AS rank
-- FROM 
--     genre_avg_revenue
-- LIMIT 10;

-- SELECT 
--     p.person_name AS actor_name,
--     SUM(m.revenue) AS total_revenue
-- FROM 
--     movie_cast mc
-- JOIN 
--     person p ON mc.person_id = p.person_id
-- JOIN 
--     movie m ON mc.movie_id = m.movie_id
-- WHERE 
--     m.revenue IS NOT NULL
-- GROUP BY 
--     p.person_name
-- ORDER BY 
--     total_revenue DESC
-- LIMIT 10;


WITH director_budgets AS (
    SELECT 
        p.person_name AS director_name,
        SUM(m.budget) AS total_budget
    FROM 
        movie_crew mc
    JOIN 
        person p ON mc.person_id = p.person_id
    JOIN 
        movie m ON mc.movie_id = m.movie_id
    WHERE 
        mc.job = 'Director'
        AND m.budget IS NOT NULL
    GROUP BY 
        p.person_name
),
ranked_directors AS (
    SELECT 
        director_name,
        total_budget,
        RANK() OVER (ORDER BY total_budget DESC) AS rank
    FROM 
        director_budgets
)
SELECT 
    director_name,
    total_budget
FROM 
    ranked_directors
WHERE 
    rank = 1;




