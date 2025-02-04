
-- *** The Lost Letter ***

-- id of Package and to address id
SELECT "id", "to_address_id"FROM "packages" WHERE "from_address_id" = (
    SELECT "id" FROM "addresses" WHERE "address" = "900 Somerville Avenue")
    AND "contents" LIKE "%letter";
-- sent address of package
SELECT "type", "address" FROM "addresses" WHERE "id" = (
    SELECT "to_address_id"FROM "packages" WHERE "from_address_id" = (
        SELECT "id" FROM "addresses" WHERE "address" = "900 Somerville Avenue")
        AND "contents" LIKE "%letter" );
-- package id of scans table 384,
SELECT * FROM scans WHERE "package_id" = (
    SELECT "id" FROM "packages" WHERE "from_address_id" = (
        SELECT "id" FROM "addresses" WHERE "address" = "900 Somerville Avenue")
    AND "contents" LIKE "%letter"
);
-- Pick up address correct
SELECT "address" FROM addresses WHERE "id" = 432;
-- Drop address
SELECT "address" FROM addresses WHERE "id" = 854;
-- *** The Devious Delivery ***
SELECT * FROM packages WHERE "from_address_id" IS NULL;
SELECT * FROM scans WHERE "package_id" = 5098;
SELECT * FROM addresses WHERE "id" = 348 OR "id" = 50;

-- *** The Forgotten Gift ***
SELECT "id", "address" FROM addresses WHERE "address" = "728 Maple Place" OR "address" = "109 Tileston Street";
-- 4983 , 9873
SELECT * FROM scans WHERE address_id IN (
    SELECT "id" FROM addresses WHERE "address" = "728 Maple Place" OR "address" = "109 Tileston Street"
    );
-- 10432 scan id
SELECT * FROM scans WHERE id = 10432;
-- 9523 package id
SELECT * FROM packages WHERE id = 9523;

SELECT * FROM scans WHERE package_id = 9523;
-- 7432 drop address_id
SELECT "id", "address" FROM addresses WHERE "id" = 7432;

-- *** The Forgotten Gift ***
SELECT * FROM addresses WHERE "address" = "728 Maple Place" OR "address" = "109 Tileston Street";
-- 4983 , 9873
SELECT * FROM packages WHERE "from_address_id" = 9873 ;
SELECT * FROM drivers WHERE "id" = 17 ;
