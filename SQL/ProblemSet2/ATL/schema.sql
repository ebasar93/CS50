CREATE TABLE passengers (
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "birth_day" NUMERIC NOT NULL,
    PRIMARY KEY("id")
);
CREATE TABLE check_in (
    "id" INTEGER,
    "passenger_id" INTEGER,
    "flight_id" INTEGER,
    "datetime" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY("id"),
    FOREIGN KEY("passenger_id") REFERENCES "passengers"("id"),
    FOREIGN KEY("flight_id") REFERENCES "flights"("id")
);
CREATE TABLE concourses (
    "id" INTEGER,
    "airline_id" TEXT NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY("airline_id") REFERENCES "airlines"("id")
);
CREATE TABLE airlines (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    PRIMARY KEY("id")
);
CREATE TABLE flights (
    "id" INTEGER,
    "flight_number" INTEGER,
    "code_departure" TEXT NOT NULL,
    "code_arrival" TEXT NOT NULL,
    "EDT" NUMERIC NOT NULL ,
    "EAT" NUMERIC NOT NULL,
    PRIMARY KEY("id")
);
