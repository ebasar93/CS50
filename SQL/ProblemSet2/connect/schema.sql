CREATE TABLE users (
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "user_name" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    PRIMARY KEY("id")
);
CREATE TABLE schools (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "type" TEXT NOT NULL,
    "location" TEXT NOT NULL,
    "year" INTEGER NOT NULL,
    PRIMARY KEY("id")
);
CREATE TABLE companies (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "type" TEXT NOT NULL,
    "location" TEXT NOT NULL,
    PRIMARY KEY("id")
);
CREATE TABLE connections_users (
    "id" INTEGER,
    "user1_id" INTEGER NOT NULL,
    "user2_id" INTEGER NOT NULL,
    PRIMARY KEY("id")
);
CREATE TABLE connections_schools (
    "id" INTEGER,
    "user_id" TEXT NOT NULL,
    "school_id" TEXT NOT NULL,
    "start_date" NUMERIC NOT NULL,
    "end_date" NUMERIC NOT NULL,
    "type" TEXT NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY ("user_id") REFERENCES "users"("id"),
    FOREIGN KEY ("school_id") REFERENCES "schools"("id")
);
CREATE TABLE connections_companies (
    "id" INTEGER,
    "user_id" TEXT NOT NULL,
    "company_id" TEXT NOT NULL,
    "start_date" NUMERIC NOT NULL,
    "end_date" NUMERIC NOT NULL,
    "title" TEXT NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY ("user_id") REFERENCES "users"("id"),
    FOREIGN KEY ("company_id") REFERENCES "companies"("id")
);
