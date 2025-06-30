-- # 45. Get the N Smallest Prices. Get the N smallest prices from the Products table.

SET @N = The given value;
SELECT ProductID, ProductName, Price
FROM Products
ORDER BY Price ASC
LIMIT @N;