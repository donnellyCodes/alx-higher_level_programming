-- creating table that uses unique constraint
CREATE TABLE IF NOT EXISTS unique_id (
	id INTEGER DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
