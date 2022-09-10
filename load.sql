SELECT
    s.id,
    s.userId,
    s.selected_tick,
    s.step_count,
    t.tick
FROM Session s
JOIN Session_Ticks t
    ON s.id = t.sessionId
GROUP BY s.id


CREATE TABLE `User` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `first_name`    TEXT NOT NULL,
    `last_name`    TEXT NOT NULL,
    `email`    TEXT NOT NULL,
    `address`    TEXT NOT NULL,
    `profile_image` TEXT NOT NULL
);


CREATE TABLE `Session` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `userId`    INTEGER NOT NULL,
    `selected_tick`     INTEGER NOT NULL,
    `step_count`   INTEGER
);

CREATE TABLE `Session_Ticks` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `sessionId`     INTEGER NOT NULL,
    `tick`      DECIMAL NOT NULL
);

CREATE TABLE `User_Session` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `userId`     INTEGER NOT NULL,
    `sessionId`      INTEGAR NOT NULL
);

INSERT INTO `User` VALUES (null, "Test", "Test", "test@test.com", "123Test", "TestImageURL");

INSERT INTO `Session_Ticks` VALUES (null, 3448, -96.33); 
INSERT INTO `Session_Ticks` VALUES (null, 3448, -96.33); 
INSERT INTO `Session_Ticks` VALUES (null, 3448, -93.47); 
INSERT INTO `Session_Ticks` VALUES (null, 3448, -89.03999999999999); 
INSERT INTO `Session_Ticks` VALUES (null, 3448, -84.61); 
INSERT INTO `Session_Ticks` VALUES (null, 3448, -80.18); 
INSERT INTO `Session_Ticks` VALUES (null, 3448, -75.75); 
INSERT INTO `Session_Ticks` VALUES (null, 3448, -71.32); 
INSERT INTO `Session_Ticks` VALUES (null, 3448, -66.89); 
INSERT INTO `Session_Ticks` VALUES (null, 3448, -62.46); 
INSERT INTO `Session_Ticks` VALUES (null, 3448, -58.03); 
INSERT INTO `Session_Ticks` VALUES (null, 3448, -53.6); 
INSERT INTO `Session_Ticks` VALUES (null, 3448, -49.17); 
INSERT INTO `Session_Ticks` VALUES (null, 3448, -44.74); 
INSERT INTO `Session_Ticks` VALUES (null, 3448, -40.31); 

INSERT INTO `Session` VALUES (3448, 1, 5, 1); 

INSERT INTO `User_Session` VALUES (1, 1, 3448); 