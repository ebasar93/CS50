CREATE TABLE ingredients (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "donut_id" INTEGER,
    "price" NUMERIC NULL CHECK("price" != 0),
    PRIMARY KEY ("id"),
    FOREIGN KEY ("donut_id") REFERENCES "donuts"("id")
);
CREATE TABLE donuts (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "type" TEXT NOT NULL CHECK ("type" IN ('Gluten Free', 'No')),
    "price" NUMERIC NULL CHECK("price" != 0),
    "order_id" INTEGER,
    PRIMARY KEY ("id"),
    FOREIGN KEY ("order_id") REFERENCES "orders"("id")
);
CREATE TABLE orders (
    "id" INTEGER,
    "order_number" INTEGER NOT NULL,
    "customer_id" INTEGER NOT NULL,
    "price" NUMERIC NULL CHECK("price" != 0),
    PRIMARY KEY ("id"),
    FOREIGN KEY ("customer_id") REFERENCES "customers"("id")
);
CREATE TABLE customers (
    "id" INTEGER,
    "first_name" INTEGER NOT NULL,
    "customer_id" INTEGER NOT NULL,
    "price" NUMERIC NULL CHECK("price" != 0),
    PRIMARY KEY ("id")
);
