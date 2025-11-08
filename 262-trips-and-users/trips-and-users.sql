# Write your MySQL query statement below
with validTrips as (
    select t.*
    from trips t
    JOIN Users c ON t.client_id = c.users_id AND c.banned = 'No' and c.role = 'client'
    JOIN Users d ON t.driver_id = d.users_id AND d.banned = 'No' and d.role = 'driver'
    and request_at between "2013-10-01" and "2013-10-03"
)


select request_at as Day,
round(sum(case when status <> 'completed' then 1 else 0 end) / count(*),2) as 'Cancellation Rate'
from validTrips
group by request_at
order by request_at asc