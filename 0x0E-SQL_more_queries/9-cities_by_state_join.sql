-- listing all cities in hbtn_0d_usa database
-- results is sorted in ascending order
SELECT c.id, c.name, s.name
FROM cities AS c
INNER JOIN states AS s
ON c.state_id = s.id
ORDER BY c.id;
