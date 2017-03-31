-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE TABLE players ( player_id SERIAL,
                       name TEXT,
                       PRIMARY KEY (player_id));

CREATE TABLE scoreboard ( match_id SERIAL,
                          player TEXT,
                          winner INTEGER,
                          loser INTEGER,
                          score INTEGER,
                          matches INTEGER,
                          PRIMARY KEY (match_id));



