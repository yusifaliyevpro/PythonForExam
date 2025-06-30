-- # 48. Calculate the Average of the First N Salaries. 
-- You have to calculate the average salary of the first N employees from the Employees table.

SET @N = The given value;
SELECT AVG(Salary) AS AvgSalary
FROM (
    SELECT Salary
    FROM Employees
    ORDER BY EmployeeID
    LIMIT @N
) AS FirstNSalaries;