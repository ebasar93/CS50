CREATE VIEW "by_district" AS
SELECT "district", TOTAL("families") AS "families" ,TOTAL("households") AS "households",
TOTAL("population") AS "population" ,TOTAL("male") AS "male" ,TOTAL("female") AS "female"  FROM census
GROUP BY "district";
