CREATE DATABASE IF NOT EXISTS test_db;
USE test_db;

CREATE TABLE IF NOT EXISTS messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message VARCHAR(255) NOT NULL
);

INSERT INTO messages (message) VALUES ('Hello, World from CodeFrontier!');
