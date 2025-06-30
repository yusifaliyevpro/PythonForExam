-- # 49. Find the N Customers Who Have Spent the Most. 
-- You have to find the top N customers who have spent the most on products. 
-- Assume there is a Sales table with CustomerID and Amount.

SET @N = The given value;
SELECT CustomerID, SUM(Amount) AS TotalSpent
FROM Sales
GROUP BY CustomerID
ORDER BY TotalSpent DESC
LIMIT @N;