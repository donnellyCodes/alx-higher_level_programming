-- listing all cities in hbtn_0d_usa database
-- results is sorted in ascending order
SELECT cities.id, cities.name, states.name
FROM cities AS cities
INNER JOIN states AS states
ON cities.id = states.id
ORDER BY cities.id;
