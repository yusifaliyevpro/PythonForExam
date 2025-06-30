-- # 44. Get the N Highest Salaries. Retrieve the N employees with the highest salaries from the Employees table.

SET @N = The given value;
SELECT EmployeeID, EmployeeName, Salary
FROM Employees
ORDER BY Salary DESC
LIMIT @N;