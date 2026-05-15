
CREATE TABLE stores (
    store_id INT PRIMARY KEY,
    store_name VARCHAR(100),
    region VARCHAR(50)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2)
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    store_id INT,
    manager_id INT
);

CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    store_id INT,
    product_id INT,
    quantity INT,
    sale_date DATE,
    revenue DECIMAL(10,2)
);


INSERT INTO products VALUES (1,'Laptop','Electronics',50000);


SELECT * FROM products;



UPDATE products
SET price = 52000
WHERE product_id = 1;



DELETE FROM products
WHERE product_id = 1;


CREATE PROCEDURE daily_sales(IN sid INT)
BEGIN
   SELECT store_id,
          sale_date,
          SUM(revenue) AS total_sales
   FROM sales
   WHERE store_id = sid
   GROUP BY sale_date;
END //

DELIMITER ;



CALL daily_sales(1);