CREATE TABLE "meteorites" (
    "name",
    "id" INTEGER,
    "nametype",
    "class",
    "mass",
    "discovery",
    "year",
    "lat",
    "long",
    PRIMARY KEY ("id")
);

CREATE TABLE "got" (
    "name",
    "id",
    "nametype",
    "class",
    "mass",
    "discovery",
    "year",
    "lat",
    "long"
);

.import --csv --skip 3 meteorites.csv got

DELETE FROM GOT WHERE "nametype" = 'Relict';
UPDATE got
SET "lat" = NULL
WHERE "lat" = '0.0' OR "lat" = '';
UPDATE got
SET "long" = NULL
WHERE "long" = '0.0' OR "long" = '';
UPDATE got
SET "year" = NULL
WHERE "year" = '0.0' OR "year" = '';
UPDATE got
SET "mass" = NULL
WHERE "mass" = '0.0' OR "mass" = '';
ALTER TABLE got
ADD COLUMN "lat2" NUMERIC;
ALTER TABLE got
ADD COLUMN "long2" NUMERIC;
ALTER TABLE got
ADD COLUMN "year2" NUMERIC;
UPDATE got
SET "long2" = ROUND("long",2);
UPDATE got
SET "lat2" = ROUND("lat",2);
UPDATE got
SET "year2" = ROUND("year",0);

INSERT INTO "meteorites" (    "name",
    "nametype",
    "class",
    "mass",
    "discovery",
    "year",
    "lat",
    "long")
    SELECT    "name",
    "nametype",
    "class",
    "mass",
    "discovery",
    "year",
    "lat2",
    "long2"
    FROM got
    ORDER BY "year", "name"
    ;

    ALTER TABLE meteorites
    DROP "nametype";



