-- In this SQL file, write (and comment!) the typical SQL queries users will run on your database

-- Add new user
INSERT INTO users ( "user_name" , "password" )
VALUES("emir", "12341234");

-- Add new day
INSERT INTO days ("user_id")
VALUES(1);

-- Insert exercise to the database

INSERT INTO exercises ("user_id", "day_id", "burnt", "name" , "duration" )
VALUES(1,1,500, "run", "00:25:41");

-- Select the exercises which took more than thirty minutes

SELECT * from exercises where "duration" >= "00:30:00";

-- Insert new meal

INSERT INTO caloric_intakes ("user_id", "day_id","type", "calories")
VALUES
(1,1,"breakfast","500"),
(1,1,"lunch","700"),
(1,1,"dinner","1000")
;

-- Calories in given dates

SELECT * FROM total_calorie_intake WHERE "calorie_total" > 2000;

-- Calories in given dates where amount is larger than 2000

SELECT * FROM total_calorie_intake WHERE "calorie_total" > 2000;
