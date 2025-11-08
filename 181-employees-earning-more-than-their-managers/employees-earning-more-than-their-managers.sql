# Write your MySQL query statement below
/*select name as Employee 
from Employee E1
where E1.managerid is not null and 
(select E2.salary from Employee E2 where E2.id = E1.managerId) < E1.salary*/


select E1.name as Employee
from Employee E1
inner join Employee E2
on E1.managerid = E2.id
where E1.salary > E2.salary