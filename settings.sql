CREATE DATABASE comics;
CREATE USER comicsuser
WITH PASSWORD 'comics';
GRANT ALL PRIVILEGES ON DATABASE comics TO comicsuser;