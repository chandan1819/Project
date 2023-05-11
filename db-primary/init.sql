CREATE TABLE users (
    name VARCHAR(255),
    street VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    date DATE
);

COPY users FROM '/docker-entrypoint-initdb.d/users.csv' DELIMITER ',' CSV HEADER;




