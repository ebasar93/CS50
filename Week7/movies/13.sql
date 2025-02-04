SELECT name FROM people JOIN stars on people.id = stars.person_id JOIN movies on stars.movie_id = movies.id WHERE title in(

SELECT title FROM people, stars, movies, ratings
WHERE people.id = stars.person_id
AND stars.movie_id = movies.id
AND name = 'Kevin Bacon' and birth = 1958) and name != 'Kevin Bacon' ;