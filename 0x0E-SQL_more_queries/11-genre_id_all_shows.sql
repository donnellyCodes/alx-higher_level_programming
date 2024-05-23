-- listing all shows contained in htbn_0d_tvshows database
-- if show does not have a genre display null
SELECT s.title, g.genre_id
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS g
ON s.id = g.show_id
ORDER BY s.title, g.genre_id;
