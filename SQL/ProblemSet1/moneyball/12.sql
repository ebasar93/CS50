CREATE TABLE AM AS
SELECT  "first_name", "last_name" FROM players
LEFT JOIN performances ON "performances"."player_id" = "players"."id"
RIGHT JOIN salaries ON "salaries"."player_id" = "performances"."player_id" AND "performances"."year" = "salaries"."year"
WHERE "performances"."year" = 2001 AND "performances"."H" > 0
ORDER BY "salary"/"performances"."H"
LIMIT 10
CREATE TABLE GOT AS
SELECT  "first_name", "last_name" FROM players
LEFT JOIN performances ON "performances"."player_id" = "players"."id"
RIGHT JOIN salaries ON "salaries"."player_id" = "performances"."player_id" AND "performances"."year" = "salaries"."year"
WHERE "performances"."year" = 2001 AND "performances"."RBI" > 0
ORDER BY "salary"/"performances"."RBI"
LIMIT 10
SELECT "first_name", "last_name" FROM AM
INTERSECT
SELECT "first_name", "last_name" FROM GOT
;
