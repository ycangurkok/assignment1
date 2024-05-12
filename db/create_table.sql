-- create_table.sql
CREATE TABLE IF NOT EXISTS Name (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL
);