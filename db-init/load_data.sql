COPY users FROM '/docker-entrypoint-initdb.d/users.csv' DELIMITER ',' CSV HEADER;
