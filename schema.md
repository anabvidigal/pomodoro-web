CREATE TABLE USERS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT,
    HashPassword TEXT,
    CardsUnlocked INTEGER
);

CREATE TABLE STICKERS (
    StickerID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT,
    Description TEXT,
    Image BLOB
);

CREATE TABLE USER_STICKERS (
    UserID INTEGER,
    StickerID INTEGER,
    PRIMARY KEY (UserID, StickerID),
    FOREIGN KEY (UserID) REFERENCES USERS(ID),
    FOREIGN KEY (StickerID) REFERENCES STICKERS(StickerID)
);

INSERT INTO STICKERS (Title, Description, Image) VALUES
    ('Cherry Tomato', 'You sure theyre not a fruit?', '/static/01.gif'),
    ('Bloody Mary', 'This form of tomato is adult-only.', '/static/02.gif'),
    ('Bruschetta', 'Tomato finger food.', '/static/03.gif');

ALTER TABLE USER_STICKERS
ADD COLUMN Amount INTEGER;

DROP TABLE USERS;

CREATE TABLE USERS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT,
    HashPassword TEXT,
    UnopenedPacks INTEGER
);

INSERT INTO USERS (ID, UnopenedPacks)
VALUES (1, 0);

UPDATE USER_STICKERS
SET Amount = 0
WHERE UserID = 1 AND StickerID IN (1, 2, 3);

UPDATE USERS
SET UnopenedPacks = 0;