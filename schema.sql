CREATE DATABASE IF NOT EXISTS finance_db;

USE finance_db;

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    revenue FLOAT,
    expense FLOAT,
    category VARCHAR(50),
    region VARCHAR(50)
);