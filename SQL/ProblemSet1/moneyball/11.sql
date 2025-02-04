SELECT "first_name", "last_name", "salary"/"performances"."H"  AS "dollars per hit" FROM players
LEFT JOIN performances ON "performances"."player_id" = "players"."id"
RIGHT JOIN salaries ON "salaries"."player_id" = "performances"."player_id" AND "performances"."year" = "salaries"."year"
WHERE "performances"."year" = 2001 AND "performances"."H" > 0
ORDER BY "dollars per hit"
LIMIT 10
;
