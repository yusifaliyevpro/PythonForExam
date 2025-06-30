-- # 41. Find the N Employees Who Have Been with the Company the Longest. 
-- Retrieve the first N employees who have been with the company the longest, based on HireDate.

SET @N = The given value; -- Set the number of employees to retrieve
SELECT EmployeeID, EmployeeName, HireDate
FROM Employees
ORDER BY HireDate ASC
LIMIT @N;