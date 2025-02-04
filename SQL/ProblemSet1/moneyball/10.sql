--SELECT "first_name", "last_name", "salary", "salaries"."year", "performances"."HR" FROM players
--LEFT JOIN performances ON "performances"."player_id" = "players"."id"
--RIGHT JOIN salaries ON "salaries"."player_id" = "performances"."player_id" AND "performances"."year" = "salaries"."year"
--LIMIT 10;


SELECT "first_name", "last_name", "salary", "salaries"."year", "performances"."HR" FROM players
LEFT JOIN salaries ON "salaries"."player_id" = "players"."id"
LEFT JOIN performances ON "performances"."player_id" = "salaries"."player_id" AND "performances"."year" = "salaries"."year"
WHERE "salary" IS NOT NULL OR "HR" IS NOT NULL
LIMIT 10;
