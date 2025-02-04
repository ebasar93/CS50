SELECT "city", COUNT("type") FROM schools WHERE "type" = 'Public School' GROUP BY "city" HAVING COUNT("type") <= 3 ORDER BY COUNT("type") DESC, "city" ;



--SELECT "city", COUNT("type") FROM schools GROUP BY "city" HAVING "type" = 'Public School' AND COUNT("type") <= 3 ORDER BY COUNT("type") DESC, "name"  ;
