CREATE VIEW "frequently_reviewed" AS
SELECT "id", "property_type", "host_name", COUNT("review_id") as "reviews" FROM
    (SELECT listings."id", "property_type", "host_name", reviews.id as "review_id"  FROM listings
    JOIN reviews  ON reviews ."listing_id" = listings."id")
GROUP BY "id" ORDER BY "reviews" DESC, "host_name" Limit 100;
