-- # 42. List N Products That Are Out of Stock. Retrieve the N products that are out of stock from the Products table.

SET @N = The given value; -- Set the number of products to retrieve
SELECT ProductID, ProductName, StockQuantity
FROM Products
WHERE StockQuantity = 0
LIMIT @N;