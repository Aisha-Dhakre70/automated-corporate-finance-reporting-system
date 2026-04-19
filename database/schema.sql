CREATE DATABASE IF NOT EXISTS finance_db;

USE finance_db;

CREATE TABLE financial_data (
    id INT AUTO_INCREMENT PRIMARY KEY,

    company VARCHAR(100),
    date DATE,

    revenue DOUBLE,
    expense DOUBLE,
    cogs DOUBLE,

    gross_profit DOUBLE,
    operating_profit DOUBLE,
    net_profit DOUBLE,

    category VARCHAR(50),
    region VARCHAR(50)
);
