DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Order_items;

CREATE TABLE Customer(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE Orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    purchase_date TEXT NOT NULL,
    country TEXT NOT NULL,
    device TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customer (id)
);

CREATE TABLE Order_items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    EAN INTEGER NOT NULL,
    quantity integer NOT NULL,
    price REAL NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Customer (id)
);
/*Dummy data*/
INSERT INTO Customer(first_name, last_name, email) VALUES('Laura', 'Palmer', 'Lpalmer@iot.com');
INSERT INTO Customer(first_name, last_name, email) VALUES('Henry','Prince-consort','almosstking@ddk.dk');

INSERT INTO Orders(customer_id, purchase_date, country, device) VALUES (1, '24-05-19', 'SWE','Mobile');
INSERT INTO Orders(customer_id, purchase_date, country, device) VALUES (2, '10-06-19', 'DEN','PC');
INSERT INTO Orders(customer_id, purchase_date, country, device) VALUES (2, '14-06-19', 'DEN','PC');

INSERT INTO Order_items(order_id, EAN, quantity, price) VALUES (1, '2310', '1','299');
INSERT INTO Order_items(order_id, EAN, quantity, price) VALUES (1, '2320', '1','149');

INSERT INTO Order_items(order_id, EAN, quantity, price) VALUES (2, '4023', '1','799');

INSERT INTO Order_items(order_id, EAN, quantity, price) VALUES (3, '3390', '1','549');
INSERT INTO Order_items(order_id, EAN, quantity, price) VALUES (3, '1054', '1','99');

