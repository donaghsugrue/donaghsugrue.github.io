-- ######### ARTIST SPECIFIC TABLES #########
-- ____________________________________________________________________________________________________________________________
-- We want to create a table with all of the artist accounts that we have.
-- We will fetch their releases through relations, so we won't include that here.
-- We want to store the artist_name, a user_id, their password as a generated hash, and the url of their profile picture.

DROP TABLE IF EXISTS artists;

CREATE TABLE artists
(
    user_id TEXT PRIMARY KEY,
    artist_name TEXT NOT NULL,
    password TEXT NOT NULL
    -- pfp TEXT NOT NULL <---- I want to hang onto this cause I want every account to have a profile picture. Will revisit.
);

-- We don't want to use an "INSERT INTO" query here for any artists accounts we want to use, because we want the password hash function to store passwords, but I need some of the user_id's for demonstrative purposes.
INSERT INTO artists (user_id, artist_name, password)
VALUES
    ("aponymband",              "Aponym",                   "tonywilson1994"),
    ("FomorianVeinHardcore",    "Fomorian Vein",            "fomorian_vein_jpg"),
    ("DeadbogNKY",              "Deadbog",                  "CD"),
    ("aneldritchabomination",   "An Eldritch Abomination",  "eLdRiTcH"),
    ("bokotono",                "BOKOTONO",                 "bokomayo4sam"),
    ("artisalie",               "Aerialist",                "arealistartisalie"),
    ("jjlee",                   "JJ Lee",                   "jjnkyjj")

;

SELECT * FROM artists;



-- ____________________________________________________________________________________________________________________________
-- We'll store all of the releases that are listed on the site in the inventory table.
-- a page showing the full range of an artists stock wioll call that from here via relation through the Artist Name.
-- We will have a per release genre, rather than a per artist genre to help with our recommendation algorithm.
-- There might be multiple format releases of the same project, so we will use an autoincremenet code as the primary key.

DROP TABLE IF EXISTS inventory;

CREATE TABLE inventory
(
    code INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    artist TEXT NOT NULL,
    format TEXT NOT NULL,
    price FLOAT NOT NULL,
    stock INT NOT NULL,
    genre TEXT NOT NULL,
    artwork TEXT NOT NULL
);

INSERT INTO inventory (title, artist, format, price, stock, genre, artwork)
VALUES
    ("Deus Incognitus", "Aponym",                   "Tape", 5.00,   10, "prog",             "aponym_deus_incognitus_tape.jpg"),
    ("Ingress",         "Aponym",                   "CD",   5.00,   30, "prog",             "aponym_ingress_cd.jpg"),
    ("Look At The Rain And Spit At It", "Fomorian Vein", "Tape", 5.00, 15, "digital hardcore", "fomorian_vein_lookattherainandspitatit_tape.jpg"),
    ("Deadbog",         "Deadbog",                  "CD",   8.00,   15, "shoegaze",         "deadbog_deadbog_cd.jpg"),
    ("hakmuziek",       "An Eldritch Abomination",  "Other",7.00,  100,"digital hardcore", "an_eldritch_abomination_hakmuziek_other.jpg"),
    ("hakmuziek",       "An Eldritch Abomination",  "Tape", 8.50,   25, "digital hardcore", "an_eldritch_abomination_hakmuziek_tape.jpg"),
    ("S/T",             "BOKOTONO",                 "USB",  10.00,  30, "prog",             "bokotono_st_usb.jpg"),
    ("_",               "Aerialist",                "Vinyl",21.00,  10, "shoegaze",         "aerialist___vinyl.jpg"),
    ("weak 4 u",        "JJ Lee",                   "USB",  1.00,   70, "hip-hop",          "jj_lee_weak_4_u_usb.jpg")
;


SELECT * FROM inventory;




-- ######### FAN SPECIFIC TABLES #########
-- ____________________________________________________________________________________________________________________________

DROP TABLE IF EXISTS fans;

CREATE TABLE fans
(
    user_id TEXT PRIMARY KEY,
    password TEXT NOT NULL
    -- pfp TEXT NOT NULL <---- I want to hang onto this cause I want every account to have a profile picture. Will revisit.

);

-- We don't want to use an "INSERT INTO" query here, because we want the password hash function to store passwords.

SELECT * FROM fans;


-- ____________________________________________________________________________________________________________________________
-- This is a table showing everything that has been purchased by a signed in Fan.
-- Upon purchase, the user_id and code are added to this table to show the link between the two.
-- We'll also call all of the codes that have a specific user_id in a function to collate all purchased releases into one "collections" page per fan.

DROP TABLE IF EXISTS collections;

CREATE TABLE collections
(
    user_id TEXT NOT NULL,
    code INT NOT NULL
);

INSERT INTO collections (user_id, code)
VALUES
    ("donaghsugrue", 4),
    ("donaghsugrue", 3),
    ("DerekBridge", 1),
    ("DerekBridge", 3),
    ("DerekBridge", 5),
    ("DerekBridge", 7)
;

SELECT * FROM collections;






-- ######### GENERIC SITE WIDE TABLES #########
-- ____________________________________________________________________________________________________________________________
-- This is a table showing messages sent via the contact form. This is a really clunky approach, but it works for now.

DROP TABLE IF EXISTS messages;

CREATE TABLE messages
(
    msg_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    subject TEXT NOT NULL,
    email TEXT NOT NULL,
    message TEXT NOT NULL
);

SELECT * FROM messages;