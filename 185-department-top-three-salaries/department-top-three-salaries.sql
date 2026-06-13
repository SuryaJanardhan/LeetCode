# Write your MySQL query statement below
select 
    Department,
    name AS Employee,
    salary AS Salary
    
    from 
(
select  E.id AS emp_id,
    E.name,
    E.salary,
    E.departmentId,
    D.id AS deptid,
    DENSE_RANK() OVER (
            PARTITION BY e.departmentId
            ORDER BY e.salary DESC
        ) AS ranky,

    D.name AS Department
    from 
        Employee as E join Department  as D on E.departmentId = D.id
) as Sambar

where ranky <= 3
;

