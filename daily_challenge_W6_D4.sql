-- Daily Challenge

-- Task 1

-- CREATE TEMP TABLE seasonal_medals AS
-- SELECT gc.person_id,
--        g.season,
--        COUNT(*) AS medal_count
-- FROM "07_games_competitor" gc
-- JOIN "08_competitor_event" ce ON gc.id = ce.competitor_id
-- JOIN "02_games" g ON gc.games_id = g.id
-- WHERE ce.medal_id != 4
-- GROUP BY gc.person_id, g.season;

-- CREATE TEMP TABLE dual_season_medalists AS
-- SELECT person_id
-- FROM seasonal_medals
-- GROUP BY person_id
-- HAVING COUNT(DISTINCT season) = 2;

-- SELECT sm.person_id,
--        MAX(CASE WHEN season = 'Summer' THEN medal_count ELSE 0 END) AS summer_medals,
--        MAX(CASE WHEN season = 'Winter' THEN medal_count ELSE 0 END) AS winter_medals
-- FROM seasonal_medals sm
-- JOIN dual_season_medalists dm ON sm.person_id = dm.person_id
-- GROUP BY sm.person_id;


-- CREATE TEMP TABLE two_sport_medalists AS
-- SELECT gc.person_id,
--        COUNT(DISTINCT e.sport_id) AS sports_count,
--        COUNT(*) AS total_medals
-- FROM games_competitor gc
-- JOIN competitor_event ce ON gc.id = ce.competitor_id
-- JOIN event e ON ce.event_id = e.id
-- WHERE ce.medal_id != 4
-- GROUP BY gc.person_id
-- HAVING COUNT(DISTINCT e.sport_id) = 2;

-- -- Top 3 by total medals
-- SELECT person_id, sports_count, total_medals
-- FROM two_sport_medalists
-- ORDER BY total_medals DESC
-- LIMIT 3;



-- Task 2

-- WITH event_medals AS (
--   SELECT gc.person_id, ce.event_id, COUNT(*) AS medal_count
--   FROM games_competitor gc
--   JOIN competitor_event ce ON gc.id = ce.competitor_id
--   WHERE ce.medal_id != 4
--   GROUP BY gc.person_id, ce.event_id
-- ),
-- top_event_per_person AS (
--   SELECT person_id, MAX(medal_count) AS top_event_medals
--   FROM event_medals
--   GROUP BY person_id
-- ),
-- region_aggregate AS (
--   SELECT pr.region_id, SUM(te.top_event_medals) AS total_top_medals
--   FROM top_event_per_person te
--   JOIN person_region pr ON te.person_id = pr.person_id
--   GROUP BY pr.region_id
-- )
-- SELECT nr.region_name, total_top_medals
-- FROM region_aggregate ra
-- JOIN noc_region nr ON ra.region_id = nr.id
-- ORDER BY total_top_medals DESC
-- LIMIT 5;



-- CREATE TEMP TABLE no_medal_long_competitors AS
-- SELECT gc.person_id, COUNT(DISTINCT gc.games_id) AS games_participated
-- FROM games_competitor gc
-- LEFT JOIN competitor_event ce ON gc.id = ce.competitor_id AND ce.medal_id != 4
-- WHERE ce.medal_id IS NULL
-- GROUP BY gc.person_id
-- HAVING COUNT(DISTINCT gc.games_id) > 3;

-- -- Get names
-- SELECT nl.person_id, p.full_name, nl.games_participated
-- FROM no_medal_long_competitors nl
-- JOIN person p ON nl.person_id = p.id;

