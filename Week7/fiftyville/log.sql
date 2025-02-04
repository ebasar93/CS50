-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT * FROM crime_scene_reports WHERE street = 'Humphrey Street';
SELECT * FROM interviews WHERE year = 2021 AND month = 7 AND day = 28;
SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND 15 < minute < 25 AND activity = 'exit';
SELECT * FROM airports JOIN flights ON airports.id = flights.origin_airport_id  WHERE year = 2021 AND month = 7 AND day = 29  ;
SELECT full_name, city FROM airports
 WHERE id =
    (SELECT destination_airport_id FROM flights
        WHERE year = 2021 AND month = 7 AND day = 29 ORDER BY hour ASC, minute ASC LIMIT 1);
SELECT passport_number
      from people
        WHERE license_plate in(
            SELECT license_plate
            FROM bakery_security_logs
             WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND 15 < minute < 25 AND activity = 'exit');
SELECT passport_number FROM passengers WHERE flight_id =
    (SELECT id FROM flights
        WHERE year = 2021 AND month = 7 AND day = 29 ORDER BY hour ASC, minute ASC LIMIT 1)
        AND passport_number IN (SELECT passport_number
      from people
        WHERE license_plate in(
            SELECT license_plate
            FROM bakery_security_logs
             WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND 15 < minute < 25 AND activity = 'exit'));
SELECT * FROM atm_transactions WHERE atm_location = 'Leggett Street' AND year = 2021 AND month = 7 AND day = 28 AND transaction_type = 'withdraw' ;
SELECT passport_number FROM people WHERE id in(
SELECT person_id from bank_accounts
    WHERE account_number IN
    (SELECT account_number FROM atm_transactions WHERE atm_location = 'Leggett Street' AND year = 2021 AND month = 7 AND day = 28

));
SELECT name FROM people where passport_number = (
SELECT passport_number FROM passengers
 WHERE flight_id =
    (SELECT id FROM flights
        WHERE year = 2021 AND month = 7 AND day = 29 ORDER BY hour ASC, minute ASC LIMIT 1)
        AND passport_number IN (SELECT passport_number
      from people
        WHERE license_plate in(
            SELECT license_plate
            FROM bakery_security_logs
             WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute < 25 AND minute > 15 AND activity = 'exit'))
    AND passport_number IN (SELECT passport_number FROM people WHERE id in(
    SELECT person_id from bank_accounts
    WHERE account_number IN
    (SELECT account_number FROM atm_transactions WHERE atm_location = 'Leggett Street' AND year = 2021 AND month = 7 AND day = 28 AND transaction_type = 'withdraw'

    ))
    AND passport_number IN (SELECT passport_number FROM people WHERE id in
    (SELECT id FROM people WHERE phone_number IN(
    SELECT caller FROM phone_calls
    WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60)))));

SELECT id FROM people WHERE phone_number IN(
SELECT caller FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60);

SELECT name FROM people WHERE phone_number IN(
SELECT receiver FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60 AND caller = (SELECT phone_number FROM people where name = 'Bruce'));


