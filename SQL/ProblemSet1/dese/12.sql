
SELECT "name", "per_pupil_expenditure", "exemplary" FROM districts
INNER JOIN staff_evaluations ON "staff_evaluations"."district_id" = "districts"."id"
INNER JOIN expenditures ON "expenditures"."district_id" = "staff_evaluations"."district_id"
WHERE "exemplary" > (SELECT AVG("exemplary") FROM staff_evaluations)
AND "per_pupil_expenditure" > (SELECT AVG("per_pupil_expenditure") FROM expenditures)
ORDER BY "exemplary" DESC, "per_pupil_expenditure" DESC
;
