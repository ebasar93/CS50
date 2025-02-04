-- In this SQL file, write (and comment!) the schema of your database, including the CREATE TABLE, CREATE INDEX, CREATE VIEW, etc. statements that compose it

CREATE TABLE users (
    "id" INTEGER,
    "user_name" TEXT NOT NULL UNIQUE ,
    "password" TEXT NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE days (
    "id" INTEGER,
    "user_id" INTEGER,
    "date" TEXT NOT NULL UNIQUE DEFAULT CURRENT_DATE   ,
    "note" TEXT ,
    PRIMARY KEY("id"),
    FOREIGN KEY("user_id") REFERENCES "users"("id")

);

CREATE TABLE exercises (
    "id" INTEGER,
    "user_id" INTEGER,
    "day_id" INTEGER,
    "burnt" INTEGER NOT NULL ,
    "name" TEXT NOT NULL,
    "duration" NUMERIC NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY("user_id") REFERENCES "users"("id"),
    FOREIGN KEY("day_id") REFERENCES "days"("id")
);

CREATE TABLE sleeps (
    "id" INTEGER,
    "user_id" INTEGER,
    "day_id" INTEGER,
    "start_time" NUMERIC NOT NULL,
    "end_time" NUMERIC NOT NULL,
    "score" INTEGER CHECK ("score" <= 100 AND "score" >= 0),
    PRIMARY KEY("id"),
    FOREIGN KEY("user_id") REFERENCES "users"("id"),
    FOREIGN KEY("day_id") REFERENCES "days"("id")
);


CREATE TABLE caloric_intakes (
    "id" INTEGER,
    "user_id" INTEGER,
    "day_id" INTEGER,
    "type" TEXT NOT NULL CHECK("type" IN ('breakfast', 'lunch', 'dinner', 'snacks', 'drinks')),
    "calories" INTEGER NOT NULL ,
    PRIMARY KEY("id"),
    FOREIGN KEY("user_id") REFERENCES "users"("id"),
    FOREIGN KEY("day_id") REFERENCES "days"("id")
);

CREATE INDEX "date_index" ON "days" ("date");

CREATE VIEW "total_calorie_intake" AS
SELECT  "date",TOTAL("calories") AS "calorie_total" FROM caloric_intakes
JOIN "days" ON "days"."id" = "caloric_intakes"."day_id"
GROUP BY "day_id";






