# HEALTH TRACKER

By EMIR BASAR
Kyrenia/Cyprus

Video overview: <https://youtu.be/6aClqkpOAAI>

## Scope

The purpose of this is to search through, analyze and make deductions about a users` daily routine from data acquired.
The database will include sleep, exercise and nutrition logs of the user and will enable queryies through these activities: number of days where the users' caloric intake was above the 2000kcal.

 Additionally, using this database one can connect one or more of these activities ; number of mondays where the user slept less than 6 hours and exercised less than 30 minutes. It is hoped that the user will be able to identify their routines and habits thus make changes to enhance their daily lives.

To summarize the database consists of;
- users log-in information
- date information,
- sleep data of the users; sleep score, start and finish time,
- exercise data; calories burned, duration, exercise name
- caloric intake of the user

Other vital features such as water & cafeine intake, stress levels, monthly cycle etc are omitted in this database.

## Functional Requirements

This database will support.

- CRUD operations for the user.
- monitoring sleep, exercise and daily caloric intake of users for a given date.
- tracking one or more types of data and their relations to each other.
- A day can be associated with multiple sleep, caloric intake and exercise data.


## Representation

### Entities

#### Users

The `users` table includes:

* `id`, which specifies the unique ID for the user as an `INTEGER`. This column thus has the `PRIMARY KEY` constraint applied.
* `user_name`, which specifies the user's user name as `TEXT`, given `TEXT` is appropriate for name fields.A `UNIQUE` constraint ensures no two students have the same username.
* `password`, which specifies the user's password as `TEXT`, given `TEXT` is appropriate for name fields.

#### Days

The `days` table includes:

* `id`, which specifies the unique ID for the day as an `INTEGER`. This column thus has the `PRIMARY KEY` constraint applied.
* `user_id`, which specifies the unique ID for the user who experienced the day, as an `INTEGER`. This column thus has the `FOREIGN KEY` constraint applied, referencing the `id` column in the `users` table to ensure data integrity.
* `date`, which specifies the actual date as `NUMERIC`, which is unique and in `YYYY-MM-DD` format.
* `note`, which specifies the notes the user want to add to the day with, `TEXT`'.

`note` column is not required to be available.

#### Exercises

The `exercises` table includes:

* `id`, which specifies the unique ID for the exercise as an `INTEGER`. This column thus has the `PRIMARY KEY` constraint applied.
* `user_id`, which specifies the unique ID for the user who did the exercise as an `INTEGER`. This column thus has the `FOREIGN KEY` constraint applied, referencing the `id` column in the `users` table to ensure data integrity.
* `day_id`, which specifies the unique ID for the date which the exercise was undertaken, as an `INTEGER`. This column thus has the `FOREIGN KEY` constraint applied, referencing the `id` column in the `days` table to ensure data integrity.
* `burnt`, which specifies the amount of calories burnt in the exercise as `INTEGER`.
* `name`, which specifies the name of the exercise as `TEXT`.
* `duration`, whick specifies the duration of the exercise as `NUMERIC` in an `HH:MM:SS` format.


#### Sleep

The `sleeps` table includes:

* `id`, which specifies the unique ID for the sleep session as an `INTEGER`. This column thus has the `PRIMARY KEY` constraint applied.
* `user_id`, which specifies the unique ID for the user who slept, as an `INTEGER`. This column thus has the `FOREIGN KEY` constraint applied, referencing the `id` column in the `users` table to ensure data integrity.
* `day_id`, which specifies the unique ID for the date in which the the sleep ceased, as an `INTEGER`. This column thus has the `FOREIGN KEY` constraint applied, referencing the `id` column in the `days` table to ensure data integrity.
* `start_time`, which specifies the time sleep started as `NUMERIC` in `YYYY-MM-DD HH:MM` format.
* `end_time`, which specifies the time sleep ended as `NUMERIC`  in `YYYY-MM-DD HH:MM` format.
* `score`, which is the sleep score of the indivudual stored as `INTEGER`, between `0` and `100`.


#### Caloric Intake

The `caloric_intakes` table includes:

* `id`, which specifies the unique ID for the meal  as an `INTEGER`. This column thus has the `PRIMARY KEY` constraint applied.
* `user_id`, which specifies the unique ID for the user who had the meal, as an `INTEGER`. This column thus has the `FOREIGN KEY` constraint applied, referencing the `id` column in the `users` table to ensure data integrity.
* `day_id`, which specifies the unique ID for the day the meal was had, as an `INTEGER`. This column thus has the `FOREIGN KEY` constraint applied, referencing the `id` column in the `days` table to ensure data integrity.
* `type`, type of the meal as `TEXT` with 5 options `('breakfast', 'lunch', 'dinner','snacks' and 'drinks')`
* `calories`, amount of calories  as an `INTEGER`.


### Relationships

As detailed by the diagram:

![ER Diagram](diagram.png)

The user experiences one or many days. The days must always have a user. The day is split into three activities; sleep, exercise and eat. It is mandatory for each of these exercises to be associated with a day, days table need not be associated with the activities. For example, an exercise must have a day it occured in, but a day could pass without an exercise. Although extremely rare, a day could pass without sleep and eating, and in more probable cimcumstances, the user might not have used his smartwatch or smartphone to record the data and have not updated the table with manual commands yet.

## Optimizations

The `date` column in `days` table is indexed to facilitate the searches in which specific dates are sought for.

A view where calories consumed grouped by days is added.

## Limitations

The overall movements of users which is not registered as an exercise (whether user is sedentary or active during the day) is not captured fully. Therefore, the total calories burned throughout the day is slightly underrepresented.


