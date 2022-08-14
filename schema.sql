-- .mode columns;
-- .headers on;
-- .tables;

-- SELECT * FROM *;

-- ____________________________________________________________________________________________________________________________________________________________________________________
-- ##########################################################################################
-- ######################################## GRAPHICS ########################################
-- ##########################################################################################

DROP TABLE IF EXISTS graphics;

CREATE TABLE graphics
(
    subtable TEXT NOT NULL PRIMARY KEY,
    heading TEXT NOT NULL,
    description TEXT NOT NULL
);

INSERT INTO graphics (subtable, heading, description)
VALUES
    ("garfield", "Garfield Merch",
        "For Christmas this year, I've gotten my friends 1 off t-shirts of their musical projects but with the
        name of the project done as the garfield logo. Any further explanation is to give this idea more creedance than it deserves.
        All intellectual property for Garfield belong to Viacom, and have been edited in line with fair use."),

    ("eldritch", "An Eldritch Abomination logos",
        "As a solo performer, I produce glitchy music to try and improve my production chops.
        If I am releasing something or performing, I tend to use the name An Eldritch Abomination in reference to the archetypal HP Lovecraft monster.
        Here are a variety of logos I've created myself and used as part of this project."),

    ("messyng", "Messyng FC memes",
        "<h2>Pronounced: &apos;m&epsiv;s&imath;&eng;</h2>
        It's quite easy to learn to edit digital photos when you have a driving motivating force behind you.
        In my case, my motivating force was trying to make my band mates laugh by editing our band name to look like the logos of some famous media franchises.
        I was unsuccessful in this endeavour most of the time, but it did make me quit proficient in Photoshop.
        All intellectual property rights belong to their respective owners, and have been edited in line with fair use, rights holders can be found by hovering over the photos."),

    ("teletext", "Teletext Records gig posters",
        "Throughout 2018 and 2019, myself and some friends found ourselves getting requested to organise shows more frequently so decided to include it under a promotion company banner called Teletext Records.
        We used this as an opporunity to try and expand our multimedia skillset, mainly in Photoshop by learning to create posters ourselves.
        We went with a uniform design practice for these and created a series of posters inspired by direct-to-video VHS box art design - not all were used but they can be seen here regardless.");




-- ######### ELDRITCH #########
-- ____________________________

DROP TABLE IF EXISTS eldritch;

CREATE TABLE eldritch
(
    href TEXT NOT NULL PRIMARY KEY,
    src TEXT NOT NULL,
    alt TEXT NOT NULL
);

INSERT INTO eldritch (href, src, alt)
VALUES
    -- Image when link is clicked. Hi-res.                  -- Image viewable on page. Should be lo-res.            -- Description, alternate text.
    ("content/eldritch/eldritch-1.png",                     "content/eldritch/eldritch-1.png",                      "A logo for An Eldritch Abomination using the Ghouls & Goblins font from: https://www.dafont.com/ghouls-ghosts-and-goblins.font"),
    ("content/eldritch/eldritch-2.png",                     "content/eldritch/eldritch-2.png",                      "A logo for An Eldritch Abomination using the Ghouls & Goblins font from: https://www.dafont.com/ghouls-ghosts-and-goblins.font"),
    ("content/eldritch/eldritch-3.png",                     "content/eldritch/eldritch-3.png",                      "A logo for An Eldritch Abomination using the Glacier font from Glyphworld: https://fontsinuse.com/typefaces/125401/glyphworld-glacier"),
    ("content/eldritch/eldritch-4.png",                     "content/eldritch/eldritch-4.png",                      "A logo for An Eldritch Abomination using the Pokémon Classic font from DaFont: https://www.dafont.com/pokemon-classic.font"),
    ("content/eldritch/eldritch-5.png",                     "content/eldritch/eldritch-5.png",                      "A logo for An Eldritch Abomination using the Ruritania font from DaFont: https://www.dafont.com/ruritania.font");






-- ######### GARFIELD #########
-- ____________________________

DROP TABLE IF EXISTS garfield;

CREATE TABLE graphics
(
    href TEXT NOT NULL PRIMARY KEY,
    src TEXT NOT NULL,
    alt TEXT NOT NULL
);

INSERT INTO garfield (href, src, alt)
VALUES
    -- Image when link is clicked. Hi-res.                              -- Image viewable on page. Should be lo-res.                        -- Description, alternate text.
    ("graphics/garfield/garfield_merch_aponym.png",                     "graphics/garfield/garfield_merch_aponym.png",                      "A logo for musical project Aponym done to look the Garfield logo"),
    ("graphics/garfield/garfield_merch_bokotono.png",                   "graphics/garfield/garfield_merch_bokotono.png",                    "A logo for musical project Bokotono done to look the Garfield logo"),
    ("graphics/garfield/garfield_merch_deadbog.png",                    "graphics/garfield/garfield_merch_deadbog.png",                     "A logo for musical project Deadbog done to look the Garfield logo"),
    ("graphics/garfield/garfield_merch_fomorian_vein.png",              "graphics/garfield/garfield_merch_fomorian_vein.png",               "A logo for musical project Fomorian Vein done to look the Garfield logo"),
    ("graphics/garfield/garfield_merch_jj_lee.png",                     "graphics/garfield/garfield_merch_jj_lee.png",                      "A logo for musical project JJ Lee done to look the Garfield logo"),
    ("graphics/garfield/garfield_merch_an_eldritch_abomination.png",    "graphics/garfield/garfield_merch_an_eldritch_abomination.png",     "A logo for musical project An Eldritch Abomination done to look like a bad 3D render of the Garfield logo");





-- ######### MESSYNG MEMES #########
-- ____________________________

DROP TABLE IF EXISTS messyng;

CREATE TABLE messyng
(
    href TEXT NOT NULL PRIMARY KEY,
    src TEXT NOT NULL,
    alt TEXT NOT NULL
);

INSERT INTO messyng (href, src, alt)
VALUES
    -- Image when link is clicked. Hi-res.                          -- Image viewable on page. Should be lo-res.            -- Description, alternate text.
    ("graphics/messyng_memes/messyng_saylor_moon.png",              "graphics/messyng_memes/messyng_saylor_moon.png",       "A logo for comedy band Messyng depicting the band members as Sailor Moon characters."),
    ("graphics/messyng_memes/mes_mess_and_messyng.png",             "graphics/messyng_memes/mes_mess_and_messyng.png",      "A logo for comedy band Messyng depicting the band members as Ed Edd And Eddy characters"),
    ("graphics/messyng_memes/messyng_actyon_man.png",               "graphics/messyng_memes/messyng_actyon_man.png",        "A logo for comedy band Messyng based on the Action Man logo"),
    ("graphics/messyng_memes/meanyes.png",                          "graphics/messyng_memes/meanyes.png",                   "A logo for comedy band Messyng based on the brand logo for Meanies crisps"),
    ("graphics/messyng_memes/messyng_amongys.png",                  "graphics/messyng_memes/messyng_amongys.png",           "A logo for comedy band Messyng depicting the band members as Among Us characters"),
    ("graphics/messyng_memes/messyng_call_cyrd.png",                "graphics/messyng_memes/messyng_call_cyrd.png",         "A logo for comedy band Messyng based on Eircell Call Cards"),
    ("graphics/messyng_memes/messyng_gamys_workshop.png",           "graphics/messyng_memes/messyng_gamys_workshop.png",    "A logo for comedy band Messyng based on the Games Workshop logo"),
    ("graphics/messyng_memes/messyng_maryo_3d.png",                 "graphics/messyng_memes/messyng_maryo_3d.png",          "A logo for comedy band Messyng using Super Mario as a mascot"),
    ("graphics/messyng_memes/messyng_messbusters.png",              "graphics/messyng_memes/messyng_messbusters.png",       "A logo for comedy band Messyng based on the Ghostbusters logo"),
    ("graphics/messyng_memes/messyng_mynecraft.png",                "graphics/messyng_memes/messyng_mynecraft.png",         "A logo for comedy band Messyng depicting the band members as Minecraft characters"),
    ("graphics/messyng_memes/messyng_neon_genesys.png",             "graphics/messyng_memes/messyng_neon_genesys.png",      "A logo for comedy band Messyng based on the Neon Genesis Evangelion logo"), 
    ("graphics/messyng_memes/messyng_powerpuff_gyrls.png",          "graphics/messyng_memes/messyng_powerpuff_gyrls.png",   "A logo for comedy band Messyng using The Powerpuff Girls as mascots"), 
    ("graphics/messyng_memes/messyng_seynfeld.png",                 "graphics/messyng_memes/messyng_seynfeld.png",          "A logo for comedy band Messyng based on the Seinfeld logo"),
    ("graphics/messyng_memes/messyng_sonyc.png",                    "graphics/messyng_memes/messyng_sonyc.png",             "A logo for comedy band Messyng using Sonic The Hedgehog as a mascot");



-- ######### TELETEXT #########
-- ____________________________

DROP TABLE IF EXISTS teletext;

CREATE TABLE teletext
(
    href TEXT NOT NULL PRIMARY KEY,
    src TEXT NOT NULL,
    alt TEXT NOT NULL
);

INSERT INTO teletext (href, src, alt)
VALUES
    -- Image when link is clicked. Hi-res.              -- Image viewable on page. Should be lo-res.        -- Description, alternate text.
    ("graphics/teletext/teletext-1.png",                "graphics/teletext/teletext-1.png",                 "A concert poster for Donnie Willow, A Burial At Sea, Gilbert and Aerialist live in Plugd."),
    ("graphics/teletext/teletext-2.png",                "graphics/teletext/teletext-2.png",                 "A concert poster for Aponym, Pretty Happy, and Deadbog live in The Kino."),
    ("graphics/teletext/teletext-3.png",                "graphics/teletext/teletext-3.png",                 "A concert poster for Rokaia, Ant Byrne, and Laila Jedir live in Pharmacia."),
    ("graphics/teletext/teletext-4.png",                "graphics/teletext/teletext-4.png",                 "A concert poster for Blue Whale, and The Great Balloon Race live in Plugd."),
    ("graphics/teletext/teletext-5.png",                "graphics/teletext/teletext-5.png",                 "A concert poster for Cassavettes, Elaine Malone, and Pale Rivers live in Plugd."),
    ("graphics/teletext/teletext-6.png",                "graphics/teletext/teletext-6.png",                 "A concert poster for Gilbert, and Dennis As A Landlord live in Plugd."),
    ("graphics/teletext/teletext-7.png",                "graphics/teletext/teletext-7.png",                 "A concert poster for Buí, Laurie Shaw & The Prison Wives, and Any Joy live in The Poor Relation."),
    ("graphics/teletext/teletext-8-a.png",              "graphics/teletext/teletext-8-a.png",               "A concert poster for Tribal Dance, That Snaake, and Gilbert live in Pharmacia."),
    ("graphics/teletext/teletext-8-b.png",              "graphics/teletext/teletext-8-b.png",               "A concert poster for Tribal Dance, That Snaake, and Gilbert live in The Poor Relation."),
    ("graphics/teletext/teletext-8-c.png",              "graphics/teletext/teletext-8-c.png",               "A concert poster for Tribal Dance, That Snaake, and Gilbert live in The Sin É."),
    ("graphics/teletext/teletext-8-z.png",              "graphics/teletext/teletext-8-z.png",               "A tour poster for Tribal Dance, That Snaake, and Gilbert's Irish tour."),
    ("graphics/teletext/teletext-9.png",                "graphics/teletext/teletext-9.png",                 "A concert poster for Gadget & The Cloud, Qwasi, An Eldritch Abomination, and Fomorian Vein live in The Sin É."),
    ("graphics/teletext/teletext-10.png",               "graphics/teletext/teletext-10.png",                "A concert poster for Bokotono, Cassavettes, Aponym and Selkies live in Fred Zeppelins."),
    ("graphics/teletext/teletext-11.png",               "graphics/teletext/teletext-11.png",                "A concert poster for A Burial At Sea, Gilbert, and An Eldritch Abomination live in Fred Zeppelins."),
    ("graphics/teletext/teletext-12.png",               "graphics/teletext/teletext-12.png",                "A concert poster for Van Panther, sunisadeadlylazer, and Electric Limes live in Plugd."),
    ("graphics/teletext/teletext-13.png",               "graphics/teletext/teletext-13.png",                "A concert poster for Shrug Life, Fonda and Trá Pháidín live in Plugd."),
    ("graphics/teletext/teletext-14.png",               "graphics/teletext/teletext-14.png",                "A concert poster for Surgeryhead, Lighght, Fomorian Vein, and An Eldritch Abomination live in Pharmacia."),
    ("graphics/teletext/teletext-15.png",               "graphics/teletext/teletext-15.png",                "A concert poster for His Father's Voice, Nerves, and Automatic Blue live in Plugd."),
    ("graphics/teletext/teletext-16.png",               "graphics/teletext/teletext-16.png",                "A concert poster for Cruiser, Actualacid, and Deadbog live in Plugd."),
    ("graphics/teletext/teletext-17.png",               "graphics/teletext/teletext-17.png",                "A concert poster for the Teletext Christmas party featuring Ghostking Is Dead, Bokotono, Hales Lake Hey Rusty, and Aponym live in Plugd."),
    ("graphics/teletext/teletext-18.png",               "graphics/teletext/teletext-18.png",                "A concert poster for T Boo, Julia Louise Knifefist, and Fomorian Vein live in Plugd."),
    ("graphics/teletext/teletext-19.png",               "graphics/teletext/teletext-19.png",                "A concert poster for the cancelled Junk Drawer, Robocobra Quartet, Olivia Furey, and Icebear show in Plugd.");










-- ____________________________________________________________________________________________________________________________________________________________________________________
-- ##########################################################################################
-- ######################################## WEBSITES ########################################
-- ##########################################################################################

-- DROP TABLE IF EXISTS websites;

-- CREATE TABLE websites
-- (
--     url TEXT NOT NULL PRIMARY KEY,
--     title TEXT NOT NULL,
--     thumbnail TEXT NOT NULL,
--     alt INTEGER NOT NULL
-- );

-- INSERT INTO websites (url, title, thumbnail, alt)
-- VALUES
--     (__,    "Messyng FC fan club",     __,     __),
--     (__,    "Teletext Records directory",     __,     __),
--     (__,    "Phoebe McDonogh artist portfolio",     __,     __),
--     (__,    "Law Society of Leiden website",     __,     __),
--     (__,    "The Depths, bespoke multimedia hosting site",     __,     __),
--     (__,    "Toilet Paper reviews",     __,     __),











-- ____________________________________________________________________________________________________________________________________________________________________________________
-- #########################################################################################
-- ######################################### GAMES #########################################
-- #########################################################################################

DROP TABLE IF EXISTS graphics;

CREATE TABLE graphics
(
    subtable TEXT NOT NULL PRIMARY KEY,
    heading TEXT NOT NULL,
    description TEXT NOT NULL
);

INSERT INTO graphics (subtable, heading, description)
VALUES
    ("snake",       "Snake",                    "",
        "For Christmas this year, I've gotten my friends 1 off t-shirts of their musical projects but with the
        name of the project done as the garfield logo. Any further explanation is to give this idea more creedance than it deserves.
        All intellectual property for Garfield belong to Viacom, and have been edited in line with fair use."),

    ("cordle",      "CORDLE",                   "",
        "As a solo performer, I produce glitchy music to try and improve my production chops.
        If I am releasing something or performing, I tend to use the name An Eldritch Abomination in reference to the archetypal HP Lovecraft monster.
        Here are a variety of logos I've created myself and used as part of this project."),

    ("dungeon",     "Dungeon Crawler 2000",     "",
        "You are a knight tasked with finding the treasure at the top of a castle.
        Inside the castle there are ghouls. If they see you, they will be hell bent on destroying you.
        Use either <i>W, A, S, D</i> or <i>arrow up, arrow left, arrow down, arrow right</i> to navigate yourself.
        Hold <i>E</i> and collide with an enemy to attack it.
        Hold <i>E</i> and collide with a treasure chest to get one of a few different items.
        Room by room you have to make it past all of the enemies that are moving toward you.
        Your score is based on how many rooms your traverse, how many enemies you kill, how much treasure you find, and how long it takes you to reach the top of the castle.
        If the game is too tricky, try this cheat code: <i>iwantnobaddies</i>
        Good luck!"),

    ("bureaucracy", "Bureaucracy Simulator",   "",
        "You have five 8-hour days to get your stupid manager to sign a stupid report and deliver it to the stupid accounting department. 
        Should be really straightforward, but you are seemingly employed ___. 
        You need to avoid your co-workers who have pointless busy-work for you to do, 
        Use either <i>W, A, S, D</i> or <i>arrow up, arrow left, arrow down, arrow right</i> to navigate yourself.
        Press <i>E</i> to interact with objects around the office.");




-- DROP TABLE IF EXISTS leaderboard;

-- CREATE TABLE leaderboard
-- (
--     player_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     player_name TEXT NOT NULL,
--     score INTEGER NOT NULL
-- );

-- INSERT INTO leaderboard (player_name, score)
-- VALUES
--     ("DMS",     001),
--     ("ASS",     005),
--     ("DJB",     010),
--     ("PVM",     011),
--     ("DOS",     015),
--     ("JJL",     050),
--     ("HEF",     051),
--     ("HEF",     055),
--     ("HEF",     100),
--     ("DMS",     101),
--     ("ASS",     105),
--     ("DJB",     110),
--     ("PVM",     111),
--     ("DOS",     115),
--     ("JJL",     150),
--     ("HEF",     151),
--     ("HEF",     155),
--     ("HEF",     500),
--     ("DMS",     501),
--     ("ASS",     505),
--     ("DJB",     510),
--     ("PVM",     511),
--     ("DOS",     515),
--     ("JJL",     550),
--     ("HEF",     551),
--     ("HEF",     555),
--     ("HEF",     999)
-- ;