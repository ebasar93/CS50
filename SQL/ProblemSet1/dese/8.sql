SELECT "name", "pupils" FROM expenditures LEFT JOIN districts ON "districts"."id" = "expenditures"."district_id";
