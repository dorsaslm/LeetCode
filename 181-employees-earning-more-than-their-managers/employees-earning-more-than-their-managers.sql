# Write your MySQL query statement below
select name as Employee 
from Employee E1
where E1.managerid is not null and 
(select E2.salary from Employee E2 where E2.id = E1.managerId) < E1.salary