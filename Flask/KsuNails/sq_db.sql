CREATE TABLE IF NOT EXISTS posts (
id integer PRIMARY KEY AUTOINCREMENT,
title text NOT NULL,
image BLOB,
text text NOT NULL,
time integer NOT NULL
);