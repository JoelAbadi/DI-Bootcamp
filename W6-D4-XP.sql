---- Exercise 1

-- SELECT m.medal_name AS Medal_Type,
--        ROUND(AVG(gc.age), 2) AS Average_Age
-- FROM olympics.games_competitor gc
-- JOIN olympics.competitor_event ce 
--   ON gc.id = ce.competitor_id
-- JOIN olympics.medal m 
--   ON ce.medal_id = m.id
-- WHERE ce.medal_id != 4
-- GROUP BY m.medal_name;


-- SELECT nr.region_name AS Region,
--        COUNT(DISTINCT pr.person_id) AS Competitor_Count
-- FROM olympics.person_region pr
-- JOIN olympics.noc_region nr 
--   ON pr.region_id = nr.id
-- WHERE pr.person_id IN (
--     SELECT gc.person_id
--     FROM olympics.games_competitor gc
--     JOIN olympics.competitor_event ce 
--       ON gc.id = ce.competitor_id
--     GROUP BY gc.person_id
--     HAVING COUNT(DISTINCT ce.event_id) > 3
-- )
-- GROUP BY nr.region_name
-- ORDER BY Competitor_Count DESC
-- LIMIT 5;


-- -- Create a temporary table with total medals per competitor
-- CREATE TEMPORARY TABLE CompetitorMedals AS
-- SELECT gc.id AS competitor_id,
--        (SELECT COUNT(*) 
--         FROM olympics.competitor_event ce2 
--         WHERE ce2.competitor_id = gc.id 
--           AND ce2.medal_id != 4) AS total_medals
-- FROM olympics.games_competitor gc;

-- -- Query the temporary table for competitors with more than 2 medals
-- SELECT competitor_id, total_medals
-- FROM CompetitorMedals
-- WHERE total_medals > 2
-- ORDER BY competitor_id
-- LIMIT 5;


-- -- Delete competitors with no medals from the temporary table
-- DELETE FROM CompetitorMedals
-- WHERE competitor_id NOT IN (
--     SELECT competitor_id 
--     FROM olympics.competitor_event 
--     WHERE medal_id != 4
-- );

-- -- Verify that only medal-winning competitors remain
-- SELECT COUNT(*) AS remaining_competitors,
--        MIN(total_medals) AS min_total_medals,
--        MAX(total_medals) AS max_total_medals
-- FROM CompetitorMedals;





-- -- Exercise 2
-- UPDATE person
-- SET height = (
--     SELECT ROUND(AVG(p2.height), 0)
--     FROM person p2
--     JOIN person_region pr2 ON p2.id = pr2.person_id
--     WHERE pr2.region_id = (
--         SELECT pr.region_id FROM person_region pr WHERE pr.person_id = person.id LIMIT 1
--     ) AND p2.height > 0
-- )
-- WHERE height = 0;



-- CREATE TEMP TABLE multi_event_competitors AS
-- SELECT gc.person_id, gc.games_id, COUNT(DISTINCT ce.event_id) AS total_events
-- FROM games_competitor gc
-- JOIN competitor_event ce ON gc.id = ce.competitor_id
-- GROUP BY gc.person_id, gc.games_id
-- HAVING COUNT(DISTINCT ce.event_id) > 1;


-- SELECT nr.region_name,
--        ROUND(AVG(medal_count), 2) AS region_avg
-- FROM (
--     SELECT pr.region_id, gc.person_id,
--            COUNT(*) FILTER (WHERE ce.medal_id != 4) AS medal_count
--     FROM person_region pr
--     JOIN games_competitor gc ON pr.person_id = gc.person_id
--     JOIN competitor_event ce ON ce.competitor_id = gc.id
--     GROUP BY pr.region_id, gc.person_id
-- ) sub
-- JOIN noc_region nr ON sub.region_id = nr.id
-- GROUP BY nr.region_name
-- HAVING AVG(medal_count) > (
--     SELECT AVG(total_medals) FROM (
--         SELECT gc.person_id, COUNT(*) FILTER (WHERE ce.medal_id != 4) AS total_medals
--         FROM games_competitor gc
--         JOIN competitor_event ce ON gc.id = ce.competitor_id
--         GROUP BY gc.person_id
--     ) avg_all
-- );



-- CREATE TEMP TABLE seasonal_participation AS
-- SELECT gc.person_id,
--        COUNT(DISTINCT g.season) AS season_count
-- FROM games_competitor gc
-- JOIN games g ON gc.games_id = g.id
-- GROUP BY gc.person_id
-- HAVING COUNT(DISTINCT g.season) = 2;


