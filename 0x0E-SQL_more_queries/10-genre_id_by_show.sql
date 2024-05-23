-- listing all shows in hbtn_0d_tvshows with atleast on genre
SELECT s.title, g.genre_id
FROM tv_shows AS s
INNER JOIN tv_shows_genres AS g
ON s.id = g.show_id
ORDER BY s.title, g.genre_id ASC;
