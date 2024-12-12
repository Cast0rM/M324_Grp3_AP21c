CREATE DATABASE IF NOT EXISTS albums_db;
USE albums_db;

-- Add table creation scripts here

CREATE TABLE albums (
    album_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    release_date DATE NOT NULL,
    band_name VARCHAR(100) NOT NULL,
    label VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);