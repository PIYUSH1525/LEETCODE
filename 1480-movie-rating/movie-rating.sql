WITH UserRatings AS (
    SELECT u.name, COUNT(mr.movie_id) AS rating_count
    FROM MovieRating mr
    JOIN Users u ON mr.user_id = u.user_id
    GROUP BY u.name
),
MaxUser AS (
    SELECT name 
    FROM UserRatings
    WHERE rating_count = (SELECT MAX(rating_count) FROM UserRatings)
    ORDER BY name
    LIMIT 1
),
MovieAvgRatings AS (
    SELECT m.title, AVG(mr.rating) AS avg_rating
    FROM MovieRating mr
    JOIN Movies m ON mr.movie_id = m.movie_id
    WHERE mr.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY m.title
),
MaxMovie AS (
    SELECT title 
    FROM MovieAvgRatings
    WHERE avg_rating = (SELECT MAX(avg_rating) FROM MovieAvgRatings)
    ORDER BY title
    LIMIT 1
)
SELECT name AS results FROM MaxUser
UNION ALL
SELECT title FROM MaxMovie;
