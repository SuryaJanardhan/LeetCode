# Write your MySQL query statement below

SELECT 
SAMBAR.Department as Department , SAMBAR.name as Employee , SAMBAR.Salary
FROM

(SELECT E.id, E.name, E.salary,E.departmentId, D.name as Department from Employee as E join Department as D where D.id = E.departmentId) as SAMBAR

WHERE salary = (
    SELECT MAX(salary)
    FROM Employee
    WHERE departmentId = SAMBAR.departmentId
)
;