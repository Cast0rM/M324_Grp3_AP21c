-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS bands_db;
USE bands_db;

-- Create the bands table
CREATE TABLE IF NOT EXISTS bands (
    band_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    genre VARCHAR(50) NOT NULL,
    founding_date DATE NOT NULL,
    members_count INT NOT NULL,
    disbanded_date VARCHAR(10) DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    -- CHECK (disbanded_date IS NULL OR disbanded_date > founding_date)
);


DELIMITER $$

CREATE TRIGGER before_band_insert
BEFORE INSERT ON bands
FOR EACH ROW
BEGIN
    IF NEW.disbanded_date IS NULL THEN
        SET NEW.disbanded_date = 'active';
    END IF;
END$$

DELIMITER ;

-- Insert initial data into the bands table
INSERT INTO bands (name, genre, founding_date, members_count, disbanded_date)
VALUES
('The Rolling Stones', 'Rock', '1962-01-01', 4, NULL),
('The Beatles', 'Pop', '1960-01-01', 4, '1970-04-10'),
('Led Zeppelin', 'Rock', '1968-01-01', 4, '1980-12-04'),
('Pink Floyd', 'Progressive Rock', '1965-01-01', 4, '2014-11-10'),
('Queen', 'Rock', '1970-01-01', 4, NULL),
('AC/DC', 'Hard Rock', '1973-01-01', 5, NULL),
('The Eagles', 'Rock', '1971-01-01', 5, NULL),
('Fleetwood Mac', 'Rock', '1967-01-01', 5, NULL),
('Metallica', 'Metal', '1981-01-01', 4, NULL),
('Nirvana', 'Grunge', '1987-01-01', 3, '1994-04-05'),
('Radiohead', 'Alternative Rock', '1985-01-01', 5, NULL),
('Coldplay', 'Pop Rock', '1996-01-01', 4, NULL),
('U2', 'Rock', '1976-01-01', 4, NULL),
('Green Day', 'Punk Rock', '1987-01-01', 3, NULL),
('Foo Fighters', 'Alternative Rock', '1994-01-01', 5, NULL),
('Arctic Monkeys', 'Indie Rock', '2002-01-01', 4, NULL),
('Imagine Dragons', 'Pop Rock', '2008-01-01', 4, NULL),
('The Killers', 'Alternative Rock', '2001-01-01', 4, NULL),
('Blink-182', 'Pop Punk', '1992-01-01', 3, NULL),
('The Who', 'Rock', '1964-01-01', 4, NULL);

-- Create a trigger to set disbanded_date to 'active' if it is NULL after every insert

