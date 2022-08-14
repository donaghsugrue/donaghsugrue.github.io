-- ######### LEADERBOARD #########
-- ____________________________________________________________________________________________________________________________

DROP TABLE IF EXISTS leaderboard;

CREATE TABLE leaderboard
(
    player_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    player_name TEXT NOT NULL,
    score INTEGER NOT NULL
);

INSERT INTO leaderboard (player_name, score)
VALUES
    ("DMS",     001),
    ("ASS",     005),
    ("DJB",     010),
    ("PVM",     011),
    ("DOS",     015),
    ("JJL",     050),
    ("HEF",     051),
    ("HEF",     055),
    ("HEF",     100),
    ("DMS",     101),
    ("ASS",     105),
    ("DJB",     110),
    ("PVM",     111),
    ("DOS",     115),
    ("JJL",     150),
    ("HEF",     151),
    ("HEF",     155),
    ("HEF",     500),
    ("DMS",     501),
    ("ASS",     505),
    ("DJB",     510),
    ("PVM",     511),
    ("DOS",     515),
    ("JJL",     550),
    ("HEF",     551),
    ("HEF",     555),
    ("HEF",     999)
;

SELECT * FROM leaderboard;