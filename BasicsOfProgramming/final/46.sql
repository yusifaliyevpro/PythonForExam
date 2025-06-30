-- # 46. List N Employees with the Most Hours Worked. 
-- Retrieve the N employees with the most hours worked from the EmployeeHours table.

SET @N = The given value;
SELECT EmployeeID, SUM(HoursWorked) AS TotalHours
FROM EmployeeHours
GROUP BY EmployeeID
ORDER BY TotalHours DESC
LIMIT @N;