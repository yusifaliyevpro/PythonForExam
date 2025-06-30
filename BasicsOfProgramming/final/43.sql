-- # 43. Calculate the Total Price of the First N Products. 
-- Calculate the total price of the first N products from the Products table.

SET @N = The given value;
SELECT SUM(Price) AS TotalPrice
FROM (
    SELECT Price
    FROM Products
    LIMIT @N
) AS TopNProducts;