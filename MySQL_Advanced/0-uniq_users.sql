-- script that creates a table users
CREATE TABLE users IF NOT EXISTS (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY(id),
    email CHAR(255) NOT NULL UNIQUE,
    name CHAR(255)
    ;)
