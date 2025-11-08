# Write your MySQL query statement below
/*select score,
(@rank := @rank + (@prev <> (@prev := score))) as `rank`
from 
Scores,
(select @rank := 0, @prev := -1) as a
order by score desc*/

select score , 
dense_rank() over(order by score desc) as "rank" 
from Scores 