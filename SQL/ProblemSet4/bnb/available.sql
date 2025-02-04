CREATE VIEW "available" AS
SELECT listings."id", "property_type", "host_name", "accommodates", "date" FROM listings
INNER JOIN availabilities ON availabilities."listing_id" = listings."id"
WHERE "available" = 'TRUE';


