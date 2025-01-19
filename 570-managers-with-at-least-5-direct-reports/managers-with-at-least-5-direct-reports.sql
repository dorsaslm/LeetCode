# Write your MySQL query statement below
select name from Employee
where id in ( 
    select managerId from employee
    where managerId is not Null
    group by managerId
    having count(managerId) > 4)
