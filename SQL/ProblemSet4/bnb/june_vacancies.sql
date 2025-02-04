CREATE  VIEW "june_vacancies" AS
SELECT "id" , "property_type", "host_name", COUNT("date") as "days_vacant" FROM
    (SELECT listings."id", "property_type", "host_name", "date" FROM listings
    JOIN availabilities ON availabilities."listing_id" = listings."id"
    WHERE "date" BETWEEN '2023-06-01' AND '2023-06-30'
    AND "available" = 'TRUE' )
GROUP BY "id";

