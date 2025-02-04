CREATE  VIEW "am" AS
SELECT listings."id", "property_type", "host_name", reviews.id as "review_id"  FROM listings
JOIN reviews  ON reviews ."listing_id" = listings."id";

CREATE VIEW "frequently_reviewed" AS
SELECT "id", "property_type", "host_name", COUNT("review_id") as "reviews" FROM am GROUP BY "id" ORDER BY "reviews" DESC, "host_name" Limit 100;


CREATE VIEW got AS
SELECT listings."id", "property_type", "host_name", "date" FROM listings
JOIN availabilities ON availabilities."listing_id" = listings."id"
WHERE "date" BETWEEN '2023-06-01' AND '2023-06-30';

CREATE  VIEW "june_vacancies" AS
SELECT "id", "property_type", "host_name", COUNT("date") as "days_vacant" FROM got GROUP BY "id";


