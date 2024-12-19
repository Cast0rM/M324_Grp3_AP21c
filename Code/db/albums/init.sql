CREATE DATABASE IF NOT EXISTS albums_db;
USE albums_db;

CREATE TABLE albums (
    album_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    release_date DATE NOT NULL,
    band_id INT NOT NULL,
    label VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO albums (title, release_date, band_id, label, price)
VALUES
('Sticky Fingers', '1971-04-23', 1, 'Rolling Stones Records', 10.99),
('Abbey Road', '1969-09-26', 2, 'Apple Records', 11.99),
('Led Zeppelin IV', '1971-11-08', 3, 'Atlantic Records', 12.99),
('The Dark Side of the Moon', '1973-03-01', 4, 'Harvest Records', 13.99),
('A Night at the Opera', '1975-11-21', 5, 'EMI', 12.49),
('Back in Black', '1980-07-25', 6, 'Albert/Atlantic', 14.99),
('Hotel California', '1976-12-08', 7, 'Asylum Records', 13.49),
('Rumours', '1977-02-04', 8, 'Warner Bros.', 11.99),
('Master of Puppets', '1986-03-03', 9, 'Elektra Records', 13.99),
('Nevermind', '1991-09-24', 10, 'DGC Records', 10.49),
('OK Computer', '1997-05-21', 11, 'Parlophone', 14.49),
('Parachutes', '2000-07-10', 12, 'Parlophone', 10.99),
('The Joshua Tree', '1987-03-09', 13, 'Island Records', 12.99),
('American Idiot', '2004-09-21', 14, 'Reprise Records', 13.49),
('The Colour and the Shape', '1997-05-20', 15, 'Roswell/Capitol', 12.99),
('AM', '2013-09-09', 16, 'Domino Records', 11.49),
('Night Visions', '2012-09-04', 17, 'Interscope Records', 10.99),
('Hot Fuss', '2004-06-07', 18, 'Island Records', 12.49),
('Enema of the State', '1999-06-01', 19, 'MCA Records', 9.99),
('Who''s Next', '1971-08-14', 20, 'Decca Records', 13.99);