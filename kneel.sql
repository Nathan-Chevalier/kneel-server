CREATE TABLE 'Metals'
(
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'metal' NVARCHAR(160) NOT NULL,
    'price' NUMERIC(5,2) NOT NULL
);

CREATE TABLE 'Sizes'
(
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'carats' NUMERIC(3,2) NOT NULL,
    'price' NUMERIC(5,2) NOT NULL
);

CREATE TABLE 'Styles'
(
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'style' VARCHAR(160) NOT NULL,
    'price' NUMERIC(5,2) NOT NULL
);

CREATE TABLE 'Orders'
(
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'styleId' INTEGER NOT NULL,
    'sizeId' INTEGER NOT NULL,
    'metalId' INTEGER NOT NULL,

    FOREIGN KEY (metalId) REFERENCES Metals (id),
    FOREIGN KEY (styleId) REFERENCES Styles (id),
    FOREIGN KEY (sizeId) REFERENCES Sizes (id)
);

-- INSERT statements for the 'Metals' table
INSERT INTO Metals ('metal', 'price') VALUES ('Gold', 39.99);
INSERT INTO Metals ('metal', 'price') VALUES ('Silver', 19.99);
INSERT INTO Metals ('metal', 'price') VALUES ('Platinum', 79.99);
INSERT INTO Metals ('metal', 'price') VALUES ('Titanium', 29.99);
INSERT INTO Metals ('metal', 'price') VALUES ('Copper', 9.99);

-- INSERT statements for the 'Sizes' table
INSERT INTO Sizes ('carats', 'price') VALUES (1.50, 199.99);
INSERT INTO Sizes ('carats', 'price') VALUES (2.00, 249.99);
INSERT INTO Sizes ('carats', 'price') VALUES (0.75, 129.99);
INSERT INTO Sizes ('carats', 'price') VALUES (3.00, 349.99);
INSERT INTO Sizes ('carats', 'price') VALUES (1.25, 169.99);

-- INSERT statements for the 'Styles' table
INSERT INTO Styles ('style', 'price') VALUES ('Classic', 49.99);
INSERT INTO Styles ('style', 'price') VALUES ('Modern', 59.99);
INSERT INTO Styles ('style', 'price') VALUES ('Vintage', 54.99);
INSERT INTO Styles ('style', 'price') VALUES ('Art Deco', 64.99);
INSERT INTO Styles ('style', 'price') VALUES ('Minimalist', 44.99);

-- INSERT statements to populate the 'orders' table
INSERT INTO Orders ('styleId', 'sizeId', 'metalId') VALUES (3, 4, 2);
INSERT INTO Orders ('styleId', 'sizeId', 'metalId') VALUES (1, 2, 5);
INSERT INTO Orders ('styleId', 'sizeId', 'metalId') VALUES (2, 3, 1);
INSERT INTO Orders ('styleId', 'sizeId', 'metalId') VALUES (4, 5, 3);
INSERT INTO Orders ('styleId', 'sizeId', 'metalId') VALUES (5, 1, 4);

SELECT
o.id,
o.styleId,
o.metalId,
o.sizeId,
Styles.id AS style_id,
Styles.style AS style,
Styles.price AS style_price,
Metals.id AS metal_id,
Metals.metal AS metal,
Metals.price AS metal_price,
Sizes.id AS size_id,
Sizes.carats AS carats,
Sizes.price AS size_price
FROM Orders o
LEFT JOIN Styles ON o.styleId = Styles.id
LEFT JOIN Metals ON o.metalId = Metals.id
LEFT JOIN Sizes ON o.sizeId = Sizes.id
GROUP BY o.id;