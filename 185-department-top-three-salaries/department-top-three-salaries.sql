# Write your MySQL query statement below
with cte as (select 
name, salary, departmentId,
DENSE_RANK() over (partition by departmentId order by salary desc) as ranknum
from Employee) 

select d.name as Department, cte.name as Employee , cte.salary
from cte inner join Department d on cte.departmentId =  d.id
where ranknum<4
