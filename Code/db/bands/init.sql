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