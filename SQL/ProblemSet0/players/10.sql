SELECT "first_name", "last_name", "height", "weight" AS "weight" FROM players WHERE "height" >
(SELECT AVG("height") FROM players) AND "weight" >  (SELECT AVG("weight") FROM players )
ORDER BY "height", "first_name", "last_name";
