SELECT "name", SUM("H") FROM performances
INNER JOIN teams ON "teams"."id" = "performances"."team_id"
WHERE "performances"."year" = 2001
GROUP BY "team_id"
ORDER BY SUM("H") DESC
LIMIT 5
;

