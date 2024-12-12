CREATE DATABASE IF NOT EXISTS bands_db;
USE bands_db;

CREATE TABLE bands (
    band_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    genre VARCHAR(50) NOT NULL,
    founding_date DATE NOT NULL,
    members_count INT NOT NULL,
    disbanded_date DATE DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (disbanded_date IS NULL OR disbanded_date > founding_date)
);