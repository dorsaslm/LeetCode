# Write your MySQL query statement below
with cte as(
select delivery_id, customer_id, order_date, customer_pref_delivery_date,
row_number() over (partition by customer_id order by order_date) as rownum
from Delivery)
select round(100 *(count(*)/(select count(*) from cte where rownum = 1)) ,2)  as immediate_percentage
from cte where cte.order_date = cte.customer_pref_delivery_date
and rownum = 1



