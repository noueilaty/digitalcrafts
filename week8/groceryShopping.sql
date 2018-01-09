-- To Run:  \i filename
\connect hassannoueilaty;
DROP DATABASE groceryShoppingDb;
CREATE DATABASE groceryShoppingDb;
\connect groceryshoppingdb;


CREATE TABLE shopping_lists(
  id SERIAL NOT NULL UNIQUE PRIMARY KEY,
  store VARCHAR(50) NOT NULL
);

CREATE TABLE grocery_items(
  id SERIAL NOT NULL UNIQUE PRIMARY KEY,
  name VARCHAR(50),
  shopping_list_id INTEGER REFERENCES shopping_lists(id),
  quantity INTEGER DEFAULT 0,
  price NUMERIC(1000, 2)
);

INSERT INTO shopping_lists (store)
VALUES ('Sprouts');

INSERT INTO shopping_lists (store)
VALUES ('Kroger');

INSERT INTO shopping_lists (store)
VALUES ('Costco');

INSERT INTO grocery_items (shopping_list_id, name, quantity, price) VALUES
  (1, 'Sugar', 1, 2.39),
  (1, 'Vanilla Extract', 1, 5.89),
  (1, 'Organic Whole Milk', 1, 4.69),
  (1, 'Raw Honey', 1, 6.89),
  (1, 'Pasture Raised Eggs', 1, 5.89),
  (2, 'Sour Cream', 1, 3.99),
  (2, 'Cilantro', 2, 0.89),
  (2, 'Jalapenos', 2, 0.79),
  (2, 'Red Onion', 3, 1.69),
  (2, 'Turnip', 1, 1.79),
  (3, 'Avocados', 6, 4.49),
  (3, 'Skirt Steak', 3, 17.97),
  (3, 'Frozen Veggies', 1, 7.39),
  (3, 'Sliced Bread', 2, 6.99),
  (3, 'Frozen Fish', 1, 16.99);

-- Requirements:

-- write a query to return shopping lists:
SELECT * FROM shopping_lists;

-- write a query to return all grocery items:
SELECT * FROM grocery_items;

-- write a query to return all grocery items where the price is greater than $10 (make sure to insert few grocery items with price > $10):
SELECT * FROM grocery_items
WHERE price>10.00;

-- write a query which returns the grocery item with maximum price:
SELECT MAX(price) AS maximum_price
FROM grocery_items;

-- write a query which returns the grocery item with minimum price:
SELECT MIN(price) AS minimum_price
FROM grocery_items;

-- write a query which returns the total sum of all the grocery items:
SELECT SUM(price)
FROM grocery_items;

-- write a query which returns the shopping list rows and grocery items of a particular shopping list:
SELECT *
FROM grocery_items
WHERE shopping_list_id=2;

-- write a query which returns the count of total grocery items in each shopping list:
SELECT SUM(quantity)
FROM grocery_items
WHERE shopping_list_id=1;

SELECT SUM(quantity)
FROM grocery_items
WHERE shopping_list_id=2;

SELECT SUM(quantity)
FROM grocery_items
WHERE shopping_list_id=3;

-- write a query which returns the sum of total grocery items in each shopping list:
SELECT SUM(price)
FROM grocery_items
WHERE shopping_list_id=1;

SELECT SUM(price)
FROM grocery_items
WHERE shopping_list_id=2;

SELECT SUM(price)
FROM grocery_items
WHERE shopping_list_id=3;

-- insert a duplicate grocery item (same name) into the grocery items table. Now, write a query which filters the duplicate item:
INSERT INTO grocery_items (name, shopping_list_id, quantity, price)
VALUES ('Sour Cream', 2, 1, 3.99);

SELECT DISTINCT name
FROM grocery_items;

-- insert grocery items with price $10. insert grocery items with price $20. Now write a query which returns all the grocery items with price between $10 and $15 dollars:

SELECT * FROM grocery_items
WHERE price >= 15 AND price <= 20
