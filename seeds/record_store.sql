
DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;

CREATE SEQUENCE IF NOT EXISTS albums_id_se;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title text,
    release_year int,
    artist_id int
);

INSERT INTO albums (title, release_year, artist_id) VALUES ('Californication',1999, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Nevermind', 1991, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('In Utero', 1993, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Ten', 1991, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('By the Way', 2002, 1);