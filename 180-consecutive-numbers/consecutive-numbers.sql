# Write your MySQL query statement below
select distinct num as ConsecutiveNums from
(select num,
LAG(num) over (order by id) as prev,
Lead(num) over (order by id) as next
from logs) as a
where num = prev and num = next