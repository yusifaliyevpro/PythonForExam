-- # 47. Find the N Oldest Employees. 
-- You have to get the first N employees with the oldest hire dates from the Employees table.

SET @N = The given value;
SELECT EmployeeID, EmployeeName, HireDate
FROM Employees
ORDER BY HireDate ASC
LIMIT @N;