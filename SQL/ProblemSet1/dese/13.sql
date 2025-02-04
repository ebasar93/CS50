SELECT "name","per_pupil_expenditure", "exemplary"  FROM districts
NATURAL JOIN expenditures
NATURAL JOIN staff_evaluations
WHERE "exemplary" > (SELECT AVG("exemplary") FROM staff_evaluations)
AND "per_pupil_expenditure" > (SELECT AVG("per_pupil_expenditure") FROM expenditures)
ORDER BY "exemplary" DESC, "per_pupil_expenditure"
;
