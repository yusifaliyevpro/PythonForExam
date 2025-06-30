-- # 50. Delete the N Oldest Products. You need to delete the first N products that were added the earliest 
-- in the Products table, based on their ProductID.

SET @N = The given value;
DELETE FROM Products
WHERE ProductID IN (
    SELECT ProductID
    FROM Products
    ORDER BY ProductID ASC
    LIMIT @N
);