-- listing all cities in california
-- results are sorted in ascending order
SELECT id, name
FROM cities
WHERE state_id IN
(SELECT id
	FROM states
	WHERE name = "California")
ORDER BY id;
